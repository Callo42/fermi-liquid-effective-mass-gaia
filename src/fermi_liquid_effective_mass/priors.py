"""Leaf-claim priors for the connected YbRh2Si2 effective-mass package."""

from .paper_shaginyan2010 import (
    gcn_03614e9b_homogeneous_isotropic_model,
    gcn_2e693115_entropy_over_temperature_mass,
    gcn_6bbfeb95_stable_landau_solutions,
    gcn_677c6c_landau_integral_relation,
    gcn_e0c364ff_inflection_fcqpt_condition,
    gcn_ecddfefa_fermion_entropy_formula,
)
from .paper_shaginyan2009 import (
    gcn_58746c_fcqpt_homogeneous_mass_equation,
    gcn_f82c178_fcqpt_inflection_cubic_spectrum,
)
from .paper_friedemann2010 import (
    gcn_48bba377_specific_heat_calibration,
    gcn_c243dcb_rbc_phase_shift_parametrization,
)
from .paper_knebel2006 import (
    gcn_5501e18a_high_field_dhva_scope,
    gcn_f20b1f42_itinerant_4f_lda_sensitivity,
)
from .paper_friedemann2013 import (
    gcn_3a8394c_lurh2si2_small_fs_reference,
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs,
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment,
)
from .paper_tokiwa2004 import (
    gcn_021fb1_high_field_a_gamma_scaling_assumption,
    gcn_24ebf8_ybrh2si2_t2_resistivity_fit_reliability,
)
from .paper_seiro2017 import gcn_fb2747_ybrh2si2_tp_tcoh_ratio
from .paper_schaufuss2008 import gcn_a76225_ybrh2si2_esr_collective_mode_assumption
from .paper_pfau2013 import (
    gcn_8f49e0_periodic_kondo_lattice_lifshitz_dos,
    gcn_dbe6ec_ybrh2si2_cef_anisotropic_hybridization,
)
from .paper_naren2013 import (
    gcn_3ba45e_ybrh2si2_thermopower_corrob_lifshitz,
    gcn_6ca2b_ybrh2si2_hall_compensation_scenario,
)
from .paper_rourke2008 import (
    gcn_5090f8_dhva_orbit_assignment_reliability,
    gcn_848945_ybrh2si2_lusmall_fs_lda_assumption,
)
from .paper_friedemann2013_field import gcn_b01616_ybrh2si2_lda_inadequate_dynamic_correlations


