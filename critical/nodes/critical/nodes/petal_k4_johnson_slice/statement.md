# Exact Johnson slice for the petal K4 auxiliary list

- **status:** PROVED
- **consumer:** `petal_k4_primitive_bound`
- **provenance:** an independently replayed local form of Paper D v13,
  `thm:capf-johnson-list(ii)` and `cor:capf-pma-johnson`; the new local value
  is the constants-explicit K4 scope bridge.

Let `T` be an evaluation set of size `ell`, let `0<=d<ell`, and let `U` be
an arbitrary received word on `T`.  If `N<=ell` and

```text
N^2 > d ell,
```

then the number of degree-`<=d` polynomials agreeing with `U` in at least
`N` positions is at most

```text
floor(ell (N-d) / (N^2-d ell)) <= ell^2.
```

The same bound holds after imposing any exact-support property, in particular
the stabilizer-primitive condition in K4.

For every G1 sunflower chart in this Johnson regime, `ell=|T|<=n`; hence its
K4 contribution is at most `n^2`.  Consequently the only unresolved K4 charts
are the correlated-target sub-Johnson charts satisfying `N^2<=d|T|`.
