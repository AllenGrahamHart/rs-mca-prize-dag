# XR active-defect primitive Pade-list census

- **status:** TARGET
- **parent:** `xr_band_maximal_window_divisor_count`

In the setup of SL-2-RES, assume `rank J_d<2d` and that the maximal
selected family is nonempty. Let `G_d` be the set of evaluation points
at which both reversed coefficient polynomials of every left syzygy
vanish. Use the proved primitive pair `P,Q` and define the base-independent
active residual support

```text
D={x in H:P(x)(u-f)(x)+Q(x)(v-g)(x)!=0},       e=|D|.
```

Then `D subset G_d` and `e<=|G_d|<=d-ell-1`. Let `R_d^D(u,v)` be the
subset of maximal selected post-strip locators for which **every** selected
ray has all of its off-core agreement points in `D`. The active-defect
router pays the complementary family with at most `n-e` locators.

In the only deficient stratum in which `R_d^D` can be nonempty, assume

```text
e >= 2(h-d).
```

The proved routers confine the target to

```text
ceil((2h+2)/3) <= d <= h-2,
K_d={(SP,SQ):S in W},
gcd(P,Q)=1,       ell=max(deg P,deg Q)<=3d-2h-1,
(f,g)=(f_0+Q tau,g_0-P tau),       deg tau<k-ell.
```

Distinct full joint cores intersect in at most `k-ell-1` points. There is
a fixed word `w` on `H\D` such that the target injects into

```text
tau in RS[F,H\D,k-ell],       agr(tau,w)=k+d.
```

For each selected projective slope `lambda=[alpha:beta]`, all roots in
`H\D` of `alpha Q-beta P` already lie in the joint core, and its exact
`h-d` off-core points form one block in `D`. The at least two selected
blocks are disjoint. These conditions are proved conclusions, not extra
premises.

Then the `D`-local maximal, selected, post-strip locator set satisfies

```text
25 |R_d^D(u,v)| <= 17 n^2 - 25(n-e).               (SL2-D)
```

The proved affine-span and mixed core/block payments close `(SL2-D)` whenever
the affine hull of the parameter set has dimension at most `10,10,9` at rates
`1/4,1/8,1/16`.  Thus a counterexample necessarily has affine dimension at
least `11,11,10`.

At those next dimensions, the proved affine-plane component payment closes
every `r>2ell` tuple with `d+ell<=6,840,580,025` at rates `1/4,1/8` and
with `d+ell<=3,435,973,837` at rate `1/16`; its `ell=1` payment at rate
`1/16` extends through `d+1=3,523,371,941`.  The
positive-dimensional conic degeneracies have constant selected ray and are
removed by the same-ray interaction strip.

The exact `phi`-fiber router sharpens the triple count to

```text
T_pack(r,ell)=binom(q,3)ell^3+binom(q,2)ell^2 u,
q=floor(r/ell),       u=r-q ell.
```

It also identifies the precise triple-invisible endpoint: every selected
block locator divides one or two members `bP-aQ` of the primitive pencil,
and every target in that endpoint owns at least two disjoint such locators.
Thus `r<=2ell` is not itself an unresolved stratum; high-fiber blocks there
remain available to triple incidence.

The common-ray eliminant uses `s+1` distinct-`phi` points directly on the
`s`-dimensional affine hull.  Its matrix-pencil argument improves the fixed
tuple owner cap from `2^s` to `s+1`.  At the next dimensions it extends the
proved `ell=1` slices through

```text
rates 1/4,1/8: d+1<=8,500,560,263,
rate 1/16:     d+1<=4,265,559,234.                  (SL2-CRE)
```

The exact higher-order fiber profile and a factorwise comparison with these
`ell=1` endpoints give the uniform higher-`ell` envelope

```text
rates 1/4,1/8: d+11ell-10<=8,500,560,263,
rate 1/16:     d+10ell-9 <=4,265,559,234.            (SL2-UE)
```

The residual high-fiber tails outside `(SL2-UE)` and the split-pencil locator
census stay open, so the node remains `TARGET`.

Finally, the two selected blocks lie in `G_d`, so the primitive multiplier
space satisfies

```text
dim K_d<=d-ell-|G_d|<=3d-2h-ell.                   (SL2-ABN)
```

At the tuple-incidence no-go boundary this is at most `6,6,2` on the three
rates. Thus the extremal residue is a bounded-nullity extension of the
separate full-rank window-divisor target, not an arbitrary-rank family.

Retaining the degree slack gives a stronger boundary normal form. Put

```text
sigma=d-ell-1-2(h-d).
```

At the same obstruction `sigma=5,5,1`. Every target has exactly two selected
live slopes; their blocks cover all but at most `sigma` points of the complete
forced-root set, and every kernel multiplier is the forced-root locator times
a polynomial of degree below `sigma+1`. Thus the positive-nullity residue is
an almost complete two-ray cover. This extra structure is absent from the
full-rank branch.

Together with the unconditional outside-`D` payment, `(SL2-D)` gives
`25|R_d(u,v)|<=17n^2` exactly. This is an owner-aware punctured list with
active-defect blocks. It is not a raw ordinary list, a one-parameter
locator-pencil count, or the upstream whole-support owner localization.

## Falsifier

One official deficient high-window system in the displayed primitive
normal form with
`25|R_d^D|>17n^2-25(n-e)`. A raw punctured list without exact maximality,
selected liveness, active-defect blocks, and the all-selected-rays-local
predicate is not a falsifier.
