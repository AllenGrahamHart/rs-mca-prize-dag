# Proof: rate-half FPC5 joint support distance

Let `(A_1,A_2)` and `(A'_1,A'_2)` be two exact cofactor pairs and put

```text
Delta=A_1A'_2-A'_1A_2.                               (1)
```

At a point `x in D intersect D'`, both defect locators vanish. The cofactor
formula for `F` gives

```text
L_1(x)A_1(x)=L_2(x)A_2(x),
L_1(x)A'_1(x)=L_2(x)A'_2(x).
```

The core and petals are disjoint, so both petal locators are nonzero at `x`.
Cross multiplication gives `Delta(x)=0`.

At a point `y in R intersect R'`, both reconstructed numerators vanish. The
guarded numerator formula gives

```text
c_2L_1(y)A_1(y)=c_1L_2(y)A_2(y),
c_2L_1(y)A'_1(y)=c_1L_2(y)A'_2(y).
```

Again all displayed scalar and locator factors are nonzero on the background,
so `Delta(y)=0`. The two root sets lie in disjoint source blocks, hence these
are `|D intersect D'|+|R intersect R'|` distinct roots of `Delta`.

Exact core defect gives `gcd(F,W)=1`. Since `F` is split on the core and
disjoint from the touched petals, the proved two-petal normal form makes this
equivalent to

```text
gcd(A_1,A_2)=gcd(A'_1,A'_2)=1.                       (2)
```

If `Delta=0`, unique factorization and (2) make the two cofactor pairs scalar
multiples: from `A_1A'_2=A'_1A_2`, coprimality forces one primitive pair to
divide the other coordinatewise, and the remaining common multiplier must be
a unit. Their locator images are then scalar multiples. Both locators are
monic, so the scalar is one and the contributors coincide. For distinct
contributors, `Delta` is therefore nonzero. Since `deg Delta<=2s`, its number
of distinct roots is at most `2s`, proving (JD1).

Now set `S=D union R`. The blocks `C,B` are disjoint, `|D|=ell+s`, and the
list threshold gives `|R|>=s`, proving (JD2). Every `(2s+1)`-subset of
`C union B` belongs to at most one combined support, by (JD1). Counting pairs
consisting of a contributor and one such subset of its combined support gives

```text
L_(s,pair) binom(ell+2s,2s+1)
 <= binom(k-1+b,2s+1).
```

Taking the integer floor proves (JD3). QED.
