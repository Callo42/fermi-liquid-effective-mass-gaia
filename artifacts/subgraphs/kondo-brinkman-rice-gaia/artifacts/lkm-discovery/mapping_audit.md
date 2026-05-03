# Mapping audit log -- kondo-brinkman-rice-gaia

## Batch checklist / report

| step | status | note |
|---|---|---|
| 1. Bootstrap from root | done | Loaded only `input/evidence_gcn_7ae79f122f1c4fcb.json`; root `gcn_7ae79f122f1c4fcb` has one evidence chain and one factor `gfac_303f81acdd314345`. |
| 2. Refine self-contained | done | Rewrote each distinct `gcn_*` as a self-contained Gaia `claim()` with system, method/regime, quantities, source paper, and verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the root and added four helper claims for Kondo-lattice screening, large mass renormalization, finite Stoner enhancement, and Nozieres-to-lattice transfer. |
| 4. Hunt open problems | done | Compared every new claim/helper against existing heavy-fermion, Mott, Brinkman-Rice, FCQPT, and YbRh2Si2 RBC context; no pair was promoted to `contradiction()` because the candidates were regime/scope qualifications. |
| 5. Mark suspicions | done | Logged false-alarm dismissals in `dismissed/open_problem_false_alarms.md` and synthesis cautions below. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims. Local CLI `gaia inquiry obligation list` and `gaia inquiry hypothesis list` reported no open items. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON. No upstream support edges from unselected roots were imported. |
| 9. Repeat / exit rationale | closed | The single selected root chain is fully mapped; remaining questions are parent-synthesis cautions, not reasons to pull unselected roots into this standalone subgraph. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_40f11182b5f74ff2` | `gcn_40f111_nozieres_local_fl_kondo_sites` | `paper:813343302173589505` | Refined premise: Nozieres single-impurity Fermi-liquid representation applied locally to screened f-ion sites, with inter-site corrections assumed small. |
| `gcn_8f275a75866e4923` | `gcn_8f275a_brinkman_rice_scope_condition` | `paper:813343302173589505` | Refined premise: Brinkman-Rice fixed-point definition plus scope condition that inter-site collective effects do not qualitatively alter local Kondo Fermi-liquid physics. |
| `gcn_7ae79f122f1c4fcb` | `gcn_7ae79f_kondo_brinkman_rice_fixed_point` | `paper:813343302173589505` | Preserved selected compound root with explicit Kondo-lattice systems, large mass renormalization, and finite order-unity Stoner enhancement. |
| helper | `helper_kondo_lattice_screened_heavy_quasiparticles` | `paper:813343302173589505` | Decomposition helper for the Kondo-lattice definition component of the root. |
| helper | `helper_brinkman_rice_large_mass_renormalization` | `paper:813343302173589505` | Decomposition helper for the large effective-mass component of Brinkman-Rice behavior. |
| helper | `helper_brinkman_rice_finite_stoner_enhancement` | `paper:813343302173589505` | Decomposition helper for the finite nondivergent Stoner-enhancement component. |
| helper | `helper_nozieres_to_kondo_lattice_fixed_point` | `paper:813343302173589505` | Decomposition helper for the transfer from single-impurity Nozieres Fermi-liquid physics to the periodic Kondo lattice. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind |
|---|---|---|---|---|
| `gfac_303f81acdd314345` | `paper:813343302173589505` | `gcn_40f11182b5f74ff2`, `gcn_8f275a75866e4923` | `gcn_7ae79f122f1c4fcb` | `deduction(..., prior=0.95)` with seven numbered LKM steps. |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_kondo_lattice_screened_heavy_quasiparticles` | Root text plus factor step 1 | `deduction([root], helper, prior=0.95)`; isolates the Kondo-lattice definition without treating it as independent evidence. |
| `helper_brinkman_rice_large_mass_renormalization` | Root text plus factor step 2 | `deduction([root], helper, prior=0.95)`; isolates the large-mass component. |
| `helper_brinkman_rice_finite_stoner_enhancement` | Root text plus factor step 5 | `deduction([root], helper, prior=0.95)`; isolates the finite-Stoner component central to the user theme. |
| `helper_nozieres_to_kondo_lattice_fixed_point` | Factor steps 4 and 6 plus both premises | `deduction([premises], helper, prior=0.95)`; isolates the single-impurity-to-lattice transfer. |

