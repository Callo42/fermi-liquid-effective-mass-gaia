"""Leaf-claim priors for the YbRh2Si2 RBC/Hall extension subgraph."""

from .paper_friedemann2010 import (
    gcn_48bba377_specific_heat_calibration,
    gcn_c243dcb_rbc_phase_shift_parametrization,
)


PRIORS = {
    gcn_c243dcb_rbc_phase_shift_parametrization: (
        0.82,
        "The LKM chain anchors the RBC phase-shift parametrization to established renormalized-band references and to Friedemann et al.'s YbRh2Si2 implementation, but it remains a phenomenological single-width representation of 4f quasiparticles; TODO:review",
    ),
    gcn_48bba377_specific_heat_calibration: (
        0.76,
        "The LKM chain makes the thermodynamic calibration explicit, yet the inference from reproducing gamma_exp to reliable band occupations and transport integrals is approximation-sensitive and not independently checked inside this selected chain; TODO:review",
    ),
}
