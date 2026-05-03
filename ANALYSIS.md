# Analysis

## Verification

The package was compiled and checked after the Friedemann2010 extension synthesis:

```bash
gaia compile .
gaia check --brief .
gaia check --hole .
gaia infer .
gaia render . --target github
gaia render . --target docs
```

Results:

- `gaia compile .`: passed, `38 knowledge`, `11 strategies`, `0 operators`.
- `gaia check --hole .`: passed, `0 holes / 10 independent claims`.
- `gaia infer .`: passed with exact junction-tree inference and convergence after 2 iterations.
- `gaia render . --target docs`: generated `docs/detailed-reasoning.md`.

## Exported Conclusions

| Label | Belief | Notes |
|---|---:|---|
| `gcn_800070efac5e476d` | 0.803 | He-3 heat-capacity route to `m*/m` and `F1`. |
| `gcn_2741cdef_practical_effective_mass_scheme` | 0.594 | YbRh2Si2 Landau/entropy route to `M*(T,B)`. |
| `gcn_42a4ff_rbc_hall_dos_values` | 0.795 | YbRh2Si2 material-specific RBC/Hall/DOS evidence. |
| `cross_thermodynamic_routes_to_effective_mass` | 0.766 | Scoped synthesis: both roots use thermodynamic quantities as operational routes to effective mass. |
| `cross_scope_caution_standard_fl_vs_fcqpt` | 0.636 | Guardrail: the roots should not be merged as equivalent claims. |
| `cross_ybrh2si2_rbc_qualifies_homogeneous_isotropic_scope` | 0.708 | Friedemann2010 RBC evidence qualifies the homogeneous isotropic YbRh2Si2 model scope. |

## Independent Premises

All independent premises have priors in `src/fermi_liquid_effective_mass/priors.py`; direct claim priors are capped at `0.90` and marked `TODO:review`.

The lowest direct prior is `gcn_03614e9b_homogeneous_isotropic_model` at `0.68`, reflecting the scope risk of applying a homogeneous isotropic model to YbRh2Si2. The new Friedemann2010 leaf priors are `gcn_c243dcb_rbc_phase_shift_parametrization` at `0.82` and `gcn_48bba377_specific_heat_calibration` at `0.76`. The highest direct prior remains `gcn_ecddfefa_fermion_entropy_formula` at `0.90`, reflecting the standard Fermi-Dirac entropy formula.

## Audit Notes

The final graph was built from three audited single-root subgraphs:

- `artifacts/subgraphs/he3-effective-mass-gaia`
- `artifacts/subgraphs/ybrh2si2-effective-mass-gaia`
- `artifacts/subgraphs/ybrh2si2-rbc-hall-gaia`

No exact cross-paper merge, equivalence, or contradiction was promoted. The synthesis uses support-only cross-paper wiring and records the standard-Fermi-liquid versus FCQPT/crossover scope distinction. The Friedemann2010 extension adds a second scope guard: material-specific RBC/Hall/DOS evidence qualifies the homogeneous isotropic YbRh2Si2 premise rather than refuting it.
