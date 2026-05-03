"""Leaf-claim priors for the combined Fermi-liquid effective-mass package."""

from .paper_alvesalo1979 import gcn_1587257a956f4d18, gcn_2ee995fe1e674e2a
from .paper_anderson1984 import (
    gcn_40f111_nozieres_local_fl_kondo_sites,
    gcn_8f275a_brinkman_rice_scope_condition,
)
from .paper_capone2001 import (
    gcn_31bc66ca16a44508,
    gcn_795699f572b24ed5,
    gcn_dd12256615264dfb,
)
from .paper_friedemann2010 import (
    gcn_48bba377_specific_heat_calibration,
    gcn_c243dcb_rbc_phase_shift_parametrization,
)
from .paper_friedemann2013 import (
    gcn_3a8394c_lurh2si2_small_fs_reference,
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs,
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment,
)
from .paper_friedemann2016 import gcn_8a1a2748_alternative_mechanisms_assumption
from .paper_knebel2006 import (
    gcn_5501e18a_high_field_dhva_scope,
    gcn_f20b1f42_itinerant_4f_lda_sensitivity,
)
from .paper_paramanik2013 import (
    gcn_2dc55af_kw_empirical_scale,
    gcn_7459a446_wilson_ratio_interpretation,
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
    gcn_5501e18a_high_field_dhva_scope: (
        0.84,
        "The high-field caveat is explicitly stated in the selected LKM chain and is physically plausible for a field-tuned heavy-fermion compound, but it is a scope caution rather than a direct measurement in this root; TODO:review",
    ),
    gcn_f20b1f42_itinerant_4f_lda_sensitivity: (
        0.78,
        "The LKM chain ties the itinerant-4f LDA sensitivity to the Knebel et al. comparison figures, but the proposition is methodological and approximation-sensitive, so the direct prior remains below 0.9; TODO:review",
    ),
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment: (
        0.78,
        "The LKM chain anchors the 5-7 kT harmonic reassignment to angular-dependence and mass comparisons, but the assignment is a reanalysis of published spectra and remains sensitive to harmonic/mixed-frequency identification; TODO:review",
    ),
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs: (
        0.74,
        "The LKM chain directly states that the refined core-4f small-FS calculation lacks a (100)-field orbit near 14 kT and that the measured peak behaves as a fundamental, but the itinerant-4f inference is conditional on excluding artefact, magnetic-breakdown, and misassignment alternatives; TODO:review",
    ),
    gcn_3a8394c_lurh2si2_small_fs_reference: (
        0.84,
        "The LuRh2Si2 reference premise is grounded in isostructural chemistry, filled Lu 4f shells, refined z_Si=0.379 c structure, and similar non-f conduction-band character, while transfer to YbRh2Si2 is still a reference-model approximation; TODO:review",
    ),
    gcn_40f111_nozieres_local_fl_kondo_sites: (
        0.78,
        "The premise is grounded in Anderson's Nozieres/Friedel-sum-rule argument for screened Kondo ions, but the extrapolation from a single impurity to a periodic lattice is explicitly approximate and inter-site corrections are only bounded qualitatively; TODO:review",
    ),
    gcn_8f275a_brinkman_rice_scope_condition: (
        0.72,
        "The premise is a scoped fixed-point identification rather than a direct measurement: it is plausible when RKKY, direct exchange, and incipient ordering are weak or irrelevant, but those boundary conditions are not independently established inside the selected root chain; TODO:review",
    ),
    gcn_31bc66ca16a44508: (
        0.82,
        "Fermi-liquid entropy scaling premise from the selected LKM chain; credible within the stated quasiparticle/coherence-scale assumptions but sensitive to the absence of other low-energy entropy carriers; TODO:review",
    ),
    gcn_795699f572b24ed5: (
        0.78,
        "Luttinger-pinning premise from the selected LKM chain for a metallic Fermi-liquid solution of the specified Hamiltonian; plausible but conditional on the solution remaining a conventional FL up to the transition; TODO:review",
    ),
    gcn_dd12256615264dfb: (
        0.80,
        "Conditional entropy-mismatch premise from the selected LKM chain; strong as a thermodynamic argument under fixed-mu/no-symmetry-breaking assumptions, but it is exactly where alternative transition routes must be reviewed; TODO:review",
    ),
    gcn_8a1a2748_alternative_mechanisms_assumption: (
        0.58,
        "Interpretive exclusion premise from the LKM chain: plausible for the selected NiS2 quantum-oscillation argument, but it explicitly depends on alternative spin-fluctuation, electron-phonon, and magnetic-reconstruction mechanisms not independently ruled out by this root JSON; TODO:review",
    ),
    gcn_2dc55af_kw_empirical_scale: (
        0.82,
        "The premise is a standard empirical correlated-metal diagnostic and is explicitly cited in the LKM chain, but the appropriate KW normalization can depend on degeneracy, carrier density, and material class; TODO:review",
    ),
    gcn_7459a446_wilson_ratio_interpretation: (
        0.74,
        "The Wilson/Sommerfeld-ratio premise is grounded in the chain and gives both Ce3+ and conduction-electron normalizations, but the choice of mu_eff changes the numerical value substantially and remains a review-sensitive convention; TODO:review",
    ),
}
