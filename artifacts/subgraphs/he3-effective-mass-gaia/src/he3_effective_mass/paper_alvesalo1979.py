"""paper_alvesalo1979 -- He-3 heat-capacity claims from Alvesalo et al. 1979.

Source: Observation of Anomalous Heat Capacity in Liquid He 3 near the Superfluid Transition
DOI: 10.1103/physrevlett.43.1509
Authors: T. A. Alvesalo | T. Haavasoja | P. C. Main | M. T. Manninen | J. Ray | Leila M. M. Rehn
Reference key: Alvesalo1979
"""

from gaia.lang import claim, deduction


_ROOT_ORIGINAL = (
    r"Assuming the standard Landau Fermi-liquid relation that the low-temperature "
    r"linear specific-heat coefficient \gamma is proportional to the quasiparticle "
    r"density of states at the Fermi surface (hence proportional to the quasiparticle "
    r"effective mass m^{*}), the measured value \gamma=2.11\ \mathrm{K}^{-1} implies "
    r"an effective-mass ratio m^{*}/m\approx 2.12 (where m is the bare fermion mass) "
    r"and, under the usual formulas that relate the effective mass renormalization to "
    r"the first Landau Fermi-liquid parameter, yields F_{1}\approx 3.36."
)

_GAMMA_LIMIT_ORIGINAL = (
    r"The observed linear-in-temperature behavior of the molar specific heat per mole, "
    r"C/(nR)=\gamma T with \gamma=2.11\pm 0.02\ \mathrm{K}^{-1} for T\gtrsim "
    r"3\ \mathrm{mK}, is assumed to represent the T\to 0 limiting Fermi-liquid "
    r"behavior so that the coefficient \gamma is identified with the standard "
    r"low-temperature Fermi-liquid specific-heat coefficient (i.e., proportional to "
    r"the quasiparticle density of states at the Fermi surface and hence to the "
    r"quasiparticle effective mass), thereby justifying extrapolation of the measured "
    r"\gamma to infer the zero-temperature effective-mass ratio m^{*}/m and the "
    r"Landau parameter F_{1}."
)

_MAPPING_ORIGINAL = (
    r"Within the conventional Landau Fermi-liquid framework for a three-dimensional "
    r"Fermi liquid, the standard mapping that relates the molar specific-heat coefficient "
    r"\gamma to the quasiparticle effective-mass renormalization m^{*}/m and that yields "
    r"the Landau parameter F_{1} from the effective mass is assumed to be valid and "
    r"numerically accurate to within the quoted experimental uncertainties; applying "
    r"these standard relations to the experimentally determined \gamma=2.11\ "
    r"\mathrm{K}^{-1} gives m^{*}/m\approx 2.12 and F_{1}\approx 3.36."
)


gcn_2ee995fe1e674e2a = claim(
    "For the normal-state liquid He-3 setting reported by Alvesalo et al. 1979, "
    "the observed molar specific heat per mole is linear for T >= about 3 mK, "
    "C/(nR) = gamma T with gamma = 2.11 +/- 0.02 K^-1; this measured linear region is "
    "assumed to represent the T -> 0 Fermi-liquid specific-heat coefficient used to "
    "infer m*/m and F1 [@Alvesalo1979].",
    lkm_id="gcn_2ee995fe1e674e2a",
    source_paper="paper:811623956246167556",
    provenance_source="lkm",
    lkm_original=_GAMMA_LIMIT_ORIGINAL,
)

gcn_1587257a956f4d18 = claim(
    "For three-dimensional normal-liquid He-3 in the conventional Landau Fermi-liquid "
    "framework used by Alvesalo et al. 1979, applying the standard mapping from "
    "gamma = 2.11 K^-1 to quasiparticle effective-mass renormalization gives "
    "m*/m approximately 2.12, and using the usual relation between m*/m and the first "
    "Landau parameter gives F1 approximately 3.36 [@Alvesalo1979].",
    lkm_id="gcn_1587257a956f4d18",
    source_paper="paper:811623956246167556",
    provenance_source="lkm",
    lkm_original=_MAPPING_ORIGINAL,
)

