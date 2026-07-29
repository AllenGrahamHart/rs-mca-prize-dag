# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one Galois-role weld

Fix a primitive eighth root `zeta`. After normalizing the first color to
one, every ordered role is

```text
lambda_(a,b)=(zeta^b-1)/(zeta^a-1),
a,b in {1,...,7},       a!=b.                       (1)
```

The Galois group of `Q(zeta)/Q` is the unit group
`{1,3,5,7}` modulo eight and sends `(a,b)` to `(ka,kb)`. The six ordered
pairs with both entries in `{2,4,6}` split into three orbits of size two,
represented by `(2,6),(2,4),(4,2)`. Their role values are respectively

```text
{i,-i},       {1+i,1-i},       {(1+i)/2,(1-i)/2},   (2)
```

which gives `P_1,P_2,P_3`.

Every other ordered pair has orbit size four. The nine representatives are
exactly (GRW3): three odd--odd orbits, two odd--even orbits in each
orientation, and one orbit in each orientation between an odd exponent and
four. Direct reduction modulo `zeta^4+1` gives their orbit polynomials
`P_4,...,P_12`. For example,

```text
lambda_(1,2)=1+zeta
```

gives `(X-1)^4+1=P_4`, while

```text
lambda_(2,1)=1/(1+zeta)
```

gives `(1-X)^4+X^4=P_10`. The remaining seven reductions give the printed
quartics.

The orbit sizes sum to

```text
3*2+9*4=42.                                         (3)
```

Thus (GRW2) enumerates exactly the same ordered normalized color pairs, with
the same multiplicities, as the resultant proof of `Lambda_321`. Both
polynomials have degree 42, so they differ by a nonzero rational scalar.

Finally (TRW2) gives `lambda=1+R/S`. Multiplying a degree-`e_j` packet by
`S^e_j` proves (GRW4), and clearing is reversible because `S!=0`. Taking
the union of the twelve packet zero loci is therefore equivalent to the
zero locus of the full role polynomial, hence to the union of the four
factor-weld zero loci (TRW4). QED.
