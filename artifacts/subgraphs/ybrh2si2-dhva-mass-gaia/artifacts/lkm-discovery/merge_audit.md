# Merge audit -- ybrh2si2-dhva-mass-gaia

## Inputs

- Selected root: `gcn_c38f8ce989fd454a`
- Source paper: `paper:812036747075518464` (Knebel et al. 2006)
- Evidence file: `input/evidence_gcn_c38f8ce989fd454a.json`

## Decisions

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| `gcn_5501e18a04cc458e` / `gcn_f20b1f42f35548fb` | keep distinct | The first claim is a high-field dHvA scope caveat; the second is an itinerant-4f LDA methodological-sensitivity caveat. | Emitted as separate leaf claims with separate priors. |
| Root components (frequencies/masses, angular-dependence mismatch, first-FS-information scope) | decompose without merging | The selected root is compound, but each component is anchored in the same root/factor steps rather than independent duplicate evidence. | Preserved root and emitted helper claims supported by the root. |
| dHvA root vs parent FCQPT homogeneous-isotropic model | no merge | The dHvA root is experimental high-field Fermi-surface information; the FCQPT branch is a universal-scaling effective-mass model. | No merge or equivalence emitted; logged as scope/synthesis caution. |
| dHvA root vs Friedemann2010 RBC/Hall/DOS subgraph | no merge | The two are complementary YbRh2Si2 Fermi-surface/effective-mass constraints from different papers and methods, not the same proposition. | No merge or equivalence emitted; logged as synthesis caution. |

No exact merges were made.
