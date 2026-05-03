# Mapping audit log -- lurh2si2-small-fs-reference-gaia

## 9-step checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_2b8dd97abcb44d53.json`; root `gcn_2b8dd97abcb44d53` has one evidence chain and one factor `gfac_468a4122e2fb414d`. |
| 2. Refine | done | Rewrote each distinct `gcn_*` as a self-contained Gaia `claim()` with system, method, quantities, source paper, `provenance_source="lkm"`, and `lkm_original`. |
| 3. Decompose | done | Preserved the compound root and added three grounded helper claims for harmonic reassignment, reduced fundamental set, and the 14 kT orbit/itinerant-4f inference. |
| 4. Hunt open problems | done | Checked the new root, premises, and helpers against existing YbRh2Si2 dHvA/RBC/FCQPT context; no same-scope logical incompatibility was found. |
| 5. Mark suspicions | done | Logged scope/model cautions in `dismissed/dhva_rbc_fcqpt_scope.md` rather than emitting false `contradiction()` edges. |
| 6. Compile + infer | done | `python -m py_compile`, `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` passed from the subgraph package directory. |
| 7. Review holes | done | `gaia check --hole .` reported 0 holes / 3 independent claims; all direct priors are capped below 0.90 and marked `TODO:review`. |
| 8. Search/support synthesis | closed by scope | No new LKM retrieval was performed; the package bootstraps only from the supplied root evidence JSON. Decomposition supports are downstream of the root to avoid double-counting. |
| 9. Exit rationale | done | The selected root chain is fully mapped, audit files are present, no contradiction/equivalence was promoted, 0 holes remain, and inference converged. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_c131e01470ea48ad` | `gcn_c131e014_ybrh2si2_midband_harmonic_assignment` | `paper:867761295154217007` | Refined premise: 5-7 kT YbRh2Si2 peaks can be assigned as harmonics of lower-frequency fundamentals under the stated angular-dependence and field-modulation conditions. |
| `gcn_3dc248d9752a416c` | `gcn_3dc248d_ybrh2si2_14kt_not_small_fs` | `paper:867761295154217007` | Refined premise: refined core-4f small-FS calculation lacks a (100)-field 14 kT orbit, so an independent measured 14 kT orbit supports high-field itinerant 4f participation if alternatives are unlikely. |
| `gcn_3a8394c769864f01` | `gcn_3a8394c_lurh2si2_small_fs_reference` | `paper:867761295154217007` | Refined premise: LuRh2Si2 is a valid small-FS reference for YbRh2Si2 because of isostructural chemistry, filled Lu 4f shell, refined `z_Si`, and similar non-f conduction-band character. |
| `gcn_2b8dd97abcb44d53` | `gcn_2b8dd97_lurh2si2_reference_reanalysis` | `paper:867761295154217007` | Selected root; preserved as an LKM claim and exported. |
| helper | `helper_ybrh2si2_5_7kt_peaks_are_harmonics` | `paper:867761295154217007` | Decomposition helper from root text and factor steps 2-3. |
| helper | `helper_ybrh2si2_reduced_fundamental_set` | `paper:867761295154217007` | Decomposition helper from factor step 3. |
| helper | `helper_14kt_orbit_supports_high_field_itinerant_4f` | `paper:867761295154217007` | Decomposition helper from root text and factor steps 4-5. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_468a4122e2fb414d` | `paper:867761295154217007` | `gcn_c131e01470ea48ad`, `gcn_3dc248d9752a416c`, `gcn_3a8394c769864f01` | `gcn_2b8dd97abcb44d53` | `deduction(...)` with five numbered LKM steps | 0.95 |

## Decomposition helpers

