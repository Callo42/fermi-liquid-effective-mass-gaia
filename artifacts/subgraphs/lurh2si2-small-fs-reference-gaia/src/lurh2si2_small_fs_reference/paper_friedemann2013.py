"""paper_friedemann2013 -- claims and deductions from Friedemann et al. 2013.

Source: Electronic Structure of LuRh2Si2: "Small" Fermi Surface Reference to YbRh2Si2
DOI: 10.48550/arXiv.1305.4555
Authors: Sven Friedemann | Swee K Goh | Patrick M C Rourke | Pascal Reiss |
Michael L Sutherland | F Malte Grosche | Gertrud Zwicknagl | Zachary Fisk
Reference key (CSL): Friedemann2013
"""

from gaia.lang import claim, deduction, support


gcn_c131e014_ybrh2si2_midband_harmonic_assignment = claim(
    r"""In the Friedemann et al. 2013 re-examination of published field-modulation dHvA data on YbRh2Si2, if the angular dependences of observed 5-7 kT peaks match two times lower-frequency branches below 4 kT and the method preferentially enhances harmonics, then the 5-7 kT peaks can be assigned as second, and in some cases higher, harmonics of lower-frequency fundamentals rather than independent fundamental orbits; the assignment is reported as consistent with tabulated frequency and mass comparisons from the published data [@Friedemann2013].""",
    lkm_id="gcn_c131e01470ea48ad",
    source_paper="paper:867761295154217007",
    provenance_source="lkm",
    lkm_original=r"""Let F_{low}(\theta) denote fundamental frequencies below 4\ \mathrm{kT} reported in prior de Haas–van Alphen studies of YbRh_{2}Si_{2} and let F_{mid}(\theta) denote observed peaks between 5\ \mathrm{kT} and 7\ \mathrm{kT}; the proposition is that if the angular dependence F_{mid}(\theta) of the 5–7\ \mathrm{kT} peaks coincides, within experimental uncertainty, with 2\times F_{low}(\theta) (the expected second-harmonic angular dependence) and if the measurement technique used in those studies (field-modulation dHvA) preferentially enhances detection of harmonics relative to fundamentals, then the 5–7\ \mathrm{kT} peaks can be assigned as second harmonics of fundamentals below 4\ \mathrm{kT} rather than as independent fundamental orbits, an assignment that is consistent with the tabulated comparisons of 2\times F and measured frequencies and masses in the published data.
      Refs. 10,13 and Fig. 10(c) in the provided paper""",
)

gcn_3dc248d_ybrh2si2_14kt_not_small_fs = claim(
    r"""For YbRh2Si2 with fields along the (100) direction, Friedemann et al. 2013 define the "small" Fermi surface as an LDA/GGA band-structure calculation in which Yb 4f electrons are core-like and non-hybridizing; if the refined z_Si=0.379 c small-Fermi-surface calculation has no extremal orbit near 14 kT and the measured F_14 ~= 14 kT dHvA peak is an independent fundamental, then the observed 14 kT orbit indicates itinerant Yb 4f participation under the high-field measurement conditions, provided instrumental, magnetic-breakdown, or misassignment alternatives are unlikely [@Friedemann2013].""",
    lkm_id="gcn_3dc248d9752a416c",
    source_paper="paper:867761295154217007",
    provenance_source="lkm",
    lkm_original=r"""Define the "small" Fermi surface as the Fermi surface obtained from band-structure calculations for YbRh_{2}Si_{2} with the Yb 4f electrons treated as core-like (non-hybridizing) in an LDA/GGA calculation; let F_{14}\approx14\ \mathrm{kT} denote an experimentally observed de Haas–van Alphen frequency reported for fields along the (100) direction; the proposition is that if a refined "small" Fermi-surface LDA/GGA calculation performed with z_{Si}=0.379\,c does not predict any extremal orbit with frequency near 14\ \mathrm{kT} for fields along (100), and if the observed F_{14} behaves as an independent fundamental in the experimental data (i.e., it is not a harmonic of a lower-frequency branch), then the presence of F_{14} in the measured spectrum indicates that Yb 4f electrons participate itinerantly in forming the Fermi surface under the measurement conditions (high magnetic fields), i.e., that the experimental Fermi surface is "large" due to f-electron contribution, assuming that alternative explanations (instrumental artefacts, magnetic-breakdown-generated high-frequency orbits, or misassignment) can be excluded or are unlikely.
      Comparison figures and discussion in the provided paper (Fig. 10 and associated text)""",
)

