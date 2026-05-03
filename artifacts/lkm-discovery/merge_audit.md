# Merge audit

No formal Gaia merge decisions have been made yet. The discovery pass found no exact contradiction or equivalence pairs among the chain-backed candidates.

## Final synthesis pass

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| He-3 subgraph package and YbRh2Si2 subgraph package | incorporated without rewriting audited intermediates | The validated subgraphs are preserved under `artifacts/subgraphs/`; the parent package copies their source-level claims into a combined namespace. | Created parent `src/fermi_liquid_effective_mass/` modules. |
| `gcn_800070efac5e476d` / `gcn_2741cdef209a457a` | no exact merge | The roots share the broad topic of effective-mass reasoning but differ by material, observable, and model scope. | Kept both selected roots exported. |
| He-3 `gamma -> m*/m` / YbRh2Si2 `S/T -> M*(T,B)` | support to scoped meta-claim, not equivalence | Both are thermodynamic operational routes to effective mass, but not the same proposition. | Added `cross_thermodynamic_routes_to_effective_mass` supported by both subgraph claims. |
| He-3 standard Landau mapping / YbRh2Si2 FCQPT crossover scheme | keep distinct with scope caution | The distinction is important for avoiding a false equivalence or false contradiction. | Added `cross_scope_caution_standard_fl_vs_fcqpt` as a supported synthesis caution. |

No exact merges were made in the final synthesis pass.

## Friedemann2010 extension synthesis pass

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| `artifacts/subgraphs/ybrh2si2-rbc-hall-gaia` | incorporated without rewriting audited intermediate | The validated extension subgraph is preserved under `artifacts/subgraphs/`; the parent package copies its source-level claims into the combined namespace. | Added parent `paper_friedemann2010.py` and imported it from `__init__.py`. |
| `gcn_c243dcb58cae4418` / `gcn_48bba377911d4985` | keep distinct | The first claim states the RBC phase-shift/CEF parametrization; the second states the specific-heat/DOS calibration and reliability proposition. They are complementary premises, not duplicates. | Kept both leaf claims and merged their capped direct priors. |
| `gcn_42a4ff7fd004413f` root components | decompose without merging | The root is compound but the method, Hall-products, and DOS/gamma components are anchored parts of the same selected LKM root rather than independent duplicate claims. | Preserved the root and copied helper claims downstream via `support([root], helper, prior=0.90)`. |
| `gcn_03614e9b_homogeneous_isotropic_model` / Friedemann2010 RBC-Hall-DOS evidence | scope qualification, not contradiction | A homogeneous isotropic FCQPT scaling approximation and a material-specific RBC/Hall/DOS calculation can both be true; the latter qualifies the former's scope by recording details the approximation omits. | Added `cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope` with support from the FCQPT premise and RBC root/helpers. |
| YbRh2Si2 FCQPT scheme / Friedemann2010 RBC calculation | no equivalence | Both address YbRh2Si2 heavy-electron effective-mass physics, but one is a universal-scaling FCQPT procedure and the other is a material-specific renormalized-band/Hall/DOS calculation. | No `equivalence()` emitted. |

No exact merges were made in the Friedemann2010 extension synthesis pass.


## 100-node extension synthesis pass -- 2026-05-03

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| Six validated subgraphs requested by parent | incorporated without rewriting audited intermediates | Each subgraph already passed compile/check-hole/infer and remains unchanged under `artifacts/subgraphs/`. | Copied validated per-paper modules into `src/fermi_liquid_effective_mass/`; merged references and priors. |
| Knebel2006 dHvA / Friedemann2010 RBC / Friedemann2013 LuRh2Si2 reference | scoped support, not equivalence | All constrain YbRh2Si2 Fermi-surface/effective-mass interpretation, but differ by field window, model, observable, and reference construction. | Added `cross_ybrh2si2_material_specific_fs_constraints` and `cross_ybrh2si2_field_method_scope_caution`. |
| Shaginyan2010 homogeneous FCQPT / YbRh2Si2 material-specific dHvA-RBC-Lu evidence | scope qualification, not contradiction | The homogeneous model deliberately omits band/lattice detail; the material-specific branches add those details without asserting same-condition incompatibility. | Kept existing RBC scope claim and added field/method scope caution. |
| Anderson1984 / Capone2001 / Friedemann2016 NiS2 Brinkman-Rice branches | thematic synthesis plus non-equivalence caution | All involve heavy quasiparticles or suppressed Z near Mott/local-moment physics, but one is Kondo-lattice, one is a conditional entropy argument, and one is NiS2 quantum-oscillation phenomenology. | Added `cross_brinkman_rice_mott_boundary_family` and `cross_brinkman_rice_scope_caution`. |
| Paramanik2013 CeMo2Si2C KW/Wilson / existing thermodynamic routes | correlated-FL consistency support | CeMo2Si2C supplies ratio-based transport/susceptibility checks complementary to gamma, S/T, and DOS/gamma effective-mass reasoning. | Added `cross_thermo_transport_correlated_fl_consistency`. |
| Cross-material heavy-FL vocabulary | no exact merge | Similar vocabulary (`heavy quasiparticles`, `large FS`, `effective mass`) occurs under different materials/mechanisms and must not inflate confidence through equivalence. | No `equivalence()` emitted. |
| Potential contradictions across different materials or field regimes | dismissed | No two admitted claims assert mutually exclusive values for the same material, observable, and conditions. | No `contradiction()` emitted. |

