"""Leaf-claim priors for the YbRh2Si2 dHvA mass extension subgraph."""

from .paper_knebel2006 import (
    gcn_5501e18a_high_field_dhva_scope,
    gcn_f20b1f42_itinerant_4f_lda_sensitivity,
)


PRIORS = {
    gcn_5501e18a_high_field_dhva_scope: (
        0.84,
        "The high-field caveat is explicitly stated in the selected LKM chain and is physically plausible for a field-tuned heavy-fermion compound, but it is a scope caution rather than a direct measurement in this root; TODO:review",
    ),
    gcn_f20b1f42_itinerant_4f_lda_sensitivity: (
        0.78,
        "The LKM chain ties the itinerant-4f LDA sensitivity to the Knebel et al. comparison figures, but the proposition is methodological and approximation-sensitive, so the direct prior remains below 0.9; TODO:review",
    ),
}
