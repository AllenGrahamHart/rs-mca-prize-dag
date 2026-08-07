# Proof - PMA petal-pattern root-pinning ledger

## 1. Petal support is larger than the defect

Use the exact core-defect form

```text
P=Q+L_(C\D)W,       F=L_D,       deg W<=d.
```

Let `r` be the number of background agreements. The retained core contributes
`k-1-d` agreements, so the list threshold gives

```text
(k-1-d)+r+h >= k+ell-1,
r+h >= d+ell.
```

Maximality gives `r<=b<ell`, hence `h>d`. Exactness of `D` also gives
`gcd(F,W)=1` by `pma_saturated_mixed_support_kernel`.

## 2. Fixed petal pattern

Fix `(I,(S_i))`, its union `Y`, and the defect degree `d`. On `Y` the pair
`(F,W)` obeys

```text
W(y)=c_iF(y)       for y in S_i.
```

Define the selected-support top-coefficient map exactly as in the saturated
kernel theorem, but using only the `h` petal points in `Y`. Since `h>d`, its
target width is

```text
w_Y=h-d-1>=0.
```

The maximal-rank proof of that theorem uses only a degree-`d` kernel locator,
a degree-at-most-`d` partner, and their coprimality. It therefore applies to
this selected labelled support and gives

```text
rank T_(Y,d)=min(d,w_Y).
```

Its canonical core-root pinning argument then bounds all monic degree-`d`
split locators in the kernel by

```text
binom(k-1,max(0,d-w_Y))
 = binom(k-1,max(0,2d+1-h)).
```

For a fixed locator `F`, the values `c_iF(y)` on the `h>d` distinct points
of `Y` determine at most one polynomial `W` of degree at most `d`. The pair
`(F,W)` determines `D`, then `P=Q+L_(C\D)W`. It also determines every
background agreement: those are precisely the background roots of `W`.
Thus no background-support factor is present, and `(PRP2)` is the complete
fixed-pattern multiplicity bound.

## 3. Pattern aggregation

There are `binom(M,t)` choices for the touched-petal set. For fixed `I`, the
number of exact patterns with total petal agreement `h` is at most
`binom(t ell,h)`; this harmlessly includes subsets that miss an allegedly
touched petal. Multiplying this pattern count by `(PRP2)` proves `(PRP1)`.

## 4. Polynomial region

Write

```text
u=t ell-h,       e=max(0,2d+1-h).
```

For one stratum with `u+e<=E`, use

```text
binom(M,t)<=2^M,
binom(t ell,h)=binom(t ell,u)<=n^u,
binom(k-1,e)<=n^e.
```

Its contribution is at most `2^M n^E`. There are at most `M` choices of
`t`, at most `E+1` relevant values of `u`, and at most `k` defect values.
Since `M,k<=n`, summing gives

```text
(E+1)n^(E+2)2^M.
```

At the lower cutoff,

```text
M=floor((n-k+1)/ell)<=n/ell<=log_2(n)/C_0,
```

so `2^M<=n^(1/C_0)`. This proves `(PRP4)`. For a full-petal pattern `u=0`
and `h=t ell`, so `(PRP3)` becomes the displayed condition
`max(0,2d+1-t ell)<=E`.
