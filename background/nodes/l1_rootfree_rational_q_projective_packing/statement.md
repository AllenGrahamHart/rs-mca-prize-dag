# L1 root-free rational-Q projective packing

- **status:** PROVED
- **role:** identify the residual boundary cell with Conjecture-F and pay its
  bounded residual-dimension range
- **consumer:** `l1_mixed_petal_amplification`

## Projective cell

Use the planted-root descent with `r<k`, and put

```text
n'=n-r,       j=m-r,       d=k-r,       j-d=w,
G=Wbar_1 P_S-Nbar_1,
V=span(G, W_1 F[X]_<d) <= F[X]_<=j.                 (PC1)
```

If the exact boundary cell is nonempty, then:

1. `dim V=d+1` and `V` has no common root on `H'=H\roots(D)`;
2. the exact cell is in bijection with the full projective split-locator
   intersection

   ```text
   P(V) intersect Dloc_j(H');                         (PC2)
   ```

3. the hyperplane at infinity `P(W_1 F[X]_<d)` contains no point of
   `Dloc_j(H')`.

Thus the residual is exactly a gcd-trivial codimension-`w` Conjecture-F cell,
not merely an injection into one.

## Packing payment

Distinct locators in `(PC2)` have root-set intersection at most `d-1`.
Consequently

```text
|P(V) intersect Dloc_j(H')|
    <= floor( binom(n',d) / binom(j,d) ).             (PC3)
```

For `d=1` this is `floor((n-r)/(m-r))`; for every fixed `d` it is polynomial
in `n`.  More generally, if `j>=alpha n'` and `d<=alpha n'/2`, then

```text
binom(n',d)/binom(j,d) <= (2/alpha)^d.                (PC4)
```

Thus `d=o(n')` costs `exp(o(n'))`, and under an agreement reserve `R` it is
absorbable whenever `d=o(R log |B|)`.  Together with the rigid `r>=k`
branch, this pays the fixed-dimensional range and the sublinear-dimensional
range at the corresponding asymptotic scale.

## Scope

`(PC3)` is an anticode/packing ceiling, not row-sharp Q flatness.  It can be
exponential when `d=Theta(n)`, and it is not normalized by the
base-field average.  No quotient coalescing, smooth-puncture inheritance, or
finite adjacent reserve fit is proved.
