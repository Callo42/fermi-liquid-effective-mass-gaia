"""paper_knebel2006 -- claims and deductions from Knebel et al. 2006.

Source: Localization of 4 f State in YbRh 2 Si 2 under Magnetic Field and High Pressure: Comparison with CeRh 2 Si 2
DOI: 10.1143/jpsj.75.114709
Authors: G. Knebel | R. Boursier | E. Hassinger | G. Lapertot | P. G. Niklowitz | A. Pourret | B. Salce | J. P. Sanchez | I. Sheikin | P. Bonville | H. Harima | J. Flouquet
Reference key (CSL): Knebel2006
"""

from gaia.lang import claim, deduction, support


ybrh2si2_high_field_dhva_scope = claim(
    r"""In Knebel et al. 2006, the YbRh2Si2 de Haas-van Alphen frequencies and cyclotron masses are measured on high-quality single crystals in steady fields from 12 T to 28 T with H parallel to the crystallographic a axis; because such high fields can polarize the system, suppress correlations, or shift bands, this high-field dHvA spectrum need not coincide with the zero- or low-field Fermi surface most directly relevant to the YbRh2Si2 quantum-critical regime [@Knebel2006].""",
    lkm_id="gcn_5501e18a04cc458e",
    source_paper="paper:812036747075518464",
    provenance_source="lkm",
    lkm_original=r"""The de Haas–van Alphen frequencies and cyclotron masses reported for YbRh2Si2 are measured in steady magnetic fields between 12 T and 28 T, field strengths at which magnetic polarization, suppression of correlations, or field-driven band shifts can modify band energies and quasiparticle renormalization; therefore the high-field dHvA spectrum obtained at these fields can differ from the zero- or low-field Fermi surface that is relevant for quantum‑critical‑point physics.
      Fig.7; Fig.8""",
)


ybrh2si2_itinerant_4f_lda_sensitivity = claim(
    r"""For YbRh2Si2, Knebel et al. 2006 report that LDA/FLAPW band-structure calculations with all 4f electrons treated as itinerant are sensitive to calculational details and to the assumed 4f energy position, making the predicted 4f-derived Fermi-surface topology and angular dependence unreliable enough that an experiment-theory mismatch need not by itself prove intrinsic 4f localization [@Knebel2006].""",
    lkm_id="gcn_f20b1f42f35548fb",
    source_paper="paper:812036747075518464",
    provenance_source="lkm",
    lkm_original=r"""The LDA/FLAPW band-structure calculations that treat all 4f electrons as itinerant are known to be sensitive to calculational details and to predict the 4f energy position and resulting Fermi-surface topology in a way that can be unreliable for 4f-derived orbits; therefore a mismatch between the measured dHvA angular dependence and predictions from itinerant‑4f LDA calculations can arise from methodological shortcomings of those calculations rather than from an intrinsic localization of the 4f electrons.
      Fig.9; Fig.11""",
)


