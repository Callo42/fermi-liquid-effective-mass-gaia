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
| TiS2 damping mismatch and NiS2 Brinkman-Rice candidate | parent candidate list | not incorporated | Not selected roots for the initial He-3/YbRh2Si2 synthesis and not direct contradictions of the validated subgraphs. |

## Priors

Leaf priors were merged from the two validated subgraphs into `src/fermi_liquid_effective_mass/priors.py`. Direct claim priors are capped at 0.90 and every justification retains `TODO:review`.

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 24 knowledge, 6 strategies, 0 operators; IR hash `sha256:7144e2d657d3f46df836592df826be25f55e8dab2778fd7f62ed390417ccd7ab`. |
| `gaia check --brief .` | pass | 8 independent premises with priors, 6 derived conclusions, 10 internal orphaned helper claims. |
| `gaia check --hole .` | pass | 0 holes / 8 independent claims; all direct priors present and capped at 0.90. |
| `gaia infer .` | pass | Inferred 18 beliefs using exact JT; converged after 2 iterations. |

## Friedemann2010 extension synthesis -- 2026-05-03

### Checklist delta

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Incorporated validated extension subgraph `artifacts/subgraphs/ybrh2si2-rbc-hall-gaia`; root evidence file `artifacts/lkm-discovery/input/evidence_gcn_42a4ff7fd004413f.json` was already preserved in the parent input folder. |
| 2. Refine | done | Copied the subgraph's self-contained Friedemann2010 claim text and preserved `lkm_id`, `source_paper`, `provenance_source`, `lkm_original`, and `derived_from_lkm_ids` decomposition metadata. |
| 3. Decompose | done | Preserved the compound root `gcn_42a4ff_rbc_hall_dos_values` and copied its three validated helper claims for RBC parametrization, Hall-product cancellation, and DOS/gamma values. |
| 4. Hunt open problems | done | Compared the Friedemann2010 RBC/Hall/DOS claims to the existing YbRh2Si2 homogeneous-isotropic FCQPT premise; dismissed contradiction because the model scopes can coexist. |
| 5. Mark suspicions | done | Recorded that material-specific band, CEF, DOS, and Hall evidence qualifies the homogeneous isotropic universal-scaling premise. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` passed from the parent package directory. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 10 independent claims; the two new Friedemann2010 leaf priors are capped below 0.90 and marked `TODO:review`. |
| 8. Search/support synthesis | done | Added support-only cross-paper wiring from the RBC root/helpers plus the homogeneous-isotropic premise to a new scope-qualification claim. |
| 9. Repeat/exit rationale | done | Exit condition met for the requested synthesis: no duplicate labels, no promoted contradiction/equivalence, 0 holes, and successful inference. |

### Friedemann2010 claims

| label | lkm id / helper | source paper | action |
|---|---|---|---|
| `gcn_c243dcb_rbc_phase_shift_parametrization` | `gcn_c243dcb58cae4418` | `paper:811773737962569729` | Friedemann2010 RBC phase-shift/CEF parametrization premise copied from validated subgraph. |
| `gcn_48bba377_specific_heat_calibration` | `gcn_48bba377911d4985` | `paper:811773737962569729` | Friedemann2010 specific-heat/DOS calibration premise copied from validated subgraph. |
| `gcn_42a4ff_rbc_hall_dos_values` | `gcn_42a4ff7fd004413f` | `paper:811773737962569729` | Selected extension root copied from validated subgraph and exported. |
| `helper_rbc_parameterization_constrained_by_cef_gamma` | helper | `paper:811773737962569729` | Decomposition helper copied from validated subgraph. |
| `helper_ybrh2si2_opposite_hall_transport_products` | helper | `paper:811773737962569729` | Decomposition helper copied from validated subgraph. |
| `helper_rbc_dos_gamma_ybrh2si2_ybir2si2` | helper | `paper:811773737962569729` | Decomposition helper copied from validated subgraph. |
| `cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope` | synthesis | synthesis | New supported scope-qualification meta-claim, not a leaf prior. |

### Friedemann2010 factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_0b967f9e875749e8` | `paper:811773737962569729` | `gcn_c243dcb_rbc_phase_shift_parametrization`, `gcn_48bba377_specific_heat_calibration` | `gcn_42a4ff_rbc_hall_dos_values` | `deduction` | 0.95 |
| root decomposition | `paper:811773737962569729` | `gcn_42a4ff_rbc_hall_dos_values` | `helper_rbc_parameterization_constrained_by_cef_gamma` | `support` | 0.90 |
| root decomposition | `paper:811773737962569729` | `gcn_42a4ff_rbc_hall_dos_values` | `helper_ybrh2si2_opposite_hall_transport_products` | `support` | 0.90 |
| root decomposition | `paper:811773737962569729` | `gcn_42a4ff_rbc_hall_dos_values` | `helper_rbc_dos_gamma_ybrh2si2_ybir2si2` | `support` | 0.90 |

### Friedemann2010 cross-paper decisions

