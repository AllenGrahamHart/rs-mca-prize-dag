# Proof

We first prove the elementary power-of-two balancing lemma. Let `zeta` be a
primitive `N=2^k` root in characteristic zero, and suppose a multiset of
`N`-th roots has zero sum. Its multiplicity polynomial can be written

```text
P(X)=sum_(e=0)^(N-1) m_e X^e in Z_{>=0}[X],       P(zeta)=0. (1)
```

The minimal polynomial of `zeta` is

```text
Phi_N(X)=X^(N/2)+1.                                   (2)
```

Because `deg P<N`, monic division in `Z[X]` gives

```text
P=(X^(N/2)+1)Q,       deg Q<N/2.                      (3)
```

Comparing the lower and upper halves of the coefficient vector gives

```text
m_e=m_(e+N/2),       0<=e<N/2.                        (4)
```

Thus every root occurs with the same multiplicity as its antipode, and the
multiset partitions into antipodal pairs.

Scale the proposed harmonic quadruple by `a_0^(-1)` and write it as
`(1,x,y,w)`. Pairwise distinct squares mean no two of these four elements are
equal or antipodal. Clearing `cr(1,x;y,w)=-1` gives the eight-term sum

```text
x+x+yw+yw-y-xy-w-xw=0.                                (5)
```

Regard the minus signs as multiplication by the `N`-th root `-1`. In the
multiset in `(5)`, the two copies of `x` need two copies of `-x`. Distinct
squares rule out obtaining `-x` from `-w,-xy,-y,-xw`; the only possibility
is

```text
yw=-x.                                                (6)
```

After removing those two antipodal pairs, the four roots

```text
w,xy,y,xw                                             (7)
```

must pair antipodally. There are only three pairings. Pairing `(w,xy)` and
`(y,xw)` forces `x^2=1`. Pairing `(w,y)` forces `w=-y`. Pairing `(w,xw)`
forces `x=-1`. Every alternative contradicts pairwise distinct squares.
This proves `(HTS1)`.

The factors in `(HTS3)` are nonzero exactly when the four normalized squares
are distinct. Introducing `u_i` with `u_if_i=1` therefore represents the
corresponding open locus without losing information over any field. The
equation `h=0` is precisely `(5)`, and the three torsion equations impose
membership in `mu_N`. The first part of the proof shows that `(HTS4)` has no
point over `Qbar`. Hilbert's Nullstellensatz makes it the unit ideal over
`Q`; clearing denominators proves `(HTS5)`. Reduction of the identity shows
that every supporting characteristic divides `Delta_H`.

Finally, each chain in `(HTS6)` is triangular and uniquely reconstructs
`z_t=z^(2^t)`. Its last equation is therefore equivalent to `z^(2^40)=1`.
There are three base variables, `3*39` power variables, and six inverse
variables, for `126` variables. The three chains contribute `3*40`
equations; adding `h` and the six inverse equations gives `127`. The power
and harmonic equations have degree at most two, while `u_if_i-1` has degree
three. Triangular elimination proves the stated scheme isomorphism. QED.
