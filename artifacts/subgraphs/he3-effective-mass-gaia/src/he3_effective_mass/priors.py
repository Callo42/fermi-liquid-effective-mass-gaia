"""Leaf-claim priors for the He-3 effective-mass Gaia package."""

from .paper_alvesalo1979 import gcn_1587257a956f4d18, gcn_2ee995fe1e674e2a


PRIORS = {
    gcn_2ee995fe1e674e2a: (
        0.78,
        "Direct calorimetric premise from the LKM chain, but it extrapolates the observed T >= about 3 mK linear region to the T -> 0 Fermi-liquid limit near the superfluid transition; TODO:review",
    ),
    gcn_1587257a956f4d18: (
        0.82,
        "Standard Landau Fermi-liquid mapping premise with values reported in the LKM chain, but the chain records the numerical mapping rather than a full derivation; TODO:review",
    ),
}