No exact merges were made in the 100-node extension synthesis pass.

## Duplicate audit pass -- 2026-05-03

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| `__conjunction_result_c6626be2` / `__conjunction_result_26617e05` | internal helper duplicate | `gaia inquiry review --strict` reported one possible duplicate, but both nodes are compiler-generated formal helper claims rather than science-facing claims. | No source-level merge applied; logged as generated-helper duplicate. |
| `gcn_c131e014_ybrh2si2_midband_harmonic_assignment` / `helper_ybrh2si2_5_7kt_peaks_are_harmonics` | auto-merge into canonical science claim | Same Friedemann2013 proposition: 5-7 kT YbRh2Si2 peaks are harmonics of lower-frequency branches, not independent fundamentals. | Removed helper claim and support strategy; replaced cross-paper uses with `gcn_c131e014_ybrh2si2_midband_harmonic_assignment`. |
| `gcn_3dc248d_ybrh2si2_14kt_not_small_fs` / `helper_14kt_orbit_supports_high_field_itinerant_4f` | auto-merge into canonical science claim | Same Friedemann2013 proposition: absence of a 14 kT orbit in the refined small-FS calculation supports high-field itinerant Yb 4f participation. | Removed helper claim and support strategy; replaced cross-paper uses with `gcn_3dc248d_ybrh2si2_14kt_not_small_fs`. |
| `gcn_31bc66ca16a44508` / `capone_fl_entropy_order_unity_at_tk` | auto-merge into canonical science claim | Same Capone2001 proposition: `S(T)/N ~ T/T_K`, so `S(T_K)` is finite and order unity for nonzero `T_K`. | Removed helper claim and deduction; replaced cross-paper uses with `gcn_31bc66ca16a44508`. |
| `gcn_dd12256615264dfb` / `capone_entropy_mismatch_requires_instability` | auto-merge into canonical science claim | Same Capone2001 proposition: fixed chemical potential, no symmetry breaking, and a singlet-Mott endpoint require an instability or intermediate phase to remove finite FL entropy. | Removed helper claim and deduction; replaced cross-paper uses with `gcn_dd12256615264dfb`. |
| `gcn_795699f572b24ed5` / `capone_luttinger_pinning_blocks_band_edge_route` | keep distinct | The helper is a derived consequence emphasizing the blocked band-edge escape route, while the canonical premise includes spectral-density pinning and resonance narrowing. | No edit. |
| `gcn_1587257a956f4d18` / `gcn_800070efac5e476d` | ambiguous, default keep | Both touch the He-3 numeric mapping, but one is the mapping premise and the other is the selected root conclusion tied to the measured gamma and inferred `F1`. | Logged; no edit; not added to `merge_decisions.todo` because the default keep does not undermine the graph. |
| YbRh2Si2 FCQPT / RBC / dHvA / LuRh2Si2-reference branches | keep distinct | They constrain related YbRh2Si2 effective-mass/Fermi-surface physics but differ by model, field regime, observable, and reference construction. | No equivalence or merge. |
| Brinkman-Rice / Mott / Kondo / NiS2 branches | keep distinct | The branches share heavy-quasiparticle and Mott-boundary vocabulary but differ by material, mechanism, and assumptions. | No equivalence or merge. |
| Thermodynamic / transport / He-3 / CeMo2Si2C branches | keep distinct | Gamma, S/T, DOS/gamma, Kadowaki-Woods, and Wilson ratios are related thermodynamic/transport diagnostics, not duplicate propositions. | No equivalence or merge. |
