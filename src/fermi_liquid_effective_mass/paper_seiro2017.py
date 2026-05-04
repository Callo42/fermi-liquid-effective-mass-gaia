"""paper_seiro2017 -- Kondo-lattice coherence hierarchy in YbRh2Si2."""

from gaia.lang import claim, deduction


gcn_fb2747_ybrh2si2_tp_tcoh_ratio = claim(
    r"""For stoichiometric YbRh2Si2, assigning T_coh approximately T_K approximately 25-30 K and extracting T_P approximately 3.3 K gives T_P/T_coh approximately 0.11; the LKM chain treats this hierarchy as meaningful for separating lattice-Kondo-dominated behavior from the onset of single-ion Kondo/coherence signatures [@Seiro2017].""",
    lkm_id="gcn_fb2747a8ec634c3f",
    source_paper="paper:867772725953823394",
    provenance_source="lkm",
    lkm_original=r"""Using the assignments T_coh approximately T_K approximately 25-30 K and the experimentally extracted crossover temperature T_P approximately 3.3 K at which pronounced lattice-Kondo-dominated spectral and transport signatures appear, the numerical ratio T_P/T_coh approximately 0.11 follows for the studied stoichiometric YbRh2Si2 samples; this numerical hierarchy is meaningful for interpreting the temperature evolution in this material, while recognizing that disorder, sample dependence, surface effects, and other microscopic parameters may alter the ratio in other systems.""",
)

gcn_3a1514_ybrh2si2_kondo_lattice_hierarchy = claim(
    r"""In stoichiometric YbRh2Si2, lattice Kondo correlations are detectable around T_coh approximately T_K approximately 25-30 K, but they dominate low-energy electronic properties only below T_P approximately 3.3 K, about 0.1*T_coh; single-ion Kondo effects therefore persist well below T_coh before lattice coherence enables the observed non-Fermi-liquid quantum-critical behavior [@Seiro2017].""",
    lkm_id="gcn_3a1514fde2d54682",
    source_paper="paper:867772725953823394",
    provenance_source="lkm",
    lkm_original=r"""For stoichiometric YbRh2Si2 the onset of lattice Kondo correlations is detectable around the coherence scale T_coh approximately T_K approximately25-30 K, yet the lattice Kondo correlations reach a regime in which they dominate low-energy electronic properties only below the crossover temperature T_P approximately 3.3 K, i.e., at T_P approximately 0.11*T_coh; consequently, single-ion Kondo effects persist down to temperatures well below T_coh before lattice coherence contributions grow sufficiently to enable the non-Fermi-liquid quantum-critical behavior observed in bulk and spectroscopic probes.""",
)

strat_gfac_717602aa489047e9_kondo_hierarchy = deduction(
    [gcn_fb2747_ybrh2si2_tp_tcoh_ratio],
    gcn_3a1514_ybrh2si2_kondo_lattice_hierarchy,
    reason=r"""1. Use STS observations that hybridization features begin below about 30 K while the Kondo-lattice peak dominates only below T_P about 3.3 K.
2. Define the target hierarchy: lattice correlations onset near T_coh approximately T_K but dominate only near 0.1*T_coh.
3. Use STS temperature evolution to separate onset near 30 K from dominance below T_P.
4. Use thermopower and Hall-mobility changes below T_P as bulk corroboration.
5. Note that the zero-bias minimum associated with single-ion Kondo effects persists to lower temperatures.
6. Combine T_coh about 25-30 K with T_P about 3.3 K to get T_P/T_coh about 0.1.
7. Conclude that lattice Kondo correlations dominate low-energy YbRh2Si2 behavior only well below the onset scale.""",
    prior=0.95,
)
