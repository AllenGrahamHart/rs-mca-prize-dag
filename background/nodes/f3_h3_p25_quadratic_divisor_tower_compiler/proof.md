# Proof

Suppose first that `t!=0,1` and `P(t)>=q`. The ordered product
representations have distinct first coordinates `x`: once `x` is fixed, the
second coordinate is `t/x`. Choose any `q` first coordinates and let `Q` be
their monic product. Every selected `x` is nonzero, so `X` has an inverse
`Z` modulo `Q`.

For every root `x` of `Q`, both

```text
1-x in H,       1-t/x=(x-t)/x in H.
```

Since `H` has order `2^s`, repeated squaring gives `(QDT2)--(QDT3)`. Monic
division by `Q` supplies unique quotient polynomials, and the two scalar
inverses exist because `t!=0,1`. Thus the system has a solution.

Conversely, let the system have a geometric solution. Equations `(QDT1)`
make `X`, `T`, and `T-1` invertible in the quotient by `Q`. The terminal
tower equations give

```text
(1-X)^n=1 mod Q,
((X-T)/X)^n=1 mod Q.                               (1)
```

The first polynomial in `(1)` is squarefree because `p` does not divide
`n`; hence its monic divisor `Q` is squarefree. It also splits over `F_p`,
because every `n`th root of unity lies there. For each of the `q` distinct
roots `x` of `Q`, equation `(1)` gives two members

```text
x in (1-H)\{0},       T/x in (1-H)\{0}.
```

The second equality follows from `(X-T)/X=1-T/X`. Thus every root gives a
distinct ordered representation of `T`, so `P(T)>=q`. Although the solution
was initially geometric, any one root has `x in F_p` and its second torsion
value lies in `F_p`; therefore `T=x(1-B_0(x)) in F_p`. The selectors make it
nonzero and nonidentity. This proves the equivalence.

For the count, the variables are:

```text
q coefficients of Q, q of Z, and T,tau,eta;
(s-1)q internal A residues and sq B residues;
two scalar congruence quotients;
2s(q-1) squaring quotients.
```

Their sum is `(4s+1)q+5-2s`. The inverse and initialization congruences each
give `q+1` coefficient equations, the two scalar inverses give two, and the
`2s` squaring congruences each give `2q-1`. Their sum is
`(4s+2)q+4-2s`. Every term is a product of at most two variables.

In characteristic zero, `(1)` would give `q=25` distinct ordered
representations of one shifted product. Shifted-product Sidonicity allows at
most two, so the system is empty. Clearing denominators in a unit-ideal
certificate therefore gives the stated characteristic outer set. QED.