| helper | evidence grounding | DSL action |
|---|---|---|
| `helper_ybrh2si2_5_7kt_peaks_are_harmonics` | Root text plus factor steps 2-3 | `support([root], helper, prior=0.90)`; downstream helper, not an independent leaf. |
| `helper_ybrh2si2_reduced_fundamental_set` | Factor step 3 | `support([root], helper, prior=0.90)`; isolates the reduced independent-frequency set. |
| `helper_14kt_orbit_supports_high_field_itinerant_4f` | Root text plus factor steps 4-5 | `support([root], helper, prior=0.90)`; isolates the 14 kT/high-field itinerant-4f inference. |

## Open-problem / contradiction hunt

| checked claim | comparison target | verdict | rationale |
|---|---|---|---|
| `gcn_c131e014_ybrh2si2_midband_harmonic_assignment` | Existing parent YbRh2Si2 RBC/Hall and FCQPT branches | dismissed | No existing package claim asserts that the same 5-7 kT peaks are independent fundamentals under the same reanalysis assumptions. |
| `gcn_3dc248d_ybrh2si2_14kt_not_small_fs` | Existing Friedemann 2010 RBC/Hall branch | dismissed as compatible | A core-4f small-FS calculation lacking a 14 kT orbit is compatible with a renormalized-band/itinerant-4f calculation used for heavy-Fermi-liquid transport. |
| `gcn_3a8394c_lurh2si2_small_fs_reference` | Existing Shaginyan 2010 homogeneous isotropic FCQPT model | dismissed as scope tension | A material-specific LuRh2Si2/YbRh2Si2 small-FS reference can coexist with a universal-scaling model that deliberately omits band topology. |
| `gcn_2b8dd97_lurh2si2_reference_reanalysis` and helpers | Existing parent synthesis caution that RBC qualifies homogeneous isotropic scope | dismissed as synthesis caution | The new root strengthens the material-specific Fermi-surface qualification but does not logically refute the parent model scope. |

## Contradictions and equivalences

| kind | decision | dsl_action |
|---|---|---|
| contradiction | none promoted | No `contradiction()` emitted. |
| equivalence | none promoted | No `equivalence()` emitted. |

## Priors

| independent leaf | prior | justification status |
|---|---|---|
| `gcn_c131e014_ybrh2si2_midband_harmonic_assignment` | 0.78 | Capped direct claim prior; justification ends with `TODO:review`. |
| `gcn_3dc248d_ybrh2si2_14kt_not_small_fs` | 0.74 | Capped direct claim prior; justification ends with `TODO:review`. |
| `gcn_3a8394c_lurh2si2_small_fs_reference` | 0.84 | Capped direct claim prior; justification ends with `TODO:review`. |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `python -m py_compile src/lurh2si2_small_fs_reference/*.py` | pass | Python syntax check passed. |
| `gaia compile .` | pass | Compiled 12 knowledge, 4 strategies, 0 operators; IR hash `sha256:5dd629dd83816b8ce11ab768307d4eeb489826da5464b0cdb15a2ab1692ffac3`. |
| `gaia check --brief .` | pass | 3 independent premises with priors, 4 derived conclusions, 5 internal orphaned structural helper claims. |
| `gaia check --hole .` | pass | 0 holes / 3 independent claims. |
| `gaia infer .` | pass | Inferred 8 beliefs using exact JT; converged after 2 iterations. |

## Synthesis cautions

- Treat the 14 kT inference as conditional: the LKM premise itself notes instrumental artefacts, magnetic-breakdown-generated high-frequency orbits, and misassignment as alternatives that must be unlikely or excluded.
- Treat the LuRh2Si2 small-FS reference as a reference-model approximation, not as direct measurement of YbRh2Si2 without 4f hybridization.
- Treat the harmonic reassignment as a reinterpretation of published dHvA spectra that benefits from extended angular-range and complementary checks, as the LKM factor step 5 states.
- In parent synthesis, connect this subgraph as material-specific Fermi-surface context for YbRh2Si2 rather than as a contradiction of RBC/Hall or homogeneous-isotropic FCQPT branches.
