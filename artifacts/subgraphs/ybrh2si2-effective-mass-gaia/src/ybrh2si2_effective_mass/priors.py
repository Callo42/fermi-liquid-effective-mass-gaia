"""Leaf-claim priors for the YbRh2Si2 effective-mass subgraph."""

from .paper_shaginyan2010 import (
    gcn_03614e9b_homogeneous_isotropic_model,
    gcn_2e693115_entropy_over_temperature_mass,
    gcn_6bbfeb95_stable_landau_solutions,
    gcn_677c6c_landau_integral_relation,
    gcn_e0c364ff_inflection_fcqpt_condition,
    gcn_ecddfefa_fermion_entropy_formula,
)


PRIORS = {
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
}
