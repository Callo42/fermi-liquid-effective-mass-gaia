"""paper_paramanik2013 -- claims and deductions from Paramanik et al. 2013.

Source: Valence fluctuation in CeMo2Si2C
DOI: 10.1016/j.jallcom.2013.05.169
Authors: U.B. Paramanik | Anupam | U. Burkhardt | R. Prasad | C. Geibel |
Z. Hossain
Reference key (CSL): Paramanik2013
"""

from gaia.lang import claim, deduction, support


_KW_PREMISE_ORIGINAL = r"""For a correlated metal characterized at low temperatures by a resistivity coefficient A (defined via ρ(T) = ρ_0 + A T^2) and an electronic specific-heat coefficient γ (defined via C(T) = γ T + ...), the empirical Kadowaki–Woods observation is that the ratio A/γ^2 typically falls near the scale ≈ 1×10^−5 μΩ·cm·(mol·K/mJ)^2 for many heavy-fermion and valence-fluctuating materials, so that proximity of the measured A/γ^2 to this scale is evidence that the standard correlated Fermi-liquid phenomenology applies to the compound.
      K. Kadowaki, S.B. Woods, Solid State Commun. 58 (1986) 507."""

_WILSON_PREMISE_ORIGINAL = r"""For a metal with a temperature-independent low-temperature molar susceptibility χ_FL and Sommerfeld coefficient γ, the Wilson–Sommerfeld ratio defined as R_W = (π^2 k_B^2 χ_FL) / (γ μ_eff^2) (with k_B the Boltzmann constant and μ_eff an effective moment scale) is expected to be of order unity for a correlated Fermi liquid when μ_eff is taken either as the free-ion Ce^{3+} moment μ_eff = 2.54 μ_B (for a 4f^1, J = 5/2 ion) or as a conduction-electron reference value μ_eff = 1.73 μ_B; either choice therefore yields a physically interpretable R_W for judging Fermi-liquid consistency."""

_ROOT_ORIGINAL = r"""Combining the experimentally determined low-temperature resistivity coefficient A = 2.57×10^−3 μΩ·cm·K^−2 and the Sommerfeld coefficient γ = 23.4 mJ mol^−1 K^−2 yields the empirical Kadowaki–Woods ratio A/γ^2 ≈ 0.5×10^−5 μΩ·cm·(mol·K/mJ)^2, comparable to the original Kadowaki–Woods scale observed in many heavy-fermion and valence-fluctuating systems. Using the low-temperature impurity-corrected molar susceptibility value χ_FL ≈ 5.6×10^−4 emu mol^−1 and the measured γ in the Sommerfeld–Wilson ratio defined as R_W = (π^2 k_B^2 χ_FL) / (γ μ_eff^2) (with k_B the Boltzmann constant and μ_eff the effective moment) gives R_W ≈ 0.81 when μ_eff = 2.54 μ_B (the free-ion Ce^{3+} moment) is used, or R_W ≈ 1.7 when μ_eff = 1.73 μ_B (a conduction-electron reference value) is used; both R_W estimates lie in the range expected for correlated Fermi liquids and are therefore consistent with Fermi-liquid phenomenology in the low-temperature state."""


gcn_2dc55af_kw_empirical_scale = claim(
    r"""For low-temperature correlated metals, the empirical Kadowaki-Woods diagnostic compares the resistivity coefficient A from rho(T)=rho_0 + A T^2 with the Sommerfeld coefficient gamma from C(T)=gamma T+..., and A/gamma^2 near 1e-5 muOmega cm (mol K/mJ)^2 is treated by the selected LKM chain as evidence for standard correlated Fermi-liquid phenomenology in heavy-fermion and valence-fluctuating materials [@Paramanik2013].""",
    lkm_id="gcn_2dc55af0490a4727",
    source_paper="paper:813219117229146113",
    provenance_source="lkm",
    lkm_original=_KW_PREMISE_ORIGINAL,
)