## Leaf priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_40f111_nozieres_local_fl_kondo_sites` | 0.78 | Grounded in Anderson's Nozieres/Friedel-sum-rule argument, but extrapolates from single-impurity physics to a periodic lattice with qualitatively bounded inter-site corrections; TODO:review. |
| `gcn_8f275a_brinkman_rice_scope_condition` | 0.72 | Plausible scoped fixed-point identification when inter-site exchange/RKKY/ordering are weak or irrelevant, but those boundary conditions are not independently established inside the selected root chain; TODO:review. |

## Open-problem / contradiction hunt

| checked claim | comparison target | verdict | rationale |
|---|---|---|---|
| `helper_brinkman_rice_finite_stoner_enhancement` | Parent Shaginyan FCQPT branch with `1/M* = 0` criticality | dismissed as regime distinction | Finite Stoner enhancement and divergent/critical effective mass are different quantities and regimes. The Anderson root concerns screened Kondo-lattice Brinkman-Rice Fermi-liquid behavior; Shaginyan concerns homogeneous isotropic FCQPT scaling. |
| `gcn_40f111_nozieres_local_fl_kondo_sites` | Parent Friedemann/YbRh2Si2 RBC phase-shift parametrization | dismissed as compatible modeling levels | Both use low-energy local f-electron phase-shift/resonance ideas. RBC adds material-specific CEF and band-transport structure rather than denying the local Kondo fixed-point analogy. |
| `gcn_8f275a_brinkman_rice_scope_condition` | Mott/local-moment context in the root and parent synthesis cautions | dismissed as explicit proximity condition | Being proximate to a Mott/local-moment instability is not the same as being in an unscreened ordered local-moment state; the selected root explicitly conditions on Kondo screening and weak/irrelevant inter-site collective effects. |
| `gcn_7ae79f_kondo_brinkman_rice_fixed_point` | Conventional almost-ferromagnetic spin-fluctuation picture | not promoted | The selected JSON contains Anderson's contrast with almost-ferromagnetic spin fluctuations, but no separately grounded same-regime claim asserting divergent Stoner enhancement. This remains a synthesis caution, not a Gaia contradiction. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate within the selected root evidence chain. | none |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| none | All apparent tensions were dismissed as compatible scope/regime distinctions. | No `contradiction()` emitted. |

## Commands and validation status

| command | status | output summary |
|---|---|---|
| `gaia compile .` | passed | Compiled 14 knowledge, 5 strategies, 0 operators; IR hash `sha256:ae08240cc...`. |
| `gaia check --brief .` | passed | 2 independent claims with priors, 5 derived conclusions, 0 structural operators; compiler also reports 7 internal orphaned conjunction/implication helper claims generated from strategies. |
| `gaia check --hole .` | passed | 0 holes / 2 independent claims; both leaf priors covered. |
| `gaia infer .` | passed | Inferred 9 beliefs with exact JT, converged in 2 iterations. |
| `gaia inquiry obligation list --scope github::kondo-brinkman-rice-gaia` | failed (CLI deviation) | Installed CLI does not accept documented `--scope`; rerun without `--scope` succeeded. |
| `gaia inquiry hypothesis list --scope github::kondo-brinkman-rice-gaia` | failed (CLI deviation) | Installed CLI does not accept documented `--scope`; rerun without `--scope` succeeded. |
| `gaia inquiry obligation list` | passed | `(no open obligations)`. |
| `gaia inquiry hypothesis list` | passed | `(no hypotheses)`. |

## Synthesis cautions

- The selected root is a fixed-point identification, not a full microscopic solution of the Kondo lattice; parent synthesis should preserve the premise that inter-site collective effects are weak or irrelevant.
- The finite Stoner enhancement component should not be conflated with absence of strong mass enhancement. Anderson's point is large mass with finite spin-susceptibility enhancement.
- The root should qualify, not refute, material-specific YbRh2Si2 RBC and FCQPT branches unless a future selected root supplies same-system contradictory values or mutually exclusive regimes.
- No external paper text, web content, or new LKM search result was imported into the Gaia source; existing parent context was used only for contradiction/dismissal judgment.

## Exit rationale

The standalone package maps the selected root and all distinct `gcn_*` claims in its chain. No unselected root was imported as Gaia evidence; copied discovery files preserve the audit trail for later parent-package synthesis.
