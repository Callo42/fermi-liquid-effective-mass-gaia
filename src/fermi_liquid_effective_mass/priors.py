"""Leaf-claim priors for the combined Fermi-liquid effective-mass package."""

from .paper_alvesalo1979 import gcn_1587257a956f4d18, gcn_2ee995fe1e674e2a
from .paper_friedemann2010 import (
    gcn_48bba377_specific_heat_calibration,
    gcn_c243dcb_rbc_phase_shift_parametrization,
)
from .paper_shaginyan2010 import (
    gcn_03614e9b_homogeneous_isotropic_model,
    gcn_2e693115_entropy_over_temperature_mass,
    gcn_6bbfeb95_stable_landau_solutions,
    gcn_677c6c_landau_integral_relation,
    gcn_e0c364ff_inflection_fcqpt_condition,
    gcn_ecddfefa_fermion_entropy_formula,
)


PRIORS = {
    gcn_2ee995fe1e674e2a: (
        0.78,
        "Direct calorimetric premise from the LKM chain, but it extrapolates the observed T >= about 3 mK linear region to the T -> 0 Fermi-liquid limit near the superfluid transition; TODO:review",
    ),
    gcn_1587257a956f4d18: (
        0.82,
        "Standard Landau Fermi-liquid mapping premise with values reported in the LKM chain, but the chain records the numerical mapping rather than a full derivation; TODO:review",
    ),
    gcn_677c6c_landau_integral_relation: (
        0.82,
        "LKM chain treats the Landau effective-mass equation as a standard phenomenological starting point near FCQPT, conditional on quasiparticle and amplitude assumptions; TODO:review",
    ),
    gcn_03614e9b_homogeneous_isotropic_model: (
        0.68,
        "Model adequacy is a deliberate universal-scaling approximation for YbRh2Si2 that neglects anisotropy and band structure, so it is plausible but scope-limited; TODO:review",
    ),
    gcn_e0c364ff_inflection_fcqpt_condition: (
        0.78,
        "The LKM chain presents the inflection-point amplitude tuning as the practical FCQPT critical construction rather than direct microscopic proof; TODO:review",
    ),
    gcn_6bbfeb95_stable_landau_solutions: (
        0.70,
        "Numerical convergence and robustness are reported for the paper's temperature and field window, but no independent numerical error audit is included in the root evidence; TODO:review",
    ),
    gcn_ecddfefa_fermion_entropy_formula: (
        0.90,
        "The Fermi-Dirac entropy expression is a standard quasiparticle combinatorial formula and is capped at the direct-claim prior limit; TODO:review",
    ),
    gcn_2e693115_entropy_over_temperature_mass: (
        0.72,
        "Using M*(T,B)=S(T,B)/T is an operational density-of-states proxy extended into crossover/NFL regimes, making it credible but approximation-sensitive; TODO:review",
    ),
    gcn_c243dcb_rbc_phase_shift_parametrization: (
        0.82,
        "The LKM chain anchors the RBC phase-shift parametrization to established renormalized-band references and to Friedemann et al.'s YbRh2Si2 implementation, but it remains a phenomenological single-width representation of 4f quasiparticles; TODO:review",
    ),
    gcn_48bba377_specific_heat_calibration: (
        0.76,
        "The LKM chain makes the thermodynamic calibration explicit, yet the inference from reproducing gamma_exp to reliable band occupations and transport integrals is approximation-sensitive and not independently checked inside this selected chain; TODO:review",
    ),
}
