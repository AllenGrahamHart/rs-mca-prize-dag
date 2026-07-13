# All-LineRay affine-core bound

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`

Let `H:F^D->W` be linear with kernel distance greater than `t`. Fix a
nonconstant syndrome line `y_0+gamma y_1`, and let `P` be a finite set of
distinct pairs `(gamma,e)` such that

```text
H e = y_0+gamma y_1,        wt(e)<=t,
{y_0,y_1} is not contained in H(F^supp(e)).
```

Choose any `e_*` occurring in `P`, and put

```text
A_P=span{e-e_*:(gamma,e) in P},
s=dim A_P,       w=max_(gamma,e) wt(e).
```

Then

```text
sum_((gamma,e) in P) 1/C(s+wt(e),s) <= 1,
|P| <= C(s+w,s) <= C(|D|,s).                         (AC)
```

Let `Gamma(P)` be the slope projection. Apply `(AC)` to a set containing
exactly one pair above every slope. If `sigma(P)` is the minimum affine error
rank over all such selectors, then

```text
|Gamma(P)| <= C(sigma(P)+t,sigma(P)).                  (SEL)
```

For an RS row at agreement `A`, take `t=r=n-A` and let `P` be all retained
LineRay pairs in any chosen stratum. The generic/common-support exclusion is
exactly the transversality hypothesis above, and RS distance is greater than
`r`. Hence the complete pair count is at most `C(s+r,s)`, while the distinct
slope count is at most `C(sigma+r,sigma)` for the minimum selector rank
`sigma`.

At all six XR candidates,

```text
d<=3  =>  C(d+r,d)<=8n^3,
d=4   =>  C(4+r,4)>8n^3,
```

for either the complete-family rank `d=s` or selector rank `d=sigma`.

Thus both XR predicates are proved whenever there exists a one-per-slope
selector of affine rank at most three. A counterexample must have rank at
least four for every selector. No assertion is made that such a selector must
exist; the high-transversal-rank branch remains open.
