# Mapping audit log -- mott-entropy-mass-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_e4ecd721edd14d3f.json` for the chain backbone. Mapped every distinct `gcn_*` in that payload: `gcn_31bc66ca16a44508`, `gcn_795699f572b24ed5`, `gcn_dd12256615264dfb`, and root `gcn_e4ecd721edd14d3f`. |
| 2. Refine | done | Rewrote each `gcn_*` as self-contained Capone-Fabrizio-Tosatti 2001 claims with explicit system/scope, quantities, assumptions, and citation. Preserved verbatim LKM text in `lkm_original`. |
| 3. Decompose | done | Added grounded helpers for FL definition/Z/T_K, Brinkman-Rice m* -> infinity/Z -> 0/T_K -> 0, Fermi-liquid entropy at T_K, singlet-Mott zero entropy, Luttinger pinning, and entropy-instability requirement. |
| 4. Hunt open problems | done | Audited existing Brinkman-Rice, NiS2, and Kondo-lattice context. No same-condition contradiction was promoted; a finite-mass spinon route remains an explicit open problem question. |
| 5. Mark suspicions | done | Prior notes flag dependence on quasiparticle/FL assumptions, Luttinger pinning up to the transition, fixed chemical potential, no symmetry breaking, and absence of extra low-energy entropy carriers. |
| 6. Compile + infer | done | `gaia compile .` and `gaia infer .` passed. IR hash is `sha256:a057f4e4a7c765c49c880f2265766ed77733a74f0a82be51ba19480522b1fd2e`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 3 independent claims. `gaia inquiry obligation list --path .` reported no open obligations. |
| 8. Search supports/open problems | done | Existing LKM context was used for contradiction/open-problem audit only; support candidates were not formalized because the package remains bootstrapped solely from the root evidence JSON. |
| 9. Repeat/exit rationale | done | Exit condition met: compile/check/hole/infer passed, no hypotheses remain, no promoted contradictions, and no unresolved merge decisions. |

## Claims

| label | lkm id | source paper | self-contained transformation | lkm_original preserved |
|---|---|---|---|---|
| `gcn_31bc66ca16a44508` | `gcn_31bc66ca16a44508` | `paper:867770551072981407` | Added Capone-Fabrizio-Tosatti scope, T_K/E_F* identification, entropy scaling, and assumptions. | yes |
| `gcn_795699f572b24ed5` | `gcn_795699f572b24ed5` | `paper:867770551072981407` | Added three-orbital Hamiltonian scope, FL condition, Luttinger pinning, and fixed-mu resonance narrowing. | yes |
| `gcn_dd12256615264dfb` | `gcn_dd12256615264dfb` | `paper:867770551072981407` | Added continuity assumptions and explicit exclusions: chemical-potential motion, symmetry breaking, and instability/intermediate phase. | yes |
| `gcn_e4ecd721edd14d3f` | `gcn_e4ecd721edd14d3f` | `paper:867770551072981407` | Preserved the selected root as a self-contained scoped conclusion tying BR mass divergence, Z/T_K collapse, FL entropy, singlet-zero entropy, and intervening phase. | yes |
| `capone_fl_definition_z_tk` | `gcn_e4ecd721edd14d3f` | `paper:867770551072981407` | Decomposition helper for the root's FL definition and Z/T_K vocabulary. | yes |
| `capone_brinkman_rice_mass_z_tk_limit` | `gcn_e4ecd721edd14d3f` | `paper:867770551072981407` | Decomposition helper for m* -> infinity, Z -> 0, E_F* ~ ZW/2, T_K -> 0. | yes |
| `capone_fl_entropy_order_unity_at_tk` | `gcn_31bc66ca16a44508` | `paper:867770551072981407` | Decomposition helper for S(T_K) being finite/order unity for nonzero T_K. | yes |
| `capone_singlet_mott_zero_entropy` | `gcn_e4ecd721edd14d3f` | `paper:867770551072981407` | Decomposition helper for the nondegenerate spin-singlet, spin-gapped, zero-entropy endpoint. | yes |
| `capone_luttinger_pinning_blocks_band_edge_route` | `gcn_795699f572b24ed5` | `paper:867770551072981407` | Decomposition helper for the fixed-chemical-potential/no-band-edge-crossover premise. | yes |
| `capone_entropy_mismatch_requires_instability` | `gcn_dd12256615264dfb` | `paper:867770551072981407` | Decomposition helper for the intervening-instability/intermediate-phase requirement. | yes |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_2737af3324f345e8` | `paper:867770551072981407` | `gcn_31bc66ca16a44508`, `gcn_795699f572b24ed5`, `gcn_dd12256615264dfb` | `gcn_e4ecd721edd14d3f` | `deduction` | 0.95 |
| decomposition | `paper:867770551072981407` | `gcn_e4ecd721edd14d3f` | `capone_fl_definition_z_tk` | `deduction` | 0.95 |
| decomposition | `paper:867770551072981407` | `gcn_e4ecd721edd14d3f` | `capone_brinkman_rice_mass_z_tk_limit` | `deduction` | 0.95 |
| decomposition | `paper:867770551072981407` | `gcn_31bc66ca16a44508` | `capone_fl_entropy_order_unity_at_tk` | `deduction` | 0.95 |
| decomposition | `paper:867770551072981407` | `gcn_e4ecd721edd14d3f` | `capone_singlet_mott_zero_entropy` | `deduction` | 0.95 |
| decomposition | `paper:867770551072981407` | `gcn_795699f572b24ed5` | `capone_luttinger_pinning_blocks_band_edge_route` | `deduction` | 0.95 |
| decomposition | `paper:867770551072981407` | `gcn_dd12256615264dfb` | `capone_entropy_mismatch_requires_instability` | `deduction` | 0.95 |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Canonical BR/Z/T_K restatements | existing match/evidence context | not promoted | Supports or restates the root's assumptions; no mutually exclusive same-condition claim. |
| Finite-mass spinon-Fermi-surface Mott route | existing evidence `gcn_5f269db6cc3e4841` | open question | Changes the mechanism so that Z can vanish without m*/m divergence; important tension, but not logically incompatible with the root's conditional Brinkman-Rice argument. |
| NiS2 pressure-tuned heavy FL | existing evidence `gcn_29401e4284574aa2` | dismissed | Experimental BR-like heavy FL near a Mott boundary; no zero-entropy singlet endpoint claim. |
| Kondo-lattice BR liquid | existing evidence `gcn_7ae79f122f1c4fcb` | dismissed | Screened f-ion Kondo-lattice fixed point, not a direct FL-to-singlet-Mott crossover. |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `gaia compile .` | pass | Compiled 19 knowledge, 7 strategies, 0 operators. |
| `gaia check --brief .` | pass | 3 independent claims with priors, 7 derived conclusions, 1 question, 8 internal strategy-helper orphan claims. |
| `gaia check --hole .` | pass | 0 holes / 3 independent claims. |
| `gaia infer .` | pass | Inferred 11 beliefs using exact JT; converged after 2 iterations. |
| `gaia inquiry obligation list .` | failed then corrected | CLI rejected positional path; corrected to `gaia inquiry obligation list --path .`. |
| `gaia inquiry obligation list --path .` | pass | No open obligations. |
| `gaia inquiry hypothesis list --path .` | pass | No hypotheses. |
