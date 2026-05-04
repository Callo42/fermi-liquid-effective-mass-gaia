# Analysis

## May 4 Regeneration

This package was regenerated from exactly one chain-backed starting root: `gcn_2741cdef209a457a`, the Shaginyan 2010 YbRh2Si2 FCQPT effective-mass scheme. All accepted extensions are connected YbRh2Si2 roots with raw LKM evidence chains. He-3, TiS2, Brinkman-Rice/Mott/NiS2, and CeMo2Si2C executable branches were removed because the May 4 bridge search did not find a chain-backed path to the active graph.

No executable parent synthesis claims remain. The package uses LKM-backed `claim(...)` nodes, direct decomposition helpers, `deduction(...)`, `support(...)`, and one `equivalence(...)` between two independently chain-backed FCQPT inflection premises. Scope, non-equivalence, non-contradiction, and failed bridge decisions are recorded in `artifacts/lkm-discovery/`.

## Node Counts

| Count | Value |
|---|---:|
| Total knowledge nodes | 89 |
| Source science-facing claims | 46 |
| Strategies | 31 |
| Operators | 1 |
| Science-facing connected components | 1 |
| Starmap rendered nodes / edges | 79 / 82 |
| Prior holes | 0 |

The graph stops below 100 nodes because the remaining available branches would either be disconnected or would require unsupported agent-authored bridge claims.

## Duplicate Audit

`gaia inquiry review --strict .` passed with 0 graph warnings, 0 graph errors, 0 missing priors, and 0 possible duplicate claims. It reports compiler-generated `__conjunction_result_*` and `__implication_result_*` structural holes plus optional unreviewed warrants; these are logged in `artifacts/lkm-discovery/merge_audit.md` as non-duplicate residual review risk.

## Verification

The required commands pass using:

```bash
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry review --strict .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia render . --target github
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia render . --target docs
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia starmap . --out docs/starmap.html
```

Latest compile hash: `sha256:db40d085e49405c939e7e60c90709a6f78ccd1645003747f35a36d41fb08a114`.

## Key Risks

- Several support edges are intentionally moderate-prior cross-paper connections between different YbRh2Si2 measurement/model surfaces; the audit logs record why these are supports rather than equivalences or new claims.
- Gaia strict review leaves 31 optional unreviewed warrant metadata items. They do not block the CLI checks or duplicate audit, but a future manual reviewer can annotate them.
- Raw evidence JSON is preserved, including rejected old branches, so artifact inventory still contains files for branches that are no longer executable imports.
