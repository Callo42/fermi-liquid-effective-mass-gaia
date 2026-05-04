"""cross_paper -- LKM-backed operators connecting the YbRh2Si2 graph."""

from gaia.lang import equivalence, support

from .paper_shaginyan2010 import (
    fcqpt_inflection_critical_condition,
    entropy_over_temperature_mass_proxy,
    ybrh2si2_entropy_effective_mass_scheme,
)
from .paper_shaginyan2009 import (
    fcqpt_cubic_spectrum_condition,
    fcqpt_t_minus_two_thirds_mass_scaling,
)
from .paper_friedemann2010 import (
    ybrh2si2_rbc_hall_dos_gamma_values,
    rbc_specific_heat_calibration,
)
from .paper_knebel2006 import (
    ybrh2si2_dhva_spectrum_lda_mismatch,
    helper_dhva_angular_dependence_itinerant_lda_mismatch,
)
from .paper_friedemann2013 import (
    ybrh2si2_lurh2si2_reference_reanalysis,
    lurh2si2_small_fs_reference,
)
from .paper_tokiwa2004 import ybrh2si2_resistivity_mass_drop
from .paper_seiro2017 import ybrh2si2_kondo_lattice_hierarchy
from .paper_schaufuss2008 import ybrh2si2_esr_heavy_quasiparticles
from .paper_pfau2013 import (
    ybrh2si2_kondo_lifshitz_interplay,
    ybrh2si2_smooth_kondo_mass_suppression,
)
from .paper_naren2013 import ybrh2si2_lifshitz_derenormalization
from .paper_rourke2008 import ybrh2si2_small_fs_mass_enhancement
from .paper_friedemann2013_field import ybrh2si2_many_body_methods_required


eq_fcqpt_inflection_condition = equivalence(
    fcqpt_inflection_critical_condition,
    fcqpt_cubic_spectrum_condition,
    reason=(
        "Both LKM-backed claims state the same FCQPT inflection-point condition: "
        "the first two derivatives of epsilon(p) vanish at p_F and the cubic term "
        "is the leading nonzero term. The 2010 chain uses it in the YbRh2Si2 "
        "effective-mass scheme; the 2009 chain uses it to derive T^(-2/3) scaling."
    ),
    prior=0.93,
)

sx_fcqpt_scaling_to_start_root = support(
    [fcqpt_t_minus_two_thirds_mass_scaling],
    ybrh2si2_entropy_effective_mass_scheme,
    reason=(
        "The Shaginyan 2009 LKM chain derives the FCQPT/NFL T^(-2/3) effective-mass "
        "solution from the same homogeneous Landau effective-mass equation and "
        "inflection condition used inside the Shaginyan 2010 YbRh2Si2 procedure. "
        "This supports the FCQPT scaling component of the starting root without "
        "adding a parent synthesis claim."
    ),
    prior=0.82,
)

sx_rbc_calibration_to_entropy_mass = support(
    [rbc_specific_heat_calibration, ybrh2si2_rbc_hall_dos_gamma_values],
    entropy_over_temperature_mass_proxy,
    reason=(
        "Friedemann 2010 LKM evidence independently uses YbRh2Si2 low-temperature "
        "specific heat and density of states to calibrate quasiparticle masses. "
        "That chain supports the starting root's use of thermodynamic entropy or "
        "specific-heat-like density-of-states quantities as an operational "
        "effective-mass proxy in YbRh2Si2."
    ),
    prior=0.78,
)

sx_lurh_reference_to_knebel_mismatch = support(
    [lurh2si2_small_fs_reference],
    helper_dhva_angular_dependence_itinerant_lda_mismatch,
    reason=(
        "Friedemann 2013 LKM evidence establishes LuRh2Si2 as a small-FS reference "
        "for YbRh2Si2; Knebel 2006 LKM evidence reports that the YbRh2Si2 dHvA "
        "angular dependence resembles the LuRh2Si2 reference more than itinerant-4f "
        "YbRh2Si2 LDA. The source claims therefore connect through the same "
        "LuRh2Si2-reference comparison."
    ),
    prior=0.84,
)

sx_rourke_to_friedemann_reanalysis = support(
    [ybrh2si2_small_fs_mass_enhancement],
    ybrh2si2_lurh2si2_reference_reanalysis,
    reason=(
        "Rourke 2008 supplies chain-backed high-field dHvA evidence that a "
        "LuRh2Si2-like small-FS D sheet matches observed YbRh2Si2 branches and "
        "implies order-ten mass enhancement. Friedemann 2013 reuses the LuRh2Si2 "
        "small-FS reference to reinterpret YbRh2Si2 dHvA branches, so the former "
        "supports the latter's reference-frame choice."
    ),
    prior=0.82,
)