PRIORS = {
    gcn_677c6c_landau_integral_relation: (
        0.82,
        "LKM chain treats the Landau effective-mass relation as a phenomenological starting equation near FCQPT; TODO:review",
    ),
    gcn_03614e9b_homogeneous_isotropic_model: (
        0.68,
        "Model adequacy is a universal-scaling approximation for YbRh2Si2 that omits material anisotropy and band structure; TODO:review",
    ),
    gcn_e0c364ff_inflection_fcqpt_condition: (
        0.78,
        "The inflection-point condition is explicitly used in the LKM chain but remains a tuned critical model construction; TODO:review",
    ),
    gcn_6bbfeb95_stable_landau_solutions: (
        0.70,
        "Numerical stability is reported for the selected temperature and field window but not independently audited in the root JSON; TODO:review",
    ),
    gcn_ecddfefa_fermion_entropy_formula: (
        0.90,
        "Fermi-Dirac entropy expression for quasiparticle occupations, capped at the direct-claim prior limit; TODO:review",
    ),
    gcn_2e693115_entropy_over_temperature_mass: (
        0.72,
        "Operational entropy-over-temperature effective-mass proxy is credible but approximation-sensitive in crossover/NFL regimes; TODO:review",
    ),
    gcn_f82c178_fcqpt_inflection_cubic_spectrum: (
        0.80,
        "Independent LKM chain states the FCQPT inflection/cubic-spectrum condition also present in the start-root chain; TODO:review",
    ),
    gcn_58746c_fcqpt_homogeneous_mass_equation: (
        0.78,
        "Asymptotic FCQPT mass equation premise follows the selected chain's homogeneous-limit derivation but is theory-scope sensitive; TODO:review",
    ),
    gcn_c243dcb_rbc_phase_shift_parametrization: (
        0.82,
        "RBC phase-shift parametrization is anchored to CEF splittings and heavy-fermion renormalized-band practice, but remains phenomenological; TODO:review",
    ),
    gcn_48bba377_specific_heat_calibration: (
        0.76,
        "Thermodynamic calibration to gamma_exp is explicit, though transport reliability inferred from the calibrated bands is approximation-sensitive; TODO:review",
    ),
    gcn_5501e18a_high_field_dhva_scope: (
        0.84,
        "High-field dHvA scope caution is explicit in the LKM chain and important for low-field QCP interpretation; TODO:review",
    ),
    gcn_f20b1f42_itinerant_4f_lda_sensitivity: (
        0.78,
        "LDA/FLAPW sensitivity is grounded in the Knebel comparison but remains a method-level caution; TODO:review",
    ),
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment: (
        0.78,
        "Harmonic reassignment is anchored to angular and mass comparisons but remains sensitive to branch-identification assumptions; TODO:review",
    ),
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs: (
        0.74,
        "High-field 14 kT inference depends on excluding artefact, magnetic-breakdown, and misassignment alternatives; TODO:review",
    ),
    gcn_3a8394c_lurh2si2_small_fs_reference: (
        0.84,
        "LuRh2Si2 reference premise is grounded in isostructural chemistry and filled Lu 4f shells but remains a transfer-model approximation; TODO:review",
    ),
    gcn_021fb1_high_field_a_gamma_scaling_assumption: (
        0.62,
        "Extending A/gamma^2 scaling from low fields to 16 T is explicitly an assumption in the LKM chain; TODO:review",
    ),
    gcn_24ebf8_ybrh2si2_t2_resistivity_fit_reliability: (
        0.76,
        "T^2 fit reliability is plausible for the reported low-temperature windows but sensitive to finite-temperature and sample effects; TODO:review",
    ),
    gcn_fb2747_ybrh2si2_tp_tcoh_ratio: (
        0.78,
        "T_P/T_coh hierarchy is a direct numerical extraction from the LKM chain but may vary with sample and surface conditions; TODO:review",
    ),
    gcn_a76225_ybrh2si2_esr_collective_mode_assumption: (
        0.68,
        "ESR collective-mode identification is supported by crossovers but depends on excluding localized-moment and bottleneck alternatives; TODO:review",
    ),
    gcn_dbe6ec_ybrh2si2_cef_anisotropic_hybridization: (
        0.78,
        "CEF-induced hybridization anisotropy is an explicit ingredient of the LKM chain but not by itself a direct measurement; TODO:review",
    ),
    gcn_8f49e0_periodic_kondo_lattice_lifshitz_dos: (
        0.76,
        "Periodic-Kondo-lattice DOS/Lifshitz premise is physically central to the chain but model-dependent; TODO:review",
    ),
    gcn_6ca2b_ybrh2si2_hall_compensation_scenario: (
        0.62,
        "Hall compensation is explicitly viable but not uniquely established by the transport data; TODO:review",
    ),
    gcn_3ba45e_ybrh2si2_thermopower_corrob_lifshitz: (
        0.78,
        "Thermopower anomalies from the same growth batch corroborate electronic-structure changes but are not uniquely diagnostic alone; TODO:review",
    ),
    gcn_848945_ybrh2si2_lusmall_fs_lda_assumption: (
        0.74,
        "LuRh2Si2 as a small-FS guide is plausible but remains an LDA/reference-transfer assumption; TODO:review",
    ),
    gcn_5090f8_dhva_orbit_assignment_reliability: (
        0.70,
        "Orbit assignment by angular/frequency matching is standard but sensitive to missing pockets and branch visibility; TODO:review",
    ),
    gcn_b01616_ybrh2si2_lda_inadequate_dynamic_correlations: (
        0.82,
        "LDA inadequacy for YbRh2Si2 masses is directly grounded in the LKM comparison with observed branches and large mass renormalization; TODO:review",
    ),
}