gcn_3a8394c_lurh2si2_small_fs_reference = claim(
    r"""Friedemann et al. 2013 treat LuRh2Si2 as an isostructural, filled-4f-shell reference for the "small" Fermi surface of YbRh2Si2 with core-like non-hybridizing Yb 4f electrons, because the Lu and Yb compounds have nearly identical lattice parameters and non-f conduction-band characters when computed and measured using the experimental z_Si=0.379 c structure [@Friedemann2013].""",
    lkm_id="gcn_3a8394c769864f01",
    source_paper="paper:867761295154217007",
    provenance_source="lkm",
    lkm_original=r"""LuRh_{2}Si_{2} is the isostructural compound to YbRh_{2}Si_{2} with a filled Lu 4f shell whereas YbRh_{2}Si_{2} has a trivalent Yb with one 4f hole; the proposition is that band-structure calculations and quantum-oscillation measurements on LuRh_{2}Si_{2} (performed and computed using the experimentally determined z_{Si}=0.379\,c) provide a valid and sufficiently accurate reference model for the "small" Fermi surface of YbRh_{2}Si_{2} in which the Yb 4f electrons are treated as core-like (non-hybridizing), because the lattice parameters and the non-f conduction-band characters are nearly identical between the two compounds, and therefore discrepancies between Lu- and Yb-based calculations and experiments can be attributed primarily to the presence or absence of Yb 4f hybridization rather than to gross structural differences.""",
)

gcn_2b8dd97_lurh2si2_reference_reanalysis = claim(
    r"""Re-examining published YbRh2Si2 de Haas-van Alphen measurements with the refined LuRh2Si2 "small" Fermi-surface reference calculated at z_Si=0.379 c supports reclassifying published 5-7 kT spectral peaks as harmonics of lower-frequency fundamentals below 4 kT, leaving independent fundamentals below 4 kT plus a distinct high-frequency fundamental near 14 kT; because the refined small-Fermi-surface LDA/GGA calculation with core-like non-hybridizing Yb 4f electrons has no (100)-field orbit near 14 kT, the independent 14 kT experimental orbit supports itinerant Yb 4f contribution to the high-field YbRh2Si2 Fermi surface rather than fully localized 4f behavior [@Friedemann2013].""",
    lkm_id="gcn_2b8dd97abcb44d53",
    source_paper="paper:867761295154217007",
    provenance_source="lkm",
    lkm_original=r"""Re-examination of published de Haas–van Alphen measurements on YbRh_{2}Si_{2}, using the refined LuRh_{2}Si_{2} "small" Fermi-surface reference computed with z_{Si}=0.379\,c and accounting for the strong tendency to generate harmonics and mixed frequencies observed in LuRh_{2}Si_{2}, shows that the published spectral peaks between \approx5\ \mathrm{kT} and \approx7\ \mathrm{kT} can be mapped onto second (and in some cases higher) harmonics of lower-frequency fundamental branches observed below 4\ \mathrm{kT} (the angular dependences and, in two of three reported cases, the effective-mass scalings are consistent with this harmonic assignment as compiled from the published frequency and mass data); this reclassification reduces the set of independent fundamental frequencies in the published YbRh_{2}Si_{2} data to a group below 4\ \mathrm{kT} and a distinct high-frequency fundamental near \sim14\ \mathrm{kT}, and because the refined "small" Fermi-surface LDA/GGA calculation with Yb 4f treated as core-like (non-hybridizing) does not predict an extremal orbit near \sim14\ \mathrm{kT} for fields along the (100) direction, the presence of an independent \sim14\ \mathrm{kT} fundamental in the experimental dHvA data supports the interpretation that Yb 4f electrons contribute itinerantly to the Fermi surface under the measurement conditions (high magnetic fields) rather than being fully localized.""",
)

