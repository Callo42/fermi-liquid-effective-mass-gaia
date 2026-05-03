# 100-node extension loop candidates

Goal: grow the final Gaia package toward ~100 total knowledge nodes without adding filler. Selection is based on scientific coherence with the current graph after the Friedemann2010 RBC/Hall extension.

Current graph before this loop:

- total knowledge nodes: 38
- science-facing claims: 21
- current scientific frontiers: material-specific YbRh2Si2 constraints, Fermi-surface/cyclotron-mass evidence, Brinkman-Rice/Mott mass renormalization, thermodynamic/transport signatures of correlated Fermi liquids.

Selected roots for this loop:

1. **YbRh2Si2 dHvA effective masses and 4f localization**
   - claim id: `gcn_c38f8ce989fd454a`
   - evidence: `input/evidence_gcn_c38f8ce989fd454a.json`
   - reason: direct experimental Fermi-surface and cyclotron-mass constraint for the same material as the YbRh2Si2 branches.

2. **LuRh2Si2 small-Fermi-surface reference for YbRh2Si2**
   - claim id: `gcn_2b8dd97abcb44d53`
   - evidence: `input/evidence_gcn_2b8dd97abcb44d53.json`
   - reason: adds a reference-compound comparison useful for interpreting YbRh2Si2 dHvA/RBC claims.

3. **Kondo-lattice Brinkman-Rice liquid**
   - claim id: `gcn_7ae79f122f1c4fcb`
   - evidence: `input/evidence_gcn_7ae79f122f1c4fcb.json`
   - reason: bridges heavy-electron mass renormalization to Brinkman-Rice fixed-point language.

4. **Fermi liquid near singlet Mott transition**
   - claim id: `gcn_e4ecd721edd14d3f`
   - evidence: `input/evidence_gcn_e4ecd721edd14d3f.json`
   - reason: supplies a theoretical boundary condition for divergent effective mass and vanishing quasiparticle weight.

5. **NiS2 Brinkman-Rice correlated Fermi liquid near Mott boundary**
   - claim id: `gcn_29401e4284574aa2`
   - evidence: `input/evidence_gcn_29401e4284574aa2.json`
   - reason: adds experimental large-Fermi-surface plus enhanced-mass evidence in a pressure-tuned Mott-adjacent metal.

6. **Kadowaki-Woods / Wilson ratios in CeMo2Si2C**
   - claim id: `gcn_bc46d7d5f5284a0e`
   - evidence: `input/evidence_gcn_bc46d7d5f5284a0e.json`
   - reason: broadens the thermodynamic-route theme with resistivity/specific-heat/susceptibility consistency checks for correlated Fermi-liquid phenomenology.

Deferred but preserved:

- `gcn_d6a5f201e3874105` (field-induced LFL scaling in HTSC): relevant but broader than the current heavy-fermion/Mott path.
- `gcn_8a68e8f918b54bd9` (Ca3Co4O9 Kadowaki-Woods): useful if the transport-ratio branch needs another independent material.
- `gcn_5f269db6cc3e4841` and `gcn_7e1ddab200e94c11`: relevant Mott/quasiparticle-weight results, but selected Mott and NiS2 roots give a more direct throughline for this loop.
