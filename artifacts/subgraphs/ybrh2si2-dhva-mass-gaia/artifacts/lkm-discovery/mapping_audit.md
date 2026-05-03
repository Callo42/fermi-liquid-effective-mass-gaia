# Mapping audit log -- ybrh2si2-dhva-mass-gaia

## Batch checklist / report

| step | status | note |
|---|---|---|
| 1. Bootstrap from root | done | Loaded only `input/evidence_gcn_c38f8ce989fd454a.json`; root `gcn_c38f8ce989fd454a` has one evidence chain and one factor `gfac_5648470e5459468a`. |
| 2. Refine self-contained | done | Rewrote every distinct `gcn_*` in the chain as a self-contained Gaia `claim()` with explicit system, field regime, method, quantities, source paper, and verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the root and added three helper claims for H-parallel-a frequencies/masses, itinerant-4f LDA angular-dependence mismatch, and first-Fermi-surface-information scope. |
| 4. Hunt open problems | done | Compared every new claim/helper against the existing YbRh2Si2 FCQPT homogeneous-isotropic and Friedemann2010 RBC/Hall context; no pair was promoted to `contradiction()` because the claims differ by field regime, observable, or model scope and can coexist. |
| 5. Mark suspicions | done | Logged high-field, itinerant-4f LDA-sensitivity, and synthesis-scope cautions below and in `dismissed/ybrh2si2_dhva_vs_rbc_fcqpt_scope.md`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory; IR hash `sha256:bf101fbccc8d5c19ab5eaece813679aa62f7293f29e42865662f74499b9aaec5`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims; `gaia inquiry obligation list` and `gaia inquiry hypothesis list` reported no open items. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON. Existing YbRh2Si2 context was used only for contradiction screening. |
| 9. Repeat / exit rationale | closed | Exit condition met for the requested root-only subgraph: compile/check/hole/infer passed, 0 holes remain, no hypotheses are open, and no logically incompatible RBC/FCQPT contradiction was promoted. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_5501e18a04cc458e` | `gcn_5501e18a_high_field_dhva_scope` | `paper:812036747075518464` | Refined premise: high-field dHvA scope caveat for YbRh2Si2. |
| `gcn_f20b1f42f35548fb` | `gcn_f20b1f42_itinerant_4f_lda_sensitivity` | `paper:812036747075518464` | Refined premise: itinerant-4f LDA/FLAPW sensitivity and unreliability caveat. |
| `gcn_c38f8ce989fd454a` | `gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch` | `paper:812036747075518464` | Preserved selected compound root with explicit frequencies, masses, field orientation, and LDA mismatch. |
| helper | `helper_dhva_frequencies_masses_h_parallel_a` | `paper:812036747075518464` | Decomposition helper for root component (a): four H-parallel-a dHvA frequencies and cyclotron masses. |
| helper | `helper_dhva_angular_dependence_itinerant_lda_mismatch` | `paper:812036747075518464` | Decomposition helper for root component (b): measured angular dependence vs itinerant-4f LDA/FLAPW and LuRh2Si2 reference resemblance. |
| helper | `helper_dhva_first_fs_information_scope` | `paper:812036747075518464` | Decomposition helper for root component (c): first experimental Fermi-surface information plus high-field/LDA-sensitivity cautions. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_5648470e5459468a` | `paper:812036747075518464` | `gcn_5501e18a04cc458e`, `gcn_f20b1f42f35548fb` | `gcn_c38f8ce989fd454a` | `deduction(..., prior=0.95)` with seven numbered LKM steps. | 0.95 |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_dhva_frequencies_masses_h_parallel_a` | Root text plus factor steps 3-4 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_dhva_angular_dependence_itinerant_lda_mismatch` | Root text plus factor steps 5-6 | `support([root], helper, prior=0.90)`; isolates the angular-dependence/LDA mismatch component. |
| `helper_dhva_first_fs_information_scope` | Root text plus factor steps 1-2 and 7 | `support([root], helper, prior=0.90)`; isolates first-FS-information significance and cautions. |

## Open-problem / contradiction hunt

| checked claim | comparison target | verdict | rationale |
|---|---|---|---|
| `gcn_5501e18a_high_field_dhva_scope` | Existing `gcn_03614e9b_homogeneous_isotropic_model` premise in the parent YbRh2Si2 FCQPT branch | dismissed as scope tension | High-field dHvA data may differ from low-field QCP physics, while the FCQPT premise is a universal-scaling model that explicitly neglects band structure; the claims can both be true. |
| `gcn_f20b1f42_itinerant_4f_lda_sensitivity` | Friedemann2010 RBC/Hall/DOS subgraph | dismissed as method distinction | Itinerant-4f LDA sensitivity and phenomenological RBC thermodynamic calibration are different modeling surfaces, not mutually exclusive propositions. |
| `gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch` | Existing FCQPT and RBC context | dismissed as synthesis caution | The dHvA root provides experimental Fermi-surface constraints that qualify model scope, but neither existing branch asserts an incompatible high-field dHvA frequency/mass spectrum. |
| helper claims | same existing YbRh2Si2 context | dismissed as decomposition-only | Helpers are components of the selected root and inherit the same scope; no independent contradiction is promoted. |

## Suspicions and obligations left for synthesis

- The dHvA result is high-field (12-28 T, H parallel a), so using it as evidence for the zero- or low-field QCP Fermi surface requires a field-evolution synthesis step.
- The itinerant-4f LDA mismatch is strong evidence that one simple band-structure prediction set fails, but the selected chain itself cautions against interpreting the mismatch as a direct proof of intrinsic 4f localization.
- Parent synthesis should connect this subgraph to the existing FCQPT and RBC branches as an experimental Fermi-surface/model-scope qualifier, not as a contradiction unless future evidence asserts incompatible predictions for the same observable and field regime.

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate within the selected root evidence chain. | none |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| dHvA high-field Fermi-surface evidence vs FCQPT homogeneous-isotropic model | Dismissed as compatible field/model-scope distinction. | No `contradiction()` emitted. |
| dHvA LDA mismatch vs Friedemann2010 RBC/Hall/DOS evidence | Dismissed as complementary method evidence rather than logical incompatibility. | No `contradiction()` emitted. |

## Priors

Leaf priors are seeded in `src/ybrh2si2_dhva_mass/priors.py`; every value is below or equal to the independent-leaf cap of 0.90 and every justification ends with `TODO:review`.

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 11 knowledge, 4 strategies, 0 operators; IR hash `sha256:bf101fbccc8d5c19ab5eaece813679aa62f7293f29e42865662f74499b9aaec5`. |
| `gaia check --brief .` | pass | 2 independent premises with priors, 4 derived conclusions, and 5 internal structural orphan helper claims from compiled strategy internals. |
| `gaia check --hole .` | pass | 0 holes / 2 independent claims; all direct priors present and capped below 0.90. |
| `gaia infer .` | pass | Inferred 7 beliefs using exact JT; converged after 2 iterations. |
| `gaia inquiry obligation list` | pass | `(no open obligations)` |
| `gaia inquiry hypothesis list` | pass | `(no hypotheses)` |
