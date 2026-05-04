"""paper_shaginyan2009 -- FCQPT effective-mass scaling evidence."""

from gaia.lang import claim, deduction


gcn_f82c178_fcqpt_inflection_cubic_spectrum = claim(
    r"""At the fermion-condensation quantum phase transition point in a homogeneous heavy-fermion liquid, the first two momentum derivatives of the single-particle spectrum vanish at the Fermi momentum p_F, so the spectrum has an inflection point at p_F and the leading nonzero Taylor term is proportional to (p-p_F)^3 [@Shaginyan2009].""",
    lkm_id="gcn_f82c17897c274163",
    source_paper="paper:811855974460555265",
    provenance_source="lkm",
    lkm_original=r"""At the fermion-condensation quantum phase transition point, the first two momentum derivatives of the single-particle spectrum vanish at the Fermi momentum $p_F$. The spectrum therefore has an inflection point at $p_F$, and the lowest nonvanishing term in the Taylor expansion of $\varepsilon(\mathbf{p})$ about $p_F$ is proportional to $(p-p_F)^3$.""",
)

gcn_58746c_fcqpt_homogeneous_mass_equation = claim(
    r"""At FCQPT, writing n_1(p,T)=n(p,T)-n(p) transforms the Landau effective-mass equation into a form where the zero-temperature inverse effective-mass term vanishes; the resulting homogeneous low-temperature equation has the solution M*(T) proportional to T^(-2/3) [@Shaginyan2009].""",
    lkm_id="gcn_58746c141eb145c4",
    source_paper="paper:811855974460555265",
    provenance_source="lkm",
    lkm_original=r"""Writing the thermal deviation of the quasiparticle distribution as $n_1(\mathbf{p})=n(\mathbf{p},T)-n(\mathbf{p})$, where $n(\mathbf{p})$ is the zero-temperature step function, transforms the Landau effective-mass equation into
$\displaystyle \frac{1}{M^{*}(T)}=\frac{1}{M^{*}}+\int \frac{\mathbf{p}_{F}\mathbf{p}_{1}}{p_{F}^{3}}F(\mathbf{p}_{F},\mathbf{p}_{1})\frac{\partial n_{1}(p_{1},T)}{\partial p_{1}}\frac{d\mathbf{p}_{1}}{(2\pi)^{3}}.$
At the fermion-condensation quantum phase transition, the zero-temperature effective mass diverges, so the first term on the right-hand side vanishes and the equation becomes homogeneous. The low-temperature solution of this homogeneous equation is
$M^{*}(T)\propto T^{-2/3}$.
[13]""",
)

gcn_45f24d_fcqpt_t_minus_two_thirds = claim(
    r"""At FCQPT, where the zero-temperature effective mass diverges and the Landau effective-mass equation becomes homogeneous, the low-temperature solution for a homogeneous heavy-fermion liquid satisfies M*(T) proportional to T^(-2/3); in the non-Fermi-liquid regime near FCQPT, the quasiparticle effective mass therefore decreases with increasing temperature according to this power law [@Shaginyan2009].""",
    lkm_id="gcn_45f24d454cd3448e",
    source_paper="paper:811855974460555265",
    provenance_source="lkm",
    lkm_original=r"""At the fermion-condensation quantum phase transition point, where the zero-temperature effective mass diverges and the Landau effective-mass equation becomes homogeneous, the low-temperature solution for a homogeneous heavy-fermion liquid satisfies
      $
      M^{*}(T)\propto T^{-2/3}.
      $
      Therefore, in the non-Fermi-liquid regime near the fermion-condensation quantum phase transition, the quasiparticle effective mass decreases with increasing temperature according to the power law $T^{-2/3}$.""",
)

strat_gfac_3874d7c0b7a44408_fcqpt_t_scaling = deduction(
    [
        gcn_f82c178_fcqpt_inflection_cubic_spectrum,
        gcn_58746c_fcqpt_homogeneous_mass_equation,
    ],
    gcn_45f24d_fcqpt_t_minus_two_thirds,
    reason=r"""1. Treat the exact inverse effective-mass relation as known and introduce the finite-temperature quasiparticle-distribution deviation n_1(p,T)=n(p,T)-n(p).
2. Invoke the FCQPT condition where the zero-temperature effective mass diverges, making the zero-temperature inverse-mass term vanish and the finite-temperature equation homogeneous.
3. Use the asymptotic low-temperature solution of the homogeneous equation, M*(T) proportional to T^(-2/3), as the non-Fermi-liquid FCQPT effective-mass law.
4. Note that away from FCQPT the system has finite-M*(0) Landau-Fermi-liquid behavior at low T, so the T^(-2/3) law identifies the FCQPT/NFL regime.""",
    prior=0.95,
)
