from pathlib import Path


STATIC_DEMO = Path("docs/index.html")


def test_static_demo_exists_and_is_offline_safe():
    page = STATIC_DEMO.read_text()
    assert "Hospitality Referral Agent" in page
    assert "Analyze referral offline" in page
    assert "OWNER APPROVAL REQUIRED" in page
    assert "DRAFT ONLY — NOTHING HAS BEEN SENT" in page
    assert "makes no network or AWS requests" in page
    assert "fetch(" not in page
    assert "XMLHttpRequest" not in page


def test_static_demo_matches_core_scoring_thresholds():
    page = STATIC_DEMO.read_text()
    assert "score >= 80" in page
    assert 'priority = "HIGH"' in page
    assert "score >= 60" in page
    assert 'priority = "MEDIUM"' in page
    assert 'priority = "LOW"' in page
