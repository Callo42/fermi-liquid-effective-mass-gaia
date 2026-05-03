# Dismissed contradiction candidates: CeMo2Si2C KW/Wilson root vs parent branches

## Candidate tensions checked

- **Thermodynamic-route branch:** the parent package has He-3 and YbRh2Si2 roots that use thermodynamic quantities as operational routes to quasiparticle effective mass (`gamma -> m*/m` for He-3 and `S/T -> M*(T,B)` for YbRh2Si2).
- **Correlated-FL/RBC branch:** the parent package has a YbRh2Si2 renormalized-band branch in which a material-specific RBC parameterization is constrained by CEF energies and low-temperature `gamma`, then used to discuss DOS and Hall-product cancellation.
- **New CeMo2Si2C root:** the selected Paramanik et al. 2013 chain combines `A`, `gamma`, and `chi_FL` into Kadowaki-Woods and Wilson/Sommerfeld ratios and interprets both as correlated Fermi-liquid consistency checks.

## Verdict

Dismissed as compatible scope distinctions, not promoted to `contradiction()` or `equivalence()`.

## Rationale

The branches can all be true. The CeMo2Si2C root is an empirical low-temperature ratio check in an intermediate-valent Ce compound. The He-3 branch maps a measured low-temperature specific-heat coefficient to an effective-mass ratio in a different Fermi liquid. The Shaginyan YbRh2Si2 branch uses a homogeneous FCQPT model and an `S/T` effective-mass proxy across crossover/non-Fermi-liquid regimes. The Friedemann YbRh2Si2 RBC branch uses material-specific band/DOS/Hall calculations. These are related thermodynamic/correlated-FL motifs, but not mutually exclusive claims about the same material, observable, and regime.

## Within-chain quantitative caution

Factor step 4 notes an alternative Tsujii/Kontani/Yoshimura degeneracy scaling: for an intermediate-valent Ce system with `N=6`, the expected `A/gamma^2` scale is `6.7e-7 muOmega cm (mol K/mJ)^2`, lower than the measured `0.5e-5` value emphasized as the original Kadowaki-Woods scale. This is retained as a synthesis caution and possible future open question about which KW normalization is most appropriate for CeMo2Si2C, but it is not a direct contradiction inside the selected chain.
