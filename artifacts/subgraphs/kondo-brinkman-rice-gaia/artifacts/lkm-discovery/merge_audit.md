# Merge audit -- kondo-brinkman-rice-gaia

| pair | verdict | reason | source pointers |
|---|---|---|---|
| `gcn_40f11182b5f74ff2` / `gcn_8f275a75866e4923` | keep distinct | One is the Nozieres local Kondo-site Fermi-liquid premise; the other is the scoped Brinkman-Rice fixed-point condition under weak or irrelevant inter-site collective effects. They are complementary premises, not duplicates. | `input/evidence_gcn_7ae79f122f1c4fcb.json` |
| `gcn_7ae79f122f1c4fcb` / decomposition helpers | keep linked, not merged | The helpers isolate grounded components of the compound root. They are derived downstream of the root to avoid treating components as independent evidence. | `src/kondo_brinkman_rice/paper_anderson1984.py` |
| Anderson 1984 Kondo/Brinkman-Rice root / parent YbRh2Si2 RBC branch | keep distinct | Anderson gives a fixed-point identification for Kondo-lattice heavy-electron compounds; the Friedemann branch gives material-specific YbRh2Si2 renormalized-band Hall/DOS values. The latter can qualify concrete band structure without duplicating the former. | parent `src/fermi_liquid_effective_mass/paper_friedemann2010.py` |
| Anderson 1984 Kondo/Brinkman-Rice root / parent Shaginyan FCQPT branch | keep distinct | Brinkman-Rice finite-Stoner fixed point and homogeneous isotropic FCQPT scaling are different regime/model claims. They are not merged and not treated as contradictions in this standalone subgraph. | parent `src/fermi_liquid_effective_mass/paper_shaginyan2010.py` |
