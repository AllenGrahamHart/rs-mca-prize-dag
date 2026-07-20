# Proof

Fix an orbit and put `m=min(v_2(u),v_2(v))`. Division by `2^m` identifies
the orbit with odd-unit dilation on a pair `(a,b)` modulo
`L=2^(s-m)`, where at least one coordinate is odd. The reduction map from
the odd units modulo `n` onto the odd units modulo `L` is surjective.

If `a` is odd, scale uniquely by `a^(-1)` to obtain `(1,w)`. The parameter
`w` is odd and different from one when `b` is odd, and is nonzero even when
`b` is even. If `a` is even, then `b` is odd and unique scaling by `b^(-1)`
gives `(w,1)` with `w` nonzero even. These cases are disjoint, and the
normalizing unit is forced in each case. Restoring the common factor `2^m`
proves existence and uniqueness in `(QRM2)`. Each parameter set has
`L/2-1=2^j-1` elements, recovering the proved degree histogram.

Let `zeta_L=zeta_n^(2^m)`. At the first two representative families the
quotient root is

```text
(1-zeta_L^w)/(1-zeta_L)=S_w(zeta_L).                (1)
```

The conjugates of `(1)` are obtained by replacing `zeta_L` by every
primitive `L`-th root. The quotient Sidonicity used by the orbit
decomposition proves that these `d=phi(L)` values are distinct. Since
`Phi_L(Z)=Z^d+1`, the defining product formula for the resultant gives

```text
Res_Z(Phi_L(Z),T-S_w(Z))
 =product_(r mod L odd)(T-S_w(zeta_L^r)).            (2)
```

Equation `(2)` is monic of degree `d` and is precisely the full Galois-orbit
polynomial, proving `(QRM3)` and its irreducibility.

It remains to normalize the reverse family. Write `a=v_2(w)`. The cyclotomic
norm of `1-zeta_L` is two. If `a=0`, multiplication by `w` permutes the
primitive `L`-th roots and hence

```text
Norm(S_w(zeta_L))=1.                                (3)
```

If `a>=1`, then `zeta_L^w` is a primitive `L/2^a`-th root. The norm of
`1-zeta_L^w` from `Q(zeta_L)` to `Q` is

```text
2^[Q(zeta_L):Q(zeta_(L/2^a))]=2^(2^a).              (4)
```

Formula `(4)` also covers `L/2^a=2`, where the smaller cyclotomic field is
`Q`. Dividing by `Norm(1-zeta_L)=2` proves `(QRM4)`.

At a reverse representative the quotient root is `S_w(zeta_L)^(-1)`.
Therefore

```text
Res_Z(Phi_L,S_wT-1)
 =product_r(S_w(zeta_L^r)T-1)
 =T^d q_(j,+,w)(T^(-1)).                            (5)
```

Here `d` is even, so no sign occurs. The leading coefficient in `(5)` is
the norm `(QRM4)`. Division by this power of two produces the monic full
Galois-orbit polynomial over `Z[1/2]`, proving `(QRM5)`. Multiplying the
polynomials for the unique representatives in `(QRM2)` partitions every
quotient root exactly once, which proves `(QRM6)`. QED.
