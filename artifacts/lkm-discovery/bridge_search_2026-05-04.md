# May 4 connected-graph bridge search

Question: can the regenerated package grow from one YbRh2Si2 starting root to about 100 nodes while remaining connected by chain-backed LKM evidence and without executable agent-authored synthesis claims?

## Searches

New raw match files:

- `input/match_may04_ybrh2si2_effective_mass_kondo_fcqpt.json`
- `input/match_may04_ybrh2si2_field_mass_kondo_suppression.json`
- `input/match_may04_ybrh2si2_dhva_rbc_effective_mass.json`
- `input/match_may04_ybrh2si2_kondo_lattice_coherence_nfl.json`

Prior bridge-search files retained:

- `input/match_16_bridge_ybrh2si2_brinkman_mott.json`
- `input/match_17_bridge_heavy_fermion_brinkman.json`
- `input/match_18_bridge_fcqpt_brinkman.json`
- `input/match_19_bridge_kondo_breakdown_ybrh2si2.json`
- `input/match_20_bridge_large_fs_heavy_brinkman.json`

## Accepted bridge paths

| path | accepted evidence |
|---|---|
| Starting FCQPT root -> FCQPT T^(-2/3) scaling | `gcn_2741cdef209a457a` to `gcn_45f24d454cd3448e` through same FCQPT inflection and homogeneous Landau effective-mass equation. |
| Starting root -> RBC thermodynamic mass proxy | `gcn_42a4ff7fd004413f` and `gcn_48bba377911d4985` support the YbRh2Si2 density-of-states/specific-heat effective-mass proxy. |
| RBC/LuRh2Si2/dHvA branch | `gcn_c38f8ce989fd454a`, `gcn_2b8dd97abcb44d53`, `gcn_d10f91dd4b8e4f21`, and `gcn_34ce9aa28e054fd1` connect through YbRh2Si2 dHvA, LuRh2Si2 small-FS reference, LDA mismatch, mass enhancement, and many-body-method requirements. |
| High-field Kondo/mass/Lifshitz branch | `gcn_b4093fb2f2e44f3b`, `gcn_3a1514fde2d54682`, `gcn_d8b1b53ca8b44189`, `gcn_4d206f9ebed246c8`, and `gcn_b5d9fe70ddb84b9d` connect through field-dependent effective mass, Kondo coherence, ESR heavy quasiparticles, and Lifshitz/de-renormalization evidence in YbRh2Si2. |

## Failed or rejected bridge attempts

| candidate | verdict |
|---|---|
| He-3 heat-capacity root (`gcn_800070efac5e476d`) | No chain-backed path to active YbRh2Si2 graph found. Including it would repeat the previous disconnected He-3/YbRh2Si2 graph. |
| Anderson/Capone/NiS2 Brinkman-Rice/Mott branches | Prior strict bridge search found no strong LKM bridge between active YbRh2Si2 and Brinkman-Rice/Mott clusters. Including them would require agent synthesis. |
| CeMo2Si2C KW/Wilson branch | Similar correlated-FL vocabulary but no chain-backed bridge to active YbRh2Si2 evidence. |
| TiS2 damping mismatch root | Chain-backed but different material and model-scope issue; no LKM-backed path to YbRh2Si2 graph. |
| `gcn_d9819ec99cc94f6b`, `gcn_174cfbc169e04bc9`, `gcn_e2ac7315fbbf4d60`, `gcn_b016160b38f34ce7` as standalone roots | Evidence fetches returned `total_chains=0`; not admissible as roots under the hard gate. Embedded premises from chain-backed parent evidence remain admissible inside their parent chains. |

## Decision

Stop at 89 total knowledge nodes, 46 science-facing source claims, and one science-facing connected component. This is below the nominal 100-node target but is the largest coherent connected graph found without adding unsupported bridges or executable synthesis claims.
