# Mapping audit log -- cemo-kadowaki-wilson-gaia

## Batch checklist / report

| step | status | note |
|---|---|---|
| 1. Bootstrap from root | done | Loaded only `input/evidence_gcn_bc46d7d5f5284a0e.json`; root `gcn_bc46d7d5f5284a0e` has one evidence chain and one factor `gfac_19fb01af249a451c`. |
| 2. Refine self-contained | done | Rewrote all three distinct `gcn_*` claims as self-contained Gaia `claim()` declarations with system, quantities, source paper, and verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the root and added three grounded helpers for `A/gamma^2`, the Wilson/Sommerfeld estimates, and the final correlated-FL consistency component. |
| 4. Hunt open problems | done | Compared every new claim/helper against the existing parent thermodynamic-route and correlated-FL/RBC branches; no pair was promoted to `contradiction()` because the material/model scopes are compatible. |
| 5. Mark suspicions | done | Logged the KW degeneracy-normalization caution, Wilson `mu_eff` convention sensitivity, and parent-branch scope dismissals below and in `dismissed/thermodynamic_route_correlated_fl_scope.md`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory; IR hash `sha256:93e28a84863d6f24d64d68b7dfb7b231a0d9e76acfbdd2e89b92609c48b38ccc`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON. |
| 9. Repeat / exit rationale | closed | The single selected root chain is fully mapped; remaining questions are synthesis cautions for a later parent-package integration step. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_2dc55af0490a4727` | `gcn_2dc55af_kw_empirical_scale` | `paper:813219117229146113` | Refined premise: empirical Kadowaki-Woods scale and its use as correlated-FL evidence. |
| `gcn_7459a44654dc416e` | `gcn_7459a446_wilson_ratio_interpretation` | `paper:813219117229146113` | Refined premise: Wilson/Sommerfeld-ratio definition and the two `mu_eff` normalizations used for FL consistency. |
| `gcn_bc46d7d5f5284a0e` | `gcn_bc46d7_cemo_kw_wilson_fl_consistency` | `paper:813219117229146113` | Preserved selected compound root with explicit CeMo2Si2C `A`, `gamma`, `chi_FL`, `A/gamma^2`, and `R_W` values. |
| helper | `helper_cemo_kw_ratio_original_scale` | `paper:813219117229146113` | Decomposition helper for the `A/gamma^2~=0.5e-5` calculation and original KW-scale comparison. |
| helper | `helper_cemo_wilson_ratio_dual_reference` | `paper:813219117229146113` | Decomposition helper for the two Wilson/Sommerfeld estimates: `R_W~=0.81` and `R_W~=1.7`. |
| helper | `helper_cemo_ratio_consistency_correlated_fl` | `paper:813219117229146113` | Decomposition helper for the grounded conclusion that the ratios mutually support correlated-FL phenomenology. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind |
|---|---|---|---|---|
| `gfac_19fb01af249a451c` | `paper:813219117229146113` | `gcn_2dc55af0490a4727`, `gcn_7459a44654dc416e` | `gcn_bc46d7d5f5284a0e` | `deduction(..., prior=0.95)` with seven numbered LKM steps. |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_cemo_kw_ratio_original_scale` | Root text plus factor steps 1-4 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_cemo_wilson_ratio_dual_reference` | Root text plus factor steps 5-6 | `support([root], helper, prior=0.90)`; isolates the Wilson/Sommerfeld component. |
| `helper_cemo_ratio_consistency_correlated_fl` | Root text plus factor step 7 | `support([KW helper, Wilson helper], helper, prior=0.90)`; isolates the final correlated-FL consistency component. |

## Open-problem / contradiction hunt

| checked claim | comparison target | verdict | rationale |
|---|---|---|---|
| `gcn_bc46d7_cemo_kw_wilson_fl_consistency` | Existing parent He-3 thermodynamic route from gamma to `m*/m` and `F1` | dismissed as related-but-distinct | Both use low-temperature thermodynamic quantities in Fermi-liquid reasoning, but they concern different materials and different derived quantities. |
| `gcn_bc46d7_cemo_kw_wilson_fl_consistency` | Existing parent YbRh2Si2 Shaginyan thermodynamic route using `S/T -> M*(T,B)` in an FCQPT crossover model | dismissed as scope distinction | CeMo2Si2C is treated as a low-temperature correlated-FL ratio check, whereas the YbRh2Si2 branch is a homogeneous heavy-electron/FCQPT model that explicitly spans crossover or non-Fermi-liquid regimes. |
| `gcn_bc46d7_cemo_kw_wilson_fl_consistency` | Existing parent YbRh2Si2 Friedemann RBC/DOS/Hall correlated-FL branch | dismissed as material/model distinction | Both branches use thermodynamic calibration motifs and correlated-FL language, but the YbRh2Si2 branch is a material-specific band/DOS/Hall calculation rather than a claim about CeMo2Si2C ratio values. |
| `helper_cemo_kw_ratio_original_scale` | Factor-step-4 alternative degeneracy-scaled KW value for intermediate-valent Ce with `N=6` | retained as synthesis caution | The selected chain itself quotes the lower `6.7e-7` scale yet emphasizes the original KW value; this is a normalization question, not a logical impossibility inside the evidence chain. |
| `helper_cemo_wilson_ratio_dual_reference` | Difference between `R_W~=0.81` and `R_W~=1.7` under two `mu_eff` choices | retained as synthesis caution | Both values are explicitly computed in the selected chain; the evidence supports a convention-sensitive interpretation rather than a contradiction. |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_2dc55af_kw_empirical_scale` | 0.82 | Standard empirical correlated-metal diagnostic, but KW normalization is material/degeneracy sensitive. |
| `gcn_7459a446_wilson_ratio_interpretation` | 0.74 | Grounded Wilson/Sommerfeld premise, but the `mu_eff` normalization choice substantially changes the reported value. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_bc46d7_cemo_kw_wilson_fl_consistency` | 0.78755228292 |
| `helper_cemo_kw_ratio_original_scale` | 0.8536897302593721 |
| `helper_cemo_wilson_ratio_dual_reference` | 0.8536897302593721 |
| `helper_cemo_ratio_consistency_correlated_fl` | 0.84221721999209 |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate within the selected root evidence chain. | none |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| CeMo2Si2C KW/Wilson root vs parent thermodynamic-route and correlated-FL branches | Dismissed as compatible scope/material distinctions. | No `contradiction()` emitted. |
| Original KW-scale comparison vs degeneracy-scaled KW caution | Retained as caution/open question, not logical contradiction. | No `contradiction()` emitted. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root or parent source claim was imported as Gaia evidence; parent comparisons are audit-only so a later synthesis step can decide whether to wire a scoped support/caution edge into the parent package.
