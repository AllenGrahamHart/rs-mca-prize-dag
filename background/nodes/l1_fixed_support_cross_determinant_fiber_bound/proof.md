# Proof - L1 fixed-support cross-determinant fiber bound

If `Z` is empty there is nothing to prove. Fix `(F_0,W_0) in Z`.

For every `(F,W) in Z`, both pairs satisfy the same labelled equations on
each `S_i`. Hence the cross determinant

```text
Delta=W_0F-WF_0                                        (1)
```

vanishes on the disjoint union of the selected supports. Their monic locators
are pairwise coprime, so

```text
S=product_i L_(S_i) | Delta.                           (2)
```

The degree bounds give `deg Delta<=2d`, while

```text
deg S=sum_i |S_i|=t ell-v.                             (3)
```

Thus the quotient in `(FB4)` has degree at most

```text
2d-(t ell-v)=r_cross.                                  (4)
```

Suppose two pairs `(F_1,W_1),(F_2,W_2)` have the same quotient. Subtracting
their cross-determinant identities gives

```text
W_0(F_1-F_2)=F_0(W_1-W_2).                             (5)
```

Since `gcd(F_0,W_0)=1`, equation `(5)` implies `F_0|(F_1-F_2)`. The two
locators are monic of degree `d`, so `deg(F_1-F_2)<=d-1`; therefore
`F_1=F_2`. Equation `(5)` then gives `W_1=W_2`. This proves injectivity.

If `r_cross>=0`, the target polynomial space has `q^(r_cross+1)` elements.
If `r_cross<0`, equations `(2)--(4)` force every `Delta` to vanish, and the
same injectivity argument gives `|Z|<=1`. This proves `(FB3)`.

For the aggregate, orient each of the `M` petals as sparse or dense and
record the at most `P` exceptional points. As in the affine compiler, the
number of exact support patterns is at most

```text
2^M(P+1)n^P.                                           (6)
```

The fixed-support theorem counts all missing-equation syndromes together, so
there is no additional `q^P` factor. On `(FB5)`, each pattern contributes at
most `q^(E+1)`. There are at most `n` defect degrees. Multiplying and using

```text
2^M<=n^(1/c_0),       q<=n^gamma                       (7)
```

gives `(FB6)`. If a per-chart family with fixed `p<=P` were
super-polynomial while `r_cross` stayed bounded, one fixed `E` would place it
inside `(FB6)`, a contradiction.