ybrh2si2_dhva_spectrum_lda_mismatch = claim(
    r"""For high-quality YbRh2Si2 single crystals measured by de Haas-van Alphen torque magnetometry in steady fields of 12-28 T with H parallel a, Knebel et al. 2006 observe four fundamental frequencies, 2730 T, 3510 T, 5370 T, and 7050 T, with cyclotron masses (15.0 +/- 0.7) m_e, (8.4 +/- 0.2) m_e, (10.1 +/- 0.2) m_e, and (14.9 +/- 0.9) m_e. The measured basal-plane angular dependence is inconsistent with itinerant-4f LDA/FLAPW calculations for YbRh2Si2 and instead qualitatively resembles LuRh2Si2 LDA calculations with 4f states below the Fermi energy, giving the first experimental Fermi-surface information for YbRh2Si2 and exposing a significant mismatch with one itinerant-4f LDA prediction set [@Knebel2006].""",
    lkm_id="gcn_c38f8ce989fd454a",
    source_paper="paper:812036747075518464",
    provenance_source="lkm",
    lkm_original=r"""De Haas–van Alphen quantum-oscillation measurements performed on high-quality YbRh2Si2 single crystals in steady magnetic fields between 12 T and 28 T with the field applied along the crystallographic a axis (H ∥ a) reveal four clear fundamental frequencies of 2730 T, 3510 T, 5370 T and 7050 T and corresponding cyclotron effective masses m* = (15.0 ± 0.7) m_e, (8.4 ± 0.2) m_e, (10.1 ± 0.2) m_e and (14.9 ± 0.9) m_e (m_e is the free-electron mass); the angular dependence of these measured frequencies in the basal plane is inconsistent with the angular dependences calculated within local‑density‑approximation (LDA) full‑potential augmented‑plane‑wave (FLAPW) band-structure calculations that assume fully itinerant 4f electrons for Yb, whereas the measured angular dependence shows qualitative resemblance to LDA calculations performed for LuRh2Si2 (where 4f states lie well below the Fermi energy), so that the measured oscillation spectrum and effective masses provide the first experimental Fermi-surface information for YbRh2Si2 and reveal a significant mismatch with one set of itinerant-4f band-structure predictions.""",
)


helper_dhva_frequencies_masses_h_parallel_a = claim(
    r"""For YbRh2Si2 at H parallel a in the 12-28 T dHvA window, Knebel et al. 2006 resolve four fundamental oscillation frequencies: 2730 T with m*=(15.0 +/- 0.7) m_e, 3510 T with m*=(8.4 +/- 0.2) m_e, 5370 T with m*=(10.1 +/- 0.2) m_e, and 7050 T with m*=(14.9 +/- 0.9) m_e [@Knebel2006].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_c38f8ce989fd454a"],
    lkm_original=r"""Report the observed dHvA frequency spectrum and its extraction: the oscillatory torque signal for $H\parallel a$ shows reproducible oscillations whose Fourier transform yields four unambiguous frequencies at $2730\ \mathrm{T}$, $3510\ \mathrm{T}$, $5370\ \mathrm{T}$, and $7050\ \mathrm{T}$ from a field window $12$–$28\ \mathrm{T}$; these frequencies correspond to extremal cross-sectional areas of Fermi-surface orbits according to the Onsager relation (frequency $F$ in tesla proportional to extremal area).
Fig.7
Describe how effective masses were determined and report the numerical values: the temperature dependence of each oscillation amplitude follows the Lifshitz–Kosevich thermal damping factor, and fitting that temperature dependence yields cyclotron effective masses $m^{\ast}$ of $(15.0\pm0.7)\,m_{e}$ for $2730\ \mathrm{T}$, $(8.4\pm0.2)\,m_{e}$ for $3510\ \mathrm{T}$, $(10.1\pm0.2)\,m_{e}$ for $5370\ \mathrm{T}$, and $(14.9\pm0.9)\,m_{e}$ for $7050\ \mathrm{T}$, where $m_{e}$ is the free-electron mass.
Fig.7""",
)


helper_dhva_angular_dependence_itinerant_lda_mismatch = claim(
    r"""For YbRh2Si2, the basal-plane angular evolution of the measured dHvA frequencies in Knebel et al. 2006 does not match the LDA/FLAPW angular dependences calculated with itinerant Yb 4f electrons, whose calculated orbits fall mostly below 1 kT or above 10 kT and have markedly different angular shapes; the measured angular dependence instead qualitatively resembles LuRh2Si2 LDA calculations where 4f states lie below the Fermi energy [@Knebel2006].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=["gcn_c38f8ce989fd454a", "gcn_f20b1f42f35548fb"],
    lkm_original=r"""Report the angular dependence of the observed frequencies within the basal plane: the two extreme frequencies (lowest and highest) are observable over the full angular sweep in the basal plane while the two intermediate frequencies are detectable only at small angles near $H\parallel a$; the measured angular dependence of the observed dHvA frequencies in the basal plane is plotted and shows a specific angular variation that is compared to calculated angular dependencies.
Fig.8
Compare experimental angular dependence and frequencies with band-structure calculations and note the mismatch: the experimentally observed frequencies (all in the few-kilotesla range) and their angular evolution are inconsistent with the LDA-calculated angular dependences for $YbRh_{2}Si_{2}$ in which itinerant $4f$ electrons produce calculated frequencies mostly below $1\ \mathrm{kT}$ or above $10\ \mathrm{kT}$, and the shapes of the calculated angular dependencies differ markedly from experiment; by contrast, LDA calculations for $LuRh_{2}Si_{2}$ (where $4f$ are well below $E_{\mathrm{F}}$) produce an angular dependence that shows qualitative similarity to the measured angular dependence, indicating that the measured spectrum does not match itinerant-4f predictions but resembles a Lu-like $4f$-localized reference.
Fig.9; Fig.11""",
)


