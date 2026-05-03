# Merge audit

Original discovery note: narrow root supplied, so no broad candidate merge pass was performed before formalization.

## Formalization decisions

| item | decision | rationale | action |
|---|---|---|---|
| `gcn_31bc66ca16a44508` / `gcn_795699f572b24ed5` / `gcn_dd12256615264dfb` | keep distinct | The three premises assert different parts of the root argument: Fermi-liquid entropy scaling, Luttinger/chemical-potential pinning, and thermodynamic continuity failure. | Separate claim labels and separate priors. |
| `gcn_e4ecd721edd14d3f` | preserve as root | The root is a long compound conclusion but is the selected LKM conclusion and must remain intact with `lkm_original`. | Canonical exported root claim. |
| Root and premise components | decompose but do not merge | FL definition, Z/T_K relation, singlet-zero-entropy endpoint, Luttinger pinning, and entropy-instability pieces are grounded in the chain steps. They are review helpers, not replacements for the original `gcn_*` claims. | Added derived helper claims and deduction strategies. |
| External Brinkman-Rice/NiS2/Kondo candidates | keep outside graph | They were used for open-problem hunting only. Strict package bootstrap is root evidence JSON only. | Recorded in contradiction/dismissal audit; no support/equivalence/contradiction edge emitted. |

No unresolved merge decisions remain.
