"""paper_capone2001 -- Capone, Fabrizio, and Tosatti Mott-entropy claims.

Source: Direct Transition Between a Singlet Mott Insulator and a Superconductor
DOI: 10.48550/arXiv.cond-mat/0101402
Authors: M. Capone | M. Fabrizio | E. Tosatti
Reference key (CSL): Capone2001
"""

from gaia.lang import claim, deduction


_ROOT_ORIGINAL = r"""A normal Fermi liquid state is defined here as an electronic phase with a well-defined Fermi surface, a finite quasiparticle weight $Z>0$ (where $Z\equiv m/m_{*}$ with $m$ the bare band mass and $m_{*}$ the quasiparticle effective mass), and a low-energy coherence scale $T_{K}$ (effective Fermi energy $E_{F}^{*}$) below which thermodynamic quantities are those of a Fermi liquid. In a Brinkman–Rice type scenario the approach to the Mott transition is characterized by a divergent effective mass $m_{*}\to\infty$ and a vanishing quasiparticle weight $Z\to0$, so that $T_{K}\to0$ and the Fermi-liquid electronic entropy per lattice site at $T\sim T_{K}$, $S(T_{K})$, remains of order unity for any $T_{K}>0$. A nondegenerate singlet Mott insulator is defined as an insulating phase whose ground state is a unique spin-singlet with a finite spin gap and strictly zero entropy as $T\to0$. Under these definitions, and assuming no motion of the chemical potential that would convert the transition into a metal–band-insulator crossover and assuming no spontaneous symmetry breaking that changes the entropy budget, a continuous adiabatic connection (a direct crossover without a thermodynamic phase transition or symmetry breaking) from the described Brinkman–Rice Fermi liquid to the defined nondegenerate singlet Mott insulator is impossible because the finite low-temperature entropy of the Fermi liquid cannot be removed continuously as $T_{K}\to0$ while the insulator has zero entropy; therefore some intervening thermodynamic instability or a distinct intermediate phase must occur between the Fermi-liquid metal and the singlet Mott insulator rather than a direct continuous Fermi-liquid–insulator crossover."""

_FL_ENTROPY_ORIGINAL = r"""In a Fermi liquid with a low-energy coherence scale $T_{K}$ (identified here with the effective coherence scale $E_{F}^{*}$), the electronic entropy per lattice site for temperatures $T\le T_{K}$ follows the low-temperature Fermi-liquid form $S(T)/N\sim T/T_{K}$, which implies that the entropy evaluated at the coherence scale, $S(T_{K})$, is of order unity and therefore finite for any $T_{K}>0$; this statement assumes a standard Fermi-liquid quasiparticle description with a low-temperature specific-heat coefficient proportional to $1/T_{K}$ and the absence of other comparably low-energy degrees of freedom contributing to the entropy."""

_LUTTINGER_ORIGINAL = r"""For the interacting lattice Hamiltonian $H=\sum_{ij\sigma}\sum_{a,b=1}^{3}t_{ij}^{ab}d_{ia\sigma}^{\dagger}d_{jb\sigma}+\sum_{i}H_{i}^{int}$ with orbital-diagonal hopping $t_{n}^{\alpha\beta}=t\delta_{\alpha\beta}$, on-site interaction term $H_{i}^{int}$ containing $U$ and $J$, and a metallic solution that remains a Fermi liquid, Luttinger's theorem implies that the interacting chemical potential $\mu$ coincides with the noninteracting chemical potential $\mu_{0}$ for the given filling and that the single-particle spectral density at the chemical potential is pinned to the noninteracting value, $\rho(\mu)=\rho_{0}(\mu_{0})$; under these conditions the Mott transition proceeds by a narrowing of the quasiparticle resonance at fixed chemical potential (the resonance height remaining pinned) rather than by moving the chemical potential to the band edge."""

