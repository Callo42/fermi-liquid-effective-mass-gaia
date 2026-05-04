"""paper_friedemann2013_field -- many-body methods for YbRh2Si2 masses."""

from gaia.lang import claim, deduction


ybrh2si2_lda_missing_dynamic_correlations = claim(
    r"""YbRh2Si2 has strong local correlations and Kondo-driven heavy quasiparticles, seen through large Sommerfeld coefficients and strongly renormalized effective masses; conventional LDA lacks dynamic local correlations and Kondo renormalization, so many-body methods such as renormalized-band approaches or DMFT are required for quantitative Fermi-surface and mass descriptions [@Friedemann2013b].""",
    lkm_id="gcn_b016160b38f34ce7",
    source_paper="paper:813199962614530051",
    provenance_source="lkm",
    lkm_original=r"""YbRh2Si2 exhibits strong local electronic correlations and Kondo-driven heavy quasiparticles, manifest as large Sommerfeld coefficients and strongly renormalized effective masses, and conventional LDA does not capture dynamic local correlations and Kondo renormalization; many-body methods such as renormalized-band approaches or DMFT are required to obtain a quantitative description.""",
)

ybrh2si2_many_body_methods_required = claim(
    r"""Density-functional LDA calculations of YbRh2Si2 in both f-core small-FS and itinerant-4f large-FS variants fail to reproduce the complete set of quantum-oscillation branches and large quasiparticle masses, so quantitative YbRh2Si2 Fermi-surface and effective-mass modeling requires many-body approaches capturing local dynamic correlations and Kondo renormalization [@Friedemann2013b].""",
    lkm_id="gcn_34ce9aa28e054fd1",
    source_paper="paper:813199962614530051",
    provenance_source="lkm",
    lkm_original=r"""Density-functional LDA calculations of YbRh2Si2 performed both in the 'f-core' approximation and in fully itinerant LDA using experimental lattice parameters fail to reproduce the complete set of experimentally observed quantum-oscillation branches and large quasiparticle masses; therefore many-body electronic-structure approaches that capture local dynamic correlations and Kondo renormalization, such as renormalized-band methods or DMFT, are required to obtain a quantitative description.""",
)

derive_ybrh2si2_many_body_methods_required = deduction(
    [ybrh2si2_lda_missing_dynamic_correlations],
    ybrh2si2_many_body_methods_required,
    reason=r"""1. Start from the refined small-FS LDA and fully itinerant LDA failures to reproduce key YbRh2Si2 quantum-oscillation branches.
2. Identify dynamic local correlations and Kondo renormalization as missing ingredients in static one-electron LDA.
3. Note that these missing ingredients affect f-derived bands, hybridization, Fermi-surface topology, and effective masses.
4. Conclude that many-body electronic-structure methods, including renormalized-band approaches or DMFT with suitable impurity solvers, are needed for quantitative YbRh2Si2 Fermi-surface and mass modeling.""",
    prior=0.95,
)
