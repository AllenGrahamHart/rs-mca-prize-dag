# E1 N=512 four-singleton collision exclusion

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let `zeta` be a primitive `512`-th root of unity. In the first surviving
`N=512,s=2` E1 band, consider the folded profile

```text
(a,b,c)=(0,4,0).
```

Its characteristic-zero difference has the form

```text
alpha=F(zeta),       F(X)=sum_(i in I) epsilon_i X^i,
|I|=4,               epsilon_i in {+1,-1},
I subset {0,...,255}.
```

For the 256 odd conjugates put `y_u=|F(zeta^u)|^2`. Define the canonical
negacyclic autocorrelation by

```text
F(X)F(X^-1)-4 = sum_(d=0)^255 A_d X^d mod (X^256+1),
V=sum_d A_d^2.
```

Then `V` is an even nonnegative integer and the geometric mean `G` of the
`y_u` satisfies the following exhaustive alternatives:

```text
V=0:    |Norm(alpha)|=2^256;
V=2:    G<19/5;
V>=4:   G<180/47.
```

In the last two cases

```text
|Norm(alpha)|=G^128<2^250.
```

Every pair-feasible row prime is odd and at least `2^250`. Therefore no such
prime divides `Norm(alpha)`, including in the `V=0` case, where the norm is a
pure power of two. By the collision-norm criterion, profile `(0,4,0)` cannot
produce a finite-field E1 collision at any named pair-feasible anchor.

Consequently the only profile still unresolved in the first `N=512,s=2`
band is `(1,2,0)`. This theorem does not exclude that profile, control any
higher band, or pay the total collision-pair allowance.
