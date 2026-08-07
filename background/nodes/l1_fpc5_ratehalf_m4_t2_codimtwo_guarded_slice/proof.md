# Proof: rate-half FPC5 codimension-two guarded slice

## 1. The boundary forces the whole background

Put `j=ell-b`. The official codimension sieve gives

```text
5ell=k+1+j,       j==3 (mod 5),       j>=3.
```

The assumption `c_petal=2` gives `s=ell-3`. The two-full-petal threshold is

```text
s<=r<=b=ell-j.
```

Therefore `ell-3<=ell-j`, so `j<=3`. Hence `j=3` and

```text
b=ell-3,       r=b=s,       5ell=k+4,       d=2ell-3.
```

Since `r=b`, every unused background point is an agreement. The core-defect
normal form says exactly that `W` vanishes there, proving `L_0|W` in (GS2).

## 2. Guarded cofactor normal form

The two touched-petal equations define unique cofactors

```text
A_i=(W-c_iF)/L_i,       deg A_i<=d-ell=ell-3.
```

Because the sunflower construction uses distinct nonzero petal labels,
`c_1`, `c_2`, and `c_2-c_1` are invertible. From

```text
W=c_1F+L_1A_1=c_2F+L_2A_2
```

we obtain

```text
(c_2-c_1)W=c_2L_1A_1-c_1L_2A_2.                     (1)
```

The condition `L_0|W` is therefore equivalent to (GS3). Dividing (1) by
`(c_2-c_1)L_0` gives `G`, and then (GS4) reconstructs `W` and `F`. The degree
bounds follow from

```text
deg(L_iA_i)<=2ell-3,
deg G<=ell,
deg(L_0G)<=2ell-3.
```

This proves the claimed linear bijection.

## 3. Dimension and locator projection

Reduction modulo `L_0` sends `(A_1,A_2)` to

```text
c_2L_1A_1-c_1L_2A_2 mod L_0.
```

The three locators have disjoint root sets, so `L_1` is a unit modulo `L_0`.
By varying `A_1` through polynomials of degree `<deg L_0=ell-3` and taking
`A_2=0`, this map reaches every residue class. Its rank is `ell-3`. Its
domain has dimension `2(ell-2)`, hence its kernel and the guarded pair slice
have dimension `ell-1`.

Finally, the projection `(F,W)->F` is injective on the guarded slice. If
`F=0`, then `W` is divisible by the pairwise-coprime product `L_0L_1L_2`, of
degree `3ell-3`, while `deg W<=2ell-3`; hence `W=0`, and then both cofactors
vanish. The locator image therefore also has dimension `ell-1`. Subtracting
from `d+1=2ell-2` proves (GS6). QED.
