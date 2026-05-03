"""Leaf-claim priors for the NiS2 Brinkman-Rice subgraph."""

from .paper_friedemann2016 import gcn_8a1a2748_alternative_mechanisms_assumption


PRIORS = {
    gcn_8a1a2748_alternative_mechanisms_assumption: (
        0.58,
        "Interpretive exclusion premise from the LKM chain: plausible for the selected NiS2 quantum-oscillation argument, but it explicitly depends on alternative spin-fluctuation, electron-phonon, and magnetic-reconstruction mechanisms not independently ruled out by this root JSON; TODO:review",
    ),
}
