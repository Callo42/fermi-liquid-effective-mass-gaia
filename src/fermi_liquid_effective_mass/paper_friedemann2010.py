"""paper_friedemann2010 -- claims and deductions from Friedemann et al. 2010.

Source: Hall effect measurements and electronic structure calculations on YbRh 2 Si 2
and its reference compounds LuRh 2 Si 2 and YbIr 2 Si 2
DOI: 10.1103/physrevb.82.035103
Authors: Sven Friedemann | Steffen Wirth | Niels Oeschler | Cornelius Krellner |
Christoph Geibel | Frank Steglich | Sam MaQuilon | Zachary Fisk | Silke Paschen |
Gertrud Zwicknagl
Reference key (CSL): Friedemann2010
"""

from gaia.lang import claim, deduction, support


gcn_c243dcb_rbc_phase_shift_parametrization = claim(
    r"""For YbRh2Si2 heavy-fermion renormalized-band calculations, Friedemann et al. 2010 use a renormalized-band method in which the low-energy local 4f contribution is represented by resonance-type phase shifts for crystalline-electric-field eigenstates; the resonance centers are split by measured CEF excitation energies, and a single positive resonance-width parameter controls the quasiparticle mass renormalization and associated Fermi-surface and transport changes [@Friedemann2010].""",
    lkm_id="gcn_c243dcb58cae4418",
    source_paper="paper:811773737962569729",
    provenance_source="lkm",
    lkm_original=r"""In the renormalized-band method (RBC) for heavy-fermion compounds the low-energy contribution of local 4f states is modeled by introducing resonance-type phase shifts for each crystalline-electric-field (CEF) eigenstate m according to
      \widetilde{\eta}_f(E) = arctan[ \widetilde{\Delta}_f / (E - \widetilde{\epsilon}_f ) ],
      with resonance-center energies \widetilde{\epsilon}_{fm} = \widetilde{\epsilon}_f + δ_m where δ_m are the measured CEF excitation energies, and with a single adjustable parameter \widetilde{\Delta}_f > 0 that controls the effective quasiparticle resonance width and thereby the mass renormalization; the proposition is that representing the low-energy 4f contribution to the quasiparticle self-energy by this single-parameter resonance form, with \widetilde{\Delta}_f fixed by experiment, captures the essential renormalization physics (mass enhancement, 4f-derived band formation, and resulting Fermi-surface topology changes) sufficiently accurately to predict the sign and the near-cancellation of band-resolved transverse transport integrals in YbRh2Si2.
      G. Zwicknagl, Adv. Phys. 41, 203 (1992); P. Thalmeier and G. Zwicknagl, Handbook on the Physics and Chemistry of Rare Earths, Vol. 34 (2005).""",
)

gcn_48bba377_specific_heat_calibration = claim(
    r"""In the Friedemann et al. 2010 renormalized-band parametrization for YbRh2Si2 and related heavy-fermion compounds, the single resonance-width parameter is adjusted so that the computed quasiparticle density of states at the Fermi level reproduces the experimentally measured low-temperature electronic specific-heat coefficient; the LKM chain treats this thermodynamic calibration as making the calculated quasiparticle masses, Fermi-surface occupations, and reduced transport integrals reliable indicators of low-temperature transport tendencies [@Friedemann2010].""",
    lkm_id="gcn_48bba377911d4985",
    source_paper="paper:811773737962569729",
    provenance_source="lkm",
    lkm_original=r"""Let \widetilde{\Delta}_f be the single resonance-width parameter of the renormalized-band parametrization introduced above, and let gamma_exp denote the experimentally measured linear coefficient of the low-temperature electronic specific heat C(T) = gamma_exp T; the proposition is that adjusting \widetilde{\Delta}_f so that the computed quasiparticle density of states at the Fermi level N(E_F) reproduces gamma_exp yields an RBC band structure whose quasiparticle effective masses and Fermi-surface occupations are sufficiently accurate that the derived reduced transport integrals \bar{\sigma}_{xx}(i) and \bar{\sigma}_{xyz}(i) and their products with the band occupations \bar{n}(i) provide reliable indicators of the material's low-temperature transport tendencies.""",
)

