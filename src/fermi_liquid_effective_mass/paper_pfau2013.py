"""paper_pfau2013 -- high-field Kondo suppression and Lifshitz interplay."""

from gaia.lang import claim, deduction


gcn_dbe6ec_ybrh2si2_cef_anisotropic_hybridization = claim(
    r"""In tetragonal YbRh2Si2, CEF ground-state symmetry of the Yb3+ 4f ion produces strongly anisotropic 4f-conduction hybridization and enhanced quasiparticle g-factor anisotropy, making particular f-derived bands sensitive to magnetic-field-driven Zeeman shifts [@Pfau2013].""",
    lkm_id="gcn_dbe6ecfc88864ea6",
    source_paper="paper:867761748805944216",
    provenance_source="lkm",
    lkm_original=r"""In tetragonal YbRh2Si2 the crystalline-electric-field ground-state symmetry of the Yb3+ 4f ion produces a strongly anisotropic hybridization matrix element between localized 4f states and conduction-electron states and simultaneously yields enhanced anisotropy of the effective quasiparticle g factor; this anisotropic CEF-induced hybridization can generate anisotropic renormalized bands and enhance the sensitivity of f-derived bands to applied magnetic field.""",
)

gcn_faee88_ybrh2si2_smooth_kondo_mass_suppression = claim(
    r"""For Yb-based Kondo systems in fields of order the single-ion Kondo scale, local Kondo screening is suppressed continuously with B, producing a continuous decrease of quasiparticle effective mass m*(B), so field mainly reduces Kondo correlations smoothly rather than abruptly localizing the 4f electrons [@Pfau2013].""",
    lkm_id="gcn_faee88cfe22142a5",
    source_paper="paper:867761748805944216",
    provenance_source="lkm",
    lkm_original=r"""For Yb-based Kondo systems under an applied magnetic field of order the single-ion Kondo energy scale, the local Kondo screening of Yb 4f moments is suppressed continuously as a function of B, and this continuous suppression produces a corresponding continuous decrease of the quasiparticle effective mass m*(B); therefore the dominant effect of magnetic field on local Kondo physics in the relevant field range is a smooth reduction of Kondo correlations rather than an abrupt localization transition of the 4f electrons.""",
)

gcn_8f49e0_periodic_kondo_lattice_lifshitz_dos = claim(
    r"""In a periodic Kondo lattice, coherent hybridized quasiparticle bands can contain sharp van-Hove-type DOS peaks or flattened dispersions; Zeeman spin splitting can move these features through the Fermi energy and cause discrete Lifshitz transitions even while overall mass renormalization is reduced smoothly [@Pfau2013].""",
    lkm_id="gcn_8f49e0480b7d4e0f",
    source_paper="paper:867761748805944216",
    provenance_source="lkm",
    lkm_original=r"""In a periodic Kondo-lattice system, coherent lattice effects produce renormalized quasiparticle bands with sharp van Hove-type peaks or flattened dispersions in N(epsilon); when a magnetic field spin-splits these quasiparticle bands, Zeeman shifts can move such DOS features through epsilon_F and cause discrete Fermi-surface topology changes even while the overall quasiparticle mass renormalization is reduced smoothly by Kondo suppression.""",
)

gcn_4d206_ybrh2si2_kondo_lifshitz_interplay = claim(
    r"""YbRh2Si2 high-field phenomenology is explained by the interplay of CEF-induced anisotropic hybridization and g-factor anisotropy, smooth field suppression of Kondo screening that reduces m*(B), and Kondo-lattice coherence that creates van-Hove-type DOS structures whose Zeeman shifts produce successive Lifshitz transitions; this accounts for continuous mass reduction plus abrupt transport/thermodynamic anomalies [@Pfau2013].""",
    lkm_id="gcn_4d206f9ebed246c8",
    source_paper="paper:867761748805944216",
    provenance_source="lkm",
    lkm_original=r"""The combined phenomenology of YbRh2Si2 in magnetic field is explained by the interplay of three microscopic ingredients: (a) CEF ground-state symmetry of the Yb3+ ion producing strongly anisotropic 4f-conduction hybridization and enhanced quasiparticle g-factor anisotropy, (b) smooth field-driven suppression of local Kondo screening that continuously reduces m*(B) and modifies the Kondo-derived coherence peak, and (c) coherence effects intrinsic to the periodic Kondo lattice that create sharp van Hove-type DOS structures so Zeeman spin-splitting moves these DOS features through the Fermi energy and produces successive Lifshitz transitions.""",
)

strat_gfac_a3846efd68654c47_kondo_lifshitz_interplay = deduction(
    [
        gcn_dbe6ec_ybrh2si2_cef_anisotropic_hybridization,
        gcn_faee88_ybrh2si2_smooth_kondo_mass_suppression,
        gcn_8f49e0_periodic_kondo_lattice_lifshitz_dos,
    ],
    gcn_4d206_ybrh2si2_kondo_lifshitz_interplay,
    reason=r"""1. Treat the three high-field transitions, renormalized-band Lifshitz predictions, and Hall evidence for continuous Kondo suppression as established starting points.
2. Identify CEF-induced anisotropic hybridization, smooth field-driven Kondo suppression, and periodic-lattice coherence with van-Hove-like DOS structures as the three ingredients.
3. Explain that anisotropic hybridization controls field-sensitive f-derived bands, smooth Kondo suppression reduces m*, and lattice coherence supplies sharp DOS features.
4. Account for distinct Lifshitz transitions at fields of order the Kondo scale, continuous m* reduction, and abrupt transport/thermodynamic signatures.
5. Use moderate gamma(B) reduction and single-impurity NRG expectations to reject a single abrupt f-localization jump.
6. Conclude that the combined mechanism explains multiple high-field YbRh2Si2 transitions without requiring a single metamagnetic jump.""",
    prior=0.95,
)