gcn_7459a446_wilson_ratio_interpretation = claim(
    r"""For a metal with temperature-independent low-temperature molar susceptibility chi_FL and Sommerfeld coefficient gamma, the selected LKM chain treats the Wilson-Sommerfeld ratio R_W=(pi^2 k_B^2 chi_FL)/(gamma mu_eff^2) as a correlated-Fermi-liquid consistency check when mu_eff is normalized either to the Ce3+ free-ion moment 2.54 mu_B or to the conduction-electron reference value 1.73 mu_B [@Paramanik2013].""",
    lkm_id="gcn_7459a44654dc416e",
    source_paper="paper:813219117229146113",
    provenance_source="lkm",
    lkm_original=_WILSON_PREMISE_ORIGINAL,
)

gcn_bc46d7_cemo_kw_wilson_fl_consistency = claim(
    r"""For CeMo2Si2C in Paramanik et al. 2013, the experimentally determined low-temperature coefficients A=2.57e-3 muOmega cm K^-2, gamma=23.4 mJ mol^-1 K^-2, and impurity-corrected chi_FL~=5.6e-4 emu mol^-1 give A/gamma^2~=0.5e-5 muOmega cm (mol K/mJ)^2 and Wilson-Sommerfeld estimates R_W~=0.81 using mu_eff=2.54 mu_B or R_W~=1.7 using mu_eff=1.73 mu_B; the selected LKM chain concludes that these Kadowaki-Woods and Wilson/Sommerfeld ratios are consistent with correlated Fermi-liquid phenomenology in the low-temperature state [@Paramanik2013].""",
    lkm_id="gcn_bc46d7d5f5284a0e",
    source_paper="paper:813219117229146113",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

helper_cemo_kw_ratio_original_scale = claim(
    r"""For CeMo2Si2C in Paramanik et al. 2013, substituting A=2.57e-3 muOmega cm K^-2 and gamma=23.4 mJ mol^-1 K^-2 gives A/gamma^2~=0.5e-5 muOmega cm (mol K/mJ)^2, which the selected LKM chain describes as essentially the original Kadowaki-Woods scale for heavy-fermion and valence-fluctuating systems [@Paramanik2013].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_bc46d7d5f5284a0e"],
    decomposition_of="gcn_bc46d7d5f5284a0e",
    lkm_original=_ROOT_ORIGINAL,
)

helper_cemo_wilson_ratio_dual_reference = claim(
    r"""For CeMo2Si2C in Paramanik et al. 2013, using chi_FL~=5.6e-4 emu mol^-1 and gamma=23.4 mJ mol^-1 K^-2 in R_W=(pi^2 k_B^2 chi_FL)/(gamma mu_eff^2) gives R_W~=0.81 for mu_eff=2.54 mu_B and R_W~=1.7 for mu_eff=1.73 mu_B, and the selected LKM chain treats both normalizations as physically interpretable correlated-Fermi-liquid estimates [@Paramanik2013].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_bc46d7d5f5284a0e"],
    decomposition_of="gcn_bc46d7d5f5284a0e",
    lkm_original=_ROOT_ORIGINAL,
)

helper_cemo_ratio_consistency_correlated_fl = claim(
    r"""For CeMo2Si2C, the selected LKM chain uses agreement of both empirical diagnostics--A/gamma^2 near the original Kadowaki-Woods scale and Wilson-Sommerfeld ratios of order unity under the two stated mu_eff normalizations--to support the narrower conclusion that low-temperature susceptibility, specific heat, and T^2 resistivity are mutually consistent with correlated Fermi-liquid phenomenology [@Paramanik2013].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_bc46d7d5f5284a0e"],
    decomposition_of="gcn_bc46d7d5f5284a0e",
    lkm_original=_ROOT_ORIGINAL,
)


strat_gfac_19fb01af249a451c_kw_wilson_fl_consistency = deduction(
    [
        gcn_2dc55af_kw_empirical_scale,
        gcn_7459a446_wilson_ratio_interpretation,
    ],
    gcn_bc46d7_cemo_kw_wilson_fl_consistency,
    reason=r"""1. This conclusion starts from the already established low-temperature transport coefficient $A=2.57\times10^{-3}\ \mu\Omega\ \mathrm{cm\ K^{-2}}$ from the fit $\rho(T)=\rho_0+AT^2$, the Sommerfeld coefficient $\gamma=23.4\ \mathrm{mJ/mol\ K^2}$ from the fit $C(T)=\gamma T+\beta T^3$, and the impurity-corrected low-temperature susceptibility $\chi_{\mathrm{FL}}\approx5.6\times10^{-4}\ \mathrm{emu/mol}$ extracted from the corrected susceptibility curve.
Fig. 4; Fig. 6; Fig. 7
2. Within Fermi-liquid theory, the paper states that the coefficient $A$ is related to $\gamma^2$. It then invokes the empirical Kadowaki-Woods ratio
$$
\frac{A}{\gamma^2},
$$
for which heavy-fermion and valence-fluctuating systems are reported to have values of order $1\times10^{-5}\ \mu\Omega\ \mathrm{cm}\ (\mathrm{mol\ K/mJ})^2$.
[38]
3. Using the measured $A$ and $\gamma$, the paper computes
$$
\frac{A}{\gamma^2}=0.5\times10^{-5}\ \mu\Omega\ \mathrm{cm}\ (\mathrm{mol\ K/mJ})^2.
$$
This is described as being essentially the original Kadowaki-Woods value.
4. The paper also notes an alternative scaling proposed by Tsujii, Kontani, and Yoshimura, according to which the ratio scales as $2/N(N-1)$ with $N$ the orbital degeneracy of the $f$ state. For an intermediate-valent Ce system, taking $N=6$ gives $A/\gamma^2=6.7\times10^{-7}\ \mu\Omega\ \mathrm{cm}\ (\mathrm{mol\ K/mJ})^2$. This comparison is quoted, but the text emphasizes that the measured value for $CeMo_2Si_2C$ is at the original Kadowaki-Woods scale.
[39]
5. For susceptibility and specific heat, the paper uses the Wilson-Sommerfeld ratio
$$
R_W=\frac{\pi^2 k_B^2 \chi_{\mathrm{FL}}}{\gamma \mu_{\mathrm{eff}}^2},
$$
where $k_B$ is the Boltzmann constant, $\chi_{\mathrm{FL}}$ is the low-temperature Fermi-liquid susceptibility, $\gamma$ is the Sommerfeld coefficient, and $\mu_{\mathrm{eff}}$ is the effective magnetic moment used in the normalization.
6. Substituting $\chi_{\mathrm{FL}}\approx5.6\times10^{-4}\ \mathrm{emu/mol}$, $\gamma=23.4\ \mathrm{mJ/mol\ K^2}$, and $\mu_{\mathrm{eff}}=2.54\ \mu_B$ as the free $Ce^{3+}$ moment gives
$$
R_W=0.81.
$$
If instead $\mu_{\mathrm{eff}}=1.73\ \mu_B$ is used as for a free conduction electron, the paper states that one gets
$$
R_W=1.7.
$$
7. Because the Kadowaki-Woods ratio is of the expected order and the Wilson ratio is close to the range expected for correlated Fermi liquids, the paper concludes that the low-temperature susceptibility, specific heat, and resistivity are mutually consistent with Fermi-liquid behavior in $CeMo_2Si_2C$.""",
    prior=0.95,
)

strat_decompose_cemo_kw_ratio = support(
    [gcn_bc46d7_cemo_kw_wilson_fl_consistency],
    helper_cemo_kw_ratio_original_scale,
    reason=(
        "The selected LKM root and factor steps 1-4 explicitly give A, gamma, "
        "the computed A/gamma^2 value, and the comparison to the original "
        "Kadowaki-Woods scale; this helper isolates only that grounded component."
    ),
    prior=0.90,
)

strat_decompose_cemo_wilson_ratio = support(
    [gcn_bc46d7_cemo_kw_wilson_fl_consistency],
    helper_cemo_wilson_ratio_dual_reference,
    reason=(
        "The selected LKM root and factor steps 5-6 explicitly define the "
        "Wilson-Sommerfeld ratio and report the two mu_eff-normalized values; "
        "this helper isolates only that grounded component."
    ),
    prior=0.90,
)

strat_decompose_cemo_fl_consistency = support(
    [
        helper_cemo_kw_ratio_original_scale,
        helper_cemo_wilson_ratio_dual_reference,
    ],
    helper_cemo_ratio_consistency_correlated_fl,
    reason=(
        "The selected LKM root and factor step 7 explicitly combine the KW and "
        "Wilson/Sommerfeld diagnostics to conclude mutual consistency among "
        "low-temperature susceptibility, specific heat, and resistivity."
    ),
    prior=0.90,
)
