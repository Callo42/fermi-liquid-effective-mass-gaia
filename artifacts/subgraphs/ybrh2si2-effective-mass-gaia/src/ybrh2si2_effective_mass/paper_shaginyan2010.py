"""paper_shaginyan2010 -- claims and deductions from Shaginyan et al. 2010.

Source: Energy scales and the non-Fermi liquid behavior in YbRh2Si2
DOI: 10.48550/arXiv.1002.3706
Authors: V.R. Shaginyan | M.Ya. Amusia | K.G. Popov | S.A. Artamonov
Reference key (CSL): Shaginyan2010
"""

from gaia.lang import claim, deduction


gcn_677c6c_landau_integral_relation = claim(
    r"""For a homogeneous three-dimensional interacting-fermion system near FCQPT, the temperature-dependent Landau integral relation defines the quasiparticle effective mass M*(T) from the bare mass, Fermi momentum, Landau interaction amplitude, quasiparticle occupation derivative, and a three-dimensional momentum integral; in Shaginyan et al. 2010 this phenomenological equation is used as the numerical starting point when a Landau amplitude exists, quasiparticles remain reasonably well defined, and n(p,T) correctly represents the distribution [@Shaginyan2010].""",
    lkm_id="gcn_677c6c11780945f1",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""For a homogeneous three-dimensional system of interacting fermions near the fermion-condensation quantum phase transition (FCQPT), the quasiparticle effective mass M*(T) can be defined by the temperature-dependent Landau integral relation
      1/M*(T) = 1/m + ∫[(p_F·p_1)/p_F^3] F(p_F,p_1) [∂n(p_1,T)/∂p_1] d p_1/(2π)^3,
      where m is the bare electron mass, p_F is the Fermi momentum, F(p_F,p_1) is the Landau interaction amplitude that parameterizes low-energy quasiparticle interactions, n(p,T) is the quasiparticle occupation number (average occupancy of the single-particle state with momentum p at temperature T), and the momentum integral is over three-dimensional momentum space; this relation is taken as the starting, phenomenological equation for numerical calculations even when M* becomes very large, provided (i) a Landau amplitude F that parameterizes low-energy interactions exists, (ii) quasiparticle excitations remain reasonably well defined (finite lifetime compared with inverse relevant energy scales), and (iii) the occupation function n(p,T) correctly describes the quasiparticle distribution entering the integral.""",
)

gcn_03614e9b_homogeneous_isotropic_model = claim(
    r"""Shaginyan et al. 2010 model YbRh2Si2 and related heavy-fermion compounds by a spatially uniform, isotropic three-dimensional heavy-electron liquid in which quasiparticle quantities depend only on |p| and T; the model deliberately neglects crystal-lattice anisotropy, Brillouin-zone structure, multiple bands, and anisotropic effective masses while treating the approximation as adequate for universal scaling of M*(T,B) and normalized thermodynamic or transport functions [@Shaginyan2010].""",
    lkm_id="gcn_03614e9b5933496a",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""The low-energy electronic state of the material of interest is modeled as a spatially uniform (homogeneous), isotropic heavy-electron (fermion) liquid in three-dimensional momentum space so that quasiparticle quantities depend only on the magnitude p = |p| and temperature T (n(p,T)), and crystal-lattice anisotropy, Brillouin-zone structure, multiple bands, and momentum-space anisotropic effective masses are neglected; this homogeneous isotropic model is used as an adequate representation of the universal scaling behavior of M*(T,B) and of normalized thermodynamic and transport functions for heavy-fermion compounds such as YbRh2Si2.""",
)

