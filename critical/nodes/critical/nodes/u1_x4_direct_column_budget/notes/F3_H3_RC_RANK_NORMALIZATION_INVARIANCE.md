# F3 h=3 RC-RANK normalization invariance

Status: PROVED ALGEBRAIC NORMALIZATION LEMMA + FINITE-FIELD REPLAY.

This packet records harmless normalizations for the h=3 rank-form
nonvanishing target.  It does not prove `RC-RANK`; it proves that the rank
target is unchanged by affine source coordinates, nonzero target scalings,
source Mobius reparametrizations, target-coordinate permutations, and
target-coordinate inversions.

## Statement

Fix Stepanov parameters `A,B,H` and rational maps

```text
r_i(X) = P_i(X) / Q_i(X),    i=1,2,3.
```

After denominator clearing, the substitution image is spanned by the columns

```text
X^a product_i P_i(X)^(H b_i) Q_i(X)^(H(B-1-b_i)),

0 <= a < A,      0 <= b_i < B.
```

Let

```text
L = (A-1) + 6H(B-1)
```

be the current degree cap for degree-2 rational maps.

### Source Affine Invariance

For `m != 0`, replace every map by

```text
r_i'(X) = r_i(mX+t).
```

Composition by `X -> mX+t` is an invertible linear map on the coefficient
space of polynomials of degree at most `L`.  It also preserves the
`A`-dimensional source factor span because

```text
span{(mX+t)^a : 0 <= a < A} = span{X^a : 0 <= a < A}.
```

Therefore the cleared substitution image for `(r_i')` is the image of the
original substitution space under an invertible coefficient-space map, and its
rank is unchanged.

### Source Mobius Invariance

More generally, let

```text
M(X) = (alpha X + beta) / (gamma X + delta),
alpha delta - beta gamma != 0.
```

Replace every map by `r_i(M(X))`, clearing each degree-2 numerator and
denominator by the common factor `(gamma X + delta)^2`.  Thus, for
`P_i(Y)=p_0+p_1Y+p_2Y^2`,

```text
P_i'(X) =
  p_0 (gamma X + delta)^2
  + p_1 (alpha X + beta)(gamma X + delta)
  + p_2 (alpha X + beta)^2,
```

and similarly for `Q_i`.

The product part of every cleared column acquires the same common factor

```text
(gamma X + delta)^(6H(B-1)).
```

The source factor remains harmless after homogenizing the degree `< A` source
span.  The forms

```text
(alpha X + beta)^a (gamma X + delta)^(A-1-a),    0 <= a < A,
```

are the image of the standard degree-`A-1` binary-form basis under an
invertible `PGL_2` change of variables, and hence span the same
`A`-dimensional polynomial space as `{1,X,...,X^(A-1)}`.  Multiplication by
the common nonzero denominator-clearing factor is injective.  Therefore the
cleared substitution rank is unchanged by source Mobius reparametrization.

### Target Scaling Invariance

For nonzero constants `c_i`, replace

```text
r_i(X) -> c_i r_i(X).
```

Equivalently, replace `P_i` by `c_i P_i`.  The column indexed by
`(a,b_1,b_2,b_3)` is multiplied by the nonzero scalar

```text
product_i c_i^(H b_i),
```

so the column matroid and the rank are unchanged.

### Target Permutation And Inversion Invariance

Permuting the three rational maps only permutes the multi-index
`(b_1,b_2,b_3)`, so the column set and rank are unchanged.

Replacing one target coordinate by its reciprocal,

```text
r_i = P_i/Q_i  ->  r_i^{-1} = Q_i/P_i,
```

also preserves rank.  In the cleared column formula this swaps the two factors
for that coordinate:

```text
P_i^(H b_i) Q_i^(H(B-1-b_i))
  <-> Q_i^(H b_i) P_i^(H(B-1-b_i)).
```

The change is exactly the column-index involution

```text
b_i -> B-1-b_i.
```

## Role in F3-RANK-AVOID

The future h=3 rank-avoidance theorem may quotient or normalize repaired
signature-curve representatives by source Mobius changes, nonzero coordinate
scalings, target-coordinate permutations, and target-coordinate inversions
without changing the `RC-RANK` inequality.  This removes the parametrization
caveat in the conic base-point equivalence packet: changing the base point on a
nondegenerate same-fiber conic only Mobius-reparametrizes the source.  The
lemma still does not replace the toral, constant-ratio, or hyperbola-line
degeneracy exclusions.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_normalization_invariance.py
```

Expected digest:

```text
H3_RC_RANK_NORMALIZATION_INVARIANCE_PASS
```
