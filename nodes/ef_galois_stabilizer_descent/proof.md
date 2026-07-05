# proof: ef_galois_stabilizer_descent

Let `G = Gal(E/B)`. The extension-fiber incidence is defined over `B`, because
the received pair `(u,v)` and the alignment equations are B-rational. Hence
`G` acts on its horizontal irreducible components.

Let `X` be one such component and let

```text
H = {g in G : gX = X}
```

be its stabilizer. Let `K = E^H` be the fixed field.

If `H = G`, then `X` is invariant under every B-automorphism. Its homogeneous
ideal is G-stable, so by Galois descent it has equations over `B`. This is the
base-descended case.

If `H` is a proper nontrivial subgroup, then the same descent argument gives
equations over the intermediate fixed field `K`, with `B < K < E`. Thus the
component is confined to an intermediate subfield and belongs to the tower
case.

If `H` is trivial, then the orbit of `X` has full size `|G|`. This is exactly
the genuinely full-field case not explained by descent or tower confinement.

These alternatives are exhaustive by the Galois correspondence. Therefore the
only component class not already base-descended or subfield-confined is the
full-orbit case routed to `ef_full_orbit_pole_forcing`.
