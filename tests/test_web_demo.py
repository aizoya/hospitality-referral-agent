import pytest

from scripts.run_web_demo import SAMPLE, _parse_form, evaluate, render_page


def test_render_page_is_offline_safe_by_default():
    page = render_page()
    assert "Hospitality Referral Agent" in page
    assert "Run live Strands + Bedrock" not in page
    assert "never sends outreach automatically" in page
    assert "Live Bedrock invocation is disabled by default" in page


def test_render_page_can_expose_controlled_live_action():
    page = render_page(live_enabled=True)
    assert "Run live Strands + Bedrock" in page
    assert "controlled session" in page


def test_offline_evaluate_preserves_owner_approval():
    data = {**SAMPLE, "action": "score"}
    result = evaluate(data)
    assert result["priority"] == "HIGH"
    assert result["approval_required"] is True
    assert result["outbound_status"] == "DRAFT_ONLY_NOT_SENT"
    assert "live_output" not in result


def test_live_evaluate_is_blocked_without_explicit_enablement():
    data = {**SAMPLE, "action": "live"}
    with pytest.raises(PermissionError):
        evaluate(data)


def test_result_page_shows_owner_approval_checkpoint():
    data = {**SAMPLE, "action": "score"}
    page = render_page(data, evaluate(data))
    assert "OWNER APPROVAL REQUIRED" in page
    assert "NOTHING HAS BEEN SENT" in page
    assert "HIGH" in page


def test_parse_form_normalizes_boolean_and_action():
    payload = (
        "business_name=Venue&contact_name=Jordan&business_type=Hotel&location=Oakland"
        "&referral_source=Partner&stated_need=Catering&urgency=medium"
        "&referral_strength=warm&contact_complete=true&notes=Hello&action=score"
    ).encode()
    parsed = _parse_form(payload)
    assert parsed["contact_complete"] is True
    assert parsed["action"] == "score"
    assert parsed["business_name"] == "Venue"
