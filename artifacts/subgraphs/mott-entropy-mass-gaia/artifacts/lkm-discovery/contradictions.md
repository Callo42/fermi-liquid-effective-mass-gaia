# Discovery contradiction flags

Broad discovery was skipped because the user supplied the narrow root `gcn_e4ecd721edd14d3f`; the formal package bootstraps only from the root evidence JSON.

## Open-problem hunt versus existing context

| candidate context | decision | rationale |
|---|---|---|
| Brinkman-Rice canonical/DMFT context (`gcn_f4c74a5922dd4aa1`, `gcn_5407089724b24dc4`) | not promoted | These restate or support the root's mass/Z/T_K assumptions. `gcn_5407089724b24dc4` has no chains in the available input, and neither supplies a mutually exclusive same-condition claim. |
| Spinon finite-mass route (`gcn_5f269db6cc3e4841`) | open question, not a `contradiction()` edge | This is a genuine research tension because it allows Z to vanish without m*/m -> infinity, but it changes the transition class to a spinon-Fermi-surface route and is not logically incompatible with the root's explicitly conditional Brinkman-Rice scenario. |
| NiS2 pressure-tuned heavy Fermi liquid (`gcn_29401e4284574aa2`) | dismissed as false alarm | NiS2 supplies experimental support for a large-Fermi-surface Brinkman-Rice-like correlated metal near a Mott boundary; it does not assert direct continuity into a nondegenerate singlet Mott insulator. |
| Kondo-lattice Brinkman-Rice liquid (`gcn_7ae79f122f1c4fcb`) | dismissed as false alarm | The Kondo-lattice fixed-point claim concerns screened f-ion heavy quasiparticles and finite Stoner enhancement, not a direct Fermi-liquid-to-zero-entropy singlet Mott endpoint. |

No formal `contradiction(...)` operator was emitted because every audited tension either changes the boundary conditions or is outside the strict root-only chain backbone.
