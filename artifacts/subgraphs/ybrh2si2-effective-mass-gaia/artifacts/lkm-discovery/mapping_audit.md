# Mapping audit log -- ybrh2si2-effective-mass-gaia

## Batch checklist

| step | status | note |
|---|---|---|
| 1. Bootstrap from root | done | Loaded only `input/evidence_gcn_2741cdef209a457a.json` for the chain backbone. |
| 2. Refine self-contained claims | done | Every `gcn_*` claim was rewritten to include system/model/method context; verbatim LKM text is preserved in `lkm_original`. |
| 3. Decompose compound claims | done | No comparison-style compound claim was decomposed; the procedure conclusion is represented through its six LKM premises and one deduction. |
| 4. Hunt open problems | done | Discovery flags plus limited LKM match searches found no strict contradiction; a YbRh2Si2 anisotropy/model-scope concern was dismissed as a Gaia contradiction and retained as a synthesis suspicion. |
| 5. Mark suspicions | done | Scope suspicion recorded: homogeneous isotropic model versus anisotropic/band-structure evidence for YbRh2Si2. |
| 6. Compile and infer | done | `gaia compile .` and `gaia infer .` passed; inference used JT exact BP and converged. |
| 7. Review obligations and holes | done | `gaia check --brief .` and `gaia check --hole .` passed with 0 holes across 6 independent claims. |
| 8. Search supports | done | Limited LKM match found same-chain support and contextual later support; no new support edge added because the package bootstrap remains rooted in the selected evidence JSON. |
| 9. Repeat / exit rationale | done | Exited after one batch because the selected root chain is fully mapped, no holes remain, no real contradiction was promoted, and no chain-backed upstream support was added under the root-only bootstrap constraint. |

## Claims

| lkm_id | label | source_paper | action |
|---|---|---|---|
| `gcn_677c6c11780945f1` | `gcn_677c6c_landau_integral_relation` | `paper:867752612177379569` | claim leaf; self-contained Landau integral relation. |
| `gcn_03614e9b5933496a` | `gcn_03614e9b_homogeneous_isotropic_model` | `paper:867752612177379569` | claim leaf; self-contained model approximation for YbRh2Si2 scaling. |
| `gcn_e0c364ff93804e75` | `gcn_e0c364ff_inflection_fcqpt_condition` | `paper:867752612177379569` | claim leaf; self-contained FCQPT inflection condition. |
| `gcn_6bbfeb95290d413d` | `gcn_6bbfeb95_stable_landau_solutions` | `paper:867752612177379569` | claim leaf; self-contained numerical-stability claim. |
| `gcn_ecddfefac84c4b46` | `gcn_ecddfefa_fermion_entropy_formula` | `paper:867752612177379569` | claim leaf; self-contained Fermi-Dirac entropy formula. |
| `gcn_2e69311592b04bcb` | `gcn_2e693115_entropy_over_temperature_mass` | `paper:867752612177379569` | claim leaf; self-contained operational M*=S/T relation. |
| `gcn_2741cdef209a457a` | `gcn_2741cdef_practical_effective_mass_scheme` | `paper:867752612177379569` | derived conclusion; exported root claim. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind |
|---|---|---|---|---|
| `gfac_749b6767459b4785` | `paper:867752612177379569` | `gcn_677c6c11780945f1`, `gcn_03614e9b5933496a`, `gcn_e0c364ff93804e75`, `gcn_6bbfeb95290d413d`, `gcn_ecddfefac84c4b46`, `gcn_2e69311592b04bcb` | `gcn_2741cdef209a457a` | `deduction(..., prior=0.95)` |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| (none in this subgraph) | no exact duplicate/equivalent pair detected | none |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| homogeneous isotropic model vs YbRh2Si2 anisotropy/Fermi-surface search hits | not a strict contradiction because microscopic anisotropy and a universal-scaling approximation can both be true under different modeling scopes | dismissed; no `contradiction()` emitted |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| `gcn_03614e9b5933496a` vs LKM anisotropy hits (`gcn_c38f8ce989fd454a`, `gcn_42a4ff7fd004413f`, `gcn_dd09c40e9184410a`) | limited LKM match search | Model-scope limitation rather than logical exclusion; retained for synthesis review. |