sx_knebel_friedemann_to_many_body_need = support(
    [
        ybrh2si2_dhva_spectrum_lda_mismatch,
        ybrh2si2_lurh2si2_reference_reanalysis,
    ],
    ybrh2si2_many_body_methods_required,
    reason=(
        "Knebel 2006 and Friedemann 2013 both provide LKM-backed YbRh2Si2 dHvA "
        "evidence where simple LDA/f-core or itinerant-4f descriptions are "
        "insufficient or strongly qualified. Those source claims directly support "
        "the Friedemann 2013 published conclusion that quantitative mass and "
        "Fermi-surface modeling needs many-body renormalization."
    ),
    prior=0.86,
)

sx_transport_mass_to_smooth_kondo = support(
    [ybrh2si2_resistivity_mass_drop],
    ybrh2si2_smooth_kondo_mass_suppression,
    reason=(
        "Tokiwa 2004 reports a high-field reduction of the YbRh2Si2 Fermi-liquid "
        "A coefficient and the inferred effective-mass scale. Pfau 2013 uses "
        "field-driven Kondo suppression as the mass-reduction ingredient in the "
        "same material and field regime, so the transport mass evidence supports "
        "that ingredient while preserving the step-like versus smooth distinction "
        "in the audit log."
    ),
    prior=0.74,
)

sx_kondo_hierarchy_to_pfau = support(
    [ybrh2si2_kondo_lattice_hierarchy],
    ybrh2si2_kondo_lifshitz_interplay,
    reason=(
        "Seiro 2017 gives chain-backed temperature hierarchy evidence for when "
        "YbRh2Si2 lattice Kondo correlations dominate low-energy properties. Pfau "
        "2013's mechanism requires periodic Kondo-lattice coherence in the same "
        "compound, so this source supports that ingredient."
    ),
    prior=0.76,
)

sx_esr_to_kondo_hierarchy = support(
    [ybrh2si2_esr_heavy_quasiparticles],
    ybrh2si2_kondo_lattice_hierarchy,
    reason=(
        "The ESR LKM chain identifies coherent heavy quasiparticles below the "
        "single-ion Kondo scale and ties ESR observables to m*(B,T). That evidence "
        "supports Seiro 2017's chain-backed separation between Kondo onset and the "
        "lower-temperature lattice-dominated regime."
    ),
    prior=0.75,
)

sx_naren_to_pfau = support(
    [ybrh2si2_lifshitz_derenormalization],
    ybrh2si2_kondo_lifshitz_interplay,
    reason=(
        "Naren 2013 separately states the same YbRh2Si2 field phenomenology in a "
        "chain-backed form: narrow Lifshitz anomalies coexist with smoother Kondo "
        "de-renormalization. This directly supports Pfau 2013's combined "
        "Kondo-suppression/Lifshitz interpretation."
    ),
    prior=0.88,
)

sx_rbc_to_many_body_need = support(
    [ybrh2si2_rbc_hall_dos_gamma_values],
    ybrh2si2_many_body_methods_required,
    reason=(
        "Friedemann 2010 provides LKM-backed renormalized-band calculations for "
        "YbRh2Si2 masses, DOS, and Hall transport. Friedemann 2013b concludes that "
        "quantitative YbRh2Si2 Fermi-surface and mass modeling requires many-body "
        "renormalization beyond static LDA. The RBC result is direct source "
        "evidence for the kind of many-body method named by that conclusion."
    ),
    prior=0.82,
)

sx_transport_mass_to_entropy_mass_proxy = support(
    [ybrh2si2_resistivity_mass_drop],
    entropy_over_temperature_mass_proxy,
    reason=(
        "Tokiwa 2004 gives LKM-backed YbRh2Si2 field-dependent effective-mass "
        "evidence through the Fermi-liquid A coefficient and gamma estimate. The "
        "Shaginyan 2010 premise uses entropy over temperature as a density-of-states "
        "effective-mass proxy in the same compound. This supports the broader "
        "thermodynamic effective-mass proxy while keeping the transport and entropy "
        "routes distinct in the audit log."
    ),
    prior=0.72,
)

sx_esr_to_entropy_mass_proxy = support(
    [ybrh2si2_esr_heavy_quasiparticles],
    entropy_over_temperature_mass_proxy,
    reason=(
        "Schaufuss 2008 states that YbRh2Si2 ESR parameters track m*(B,T), "
        "N(E_F;B,T), and gamma-linked heavy-quasiparticle behavior. That raw LKM "
        "claim supports the Shaginyan 2010 use of thermodynamic density-of-states "
        "quantities as effective-mass proxies without asserting equivalence."
    ),
    prior=0.70,
)