| item | decision | dsl_action | rationale |
|---|---|---|---|
| Material-specific RBC/Hall/DOS evidence vs homogeneous isotropic FCQPT premise | scope qualification | `support([...], cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope, prior=0.90)` | The Shaginyan premise explicitly omits anisotropy, band topology, multiple bands, and anisotropic effective masses, while Friedemann2010 explicitly supplies CEF/gamma calibration, band-resolved Hall cancellation, and DOS/gamma values for YbRh2Si2. |
| FCQPT model and RBC calculation | dismissed equivalence | no `equivalence()` | The model surfaces address related YbRh2Si2 effective-mass physics but are not the same proposition. |
| FCQPT homogeneous-isotropic premise and RBC material-specific evidence | dismissed contradiction | no `contradiction()` | The two claims can both be true under their stated scopes; the RBC evidence qualifies model scope rather than logically excluding it. |

### Friedemann2010 priors

Merged new leaf priors into `src/fermi_liquid_effective_mass/priors.py` without changing existing priors:

| claim | prior | status |
|---|---|---|
| `gcn_c243dcb_rbc_phase_shift_parametrization` | 0.82 | capped direct claim prior with `TODO:review` |
| `gcn_48bba377_specific_heat_calibration` | 0.76 | capped direct claim prior with `TODO:review` |

### Gaia CLI verification after Friedemann2010 extension

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 38 knowledge, 11 strategies, 0 operators; IR hash `sha256:40777a6dbe1830cf56c3c09691ed7f120267977c7fdd7e8db0329a8195005a75`. |
| `gaia check --brief .` | pass | 10 independent premises with priors, 11 derived conclusions, 17 internal orphaned helper/operator-result claims. |
| `gaia check --hole .` | pass | 0 holes / 10 independent claims; all direct priors present and capped at 0.90. |
| `gaia infer .` | pass | Inferred 27 beliefs using exact JT; converged after 2 iterations. |


## 100-node extension synthesis -- 2026-05-03

