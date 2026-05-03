# Focused bridge search

Question: can one LKM-backed root connect the YbRh2Si2/material-specific effective-mass cluster to the Brinkman-Rice/Mott-boundary cluster without adding a weak agent-only synthesis bridge?

Search files:

- `input/match_16_bridge_ybrh2si2_brinkman_mott.json`
- `input/match_17_bridge_heavy_fermion_brinkman.json`
- `input/match_18_bridge_fcqpt_brinkman.json`
- `input/match_19_bridge_kondo_breakdown_ybrh2si2.json`
- `input/match_20_bridge_large_fs_heavy_brinkman.json`

Strict bridge filter required all three:

- YbRh2Si2/heavy-fermion/Kondo/FCQPT/Fermi-surface side.
- Brinkman-Rice/Mott/quasiparticle-weight/local-moment side.
- Effective-mass/quasiparticle/Fermi-liquid side.

## Result

No new chain-backed result was strong enough to connect the two existing starmap clusters.

The only strict-filter candidate was:

- `gcn_8a1a27485204457b` from the NiS2 paper, already present as the alternative-mechanisms premise inside `gcn_29401e42_nis2_brinkman_rice`.

Top bridge-adjacent candidates checked:

| claim id | evidence | verdict |
|---|---|---|
| `gcn_45f24d454cd3448e` | `input/evidence_gcn_45f24d454cd3448e.json` | Chain-backed FCQPT effective-mass scaling (`M*(T) ~ T^-2/3`); stays in FCQPT/YbRh2Si2-style heavy-fermion scaling, not a Brinkman-Rice/Mott bridge. |
| `gcn_4d206f9ebed246c8` | `input/evidence_gcn_4d206f9ebed246c8.json` | Chain-backed YbRh2Si2 high-field Kondo suppression / Lifshitz-transition phenomenology; useful future YbRh2Si2 extension, but not a direct bridge to Brinkman-Rice/Mott claims. |
| `gcn_3a1514fde2d54682` | `input/evidence_gcn_3a1514fde2d54682.json` | Chain-backed YbRh2Si2 lattice-Kondo coherence scale; useful future heavy-fermion/Kondo extension, but not a direct Brinkman-Rice/Mott bridge. |
| `gcn_b4093fb2f2e44f3b` | `input/evidence_gcn_b4093fb2f2e44f3b.json` | Chain-backed YbRh2Si2 field suppression of Kondo state through resistivity coefficient `A(B)`; YbRh2Si2-side extension only. |
| `gcn_d9819ec99cc94f6b` | `input/evidence_gcn_d9819ec99cc94f6b.json` | No evidence chains; not admissible as a root. |

## Decision

Keep the graph as-is. Do not add an agent-only bridge and do not add a weak LKM root. The two starmap clusters are scientifically acceptable: one cluster covers thermodynamic/YbRh2Si2 material-specific effective-mass constraints, and the other covers Brinkman-Rice/Mott-boundary heavy-quasiparticle reasoning.