gcn_42a4ff_rbc_hall_dos_values = claim(
    r"""Renormalized-band calculations constrained by experimental CEF energies and low-temperature specific heat produce two dominant quasiparticle bands for YbRh2Si2 with opposite-sign reduced transverse transport products: band 1 (donut) remains holelike with \bar{n}(1)\bar{\sigma}_{xyz}(1)=+0.0037675, while band 2 (jungle-gym) becomes predominantly electronlike with \bar{n}(2)\bar{\sigma}_{xyz}(2)=-0.0041076, so their nearly equal magnitudes strongly cancel in the numerator of the low-field Hall coefficient. The same calculation gives N(E_F)~=290 states/(eV unit cell) and gamma~=680 mJ mol^-1 K^-2 for YbRh2Si2, and N(E_F)~=48 states/(eV unit cell) and gamma~=113 mJ mol^-1 K^-2 for YbIr2Si2 [@Friedemann2010].""",
    lkm_id="gcn_42a4ff7fd004413f",
    source_paper="paper:811773737962569729",
    provenance_source="lkm",
    lkm_original=r"""Renormalized-band calculations that incorporate a phenomenological 4f-derived quasiparticle resonance (with crystal-electric-field excitation energies taken from experiment and with the resonance width parameter adjusted to reproduce the low-temperature specific-heat coefficient) produce two dominant quasiparticle bands for YbRh2Si2 whose reduced transverse transport integrals have opposite sign: in the heavy-Fermi-liquid renormalized-band (RBC) description band 1 (donut) remains holelike, giving a positive reduced transverse transport integral, while band 2 (jungle-gym) becomes predominantly electronlike, giving a negative reduced transverse transport integral. Expressing the transport contributions in the RBC in terms of the band occupation per unit cell \bar{n}(i) (the number of occupied states per unit cell in band i) and the reduced transverse transport integral \bar{\sigma}_{xyz}(i), the calculated products \bar{n}(i)\bar{\sigma}_{xyz}(i) for YbRh2Si2 are +0.0037675 for band 1 and -0.0041076 for band 2, i.e., two contributions nearly equal in magnitude and opposite in sign so that their sum -- which enters the numerator of the low-field Hall coefficient in the Boltzmann formula -- is strongly cancelled. The same renormalized-band calculation yields a quasiparticle density of states at the Fermi energy N(E_F) ~= 290 states/(eV unit cell) for YbRh2Si2 corresponding to a Sommerfeld coefficient gamma ~= 680 mJ mol^-1 K^-2, while for YbIr2Si2 the RBC gives N(E_F) ~= 48 states/(eV unit cell) and gamma ~= 113 mJ mol^-1 K^-2; these density-of-states values are those computed within the RBC parametrization constrained by thermodynamic data.""",
)

helper_rbc_parameterization_constrained_by_cef_gamma = claim(
    r"""In the Friedemann et al. 2010 YbRh2Si2 renormalized-band calculation, experimental CEF excitation energies set the resonance-center splittings and the single resonance-width parameter is fixed by reproducing the low-temperature specific-heat coefficient, making the calculation a material-specific thermodynamically constrained RBC parametrization [@Friedemann2010].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=[
        "gcn_42a4ff7fd004413f",
        "gcn_c243dcb58cae4418",
        "gcn_48bba377911d4985",
    ],
    lkm_original=r"""Summarize the renormalized band method inputs and parameter determination: transform the $4f$ states into crystalline-electric-field (CEF) eigenstates $|m\rangle$ and introduce resonance-type phase shifts
$\widetilde{\eta}_{f}(E)\simeq\arctan\dfrac{\widetilde{\Delta}_{f}}{E-\widetilde{\epsilon}_{f}}$,
where $\widetilde{\Delta}_{f}$ is the resonance width accounting for the renormalized quasiparticle mass and $\widetilde{\epsilon}_{f}$ the position of the $f$-derived band center; the CEF-split resonance centers are $\widetilde{\epsilon}_{fm}=\widetilde{\epsilon}_{f}+\delta_{m}$ (for the Yb hole analog the sign convention leads to $\widetilde{\epsilon}_{f}<0$ and $\widetilde{\epsilon}_{fm}=\widetilde{\epsilon}_{f}-\delta_{m}$). The single free parameter $\widetilde{\Delta}_{f}$ is fixed by reproducing the experimentally observed low-temperature linear-in-$T$ specific-heat coefficient, thereby grounding the RBC parametrization in thermodynamic data.
[24]""",
)

helper_ybrh2si2_opposite_hall_transport_products = claim(
    r"""For YbRh2Si2 in the Friedemann et al. 2010 heavy-Fermi-liquid RBC calculation, the band-resolved products entering the Hall numerator have opposite signs and nearly equal magnitudes: +0.0037675 for the donut band and -0.0041076 for the jungle-gym band, implying strong cancellation in the low-field Hall coefficient numerator [@Friedemann2010].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_42a4ff7fd004413f"],
    lkm_original=r"""Report the numerical RBC results for YbRh$_2$Si$_2$: the renormalized-band calculation yields for band 1 (donut) a positive reduced transverse transport product $\bar{n}(1)\bar{\sigma}_{xyz}(1)=+0.0037675$ and for band 2 (jungle-gym) a negative product $\bar{n}(2)\bar{\sigma}_{xyz}(2)=-0.0041076$ as listed in the transport-results Table I. These opposite signs indicate that band 1 remains predominantly holelike while band 2 becomes predominantly electronlike in the heavy-Fermi-liquid limit. The near equality in magnitude implies strong cancellation when summing the two contributions in the numerator of $R_{H}$.
Table I""",
)

