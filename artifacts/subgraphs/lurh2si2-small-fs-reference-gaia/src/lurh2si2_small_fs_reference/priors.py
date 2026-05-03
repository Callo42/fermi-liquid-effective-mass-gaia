"""Leaf-claim priors for the LuRh2Si2 small-FS reference extension subgraph."""

from .paper_friedemann2013 import (
    gcn_3a8394c_lurh2si2_small_fs_reference,
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs,
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment,
)


PRIORS = {
    gcn_c131e014_ybrh2si2_midband_harmonic_assignment: (
        0.78,
        "The LKM chain anchors the 5-7 kT harmonic reassignment to angular-dependence and mass comparisons, but the assignment is a reanalysis of published spectra and remains sensitive to harmonic/mixed-frequency identification; TODO:review",
    ),
    gcn_3dc248d_ybrh2si2_14kt_not_small_fs: (
        0.74,
        "The LKM chain directly states that the refined core-4f small-FS calculation lacks a (100)-field orbit near 14 kT and that the measured peak behaves as a fundamental, but the itinerant-4f inference is conditional on excluding artefact, magnetic-breakdown, and misassignment alternatives; TODO:review",
    ),
    gcn_3a8394c_lurh2si2_small_fs_reference: (
        0.84,
        "The LuRh2Si2 reference premise is grounded in isostructural chemistry, filled Lu 4f shells, refined z_Si=0.379 c structure, and similar non-f conduction-band character, while transfer to YbRh2Si2 is still a reference-model approximation; TODO:review",
    ),
}
