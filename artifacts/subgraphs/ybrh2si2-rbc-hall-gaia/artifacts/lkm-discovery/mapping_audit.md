# Mapping audit log -- ybrh2si2-rbc-hall-gaia

## Batch checklist / report

| step | status | note |
|---|---|---|
| 1. Bootstrap from root | done | Loaded only `input/evidence_gcn_42a4ff7fd004413f.json`; root `gcn_42a4ff7fd004413f` has one evidence chain and one factor `gfac_0b967f9e875749e8`. |
| 2. Refine self-contained | done | Rewrote each distinct `gcn_*` as a self-contained Gaia `claim()` with system, method, quantities, source paper, and verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the root and added three helper claims for method/parameterization, opposite-sign Hall products, and RBC DOS/gamma values. |
| 4. Hunt open problems | done | Compared every new claim/helper against the existing YbRh2Si2 homogeneous-isotropic FCQPT context; no pair was promoted to `contradiction()` because the claims have compatible scopes. |
| 5. Mark suspicions | done | Logged scope and model-sensitivity suspicions below and in `dismissed/homogeneous_isotropic_vs_rbc_scope.md`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims; `gaia inquiry obligation list` and `gaia inquiry hypothesis list` reported no open items. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON. Existing discovery files are preserved for later parent synthesis. |
| 9. Repeat / exit rationale | closed | The single selected root chain is fully mapped; remaining questions are synthesis obligations, not reasons to pull unselected roots into this standalone subgraph. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_c243dcb58cae4418` | `gcn_c243dcb_rbc_phase_shift_parametrization` | `paper:811773737962569729` | Refined premise: RBC phase-shift parametrization for YbRh2Si2 heavy-fermion renormalized-band calculations. |
| `gcn_48bba377911d4985` | `gcn_48bba377_specific_heat_calibration` | `paper:811773737962569729` | Refined premise: specific-heat/DOS calibration of the resonance-width parameter and its reliability claim for transport indicators. |
| `gcn_42a4ff7fd004413f` | `gcn_42a4ff_rbc_hall_dos_values` | `paper:811773737962569729` | Preserved selected compound root with explicit YbRh2Si2/YbIr2Si2 values and Hall-product signs. |
| helper | `helper_rbc_parameterization_constrained_by_cef_gamma` | `paper:811773737962569729` | Decomposition helper for root component (a): RBC CEF/gamma-constrained method and parameterization. |
| helper | `helper_ybrh2si2_opposite_hall_transport_products` | `paper:811773737962569729` | Decomposition helper for root component (b): opposite-sign YbRh2Si2 band transport products and Hall cancellation. |
| helper | `helper_rbc_dos_gamma_ybrh2si2_ybir2si2` | `paper:811773737962569729` | Decomposition helper for root component (c): RBC DOS and Sommerfeld coefficients for YbRh2Si2 and YbIr2Si2. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind |
|---|---|---|---|---|
| `gfac_0b967f9e875749e8` | `paper:811773737962569729` | `gcn_c243dcb58cae4418`, `gcn_48bba377911d4985` | `gcn_42a4ff7fd004413f` | `deduction(..., prior=0.95)` with six numbered LKM steps. |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_rbc_parameterization_constrained_by_cef_gamma` | Root text plus factor step 2 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_ybrh2si2_opposite_hall_transport_products` | Root text plus factor step 4 | `support([root], helper, prior=0.90)`; isolates the Hall-transport component. |
| `helper_rbc_dos_gamma_ybrh2si2_ybir2si2` | Root text plus factor step 5 | `support([root], helper, prior=0.90)`; isolates the DOS/gamma component. |

## Open-problem / contradiction hunt

| checked claim | comparison target | verdict | rationale |
|---|---|---|---|
| `gcn_c243dcb_rbc_phase_shift_parametrization` | Existing `gcn_03614e9b_homogeneous_isotropic_model` premise in the parent YbRh2Si2 FCQPT branch | dismissed as scope tension | RBC explicitly keeps material-specific CEF splitting, bands, and transport integrals, while the FCQPT premise deliberately neglects band structure for universal scaling. Different model scopes can both be true. |
| `gcn_48bba377_specific_heat_calibration` | Existing entropy/S/T effective-mass route in the parent YbRh2Si2 branch | dismissed as scope tension | Both use thermodynamic low-energy quantities as calibrations/proxies, but one calibrates an RBC DOS and the other extracts M*(T,B) in a homogeneous FCQPT model. They are not mutually exclusive. |
| `gcn_42a4ff_rbc_hall_dos_values` | Existing parent branch's homogeneous isotropic effective-mass scheme | dismissed as scope tension | The root sharpens a weak premise in the existing graph by adding material-specific band/Hall/DOS evidence, but it does not state that universal FCQPT scaling is false. |
| helper claims | same existing parent context | dismissed as decomposition-only | Helpers are components of the selected root and inherit the same scope; no independent contradiction is promoted. |

## Suspicions and obligations left for synthesis

- The specific-heat calibration premise is approximation-sensitive: reproducing `gamma_exp` constrains the DOS, but the LKM chain does not independently audit whether the same parametrization uniquely fixes band occupations and Hall integrals.
- The Hall-cancellation conclusion depends on band-resolved relaxation-time weighting in later interpretation; the selected root gives cancellation of reduced products, not a full material-specific low-field Hall coefficient prediction under arbitrary scattering assumptions.
- Parent synthesis should connect this subgraph to the existing YbRh2Si2 branch as a scope qualifier for the homogeneous isotropic premise, not as a contradiction.
- The graph-guided candidate list identifies a possible future follow-up (`gcn_c38f8ce989fd454a`, dHvA masses and 4f localization) if synthesis needs an experimental Fermi-surface check against RBC.

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate within the selected root evidence chain. | none |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| homogeneous isotropic FCQPT premise vs material-specific RBC/Hall evidence | Dismissed as compatible model-scope distinction. | No `contradiction()` emitted. |

## Exit rationale

The standalone package maps the selected root and all distinct `gcn_*` claims in its chain. No unselected root was imported as Gaia evidence; copied discovery files preserve the audit trail for a later parent-package synthesis step.