helper_dhva_first_fs_information_scope = claim(
    r"""The Knebel et al. 2006 dHvA frequencies and heavy cyclotron masses constitute first experimental Fermi-surface information for YbRh2Si2, but the selected LKM chain also records a high-field scope caution and an itinerant-4f LDA-method sensitivity caution when using those data to infer low-field quantum-critical 4f localization [@Knebel2006].""",
    provenance_source="lkm_decomposition",
    derived_from_lkm_ids=[
        "gcn_c38f8ce989fd454a",
        "gcn_5501e18a04cc458e",
        "gcn_f20b1f42f35548fb",
    ],
    lkm_original=r"""Start from the upstream established result: accept as already established the upstream conclusion that LDA band-structure calculations place significant sensitivity of predicted Fermi-surface angular dependence to the $4f$ position and that itinerant-4f LDA angular dependence does not match experiment (upstream conclusion known and available for use).
Define experimental method and conditions for the quantum-oscillation measurements: de Haas–van Alphen (dHvA) measurements were performed on highest-quality single crystals (RRR $\approx300$) at ambient pressure using a cantilever torque meter in steady magnetic fields between $12$ and $28\ \mathrm{T}$ with a dilution refrigerator base temperature of $30\ \mathrm{mK}$; the magnetic field was applied parallel to the crystallographic $a$ axis ($H\parallel a$) for the principal data set.
Conclude the significance of the dHvA measurements: these dHvA frequencies and extracted effective masses constitute the first experimental Fermi-surface information for $YbRh_{2}Si_{2}$; the measured oscillation spectrum and heavy effective masses reveal a significant mismatch with itinerant-4f LDA band-structure predictions, thereby providing experimental constraints that point to intermediate valence and sensitivity of the $4f$ contribution rather than the simple itinerant-$4f$ LDA picture.
Fig.7; Fig.8; Fig.9; Fig.11""",
)


