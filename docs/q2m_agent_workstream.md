# Q2M SysML v2 modelling workstream (opt-in)

This is an OPTIONAL role-scoped integration, not a modification to ViableOS's
default organisation or a deployment to a running OpenClaw installation.

## Why
A question about a system should produce answers in six categories: identity,
purpose/needs, structure/relationships, functions/dynamics, rules/evidence,
and environment. These categories feed an engineering derivation chain and
ultimately one traceable SysML v2 model with structural and dynamic views.

## Enable in a ViableOS configuration
Add the opt-in property and explicitly tag only the **engineering** S1 units:

```json
{
  "viable_system": {
    "q2m_workstream": {"enabled": true},
    "system_1": [
      {
        "name": "Systems Modelling",
        "purpose": "Produce verified system-model candidates",
        "q2m_roles": [
          "ontology_agent",
          "needs_agent",
          "requirements_agent",
          "architecture_agent",
          "dynamics_agent"
        ]
      }
    ]
  }
}
```

The fragment above illustrates NEW fields; merge it into a complete, valid
ViableOS configuration rather than using it as an entire configuration.
Do not replace existing system_1 units to enable this feature.

## Role mapping
- **S1**: only explicitly tagged modelling units receive detailed Q2M instructions.
- **S2**: coordinate dependencies, conflicts and serialized graph merges.
- **S3**: manage model baselines, readiness gates and technical capacity.
- **S3***: independent read-only evidence and quality review.
- **S4**: monitor standards, technical evidence and environmental changes.
- **S5**: policy/identity; elevate important approvals to the human owner.

## Produced model artifacts
1. Knowledge matrix with 24 answer types across six categories.
2. Ontology with stable IDs for entities AND relationships.
3. Purpose -> needs -> requirements -> functions -> components/interfaces trace.
4. Structural graph and typed adjacency matrices.
5. Dynamic actions, state machine, temporal equations and feedback loops.
6. Verification cases, validation evidence, uncertainty register, change impacts.
7. SysML v2 textual source plus accessible model-view prompts.

No generated model is 'verified' merely because the agent wrote a test.
No language-conformance claim without a SysML v2 parser. Human approval
is required before promotion to an accepted baseline.

## Compatibility and controls
If `q2m_workstream.enabled` is absent/false, output is unchanged. If true,
untagged S1 units are unchanged. Existing ViableOS tool access, anti-loop,
workspace, escalation and human-in-the-loop restrictions still apply.

See the external standalone Q2M skill package for offline graph QA and
worked heating-system example. The embedded guidance deliberately has no
new network or package dependencies.
