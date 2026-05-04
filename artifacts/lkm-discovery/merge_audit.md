# Merge audit -- May 4 regeneration

## Duplicate and merge decisions

| pair_or_item | verdict | reason | action |
|---|---|---|---|
| `gcn_e0c364ff_inflection_fcqpt_condition` / `gcn_f82c178_fcqpt_inflection_cubic_spectrum` | independent same proposition | Same FCQPT inflection/cubic-spectrum condition appears in two chain-backed Shaginyan roots. | Kept both source claims and added `equivalence()`; no merge because independent sources preserve provenance. |
| Friedemann2010 `helper_rbc_parameterization_constrained_by_cef_gamma` / premises `gcn_c243dcb...`, `gcn_48bba377...` | direct decomposition, keep | Helper isolates part of the root claim for readability and is derived from root support, not an independent premise. | Kept. |
| Knebel2006 dHvA helpers / root `gcn_c38f8ce...` | direct decompositions, keep | Helpers isolate frequencies/masses, LDA mismatch, and scope cautions from one chain-backed root. | Kept. |
| Friedemann2013 `helper_ybrh2si2_reduced_fundamental_set` / root `gcn_2b8dd97...` | direct decomposition, keep | Helper is a narrower component of the root reanalysis. | Kept. |
| Entropy/gamma/ESR/transport/dHvA effective-mass proxies | related but not equivalent | These are distinct probes or operational proxies under different methods and field/temperature scopes. | Connected with support only; no `equivalence()` or merge. |
| Tokiwa step-like mass drop / Pfau-Naren smooth Kondo de-renormalization | not contradiction; scope distinction | Abrupt transport/Lifshitz signatures and smoother Kondo-weight reduction can coexist in the raw high-field YbRh2Si2 evidence. | Logged in `contradictions.md`; no `contradiction()`. |
| He-3, TiS2, Brinkman-Rice/Mott, NiS2, CeMo2Si2C old branches | rejected, not merged | No chain-backed bridge to the active YbRh2Si2 graph under May 4 rules. | Removed from executable imports/source package; raw artifacts and subgraphs preserved. |

## `gaia inquiry review --strict` status

Strict review after the May 4 rebuild:

| item | verdict |
|---|---|
| command status | pass / exit 0 |
| possible duplicate claims | 0 |
| independent claims missing priors | 0 |
| graph warnings/errors | 0 / 0 |
| structural holes | 42 compiler-generated `__conjunction_result_*` / `__implication_result_*` helper nodes |
| unreviewed warrants | 31 source strategies remain unreviewed by Gaia's optional warrant-review metadata flow |

Duplicate audit status: no source science-facing duplicate claims were reported. The structural-hole entries are internal generated helper nodes, not source claims to merge. The optional warrant-review items are tracked as a residual review-workflow risk, but they do not indicate duplicate science claims and the strict command passed.
