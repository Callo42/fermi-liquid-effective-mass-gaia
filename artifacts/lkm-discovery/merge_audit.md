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

## Friedemann2010 extension synthesis pass

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| `artifacts/subgraphs/ybrh2si2-rbc-hall-gaia` | incorporated without rewriting audited intermediate | The validated extension subgraph is preserved under `artifacts/subgraphs/`; the parent package copies its source-level claims into the combined namespace. | Added parent `paper_friedemann2010.py` and imported it from `__init__.py`. |
| `gcn_c243dcb58cae4418` / `gcn_48bba377911d4985` | keep distinct | The first claim states the RBC phase-shift/CEF parametrization; the second states the specific-heat/DOS calibration and reliability proposition. They are complementary premises, not duplicates. | Kept both leaf claims and merged their capped direct priors. |
| `gcn_42a4ff7fd004413f` root components | decompose without merging | The root is compound but the method, Hall-products, and DOS/gamma components are anchored parts of the same selected LKM root rather than independent duplicate claims. | Preserved the root and copied helper claims downstream via `support([root], helper, prior=0.90)`. |
| `gcn_03614e9b_homogeneous_isotropic_model` / Friedemann2010 RBC-Hall-DOS evidence | scope qualification, not contradiction | A homogeneous isotropic FCQPT scaling approximation and a material-specific RBC/Hall/DOS calculation can both be true; the latter qualifies the former's scope by recording details the approximation omits. | Added `cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope` with support from the FCQPT premise and RBC root/helpers. |
| YbRh2Si2 FCQPT scheme / Friedemann2010 RBC calculation | no equivalence | Both address YbRh2Si2 heavy-electron effective-mass physics, but one is a universal-scaling FCQPT procedure and the other is a material-specific renormalized-band/Hall/DOS calculation. | No `equivalence()` emitted. |

No exact merges were made in the Friedemann2010 extension synthesis pass.
