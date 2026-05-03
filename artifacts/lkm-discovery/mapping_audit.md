# Mapping audit log -- fermi-liquid-effective-mass-gaia

## 9-step synthesis checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Incorporated validated subgraph packages `artifacts/subgraphs/he3-effective-mass-gaia` and `artifacts/subgraphs/ybrh2si2-effective-mass-gaia`; root evidence files remain under `artifacts/lkm-discovery/input/`. |
| 2. Refine | done | Carried forward the subgraph self-contained claim text and preserved `lkm_id`, `source_paper`, `provenance_source`, and `lkm_original` metadata on LKM-derived claims. |
| 3. Decompose | done | Preserved the He-3 root decomposition into `he3_gamma_implies_mstar_ratio_2_12` and `he3_mstar_ratio_yields_f1_3_36`; did not decompose the YbRh2Si2 procedure beyond the validated subgraph. |
| 4. Hunt open problems | done | Rechecked discovery flags and subgraph audit trails; no cross-system contradiction was promoted. |
| 5. Mark suspicions | done | Retained the scope caution that YbRh2Si2 uses a homogeneous isotropic FCQPT/crossover model while He-3 uses a standard low-temperature Fermi-liquid mapping. |
| 6. Compile + infer | done | `gaia compile .` and `gaia infer .` passed from the parent package directory; IR hash `sha256:7144e2d657d3f46df836592df826be25f55e8dab2778fd7f62ed390417ccd7ab`. |
| 7. Review obligations/holes | done | `gaia check --hole .` passed with 0 holes across 8 independent claims. |
| 8. Search/support synthesis | done | Added support-only cross-paper wiring grounded by the two selected roots and their thermodynamic effective-mass premises. |
| 9. Repeat/exit rationale | done | Exit condition met for the requested synthesis: compile/check/hole/infer passed and no exact merge/equivalence/contradiction was promoted. |

## Subgraphs incorporated

| subgraph | root | source paper | action |
|---|---|---|---|
| `artifacts/subgraphs/he3-effective-mass-gaia` | `gcn_800070efac5e476d` | Alvesalo et al. 1979 | Copied validated claims, decomposition helpers, and deductions into `paper_alvesalo1979.py`; subgraph directory left untouched. |
| `artifacts/subgraphs/ybrh2si2-effective-mass-gaia` | `gcn_2741cdef209a457a` | Shaginyan et al. 2010 | Copied validated claims and deduction into `paper_shaginyan2010.py`; subgraph directory left untouched. |

## Claims

