# L1 coarse p-free Wronskian neighbor compiler

- **status:** PROVED
- **role:** compile coarse p-free collisions into unique low-degree
  Wronskian certificates
- **consumer:** `l1_mixed_petal_amplification`

## Setup

Use the coarse p-free map `Phi_free` from
`l1_coarse_pfree_wronskian_distance_packing`. Fix an `a`-set `A` in one
fiber. For another member `B`, put

```text
X=A\B,       Y=B\A,       |X|=|Y|=t,
F_X=product_(x in X)(Z-x),       F_Y=product_(y in Y)(Z-y),
W_(X,Y)=F_X'F_Y-F_XF_Y'.                              (WNC1)
```

Then

```text
tau_0=ceil((d+2)/2),
tau_p=max(tau_0,min(d+1,p)),       t>=tau_p,
D_t:=2t-d-2>=0,
deg W_(X,Y)<=D_t.                                     (WNC2)
```

## Unique certificate

For fixed `X`, the polynomial `W_(X,Y)` determines `Y` uniquely among monic
degree-`t` tails. Moreover it is nonzero at every point of `X union Y`.

For `t` distinct field points define the exact full-support certificate count

```text
R_q(t,D)=sum_(j=0)^t (-1)^j binom(t,j)
                         q^max(D+1-j,0).              (WNC3)
```

This is the number of degree-at-most-`D` polynomials nonzero on all `t`
points. Hence, for fixed `X`, at most

```text
min(binom(n-a,t), R_q(t,D_t))                         (WNC4)
```

members `B` have `A\B=X`. Every nonempty coarse fiber therefore obeys

```text
|Phi_free^(-1)(z)|
 <=1+sum_(t=tau_p)^min(a,n-a)
       binom(a,t) min(binom(n-a,t),R_q(t,2t-d-2)).    (WNC5)
```

## Collision-gap parity

Write `t=tau_0+j`. At formal half-depth excess `j>=0`,

```text
d even:       D_t=2j,
d odd:        D_t=2j+1.                               (WNC6)
```

Thus the minimum-width certificate is constant when `d` is even and linear
when `d` is odd. Its exact certificate counts are respectively

```text
q-1,       (q-1)(q+1-tau_0).                          (WNC7)
```

Only strata with `j>=tau_p-tau_0` are admissible. In particular, at an
official checkpoint depth every stratum with `t<p` is empty.

## Scope

This is an arbitrary-target, characteristic-safe neighbor theorem for the
coarse p-free map. It removes any hidden multiplicity after `(X,W)` is fixed
and gives an exact collision-gap hierarchy. The remaining choice of `X` can
still be exponential when `tau_p=Theta(n)`, so `(WNC5)` does not prove
row-sharp Q, Pade-graph coalescing, or L1. It is not the exact mixed-prefix
decorated shift-pair compiler.
