# Merge audit

No formal Gaia merge decisions have been made yet. The discovery pass found no exact contradiction or equivalence pairs among the chain-backed candidates.

## Subgraph mapping pass

| pair_or_item | verdict | reason | source pointers |
|---|---|---|---|
| root evidence chain `gcn_2741cdef209a457a` | keep all seven `gcn_*` claims distinct | The six premises describe separate assumptions or components of the computational scheme; the conclusion is the synthesized procedure. Merging would hide independent leaf priors. | `input/evidence_gcn_2741cdef209a457a.json` |
| `gcn_6bbfeb95290d413d` LKM match hit during support search | same as existing leaf, not re-added | The limited support search returned the same premise already present in the root chain. | LKM match query: `YbRh2Si2 effective mass entropy Landau equation` |
| YbRh2Si2 anisotropy / Fermi-surface LKM hits vs homogeneous isotropic model | dismissed as strict contradiction; retained as synthesis suspicion | High-field dHvA and electronic-structure results expose model-scope limitations, but they do not logically negate the claim that an isotropic model is used for universal scaling behavior. | LKM match query: `YbRh2Si2 anisotropy band structure effective mass` |
