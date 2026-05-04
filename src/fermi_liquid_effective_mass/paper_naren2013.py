"""paper_naren2013 -- Lifshitz transitions and de-renormalization in YbRh2Si2."""

from gaia.lang import claim, deduction


gcn_6ca2b_ybrh2si2_hall_compensation_scenario = claim(
    r"""In multiband YbRh2Si2, two Fermi-surface sheets undergoing Lifshitz transitions near similar fields can contribute Hall-coefficient changes of opposite sign and comparable magnitude, partially cancelling the total Hall response near B2; the LKM chain treats this as viable but not uniquely established by transport data [@Naren2013].""",
    lkm_id="gcn_6ca2b25227f04480",
    source_paper="paper:867773002954047503",
    provenance_source="lkm",
    lkm_original=r"""In a multiband metal such as YbRh2Si2, if two distinct Fermi-surface sheets each undergo Lifshitz transitions at similar magnetic fields but produce Hall-coefficient changes of opposite sign and comparable magnitude, their net contributions can partially cancel so that the total Hall coefficient R_H shows only a weak or absent signature near the intermediate transition field B2; this compensation scenario is viable given the presence of multiple bands but is not uniquely established by the available transport data.""",
)

gcn_3ba45e_ybrh2si2_thermopower_corrob_lifshitz = claim(
    r"""Thermopower measurements on a YbRh2Si2 sample from the same growth batch as magnetotransport samples show anomalies near 9-11 T and around 9.5 T, corroborating that the magnetotransport anomalies have an electronic-structure origin such as Lifshitz transitions [@Naren2013].""",
    lkm_id="gcn_3ba45e9eb8b44e29",
    source_paper="paper:867773002954047503",
    provenance_source="lkm",
    lkm_original=r"""Thermopower measurements performed on a sample from the same crystal-growth batch as the magnetotransport samples show anomalies at similar magnetic fields, features around 9-11 T and an additional feature near approximately 9.5 T, which corroborates that the transport anomalies observed in magnetotransport have an electronic-structure origin such as Lifshitz transitions.""",
)

gcn_b5d9_ybrh2si2_lifshitz_derenormalization = claim(
    r"""Combining magnetoresistance and Hall data on YbRh2Si2 down to 50 mK and up to 15 T with field-dependent renormalized-band calculations assigns anomalies at B1 about 3 T, B2 about 9 T, and B3 about 11-11.5 T to Zeeman-driven Lifshitz transitions, while Kondo quasiparticle de-renormalization proceeds as a smoother crossover; sharp Fermi-surface topology changes and smooth Kondo-weight suppression therefore coexist with distinct field dependences [@Naren2013].""",
    lkm_id="gcn_b5d9fe70ddb84b9d",
    source_paper="paper:867773002954047503",
    provenance_source="lkm",
    lkm_original=r"""Combining high-resolution magnetotransport data with field-dependent renormalized-band calculations, the experimental anomalies at B1 approximately 3 T, B2 approximately 9 T and B3 approximately 11-11.5 T can be assigned to Zeeman-driven Lifshitz transitions of heavy-fermion bands in narrow field windows, whereas the overall suppression of Kondo quasiparticle weight proceeds as a comparatively smooth crossover over a broader field range. The data support coexistence of sharp Fermi-surface topology changes and smooth Kondo de-renormalization with distinct field dependences in YbRh2Si2.""",
)

strat_gfac_3419693df9e1427e_lifshitz_derenorm = deduction(
    [
        gcn_6ca2b_ybrh2si2_hall_compensation_scenario,
        gcn_3ba45e_ybrh2si2_thermopower_corrob_lifshitz,
    ],
    gcn_b5d9_ybrh2si2_lifshitz_derenormalization,
    reason=r"""1. Use the multiband Hall-compensation scenario to explain why the intermediate B2 feature may appear weak in the total Hall coefficient.
2. Use thermopower anomalies near the same fields to corroborate the electronic-structure origin of the magnetotransport anomalies.
3. Combine magnetoresistance/Hall data with field-dependent renormalized-band calculations that track van-Hove peak positions and Fermi-surface topology.
4. Assign B1, B2, and B3 anomalies to Lifshitz transitions in heavy-fermion bands.
5. Distinguish these narrow topology changes from the broader smooth Kondo quasiparticle de-renormalization.
6. Conclude that YbRh2Si2 exhibits coexisting sharp Fermi-surface topology changes and smooth Kondo-weight suppression.""",
    prior=0.95,
)
