"""paper_anderson1984 -- claims and deductions from Anderson 1984.

Source: Heavy-electron superconductors, spin fluctuations, and triplet pairing
DOI: 10.1103/physrevb.30.1549
Authors: P. W. Anderson
Reference key (CSL): Anderson1984
"""

from gaia.lang import claim, deduction


gcn_40f111_nozieres_local_fl_kondo_sites = claim(
    r"""For a metallic Kondo lattice made of a periodic subset of localized magnetic f-electron shells hybridized with conduction electrons, Anderson 1984 treats the leading low-energy local physics at each screened f-ion site as the Nozieres single-impurity Fermi-liquid representation: for energies E << T_K, scattering is described by Friedel-sum-rule phase shifts and finite analytic residual interactions, with inter-site corrections assumed small compared with the single-site Kondo scale [@Anderson1984].""",
    lkm_id="gcn_40f11182b5f74ff2",
    source_paper="paper:813343302173589505",
    provenance_source="lkm",
    lkm_original=r"""For a metallic crystalline system in which a periodic subset of lattice sites host localized magnetic $f$-electron shells that hybridize with conduction electrons (a "Kondo lattice"), the low-energy local many-body physics at each $f$-ion site is accurately described, to leading order in inter-site coupling, by the Nozières single-impurity Fermi-liquid representation: for energies $E\ll T_K$ (with $T_K$ the single-site Kondo scale) the local scattering of conduction electrons by each $f$-ion is characterized by Fermi-liquid phase shifts fixed by the Friedel sum rule and by low-energy residual interactions that are finite and analytic in energy, and corrections due to inter-site hybridization and inter-ion interactions are parametrically small in the ratio of inter-site coupling energy scales to $T_K$.""",
)

gcn_8f275a_brinkman_rice_scope_condition = claim(
    r"""Anderson 1984 defines the relevant Brinkman-Rice Fermi-liquid fixed point for Kondo-lattice metals as a Fermi liquid proximate to a Mott or local-moment instability, with very large effective-mass renormalization but finite nondivergent Stoner enhancement; the selected chain applies this description when direct inter-site exchange, RKKY coupling, and incipient magnetic order are weak or irrelevant enough that local Nozieres-type Kondo Fermi-liquid physics remains qualitatively intact [@Anderson1984].""",
    lkm_id="gcn_8f275a75866e4923",
    source_paper="paper:813343302173589505",
    provenance_source="lkm",
    lkm_original=r"""Define a Brinkman–Rice Fermi-liquid fixed point as a Fermi-liquid proximate to a Mott/local-moment instability with very large effective-mass renormalization and a finite (nondivergent) Stoner enhancement of the uniform spin susceptibility; the claim is that for a Kondo-lattice metal in which inter-site interactions (direct inter-site exchange, RKKY couplings, or incipient magnetic ordering tendencies) are sufficiently weak or irrelevant, these inter-site collective effects do not qualitatively alter the local Nozières-type Fermi-liquid physics and the Brinkman–Rice description remains the appropriate low-energy fixed point.""",
)

gcn_7ae79f_kondo_brinkman_rice_fixed_point = claim(
    r"""For Anderson 1984 heavy-electron Kondo-lattice materials such as CeAl3, CeCu2Si2, UBe13, and UPt3, when localized f-ion moments are quenched by Kondo screening and inter-site collective effects do not qualitatively override the local Nozieres Fermi-liquid physics, the ground state is described as a Brinkman-Rice type Fermi-liquid fixed point: a coherent heavy-quasiparticle Fermi liquid with very large quasiparticle effective-mass renormalization and a finite, order-unity Stoner enhancement of the uniform spin susceptibility rather than a divergent almost-ferromagnetic enhancement [@Anderson1984].""",
    lkm_id="gcn_7ae79f122f1c4fcb",
    source_paper="paper:813343302173589505",
    provenance_source="lkm",
    lkm_original=r"""The ground state of a periodic Kondo-lattice of localized $f$-ions whose local magnetic moments are quenched by Kondo screening is described by a Brinkman–Rice type Fermi-liquid fixed point (a "Brinkman–Rice liquid"), i.e., a strongly renormalized Fermi liquid in which local on-site correlations produce very large quasiparticle effective-mass renormalizations while the uniform-spin susceptibility enhancement (the Stoner enhancement) remains finite and of order unity rather than diverging. Here "Kondo-lattice" denotes a crystalline solid in which a periodic subset of lattice sites host local magnetic degrees of freedom from $f$-electron shells that hybridize with conduction electrons to form a coherent heavy-quasiparticle band, and "Brinkman–Rice liquid" denotes a Fermi-liquid fixed point proximate to a Mott- or local-moment instability characterized by large mass renormalization and a finite Stoner enhancement factor.""",
)