helper_ybrh2si2_5_7kt_peaks_are_harmonics = claim(
    r"""In the Friedemann et al. 2013 reinterpretation, the YbRh2Si2 dHvA peaks between about 5 kT and 7 kT are treated as harmonics, not independent fundamental Fermi-surface orbits, because their angular dependences and reported masses track multiples of lower-frequency branches below 4 kT [@Friedemann2013].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=[
        "gcn_2b8dd97abcb44d53",
        "gcn_c131e01470ea48ad",
    ],
    lkm_original=r"""Factor steps 2-3 state that frequencies from about 5 kT to 7 kT were compared with integer multiples of fundamentals below about 4 kT; the plotted angular dependences and Table III support assigning the mid-band peaks as second or higher harmonics rather than independent fundamentals.""",
)

helper_ybrh2si2_reduced_fundamental_set = claim(
    r"""After the harmonic reassignment in Friedemann et al. 2013, the independent YbRh2Si2 dHvA frequencies retained by the analysis consist of lower-frequency fundamentals below 4 kT plus a distinct high-frequency fundamental near 14 kT [@Friedemann2013].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=[
        "gcn_2b8dd97abcb44d53",
        "gcn_c131e01470ea48ad",
    ],
    lkm_original=r"""Factor step 3 states that reinterpreting the 5-7 kT peaks as harmonics reduces the independent fundamental frequencies to a group below 4 kT plus a distinct high-frequency fundamental near about 14 kT.""",
)