helper_rbc_dos_gamma_ybrh2si2_ybir2si2 = claim(
    r"""The Friedemann et al. 2010 RBC density-of-states calculation gives N(E_F)~=290 states/(eV unit cell) and gamma~=680 mJ mol^-1 K^-2 for YbRh2Si2, while the same RBC parametrization gives N(E_F)~=48 states/(eV unit cell) and gamma~=113 mJ mol^-1 K^-2 for YbIr2Si2 [@Friedemann2010].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_42a4ff7fd004413f"],
    lkm_original=r"""State the RBC prediction for the renormalized density of states at the Fermi energy and its thermodynamic implication: for YbRh$_2$Si$_2$ the RBC yields $N(E_{F})\approx 290\ \mathrm{states/(eV\ unit\ cell)}$, which corresponds (via the standard relation between DOS and the Sommerfeld coefficient for the electronic specific heat) to a Sommerfeld coefficient $\gamma\approx680\ \mathrm{mJ\ mol^{-1}K^{-2}}$; for YbIr$_2$Si$_2$ RBC gives $N(E_{F})\approx48\ \mathrm{states/(eV\ unit\ cell)}$ and $\gamma\approx113\ \mathrm{mJ\ mol^{-1}K^{-2}}$. These values follow from the calculated renormalized quasiparticle DOS displayed in the RBC results.
Fig. 4""",
)


strat_gfac_0b967f9e875749e8_rbc_hall_dos = deduction(
    [
        gcn_c243dcb_rbc_phase_shift_parametrization,
        gcn_48bba377_specific_heat_calibration,
    ],
    gcn_42a4ff_rbc_hall_dos_values,
    reason=r"""1. Start from the established upstream result that two principal bands (donut $i=1$ and jungle-gym $i=2$) dominate the Hall transport integrals, and aim to determine how inclusion of $4f$-derived quasiparticles in a renormalized-band calculation (RBC) modifies the band-resolved transport integrals and their signs.
2. Summarize the renormalized band method inputs and parameter determination: transform the $4f$ states into crystalline-electric-field (CEF) eigenstates $|m\rangle$ and introduce resonance-type phase shifts
$\widetilde{\eta}_{f}(E)\simeq\arctan\dfrac{\widetilde{\Delta}_{f}}{E-\widetilde{\epsilon}_{f}}$,
where $\widetilde{\Delta}_{f}$ is the resonance width accounting for the renormalized quasiparticle mass and $\widetilde{\epsilon}_{f}$ the position of the $f$-derived band center; the CEF-split resonance centers are $\widetilde{\epsilon}_{fm}=\widetilde{\epsilon}_{f}+\delta_{m}$ (for the Yb hole analog the sign convention leads to $\widetilde{\epsilon}_{f}<0$ and $\widetilde{\epsilon}_{fm}=\widetilde{\epsilon}_{f}-\delta_{m}$). The single free parameter $\widetilde{\Delta}_{f}$ is fixed by reproducing the experimentally observed low-temperature linear-in-$T$ specific-heat coefficient, thereby grounding the RBC parametrization in thermodynamic data.
[24]
3. Compute the renormalized band dispersions $E(i,\mathbf{k})$ using the RBC Hamiltonian and the experimental CEF scheme and resonance widths; from these dispersions evaluate the band-resolved reduced transport integrals $\bar{\sigma}_{xx}(i)$ and $\bar{\sigma}_{xyz}(i)$ as defined by the decomposition
$\sigma_{xx}(i)=\sigma(i)\bar{\sigma}_{xx}(i)$ and $\sigma_{xyz}(i)=\sigma_{B}(i)\bar{\sigma}_{xyz}(i)$
with the prefactors $\sigma(i)=\dfrac{e^{2}}{m}\pi(i)\bar{n}(i)$ and $\sigma_{B}(i)=\dfrac{|e|^{3}}{m^{2}c}[\pi(i)]^{2}\bar{n}(i)$ and $\bar{n}(i)$ the band occupation per unit cell. This defines the reduced-transport products $\bar{n}(i)\bar{\sigma}_{xyz}(i)$ which directly enter the numerator of the Hall coefficient.
(Equations reproduced from the transport decomposition in the paper.)
4. Report the numerical RBC results for YbRh$_2$Si$_2$: the renormalized-band calculation yields for band 1 (donut) a positive reduced transverse transport product $\bar{n}(1)\bar{\sigma}_{xyz}(1)=+0.0037675$ and for band 2 (jungle-gym) a negative product $\bar{n}(2)\bar{\sigma}_{xyz}(2)=-0.0041076$ as listed in the transport-results Table I. These opposite signs indicate that band 1 remains predominantly holelike while band 2 becomes predominantly electronlike in the heavy-Fermi-liquid limit. The near equality in magnitude implies strong cancellation when summing the two contributions in the numerator of $R_{H}$.
Table I
5. State the RBC prediction for the renormalized density of states at the Fermi energy and its thermodynamic implication: for YbRh$_2$Si$_2$ the RBC yields $N(E_{F})\approx 290\ \mathrm{states/(eV\ unit\ cell)}$, which corresponds (via the standard relation between DOS and the Sommerfeld coefficient for the electronic specific heat) to a Sommerfeld coefficient $\gamma\approx680\ \mathrm{mJ\ mol^{-1}K^{-2}}$; for YbIr$_2$Si$_2$ RBC gives $N(E_{F})\approx48\ \mathrm{states/(eV\ unit\ cell)}$ and $\gamma\approx113\ \mathrm{mJ\ mol^{-1}K^{-2}}$. These values follow from the calculated renormalized quasiparticle DOS displayed in the RBC results.
Fig. 4
6. Conclude that in the heavy-Fermi-liquid limit the RBC produces two dominant bands with opposite Hall character for YbRh$_2$Si$_2$, with nearly compensating contributions to the Hall numerator (the products $\bar{n}(i)\bar{\sigma}_{xyz}(i)$ are close in magnitude and opposite in sign), thereby explaining why the total Hall coefficient is expected to be small and highly sensitive to weighting factors (such as band-dependent relaxation times). This explains the RBC-based mechanistic origin of cancellation and near-compensation observed in the numerical transport integrals.
Table I""",
    prior=0.95,
)

strat_decompose_rbc_parameterization = support(
    [gcn_42a4ff_rbc_hall_dos_values],
    helper_rbc_parameterization_constrained_by_cef_gamma,
    reason=(
        "The root LKM claim explicitly states that the RBC incorporates CEF excitation "
        "energies from experiment and adjusts the resonance width to reproduce the "
        "low-temperature specific-heat coefficient; this helper isolates that "
        "method/parameterization component."
    ),
    prior=0.90,
)

strat_decompose_ybrh2si2_hall_products = support(
    [gcn_42a4ff_rbc_hall_dos_values],
    helper_ybrh2si2_opposite_hall_transport_products,
    reason=(
        "The root LKM claim and factor step 4 explicitly give the YbRh2Si2 band-1 "
        "and band-2 reduced transverse transport products and their opposite signs; "
        "this helper isolates the Hall-cancellation component."
    ),
    prior=0.90,
)

strat_decompose_rbc_dos_gamma_values = support(
    [gcn_42a4ff_rbc_hall_dos_values],
    helper_rbc_dos_gamma_ybrh2si2_ybir2si2,
    reason=(
        "The root LKM claim and factor step 5 explicitly give the RBC density-of-states "
        "and Sommerfeld-coefficient values for YbRh2Si2 and YbIr2Si2; this helper "
        "isolates the DOS/gamma component."
    ),
    prior=0.90,
)
