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