derive_ybrh2si2_dhva_spectrum_lda_mismatch = deduction(
    [
        ybrh2si2_high_field_dhva_scope,
        ybrh2si2_itinerant_4f_lda_sensitivity,
    ],
    ybrh2si2_dhva_spectrum_lda_mismatch,
    reason=r"""1. Start from the upstream established result: accept as already established the upstream conclusion that LDA band-structure calculations place significant sensitivity of predicted Fermi-surface angular dependence to the $4f$ position and that itinerant-4f LDA angular dependence does not match experiment (upstream conclusion known and available for use).
2. Define experimental method and conditions for the quantum-oscillation measurements: de Haas–van Alphen (dHvA) measurements were performed on highest-quality single crystals (RRR $\approx300$) at ambient pressure using a cantilever torque meter in steady magnetic fields between $12$ and $28\ \mathrm{T}$ with a dilution refrigerator base temperature of $30\ \mathrm{mK}$; the magnetic field was applied parallel to the crystallographic $a$ axis ($H\parallel a$) for the principal data set.
3. Report the observed dHvA frequency spectrum and its extraction: the oscillatory torque signal for $H\parallel a$ shows reproducible oscillations whose Fourier transform yields four unambiguous frequencies at $2730\ \mathrm{T}$, $3510\ \mathrm{T}$, $5370\ \mathrm{T}$, and $7050\ \mathrm{T}$ from a field window $12$–$28\ \mathrm{T}$; these frequencies correspond to extremal cross-sectional areas of Fermi-surface orbits according to the Onsager relation (frequency $F$ in tesla proportional to extremal area).
Fig.7
4. Describe how effective masses were determined and report the numerical values: the temperature dependence of each oscillation amplitude follows the Lifshitz–Kosevich thermal damping factor, and fitting that temperature dependence yields cyclotron effective masses $m^{\ast}$ of $(15.0\pm0.7)\,m_{e}$ for $2730\ \mathrm{T}$, $(8.4\pm0.2)\,m_{e}$ for $3510\ \mathrm{T}$, $(10.1\pm0.2)\,m_{e}$ for $5370\ \mathrm{T}$, and $(14.9\pm0.9)\,m_{e}$ for $7050\ \mathrm{T}$, where $m_{e}$ is the free-electron mass.
Fig.7
5. Report the angular dependence of the observed frequencies within the basal plane: the two extreme frequencies (lowest and highest) are observable over the full angular sweep in the basal plane while the two intermediate frequencies are detectable only at small angles near $H\parallel a$; the measured angular dependence of the observed dHvA frequencies in the basal plane is plotted and shows a specific angular variation that is compared to calculated angular dependencies.
Fig.8
6. Compare experimental angular dependence and frequencies with band-structure calculations and note the mismatch: the experimentally observed frequencies (all in the few-kilotesla range) and their angular evolution are inconsistent with the LDA-calculated angular dependences for $YbRh_{2}Si_{2}$ in which itinerant $4f$ electrons produce calculated frequencies mostly below $1\ \mathrm{kT}$ or above $10\ \mathrm{kT}$, and the shapes of the calculated angular dependencies differ markedly from experiment; by contrast, LDA calculations for $LuRh_{2}Si_{2}$ (where $4f$ are well below $E_{\mathrm{F}}$) produce an angular dependence that shows qualitative similarity to the measured angular dependence, indicating that the measured spectrum does not match itinerant-4f predictions but resembles a Lu-like $4f$-localized reference.
Fig.9; Fig.11
7. Conclude the significance of the dHvA measurements: these dHvA frequencies and extracted effective masses constitute the first experimental Fermi-surface information for $YbRh_{2}Si_{2}$; the measured oscillation spectrum and heavy effective masses reveal a significant mismatch with itinerant-4f LDA band-structure predictions, thereby providing experimental constraints that point to intermediate valence and sensitivity of the $4f$ contribution rather than the simple itinerant-$4f$ LDA picture.
Fig.7; Fig.8; Fig.9; Fig.11""",
    prior=0.95,
)


strat_decompose_dhva_frequencies_masses = support(
    [ybrh2si2_dhva_spectrum_lda_mismatch],
    helper_dhva_frequencies_masses_h_parallel_a,
    reason="The selected root explicitly reports the four H-parallel-a frequencies and cyclotron masses; this helper isolates the experimental quantum-oscillation measurement component without adding independent evidence.",
    prior=0.90,
)


strat_decompose_dhva_lda_mismatch = support(
    [ybrh2si2_dhva_spectrum_lda_mismatch],
    helper_dhva_angular_dependence_itinerant_lda_mismatch,
    reason="The selected root and LKM factor step 6 explicitly compare the observed basal-plane angular dependence with itinerant-4f YbRh2Si2 LDA/FLAPW and LuRh2Si2 reference calculations; this helper isolates the experiment-theory mismatch component.",
    prior=0.90,
)


strat_decompose_dhva_scope_caution = support(
    [ybrh2si2_dhva_spectrum_lda_mismatch],
    helper_dhva_first_fs_information_scope,
    reason="The selected root says the measurements provide first experimental Fermi-surface information, while the same chain's premises caution that high-field data and itinerant-4f LDA details limit direct low-field quantum-critical interpretation.",
    prior=0.90,
)
