"""Leaf-claim priors for the Mott entropy/effective-mass Gaia package."""

from .paper_capone2001 import (
    gcn_31bc66ca16a44508,
    gcn_795699f572b24ed5,
    gcn_dd12256615264dfb,
)


PRIORS = {
    gcn_31bc66ca16a44508: (
        0.82,
        "Fermi-liquid entropy scaling premise from the selected LKM chain; credible within the stated quasiparticle/coherence-scale assumptions but sensitive to the absence of other low-energy entropy carriers; TODO:review",
    ),
    gcn_795699f572b24ed5: (
        0.78,
        "Luttinger-pinning premise from the selected LKM chain for a metallic Fermi-liquid solution of the specified Hamiltonian; plausible but conditional on the solution remaining a conventional FL up to the transition; TODO:review",
    ),
    gcn_dd12256615264dfb: (
        0.80,
        "Conditional entropy-mismatch premise from the selected LKM chain; strong as a thermodynamic argument under fixed-mu/no-symmetry-breaking assumptions, but it is exactly where alternative transition routes must be reviewed; TODO:review",
    ),
}