| label | lkm id | source paper | action |
|---|---|---|---|
| `gcn_2ee995fe1e674e2a` | `gcn_2ee995fe1e674e2a` | `paper:811623956246167556` | He-3 gamma/extrapolation premise copied from validated subgraph. |
| `gcn_1587257a956f4d18` | `gcn_1587257a956f4d18` | `paper:811623956246167556` | He-3 Landau mapping premise copied from validated subgraph. |
| `gcn_800070efac5e476d` | `gcn_800070efac5e476d` | `paper:811623956246167556` | He-3 selected root copied from validated subgraph and exported. |
| `he3_gamma_implies_mstar_ratio_2_12` | `gcn_800070efac5e476d` | `paper:811623956246167556` | Decomposition helper copied from validated subgraph. |
| `he3_mstar_ratio_yields_f1_3_36` | `gcn_800070efac5e476d` | `paper:811623956246167556` | Decomposition helper copied from validated subgraph. |
| `gcn_677c6c_landau_integral_relation` | `gcn_677c6c11780945f1` | `paper:867752612177379569` | YbRh2Si2 Landau integral premise copied from validated subgraph. |
| `gcn_03614e9b_homogeneous_isotropic_model` | `gcn_03614e9b5933496a` | `paper:867752612177379569` | YbRh2Si2 model-scope premise copied from validated subgraph. |
| `gcn_e0c364ff_inflection_fcqpt_condition` | `gcn_e0c364ff93804e75` | `paper:867752612177379569` | YbRh2Si2 FCQPT inflection premise copied from validated subgraph. |
| `gcn_6bbfeb95_stable_landau_solutions` | `gcn_6bbfeb95290d413d` | `paper:867752612177379569` | YbRh2Si2 numerical-stability premise copied from validated subgraph. |
| `gcn_ecddfefa_fermion_entropy_formula` | `gcn_ecddfefac84c4b46` | `paper:867752612177379569` | YbRh2Si2 entropy-formula premise copied from validated subgraph. |
| `gcn_2e693115_entropy_over_temperature_mass` | `gcn_2e69311592b04bcb` | `paper:867752612177379569` | YbRh2Si2 S/T effective-mass premise copied from validated subgraph. |
| `gcn_2741cdef_practical_effective_mass_scheme` | `gcn_2741cdef209a457a` | `paper:867752612177379569` | YbRh2Si2 selected root copied from validated subgraph and exported. |
| `cross_thermodynamic_routes_to_effective_mass` | synthesis | synthesis | Meta-claim added as a supported conclusion, not a leaf prior. |
| `cross_scope_caution_standard_fl_vs_fcqpt` | synthesis | synthesis | Scope-caution meta-claim added as a supported conclusion, not a leaf prior. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_944c3769779445a4` | `paper:811623956246167556` | `gcn_2ee995fe1e674e2a`, `gcn_1587257a956f4d18` | `gcn_800070efac5e476d` | `deduction` | 0.95 |
| He-3 root decomposition | `paper:811623956246167556` | `gcn_800070efac5e476d` | `he3_gamma_implies_mstar_ratio_2_12` | `deduction` | 0.95 |
| He-3 root decomposition | `paper:811623956246167556` | `gcn_800070efac5e476d` | `he3_mstar_ratio_yields_f1_3_36` | `deduction` | 0.95 |
| `gfac_749b6767459b4785` | `paper:867752612177379569` | `gcn_677c6c_landau_integral_relation`, `gcn_03614e9b_homogeneous_isotropic_model`, `gcn_e0c364ff_inflection_fcqpt_condition`, `gcn_6bbfeb95_stable_landau_solutions`, `gcn_ecddfefa_fermion_entropy_formula`, `gcn_2e693115_entropy_over_temperature_mass` | `gcn_2741cdef_practical_effective_mass_scheme` | `deduction` | 0.95 |

## Cross-paper decisions

| item | decision | dsl_action | rationale |
|---|---|---|---|
| He-3 `gamma -> m*/m` and YbRh2Si2 `S/T -> M*(T,B)` | cautious thematic synthesis | `support([he3_gamma_implies_mstar_ratio_2_12, gcn_2e693115_entropy_over_temperature_mass], cross_thermodynamic_routes_to_effective_mass, prior=0.84)` | Both subgraph claims explicitly use a low-energy thermodynamic quantity as an operational route to effective mass. |
| He-3 standard Fermi-liquid mapping versus YbRh2Si2 FCQPT/crossover model | preserve scope caution | `support([...], cross_scope_caution_standard_fl_vs_fcqpt, prior=0.88)` | The systems and model regimes differ, so the graph records non-equivalence rather than forcing an `equivalence()`. |

## Dismissed non-equivalences and false contradictions

| pair_or_flag | origin | decision | rationale |
|---|---|---|---|
| He-3 root versus YbRh2Si2 root | parent discovery + subgraph audits | no equivalence | Both concern effective mass, but one maps liquid He-3 gamma to m*/m while the other computes heavy-electron M*(T,B) near FCQPT. |
| He-3 standard mapping versus YbRh2Si2 FCQPT/crossover model | parent `contradictions.md` note | no contradiction | Different material regimes and assumptions can both be true under their scopes. |
| TiS2 damping mismatch and NiS2 Brinkman-Rice candidate | parent candidate list | not incorporated | Not selected roots for this two-root synthesis and not direct contradictions of the two validated subgraphs. |

## Priors

Leaf priors were merged from the two validated subgraphs into `src/fermi_liquid_effective_mass/priors.py`. Direct claim priors are capped at 0.90 and every justification retains `TODO:review`.

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 24 knowledge, 6 strategies, 0 operators; IR hash `sha256:7144e2d657d3f46df836592df826be25f55e8dab2778fd7f62ed390417ccd7ab`. |
| `gaia check --brief .` | pass | 8 independent premises with priors, 6 derived conclusions, 10 internal orphaned helper claims. |
| `gaia check --hole .` | pass | 0 holes / 8 independent claims; all direct priors present and capped at 0.90. |
| `gaia infer .` | pass | Inferred 18 beliefs using exact JT; converged after 2 iterations. |
