"""Opt-in Q2M (Question-to-Model) guidance for generated ViableOS agents.

No change to existing generated skills unless viable_system.q2m_workstream.enabled
is true. S1 modelling workers also require explicit q2m_roles per unit.
"""
from __future__ import annotations

from typing import Any

Q2M_ROLES = {
    "ontology_agent": "Define system identity, ontology, boundary, context and unknowns. Return typed entities/relationships with provenance.",
    "needs_agent": "Derive purpose and stakeholder needs; trace each need to a concern, without inventing technical solutions.",
    "requirements_agent": "Derive individually testable shall-statements, acceptance methods and criteria; trace each to its originating need.",
    "architecture_agent": "Derive functions then allocate them to components; type composition, interface and material/energy/information relationships.",
    "dynamics_agent": "Define actions, state variables, state machines, time scales, transition guards, disturbances and feedback.",
    "assurance_agent": "Independently review traceability, graph consistency, parser results, observed evidence and unsupported claims.",
}

Q2M_SHARED = """
## Q2M modelling method
Use the six-category Question–Answer Ontology: (1) ontology/identity,
(2) teleology/purpose and needs, (3) structure/relations,
(4) function/dynamics, (5) governance/epistemology/evidence, and
(6) operating context/limitations. These are knowledge questions,
not native SysML metaclasses.

Follow purpose -> needs -> testable requirements -> functions -> components
and interfaces -> actions, states and feedback -> verification/validation.
Keep stable IDs for every entity and typed relationship; dependencies
may refer to other relationship IDs. Build structural and dynamic views
of the SAME model. Use genuine SysML v2 textual notation (not SysML v1
blocks or a diagram invented as notation). A JSON trace graph is staging
data, not SysML.

Mark every numerical requirement as sourced, provisional, or unknown.
Never call a model verified, validated or standards-compliant without
actual evidence, independent review and (for syntax) a SysML v2 parser.
Work only within existing tool permissions and workspace boundaries.
Make proposals against a named baseline revision; do not alter approved
baselines without the required human decision.
"""

VSM_GUIDANCE = {
    "s2": "Coordinate Q2M specialist handoffs; serialize same-ID model edits and route conflicts. Never perform S1 modelling work yourself.",
    "s3": "Track model coverage, resource use, proposed baselines and quality gates. Do not approve unreviewed model revisions.",
    "s3star": "Independently audit model traces, requirements, guards, relationships, evidential claims and parser checks. Remain read-only.",
    "s4": "Monitor outside-in changes in modelling standards, domain evidence, environmental constraints and relevant technologies. Cite sources.",
    "s5": "Protect purpose, scope and assurance policy. Present human decisions for changes to safety boundaries or accepted baselines; never approve alone.",
}


def q2m_skill_appendix(
    viable_system: dict[str, Any],
    vsm_role: str,
    unit: dict[str, Any] | None = None,
) -> str:
    """Return role-scoped appendix, or an empty string if not enabled/relevant."""
    config = viable_system.get("q2m_workstream") or {}
    if not isinstance(config, dict) or config.get("enabled") is not True:
        return ""
    if vsm_role == "s1":
        raw_roles = (unit or {}).get("q2m_roles") or []
        if not isinstance(raw_roles, list):
            return ""
        roles = [role for role in raw_roles if isinstance(role, str) and role in Q2M_ROLES]
        if not roles:
            return ""
        assignment = "\n".join(f"- {role}: {Q2M_ROLES[role]}" for role in dict.fromkeys(roles))
        return Q2M_SHARED + "\n## Your Q2M specialist assignments\n" + assignment + "\n"
    guidance = VSM_GUIDANCE.get(vsm_role)
    return Q2M_SHARED + "\n## Your ViableOS Q2M responsibility\n- " + guidance + "\n" if guidance else ""
