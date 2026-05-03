# Analysis

## Verification

The package was compiled and checked after synthesis:

```bash
gaia compile .
gaia check --brief .
gaia check --hole .
gaia infer .
gaia render . --target github
gaia render . --target docs
```

Results:

- `gaia compile .`: passed, `24 knowledge`, `6 strategies`, `0 operators`.
- `gaia check --hole .`: passed, `0 holes / 8 independent claims`.
- `gaia infer .`: passed with exact junction-tree inference and convergence after 2 iterations.
- `gaia render . --target docs`: generated `docs/detailed-reasoning.md`.

## Exported Conclusions

| Label | Belief | Notes |
|---|---:|---|
| `gcn_800070efac5e476d` | 0.803 | He-3 heat-capacity route to `m*/m` and `F1`. |
| `gcn_2741cdef_practical_effective_mass_scheme` | 0.594 | YbRh2Si2 Landau/entropy route to `M*(T,B)`. |
| `cross_thermodynamic_routes_to_effective_mass` | 0.766 | Scoped synthesis: both roots use thermodynamic quantities as operational routes to effective mass. |
| `cross_scope_caution_standard_fl_vs_fcqpt` | 0.636 | Guardrail: the roots should not be merged as equivalent claims. |

## Independent Premises

All independent premises have priors in `src/fermi_liquid_effective_mass/priors.py`; direct claim priors are capped at `0.90` and marked `TODO:review`.

The lowest direct prior is `gcn_03614e9b_homogeneous_isotropic_model` at `0.68`, reflecting the scope risk of applying a homogeneous isotropic model to YbRh2Si2. The highest is `gcn_ecddfefa_fermion_entropy_formula` at `0.90`, reflecting the standard Fermi-Dirac entropy formula.

## Audit Notes

The final graph was built from two audited single-root subgraphs:

- `artifacts/subgraphs/he3-effective-mass-gaia`
- `artifacts/subgraphs/ybrh2si2-effective-mass-gaia`

No exact cross-paper merge, equivalence, or contradiction was promoted. The synthesis uses support-only cross-paper wiring and records the standard-Fermi-liquid versus FCQPT/crossover scope distinction.
