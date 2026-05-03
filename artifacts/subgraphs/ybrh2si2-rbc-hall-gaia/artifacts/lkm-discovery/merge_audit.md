# Merge audit -- ybrh2si2-rbc-hall-gaia

## Inputs

- Selected root: `gcn_42a4ff7fd004413f`
- Source paper: `paper:811773737962569729` (Friedemann et al. 2010)
- Evidence file: `input/evidence_gcn_42a4ff7fd004413f.json`

## Decisions

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| `gcn_c243dcb58cae4418` / `gcn_48bba377911d4985` | keep distinct | One claim describes the RBC resonance/CEF parametrization; the other describes the thermodynamic calibration and reliability proposition. | Emitted as separate leaf claims with separate priors. |
| Root components (method, Hall products, DOS/gamma) | decompose without merging | The root is compound, but each component is an anchored part of the same selected LKM claim rather than an independent duplicate. | Preserved root and emitted helper claims supported by the root. |
| Existing parent FCQPT homogeneous-isotropic premise / new RBC material-specific premise | no merge | The two claims differ in model scope and source paper; merging would erase the distinction that motivated this extension. | No merge or equivalence emitted; logged as scope suspicion. |

No exact merges were made.
