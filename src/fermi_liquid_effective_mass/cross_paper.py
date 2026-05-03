"""cross_paper -- cautious synthesis across the selected LKM roots."""

from gaia.lang import claim, support

from .paper_alvesalo1979 import (
    gcn_1587257a956f4d18,
    gcn_800070efac5e476d,
    he3_gamma_implies_mstar_ratio_2_12,
)
from .paper_anderson1984 import (
    gcn_7ae79f_kondo_brinkman_rice_fixed_point,
    gcn_8f275a_brinkman_rice_scope_condition,
    helper_brinkman_rice_finite_stoner_enhancement,
    helper_brinkman_rice_large_mass_renormalization,
    helper_kondo_lattice_screened_heavy_quasiparticles,
)
from .paper_capone2001 import (
    capone_brinkman_rice_mass_z_tk_limit,
    gcn_e4ecd721edd14d3f,
    gcn_31bc66ca16a44508,
    gcn_dd12256615264dfb,
)
from .paper_friedemann2010 import (
    gcn_42a4ff_rbc_hall_dos_values,
    helper_rbc_dos_gamma_ybrh2si2_ybir2si2,
    helper_rbc_parameterization_constrained_by_cef_gamma,
    helper_ybrh2si2_opposite_hall_transport_products,
)
from .paper_friedemann2013 import (
    gcn_2b8dd97_lurh2si2_reference_reanalysis,
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs,
    gcn_3a8394c_lurh2si2_small_fs_reference,
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment,
    helper_ybrh2si2_reduced_fundamental_set,
)
from .paper_friedemann2016 import (
    gcn_29401e42_nis2_brinkman_rice,
    helper_brinkman_rice_large_fs_heavy_quasiparticles,
    helper_nis2_large_fs_603kt_belly_orbit,
    helper_nis2_mstar_6_me,
)
from .paper_knebel2006 import (
    gcn_5501e18a_high_field_dhva_scope,
    gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch,
    gcn_f20b1f42_itinerant_4f_lda_sensitivity,
    helper_dhva_angular_dependence_itinerant_lda_mismatch,
    helper_dhva_first_fs_information_scope,
    helper_dhva_frequencies_masses_h_parallel_a,
)
from .paper_paramanik2013 import (
    gcn_bc46d7_cemo_kw_wilson_fl_consistency,
    helper_cemo_kw_ratio_original_scale,
    helper_cemo_ratio_consistency_correlated_fl,
    helper_cemo_wilson_ratio_dual_reference,
)
from .paper_shaginyan2010 import (
    gcn_03614e9b_homogeneous_isotropic_model,
    gcn_2741cdef_practical_effective_mass_scheme,
    gcn_2e693115_entropy_over_temperature_mass,
)


cross_thermodynamic_routes_to_effective_mass = claim(
    "Across the He-3 and Shaginyan YbRh2Si2 roots, low-energy thermodynamic "
    "quantities are used as operational routes to quasiparticle effective mass: "
    "Alvesalo et al. infer m*/m for liquid He-3 from the linear specific-heat "
    "coefficient gamma, while Shaginyan et al. extract M*(T,B) for YbRh2Si2 "
    "from S(T,B)/T within their heavy-electron Landau/FCQPT scheme.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_800070efac5e476d",
        "gcn_2e69311592b04bcb",
        "gcn_2741cdef209a457a",
    ],
)

cross_scope_caution_standard_fl_vs_fcqpt = claim(
    "The He-3 and YbRh2Si2 effective-mass routes should not be treated as equivalent "
    "claims: the He-3 chain uses a standard low-temperature Landau Fermi-liquid "
    "mapping from gamma to m*/m, whereas the YbRh2Si2 chain uses a homogeneous "
    "isotropic heavy-electron model near FCQPT and applies S/T as an operational "
    "effective-mass measure through crossover or non-Fermi-liquid regimes.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_1587257a956f4d18",
        "gcn_03614e9b5933496a",
        "gcn_2e69311592b04bcb",
    ],
)

cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope = claim(
    "Material-specific YbRh2Si2 renormalized-band evidence from Friedemann et al. "
    "qualifies, rather than refutes, the homogeneous isotropic FCQPT premise in "
    "the Shaginyan et al. branch: the FCQPT premise is a universal-scaling "
    "approximation that deliberately omits lattice anisotropy, band topology, "
    "multiple bands, CEF splitting, and band-resolved Hall cancellations, while "
    "the RBC/Hall/DOS chain supplies those omitted material-specific details for "
    "YbRh2Si2.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_03614e9b5933496a",
        "gcn_42a4ff7fd004413f",
        "gcn_c243dcb58cae4418",
        "gcn_48bba377911d4985",
    ],
)