### Checklist delta

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Incorporated six validated subgraphs: `ybrh2si2-dhva-mass-gaia`, `lurh2si2-small-fs-reference-gaia`, `kondo-brinkman-rice-gaia`, `mott-entropy-mass-gaia`, `nis2-brinkman-rice-gaia`, and `cemo-kadowaki-wilson-gaia`. Subgraph directories remain unchanged under `artifacts/subgraphs/`. |
| 2. Refine | done | Copied the validated per-paper modules into `src/fermi_liquid_effective_mass/`, preserving `lkm_id`, `source_paper`, `provenance_source`, `lkm_original`, `derived_from_lkm_ids`, and `decomposition_of` metadata. |
| 3. Decompose | done | Preserved every validated helper/decomposition claim from the six subgraphs; no new decomposition rewrites were made during parent synthesis. |
| 4. Hunt open problems | done | Rechecked YbRh2Si2 dHvA/RBC/FCQPT, Kondo/Mott/NiS2 Brinkman-Rice, and CeMo2Si2C thermodynamic/transport interfaces; no same-condition logical contradiction was promoted. |
| 5. Mark suspicions | done | Added support-scoped caution claims for YbRh2Si2 field/method scope, Brinkman-Rice non-equivalence, and CeMo2Si2C ratio-normalization sensitivity. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` passed; final post-duplicate-audit IR hash `sha256:0c8dc1a153a399df924c4300e2a480faaf07e05fa666c49dad4bb19fb2e51b4d`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 23 independent claims; all direct priors retain `TODO:review` and are <= 0.90. |
| 8. Search/support synthesis | done | Added five parent support-backed synthesis claims and no equivalence/contradiction operators. |
| 9. Repeat/exit rationale | done | Final graph has 121 total knowledge nodes (63 science-facing, 58 internal helpers) after duplicate cleanup, above the ~100-node target; stopped without adding more branches. |

### Subgraphs incorporated in this batch

| subgraph | root | source paper | parent action |
|---|---|---|---|
| `artifacts/subgraphs/ybrh2si2-dhva-mass-gaia` | `gcn_c38f8ce989fd454a` | Knebel et al. 2006 | Copied `paper_knebel2006.py`; exported `gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch`; merged two priors and `Knebel2006` reference. |
| `artifacts/subgraphs/lurh2si2-small-fs-reference-gaia` | `gcn_2b8dd97abcb44d53` | Friedemann et al. 2013 | Copied `paper_friedemann2013.py`; exported `gcn_2b8dd97_lurh2si2_reference_reanalysis`; merged three priors and `Friedemann2013` reference. |
| `artifacts/subgraphs/kondo-brinkman-rice-gaia` | `gcn_7ae79f122f1c4fcb` | Anderson 1984 | Copied `paper_anderson1984.py`; exported `gcn_7ae79f_kondo_brinkman_rice_fixed_point`; merged two priors and `Anderson1984` reference. |
| `artifacts/subgraphs/mott-entropy-mass-gaia` | `gcn_e4ecd721edd14d3f` | Capone/Fabrizio/Tosatti 2001 | Copied `paper_capone2001.py`; exported `gcn_e4ecd721edd14d3f`; merged three priors and `Capone2001` reference. |
| `artifacts/subgraphs/nis2-brinkman-rice-gaia` | `gcn_29401e4284574aa2` | Friedemann et al. 2016 | Copied `paper_friedemann2016.py`; exported `gcn_29401e42_nis2_brinkman_rice`; merged one prior and `Friedemann2016` reference. |
| `artifacts/subgraphs/cemo-kadowaki-wilson-gaia` | `gcn_bc46d7d5f5284a0e` | Paramanik et al. 2013 | Copied `paper_paramanik2013.py`; exported `gcn_bc46d7_cemo_kw_wilson_fl_consistency`; merged two priors and `Paramanik2013` reference. |

### Cross-paper decisions

| item | decision | dsl_action | rationale |
|---|---|---|---|
| YbRh2Si2 RBC/Hall/DOS + high-field dHvA + LuRh2Si2 reference | material-specific constraint synthesis | `support([...], cross_ybrh2si2_material_specific_fs_constraints, prior=0.88)` | All three branches constrain YbRh2Si2 Fermi-surface/effective-mass interpretation, but the methods and fields differ. |
| YbRh2Si2 high-field/method caveats vs homogeneous FCQPT scope | scope caution | `support([...], cross_ybrh2si2_field_method_scope_caution, prior=0.90)` | High-field dHvA, LDA sensitivity, harmonic reassignment, small-FS reference, and homogeneous isotropic modeling can coexist under scoped conditions. |
| Anderson Kondo BR + Capone Mott entropy + NiS2 BR | thematic support | `support([...], cross_brinkman_rice_mott_boundary_family, prior=0.86)` | The branches share heavy-quasiparticle/Mott-boundary vocabulary but are not the same claim. |
| Anderson/Capone/NiS2 BR surfaces | non-equivalence caution | `support([...], cross_brinkman_rice_scope_caution, prior=0.89)` | Kondo-lattice fixed point, entropy obstruction, and NiS2 pressure-tuned quantum oscillations have distinct mechanisms and conditions. |
| CeMo2Si2C KW/Wilson ratios + thermodynamic effective-mass routes | correlated-FL phenomenology support | `support([...], cross_thermo_transport_correlated_fl_consistency, prior=0.84)` | CeMo2Si2C adds transport/susceptibility consistency checks complementary to gamma, S/T, and DOS/gamma thermodynamic routes. |

### Dismissed non-equivalences and false contradictions

| pair_or_flag | origin | decision | rationale |
|---|---|---|---|
| YbRh2Si2 dHvA high-field spectrum vs low-field/QCP FCQPT branch | Knebel2006 audit + parent context | no contradiction | The dHvA measurements are 12-28 T high-field constraints; FCQPT branch is a homogeneous universal-scaling model. |
| Itinerant-4f LDA mismatch vs Friedemann2010 RBC | Knebel2006 audit | no contradiction | LDA/FLAPW mismatch and thermodynamically calibrated RBC are different modeling surfaces. |
| Friedemann2013 14 kT inference vs RBC/Hall branch | Friedemann2013 audit | no contradiction/equivalence | Small-FS reference and harmonic reassignment constrain high-field YbRh2Si2 interpretation, not the same proposition as RBC Hall/DOS values. |
| Anderson Kondo-lattice Brinkman-Rice vs Shaginyan FCQPT | Anderson1984 audit | no contradiction | Finite Stoner enhancement and FCQPT effective-mass criticality involve different quantities/regimes. |
| Capone entropy obstruction vs NiS2 pressure-metalized heavy FL | Capone2001 and NiS2 audits | no contradiction | Capone addresses a conditional FL-to-singlet-Mott transition; NiS2 reports a correlated metal near a Mott boundary. |
| NiS2 BR interpretation vs named alternatives | NiS2 audit | not promoted | Alternative mechanisms are not independently established by a second selected root; reflected by low prior on the exclusion premise. |
| CeMo2Si2C KW original scale vs degeneracy-scaled caution | CeMo2Si2C audit | no contradiction | The source itself quotes both normalization contexts; the issue is convention/material sensitivity. |

### Gaia CLI verification after 100-node synthesis

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 121 knowledge, 40 strategies, 0 operators; final post-duplicate-audit IR hash `sha256:0c8dc1a153a399df924c4300e2a480faaf07e05fa666c49dad4bb19fb2e51b4d`. |
| `gaia check --brief .` | pass | 23 independent premises with priors, 40 derived conclusions, 58 internal helper claims. |
| `gaia check --hole .` | pass | 0 holes / 23 independent claims. |
| `gaia infer .` | pass | Inferred 81 beliefs using exact JT; converged after 2 iterations. |
| `gaia render . --target github` | pass | Refreshed `.github-output/README.md`; generated overview graph preserved in `README.md`. |
| `gaia render . --target docs` | pass | Refreshed `docs/detailed-reasoning.md`. |
