# Merge audit

Original discovery note preserved: no formal Gaia merge decisions had been made at discovery time, and the discovery pass found no exact contradiction or equivalence pairs among the chain-backed candidates.

## Formalization decisions

| item | decision | rationale | action |
|---|---|---|---|
| `gcn_2ee995fe1e674e2a` / `gcn_1587257a956f4d18` | keep distinct | One claim asserts the experimental/extrapolation premise for the measured gamma; the other asserts the Landau mapping premise and numeric conversion. | Separate claim labels and separate priors. |
| `gcn_800070efac5e476d` components | decompose but do not merge | The root is a compound conclusion containing both gamma -> m*/m and m*/m -> F1 components. Both are explicitly supported by the LKM text. | Root claim preserved; two derived helper claims added. |
| Search-hit restatements of the Landau relation | keep outside graph | LKM match probes surfaced related chainless or non-root support/background claims. The package remains chain-backed to the selected He-3 root for this pilot. | Raw match JSON preserved in `input/`; no merge/equivalence edge emitted. |