gcn_e0c364ff_inflection_fcqpt_condition = claim(
    r"""In the homogeneous isotropic Landau model used by Shaginyan et al. 2010, the Landau interaction amplitude can be tuned so that the self-consistent single-particle spectrum ε(p) has both dε/dp and d²ε/dp² equal to zero at p = p_F, leaving a cubic leading term near p_F and enforcing the FCQPT critical condition 1/M* = 0 at T = 0 [@Shaginyan2010].""",
    lkm_id="gcn_e0c364ff93804e75",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""It is possible to choose the Landau interaction amplitude F(p_F,p_1) so that the self-consistent single-particle spectrum ε(p) obtained from the corresponding Landau functional has an inflection point at the Fermi momentum p_F, i.e. the first and second derivatives of ε(p) with respect to p vanish at p = p_F,
      (dε/dp)|_{p=p_F} = 0,  (d^2ε/dp^2)|_{p=p_F} = 0,
      which implies the lowest nonzero term in the Taylor expansion of ε(p) about p_F is ∝ (p − p_F)^3; imposing these conditions places the system at the fermion-condensation quantum phase transition (FCQPT) critical condition by enforcing 1/M* = 0 at T = 0, and such an amplitude can be tuned in practical model implementations to represent the critical condition rather than being a purely formal construction.""",
)

gcn_6bbfeb95_stable_landau_solutions = claim(
    r"""For the temperature and magnetic-field ranges considered by Shaginyan et al. 2010 for YbRh2Si2, including fields up to about 1.5 T, the homogeneous isotropic Landau integral equation with an inflection-point-enforcing amplitude admits stable numerical solutions for ε(p) and n(p,T) that are robust enough to compute entropy with controlled numerical error [@Shaginyan2010].""",
    lkm_id="gcn_6bbfeb95290d413d",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""The homogeneous isotropic Landau integral equation for the reciprocal effective mass,
      1/M*(T) = 1/m + ∫ K(p_F,p_1;F) [∂n(p_1,T)/∂p_1] dp_1,
      where the kernel K is determined by a chosen Landau amplitude F that enforces an inflection point at p_F, admits stable numerical solutions for the self-consistent single-particle spectrum ε(p) and occupation n(p,T) using standard numerical iterative schemes or matrix-discretization methods; in practice these numerical methods converge for the range of temperatures and magnetic fields considered in the calculations and in the experimental datasets on YbRh2Si2 (magnetic fields up to about 1.5 T), the convergence is robust to discretization and to reasonable variations of the amplitude coefficients, and the resulting solutions are sufficiently resolved to compute thermodynamic quantities such as entropy with controlled numerical error.""",
)

gcn_ecddfefa_fermion_entropy_formula = claim(
    r"""For fermionic quasiparticle excitations whose occupation numbers n(p,T) encode the low-energy statistical state, the entropy per unit volume is given by the Fermi-Dirac combinatorial expression S(T) = -2 ∫[n ln n + (1-n) ln(1-n)] dp/(2π)^3, with spin degeneracy 2 and a three-dimensional momentum integral [@Shaginyan2010].""",
    lkm_id="gcn_ecddfefac84c4b46",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""The thermodynamic entropy per unit volume S(T) of a system of fermionic quasiparticle excitations characterized by occupation numbers n(p,T) is given by the Fermi-Dirac combinatorial expression
      S(T) = −2 ∫ [ n(p,T) ln n(p,T) + (1 − n(p,T)) ln (1 − n(p,T)) ] d p/(2π)^3,
      where the prefactor 2 accounts for spin degeneracy and the momentum integral is over three-dimensional momentum space; this formula yields the entropy of the quasiparticle distribution under the assumption that the occupations n(p,T) encode the full statistical state of the low-energy degrees of freedom.""",
)

gcn_2e693115_entropy_over_temperature_mass = claim(
    r"""Shaginyan et al. 2010 operationally estimate the quasiparticle effective mass M*(T,B) from entropy by M*(T,B) = S(T,B)/T, using consistent units, as a density-of-states-like effective mass measure even in FCQPT crossover or non-Fermi-liquid regimes where the system is not strictly in the low-temperature Landau Fermi-liquid limit [@Shaginyan2010].""",
    lkm_id="gcn_2e69311592b04bcb",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""The quasiparticle effective mass M*(T,B) is operationally estimated from the thermodynamic entropy S(T,B) computed from the quasiparticle occupation numbers by the relation
      M*(T,B) = S(T,B)/T,
      where S(T,B) is the entropy per unit volume (or per particle/mole with consistent units) and T is temperature; this relation is used as an operational measure of an effective density-of-states proportional to an effective mass even in crossover or non-Fermi-liquid regimes near FCQPT where the system is not strictly in the low-temperature Landau Fermi-liquid limit.""",
)

