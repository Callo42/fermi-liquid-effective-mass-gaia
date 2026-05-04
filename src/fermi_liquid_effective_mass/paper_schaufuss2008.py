"""paper_schaufuss2008 -- ESR access to YbRh2Si2 heavy quasiparticles."""

from gaia.lang import claim, deduction


gcn_a76225_ybrh2si2_esr_collective_mode_assumption = claim(
    r"""Identifying the YbRh2Si2 ESR line as a collective heavy-quasiparticle resonance rests on empirical ESR/thermodynamic/NMR crossovers and on many-body narrowing proposals, while requiring alternatives such as residual localized Yb3+ ESR or conventional conduction-electron spin resonance to be excluded in the same temperature-field domain [@Schaufuss2008].""",
    lkm_id="gcn_a76225d44bfb476d",
    source_paper="paper:867762218521854503",
    provenance_source="lkm",
    lkm_original=r"""The identification of the observed ESR in YbRh2Si2 as a collective resonance of the coherent heavy quasiparticles formed below T_0 approximately 25 K rests on (a) the empirical coincidence of crossovers in the ESR g-factor and linewidth with crossovers seen in thermodynamic (Sommerfeld coefficient gamma) and 29Si NMR observables, and (b) theoretical proposals that many-body narrowing can render a collective ESR observable in a Kondo lattice; this identification requires excluding quantitatively adequate alternative scenarios in the same temperature-field domain.""",
)

gcn_d8b1_ybrh2si2_esr_heavy_quasiparticles = claim(
    r"""In YbRh2Si2, the anisotropic persistent ESR line, g-factor behavior tracking gamma=C_el/T and NMR observables, and low-temperature T^2 linewidth behavior show that ESR is a resonance of coherent heavy quasiparticles formed below T_K approximately T_0 approximately 25 K; ESR parameters are governed by m*(B,T), N(E_F;B,T), and quasiparticle spin relaxation, giving access to Kondo-state evolution and NFL-to-LFL crossover behavior [@Schaufuss2008].""",
    lkm_id="gcn_d8b1b53ca8b44189",
    source_paper="paper:867762218521854503",
    provenance_source="lkm",
    lkm_original=r"""The combination of experimental facts — (i) the presence of a strongly anisotropic and persistent ESR line in YbRh2Si2, (ii) a g-factor whose temperature and magnetic-field dependences mirror the temperature- and field-dependent Sommerfeld coefficient gamma = C_el/T and the 29Si NMR Knight shift and 1/(T1T), and (iii) a linewidth that acquires a T^2 low-temperature behaviour together with a field-dependent residual broadening — demonstrates that the observed ESR in YbRh2Si2 is a resonance excitation of the coherent heavy quasiparticles that form below the single-ion Kondo scale T_K approximately T_0 approximately 25 K. Consequently, the ESR parameters are governed by the field- and temperature-dependent quasiparticle effective mass m*(B,T), the quasiparticle density of states at the Fermi level N(E_F;B,T), and the quasiparticle spin relaxation times; therefore ESR provides direct experimental access to the dynamics and evolution of the Kondo state and to the crossover between non-Fermi-liquid and Landau Fermi-liquid regimes in this Kondo-lattice system.""",
)

strat_gfac_44921f1b7d4e4c4a_esr_heavy_qp = deduction(
    [gcn_a76225_ybrh2si2_esr_collective_mode_assumption],
    gcn_d8b1_ybrh2si2_esr_heavy_quasiparticles,
    reason=r"""1. Start from the observed anisotropic ESR resonance, the ESR g-factor crossover that tracks gamma and NMR quantities, and the ESR linewidth crossover to low-temperature T^2 behavior.
2. Identify ESR as a heavy-quasiparticle collective resonance below T0 about 25 K using empirical crossovers and many-body-narrowing proposals.
3. Relate resonance field/g-factor and linewidth to m*(B,T), N(E_F;B,T), and quasiparticle spin relaxation.
4. Exclude local-moment, conventional conduction-electron, and bottleneck alternatives within the same temperature-field domain.
5. Conclude that ESR probes Kondo-state evolution and the NFL-to-LFL crossover in YbRh2Si2.""",
    prior=0.95,
)
