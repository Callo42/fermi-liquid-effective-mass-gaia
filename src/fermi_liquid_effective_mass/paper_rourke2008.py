"""paper_rourke2008 -- field dependence of the YbRh2Si2 Fermi surface."""

from gaia.lang import claim, deduction


ybrh2si2_lusmall_fs_lda_assumption = claim(
    r"""Using LuRh2Si2 LDA+SOC Fermi-surface topology as a qualitative small-Fermi-surface guide for YbRh2Si2 assumes isostructural substitution and neglect of heavy-fermion correlations do not change the gross topology relevant to orbit identification [@Rourke2008].""",
    lkm_id="gcn_848945fcb6214456",
    source_paper="paper:811888199457570817",
    provenance_source="lkm",
    lkm_original=r"""Consider electronic-structure calculations within LDA+SOC on LuRh2Si2 with filled 4f shell and YbRh2Si2 with active 4f quasihole. The assumption is that the LuRh2Si2 LDA+SOC Fermi-surface topology gives a qualitatively accurate small-FS topology for YbRh2Si2 when 4f electrons are localized, even though strong many-body renormalizations in YbRh2Si2 are not captured by LDA.""",
)

dhva_orbit_assignment_reliability = claim(
    r"""Assigning YbRh2Si2 observed dHvA branches to calculated small-Fermi-surface D-sheet orbits assumes the calculated angular dispersions are distinct, no unexpected pockets produce coincident frequencies, and branch visibility does not confound the mapping [@Rourke2008].""",
    lkm_id="gcn_5090f81994f14b4c",
    source_paper="paper:811888199457570817",
    provenance_source="lkm",
    lkm_original=r"""Given experimentally observed dHvA frequencies and angular dependences and calculated extremal frequencies and angular dependences for candidate Fermi-surface sheets, matching frequencies and angular dependences allows assignment of each observed branch to a calculated orbit, assuming distinct calculated angular dispersions, no uncalculated coincident pockets, and no experimental-resolution or amplitude-variation confounding.""",
)

ybrh2si2_small_fs_mass_enhancement = claim(
    r"""LDA+SOC calculations for LuRh2Si2 as the small-Fermi-surface analogue produce a D-sheet topology whose predicted orbits match YbRh2Si2 dHvA frequencies better than large-FS YbRh2Si2 LDA+SOC; comparing calculated band masses with measured cyclotron masses yields m*/m_b enhancements of order ten, consistent with strong many-body renormalization [@Rourke2008].""",
    lkm_id="gcn_d10f91dd4b8e4f21",
    source_paper="paper:811888199457570817",
    provenance_source="lkm",
    lkm_original=r"""Band-structure calculations carried out within LDA+SOC for LuRh2Si2 produce a D-sheet Fermi-surface topology whose predicted extremal orbits and angular dependences qualitatively match the observed YbRh2Si2 dHvA frequencies and angular behavior better than the large-FS YbRh2Si2 calculation; band masses m_b computed from the small-FS D-sheet provide a reference against which measured cyclotron masses yield m*/m_b of order ten, consistent with strong many-body renormalization.""",
)

derive_ybrh2si2_small_fs_mass_enhancement = deduction(
    [
        ybrh2si2_lusmall_fs_lda_assumption,
        dhva_orbit_assignment_reliability,
    ],
    ybrh2si2_small_fs_mass_enhancement,
    reason=r"""1. Perform all-itinerant LDA+SOC calculations for LuRh2Si2 as the small-FS analogue and YbRh2Si2 as the large-FS case.
2. Match observed YbRh2Si2 dHvA frequencies and angular dependences to calculated D-sheet hole orbits.
3. Note that the LuRh2Si2 small-FS topology matches the detected orbits better than the large-FS YbRh2Si2 calculation.
4. Compare measured cyclotron masses with calculated band masses.
5. Conclude that the observed branches carry mass enhancements of order ten, consistent with strong many-body renormalization.""",
    prior=0.95,
)