gcn_2741cdef_practical_effective_mass_scheme = claim(
    r"""For YbRh2Si2 in the homogeneous isotropic heavy-electron liquid model of Shaginyan et al. 2010, a practical scheme for field- and temperature-dependent effective mass is to solve the Landau effective-mass integral equation for ε(p) and n(p,T,B), tune the Landau amplitude so ε(p) has an inflection point at p_F and realizes 1/M* = 0 at T = 0, compute entropy from the Fermi-Dirac occupation formula, and extract M*(T,B) = S(T,B)/T; this procedure yields the interpolating and scaling behavior used for the YbRh2Si2 comparison [@Shaginyan2010].""",
    lkm_id="gcn_2741cdef209a457a",
    source_paper="paper:867752612177379569",
    provenance_source="lkm",
    lkm_original=r"""A practical computational scheme for obtaining the temperature- and field-dependent effective mass in a homogeneous heavy-electron liquid is: (i) solve the temperature-dependent Landau integral equation
      1/M*(T,B) = 1/m + ∫[(p_F·p1)/p_F^3] F(p_F,p1;B) [∂n(p1,T,B)/∂p1] d p1/(2π)^3,
      for the self-consistent single-particle spectrum ε(p) and occupation numbers n(p,T,B), where m is the bare electron mass, p_F the Fermi momentum, F(p_F,p1;B) a chosen Landau interaction amplitude possibly dependent on field B, and the momentum integrals are over three-dimensional momentum space; (ii) choose the Landau amplitude coefficients so that ε(p) has an inflection point at p = p_F (i.e., the first and second derivatives dε/dp and d^2ε/dp^2 vanish at p_F), which enforces the fermion-condensation critical condition 1/M* = 0 at T = 0; (iii) compute the thermodynamic entropy S(T,B) per unit volume from the obtained occupations n(p,T,B) using the Fermi-Dirac combinatorial formula S(T,B) = −2 ∫ [n ln n + (1−n) ln(1−n)] d p/(2π)^3 (spin degeneracy 2); and (iv) extract the effective mass operationally via the Landau relation M*(T,B) = S(T,B)/T (with consistent units); this procedure, applied within the homogeneous isotropic heavy-electron liquid model (i.e., neglecting crystal-lattice anisotropy and band structure), yields M*(T,B) exhibiting the interpolating and scaling properties described above.""",
)

