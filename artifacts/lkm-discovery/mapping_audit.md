# Mapping audit log -- fermi-liquid-effective-mass-gaia May 4 regeneration

## Gate summary

- Starting root: exactly one chain-backed LKM root, `gcn_2741cdef209a457a`.
- Accepted extensions: 11 connected Turn-2 roots, each with `total_chains > 0`.
- Removed executable He-3, Brinkman-Rice/Mott, NiS2, and CeMo2Si2C branches because no chain-backed bridge to the active YbRh2Si2 graph was found.
- Removed all executable `provenance_source="synthesis"` parent claims.
- Scope, non-contradiction, non-equivalence, and failed-bridge judgments are recorded here, in `merge_audit.md`, `contradictions.md`, `equivalences.md`, and `bridge_search_2026-05-04.md`, not as `claim(...)` nodes.

## Per-pass TODO checklist

| pass | single package from one root | LKM-backed/direct decomposition only | connected extension path | no banned synthesis provenance | scope judgments in audit files | compile/hole/infer | audit files current | README/analysis honest |
|---|---|---|---|---|---|---|---|---|
| Turn-1 start: `gcn_2741cdef209a457a` | pass | pass | pass | pass | pass | pass | pass | pass |
| Extension: `gcn_45f24d454cd3448e` | pass | pass | FCQPT inflection equivalence to start-root premise | pass | pass | pass | pass | pass |
| Extension: `gcn_42a4ff7fd004413f` | pass | pass | YbRh2Si2 thermodynamic DOS/gamma mass proxy supports start-root entropy/mass proxy | pass | pass | pass | pass | pass |
| Extension: `gcn_c38f8ce989fd454a` | pass | pass | YbRh2Si2 dHvA/LDA branch connected through LuRh2Si2 reference and many-body-method support | pass | pass | pass | pass | pass |
| Extension: `gcn_2b8dd97abcb44d53` | pass | pass | LuRh2Si2 small-FS reference and YbRh2Si2 dHvA reanalysis connect to Knebel/Rourke branches | pass | pass | pass | pass | pass |
| Extension: `gcn_b4093fb2f2e44f3b` | pass | pass | Field-dependent `A(B)`/gamma mass evidence supports start-root mass proxy and Pfau Kondo-suppression ingredient | pass | pass | pass | pass | pass |
| Extension: `gcn_3a1514fde2d54682` | pass | pass | Kondo-lattice coherence hierarchy supports Pfau Kondo-lattice ingredient | pass | pass | pass | pass | pass |
| Extension: `gcn_d8b1b53ca8b44189` | pass | pass | ESR heavy-quasiparticle evidence supports Kondo hierarchy and entropy/mass proxy | pass | pass | pass | pass | pass |
| Extension: `gcn_4d206f9ebed246c8` | pass | pass | YbRh2Si2 high-field Kondo suppression/Lifshitz branch connected to Tokiwa, Seiro, and Naren evidence | pass | pass | pass | pass | pass |
| Extension: `gcn_b5d9fe70ddb84b9d` | pass | pass | Lifshitz/de-renormalization root directly supports Pfau combined mechanism | pass | pass | pass | pass | pass |
| Extension: `gcn_d10f91dd4b8e4f21` | pass | pass | Rourke high-field small-FS mass-enhancement branch supports Friedemann 2013 LuRh2Si2 reference reanalysis | pass | pass | pass | pass | pass |
| Extension: `gcn_34ce9aa28e054fd1` | pass | pass | Many-body-method requirement is supported by YbRh2Si2 RBC/dHvA/LDA-failure evidence | pass | pass | pass | pass | pass |
| Connectivity repair support edges | pass | pass | Science-facing source graph is one connected component after ignoring generated `__*` helpers | pass | pass | pass | pass | pass |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_749b6767459b4785` | `paper:867752612177379569` | `gcn_677c6c...`, `gcn_03614e9b...`, `gcn_e0c364ff...`, `gcn_6bbfeb95...`, `gcn_ecddfefa...`, `gcn_2e693115...` | `gcn_2741cdef_practical_effective_mass_scheme` | deduction | 0.95 |
| `gfac_3874d7c0b7a44408` | `paper:811855974460555265` | `gcn_f82c178...`, `gcn_58746c...` | `gcn_45f24d_fcqpt_t_minus_two_thirds` | deduction | 0.95 |
| `gfac_0b967f9e875749e8` | `paper:811773737962569729` | `gcn_c243dcb...`, `gcn_48bba377...` | `gcn_42a4ff_rbc_hall_dos_values` | deduction | 0.95 |
| `gfac_5648470e5459468a` | `paper:812036747075518464` | `gcn_5501e18a...`, `gcn_f20b1f42...` | `gcn_c38f8ce_ybrh2si2_dhva_spectrum_lda_mismatch` | deduction | 0.95 |
| `gfac_468a4122_lurh2si2_reference_reanalysis` | `paper:867761295154217007` | `gcn_c131e014...`, `gcn_3dc248d...`, `gcn_3a8394c...` | `gcn_2b8dd97_lurh2si2_reference_reanalysis` | deduction | 0.95 |
| `gfac_d438ed7a0cad4d2e` | `paper:812369321199140865` | `gcn_021fb1...`, `gcn_24ebf8...` | `gcn_b4093_ybrh2si2_resistivity_mass_drop` | deduction | 0.95 |
| `gfac_717602aa489047e9` | `paper:867772725953823394` | `gcn_fb2747...` | `gcn_3a1514_ybrh2si2_kondo_lattice_hierarchy` | deduction | 0.95 |
| `gfac_44921f1b7d4e4c4a` | `paper:867762218521854503` | `gcn_a76225...` | `gcn_d8b1_ybrh2si2_esr_heavy_quasiparticles` | deduction | 0.95 |
| `gfac_a3846efd68654c47` | `paper:867761748805944216` | `gcn_dbe6ec...`, `gcn_faee88...`, `gcn_8f49e0...` | `gcn_4d206_ybrh2si2_kondo_lifshitz_interplay` | deduction | 0.95 |
| `gfac_3419693df9e1427e` | `paper:867773002954047503` | `gcn_6ca2b...`, `gcn_3ba45e...` | `gcn_b5d9_ybrh2si2_lifshitz_derenormalization` | deduction | 0.95 |
| `gfac_7960d27e3ad54880` | `paper:811888199457570817` | `gcn_848945...`, `gcn_5090f8...` | `gcn_d10f91_ybrh2si2_small_fs_mass_enhancement` | deduction | 0.95 |
| `gfac_9d14afa95eda494a` | `paper:813199962614530051` | `gcn_b01616...` | `gcn_34ce9_ybrh2si2_many_body_methods_required` | deduction | 0.95 |

## Cross-paper operator/support wiring

| item | action | LKM-backed rationale |
|---|---|---|
| Shaginyan 2010 FCQPT inflection premise / Shaginyan 2009 FCQPT inflection premise | `equivalence(..., prior=0.93)` | Both raw LKM claims state the same zero-derivative/cubic-spectrum FCQPT condition. |
| Shaginyan 2009 T^(-2/3) scaling / Shaginyan 2010 practical scheme | support | Same homogeneous Landau equation and FCQPT limit support the starting root's scaling component. |
| Friedemann 2010 RBC/gamma evidence / Shaginyan entropy-over-temperature mass proxy | support | Both use YbRh2Si2 thermodynamic density-of-states quantities as effective-mass proxies. |
| Friedemann 2010 RBC / Friedemann 2013b many-body method need | support | RBC is one of the many-body approaches the LKM conclusion says is required beyond static LDA. |
| Tokiwa high-field `A(B)` mass drop / Shaginyan entropy-over-temperature mass proxy | support | Same material and field-dependent effective-mass theme, distinct proxy routes. |
| ESR heavy quasiparticles / Shaginyan entropy-over-temperature mass proxy | support | ESR raw claim explicitly ties observables to `m*(B,T)`, DOS, and gamma-linked quasiparticle behavior. |
| LuRh2Si2 small-FS reference / Knebel dHvA-LDA mismatch / Rourke high-field branch / Friedemann 2013 reanalysis | support | All connections are grounded in raw YbRh2Si2/LuRh2Si2 dHvA and reference-model claims. |
| Tokiwa/Seiro/Naren high-field Kondo evidence / Pfau high-field Kondo-Lifshitz interpretation | support | The raw claims share YbRh2Si2 high-field Kondo suppression, mass reduction, and Lifshitz/de-renormalization evidence. |

## Semantic label presentation pass

| item | action | rationale |
|---|---|---|
| source `gcn_*` claim labels | renamed to semantic snake-case labels | Presentation-only refactor; claim content, LKM IDs, provenance metadata, priors, and graph wiring are unchanged. Full old-to-new mapping is in `semantic_label_audit.md`. |
| source `strat_gfac_*` deduction labels | renamed to semantic `derive_*` labels | Avoid raw factor-id fragments in rendered strategy labels while preserving factor IDs in this audit and raw LKM JSON. |
| `helper_*`, `sx_*`, `eq_*`, `strat_decompose_*`, generated `__*` labels | left unchanged | These labels were already semantic or compiler-generated internals. |

## Verification snapshot

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | 89 knowledge, 31 strategies, 1 operator; IR hash `sha256:2580858f...`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 25 independent claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | 58 beliefs inferred; exact JT converged after 2 iterations. |

## Coherent stopping rationale

The package stops at 89 total knowledge nodes. Adding the prior He-3, Brinkman-Rice/Mott, NiS2, or CeMo2Si2C branches would require either accepting disconnected components or restoring agent-authored synthesis claims. The May 4 rebuild therefore prefers one connected YbRh2Si2 graph below the nominal 100-node target over an inflated graph with unsupported bridges.
