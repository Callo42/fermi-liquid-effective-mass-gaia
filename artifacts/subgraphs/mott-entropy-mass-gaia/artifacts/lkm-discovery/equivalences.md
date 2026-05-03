# Discovery equivalence flags

Broad discovery was skipped because the user supplied the narrow root `gcn_e4ecd721edd14d3f`.

| candidate | decision | rationale |
|---|---|---|
| `gcn_5407089724b24dc4` versus the entropy/Z/T_K component of `gcn_e4ecd721edd14d3f` | keep outside graph | It appears to restate a grounded subcomponent of the root, but the available evidence file reports `total_chains: 0`; strict root-evidence bootstrap prevents importing or merging it. |
| Root decomposition helper claims | decompose, not merge | Helper claims expose grounded parts of the selected root and premises for review. The original LKM `gcn_*` claims are preserved as canonical claims, so no equivalence merge is needed. |

No formal cross-claim equivalence was emitted.
