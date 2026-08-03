# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 3 is

```text
(de,-de), (de,sigma_o ef), (bf,sigma_c cf).
```

Let `A_i,B_i` be the three source-pencil coefficient pairs, and let
`F(x,y)=paired(x,y)`. Direct expansion proves that `F` is symmetric and has
the nine-term form

```text
F(x,y) = a x^2 y^2 + b(x^2 y+x y^2) + c(x^2+y^2)
         + d x y + e(x+y) + f_0.
```

In particular,

```text
F(q,-q) = 4(C_4 q^4 + C_2 q^2 + C_0),
C_4 = A_0 A_1^2 A_2,
C_2 = A_0^2 B_2^2 - A_0 A_1 B_1 B_2
      - 2 A_0 A_2 B_0 B_2 - A_1 A_2 B_0 B_1 + A_2^2 B_0^2,
C_0 = B_0 B_1^2 B_2.
```

Thus the first paired equation is a quadratic `Q(x)=0` in `x=q^2`.

Let `m=df`, `s=(d+f)^2`, and `y=1/d^2`. Then

```text
1 + (2m-s)y + m^2 y^2 = 0,
ef = q m y.
```

The second paired equation is the quadratic
`F(q,sigma_o q m y)=0`. The division-free resultant identity for two
quadratics produces a polynomial `T(q)` over the six-dimensional source
algebra. Reduce it exactly modulo `F(q,-q)` to
`R(q)=E(x)+q O(x)` with degree at most three in `q`. Any common `q` obeys

```text
E(x)^2 - x O(x)^2 = R(q)R(-q) = 0.
```

Reduce this cubic parity condition modulo the quadratic `Q(x)`. Every census
row leaves a linear remainder `r_0+r_1 x`; the division-free
quadratic-linear resultant gives the final source cut. The one inverse of
the leading coefficient is cached, and its numerator and denominator are
retained in the exceptional-root ledger. The direct norm in the basis
`1,t,t^2,b,bt,bt^2` agrees exactly with the quadratic-over-cubic tower norm.

Every deployed-field root of the norm numerator and denominator, every
inverse-guard numerator and denominator, and the base-cubic leading
coefficient is lifted through the base cubic, the `b` quadratic, linear `c`
recovery, product-rank cofactors, and compact kernel. At each source point,
all roots of `F(q,-q)` are enumerated. For each one, the exact roots of the
two `y` quadratics are intersected; every field root of `d^2=1/y` is then
lifted, with `e=q/d` and `f=m/d`.

Across eight rows there are 108 candidate `r` values, 184 source points, 480
enumerated `q` rows, 192 reconstructed targets, and 384 final evaluations of
`F(bf,sigma_c cf)`. Every final value is nonzero. The witness, boundary, and
unresolved ledgers are empty. This proves all 16 raw matching-3 cases empty.

The transposition of residual positions zero and one exchanges two records
that are both exactly `de`. It maps canonical matching 3 to matching 6.
Because `F` is symmetric, the three equations, missing-product relation,
missing-sum relation, and target guards are preserved value-for-value. Hence
the 16 matching-3 exclusions transport to all 16 matching-6 cases. All 32
stated cases are empty. QED.
