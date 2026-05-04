# Semantic label audit -- fermi-liquid-effective-mass-gaia

Purpose: presentation-only node-label conversion on 2026-05-04. Scientific claim strings, graph logic, priors, LKM IDs, `lkm_original`, `source_paper`, `provenance_source`, `derived_from_lkm_ids`, and raw evidence artifacts were not changed.

## Science-facing claim labels

| old label | new label | rationale |
|---|---|---|
| `gcn_677c6c_landau_integral_relation` | `landau_mass_integral_relation` | Landau effective-mass integral relation defining M*(T). |
| `gcn_03614e9b_homogeneous_isotropic_model` | `homogeneous_isotropic_heavy_liquid_model` | Homogeneous isotropic heavy-electron model assumption. |
| `gcn_e0c364ff_inflection_fcqpt_condition` | `fcqpt_inflection_critical_condition` | FCQPT condition from vanishing first and second derivatives at p_F. |
| `gcn_6bbfeb95_stable_landau_solutions` | `stable_landau_numerical_solutions` | Stable numerical solutions of the Landau equation. |
| `gcn_ecddfefa_fermion_entropy_formula` | `fermion_entropy_formula` | Fermi-Dirac quasiparticle entropy formula. |
| `gcn_2e693115_entropy_over_temperature_mass` | `entropy_over_temperature_mass_proxy` | Operational M*(T,B)=S/T mass proxy. |
| `gcn_2741cdef_practical_effective_mass_scheme` | `ybrh2si2_entropy_effective_mass_scheme` | YbRh2Si2 practical effective-mass scheme from Landau solution and entropy. |
| `gcn_f82c178_fcqpt_inflection_cubic_spectrum` | `fcqpt_cubic_spectrum_condition` | FCQPT cubic leading spectrum condition. |
| `gcn_58746c_fcqpt_homogeneous_mass_equation` | `fcqpt_homogeneous_mass_equation` | Homogeneous FCQPT mass equation leading to T^(-2/3). |
| `gcn_45f24d_fcqpt_t_minus_two_thirds` | `fcqpt_t_minus_two_thirds_mass_scaling` | FCQPT T^(-2/3) effective-mass scaling. |
| `gcn_c243dcb_rbc_phase_shift_parametrization` | `rbc_phase_shift_parametrization` | Renormalized-band phase-shift parametrization. |
| `gcn_48bba377_specific_heat_calibration` | `rbc_specific_heat_calibration` | Specific-heat calibration of the RBC resonance-width parameter. |
| `gcn_42a4ff_rbc_hall_dos_values` | `ybrh2si2_rbc_hall_dos_gamma_values` | YbRh2Si2 RBC Hall cancellation plus DOS/gamma values. |
| `gcn_5501e18a_high_field_dhva_scope` | `ybrh2si2_high_field_dhva_scope` | High-field dHvA scope caution for YbRh2Si2. |
| `gcn_f20b1f42_itinerant_4f_lda_sensitivity` | `ybrh2si2_itinerant_4f_lda_sensitivity` | Itinerant-4f LDA sensitivity caution. |
| `gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch` | `ybrh2si2_dhva_spectrum_lda_mismatch` | YbRh2Si2 dHvA frequencies/masses and LDA mismatch. |
| `gcn_c131e014_ybrh2si2_midband_harmonic_assignment` | `ybrh2si2_midband_harmonic_assignment` | Mid-band dHvA peaks assigned as harmonics. |
| `gcn_3dc248d_ybrh2si2_14kt_not_small_fs` | `ybrh2si2_14kt_orbit_not_small_fs` | 14 kT orbit absent from the small-FS calculation. |
| `gcn_3a8394c_lurh2si2_small_fs_reference` | `lurh2si2_small_fs_reference` | LuRh2Si2 as the small-FS reference for YbRh2Si2. |
| `gcn_2b8dd97_lurh2si2_reference_reanalysis` | `ybrh2si2_lurh2si2_reference_reanalysis` | YbRh2Si2 dHvA reanalysis using the LuRh2Si2 reference. |
| `gcn_021fb1_high_field_a_gamma_scaling_assumption` | `high_field_a_gamma_scaling_assumption` | High-field use of A proportional to gamma^2 scaling. |
| `gcn_24ebf8_ybrh2si2_t2_resistivity_fit_reliability` | `ybrh2si2_t2_resistivity_fit_reliability` | Reliability of T^2 resistivity fits for A(B). |
| `gcn_b4093_ybrh2si2_resistivity_mass_drop` | `ybrh2si2_resistivity_mass_drop` | Step-like effective-mass drop from A(B) across B*. |
| `gcn_fb2747_ybrh2si2_tp_tcoh_ratio` | `ybrh2si2_tp_tcoh_ratio` | T_P/T_coh numerical hierarchy in stoichiometric YbRh2Si2. |
| `gcn_3a1514_ybrh2si2_kondo_lattice_hierarchy` | `ybrh2si2_kondo_lattice_hierarchy` | Kondo-lattice coherence hierarchy in YbRh2Si2. |
| `gcn_a76225_ybrh2si2_esr_collective_mode_assumption` | `ybrh2si2_esr_collective_mode_assumption` | Assumption identifying ESR as a heavy-quasiparticle collective mode. |
| `gcn_d8b1_ybrh2si2_esr_heavy_quasiparticles` | `ybrh2si2_esr_heavy_quasiparticles` | ESR evidence for coherent heavy quasiparticles. |
| `gcn_dbe6ec_ybrh2si2_cef_anisotropic_hybridization` | `ybrh2si2_cef_anisotropic_hybridization` | CEF-induced anisotropic hybridization and g-factor anisotropy. |
| `gcn_faee88_ybrh2si2_smooth_kondo_mass_suppression` | `ybrh2si2_smooth_kondo_mass_suppression` | Smooth field suppression of Kondo screening and m*(B). |
| `gcn_8f49e0_periodic_kondo_lattice_lifshitz_dos` | `periodic_kondo_lattice_lifshitz_dos` | Periodic Kondo-lattice DOS features causing Lifshitz transitions. |
| `gcn_4d206_ybrh2si2_kondo_lifshitz_interplay` | `ybrh2si2_kondo_lifshitz_interplay` | YbRh2Si2 high-field Kondo suppression and Lifshitz interplay. |
| `gcn_6ca2b_ybrh2si2_hall_compensation_scenario` | `ybrh2si2_hall_compensation_scenario` | Multiband Hall compensation scenario near B2. |
| `gcn_3ba45e_ybrh2si2_thermopower_corrob_lifshitz` | `ybrh2si2_thermopower_lifshitz_corroboration` | Thermopower anomalies corroborating Lifshitz-type electronic-structure changes. |
| `gcn_b5d9_ybrh2si2_lifshitz_derenormalization` | `ybrh2si2_lifshitz_derenormalization` | Coexisting Lifshitz transitions and smooth Kondo de-renormalization. |
| `gcn_848945_ybrh2si2_lusmall_fs_lda_assumption` | `ybrh2si2_lusmall_fs_lda_assumption` | LuRh2Si2 LDA topology as a small-FS guide for YbRh2Si2. |
| `gcn_5090f8_dhva_orbit_assignment_reliability` | `dhva_orbit_assignment_reliability` | Reliability assumptions for assigning dHvA branches to calculated orbits. |
| `gcn_d10f91_ybrh2si2_small_fs_mass_enhancement` | `ybrh2si2_small_fs_mass_enhancement` | Small-FS dHvA match with order-ten mass enhancement. |
| `gcn_b01616_ybrh2si2_lda_inadequate_dynamic_correlations` | `ybrh2si2_lda_missing_dynamic_correlations` | Static LDA missing dynamic correlations and Kondo renormalization. |
| `gcn_34ce9_ybrh2si2_many_body_methods_required` | `ybrh2si2_many_body_methods_required` | Many-body methods required for quantitative YbRh2Si2 mass/FS modeling. |