gcn_800070efac5e476d = claim(
    "For the normal-state liquid He-3 setting reported by Alvesalo et al. 1979, "
    "assuming the standard Landau Fermi-liquid relation between the low-temperature "
    "linear specific-heat coefficient gamma and the quasiparticle density of states, "
    "the measured gamma = 2.11 K^-1 implies m*/m approximately 2.12 and F1 "
    "approximately 3.36 [@Alvesalo1979].",
    lkm_id="gcn_800070efac5e476d",
    source_paper="paper:811623956246167556",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

he3_gamma_implies_mstar_ratio_2_12 = claim(
    "For the normal-state liquid He-3 setting reported by Alvesalo et al. 1979, "
    "the measured gamma = 2.11 K^-1 implies a quasiparticle effective-mass ratio "
    "m*/m approximately 2.12 under the standard Landau Fermi-liquid mapping "
    "[@Alvesalo1979].",
    lkm_id="gcn_800070efac5e476d",
    source_paper="paper:811623956246167556",
    provenance_source="lkm",
    decomposition_of="gcn_800070efac5e476d",
    lkm_original=_ROOT_ORIGINAL,
)

he3_mstar_ratio_yields_f1_3_36 = claim(
    "For the normal-state liquid He-3 setting reported by Alvesalo et al. 1979, "
    "the inferred effective-mass ratio m*/m approximately 2.12 yields the first "
    "Landau Fermi-liquid parameter F1 approximately 3.36 under the usual relation "
    "between effective-mass renormalization and F1 [@Alvesalo1979].",
    lkm_id="gcn_800070efac5e476d",
    source_paper="paper:811623956246167556",
    provenance_source="lkm",
    decomposition_of="gcn_800070efac5e476d",
    lkm_original=_ROOT_ORIGINAL,
)

strat_gfac_944c3769779445a4 = deduction(
    [gcn_2ee995fe1e674e2a, gcn_1587257a956f4d18],
    gcn_800070efac5e476d,
    reason=r"""1. Take as given the experimentally determined normal-state coefficient $\gamma=2.11\ \mathrm{K}^{-1}$ from the preceding result (the molar specific heat coefficient in the $T\to 0$ limiting normal Fermi-liquid behavior).
2. State the assumption invoked by the authors to map $\gamma$ to quasiparticle effective mass and Landau Fermi-liquid parameters: assume that the observed linear region corresponds to the $T\to 0$ limiting behavior of a Fermi liquid (i.e., that $\gamma$ reflects the quasiparticle density of states at the Fermi surface and scales with the effective mass $m^{*}$).
3. Record the authors' asserted mapping result without reproducing an explicit derivation (the authors give the numerical mapping result directly): using $\gamma=2.11\ \mathrm{K}^{-1}$ and the assumed Fermi-liquid mapping, the inferred quasiparticle effective-mass ratio is $m^{*}/m=2.12$, and the corresponding first Landau Fermi-liquid parameter is $F_{1}=3.36$; the authors present these numerical values as the outcome of the mapping from $\gamma$ to $m^{*}/m$ and $F_{1}$.
4. Note the paper's comparison to earlier work that motivates the significance of these numbers: the reported $\gamma$ is about $30\%$ smaller than values reported earlier by Mota et al. and Abel et al., and the authors remark that around $20\ \mathrm{mK}$ where the experiments overlap the values of $C/(nR T)$ differ by about $23\%$, supporting that these inferred Fermi-liquid parameters represent a substantial revision relative to prior results. [12] [13]""",
    prior=0.95,
)

strat_decompose_root_to_mstar = deduction(
    [gcn_800070efac5e476d],
    he3_gamma_implies_mstar_ratio_2_12,
    reason=(
        "1. The LKM root explicitly contains the component assertion that gamma = "
        "2.11 K^-1 implies m*/m approximately 2.12 for the Alvesalo et al. He-3 "
        "Fermi-liquid analysis."
    ),
    prior=0.95,
)

strat_decompose_root_to_f1 = deduction(
    [gcn_800070efac5e476d],
    he3_mstar_ratio_yields_f1_3_36,
    reason=(
        "1. The LKM root explicitly contains the component assertion that the inferred "
        "effective-mass ratio m*/m approximately 2.12 yields F1 approximately 3.36 "
        "under the usual Landau Fermi-liquid relation."
    ),
    prior=0.95,
)
