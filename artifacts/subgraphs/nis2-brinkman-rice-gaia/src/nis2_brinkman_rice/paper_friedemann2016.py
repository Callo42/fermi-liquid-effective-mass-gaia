"""paper_friedemann2016 -- NiS2 quantum-oscillation Brinkman-Rice claims.

Source: Large Fermi Surface of Heavy Electrons at the Border of Mott Insulating State in NiS2
DOI: 10.1038/srep25335
Authors: S. Friedemann | H. Chang | M. B. Gamza | P. Reiss | X. Chen |
P. Alireza | W. A. Coniglio | D. Graf | S. Tozer | F. M. Grosche
Reference key (CSL): Friedemann2016
"""

from gaia.lang import claim, deduction


_ROOT_ORIGINAL = r"""The simultaneous observation of a large Fermi-surface cross-sectional area (the 6.03 kT belly orbit) and a strongly enhanced quasiparticle effective mass m* = 6(2) m_e in NiS₂ pressurized to ≈3.8 GPa is consistent with the Brinkman–Rice picture of a correlated Fermi liquid near a Mott insulator, in which coherent Fermi-liquid quasiparticles form a heavy Fermi liquid whose Fermi-surface volume remains equal to that of the corresponding uncorrelated band while the quasiparticle spectral weight Z (the residue of the single-particle Green's function at the quasiparticle pole) and the quasiparticle velocities are strongly reduced."""

_ALTERNATIVES_ORIGINAL = r"""The inference that the coexistence of a large Fermi-surface extremal area and an enhanced quasiparticle effective mass demonstrates realization of the Brinkman–Rice correlated-metal scenario (suppressed quasiparticle weight Z with preserved Luttinger volume) presumes that alternative mechanisms—such as strong renormalization by spin fluctuations, enhanced electron–phonon coupling, or Fermi-surface reconstruction associated with proximate magnetic order—cannot produce the same pair of experimental observations without invoking Brinkman–Rice physics.
      Brinkman, W. F. & Rice, T. M. Application of Gutzwiller's Variational Method to the Metal-Insulator Transition. Phys. Rev. B 2, 4302–4304 (1970)."""

_BRINKMAN_RICE_STEP_ORIGINAL = r"""Define the Brinkman-Rice picture as the theoretical framework in which, on approaching a Mott insulating state by bandwidth reduction, the quasiparticle weight $Z$ is suppressed (possibly to $Z\to 0$), quasiparticle velocities are reduced, the effective mass $m^*$ is strongly enhanced (and in some treatments can diverge), while the Fermi surface volume remains that of the corresponding uncorrelated metal as required by Luttinger's theorem; cite the original Brinkman-Rice argument and Luttinger's theorem as the conceptual bases.
[6]
[9]"""


gcn_8a1a2748_alternative_mechanisms_assumption = claim(
    "For pressure-metalized NiS2 near 3.8 GPa, interpreting the coexistence of a "
    "large Fermi-surface extremal area and enhanced quasiparticle effective mass as "
    "realization of the Brinkman-Rice correlated-metal scenario relies on the "
    "assumption that spin-fluctuation renormalization, enhanced electron-phonon "
    "coupling, or Fermi-surface reconstruction from proximate magnetic order cannot "
    "produce the same pair of observations without Brinkman-Rice physics "
    "[@Friedemann2016].",
    lkm_id="gcn_8a1a27485204457b",
    source_paper="paper:814525482547544066",
    provenance_source="lkm",
    lkm_original=_ALTERNATIVES_ORIGINAL,
)