cross_ybrh2si2_material_specific_fs_constraints = claim(
    "Within YbRh2Si2, Friedemann 2010 RBC/Hall/DOS evidence, Knebel 2006 "
    "high-field dHvA frequencies and cyclotron masses, and Friedemann 2013 "
    "LuRh2Si2 small-Fermi-surface reanalysis jointly constrain the material-specific "
    "Fermi-surface/effective-mass picture. The synthesis is a field- and "
    "method-scoped constraint claim, not an equivalence among RBC, high-field dHvA, "
    "and homogeneous FCQPT descriptions.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_42a4ff7fd004413f",
        "gcn_c38f8ce989fd454a",
        "gcn_2b8dd97abcb44d53",
        "gcn_3a8394c769864f01",
    ],
)

cross_ybrh2si2_field_method_scope_caution = claim(
    "The YbRh2Si2 material-specific evidence should be read with field and method "
    "scope intact: Knebel dHvA uses 12-28 T fields and reports an itinerant-4f LDA "
    "mismatch, Friedemann 2013 reassigns published mid-band peaks using a LuRh2Si2 "
    "small-FS reference, and Friedemann 2010 RBC uses thermodynamically calibrated "
    "renormalized bands. These branches qualify low-field/QCP and homogeneous "
    "isotropic claims without creating a same-condition contradiction.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_5501e18a04cc458e",
        "gcn_f20b1f42f35548fb",
        "gcn_2b8dd97abcb44d53",
        "gcn_03614e9b5933496a",
    ],
)

cross_brinkman_rice_mott_boundary_family = claim(
    "The Anderson Kondo-lattice Brinkman-Rice fixed point, the Capone-Fabrizio-Tosatti "
    "Mott entropy/Z/T_K boundary argument, and the Friedemann NiS2 large-FS plus "
    "m*=6(2)m_e result form a coherent Mott-boundary/heavy-quasiparticle theme: "
    "large effective mass or suppressed Z appears near a local-moment or Mott "
    "instability while Fermi-liquid coherence remains central to the claim.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_7ae79f122f1c4fcb",
        "gcn_e4ecd721edd14d3f",
        "gcn_29401e4284574aa2",
    ],
)

cross_brinkman_rice_scope_caution = claim(
    "The Brinkman-Rice-related branches are not interchangeable: Anderson 1984 "
    "addresses a screened Kondo-lattice fixed point with finite Stoner enhancement, "
    "Capone-Fabrizio-Tosatti 2001 gives a conditional entropy obstruction for a "
    "direct Fermi-liquid to singlet-Mott crossover, and Friedemann 2016 reports "
    "NiS2 pressure-tuned quantum-oscillation evidence consistent with Brinkman-Rice "
    "large-Fermi-surface heavy quasiparticles.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_7ae79f122f1c4fcb",
        "gcn_e4ecd721edd14d3f",
        "gcn_29401e4284574aa2",
    ],
)

cross_thermo_transport_correlated_fl_consistency = claim(
    "CeMo2Si2C Kadowaki-Woods and Wilson/Sommerfeld ratios extend the package's "
    "thermodynamic effective-mass theme into transport and susceptibility "
    "phenomenology: low-temperature A/gamma^2 and R_W values are used as correlated "
    "Fermi-liquid consistency checks, complementary to He-3 gamma-based mass "
    "extraction and YbRh2Si2 thermodynamic/RBC effective-mass constraints.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_bc46d7d5f5284a0e",
        "gcn_800070efac5e476d",
        "gcn_2e69311592b04bcb",
        "gcn_42a4ff7fd004413f",
    ],
)

strat_cross_he3_ybrh2si2_thermodynamic_routes = support(
    [he3_gamma_implies_mstar_ratio_2_12, gcn_2e693115_entropy_over_temperature_mass],
    cross_thermodynamic_routes_to_effective_mass,
    reason=(
        "The He-3 decomposition explicitly grounds gamma -> m*/m, and the YbRh2Si2 "
        "premise explicitly grounds S(T,B)/T -> M*(T,B). Together they support only "
        "the scoped meta-claim that both chains operationalize effective mass through "
        "thermodynamic low-energy quantities, not that the systems or equations are "
        "equivalent."
    ),
    prior=0.84,
)

strat_cross_scope_caution = support(
    [
        gcn_800070efac5e476d,
        gcn_2741cdef_practical_effective_mass_scheme,
        gcn_1587257a956f4d18,
        gcn_03614e9b_homogeneous_isotropic_model,
    ],
    cross_scope_caution_standard_fl_vs_fcqpt,
    reason=(
        "The selected roots and mapping premises specify different systems and "
        "model scopes: standard low-temperature Landau Fermi-liquid reasoning for "
        "normal liquid He-3 versus a homogeneous isotropic heavy-electron FCQPT "
        "crossover model for YbRh2Si2. This warrants a scope-caution claim rather "
        "than equivalence or contradiction."
    ),
    prior=0.88,
)

strat_cross_ybrh2si2_rbc_scope_qualification = support(
    [
        gcn_03614e9b_homogeneous_isotropic_model,
        gcn_42a4ff_rbc_hall_dos_values,
        helper_rbc_parameterization_constrained_by_cef_gamma,
        helper_ybrh2si2_opposite_hall_transport_products,
        helper_rbc_dos_gamma_ybrh2si2_ybir2si2,
    ],
    cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope,
    reason=(
        "The Shaginyan premise explicitly says the homogeneous isotropic model "
        "neglects crystal-lattice anisotropy, Brillouin-zone structure, multiple "
        "bands, and anisotropic effective masses for universal scaling. The "
        "Friedemann RBC root and helpers explicitly add material-specific CEF/gamma "
        "calibration, band-resolved Hall-product cancellation, and DOS/gamma values "
        "for YbRh2Si2. These facts ground a scope-qualification claim because the "
        "model scopes differ while remaining jointly satisfiable."
    ),
    prior=0.90,
)

