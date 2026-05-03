"""Leaf-claim priors for the Kondo/Brinkman-Rice extension subgraph."""

from .paper_anderson1984 import (
    gcn_40f111_nozieres_local_fl_kondo_sites,
    gcn_8f275a_brinkman_rice_scope_condition,
)


PRIORS = {
    gcn_40f111_nozieres_local_fl_kondo_sites: (
        0.78,
        "The premise is grounded in Anderson's Nozieres/Friedel-sum-rule argument for screened Kondo ions, but the extrapolation from a single impurity to a periodic lattice is explicitly approximate and inter-site corrections are only bounded qualitatively; TODO:review",
    ),
    gcn_8f275a_brinkman_rice_scope_condition: (
        0.72,
        "The premise is a scoped fixed-point identification rather than a direct measurement: it is plausible when RKKY, direct exchange, and incipient ordering are weak or irrelevant, but those boundary conditions are not independently established inside the selected root chain; TODO:review",
    ),
}
