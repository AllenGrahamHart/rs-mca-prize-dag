# Proof

Multiplying a putative relation in `(F4G4)` by `P` gives

```text
sum_i lambda_i H_i(Y)Q_i(X)=0.                           (1)
```

The elements `1,X,X^2,X^3` are a basis of `F(X)` over `F(Y)`. Splitting
`(1)` into residue classes modulo four therefore gives

```text
M(Y)(lambda_i H_i(Y))_i=0.                              (2)
```

If `rank M=4`, equation `(2)` is impossible. Suppose `rank M=3`. Every
`Q_i` has degree at most six in the three profiles under consideration, so
every entry of `M` has degree at most one in `Y`. A primitive polynomial
generator `K=(K_i)` for the one-dimensional kernel can be obtained from
`3 x 3` cofactors. Hence

```text
deg K_i<=3.                                             (3)
```

The polynomial kernel of a rank-three matrix over the PID `F[Y]` is generated
by `K`, after removing the common divisor of its entries. Thus `(2)` gives

```text
(lambda_i H_i)_i=G(Y)(K_i)_i                            (4)
```

for one polynomial `G`. All entries on the left are nonzero and have degree
`s`, so `(3)` implies

```text
deg G>=s-3.                                             (5)
```

For every pair `i!=j`, the polynomial `G(X^4)` divides both
`H_i(X^4)=P_iA_i` and `H_j(X^4)=P_jA_j`. Therefore

```text
deg gcd(A_i,A_j)>=4 deg G-ell_i-ell_j.                 (6)
```

Here `ell_i+ell_j<=4`. For `s>=5`, `(5)` makes the right side positive,
contradicting pairwise coprimality of the locators. This proves `(F4G4)`.

It remains to bound the residue rank in the two non-`K_4` profiles. In each
case select three denominators whose total degree is four: degrees `(2,1,1)`
for linear `K_4-e`, and `(2,1,1)` for triangle-plus-singleton. Remove the
fourth denominator, which multiplies all three selected columns by the same
nonzero element of `F(X)` and does not alter their `F(Y)`-rank. The selected
columns are then the three polynomials

```text
product_(j!=i) P_j
```

of degree at most three. A relation over `F(Y)` is therefore an ordinary
polynomial relation in the basis `1,X,X^2,X^3`. Evaluating that polynomial
identity at either root of `P_i` kills the other two terms and forces the
`i`th coefficient to vanish. Pairwise coprimality makes the surviving value
nonzero. Repeating for the three indices proves independence, so `rank M>=3`.
Together with `(F4G4)`, this excludes both profiles.

In the `K_4` profile, two columns cannot be proportional over `F(Y)`. Indeed,
their ratio is `P_j/P_i`, a nonconstant rational map of degree two because
the monic quadratics are coprime. A nonconstant element of `F(X^4)` has
rational-map degree divisible by four. Hence `rank M>=2`. The only remaining
case is exactly `(F4G6)`. Finally, the displayed antipodal family lies in the
two-dimensional space `<1,X^2>_(F(Y))`, proving that the rank-two locus is
not empty. QED.
