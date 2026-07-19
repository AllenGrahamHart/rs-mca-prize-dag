# XR rank-five `u=1` split-locator nonbasis bound

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_rank_five_extension_list_reduction`

In the rank-five extension-list reduction with `u=1`, delete the `v` loop
coordinates and scale the others. The kernel is the evaluation of a
four-dimensional subspace

```text
W subset F[X]_{<=4}
```

with no common evaluation root on the remaining `N`-point domain `E`.
For each four-set `T subset E`, put `L_T=product_(x in T)(X-x)`.

The set `T` is a nonbasis of the coordinate matroid of `W` exactly when

```text
L_T in W.                                               (NB1)
```

The total number `Z_4(W,E)` of such nonbasis four-sets satisfies

```text
Z_4(W,E)
 <= floor((C(N,3)+(N-2)(N-4))/4).                       (NB2)
```

The same bound applies after restricting to any agreement set. At the three
RowC rows, an agreement set has size `10,10,8`, so it contains at most

```text
42,42,20
```

nonbasis four-sets and therefore at least

```text
168,168,50
```

kernel bases.

This is the exact source-to-flat bridge for the one-defect quartic kernel and
a source-specific refinement of the abstract split-locator flat theorem in
upstream PR `przchojecki/rs-mca#747`. The resulting basis bounds do not by
themselves pay either XR consumer.
