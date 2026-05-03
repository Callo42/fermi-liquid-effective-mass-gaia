# Mapping audit log -- he3-effective-mass-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_800070efac5e476d.json` for the chain backbone. |
| 2. Refine | done | Rewrote each gcn claim to include the normal-state liquid He-3 setting reported by Alvesalo et al. 1979, measured gamma, inferred m*/m, F1, and source context. |
| 3. Decompose | done | Preserved root `gcn_800070efac5e476d`; decomposed its two numeric components into derived helper claims because both components are explicit in the LKM root and factor steps. |
| 4. Hunt open problems | done | Checked discovery flags and three LKM match probes; no direct same-condition contradiction was promoted. |
| 5. Mark suspicions | done | Left review notes on extrapolating T >= about 3 mK to T -> 0 and on the numerical mapping being asserted without derivation in the LKM chain. |
| 6. Compile + infer | done | `gaia compile .` and `gaia infer .` passed after adding the workspace virtualenv bin directory to PATH. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims; `gaia inquiry obligation list` reported no open obligations. |
| 8. Search supports | done | LKM match outputs saved under `input/open_problem_match_*.json`; support candidates were not formalized because this package stays chain-backed to the selected root. |
| 9. Repeat/exit rationale | done | Exit condition met: compile/check/hole/infer passed, no hypotheses remain, no promoted contradictions, and no unresolved merge decisions. |

## Audit repair -- unsupported pressure wording

| date | finding | repair |
|---|---|---|
| 2026-05-03 | Parent audit found that generated self-contained claims used an unsupported pressure condition even though the loaded LKM evidence JSON did not clearly anchor that condition. | Removed the unsupported pressure condition from generated claim text and audit/dismissal notes. Claims now refer only to "the normal-state liquid He-3 setting reported by Alvesalo et al. 1979" unless a condition is explicitly present in the LKM chain. |

## Claims

| label | lkm id | source paper | self-contained transformation | lkm_original preserved |
|---|---|---|---|---|
| `gcn_2ee995fe1e674e2a` | `gcn_2ee995fe1e674e2a` | `paper:811623956246167556` | Added normal-state liquid He-3 setting as reported by Alvesalo et al. 1979, T >= about 3 mK linear region, gamma value, T -> 0 inference role, and citation. | yes |
| `gcn_1587257a956f4d18` | `gcn_1587257a956f4d18` | `paper:811623956246167556` | Added three-dimensional normal-liquid He-3 and conventional Landau Fermi-liquid mapping context, with gamma, m*/m, and F1 values. | yes |
| `gcn_800070efac5e476d` | `gcn_800070efac5e476d` | `paper:811623956246167556` | Added normal-state liquid He-3 setting as reported by Alvesalo et al. 1979, standard Landau mapping, and all numeric values. | yes |
| `he3_gamma_implies_mstar_ratio_2_12` | `gcn_800070efac5e476d` | `paper:811623956246167556` | Derived decomposition helper for the gamma -> m*/m component of the root. | yes |
| `he3_mstar_ratio_yields_f1_3_36` | `gcn_800070efac5e476d` | `paper:811623956246167556` | Derived decomposition helper for the m*/m -> F1 component of the root. | yes |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_944c3769779445a4` | `paper:811623956246167556` | `gcn_2ee995fe1e674e2a`, `gcn_1587257a956f4d18` | `gcn_800070efac5e476d` | `deduction` | 0.95 |
| decomposition | `paper:811623956246167556` | `gcn_800070efac5e476d` | `he3_gamma_implies_mstar_ratio_2_12` | `deduction` | 0.95 |
| decomposition | `paper:811623956246167556` | `gcn_800070efac5e476d` | `he3_mstar_ratio_yields_f1_3_36` | `deduction` | 0.95 |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| TiS2 damping mismatch | copied discovery `contradictions.md` | dismissed | Different material and model-scope limitation; not a He-3 effective-mass contradiction. |
| YbRh2Si2 heavy-electron/FCQPT effective mass | copied discovery `contradictions.md` | dismissed | Different material regime and assumptions; not mutually exclusive with the He-3 claim. |
| Zeise et al. 1981 lower effective-mass agreement | `open_problem_match_gamma_discrepancy.json` | support candidate only | Supports the lower Alvesalo scale relative to Abel et al.; no contradiction. |
| Lhota et al. temperature-scale check | `open_problem_match_gamma_discrepancy.json` | support candidate only | Suggests temperature-scale error is too small to explain the approximately 30% discrepancy; no contradiction with the root. |
| Helium-isotope droplet m*/m = 10.2 +/- 0.5 | `open_problem_match_gamma_discrepancy.json` | dismissed | Liquid-solid helium-isotope droplets and different assumptions; not the same bulk normal-liquid He-3 condition. |
| Kollar and Vollhardt gamma(P) relation | `open_problem_match_he3_mapping_values.json` | support/background candidate | Restates the same Landau relation over a pressure range; no conflicting same-condition value surfaced. |
| Aziz and Pathria F1(rho) series | `open_problem_match_f1_alternative.json` | dismissed | Density-dependent empirical series from sound-propagation data; not a direct contradiction of Alvesalo's reported He-3 F1 value because the conditions and inference path differ. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| None | Discovery found no exact equivalence pairs among chain-backed candidates. | none |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| See `dismissed/open_problem_false_alarms.md` | discovery + LKM match probes | Boundary-condition, material, or support-only cases rather than logical contradictions. |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 9 knowledge, 3 strategies, 0 operators; repaired IR hash prefix `sha256:be3e2f8f0`. |
| `gaia check --brief .` | pass | 2 independent premises with priors, 3 derived conclusions, 4 internal orphaned strategy-helper claims. |
| `gaia check --hole .` | pass | 0 holes / 2 independent claims. |
| `gaia infer .` | pass | Inferred 6 beliefs using exact JT; converged after 2 iterations. |
| `gaia inquiry obligation list` | pass | No open obligations. |
| `gaia inquiry hypothesis list` | pass | No hypotheses. |