helper_kondo_lattice_screened_heavy_quasiparticles = claim(
    r"""In the Anderson 1984 usage isolated by the LKM chain, a Kondo lattice is a periodic array of magnetic f-ions in U or Ce heavy-electron compounds whose local moments are quenched by Kondo screening, leaving coherent very-heavy quasiparticles at low energy [@Anderson1984].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_7ae79f122f1c4fcb"],
    lkm_original=r"""Define "Kondo-lattice": a periodic array of magnetic $f$-ions whose local moments are quenched by Kondo screening so that the low-energy degrees of freedom form a Fermi liquid of very heavy quasiparticles; this definition is taken from the identification of certain U and Ce compounds as such systems (examples: $CeAl_{3}$, $CeCu_{2}Si_{2}$, $UBe_{13}$, $UPt_3$) which are described in the paper as "Kondo lattices".""",
)

helper_brinkman_rice_large_mass_renormalization = claim(
    r"""The Brinkman-Rice liquid component in the Anderson 1984 Kondo-lattice chain asserts a strongly renormalized Fermi liquid with very large quasiparticle effective-mass enhancement near a Mott or local-moment instability [@Anderson1984].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_7ae79f122f1c4fcb", "gcn_8f275a75866e4923"],
    lkm_original=r"""Define "Brinkman–Rice liquid" (Brinkman–Rice Fermi-liquid fixed point): a Fermi-liquid fixed point near a Mott- or local-moment instability characterized by (a) very large effective-mass renormalization (heavy quasiparticles) and (b) a Stoner enhancement factor that attains an $O(1)$ finite constant (rather than diverging) as the paramagnetic instability is approached.""",
)

helper_brinkman_rice_finite_stoner_enhancement = claim(
    r"""The Brinkman-Rice liquid component in the Anderson 1984 Kondo-lattice chain asserts that the uniform-spin susceptibility enhancement remains finite and order unity, with the paper using a near-constant Stoner enhancement factor around 4 as the characteristic sign rather than a divergent almost-ferromagnetic enhancement [@Anderson1984].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_7ae79f122f1c4fcb", "gcn_8f275a75866e4923"],
    lkm_original=r"""Explain the characteristic Brinkman–Rice signature as used in the paper: the "Stoner enhancement" factor (the factor by which the uniform spin susceptibility is enhanced relative to the noninteracting quasiparticle density-of-states contribution) takes on a near-constant value (the paper cites an example value "near 4") across pressures rather than diverging while the effective mass appears to be increasing; this observation is described as the characteristic sign of Brinkman–Rice behavior and is used as a key empirical/theoretical signature.""",
)

helper_nozieres_to_kondo_lattice_fixed_point = claim(
    r"""The Anderson 1984 chain transfers the Nozieres single-impurity Kondo Fermi-liquid mechanism to a periodic Kondo lattice by treating inter-ion interactions as slight modifications and by using sum-rule-fixed local phase shifts and opposite-spin on-site residual interactions to motivate the same finite-Stoner, large-mass fixed-point structure [@Anderson1984].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=[
        "gcn_40f11182b5f74ff2",
        "gcn_8f275a75866e4923",
        "gcn_7ae79f122f1c4fcb",
    ],
    lkm_original=r"""Connect the Kondo-lattice picture to Brinkman–Rice behavior: using the facts that (i) the local $f$-site physics is essentially the single-impurity Kondo problem represented by the Nozières Fermi-liquid ansatz, and (ii) the Stoner enhancement in this context is controlled by an interaction effective only in the opposite-spin (antiparallel-spin) channel on a site, conclude that the same mechanism that produces a finite, substantial Stoner enhancement in the single-impurity Kondo problem should apply to the periodic Kondo lattice as well; hence the ground state should be described by the Brinkman–Rice Fermi-liquid fixed point rather than by a conventional almost-ferromagnetic spin-fluctuation fixed point.""",
)


