# LKM candidates: Fermi-liquid effective mass

Discovery queries:

- `Fermi liquid effective mass`
- `quasiparticle effective mass Fermi liquid`
- `effective mass enhancement in Fermi liquid`
- `heavy fermion Fermi liquid effective mass`
- `electron effective mass Fermi-liquid theory`

Raw inputs are preserved under `artifacts/lkm-discovery/input/`.

## Chain-backed candidates

[1] Liquid He-3 near superfluid transition | gamma = 2.11 K^-1 implies m*/m approximately 2.12 and F1 approximately 3.36 | Alvesalo et al. 1979 | Heat-capacity data are mapped through standard Landau Fermi-liquid relations to an effective-mass ratio.

- claim id: `gcn_800070efac5e476d`
- source: `paper:811623956246167556`
- title: `Observation of Anomalous Heat Capacity in Liquid He 3 near the Superfluid Transition`
- evidence file: `input/evidence_gcn_800070efac5e476d.json`
- total chains: 1

[2] YbRh2Si2 / homogeneous heavy-electron liquid | solve the Landau effective-mass equation and extract M*(T,B) = S(T,B)/T | Shaginyan et al. 2010 | A computational recipe produces temperature- and field-dependent effective mass near fermion-condensation criticality.

- claim id: `gcn_2741cdef209a457a`
- source: `paper:867752612177379569`
- title: `Energy scales and the non-Fermi liquid behavior in YbRh2Si2`
- evidence file: `input/evidence_gcn_2741cdef209a457a.json`
- total chains: 1

[3] Layered TiS2 optical/transport Fermi-liquid damping | fitted prefactor p approximately 13.6 exceeds isotropic effective-mass Fermi-liquid prediction p = 2*pi approximately 6.28 | Julien et al. 1991 | The quantitative mismatch points to anisotropy, restricted umklapp phase space, effective-mass uncertainty, or disorder.

- claim id: `gcn_72cad51e8f544730`
- source: `paper:812409375854428160`
- title: `Fermi liquid reflectivity of TiS2`
- evidence file: `input/evidence_gcn_72cad51e8f544730.json`
- total chains: 1

[4] Pressure-metalized NiS2 near a Mott insulator | 6.03 kT belly orbit and m* = 6(2) m_e at approximately 3.8 GPa | Friedemann et al. 2016 | Large Fermi-surface volume plus strongly enhanced effective mass support a Brinkman-Rice correlated Fermi liquid.

- claim id: `gcn_29401e4284574aa2`
- source: `paper:814525482547544066`
- title: `Large Fermi Surface of Heavy Electrons at the Border of Mott Insulating State in NiS2`
- evidence file: `input/evidence_gcn_29401e4284574aa2.json`
- total chains: 1

## Chainless matches

The match union contained 25 distinct claim ids. Evidence fetching found 4 chain-backed candidates, 20 chainless candidates, and 1 transient `code=290001` claim that still failed after retry (`gcn_6d0a196f674543cc`). Chainless matches are retained as raw JSON only and are not eligible as Gaia roots unless the user explicitly waives the chain-backed-root invariant.
