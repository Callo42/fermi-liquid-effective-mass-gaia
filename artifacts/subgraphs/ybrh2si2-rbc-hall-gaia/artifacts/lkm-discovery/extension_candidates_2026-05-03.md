# Graph-guided extension candidates

Search basis: current graph weak point and synthesis claims. The current graph's lowest direct prior is the YbRh2Si2 homogeneous isotropic heavy-electron model premise, and the synthesis cautions against merging standard low-temperature Fermi-liquid reasoning with FCQPT/crossover reasoning. The extension search therefore targeted material-specific heavy-fermion effective mass, Fermi-surface evidence, Brinkman-Rice/Mott physics, and thermodynamic transport ratios.

New LKM match files:

- `input/match_06_graph_brinkman_rice_mott.json`
- `input/match_07_graph_heavy_fermion_scaling.json`
- `input/match_08_graph_kadowaki_woods.json`
- `input/match_09_graph_sommerfeld_heavy_fermion.json`
- `input/match_10_graph_ybrh2si2_anisotropy.json`

Evidence fetch summary: 16 graph-guided candidates were evidence-checked; 11 returned `total_chains > 0`.

## Recommended extension field

**Material-specific heavy-fermion electronic structure and effective mass in YbRh2Si2.**

This is the most relevant field because it directly tests the current graph's weakest premise: whether a homogeneous isotropic heavy-electron model is adequate for YbRh2Si2. It also gives concrete Fermi-surface, cyclotron-mass, renormalized-band, and Sommerfeld-coefficient evidence that can sharpen or qualify the existing FCQPT effective-mass route.

## Ranked chain-backed candidates

[1] YbRh2Si2 renormalized-band/Hall transport | RBC constrained by specific heat gives `N(E_F) ~= 290 states/(eV unit cell)`, `gamma ~= 680 mJ mol^-1 K^-2`, and near-cancellation of band Hall terms | Friedemann et al. 2010 | Most direct material-specific extension of the current YbRh2Si2 branch.

- claim id: `gcn_42a4ff7fd004413f`
- source: `paper:811773737962569729`
- title: `Hall effect measurements and electronic structure calculations on YbRh 2 Si 2 and its reference compounds LuRh 2 Si 2 and YbIr 2 Si 2`
- evidence file: `input/evidence_gcn_42a4ff7fd004413f.json`
- total chains: 1

[2] YbRh2Si2 quantum oscillation masses and 4f localization | dHvA frequencies 2730, 3510, 5370, 7050 T with cyclotron masses 15.0, 8.4, 10.1, 14.9 `m_e`; angular dependence mismatches itinerant-4f LDA | Knebel et al. 2006 | Strong empirical constraint on Fermi-surface topology and effective masses in the same material.

- claim id: `gcn_c38f8ce989fd454a`
- source: `paper:812036747075518464`
- title: `Localization of 4 f State in YbRh 2 Si 2 under Magnetic Field and High Pressure: Comparison with CeRh 2 Si 2`
- evidence file: `input/evidence_gcn_c38f8ce989fd454a.json`
- total chains: 1

[3] Kondo-lattice Brinkman-Rice liquid | Periodic Kondo lattice ground state described as a Brinkman-Rice Fermi-liquid fixed point with large mass renormalization and finite Stoner enhancement | Anderson 1984 | Useful conceptual bridge from heavy-electron mass renormalization to Brinkman-Rice/Mott language.

- claim id: `gcn_7ae79f122f1c4fcb`
- source: `paper:813343302173589505`
- title: `Heavy-electron superconductors, spin fluctuations, and triplet pairing`
- evidence file: `input/evidence_gcn_7ae79f122f1c4fcb.json`
- total chains: 1

[4] Brinkman-Rice Fermi liquid near singlet Mott transition | As `m* -> infinity` and `Z -> 0`, a direct continuous FL-to-singlet-Mott-insulator crossover is impossible without an intervening instability or phase | Capone et al. 2001 | Strong theoretical boundary condition for extending toward Mott physics.

- claim id: `gcn_e4ecd721edd14d3f`
- source: `paper:867770551072981407`
- title: `Direct Transition Between a Singlet Mott Insulator and a Superconductor`
- evidence file: `input/evidence_gcn_e4ecd721edd14d3f.json`
- total chains: 1

[5] Kadowaki-Woods and Wilson ratio in CeMo2Si2C | `A/gamma^2 ~= 0.5e-5` and `R_W ~= 0.81` or `1.7`, consistent with correlated Fermi-liquid phenomenology | Paramanik et al. 2013 | Broadens the thermodynamic-route theme through transport/susceptibility consistency checks, but is less directly tied to YbRh2Si2.

- claim id: `gcn_bc46d7d5f5284a0e`
- source: `paper:813219117229146113`
- title: `Valence fluctuation in CeMo2Si2C`
- evidence file: `input/evidence_gcn_bc46d7d5f5284a0e.json`
- total chains: 1

## Recommendation

Add candidate `[1]` first, and treat `[2]` as the paired follow-up if the graph needs an explicit experiment-vs-model tension inside YbRh2Si2. Candidate `[3]` is the best bridge if the goal shifts toward the NiS2/Brinkman-Rice direction.
