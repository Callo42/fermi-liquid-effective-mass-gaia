"""paper_tokiwa2004 -- high-field suppression of YbRh2Si2 effective mass."""

from gaia.lang import claim, deduction


gcn_021fb1_high_field_a_gamma_scaling_assumption = claim(
    r"""For YbRh2Si2, using the low-field empirical scaling A proportional to gamma^2 to estimate gamma at 16 T assumes that the same A/gamma^2 proportionality established up to about 4 T continues to hold at much higher fields [@Tokiwa2004].""",
    lkm_id="gcn_021fb1e050924558",
    source_paper="paper:812369321199140865",
    provenance_source="lkm",
    lkm_original=r"""Let A(B) denote the coefficient of the T^2 term in the low-temperature electrical resistivity rho(T,B) = rho0(B) + A(B) T^2 and let gamma(B) denote the electronic specific-heat coefficient defined by Cel(T,B) = gamma(B) T + ...; although an empirical scaling relation A proportional to gamma^2 has been demonstrated for YbRh2Si2 up to magnetic fields of approximately 4 T in previous work, we assume for the purpose of estimating gamma at 16 T that this proportionality relation continues to hold with the same proportionality constant at much higher fields (for example at 16 T), so that the measured reduction of A(B) at 16 T can be converted into an estimate gamma(16 T) approximately 70 mJ mol-1 K-2 by applying the same A/gamma^2 ratio determined at low fields.""",
)

gcn_24ebf8_ybrh2si2_t2_resistivity_fit_reliability = claim(
    r"""Four-terminal AC resistivity measurements on YbRh2Si2 single crystals fit rho(T,B)=rho0(B)+A(B)T^2 over the reported low-temperature intervals; the LKM chain assumes the fitted A(B) values are reliable enough that systematic finite-temperature and sample effects are small compared with the observed step-like change across B* [@Tokiwa2004].""",
    lkm_id="gcn_24ebf85923cb4ba3",
    source_paper="paper:812369321199140865",
    provenance_source="lkm",
    lkm_original=r"""For four-terminal AC resistivity measurements on single crystals of YbRh2Si2 the measured resistivity is modeled as rho(T,B) = rho0(B) + A(B) T^2 and least-squares fits to this T^2 form are applied over the reported low-temperature interval; we assume that within the temperature range used for the fits the resistivity is well described by the pure T^2 behavior so that the fitted values of A(B) are reliable and that systematic uncertainties from higher-temperature scattering channels, finite-temperature crossovers, and sample-dependent inhomogeneities are small compared to the observed step-like change of A(B) across B*.""",
)

gcn_b4093_ybrh2si2_resistivity_mass_drop = claim(
    r"""For YbRh2Si2 with B perpendicular to c and B>0.06 T, low-temperature resistivity follows rho(T,B)=rho0(B)+A(B)T^2; A(B) drops drastically when B crosses B*=(9.5 +/- 0.5) T, indicating a step-like effective-mass decrease in a Fermi-liquid picture, and the low-field A proportional to gamma^2 scaling estimates gamma(16 T) near 70 mJ mol^-1 K^-2 [@Tokiwa2004].""",
    lkm_id="gcn_b4093fb2f2e44f3b",
    source_paper="paper:812369321199140865",
    provenance_source="lkm",
    lkm_original=r"""In measurements on single crystals of YbRh2Si2 the low-temperature electrical resistivity as a function of temperature T and magnetic field B applied perpendicular to the c axis is described for B > 0.06 T by a Landau Fermi-liquid form rho(T,B) = rho0(B) + A(B) T^2, where rho0(B) is the residual resistivity and A(B) is the transport coefficient; the empirically determined A(B) exhibits a drastic, step-like reduction when B is increased from below to above B* = (9.5 +/- 0.5) T, which indicates a step-like decrease of the quasiparticle effective mass in the Fermi-liquid picture; applying the empirical low-field scaling relation A proportional to gamma^2, where gamma(B) is the electronic specific-heat coefficient defined by Cel(T,B) = gamma(B) T + ..., and using the same A/gamma^2 proportionality constant determined at low fields, the electronic specific-heat coefficient is estimated to be gamma(16 T) approximately 70 mJ mol-1 K-2 at B = 16 T.""",
)

strat_gfac_d438ed7a0cad4d2e_ybrh2si2_mass_drop = deduction(
    [
        gcn_021fb1_high_field_a_gamma_scaling_assumption,
        gcn_24ebf8_ybrh2si2_t2_resistivity_fit_reliability,
    ],
    gcn_b4093_ybrh2si2_resistivity_mass_drop,
    reason=r"""1. Treat the broadened anomaly at B* about 9.5 T and its susceptibility, magnetostriction, and magnetization signatures as prior context.
2. Define the Landau-Fermi-liquid resistivity form rho(T,B)=rho0+A(B)T^2 for B>0.06 T with B perpendicular to c.
3. Fit low-temperature resistivity data to extract A(B).
4. Observe a drastic step-like decrease of A(B) when B crosses B*.
5. Use the earlier empirical YbRh2Si2 relation A proportional to gamma^2.
6. Apply the same A/gamma^2 constant at high field to estimate gamma(16 T) near 70 mJ mol^-1 K^-2.
7. Conclude that the A(B) drop indicates a step-like quasiparticle effective-mass decrease in the Fermi-liquid picture.""",
    prior=0.95,
)