helper_14kt_orbit_supports_high_field_itinerant_4f = claim(
    r"""In Friedemann et al. 2013, the independent YbRh2Si2 dHvA orbit near 14 kT is treated as evidence for high-field itinerant Yb 4f participation because it is absent from the refined core-4f small-Fermi-surface calculation for fields along (100) [@Friedemann2013].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=[
        "gcn_2b8dd97abcb44d53",
        "gcn_3dc248d9752a416c",
        "gcn_3a8394c769864f01",
    ],
    lkm_original=r"""Factor steps 4-5 state that the refined small-Fermi-surface calculation for core-like Yb 4f electrons does not predict an orbit near 14 kT for fields along (100), while the experimental 14 kT feature behaves as an independent fundamental; the LKM conclusion interprets this as support for high-field Yb 4f contribution to the Fermi surface.""",
)


strat_gfac_468a4122_lurh2si2_reference_reanalysis = deduction(
    [
        gcn_c131e014_ybrh2si2_midband_harmonic_assignment,
        gcn_3dc248d_ybrh2si2_14kt_not_small_fs,
        gcn_3a8394c_lurh2si2_small_fs_reference,
    ],
    gcn_2b8dd97_lurh2si2_reference_reanalysis,
    reason=r"""1. Start from the refined "small" Fermi-surface reference provided by LuRh$_2$Si$_2$ calculations and from the identification that harmonics and magnetic-interaction mixing are prevalent in LuRh$_2$Si$_2$: the previously established calculated "small" Fermi surface for LuRh$_2$Si$_2$ using $z_{\text{Si}}=0.379\,c$ serves as a reference for analogous "small" Fermi-surface calculations on YbRh$_2$Si$_2$ in which the Yb $4f$ electrons are treated as core-like (non-hybridizing), and the presence of many harmonics and mixing products in LuRh$_2$Si$_2$ motivates re-examination of published de Haas-van Alphen (dHvA) data on YbRh$_2$Si$_2$ for possible harmonic assignments.
Fig. 10
[13]
2. Describe the re-analysis procedure and evidence for harmonics in YbRh$_2$Si$_2$: the dHvA frequencies reported previously for YbRh$_2$Si$_2$ were compared to calculated fundamental frequencies of the "small" Fermi-surface calculation and to integer multiples (harmonics) of the low-frequency fundamentals (below $\sim 4\ \mathrm{kT}$); the authors overlay second and higher harmonic angular dependences on the experimental dHvA frequency-versus-angle plot and find that the experimental frequencies in the range approximately $5\ \mathrm{kT}$ to $7\ \mathrm{kT}$ match the angular dependence expected for second harmonics of the lower-frequency fundamentals, as illustrated in the comparison plot and summarized in a table that compares expected harmonic values to measured frequencies and masses.
Fig. 10
Table III
3. Report the reduced set of independent fundamental frequencies implied by the harmonic reassignment: if the frequencies between $\sim 5\ \mathrm{kT}$ and $7\ \mathrm{kT}$ in the published YbRh$_2$Si$_2$ data are reinterpreted as second (or higher) harmonics of fundamentals below $4\ \mathrm{kT}$, then the number of independent fundamental frequencies in YbRh$_2$Si$_2$ is reduced to a set of fundamentals below $4\ \mathrm{kT}$ plus a distinct high-frequency fundamental near $\sim 14\ \mathrm{kT}$ (the latter is not accounted for as a harmonic of the low-frequency group).
Fig. 10
Table III
4. Contrast the high-frequency fundamental with the "small" Fermi-surface prediction and infer $f$-electron involvement: within the refined "small" Fermi-surface calculation for YbRh$_2$Si$_2$ (i.e., treating Yb $4f$ electrons as core-like), no high-frequency orbit near $\sim 14\ \mathrm{kT}$ is predicted for fields along the (100) direction; because the experimentally observed $\sim 14\ \mathrm{kT}$ frequency behaves as an independent fundamental (not a harmonic of lower frequencies) in the dHvA data, its presence indicates that the "small" $f$-core calculation does not account for this orbit, supporting the conclusion that the Yb $4f$ electrons contribute to the Fermi surface at high magnetic fields (i.e., the $4f$ electrons are at least partially itinerant under those conditions rather than fully localized).
Fig. 10
[13]
5. State the authors' interpretive conclusion and suggested further checks: the re-examination reduces the set of independent fundamentals in YbRh$_2$Si$_2$ to low-frequency fundamentals below $4\ \mathrm{kT}$ plus a single high-frequency near $\sim 14\ \mathrm{kT}$; because the refined "small" Fermi-surface calculation does not predict the $\sim 14\ \mathrm{kT}$ orbit for fields along (100), the presence of that high-frequency fundamental supports the conclusion that the Yb $4f$ electrons contribute to the Fermi surface at high magnetic fields rather than being fully localized; the authors also suggest further experimental checks (extended angular range measurements and complementary techniques) to solidify the harmonic assignments.
Fig. 10
[10]""",
    prior=0.95,
)

strat_decompose_ybrh2si2_5_7kt_harmonics = support(
    [gcn_2b8dd97_lurh2si2_reference_reanalysis],
    helper_ybrh2si2_5_7kt_peaks_are_harmonics,
    reason=(
        "The root LKM claim and factor steps 2-3 explicitly identify the 5-7 kT "
        "YbRh2Si2 peaks as second or higher harmonics of branches below 4 kT; "
        "this helper isolates that evidence-grounded component."
    ),
    prior=0.90,
)

strat_decompose_ybrh2si2_fundamental_set = support(
    [gcn_2b8dd97_lurh2si2_reference_reanalysis],
    helper_ybrh2si2_reduced_fundamental_set,
    reason=(
        "The root LKM claim and factor step 3 explicitly state the reduced set of "
        "independent YbRh2Si2 fundamentals after the harmonic reassignment."
    ),
    prior=0.90,
)

strat_decompose_ybrh2si2_14kt_itinerant_4f = support(
    [gcn_2b8dd97_lurh2si2_reference_reanalysis],
    helper_14kt_orbit_supports_high_field_itinerant_4f,
    reason=(
        "The root LKM claim and factor steps 4-5 explicitly connect the independent "
        "14 kT orbit, its absence from the core-4f small-Fermi-surface calculation, "
        "and the high-field itinerant-4f interpretation."
    ),
    prior=0.90,
)
