# Mapping audit log -- nis2-brinkman-rice-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_29401e4284574aa2.json`; root `gcn_29401e4284574aa2` has one chain and one factor `gfac_dfd930ba89614e8a`. |
| 2. Refine | done | Rewrote each distinct `gcn_*` as self-contained Gaia claim text with NiS2, pressure, observed quantities, source context, and verbatim `lkm_original`. |
| 3. Decompose | done | Preserved the compound root and added helper claims for the 6.03 kT large Fermi-surface orbit, m* = 6(2) m_e, and the Brinkman-Rice large-FS/heavy-quasiparticle signature. |
| 4. Hunt open problems | done | Compared the NiS2 root/helpers against Mott alternative mechanisms, Kondo/Kondo-breakdown language, and the existing YbRh2Si2 FCQPT/RBC branches; no pair was promoted to `contradiction()` under the root-only evidence constraint. |
| 5. Mark suspicions | done | The alternative-mechanisms premise is intentionally weak and has a 0.58 prior; branch-scope false alarms are documented in `dismissed/open_problem_branch_checks.md`. |
| 6. Compile + infer | done | `python -m py_compile`, `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` passed. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 1 independent claim; `gaia inquiry obligation list` and `gaia inquiry hypothesis list` reported no open items. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: the user required bootstrapping only from the supplied root evidence JSON. |
| 9. Repeat / exit rationale | done | Exit condition met for the root-only subgraph: every distinct `gcn_*` is mapped, helpers are derived, priors cover all leaves, no hypotheses remain, and no unsupported roots were imported. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_8a1a27485204457b` | `gcn_8a1a2748_alternative_mechanisms_assumption` | `paper:814525482547544066` | Refined premise: excludes spin-fluctuation, electron-phonon, or magnetic-reconstruction alternatives as sufficient explanations for the same observations. |
| `gcn_29401e4284574aa2` | `gcn_29401e42_nis2_brinkman_rice` | `paper:814525482547544066` | Preserved selected compound root with explicit NiS2 pressure, 6.03 kT belly orbit, m* = 6(2) m_e, large Fermi surface, and Brinkman-Rice interpretation. |
| helper | `helper_nis2_large_fs_603kt_belly_orbit` | `paper:814525482547544066` | Decomposition helper for the large-Fermi-surface component grounded in root text and factor steps 1, 3, and 5. |
| helper | `helper_nis2_mstar_6_me` | `paper:814525482547544066` | Decomposition helper for the effective-mass component grounded in root text and factor steps 1, 3, and 5. |
| helper | `helper_brinkman_rice_large_fs_heavy_quasiparticles` | `paper:814525482547544066` | Decomposition helper for the Brinkman-Rice signature grounded in factor step 2 and the root. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_dfd930ba89614e8a` | `paper:814525482547544066` | `gcn_8a1a27485204457b` | `gcn_29401e4284574aa2` | `deduction` with five numbered LKM steps | 0.95 |
| decomposition | `paper:814525482547544066` | `gcn_29401e4284574aa2` | `helper_nis2_large_fs_603kt_belly_orbit` | `deduction` | 0.95 |
| decomposition | `paper:814525482547544066` | `gcn_29401e4284574aa2` | `helper_nis2_mstar_6_me` | `deduction` | 0.95 |
| decomposition | `paper:814525482547544066` | `gcn_29401e4284574aa2` | `helper_brinkman_rice_large_fs_heavy_quasiparticles` | `deduction` | 0.95 |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_nis2_large_fs_603kt_belly_orbit` | Root text plus factor steps 1, 3, and 5 | `deduction([root], helper, prior=0.95)`; isolates the large-Fermi-surface component without treating it as an independent LKM leaf. |
| `helper_nis2_mstar_6_me` | Root text plus factor steps 1, 3, and 5 | `deduction([root], helper, prior=0.95)`; isolates the reported effective-mass component. |
| `helper_brinkman_rice_large_fs_heavy_quasiparticles` | Factor step 2 plus root interpretation | `deduction([root], helper, prior=0.95)`; isolates the theoretical Brinkman-Rice signature. |

## Open-problem / contradiction hunt

| checked claim | comparison target | verdict | rationale |
|---|---|---|---|
| `gcn_8a1a2748_alternative_mechanisms_assumption` | Mott-boundary alternatives in the selected factor: carrier depletion, Fermi-surface reconstruction, loss of coherence, spin fluctuations, electron-phonon enhancement | not promoted; retained as weak premise | These alternatives are named inside the same LKM factor as mechanisms to be excluded, but the supplied root JSON does not include a second chain-backed claim asserting one of them for the same NiS2 pressure setting. The premise receives a low prior instead of a Gaia contradiction. |
| `helper_nis2_large_fs_603kt_belly_orbit` | Kondo-breakdown / small-vs-large-FS language from YbRh2Si2 heavy-fermion branches | dismissed as material/mechanism scope difference | The NiS2 claim concerns a bandwidth-controlled Mott boundary in a 3d correlated metal; YbRh2Si2 Kondo-lattice large/small-FS questions concern f-electron localization and Kondo screening. Both classes can contain large-FS heavy quasiparticles under different mechanisms. |
| `helper_nis2_mstar_6_me` | YbRh2Si2 FCQPT effective-mass branch (`M*(T,B)=S/T`, homogeneous isotropic model) | dismissed as different observable regime | NiS2 reports a quantum-oscillation cyclotron mass at about 3.8 GPa; the YbRh2Si2 branch formalizes field/temperature scaling of an operational thermodynamic effective mass. No same-system same-quantity conflict is present. |
| `helper_brinkman_rice_large_fs_heavy_quasiparticles` | YbRh2Si2 RBC/Kondo renormalized-band branch | dismissed as analogy, not equivalence or contradiction | Both involve heavy quasiparticles and large-FS language, but the RBC/Kondo branch is material-specific 4f renormalized-band physics while NiS2 is framed as Brinkman-Rice bandwidth-controlled Mott physics. |
| `gcn_29401e42_nis2_brinkman_rice` | Existing parent synthesis cautions about homogeneous-isotropic FCQPT vs material-specific band structure | dismissed as cross-system synthesis caution | The caution sharpens future synthesis language but does not make the NiS2 root and YbRh2Si2 roots mutually exclusive. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No exact duplicate or independent same-proposition claim appears in the supplied root JSON. | none |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| NiS2 Brinkman-Rice interpretation vs named alternatives | underdetermined by root-only evidence; model-selection weakness, not emitted contradiction | No `contradiction()` emitted; premise prior lowered to 0.58 and dismissal/suspicion documented. |
| NiS2 Mott/Brinkman-Rice vs YbRh2Si2 Kondo/FCQPT/RBC branches | different material and mechanism scope | No `contradiction()` emitted. |

## Synthesis cautions

- Do not treat the NiS2 Brinkman-Rice helper as equivalent to YbRh2Si2 Kondo/RBC heavy-fermion claims; they share heavy-Fermi-liquid vocabulary but arise from different microscopic mechanisms.
- The root evidence supports "consistent with Brinkman-Rice" rather than uniquely proving Brinkman-Rice; the alternative-mechanisms exclusion is the only independent LKM premise and is prior-limited.
- Parent synthesis should use this subgraph as a Mott-boundary case of large-FS heavy quasiparticles, not as direct support for FCQPT scaling or Kondo breakdown.

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `python -m py_compile src/nis2_brinkman_rice/*.py` | pass | Python syntax/AST sanity passed for all source modules. |
| `gaia compile .` | pass | Compiled 9 knowledge, 4 strategies, 0 operators; IR hash prefix `sha256:e78e2074b`. |
| `gaia check --brief .` | pass | 1 independent premise with prior, 4 derived conclusions, 4 internal orphaned strategy-helper claims. |
| `gaia check --hole .` | pass | 0 holes / 1 independent claim. |
| `gaia infer .` | pass | Inferred 5 beliefs using exact JT; converged after 2 iterations. |
| `gaia inquiry obligation list` | pass | No open obligations. |
| `gaia inquiry hypothesis list` | pass | No hypotheses. |

## Deviations

- No LKM match or evidence calls beyond the supplied root JSON were made, honoring the user's bootstrap-only requirement.
- No Gaia `contradiction()` operators or inquiry hypotheses were emitted because no admitted second chain-backed claim creates a same-system mutual exclusion.
