# Proof - L1 Mersenne HNF m=8 order-one cubic three-color remainder router

Let the three colors used by a packet be `alpha,beta,gamma`. At every root
`x` of the squarefree polynomial `L`, one has

```text
(E(x)-alpha)(E(x)-beta)(E(x)-gamma)=0.               (1)
```

Consequently

```text
L(W) divides (E(W)-alpha)(E(W)-beta)(E(W)-gamma).    (2)
```

This is exactly the six-coefficient remainder equation in (TCR4). Each
color is used, so each corresponding fiber has a common root with `L`; this
is exactly the three resultant equations. Conversely, these equations are
only used as necessary conditions, so no assignment or outer converse is
being inferred from them.

A cubic fiber contains at most three distinct roots. The six roots therefore
cannot use one color. If they use two, both multiplicities must be three,
which the first dependency excludes. With exactly three nonempty fibers,
the only partitions of six with parts at most three are

```text
3+2+1,       2+2+2.                                  (3)
```

Their ordered multiplicities are read exactly from
`deg gcd(L,E-alpha)`, `deg gcd(L,E-beta)`, and `deg gcd(L,E-gamma)`.
Standard subresultant vanishing plus the next nonvanishing subresultant
therefore gives the stated saturated profile split.

It remains to prove the seven-orbit claim. Identify `mu_8` with `Z/8Z` by
`j -> omega^j`. Translating a three-subset corresponds to multiplying all
colors by one eighth root. If `E` solves (2) for a set `T`, then `omega^a E`
solves it for `T+a`, since

```text
Q_(T+a)(omega^a E)=omega^(3a)Q_T(E).                 (4)
```

No nonzero translation stabilizes a three-subset: its translation orbits
have sizes dividing eight, and no union of such nontrivial orbits has size
three. Thus every orbit has size eight and the 56 three-subsets form seven
orbits. Writing the three positive cyclic gaps, whose sum is eight, gives
the seven necklaces

```text
(1,1,6), (1,2,5), (1,5,2), (1,3,4),
(1,4,3), (2,2,4), (2,3,3),                           (5)
```

which yield exactly the representatives in (TCR1).

Finally the h=7 conic and norm-color equation are inherited necessary
conditions. All polynomial degrees in (TCR4), including the degree-nine
composition before reduction, are fixed independently of `p`. Hence the
seven systems and the two subresultant profiles are bounded exact closure
packets. QED.
