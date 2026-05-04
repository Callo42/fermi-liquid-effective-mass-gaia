# LKM candidates: May 4 Fermi-liquid effective-mass regeneration

Updated discovery queries:

- `YbRh2Si2 effective mass Kondo lattice FCQPT`
- `YbRh2Si2 field dependent effective mass Kondo suppression Fermi liquid`
- `YbRh2Si2 Fermi surface dHvA renormalized band effective mass`
- `YbRh2Si2 Kondo lattice coherence non Fermi liquid effective mass`

Raw match inputs are preserved under `artifacts/lkm-discovery/input/` as `match_may04_*.json`. Evidence files for accepted or checked roots are also preserved there.

## Exactly one starting root

[1] YbRh2Si2 / homogeneous heavy-electron liquid | solve the Landau effective-mass equation and extract `M*(T,B)=S(T,B)/T` | Shaginyan et al. 2010 | Single chain-backed starting root for the regenerated package.

- claim id: `gcn_2741cdef209a457a`
- source: `paper:867752612177379569`
- title: `Energy scales and the non-Fermi liquid behavior in YbRh2Si2`
- evidence file: `input/evidence_gcn_2741cdef209a457a.json`
- total chains: 1
- decision: selected as the only Turn-1 root because it is YbRh2Si2-specific, field/temperature effective-mass centered, and expandable through FCQPT, thermodynamic, Kondo, renormalized-band, and dHvA claims.

## Accepted connected Turn-2 extension roots

Each extension below has `total_chains > 0` and an LKM-backed path to the current YbRh2Si2 graph. The executable DSL uses only LKM claims, direct decompositions, deductions, support, and one equivalence; it does not create parent synthesis claims.

| order | claim id | paper | connected path |
|---:|---|---|---|
| 1 | `gcn_45f24d454cd3448e` | Shaginyan et al. 2009 | Shares the FCQPT inflection/homogeneous Landau effective-mass equation with the starting root; connected by `equivalence()` on the inflection condition and `support()` from T^(-2/3) scaling to the starting effective-mass scheme. |
| 2 | `gcn_42a4ff7fd004413f` | Friedemann et al. 2010 | Connects through YbRh2Si2 thermodynamic calibration of quasiparticle mass/DOS and supports the starting root's density-of-states effective-mass proxy. |
| 3 | `gcn_c38f8ce989fd454a` | Knebel et al. 2006 | Connects to the YbRh2Si2 Fermi-surface/effective-mass branch through dHvA frequencies, cyclotron masses, and LDA mismatch, then through LuRh2Si2 reference support. |
| 4 | `gcn_2b8dd97abcb44d53` | Friedemann et al. 2013 | Connects through the LuRh2Si2 small-FS reference and reanalysis of YbRh2Si2 dHvA branches. |
| 5 | `gcn_b4093fb2f2e44f3b` | Tokiwa et al. 2004 | Connects through field-dependent YbRh2Si2 effective-mass evidence from `A(B)` and gamma estimates; supports the thermodynamic/mass-proxy branch and high-field Kondo-suppression premise. |
| 6 | `gcn_3a1514fde2d54682` | Seiro et al. 2017 | Connects through YbRh2Si2 Kondo-lattice coherence hierarchy and supports the periodic Kondo-lattice ingredient of the high-field Lifshitz mechanism. |
| 7 | `gcn_d8b1b53ca8b44189` | Schaufuss et al. 2008 | Connects through ESR evidence that tracks `m*(B,T)`, gamma-linked quasiparticle behavior, and Kondo-state evolution. |
| 8 | `gcn_4d206f9ebed246c8` | Pfau et al. 2013 | Connects through YbRh2Si2 high-field Kondo suppression, effective-mass reduction, and Lifshitz transitions. |
| 9 | `gcn_b5d9fe70ddb84b9d` | Naren et al. 2013 | Connects through the same high-field Lifshitz/de-renormalization mechanism and supports the Pfau combined interpretation. |
| 10 | `gcn_d10f91dd4b8e4f21` | Rourke et al. 2008 | Connects through LuRh2Si2 small-FS comparison and mass enhancements for YbRh2Si2 dHvA branches. |
| 11 | `gcn_34ce9aa28e054fd1` | Friedemann et al. 2013b | Connects through YbRh2Si2 dHvA/LDA failures and the need for many-body mass/Fermi-surface modeling. |

## Rejected or not accepted

| claim id / topic | evidence status | verdict |
|---|---|---|
| `gcn_800070efac5e476d` He-3 heat-capacity effective mass | chain-backed from prior discovery | Rejected for May 4 rebuild: no chain-backed bridge to the active YbRh2Si2 graph was found, and the user explicitly instructed not to include He-3 without such a bridge. |
| `gcn_7ae79f122f1c4fcb`, `gcn_e4ecd721edd14d3f`, `gcn_29401e4284574aa2`, `gcn_bc46d7d5f5284a0e` Brinkman-Rice/Mott/CeMo2Si2C branches | chain-backed from prior package | Rejected for this connected rebuild: May 3 bridge search found no strong YbRh2Si2-to-Brinkman-Rice/Mott LKM bridge, so retaining them would require agent-only synthesis. |
| `gcn_72cad51e8f544730` TiS2 damping mismatch | chain-backed from prior discovery | Rejected: different material and model-scope problem, no LKM-backed path to the YbRh2Si2 graph. |
| `gcn_d9819ec99cc94f6b` Brinkman-Rice photoemission discriminator | `total_chains=0` | Rejected by chain-backed gate. |
| `gcn_174cfbc169e04bc9` smooth Kondo quasiparticle-weight suppression | `total_chains=0` on evidence fetch | Not accepted as an extension root; its content is represented only where embedded inside chain-backed Pfau/Naren roots. |
| `gcn_e2ac7315fbbf4d60` 3D DOS/effective-mass scaling | `total_chains=0` on evidence fetch | Not accepted as a root. |
| `gcn_b016160b38f34ce7` LDA lacks dynamic correlations | `total_chains=0` standalone | Not accepted as a root; used only as an embedded LKM premise in the chain-backed `gcn_34ce9aa28e054fd1` evidence. |

## Stopping point

The rebuilt package compiles to 89 total knowledge nodes and 46 science-facing source claims in one science-facing connected component. Additional previously available branches would break the connected-root rule or require unsupported synthesis claims, so the package stops at the largest coherent connected graph found in the May 4 pass.