_CONTINUITY_ORIGINAL = r"""Consider a Fermi-liquid metallic phase with coherence scale $T_{K}>0$ whose entropy per site at $T\sim T_{K}$ is of order unity, and consider a target Mott insulating phase that is a nondegenerate spin singlet with strictly zero entropy as $T\to0$; under the assumption of thermodynamic continuity (no phase transition or spontaneous symmetry breaking) and with the chemical potential pinned (as by Luttinger's theorem), a continuous adiabatic connection from the finite-$T_{K}$ Fermi liquid to the zero-entropy singlet Mott insulator is impossible because the finite low-temperature entropy of the metal cannot be removed continuously as $T_{K}\to0$ without either (i) moving the chemical potential to the band edge, (ii) breaking a symmetry that alters the entropy counting, or (iii) encountering a thermodynamic instability that creates a new phase which removes the entropy; hence, absent (i) or (ii), some thermodynamic instability or new intermediate phase must intervene prior to or at the transition."""


gcn_31bc66ca16a44508 = claim(
    r"""For the Capone-Fabrizio-Tosatti 2001 Brinkman-Rice/DMFT discussion, a Fermi-liquid metal with coherence scale T_K identified with E_F* has electronic entropy per lattice site S(T)/N ~ T/T_K for T <= T_K; therefore S(T_K) is finite and of order unity for every T_K > 0, assuming ordinary Fermi-liquid quasiparticles and no additional comparably low-energy entropy carriers [@Capone2001].""",
    lkm_id="gcn_31bc66ca16a44508",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    lkm_original=_FL_ENTROPY_ORIGINAL,
)

gcn_795699f572b24ed5 = claim(
    r"""For the three-orbital interacting lattice Hamiltonian considered by Capone, Fabrizio, and Tosatti 2001, if the metallic solution remains a Fermi liquid then Luttinger's theorem pins the interacting chemical potential to the noninteracting value and pins the spectral density at the chemical potential to rho_0(mu_0); the Mott transition then occurs by narrowing the quasiparticle resonance at fixed chemical potential rather than by shifting mu to a band edge [@Capone2001].""",
    lkm_id="gcn_795699f572b24ed5",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    lkm_original=_LUTTINGER_ORIGINAL,
)

gcn_dd12256615264dfb = claim(
    r"""In the Capone-Fabrizio-Tosatti 2001 setting, a Fermi-liquid metal with T_K > 0 and order-unity entropy near T ~ T_K cannot be continuously and adiabatically connected to a nondegenerate spin-singlet Mott insulator with zero T -> 0 entropy while Luttinger's theorem pins the chemical potential and no symmetry breaking changes the entropy accounting; absent chemical-potential motion or symmetry breaking, a thermodynamic instability or intermediate phase must intervene [@Capone2001].""",
    lkm_id="gcn_dd12256615264dfb",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    lkm_original=_CONTINUITY_ORIGINAL,
)

