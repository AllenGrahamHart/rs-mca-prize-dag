# Post-strip affine-pencil charge

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependencies:** `xr_affine_core_all_zero_charge`,
  `xr_strip_classification_rungs`

Let `H:F^D->Y` be linear, where `|D|=n` and `ker H` has minimum distance at
least `R+1` with `R=n-k`. Fix `1<=h<=R`, put `r=R-h`, and let `P` contain one
pair `(gamma,e)` at each of a finite set of distinct slopes. Assume

```text
e in A,       He=y_0+gamma y_1,       wt(e)<=r,
```

where `A` is an affine space above the nonconstant syndrome line, has affine
dimension `s`, and satisfies the genericity hypothesis of the affine-core
charge. Put `a=s-1`, and assume `n-r>=a+1`.

Suppose additionally that for distinct pairs in `P`,

```text
|Z_e intersect Z_f| <= kappa <= k.
```

Then

```text
|P| C(h+a,a)
 <= C(n,a) floor((n-kappa)/(k+h-kappa)).              (PSP)
```

The post-strip high-core selector uses `kappa=k`, giving the cap
`floor(R/h)`. The low-core selector may use `kappa=k-1`, giving the slightly
stronger cap `floor((R+1)/(h+1))`.

At the six XR rows, either application pays full-domain selector ranks

```text
4,4,4,15,15,14.
```

Therefore every remaining selector has rank at least `5,5,5` on the RowC
rows and at least `16,16,15` on the prize rows. This is a rank-frontier
improvement, not a proof of either XR target.
