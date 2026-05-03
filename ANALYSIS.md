# Analysis

## Verification

The package was compiled, checked, inferred, and rendered after the 100-node synthesis:

```bash
gaia compile .
gaia check --brief .
gaia check --hole .
gaia infer .
gaia render . --target github
gaia render . --target docs
gaia starmap . --out docs/starmap.html
```

Results:

- `gaia compile .`: passed, `121 knowledge`, `40 strategies`, `0 operators`; IR hash `sha256:0c8dc1a153a399df924c4300e2a480faaf07e05fa666c49dad4bb19fb2e51b4d`.
- `gaia check --brief .`: passed, `23` independent premises, `40` derived conclusions, `58` internal orphaned strategy-helper claims.
- `gaia check --hole .`: passed, `0 holes / 23 independent claims`.
- `gaia infer .`: passed with exact junction-tree inference; `81` beliefs inferred and convergence after `2` iterations.
- `gaia render . --target github`: passed and refreshed `.github-output/README.md`.
- `gaia render . --target docs`: passed and refreshed `docs/detailed-reasoning.md`.
- `gaia starmap . --out docs/starmap.html`: passed using Gaia branch `feat/starmap_rsw`, producing an interactive single-file starmap with `103` rendered nodes and `132` edges.

## Node Counts

| Count | Value | Definition |
|---|---:|---|
| Total knowledge nodes | 121 | All entries in `.gaia/ir.json` `knowledges`. |
| Science-facing claims | 63 | Non-internal claims declared by source modules. |
| Internal helper claims | 58 | Compiler-generated `__conjunction_result_*` and `__implication_result_*` helper claims. |
| Strategies | 40 | Source-level deduction/support strategies. |
| Operators | 0 | No equivalence or contradiction operators were promoted. |

The graph remains above the requested ~100-node target after duplicate cleanup, so no additional branch was added.

## Exported Conclusions

| Label | Belief | Notes |
|---|---:|---|
| `gcn_800070efac5e476d` | 0.80 | He-3 heat-capacity route to `m*/m` and `F1`. |
| `gcn_2741cdef_practical_effective_mass_scheme` | 0.59 | YbRh2Si2 homogeneous FCQPT Landau/entropy route to `M*(T,B)`. |
| `gcn_42a4ff_rbc_hall_dos_values` | 0.80 | YbRh2Si2 material-specific RBC/Hall/DOS evidence. |
| `gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch` | 0.81 | YbRh2Si2 high-field dHvA frequencies, masses, and itinerant-4f LDA mismatch. |
| `gcn_2b8dd97_lurh2si2_reference_reanalysis` | 0.73 | LuRh2Si2 small-FS reference reanalysis of YbRh2Si2 dHvA peaks. |
| `gcn_7ae79f_kondo_brinkman_rice_fixed_point` | 0.77 | Anderson Kondo-lattice Brinkman-Rice fixed point. |
| `gcn_e4ecd721edd14d3f` | 0.74 | Capone-Fabrizio-Tosatti Brinkman-Rice/Mott entropy obstruction. |
| `gcn_29401e42_nis2_brinkman_rice` | 0.77 | NiS2 large-FS + `m*=6(2)m_e` Brinkman-Rice consistency claim. |
| `gcn_bc46d7_cemo_kw_wilson_fl_consistency` | 0.79 | CeMo2Si2C KW/Wilson correlated-FL consistency. |
| `cross_thermodynamic_routes_to_effective_mass` | 0.77 | Scoped thermodynamic routes to effective mass. |
| `cross_scope_caution_standard_fl_vs_fcqpt` | 0.64 | Guardrail against merging standard FL and FCQPT/crossover reasoning. |
| `cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope` | 0.71 | RBC evidence qualifies the homogeneous YbRh2Si2 model scope. |
| `cross_ybrh2si2_material_specific_fs_constraints` | 0.67 | RBC, high-field dHvA, and LuRh2Si2 small-FS reference jointly constrain YbRh2Si2. |
| `cross_ybrh2si2_field_method_scope_caution` | 0.62 | Field/method caution for YbRh2Si2 branches. |
| `cross_brinkman_rice_mott_boundary_family` | 0.68 | Kondo, Mott entropy, and NiS2 roots form a scoped Mott-boundary theme. |
| `cross_brinkman_rice_scope_caution` | 0.66 | Guardrail against equating the Brinkman-Rice-related roots. |
| `cross_thermo_transport_correlated_fl_consistency` | 0.65 | CeMo2Si2C ratios extend thermodynamic effective-mass reasoning into transport/susceptibility phenomenology. |

## Priors And Holes

All independent leaves have priors in `src/fermi_liquid_effective_mass/priors.py`. Direct claim priors remain capped at `0.90`; every justification retains `TODO:review`. The weakest prior is `gcn_8a1a2748_alternative_mechanisms_assumption` at `0.58`, reflecting that alternative mechanisms for the NiS2 observations are not independently ruled out by that root JSON.

## Audit Notes

The final graph incorporates six newly validated subgraphs without editing their directories under `artifacts/subgraphs/`. No cross-material equivalence or contradiction was forced. The synthesis uses support-scoped claims and explicit scope cautions for YbRh2Si2 field/method differences, Kondo-vs-Mott-vs-NiS2 Brinkman-Rice usage, and CeMo2Si2C ratio phenomenology.

## Duplicate Audit

The Turn-3 duplicate audit found no exact duplicate science-facing claim content. Four same-paper helper restatements were merged into their canonical science claims:

- Friedemann2013 5-7 kT harmonic helper -> `gcn_c131e014_ybrh2si2_midband_harmonic_assignment`
- Friedemann2013 14 kT high-field itinerant-4f helper -> `gcn_3dc248d_ybrh2si2_14kt_not_small_fs`
- Capone2001 entropy-at-`T_K` helper -> `gcn_31bc66ca16a44508`
- Capone2001 entropy-mismatch-instability helper -> `gcn_dd12256615264dfb`

The only remaining duplicate reported by `gaia inquiry review --strict` is between compiler-generated internal helper claims, not source science claims.

## Bridge Search

The interactive starmap has two clusters: a thermodynamic/YbRh2Si2 material-specific cluster and a Brinkman-Rice/Mott-boundary cluster. A focused LKM bridge search was run after duplicate cleanup to look for a chain-backed claim that could connect them without an agent-only synthesis bridge.

No suitable bridge root was found. The top chain-backed bridge-adjacent candidates stayed on the YbRh2Si2 side: FCQPT effective-mass scaling, high-field Kondo suppression/Lifshitz phenomenology, and lattice-Kondo coherence. The only strict-filter candidate was already present as the NiS2 alternative-mechanisms premise. The decision is therefore to keep the graph disconnected rather than add a weak bridge. Details are logged in `artifacts/lkm-discovery/bridge_search_2026-05-03.md`.
