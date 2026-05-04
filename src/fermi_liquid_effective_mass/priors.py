"""Leaf-claim priors for the connected YbRh2Si2 effective-mass package."""

from .paper_shaginyan2010 import (
    homogeneous_isotropic_heavy_liquid_model,
    entropy_over_temperature_mass_proxy,
    stable_landau_numerical_solutions,
    landau_mass_integral_relation,
    fcqpt_inflection_critical_condition,
    fermion_entropy_formula,
)
from .paper_shaginyan2009 import (
    fcqpt_homogeneous_mass_equation,
    fcqpt_cubic_spectrum_condition,
)
from .paper_friedemann2010 import (
    rbc_specific_heat_calibration,
    rbc_phase_shift_parametrization,
)
from .paper_knebel2006 import (
    ybrh2si2_high_field_dhva_scope,
    ybrh2si2_itinerant_4f_lda_sensitivity,
)
from .paper_friedemann2013 import (
    lurh2si2_small_fs_reference,
    ybrh2si2_14kt_orbit_not_small_fs,
    ybrh2si2_midband_harmonic_assignment,
)
from .paper_tokiwa2004 import (
    high_field_a_gamma_scaling_assumption,
    ybrh2si2_t2_resistivity_fit_reliability,
)
from .paper_seiro2017 import ybrh2si2_tp_tcoh_ratio
from .paper_schaufuss2008 import ybrh2si2_esr_collective_mode_assumption
from .paper_pfau2013 import (
    periodic_kondo_lattice_lifshitz_dos,
    ybrh2si2_cef_anisotropic_hybridization,
)
from .paper_naren2013 import (
    ybrh2si2_thermopower_lifshitz_corroboration,
    ybrh2si2_hall_compensation_scenario,
)
from .paper_rourke2008 import (
    dhva_orbit_assignment_reliability,
    ybrh2si2_lusmall_fs_lda_assumption,
)
from .paper_friedemann2013_field import ybrh2si2_lda_missing_dynamic_correlations


PRIORS = {
    landau_mass_integral_relation: (
        0.82,
        "LKM chain treats the Landau effective-mass relation as a phenomenological starting equation near FCQPT; TODO:review",
    ),
    homogeneous_isotropic_heavy_liquid_model: (
        0.68,
        "Model adequacy is a universal-scaling approximation for YbRh2Si2 that omits material anisotropy and band structure; TODO:review",
    ),
    fcqpt_inflection_critical_condition: (
        0.78,
        "The inflection-point condition is explicitly used in the LKM chain but remains a tuned critical model construction; TODO:review",
    ),
    stable_landau_numerical_solutions: (
        0.70,
        "Numerical stability is reported for the selected temperature and field window but not independently audited in the root JSON; TODO:review",
    ),
    fermion_entropy_formula: (
        0.90,
        "Fermi-Dirac entropy expression for quasiparticle occupations, capped at the direct-claim prior limit; TODO:review",
    ),
    entropy_over_temperature_mass_proxy: (
        0.72,
        "Operational entropy-over-temperature effective-mass proxy is credible but approximation-sensitive in crossover/NFL regimes; TODO:review",
    ),
    fcqpt_cubic_spectrum_condition: (
        0.80,
        "Independent LKM chain states the FCQPT inflection/cubic-spectrum condition also present in the start-root chain; TODO:review",
    ),
    fcqpt_homogeneous_mass_equation: (
        0.78,
        "Asymptotic FCQPT mass equation premise follows the selected chain's homogeneous-limit derivation but is theory-scope sensitive; TODO:review",
    ),
    rbc_phase_shift_parametrization: (
        0.82,
        "RBC phase-shift parametrization is anchored to CEF splittings and heavy-fermion renormalized-band practice, but remains phenomenological; TODO:review",
    ),
    rbc_specific_heat_calibration: (
        0.76,
        "Thermodynamic calibration to gamma_exp is explicit, though transport reliability inferred from the calibrated bands is approximation-sensitive; TODO:review",
    ),
    ybrh2si2_high_field_dhva_scope: (
        0.84,
        "High-field dHvA scope caution is explicit in the LKM chain and important for low-field QCP interpretation; TODO:review",
    ),
    ybrh2si2_itinerant_4f_lda_sensitivity: (
        0.78,
        "LDA/FLAPW sensitivity is grounded in the Knebel comparison but remains a method-level caution; TODO:review",
    ),
    ybrh2si2_midband_harmonic_assignment: (
        0.78,
        "Harmonic reassignment is anchored to angular and mass comparisons but remains sensitive to branch-identification assumptions; TODO:review",
    ),
    ybrh2si2_14kt_orbit_not_small_fs: (
        0.74,
        "High-field 14 kT inference depends on excluding artefact, magnetic-breakdown, and misassignment alternatives; TODO:review",
    ),
    lurh2si2_small_fs_reference: (
        0.84,
        "LuRh2Si2 reference premise is grounded in isostructural chemistry and filled Lu 4f shells but remains a transfer-model approximation; TODO:review",
    ),
    high_field_a_gamma_scaling_assumption: (
        0.62,
        "Extending A/gamma^2 scaling from low fields to 16 T is explicitly an assumption in the LKM chain; TODO:review",
    ),
    ybrh2si2_t2_resistivity_fit_reliability: (
        0.76,
        "T^2 fit reliability is plausible for the reported low-temperature windows but sensitive to finite-temperature and sample effects; TODO:review",
    ),
    ybrh2si2_tp_tcoh_ratio: (
        0.78,
        "T_P/T_coh hierarchy is a direct numerical extraction from the LKM chain but may vary with sample and surface conditions; TODO:review",
    ),
    ybrh2si2_esr_collective_mode_assumption: (
        0.68,
        "ESR collective-mode identification is supported by crossovers but depends on excluding localized-moment and bottleneck alternatives; TODO:review",
    ),
    ybrh2si2_cef_anisotropic_hybridization: (
        0.78,
        "CEF-induced hybridization anisotropy is an explicit ingredient of the LKM chain but not by itself a direct measurement; TODO:review",
    ),
    periodic_kondo_lattice_lifshitz_dos: (
        0.76,
        "Periodic-Kondo-lattice DOS/Lifshitz premise is physically central to the chain but model-dependent; TODO:review",
    ),
    ybrh2si2_hall_compensation_scenario: (
        0.62,
        "Hall compensation is explicitly viable but not uniquely established by the transport data; TODO:review",
    ),
    ybrh2si2_thermopower_lifshitz_corroboration: (
        0.78,
        "Thermopower anomalies from the same growth batch corroborate electronic-structure changes but are not uniquely diagnostic alone; TODO:review",
    ),
    ybrh2si2_lusmall_fs_lda_assumption: (
        0.74,
        "LuRh2Si2 as a small-FS guide is plausible but remains an LDA/reference-transfer assumption; TODO:review",
    ),
    dhva_orbit_assignment_reliability: (
        0.70,
        "Orbit assignment by angular/frequency matching is standard but sensitive to missing pockets and branch visibility; TODO:review",
    ),
    ybrh2si2_lda_missing_dynamic_correlations: (
        0.82,
        "LDA inadequacy for YbRh2Si2 masses is directly grounded in the LKM comparison with observed branches and large mass renormalization; TODO:review",
    ),
}
