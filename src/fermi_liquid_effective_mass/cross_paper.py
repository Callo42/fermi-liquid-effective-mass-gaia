"""cross_paper -- cautious synthesis across the two selected LKM roots."""

from gaia.lang import claim, support

from .paper_alvesalo1979 import (
    gcn_1587257a956f4d18,
    gcn_800070efac5e476d,
    he3_gamma_implies_mstar_ratio_2_12,
)
from .paper_shaginyan2010 import (
    gcn_03614e9b_homogeneous_isotropic_model,
    gcn_2741cdef_practical_effective_mass_scheme,
    gcn_2e693115_entropy_over_temperature_mass,
)


cross_thermodynamic_routes_to_effective_mass = claim(
    "Across the two selected LKM roots, low-energy thermodynamic quantities are used "
    "as operational routes to quasiparticle effective mass: Alvesalo et al. infer "
    "m*/m for liquid He-3 from the linear specific-heat coefficient gamma, while "
    "Shaginyan et al. extract M*(T,B) for YbRh2Si2 from S(T,B)/T within their "
    "heavy-electron Landau/FCQPT scheme.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_800070efac5e476d",
        "gcn_2e69311592b04bcb",
        "gcn_2741cdef209a457a",
    ],
)

cross_scope_caution_standard_fl_vs_fcqpt = claim(
    "The He-3 and YbRh2Si2 effective-mass routes should not be treated as equivalent "
    "claims: the He-3 chain uses a standard low-temperature Landau Fermi-liquid "
    "mapping from gamma to m*/m, whereas the YbRh2Si2 chain uses a homogeneous "
    "isotropic heavy-electron model near FCQPT and applies S/T as an operational "
    "effective-mass measure through crossover or non-Fermi-liquid regimes.",
    provenance_source="synthesis",
    derived_from_lkm_ids=[
        "gcn_1587257a956f4d18",
        "gcn_03614e9b5933496a",
        "gcn_2e69311592b04bcb",
    ],
)

strat_cross_he3_ybrh2si2_thermodynamic_routes = support(
    [he3_gamma_implies_mstar_ratio_2_12, gcn_2e693115_entropy_over_temperature_mass],
    cross_thermodynamic_routes_to_effective_mass,
    reason=(
        "The He-3 decomposition explicitly grounds gamma -> m*/m, and the YbRh2Si2 "
        "premise explicitly grounds S(T,B)/T -> M*(T,B). Together they support only "
        "the scoped meta-claim that both chains operationalize effective mass through "
        "thermodynamic low-energy quantities, not that the systems or equations are "
        "equivalent."
    ),
    prior=0.84,
)

strat_cross_scope_caution = support(
    [
        gcn_800070efac5e476d,
        gcn_2741cdef_practical_effective_mass_scheme,
        gcn_1587257a956f4d18,
        gcn_03614e9b_homogeneous_isotropic_model,
    ],
    cross_scope_caution_standard_fl_vs_fcqpt,
    reason=(
        "The selected roots and mapping premises specify different systems and "
        "model scopes: standard low-temperature Landau Fermi-liquid reasoning for "
        "normal liquid He-3 versus a homogeneous isotropic heavy-electron FCQPT "
        "crossover model for YbRh2Si2. This warrants a scope-caution claim rather "
        "than equivalence or contradiction."
    ),
    prior=0.88,
)