gcn_29401e42_nis2_brinkman_rice = claim(
    "In NiS2 pressurized to approximately 3.8 GPa, the simultaneous observation of "
    "a large Fermi-surface cross-sectional area, specifically the 6.03 kT belly "
    "orbit, and a strongly enhanced quasiparticle effective mass m* = 6(2) m_e is "
    "consistent with the Brinkman-Rice picture of a correlated Fermi liquid near a "
    "Mott insulator: coherent heavy quasiparticles retain the uncorrelated-band "
    "Fermi-surface volume while quasiparticle spectral weight Z and quasiparticle "
    "velocities are strongly reduced [@Friedemann2016].",
    lkm_id="gcn_29401e4284574aa2",
    source_paper="paper:814525482547544066",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

helper_nis2_large_fs_603kt_belly_orbit = claim(
    "For NiS2 pressurized to approximately 3.8 GPa, the selected LKM root treats the "
    "6.03 kT belly quantum-oscillation orbit as a large Fermi-surface cross-sectional "
    "area matching the uncorrelated-band large-Fermi-surface expectation "
    "[@Friedemann2016].",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_29401e4284574aa2"],
    decomposition_of="gcn_29401e4284574aa2",
    lkm_original=_ROOT_ORIGINAL,
)

helper_nis2_mstar_6_me = claim(
    "For the same pressure-metalized NiS2 setting, the selected LKM root reports a "
    "strongly enhanced quasiparticle effective mass m* = 6(2) m_e for the observed "
    "Fermi-liquid quasiparticles [@Friedemann2016].",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_29401e4284574aa2"],
    decomposition_of="gcn_29401e4284574aa2",
    lkm_original=_ROOT_ORIGINAL,
)

helper_brinkman_rice_large_fs_heavy_quasiparticles = claim(
    "In the Brinkman-Rice picture invoked by the selected LKM factor, approaching a "
    "Mott insulating state by bandwidth reduction suppresses quasiparticle weight Z "
    "and quasiparticle velocities, strongly enhances m*, and preserves the large "
    "Fermi-surface volume of the corresponding uncorrelated metal "
    "[@Friedemann2016].",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_29401e4284574aa2"],
    decomposition_of="gcn_29401e4284574aa2",
    lkm_original=_BRINKMAN_RICE_STEP_ORIGINAL,
)


strat_gfac_dfd930ba89614e8a_brinkman_rice = deduction(
    [gcn_8a1a2748_alternative_mechanisms_assumption],
    gcn_29401e42_nis2_brinkman_rice,
    reason=r"""1. Treat conclusion 2 (the metallic state has a large Fermi surface matching the uncorrelated-band prediction) and conclusion 3 (the quasiparticle effective mass is strongly enhanced to $m^* = 6(2)\ m_e$) as established upstream results to be taken as known starting points for the present reasoning.
2. Define the Brinkman-Rice picture as the theoretical framework in which, on approaching a Mott insulating state by bandwidth reduction, the quasiparticle weight $Z$ is suppressed (possibly to $Z\to 0$), quasiparticle velocities are reduced, the effective mass $m^*$ is strongly enhanced (and in some treatments can diverge), while the Fermi surface volume remains that of the corresponding uncorrelated metal as required by Luttinger's theorem; cite the original Brinkman-Rice argument and Luttinger's theorem as the conceptual bases.
[6]
[9]
3. Observe that the empirical combination established in conclusions 2 and 3 -- a large Fermi surface volume equal to the uncorrelated-band value and a strongly enhanced quasiparticle mass -- matches the key qualitative signatures of a Brinkman-Rice correlated Fermi liquid proximate to a Mott insulator, namely: preserved large Fermi volume and suppressed quasiparticle weight manifesting as heavy quasiparticles.
Fig. 5
Fig. 4
4. Note that alternative theoretical scenarios that envisage a continuous depletion of carrier concentration or Fermi-surface reconstruction on approach to the insulating state would predict a reduced Fermi surface volume or the absence of a large uncorrelated-like Fermi surface in the immediate metallic regime; because the measured experimental combination does not display such carrier depletion or reconstruction, the experimental findings are consistent with the Brinkman-Rice description rather than with those alternative scenarios.
[40]
5. Conclude that the coexistence of a large Fermi surface volume (conclusion 2) and a strongly enhanced quasiparticle mass (conclusion 3) in pressure-metalized NiS$_2$ is consistent with the Brinkman-Rice picture of a correlated Fermi liquid proximate to a Mott insulator: coherent quasiparticles form a heavy Fermi liquid whose Fermi surface volume remains that of the uncorrelated band while the quasiparticle weight $Z$ and quasiparticle velocities are reduced.
Table 1""",
    prior=0.95,
)

strat_decompose_nis2_large_fs = deduction(
    [gcn_29401e42_nis2_brinkman_rice],
    helper_nis2_large_fs_603kt_belly_orbit,
    reason=(
        "1. The LKM root explicitly contains the component assertion that NiS2 at "
        "approximately 3.8 GPa shows a large Fermi-surface cross-sectional area, "
        "identified as the 6.03 kT belly orbit."
    ),
    prior=0.95,
)

strat_decompose_nis2_mstar = deduction(
    [gcn_29401e42_nis2_brinkman_rice],
    helper_nis2_mstar_6_me,
    reason=(
        "1. The LKM root explicitly contains the component assertion that "
        "pressure-metalized NiS2 has a strongly enhanced quasiparticle effective "
        "mass m* = 6(2) m_e."
    ),
    prior=0.95,
)

strat_decompose_brinkman_rice_signature = deduction(
    [gcn_29401e42_nis2_brinkman_rice],
    helper_brinkman_rice_large_fs_heavy_quasiparticles,
    reason=(
        "1. The LKM factor step defining the Brinkman-Rice picture explicitly links "
        "preserved Fermi volume with reduced Z, reduced quasiparticle velocities, "
        "and enhanced effective mass near the Mott boundary."
    ),
    prior=0.95,
)