strat_cross_ybrh2si2_material_fs_constraints = support(
    [
        gcn_42a4ff_rbc_hall_dos_values,
        helper_rbc_parameterization_constrained_by_cef_gamma,
        helper_dhva_frequencies_masses_h_parallel_a,
        helper_dhva_angular_dependence_itinerant_lda_mismatch,
        gcn_2b8dd97_lurh2si2_reference_reanalysis,
        gcn_3a8394c_lurh2si2_small_fs_reference,
    ],
    cross_ybrh2si2_material_specific_fs_constraints,
    reason=(
        "All premises are material-specific YbRh2Si2 or LuRh2Si2-reference "
        "constraints: RBC supplies thermodynamically calibrated band/DOS/Hall "
        "information, Knebel dHvA supplies high-field frequencies and cyclotron "
        "masses plus an LDA mismatch, and Friedemann 2013 supplies the LuRh2Si2 "
        "small-FS reanalysis. The support is scoped to joint constraints and does "
        "not assert equivalence of the methods."
    ),
    prior=0.88,
)

strat_cross_ybrh2si2_field_method_scope_caution = support(
    [
        gcn_5501e18a_high_field_dhva_scope,
        gcn_f20b1f42_itinerant_4f_lda_sensitivity,
        helper_dhva_first_fs_information_scope,
        gcn_c131e014_ybrh2si2_midband_harmonic_assignment,
        helper_ybrh2si2_reduced_fundamental_set,
        gcn_3dc248d_ybrh2si2_14kt_not_small_fs,
        gcn_03614e9b_homogeneous_isotropic_model,
    ],
    cross_ybrh2si2_field_method_scope_caution,
    reason=(
        "The dHvA and reanalysis branches explicitly carry high-field, harmonic "
        "assignment, small-FS-reference, and LDA-sensitivity caveats, while the "
        "Shaginyan premise explicitly states the homogeneous isotropic model scope. "
        "Those conditions ground a caution claim rather than a contradiction."
    ),
    prior=0.90,
)

strat_cross_brinkman_rice_mott_boundary_family = support(
    [
        gcn_7ae79f_kondo_brinkman_rice_fixed_point,
        helper_brinkman_rice_large_mass_renormalization,
        capone_brinkman_rice_mass_z_tk_limit,
        gcn_31bc66ca16a44508,
        gcn_29401e42_nis2_brinkman_rice,
        helper_nis2_large_fs_603kt_belly_orbit,
        helper_nis2_mstar_6_me,
    ],
    cross_brinkman_rice_mott_boundary_family,
    reason=(
        "The three branches independently invoke heavy quasiparticles, mass "
        "enhancement or Z/T_K collapse, and proximity to a Mott or local-moment "
        "boundary. The support is thematic and mechanism-scoped, preserving the "
        "different material settings."
    ),
    prior=0.86,
)

strat_cross_brinkman_rice_scope_caution = support(
    [
        helper_kondo_lattice_screened_heavy_quasiparticles,
        helper_brinkman_rice_finite_stoner_enhancement,
        gcn_8f275a_brinkman_rice_scope_condition,
        gcn_e4ecd721edd14d3f,
        gcn_dd12256615264dfb,
        helper_brinkman_rice_large_fs_heavy_quasiparticles,
    ],
    cross_brinkman_rice_scope_caution,
    reason=(
        "The imported helpers spell out distinct scopes: screened f-ion Kondo "
        "lattices with finite Stoner enhancement, a conditional singlet-Mott "
        "entropy obstruction, and pressure-metalized NiS2 large-FS heavy "
        "quasiparticles. They justify a non-equivalence caution."
    ),
    prior=0.89,
)

strat_cross_thermo_transport_correlated_fl_consistency = support(
    [
        gcn_bc46d7_cemo_kw_wilson_fl_consistency,
        helper_cemo_kw_ratio_original_scale,
        helper_cemo_wilson_ratio_dual_reference,
        helper_cemo_ratio_consistency_correlated_fl,
        he3_gamma_implies_mstar_ratio_2_12,
        gcn_2e693115_entropy_over_temperature_mass,
        helper_rbc_dos_gamma_ybrh2si2_ybir2si2,
    ],
    cross_thermo_transport_correlated_fl_consistency,
    reason=(
        "CeMo2Si2C supplies ratio-based transport/susceptibility consistency "
        "checks, while the existing He-3 and YbRh2Si2 branches supply gamma, S/T, "
        "and DOS/gamma thermodynamic effective-mass routes. Together they ground a "
        "correlated-FL phenomenology theme without equating the materials."
    ),
    prior=0.84,
)
