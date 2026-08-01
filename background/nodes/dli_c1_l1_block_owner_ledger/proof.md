# Proof

## The convolution step

The signed differences of Boolean vectors on the first 4(j+1) coordinates
decompose as (difference on the first 4j coordinates) + (difference on
block j), and the ternary weight is additive over the split. Hence the
weighted difference fibres satisfy the exact convolution
`K_(j+1) = K_j * kappa_j`, where `kappa_j` is the weighted ternary
difference measure of the four new coordinates. Each coordinate
contributes a factor `(1 + 1/2 + 1/2) = 2` of total mass (d=0 at weight
one; d=+-1 at weight 1/2 each), so `sum_s kappa_j(s) = 2^4 = 16`.

Evaluating the convolution at zero:

```text
Z_(j+1) = K_(j+1)(0)
        = kappa_j(0) K_j(0) + sum_(s != 0) kappa_j(s) K_j(-s).
```

`kappa_j(0) = 1` (the zero pattern) plus the mass of nonzero ternary
patterns on block j summing to zero; such a pattern is a signed relation
of weight <= 4 among four consecutive powers of omega, i.e. (after
dividing by omega^(4j)) a weight-<=4 relation at L=1 — excluded by the
banked Newton short-window exclusion (weights <= 2) and the terminal
ambient weight-3/4 exclusions. Hence `kappa_j(0) = 1` and
`Z_(j+1) = Z_j + A_j`, which is (BO-1); the nonzero mass is 16 - 1 = 15.

## The Haar baseline

`B_j = 2^(4j)/q` satisfies
`B_(j+1) = 2^(4(j+1))/q = 16 B_j = B_j + 15 B_j`, so

```text
X_(j+1) = Z_(j+1) - B_(j+1)
        = (Z_j + A_j) - (B_j + 15 * 2^(4j)/q)
        = X_j + [A_j - 15 * 2^(4j)/q],
```

which is (BO-2). `Z_0 = 1` (the empty difference) and `B_0 = 1/q` give
`X_0 = 1 - 1/q`; summing (BO-2) over j = 0..63 telescopes to (BO-3).
Since `Z - 2^256/q <= 4` iff the right side of (BO-3) is at most 4,
subtracting `1 - 1/q` gives (BO-4). QED.

The identity (BO-3) itself is unconditional; only the interpretation of
`A_j` as strictly first-owner NEW mass (equivalently `kappa_j(0) = 1`)
uses the banked weight-<=4 exclusions, and those hold on every admissible
row.