## Deduction strategy labels

These strategy variables were renamed to avoid displaying raw `gfac_*` fragments in rendered strategy nodes. Factor IDs remain preserved in `mapping_audit.md` and in raw LKM JSON.

| old label | new label | rationale |
|---|---|---|
| `strat_gfac_749b6767459b4785_effective_mass_scheme` | `derive_ybrh2si2_entropy_effective_mass_scheme` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_3874d7c0b7a44408_fcqpt_t_scaling` | `derive_fcqpt_t_minus_two_thirds_mass_scaling` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_0b967f9e875749e8_rbc_hall_dos` | `derive_ybrh2si2_rbc_hall_dos_gamma_values` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_5648470e5459468a_dhva_mass_lda_mismatch` | `derive_ybrh2si2_dhva_spectrum_lda_mismatch` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_468a4122_lurh2si2_reference_reanalysis` | `derive_ybrh2si2_lurh2si2_reference_reanalysis` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_d438ed7a0cad4d2e_ybrh2si2_mass_drop` | `derive_ybrh2si2_resistivity_mass_drop` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_717602aa489047e9_kondo_hierarchy` | `derive_ybrh2si2_kondo_lattice_hierarchy` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_44921f1b7d4e4c4a_esr_heavy_qp` | `derive_ybrh2si2_esr_heavy_quasiparticles` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_a3846efd68654c47_kondo_lifshitz_interplay` | `derive_ybrh2si2_kondo_lifshitz_interplay` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_3419693df9e1427e_lifshitz_derenorm` | `derive_ybrh2si2_lifshitz_derenormalization` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_7960d27e3ad54880_small_fs_mass_enhancement` | `derive_ybrh2si2_small_fs_mass_enhancement` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_9d14afa95eda494a_many_body_methods` | `derive_ybrh2si2_many_body_methods_required` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |

## Labels intentionally left unchanged

- `helper_*` decomposition labels were already semantic and are direct LKM-backed/decomposition claims, so they were left unchanged.
- `sx_*`, `eq_*`, and `strat_decompose_*` operator labels were already semantic and were left unchanged.
- Compiler-generated internal `.gaia` helper labels such as `__conjunction_result_*` and `__implication_result_*` are regenerated by Gaia and were not manually renamed.
