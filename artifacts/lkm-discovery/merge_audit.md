# Merge audit

No formal Gaia merge decisions have been made yet. The discovery pass found no exact contradiction or equivalence pairs among the chain-backed candidates.

## Final synthesis pass

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| He-3 subgraph package and YbRh2Si2 subgraph package | incorporated without rewriting audited intermediates | The validated subgraphs are preserved under `artifacts/subgraphs/`; the parent package copies their source-level claims into a combined namespace. | Created parent `src/fermi_liquid_effective_mass/` modules. |
| `gcn_800070efac5e476d` / `gcn_2741cdef209a457a` | no exact merge | The roots share the broad topic of effective-mass reasoning but differ by material, observable, and model scope. | Kept both selected roots exported. |
| He-3 `gamma -> m*/m` / YbRh2Si2 `S/T -> M*(T,B)` | support to scoped meta-claim, not equivalence | Both are thermodynamic operational routes to effective mass, but not the same proposition. | Added `cross_thermodynamic_routes_to_effective_mass` supported by both subgraph claims. |
| He-3 standard Landau mapping / YbRh2Si2 FCQPT crossover scheme | keep distinct with scope caution | The distinction is important for avoiding a false equivalence or false contradiction. | Added `cross_scope_caution_standard_fl_vs_fcqpt` as a supported synthesis caution. |

No exact merges were made in the final synthesis pass.
