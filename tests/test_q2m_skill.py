"""Q2M opt-in behavior and role scoping tests (no network calls)."""
from viableos.q2m_skill import q2m_skill_appendix


def test_q2m_default_disabled_for_all_agents():
    config = {}
    for role in ["s1", "s2", "s3", "s3star", "s4", "s5"]:
        assert q2m_skill_appendix(config, role) == ""


def test_q2m_unrelated_s1_unit_unmodified():
    config = {"q2m_workstream": {"enabled": True}}
    assert q2m_skill_appendix(config, "s1", {"name": "Marketing"}) == ""


def test_q2m_only_explicitly_tagged_s1_roles():
    config = {"q2m_workstream": {"enabled": True}}
    text = q2m_skill_appendix(config, "s1", {
        "name": "System Engineering",
        "q2m_roles": ["requirements_agent", "architecture_agent", "unknown_agent"],
    })
    assert "requirements_agent" in text
    assert "architecture_agent" in text
    assert "unknown_agent" not in text
    assert "six-category" in text
    assert "approved" in text


def test_q2m_s3star_is_independent_and_read_only():
    config = {"q2m_workstream": {"enabled": True}}
    text = q2m_skill_appendix(config, "s3star")
    assert "independently" in text.lower()
    assert "read-only" in text.lower()
    assert "real" not in text or "evidence" in text


def test_q2m_unsupported_role_is_noop():
    config = {"q2m_workstream": {"enabled": True}}
    assert q2m_skill_appendix(config, "unknown") == ""
