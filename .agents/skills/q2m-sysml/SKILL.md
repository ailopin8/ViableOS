---
name: q2m-sysml
description: Use to derive purpose, stakeholder needs, testable requirements, functional/structural architectures, typed relationships, state machines and assurance evidence from a system question, and construct or review SysML v2 models. Do not use for generic definitions with no system-model deliverable.
---

# Q2M SysML v2 agent modelling method

When a user asks to create, revise or review a systems engineering model:
1. Capture the system question, model purpose, boundary, context, stakeholders,
   unresolved assumptions, required decision and source authority.
2. Collect answers across six categories: ontology, teleology, structure,
   function/dynamics, governance/evidence, operating context.
3. Identify stable entity and relationship IDs, typed endpoints, and explicit
   relationship direction, units, ports, material/energy/information exchanges.
   A relationship may itself be the subject/target of another relationship.
4. Derive stakeholder needs and testable 'shall' requirements; attach their
   acceptance criteria and derivation provenance.
5. Derive functions and allocate them to candidate parts. Draw structural
   and dynamic views from the same model; model actions, state machines,
   transition guards, feedback and change through time.
6. Express formal content using native SysML v2 definitions/usages, requirements,
   parts, actions, states, ports, verification cases and relevant constraints.
7. Review every trace and compare claims against source evidence. Verify model
   syntax with a real SysML v2 parser before claiming conformance. Do not
   claim verification/validation without executed evidence.
8. Return reviewed proposals to the owner/coordinator for baseline approval;
   preserve all IDs and revision history.

When working on ViableOS's generated agents, keep this as a scoped optional
workstream, not a replacement for VSM governance. See
`src/viableos/q2m_skill.py` and `docs/q2m_agent_workstream.md`.