gcn_e4ecd721edd14d3f = claim(
    r"""For the Capone-Fabrizio-Tosatti 2001 Brinkman-Rice-type route toward a nondegenerate singlet Mott insulator, a normal Fermi liquid has a well-defined Fermi surface, finite quasiparticle weight Z > 0 with Z = m/m*, and coherence scale T_K ~ E_F*; as m* -> infinity, Z -> 0 and T_K -> 0, while S(T_K) remains order unity for each T_K > 0. Because the target singlet Mott insulator has a unique spin-singlet ground state, a spin gap, and zero entropy as T -> 0, a direct continuous Fermi-liquid-to-insulator crossover is impossible under fixed chemical potential and no-symmetry-breaking assumptions; an intervening thermodynamic instability or distinct intermediate phase must occur [@Capone2001].""",
    lkm_id="gcn_e4ecd721edd14d3f",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

capone_fl_definition_z_tk = claim(
    r"""In the Capone-Fabrizio-Tosatti 2001 root, the scoped normal Fermi liquid is a metal with a well-defined Fermi surface, finite quasiparticle weight Z > 0, Z = m/m* with m the bare band mass and m* the quasiparticle effective mass, and a low-energy coherence scale T_K identified with E_F* below which thermodynamics are Fermi-liquid-like [@Capone2001].""",
    lkm_id="gcn_e4ecd721edd14d3f",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    decomposition_of="gcn_e4ecd721edd14d3f",
    lkm_original=_ROOT_ORIGINAL,
)

capone_brinkman_rice_mass_z_tk_limit = claim(
    r"""In the Brinkman-Rice-type scenario described by Capone, Fabrizio, and Tosatti 2001, approaching the Mott transition drives m* -> infinity and Z -> 0; because the low-energy resonance width satisfies E_F* ~ ZW/2 and T_K ~ E_F*, the coherence scale T_K also tends to zero [@Capone2001].""",
    lkm_id="gcn_e4ecd721edd14d3f",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    decomposition_of="gcn_e4ecd721edd14d3f",
    lkm_original=_ROOT_ORIGINAL,
)

capone_singlet_mott_zero_entropy = claim(
    r"""The target Mott insulator in the Capone-Fabrizio-Tosatti 2001 argument is nondegenerate, has a unique spin-singlet ground state and finite spin gap, and therefore has strictly zero entropy in the T -> 0 limit [@Capone2001].""",
    lkm_id="gcn_e4ecd721edd14d3f",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    decomposition_of="gcn_e4ecd721edd14d3f",
    lkm_original=_ROOT_ORIGINAL,
)

capone_luttinger_pinning_blocks_band_edge_route = claim(
    r"""Within the Capone-Fabrizio-Tosatti Fermi-liquid solution obeying Luttinger's theorem, the chemical potential remains pinned to the noninteracting value, so the Mott transition cannot be converted into a trivial metal-to-band-insulator crossover by sliding the chemical potential to a band edge [@Capone2001].""",
    lkm_id="gcn_795699f572b24ed5",
    source_paper="paper:867770551072981407",
    provenance_source="lkm",
    decomposition_of="gcn_795699f572b24ed5",
    lkm_original=_LUTTINGER_ORIGINAL,
)

strat_gfac_2737af3324f345e8 = deduction(
    [gcn_31bc66ca16a44508, gcn_795699f572b24ed5, gcn_dd12256615264dfb],
    gcn_e4ecd721edd14d3f,
    reason=r"""1. Define "Fermi liquid (FL)" as a normal metallic state characterized by a finite quasiparticle weight $Z>0$, where the quasiparticle effective mass is $m_{*}$ and $Z\equiv m/m_{*}$ with $m$ the noninteracting mass; define the coherence (effective Fermi) energy scale $E_{F}^{*}$ as the width of the low-energy quasiparticle resonance and identify it later with $E_{F}^{*}\simeq ZW/2$, where $W$ is the noninteracting bandwidth.
2. State the DMFT picture for a Brinkman-Rice type Mott transition: within Dynamical Mean Field Theory (DMFT) the metal near the Mott transition is described by a narrow low-energy Kondo-like quasiparticle resonance sitting at the chemical potential together with high-energy Hubbard bands; the resonance width plays the role of an effective Kondo temperature $T_{K}$ or effective Fermi energy $E_{F}^{*}$ below which the system behaves as a FL. [1]
[1]
Fig. 1
3. Introduce the quantitative relation between the resonance width and the quasiparticle weight: the peak width is given by $E_{F}^{*}\simeq ZW/2$, where $Z\equiv m/m_{*}$ and $W$ is the bare bandwidth; consequently $T_{K}\sim E_{F}^{*}\sim ZW/2$, so that $T_{K}\to0$ as $Z\to0$ when $m_{*}\to\infty$.
4. Relate low-temperature entropy of the FL to the coherence scale: for temperature $T\leq T_{K}$ the entropy per site $S(T)/N$ behaves as $S(T)/N\sim T/T_{K}$ so that the entropy at the coherence scale, $S(T_{K})$, is of order unity (i.e., finite) for $U$ up to the critical value where $T_{K}$ vanishes; thus a FL with a finite $T_{K}$ carries a finite low-temperature entropy per site on the order of one at temperatures of order $T_{K}$.
5. Characterize the nondegenerate singlet Mott insulator targeted in the paper: the insulator is nondegenerate and a spin singlet, hence it has zero entropy at zero temperature and a finite spin gap for spin excitations.
6. Invoke the numerical/DMFT observation that, in the Brinkman-Rice scenario relevant to the models considered, $Z$ decreases continuously to zero as $U$ approaches the critical value $U_{c2}$, so that the FL coherence scale $T_{K}$ vanishes continuously at the transition (the paper reports this continuous vanishing numerically and displays the narrowing resonance in the spectral function). [2]
[2]
Fig. 1; Fig. 2(a)
7. Point out the entropy mismatch at a continuous crossover: because the FL for $U\lesssim U_{c2}$ possesses a finite low-temperature entropy on the scale $T_{K}$ and the singlet Mott insulator for $U\gtrsim U_{c2}$ has zero entropy, a continuous crossover that smoothly transforms the FL into the zero-entropy singlet insulator would require that the finite entropy of the FL be continuously removed exactly as $T_{K}\to0$ at the transition; this is incompatible with the insulator having zero entropy unless some phase transition or instability removes the entropy of the metallic solution prior to or at the MT.
8. Explain why Luttinger's theorem prevents a trivial resolution: by Luttinger's theorem the chemical potential in the interacting system must coincide with the bare chemical potential, and the spectral density at the chemical potential must be pinned to the noninteracting value; hence, within solutions obeying Luttinger theorem, the MT proceeds by narrowing of the resonance at fixed chemical potential (rather than by shifting the chemical potential to the band edge), and therefore the finite FL entropy associated with the finite $T_{K}$ cannot be transferred continuously into a zero-entropy insulator without violating this constraint. This argument relies on the DMFT/FL picture and Luttinger theorem as discussed in the paper. [2]
[2]
9. List the only possible ways out discussed in the paper and rule them out or note them as alternatives: (a) a breakdown of Luttinger's theorem before the MT could allow the chemical potential to move and connect smoothly to a zero-entropy insulator - the authors regard this as a possible but nonstandard scenario; (b) the insulator could break a symmetry (e.g., spin SU(2)), in which case the metal could break the same symmetry and the transition could be of a metal-band-insulator type - this is not the present case because the insulator under study is nondegenerate and does not break symmetry; therefore neither of these standard resolutions applies to the singlet, nondegenerate Mott insulator considered.
10. Conclude that continuity is impossible: combining the finite FL entropy at the vanishing coherence scale, the pinning enforced by Luttinger theorem, and the zero entropy of the singlet Mott insulator, the FL state characterized by finite $Z$ (for $U$ just below the MT) cannot be continuously connected, within a Brinkman-Rice type scenario where $m_{*}\to\infty$ and $Z\to0$, to a nondegenerate singlet Mott insulator; therefore some intermediate phase must intrude between the FL metal and the singlet Mott insulator rather than a direct continuous FL-insulator crossover.""",
    prior=0.95,
)

strat_decompose_root_to_fl_definition = deduction(
    [gcn_e4ecd721edd14d3f],
    capone_fl_definition_z_tk,
    reason=(
        "1. The root explicitly defines the scoped normal Fermi liquid by its Fermi "
        "surface, finite Z > 0, Z = m/m*, and coherence scale T_K."
    ),
    prior=0.95,
)

strat_decompose_root_to_br_limit = deduction(
    [gcn_e4ecd721edd14d3f],
    capone_brinkman_rice_mass_z_tk_limit,
    reason=(
        "1. The root explicitly states the Brinkman-Rice limiting behavior: "
        "m* -> infinity, Z -> 0, and T_K -> 0."
    ),
    prior=0.95,
)

strat_decompose_root_to_singlet_entropy = deduction(
    [gcn_e4ecd721edd14d3f],
    capone_singlet_mott_zero_entropy,
    reason=(
        "1. The root explicitly defines the nondegenerate singlet Mott insulator "
        "as a unique spin-singlet, spin-gapped endpoint with zero entropy as T -> 0."
    ),
    prior=0.95,
)

strat_decompose_luttinger_premise = deduction(
    [gcn_795699f572b24ed5],
    capone_luttinger_pinning_blocks_band_edge_route,
    reason=(
        "1. Premise gcn_795699f572b24ed5 explicitly states that Luttinger's "
        "theorem pins mu to mu_0 and keeps the resonance at fixed chemical "
        "potential rather than moving to the band edge."
    ),
    prior=0.95,
)

