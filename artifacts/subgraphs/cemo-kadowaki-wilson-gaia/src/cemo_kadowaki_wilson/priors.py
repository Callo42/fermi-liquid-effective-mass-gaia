"""Leaf-claim priors for the CeMo2Si2C KW/Wilson extension subgraph."""

from .paper_paramanik2013 import (
    gcn_2dc55af_kw_empirical_scale,
    gcn_7459a446_wilson_ratio_interpretation,
)


PRIORS = {
    gcn_2dc55af_kw_empirical_scale: (
        0.82,
        "The premise is a standard empirical correlated-metal diagnostic and is explicitly cited in the LKM chain, but the appropriate KW normalization can depend on degeneracy, carrier density, and material class; TODO:review",
    ),
    gcn_7459a446_wilson_ratio_interpretation: (
        0.74,
        "The Wilson/Sommerfeld-ratio premise is grounded in the chain and gives both Ce3+ and conduction-electron normalizations, but the choice of mu_eff changes the numerical value substantially and remains a review-sensitive convention; TODO:review",
    ),
}
