# Proof

## (i) Factorisation and invertibility

With `N = 256L` and `omega` of exact order `2N = 512L`, every `0 <= y < N`
has the unique representation `y = a + 256b`, `0 <= a < 256`, `0 <= b < L`.
For row index `j`,

```text
omega^((2j+1)y) = omega^((2j+1)a) * (omega^256)^((2j+1)b).
```

Set `theta = omega^256`. Its order is
`512L / gcd(512L, 256) = 512L/256 = 2L` exactly (gcd is 256 because
`256 | 512L`). This is `(KBB-1)` with `D_a` and `F` as displayed.

The exponents `2j+1`, `j = 0..L-1`, are the odd residues modulo `2L`, so
`theta^(2j+1)` runs over the `L` roots of `X^L + 1`: each satisfies
`(theta^(2j+1))^L = theta^(2j+1)L = (theta^L)^(2j+1) = (-1)^(2j+1) = -1`
(`theta^L = -1` since `theta` has exact order `2L`), and they are pairwise
distinct because `theta` has exact order `2L` and the odd residues are
distinct mod `2L`. `F` is the Vandermonde matrix on these `L` distinct
nodes, so

```text
det F = prod_(i<j) (theta^(2j+1) - theta^(2i+1)) != 0.
```

Each `D_a` is diagonal with nonzero entries. Hence every
`A_a = D_a F` is invertible. QED (i).

## (ii) Parallelepipeds

`A_a` invertible restricts to an injection on `{0,1}^L`, so
`|S_a| = 2^L`, and `Y_a = A_a B_a` with `B_a` uniform on `{0,1}^L` is
uniform on `S_a`. Independence of the 256 blocks of Boolean input gives
the convolution form. QED (ii).

## (iii) Exact marginals

For `lambda` uniform on `F_q^L`, the map `lambda -> A_a^T lambda` is a
bijection of `F_q^L` (transpose of an invertible matrix), so
`C_a = A_a^T lambda` is uniform; the coordinates of a uniform vector on
`F_q^L` are independent uniform residues. QED (iii).

## (iv) Companion orbit

`D_a = D_1^a` entrywise, since the `(j,j)` entry is
`omega^((2j+1)a) = (omega^(2j+1))^a`. Hence

```text
C_a = A_a^T lambda = F^T D_a lambda = F^T D_1^a lambda
    = (F^T D_1 F^(-T))^a (F^T lambda) = M^a C_0,
```

using `F^T D_1^a F^(-T) = (F^T D_1 F^(-T))^a` (conjugation is a group
homomorphism). QED (iv).

The scope fences in the statement are exact: nothing above constrains the
joint distribution of `(C_0, ..., C_255)` beyond `(KBB-2)`, and no metric
property of `M` is asserted.