strat_gfac_749b6767459b4785_effective_mass_scheme = deduction(
    [
        gcn_677c6c_landau_integral_relation,
        gcn_03614e9b_homogeneous_isotropic_model,
        gcn_e0c364ff_inflection_fcqpt_condition,
        gcn_6bbfeb95_stable_landau_solutions,
        gcn_ecddfefa_fermion_entropy_formula,
        gcn_2e693115_entropy_over_temperature_mass,
    ],
    gcn_2741cdef_practical_effective_mass_scheme,
    reason=r"""1. State the fundamental equation used to compute the temperature- and field-dependent quasiparticle effective mass $M^{*}(T,B)$: the Landau form relating the inverse effective mass to the bare mass $m$ and the quasiparticle distribution, written explicitly as
$$
\frac{1}{M^{*}(T)}=\frac{1}{m}+\int \frac{\mathbf{p}_{F}\cdot\mathbf{p}_1}{p_{F}^{3}}\;F(\mathbf{p}_{F},\mathbf{p}_1)\;\frac{\partial n(p_1,T)}{\partial p_1}\;\frac{d\mathbf{p}_1}{(2\pi)^3},
$$
where $M^{*}(T)$ is the quasiparticle effective mass as a function of temperature $T$, $m$ is the bare electron mass, $\mathbf{p}_F$ is the Fermi momentum vector, $p_F=|\mathbf{p}_F|$, $F(\mathbf{p}_F,\mathbf{p}_1)$ is the Landau interaction amplitude, and $n(p,T)$ is the quasiparticle occupation number. This equation is the starting point for the numerical solution described below.
2. Specify the model assumption for the calculations: use the homogeneous heavy-electron (fermion) liquid model (a spatially uniform system), thereby neglecting crystal-lattice anisotropy; this means the occupation numbers depend only on momentum magnitude $p$ and temperature $T$, $n(p,T)$, and spatial inhomogeneities and band-structure anisotropies are not included.
3. Choose a special form of the Landau interaction amplitude $F(\mathbf{p}_F,\mathbf{p}_1)$ whose coefficients are tuned so that the single-particle spectrum $\varepsilon(p)$ has an inflection point at the Fermi momentum $p_F$; concretely, impose that the first and second derivatives of $\varepsilon(p)$ with respect to $p$ vanish at $p=p_F$, i.e. $\left.\frac{d\varepsilon}{dp}\right|_{p=p_F}=0$ and $\left.\frac{d^2\varepsilon}{dp^2}\right|_{p=p_F}=0$, where $\varepsilon(p)$ is the single-particle spectrum and $p$ is momentum. The vanishing of the first derivative is equivalent to $1/M^{*}=0$ at the QCP, and the vanishing of two derivatives ensures the lowest nonzero term in the Taylor expansion of $\varepsilon(p)$ about $p_F$ is proportional to $(p-p_F)^3$. This choice enforces that the system is placed at the fermion-condensation quantum phase transition (FCQPT) critical condition for the calculation. [12][15]
[12]
4. Solve the Landau integral equation given in the first step numerically (the temperature-dependent Landau equation reproduced there) with the specially chosen Landau amplitude from the previous step. The numerical solution yields the single-particle spectrum $\varepsilon(p)$ and the temperature-dependent occupation numbers $n(p,T)$ consistent with the interaction amplitude and imposed inflection-point condition; these are obtained for given external parameters $T$ and magnetic field $B$ (with $B$ entering via Zeeman splitting and through the dependence of $n(p,T)$ and the amplitude on polarization, implemented as in the computational scheme described).
[15]
5. Compute the thermodynamic entropy $S(B,T)$ from the occupation numbers $n(p,T)$ using the combinatorial formula for the entropy of a system of fermionic quasiparticles,
$$
S=-2\int\Bigl[n(p)\ln n(p)+(1-n(p))\ln(1-n(p))\Bigr]\frac{d\mathbf{p}}{(2\pi)^3},
$$
where $S$ is the entropy at given magnetic field $B$ and temperature $T$, $n(p)=n(p,T)$ is the quasiparticle occupation number, and the factor $-2$ accounts for spin degeneracy. This formula gives $S(B,T)$ directly from the computed $n(p,T)$.
6. Extract the effective mass $M^{*}(T,B)$ from the computed entropy using the Landau relation connecting entropy and effective mass in a Fermi liquid, written explicitly as
$$
M^{*}(T,B)=\frac{S(T,B)}{T},
$$
where $S(T,B)$ is the entropy per mole (or per particle, depending on units) computed in the previous step and $T$ is temperature. This relation is applied to obtain $M^{*}(T,B)$ from the numerically computed $S(T,B)$ for each $(T,B)$ point.
7. Normalize the computed effective mass $M^{*}(T,B)$ by its maximum value $M_{M}^{*}$ occurring at the temperature $T=T_M$ for a given $B$, and introduce the normalized temperature $y=T/T_M$; the normalized effective mass is $M_N^{*}(y)=M^{*}(T,B)/M_{M}^{*}$. Use these normalized quantities to examine the interpolating/scaling properties of the computed $M^{*}(T,B)$ and to compare directly with experiment on a common dimensionless axis. The computed normalized entropy and normalized effective mass as functions of normalized variables show collapse onto single curves, corroborating the scaling picture (this computed normalized entropy behavior is presented graphically in the calculations shown).
Fig. 3
8. State the practical computational scheme in a concise sequence usable for reproducing theoretical curves and for comparison with experiments: (i) choose a Landau amplitude whose coefficients produce an inflection point in $\varepsilon(p)$ at $p_F$ (first two derivatives zero); (ii) numerically solve the temperature-dependent Landau equation reproduced above to obtain $\varepsilon(p)$ and $n(p,T)$; (iii) compute the entropy $S(B,T)$ from $n(p,T)$ using the combinatorial entropy formula reproduced above; (iv) obtain $M^{*}(T,B)$ by $M^{*}=S/T$ and construct normalized quantities $M_N^{*}=M^{*}/M_{M}^{*}$ and $y=T/T_M$ for scaling analysis. This scheme is implemented within the homogeneous heavy-electron liquid model (neglecting crystal-lattice anisotropy) and yields $M^{*}(T,B)$ exhibiting the interpolating and scaling properties used elsewhere in the paper.""",
    prior=0.95,
)
