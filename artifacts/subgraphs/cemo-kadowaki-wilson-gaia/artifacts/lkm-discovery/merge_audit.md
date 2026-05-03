# Merge audit -- cemo-kadowaki-wilson-gaia

| pair | verdict | reason | source pointers |
|---|---|---|---|
| `gcn_2dc55af0490a4727` / `gcn_7459a44654dc416e` | keep distinct | The first premise is the empirical Kadowaki-Woods scale; the second is the Wilson/Sommerfeld-ratio interpretation. They support the same root but assert different diagnostics. | `input/evidence_gcn_bc46d7d5f5284a0e.json` -> factor `gfac_19fb01af249a451c` premises |
| `gcn_bc46d7d5f5284a0e` / decomposition helpers | keep distinct | Helpers are derived component claims for A/gamma^2, Wilson/Sommerfeld estimates, and the narrower FL-consistency synthesis; the original compound root is preserved with its `lkm_original`. | root claim plus factor steps 1-7 |
| CeMo2Si2C KW/Wilson root / parent thermodynamic-route claims | no merge | The parent claims concern He-3 gamma-to-mass and YbRh2Si2 S/T-to-M* routes, not the same proposition as CeMo2Si2C ratio consistency. | parent source read-only context |
| CeMo2Si2C KW/Wilson root / parent correlated-FL RBC claims | no merge | The parent RBC branch is a material-specific YbRh2Si2 band/DOS/Hall calculation; it is thematically related but not semantically identical to the CeMo2Si2C empirical-ratio claim. | parent source read-only context |
