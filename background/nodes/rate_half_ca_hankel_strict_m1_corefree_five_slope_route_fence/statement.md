# Strict `m=1` core-free five-slope Hankel route fence

- **status:** PROVED
- **closure:** exact finite-field witness and complete locator-line census
- **consumer:** `rate_half_band_closure` as evidence only
- **dependency:** `rate_half_ca_hankel_split_pencil_equivalence`

The strict `A=3` endpoint bound is false as a theorem uniform in the scale
parameter `m`, even after imposing core-freeness and the full Hankel/apolar
origin. At the exact `m=1` analogue, put

```text
F=F_17,       D=F_17^*,       N=16,       R=k=8,
r=rho=3,      A=R+1-2rho=3,  e=1,       s=0.
```

The primitive generic kernel form

```text
Q(z;X)=X^3+(9+4z)X^2+12zX+7                         (M1F1)
```

is the kernel of the `5 x 4` syndrome Hankel pencil formed from

```text
y_0=(1,10,16,2,14,0,3,11),
y_1=(0,14,9,7,13,12,15,0).                           (M1F2)
```

The pencil has rank three at every finite slope and at infinity. It is
column-far, has no fixed evaluation-domain root, and has exactly five finite
supported slopes:

```text
z=0:  {1,2,5}
z=1:  {3,7,11}
z=2:  {9,12,13}
z=4:  {4,6,16}
z=15: {8,10,15}.                                     (M1F3)
```

These five triples partition `D\{14}`. Hence

```text
T=5>rho+1=4,                                          (M1F4)
```

which is the one-slope failure shape predicted by the strict endpoint
ledger.

The witness is not isolated at locator level. Among all `C(16,3)=560` monic
split cubic locators over `D`, the maximum number on a core-free affine
coefficient line is exactly five. There are exactly `16` such five-lines,
one for each omitted domain point. For every one of them, the linear Hankel
compatibility system has projective nullity one and its unique syndrome
pencil has rank three at all `18` projective slopes.

This does not refute the official endpoint, where `m=2^37`. The surviving
`m=1` family is a rank-two separated pencil. The proved official
`m>1` component-defect, separation-rank, and separated-pullback exclusions
are therefore load-bearing: no argument using only root incidence,
core-freeness, split fibers, or the Hankel equations can close the official
endpoint uniformly in `m`.

