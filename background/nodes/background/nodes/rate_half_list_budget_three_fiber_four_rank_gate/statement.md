# Budget-three fiber-four residue-rank gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_multideletion_multifiber_exclusion`

Let `F` have odd characteristic and put `Y=X^4`. For `i=0,1,2,3`, let
`P_i in F[X]` be pairwise coprime monic polynomials with degrees `ell_i`, and
assume, up to permutation, that

```text
(ell_i) in {(2,2,1,1),(1,1,1,2),(2,2,2,2)}.             (F4G0)
```

Put

```text
P=product_i P_i,        Q_i=P/P_i.                         (F4G1)
```

Write the four residue classes of `Q_i` as

```text
Q_i(X)=sum_(r=0)^3 X^r M_ri(Y),
M(Y)=(M_ri(Y))_(0<=r,i<=3).                               (F4G2)
```

Suppose `H_i(Y)` are monic of one common degree `s>=5`, each
`P_i(X)` divides `H_i(X^4)`, and the four locators

```text
A_i(X)=H_i(X^4)/P_i(X)                                   (F4G3)
```

are pairwise coprime. If all four coefficients `lambda_i in F` are nonzero,
then

```text
sum_i lambda_i A_i=0   implies   rank_(F(Y)) M<=2.        (F4G4)
```

For the profiles

```text
linear K_4-e:             (ell_i)=(2,2,1,1),
triangle plus singleton:  (ell_i)=(1,1,1,2),              (F4G5)
```

the matrix `M` always has rank at least three. Hence no relation `(F4G4)`
exists in either profile.

For the linear `K_4` profile `(2,2,2,2)`, `rank M>=2`. Thus a fiber-four
construction can survive this gate only on the exact rank-two reciprocal
locus

```text
dim_(F(X^4)) span {1/P_0,1/P_1,1/P_2,1/P_3}=2.           (F4G6)
```

This locus is nonempty: if `P_i=X^2-a_i` are pairwise coprime, then

```text
1/(X^2-a_i)=(X^2+a_i)/(Y-a_i^2)
```

lies in `<1,X^2>_(F(Y))`. This example establishes only that the algebraic
rank-two gate is real; it does not construct pairwise-coprime official block
locators satisfying the required relation.

At the prize maximum, `s=d/4=2^37`. Consequently the direct one-map
equal-complete-fiber residual at `m=4` is eliminated in the linear `K_4-e`
and triangle-plus-singleton chambers and reduced to `(F4G6)` in the linear
`K_4` chamber.
