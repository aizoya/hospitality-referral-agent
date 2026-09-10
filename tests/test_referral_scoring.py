from src.referral_agent import score_referral_record


def test_high_priority_warm_referral():
    result = score_referral_record(
        {
            "business_name": "Harbor Events",
            "contact_name": "Jordan Lee",
            "business_type": "event venue",
            "location": "Oakland, CA",
            "referral_source": "existing catering client",
            "stated_need": "Needs a reliable caterer for two September events",
            "urgency": "high",
            "contact_complete": True,
            "referral_strength": "hot",
        }
    )
    assert result["score"] == 100
    assert result["priority"] == "HIGH"
    assert result["recommended_timing"] == "within 24 hours"
    assert result["approval_required"] is True
    assert result["outbound_status"] == "DRAFT_ONLY_NOT_SENT"


def test_medium_priority_record():
    result = score_referral_record(
        {
            "business_type": "restaurant",
            "stated_need": "Interested in referral partnership",
            "urgency": "low",
            "contact_complete": False,
            "referral_strength": "cold",
        }
    )
    assert result["score"] == 66
    assert result["priority"] == "MEDIUM"
    assert result["recommended_timing"] == "within 3 business days"


def test_missing_details_do_not_inflate_score():
    result = score_referral_record({})
    assert result["score"] == 31
    assert result["priority"] == "LOW"
    assert result["approval_required"] is True
