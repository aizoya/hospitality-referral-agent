from types import SimpleNamespace

import scripts.live_validation as live_validation


def test_run_step_returns_subprocess_code(monkeypatch):
    def fake_run(command, check=False):
        assert command == ["python", "-V"]
        assert check is False
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(live_validation.subprocess, "run", fake_run)
    assert live_validation.run_step("version", ["python", "-V"]) == 0


def test_main_blocks_before_demo_when_preflight_fails(monkeypatch):
    calls = []

    def fake_run_step(label, command):
        calls.append((label, command))
        return 1

    monkeypatch.setattr(live_validation, "run_step", fake_run_step)
    monkeypatch.setattr(live_validation.sys, "argv", ["live_validation", "--region", "us-west-2"])

    assert live_validation.main() == 1
    assert len(calls) == 1
    assert calls[0][0] == "AWS / Bedrock preflight"
    assert "scripts.aws_preflight" in calls[0][1]


def test_main_runs_demo_after_successful_preflight(monkeypatch):
    calls = []

    def fake_run_step(label, command):
        calls.append((label, command))
        return 0

    monkeypatch.setattr(live_validation, "run_step", fake_run_step)
    monkeypatch.setattr(
        live_validation.sys,
        "argv",
        ["live_validation", "--region", "us-west-2", "--model", "example-model"],
    )

    assert live_validation.main() == 0
    assert [label for label, _ in calls] == [
        "AWS / Bedrock preflight",
        "Live Strands demo",
    ]
    assert "--model" in calls[0][1]
    assert "example-model" in calls[0][1]
    assert "--model" in calls[1][1]
    assert "example-model" in calls[1][1]
    assert calls[0][1][calls[0][1].index("--region") + 1] == "us-west-2"
    assert calls[1][1][calls[1][1].index("--region") + 1] == "us-west-2"
