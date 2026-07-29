# Proof - L1 Mersenne HNF m=8 order-one quadratic two-pair univariate reduction

The quadratic-collision router gives

```text
r(18+d-d^2)+192=0.                                  (1)
```

If `D=18+d-d^2` vanished, (1) would give `192=0`, impossible in every
official characteristic. This proves (QUR2).

In terms of `d` and `r`, the `h=7` residual conic equation before completing
the square is

```text
35r^2d^2+14(11d^2+27d+27)rd
 +120(d^4+4d^3+7d^2+6d+3)=0.                        (2)
```

Substitute `r=-192/D` and multiply by `D^2/24`. Equation (2) becomes

```text
5(d^4+4d^3+7d^2+6d+3)D^2
 -112(11d^2+27d+27)dD+53760d^2=0.                  (3)
```

Direct expansion of (3) is exactly the polynomial in (QUR3).

Every actual survivor also has

```text
d^(p+1)=zeta,       zeta^8=1.                       (4)
```

Therefore its `d` is a common root of the two polynomials in (QUR4). A unit
gcd for each of the eight colors excludes every possible `d` on that row.
Conversely, a common root has passed only the conic, collision, and outer
torsion equations used here, so no sufficiency statement follows. QED.
