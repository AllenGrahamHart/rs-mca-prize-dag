# Proof

## 1. (LA-EQ)

Let a strict `A=3`, `e=m` endpoint configuration exist. By (SAT4)-(SAT5) it
has at least `15m` parameter-saturated points, and by (RNC1)-(RNC2) it
carries a nonzero kernel biform `Q` of bidegree `(m, rho)` vanishing on all
its incidences. Restrict the configuration to any `7m-1` of those saturated
points: `Q` still vanishes on every incidence of the restriction, so the
layer-A evaluation matrix of the restriction has nullity `>= 1`. Hence, if
`H` is any hypothesis set the restriction satisfies and `(LA-W COUNT | H)`
asserts full rank, then no such endpoint exists.

So a conditional rank theorem would *imply* the endpoint exclusion. It is a
strengthening, and by sections 2-4 a **strict** one.

## 2. (H1) is false

Set `Q = (Z-g)(Z-h)C(X) + a(Z-h)sigma_g(X) - b(Z-g)sigma_h(X)` with
`sigma_g, sigma_h` the monic degree-`rho` polynomials with root sets
`S_g, S_h subset mu_32`, `|S_g ^ S_h| = m-1 = 1`. Then

```text
Q(g, X) = a(g-h) sigma_g(X),        Q(h, X) = b(g-h) sigma_h(X),
```

so `g` and `h` are supported slopes with supports exactly `S_g, S_h`, both
split over `mu_32`. For `x in S_g \ S_h`, `sigma_g(x) = 0` and

```text
Q(Z,x) = (Z-g)[(Z-h)C(x) - b sigma_h(x)],
```

so `x` has a second slope `h + b sigma_h(x)/C(x)`; symmetrically for
`x in S_h \ S_g` the second slope is `g - a sigma_g(x)/C(x)`. The shared
point `x_0` has `Q(Z,x_0) = (Z-g)(Z-h)C(x_0)`, so its two slopes are `g` and
`h`. Every point of `W = S_g u S_h` is thus saturated by exactly `m = 2`
slopes, `|W| = 2rho - (m-1) = 13 = 7m-1`, and there are `26` incidences
against `(m+1)(rho+1) = 24` coefficients — count excess `3m^2-5m = +2`.

The verifier builds admissible instances at random and finds layer-A nullity
exactly `1` in every one (`47/47` at `q=97`, `37/37` at `q=193`). The kernel
is spanned by `Q` itself. So the count excess does not force full rank, and
the H1 rung cannot carry a rank theorem.

## 3. (H1+H2) is false, and the solve is one scalar condition

H2 additionally demands that ALL pair intersections be `<= m-1 = 1` and that
`T = rho+2 = 9` exactly. A merged slope obtained from two points of the same
side would have both its points inside one of `S_g, S_h`, giving a pair
intersection `2 > 1`. So the merges must be **cross** merges, one point from
each side. Five cross merges plus two singletons account for the `12`
non-shared points and give `2 + 5 + 2 = 9` slopes with support profile
`[7,7,2,2,2,2,2,1,1]`.

Prescribing the merged VALUE `tau` turns each merge into a prescribed value
of `C`:

```text
C(x_1)(tau - h) = b sigma_h(x_1),      C(x_2)(g - tau) = a sigma_g(x_2),
```

both **linear** in the unknowns `(C_0,...,C_7, a)`. Five cross pairs give
`10` such equations on `9` unknowns: solvability is a single scalar
condition. The verifier fixes four target slopes, scans the fifth over
`F_q`, solves the linear system, and then checks the resulting object
independently: `C` nonvanishing on `W`, the induced slope multiset, the
profile, `T = 9`, max pair-intersection `1`, `26` incidences, and layer-A
nullity `1`. An exhibit is produced at `q = 97`.

## 4. (FENCE-m): nullity `>= 2m`, with equality measured

Take `D = mu_{16m}`, so `x -> x^{2m}` has image `mu_8` and fibres of size
`2m`. Choose `4` fibres (`8m` points) and let `W` be `a = 7m-1 <= 8m` of
them. For `x in W`, `gamma^m = x^{2m}` has exactly `m` solutions, all of them
among the `4m` `m`-th roots of the four chosen fibre values; adjoining one
spare gives `T = 4m+1` slopes and `m(7m-1)` incidences against
`(m+1)(rho+1) = 4m(m+1)` coefficients, `rho = 4m-1`.

Every biform `A(X)(Z^m - X^{2m})` with `deg A <= rho - 2m = 2m-1` has the
allowed bidegree and vanishes on every incidence, so

```text
nullity >= 2m
```

for free. The verifier confirms **equality** at `m = 3` over `mu_48` at
`q = 97`: `60 x 48`, rank `42`, nullity `6`. The count excess there is
`3m^2-5m = +12`, so the bare count is dead at `m = 3` as well as at `m = 2`.

## 5. What is NOT proved

(LA-PADE)/(LA-DEG) is carried at POSED and is not re-derived here. H3 and H4
are untested. No (SAT2)-satisfying configuration at `m >= 2` was built or
sought — that rung is the open realizability problem, and it is where the
ladder terminates.
