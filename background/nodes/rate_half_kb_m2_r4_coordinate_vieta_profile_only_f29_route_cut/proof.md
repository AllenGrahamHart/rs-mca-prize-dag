# Proof

Write negation modulo 29 as the deck involution. The certificate prints five
`J-J` edge orbits over `K`, one `I-I` orbit over `xi`, and six paired records
over `J=L^c`. Direct deck transport gives 24 star slots. Counting their
categories gives `(10,10,4)`; every one of the twelve labels has degree four.
Exactly the two edges in each of the repeated `{3,5}|{-3,-5}` records occur
twice, so

```text
sum_e binom(m_e,2)=2.                              (1)
```

The six right records give a diagonal-free two-regular pole graph. Their
omitted labels exhaust `I`; the four mixed stars occur at the two right
vertices whose neighbors are the bar-pair `{2,-2}`. Hence all facet,
transport, color, and defect conditions are simultaneous.

For a printed edge `{a,b}` above `kappa`, choose the printed square root `r`
and put `p=ab`, `q=r(a+b)`. The five records are

```text
kappa:   1   -1    4   -4    9
p:      15    6   15   14   10
q:       8    2   16   10   21.                  (2)
```

Evaluation of the three coefficient forms gives

```text
A_2:    15   26   22    8   19,
A_0:    22   11   11   25   16,
B_1:    25   23   28   20    4.
```

Every leading value is nonzero, and direct substitution proves

```text
A_0(kappa)=p A_2(kappa),
kappa B_1(kappa)=-q A_2(kappa).                   (3)
```

Thus the displayed coefficient vector is a nonzero kernel vector. The
upper-left `7 x 7` minor on matrix rows and columns `0,...,6` is `28`, so the
rank is exactly seven.

The coefficients of `H` as a quadratic in `T` are primitive. Its
discriminant is

```text
Delta(X)=D(X^2),
D(W)=16W^4+19W^3+8W^2+6W+10.
```

The constant term is nonzero and `gcd(D,D')=1`. Over an algebraic closure,
`D(X^2)` therefore has simple nonzero roots and is not a square. Gauss's
lemma and the quadratic discriminant criterion prove that `H` is
geometrically irreducible.

Finally multiply

```text
Phi_+(y,W)=(yA_2+A_0)^2-WyB_1^2
```

over `y=2^2,3^2,5^2`. Exact polynomial division gives

```text
R_J/K_5^2=W^2+22W+9=(W-13)(W-23).                (4)
```

The six `J` labels are `2,27,3,26,5,24`, so neither forced root is allowed.
More precisely, the four mixed stars occur at right vertices `3,26`, so the
source-facet coloring prescribes `c_col=(W-3)(W-26)=W^2+20`, visibly different
from `(4)`. Moreover at `W=xi=20`, the left side of the cleared companion
identity is `c_0(20)R_I(20)=8`, whereas `R_7(20)^2=0`. Thus both the colored
support and the second quotient identity reject the witness. QED.
