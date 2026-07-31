# Proof

The coordinate source-facet theorem partitions the 24 complete-source
points into five deck-paired fibers over `K`, one over `eta`, and six over
`L^c`.  Deck transport sends

```text
(x,a,b) -> (-x,-a,-b).
```

It preserves both values in `(KBCV-1)`, proving that the twelve records are
well defined.

For positive parity write

```text
H(T,X)=A_2(W)T^2+A_0(W)+XT B_1(W).
```

At `X=x_kappa`, Vieta's formulas for the prescribed roots `a_kappa` and
`b_kappa` give

```text
A_0(kappa)=p_kappa A_2(kappa),
x_kappa B_1(kappa)=-(a_kappa+b_kappa)A_2(kappa).
```

Multiplying the second equality by `x_kappa` and using `x_kappa^2=kappa`
gives `(KBCV-2+)`.  Conversely these equations and `A_2(kappa)!=0`
recover the prescribed two roots.  The deck-conjugate equation recovers the
other star in the orbit.

For negative parity write

```text
H(T,X)=T A_1(W)+X(B_2(W)T^2+B_0(W)).
```

Dividing by the nonzero leading coefficient `x_kappa B_2(kappa)` and using
Vieta gives `(KBCV-2-)`; the converse is identical.  The coefficient counts
from the coordinate normal form make these homogeneous systems `24 x 8`
and `24 x 7`.

The first equation in positive parity says that the two quadratic forms
`A_0,A_2` supply a kernel vector for the matrix with rows `M_+(kappa)`.
The vector is nonzero because `A_2` is nonzero on every source fiber.  Hence
the rank is at most five.  The negative argument uses the two linear forms
`B_0,B_2` and gives rank at most three.  Restriction of the positive matrix
to the six rows `K union {eta}` proves `(KBCV-5)`.

For negative parity, leading support makes `B_0/B_2` defined at all twelve
source labels.  If the ratio were constant, every edge would have one fixed
product `p`.  A nonzero label `a` then has the unique possible partner
`p/a`.  Since every source label has degree four, that edge has weight at
least four and contributes at least `binom(4,2)=6`, contradicting the proved
defect budget three.  Thus `B_0/B_2` is a nonconstant projective linear map,
so it is injective.  Distinct source labels consequently have distinct edge
products.

On the three deck pairs of `J`, let `l_i` count antipodal edge orbits and
`m_ij` count cross-pair orbits.  The two profiles give the degree equations

```text
2l_i + sum_(j!=i) m_ij = d_i,       sum l_i+sum m_ij=5,
```

for `d=(4,4,2)` or `(4,3,3)`.  Solving these nonnegative integer equations
up to the swap of equal-degree vertices gives seven solutions for each
profile.  Injectivity permits at most one loop of each type and at most the
two products `+a_i a_j,-a_i a_j` on a cross pair.  Imposing
`l_i<=1,m_ij<=2` leaves precisely the seven tuples in `(KBCV-6)`.

The converse parts above show that a complete-system survivor has exactly
the prescribed 24 stars.  Multiplying their row divisors gives the
complete-source square.  Splitting that divisor into its `I` and `J`
incidences gives the two colored quotient identities from the existing
colored-resultant compiler.  Thus those identities are automatic on a
complete exact packet, while still furnishing an independent replay.

For the recorded `F_29` packet, the products on `K union {eta}` are

```text
(15,6,15,14,10,4)
```

at quotient labels `(1,-1,4,-4,9,-9)`.  Exact elimination gives rank five
on the first five rows and determinant `10` on all six rows.  The packet is
therefore rejected by `(KBCV-5)`.

For the second `F_29` claim, substitute `(A,B,C,D,E,F)=(1,4,6,9,7,5)`
into the defect-zero fixture's twelve edge products.  Row reduction gives

```text
rank M_+(K union {eta})=5,       rank M_+(Omega)=6.
```

The displayed kernel and its six denominator evaluations verify full
leading support on the separator.  Finally, the seven signed square-pairs
in `F_29` are represented by `1,4,5,6,7,9,13`.  Deterministic enumeration
of their 5,040 ordered six-subsets gives the exact counts 140 and zero.
The fixture's graph checks are label-independent, so every assignment keeps
its source-facet census and defect zero. QED.
