# Proof - L1 bounded-mark affine split-pencil compiler

## 1. Affine syndrome fibers

Take two monic pairs `(F,W),(F',W') in X_S` with the same missing-equation
syndrome. Their difference `(G,B)=(F-F',W-W')` has

```text
deg G<=d-1,       deg B<=d.                              (1)
```

It satisfies the fixed partial equations on every `S_i`; equality of the
syndromes supplies the missing equations on every `V_i`. Hence it satisfies
the full equations on every `T_i` and lies in `H_T^0`. Conversely, adding an
element of `H_T^0` to one monic representative preserves monicity, every
partial equation, and every missing-equation syndrome. This proves `(AC4)`.

The syndrome target has `v` coordinates over `F_q`, so it has `q^v` values.
Only values in the image can give nonempty fibers, proving the first claim.
Additional fixed equations cause no change: their homogeneous differences
are simply included in `H_T^0`.

## 2. One-direction homogenization

Every first component in `H_T^0` has zero `X^d` coefficient, while the first
component of `z_y` is monic of degree `d`. Therefore

```text
K z_y intersect H_T^0={0}.                               (2)
```

This gives `dim Hhat_y=dim H_T^0+1`. In a vector
`lambda z_y+h`, the leading coefficient of the first component is exactly
`lambda`. It is monic exactly when `lambda=1`, so the monic hyperplane is
`z_y+H_T^0`. This proves `(AC5)` and the projective-extension claim.

Exact split-locator, root-location, squarefreeness, saturation, and absence
of extra agreements only restrict the monic points in this hyperplane. The
affine decomposition therefore remains valid after all actual-codeword
guards are imposed.

## 3. Bounded-basepoint split pencil

For an actual L1 pair, the equations on `S_i` and polynomial divisibility
give

```text
W-c_iF=L_(S_i)A_i,       deg A_i<=d-|S_i|=d-ell+|V_i|.  (3)
```

The petals are disjoint, so their mark locators are pairwise coprime and
`J_i=J/L_(V_i)` is a polynomial. Multiplying `(3)` by `J` gives

```text
J(W-c_iF)
 =L_(S_i)L_(V_i)J_iA_i
 =L_(T_i)C_i.                                           (4)
```

Moreover,

```text
deg C_i
 <=(v-|V_i|)+(d-ell+|V_i|)
 =d-ell+v.                                              (5)
```

Exact defect gives `gcd(F,W)=1`. The monic gcd identity in `K[X]` therefore
gives

```text
gcd(JF,JW)=J gcd(F,W)=J,                                (6)
```

which proves `(AC7)`. Notice that no common constant-shift representation
of the arbitrary locators `L_(T_i)` was used.

## 4. L1 counting pre-factor

Orient a petal as dense when its support has more than `ell/2` points, with
ties sparse. Relative to the full baseline on a dense petal and the empty
baseline on a sparse petal, the symmetric-difference exception count is
exactly

```text
p=sum_i min(|S_i|,ell-|S_i|).                           (7)
```

There are at most `2^M` orientation vectors and at most
`sum_(e=0)^P binom(Mell,e)` exception sets when `p<=P`, proving `(AC8)`.
The omitted points on dense petals are a subset of those exceptions, so
`v<=p<=P`; Section 1 contributes at most `q^P` syndromes. Sparse-petal
equations can remain among the fixed equations, while background agreements
are determined by the reconstructed pair and add no support choice.

Finally, `(AC9)` gives

```text
2^M<=n^(1/c_0),       q^P<=n^(gamma P),
sum_(e=0)^P binom(Mell,e)<=(P+1)n^P.                   (8)
```

Multiplying proves `(AC10)`. Each monic pair reconstructs at most one L1
listed codeword by the exact core-defect normal form. There are at most `n`
possible defect degrees. Thus a uniform `n^B` cell bound and an `n^A`
canonical first-match chart bound multiply by only the displayed factors,
giving `(AC11)` and proving the final reduction.