strat_gfac_303f81acdd314345_kondo_brinkman_rice = deduction(
    [
        gcn_40f111_nozieres_local_fl_kondo_sites,
        gcn_8f275a_brinkman_rice_scope_condition,
    ],
    gcn_7ae79f_kondo_brinkman_rice_fixed_point,
    reason=r"""1. Define "Kondo-lattice": a periodic array of magnetic $f$-ions whose local moments are quenched by Kondo screening so that the low-energy degrees of freedom form a Fermi liquid of very heavy quasiparticles; this definition is taken from the identification of certain U and Ce compounds as such systems (examples: $CeAl_{3}$, $CeCu_{2}Si_{2}$, $UBe_{13}$, $UPt_3$) which are described in the paper as "Kondo lattices".
1
2. Define "Brinkman–Rice liquid" (Brinkman–Rice Fermi-liquid fixed point): a Fermi-liquid fixed point near a Mott- or local-moment instability characterized by (a) very large effective-mass renormalization (heavy quasiparticles) and (b) a Stoner enhancement factor that attains an $O(1)$ finite constant (rather than diverging) as the paramagnetic instability is approached; this characterization is taken from the paper's discussion of Brinkman and Rice and of the Brinkman–Rice viewpoint for $^3$He analogies.
6
3. Note the empirical observation motivating the analogy: a number of U and Ce compounds appear best described as Kondo-lattice systems in which the $f$-shell magnetism is quenched by the Kondo effect, leaving a Fermi liquid of extremely heavy electrons, and several of these compounds become superconducting in a low temperature range (between 1 and 0.1 K) as listed in the paper.
1
4. Invoke the Nozières Fermi-liquid ansatz for Kondo ions: treat each Kondo ion by the Fermi-liquid representation of the single-impurity Kondo problem (the Nozières ansatz), with only slight modifications due to inter-ion interactions; the paper justifies this by stating that many Fermi-liquid parameters are fixed by general sum rules (for example the Friedel sum rule for phase shifts) and thus band formation should not strongly modify them.
9
5. Explain the characteristic Brinkman–Rice signature as used in the paper: the "Stoner enhancement" factor (the factor by which the uniform spin susceptibility is enhanced relative to the noninteracting quasiparticle density-of-states contribution) takes on a near-constant value (the paper cites an example value "near 4") across pressures rather than diverging while the effective mass appears to be increasing; this observation is described as the characteristic sign of Brinkman–Rice behavior and is used as a key empirical/theoretical signature.
7
6. Connect the Kondo-lattice picture to Brinkman–Rice behavior: using the facts that (i) the local $f$-site physics is essentially the single-impurity Kondo problem represented by the Nozières Fermi-liquid ansatz, and (ii) the Stoner enhancement in this context is controlled by an interaction effective only in the opposite-spin (antiparallel-spin) channel on a site, conclude that the same mechanism that produces a finite, substantial Stoner enhancement in the single-impurity Kondo problem should apply to the periodic Kondo lattice as well; hence the ground state should be described by the Brinkman–Rice Fermi-liquid fixed point rather than by a conventional almost-ferromagnetic spin-fluctuation fixed point.
4
7. Record the explicit statement of the claim: the appropriate fixed point to describe the ground state of the Kondo lattice is the Brinkman–Rice liquid (the paper states this assertion directly), i.e., a Fermi-liquid fixed point characterized by large mass renormalization and a finite Stoner enhancement factor.""",
    prior=0.95,
)

strat_decompose_kondo_lattice_definition = deduction(
    [gcn_7ae79f_kondo_brinkman_rice_fixed_point],
    helper_kondo_lattice_screened_heavy_quasiparticles,
    reason=(
        "1. The selected root and factor step 1 explicitly define the Kondo-lattice "
        "setting as a periodic array of screened f-ion moments forming very heavy "
        "low-energy quasiparticles."
    ),
    prior=0.95,
)

strat_decompose_large_mass_component = deduction(
    [gcn_7ae79f_kondo_brinkman_rice_fixed_point],
    helper_brinkman_rice_large_mass_renormalization,
    reason=(
        "1. The selected root and factor step 2 explicitly include very large "
        "effective-mass renormalization as one component of the Brinkman-Rice "
        "Fermi-liquid fixed point."
    ),
    prior=0.95,
)

strat_decompose_finite_stoner_component = deduction(
    [gcn_7ae79f_kondo_brinkman_rice_fixed_point],
    helper_brinkman_rice_finite_stoner_enhancement,
    reason=(
        "1. The selected root and factor step 5 explicitly state that the Stoner "
        "enhancement remains finite and near constant, rather than diverging, in "
        "the Brinkman-Rice interpretation."
    ),
    prior=0.95,
)

strat_decompose_nozieres_transfer_component = deduction(
    [
        gcn_40f111_nozieres_local_fl_kondo_sites,
        gcn_8f275a_brinkman_rice_scope_condition,
    ],
    helper_nozieres_to_kondo_lattice_fixed_point,
    reason=(
        "1. Factor steps 4 and 6 explicitly transfer the Nozieres single-impurity "
        "Fermi-liquid ansatz to periodic Kondo ions under slight inter-ion "
        "modifications, then use this transfer to justify the finite-Stoner "
        "Brinkman-Rice fixed-point picture."
    ),
    prior=0.95,
)
