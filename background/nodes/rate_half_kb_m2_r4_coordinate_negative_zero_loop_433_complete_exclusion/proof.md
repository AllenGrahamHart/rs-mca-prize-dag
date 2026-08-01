# Proof

The parent complete-Vieta router reduces the full 64-packet common atlas to
the four lanes `(KBZ433X-1)`.  Its product solvers are exhaustive: every
compatible multiplicative system is either an enumerated isolated exponent
triple or a rank-deficient binomial family.  Families already forcing a
target-square or product collision are not actual packets.

For an outside target edge `{u,v}`, the parent reconstructs the Mobius
product map and the global forms `A_1,B_2`.  If `p=uv`, its forced quotient
label and necessary squared-sum residual are

```text
kappa=(n_0-pd_0)/(pd_1-n_1),
R=A_1(kappa)^2-kappa(u+v)^2 B_2(kappa)^2.           (1)
```

Clearing the protected Mobius denominator gives a polynomial in
`F_p[D,E,F]`.  Every actual packet must make all seven such polynomials
zero.  Direct exact replay on every guarded isolated Smith assignment in
`(KBZ433X-1)` fails already at the first outside edge.

It remains only to justify the free systems without sampling.  There are
exactly

```text
12/Z2:  8 systems on each of 8 product rows =64;
12/Z3: 16 systems on each of 4 product rows =64;
13/Z2:  8 systems on each of 4 product rows =32;
14/Z2:  8 systems on each of 4 product rows =32.  (2)
```

Each product row has two common q records.  Thus `(2)` gives 384 exact
family/common-record ideals.  For every ideal, append the cleared residuals
from `(1)` in outside-edge order and compute a Groebner basis over `F_p`.
The basis becomes `[1]` at row 0 for all `12/Z2` routes, row 1 for all
`12/Z3` routes, and row 2 for all `13/Z2` and `14/Z2` routes.  This is
exactly `(KBZ433X-2)`.

A unit ideal has no point over the algebraic closure, so none of these
families has a deployed-extension point.  This removes every residual route
in `(KBZ433X-1)`.  The parent already removed every other common cell and
product type, proving the complete exclusion. QED.
