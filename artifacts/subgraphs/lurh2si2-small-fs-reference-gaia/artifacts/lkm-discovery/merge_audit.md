# Merge audit log -- lurh2si2-small-fs-reference-gaia

## Merge and equivalence decisions

| pair_or_set | verdict | reason | source pointers |
|---|---|---|---|
| `gcn_2b8dd97abcb44d53`, `gcn_c131e01470ea48ad`, `gcn_3dc248d9752a416c`, `gcn_3a8394c769864f01` | keep distinct | The root is a compound conclusion; the three premises isolate harmonic assignment, 14 kT/small-FS mismatch, and LuRh2Si2 reference validity. They are not duplicate propositions. | `input/evidence_gcn_2b8dd97abcb44d53.json` |
| `gcn_2b8dd97abcb44d53` vs decomposition helpers | keep root and helpers | Helpers are agent-created decomposition claims derived from explicit factor steps; the root remains the LKM conclusion and is not merged into any helper. | root claim plus factor steps 2-5 |
| 2013 LuRh2Si2 small-FS/dHvA root vs existing Friedemann 2010 RBC/Hall root | keep distinct | Related YbRh2Si2 Fermi-surface physics, but different propositions: dHvA harmonic reinterpretation and 14 kT orbit evidence versus RBC Hall/DOS transport values. | parent `paper_friedemann2010.py`, target `paper_friedemann2013.py` |
| 2013 dHvA root vs Shaginyan 2010 FCQPT effective-mass scheme | keep distinct | Related heavy-fermion context, but no same proposition and no same-scope incompatible assertion. | parent `paper_shaginyan2010.py`, target `paper_friedemann2013.py` |

## Auto-merges

None.

## Independent agreement / equivalence

None emitted. Related context is preserved for later parent synthesis rather than forced into `equivalence()`.
