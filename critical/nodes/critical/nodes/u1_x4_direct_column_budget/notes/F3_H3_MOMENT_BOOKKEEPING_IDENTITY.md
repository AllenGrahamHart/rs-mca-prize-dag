# F3 h=3 moment bookkeeping identity

Status: PROVED ARITHMETIC IDENTITY, NOT AN `H3-ACT` BOUND.

This packet isolates the exact moment identity referenced in the h=3 program:
the ordered-triple second moment is `72*T_3` plus trivial multiset terms and a
repeat-entry residue.  It is bookkeeping for the T2 route, not a bound on the
moment.

## Pre-registration

Question:

```text
How exactly does the ordered-triple moment M relate to the h=3 trade count T_3?
```

Success criterion:

- define `M` over ordered triples using the `(sum x, sum x^2)` signature;
- prove the contribution of disjoint distinct triple-pairs is exactly `72`;
- state the exact trivial multiset term;
- isolate the repeat-entry residue without assuming it vanishes;
- replay the identity on finite subgroup rows.

Failure criterion:

- drop the repeat-entry residue;
- count ordered pairs as unordered pairs, or lose the sixfold ordering factor;
- treat the identity as a moment bound.

## Identity

Let `H` be a finite subgroup of a field of odd characteristic.  For an ordered
triple `x=(x_1,x_2,x_3) in H^3`, define

```text
sigma(x) = (x_1+x_2+x_3, x_1^2+x_2^2+x_3^2).
```

Since

```text
e_2 = ((sum x)^2 - sum x^2)/2,
```

equality of `sigma` is equivalent to equality of `(e_1,e_2)`.

Let

```text
M = #{ (x,y) in H^3 x H^3 : sigma(x)=sigma(y) }.
```

Let `T_3` count unordered pairs `{A,B}` of disjoint 3-element subsets of `H`
with equal `(e_1,e_2)`.  Then

```text
M = trivial + 72 T_3 + repeat_residue.
```

The trivial term comes from identical multisets:

```text
trivial = 36 * binom(n,3) + 9 * n(n-1) + n.
```

Here `36=6^2` for three distinct entries, `9=3^2` for one repeated pair, and
`1` for a triple repeat.

The factor `72` is exact: a disjoint unordered pair of distinct-entry triples
has two side orderings and `6` orderings on each side, so it contributes

```text
2 * 6 * 6 = 72
```

ordered pairs to `M`.

The residual term is nonnegative and consists precisely of same-signature
ordered multiset-pairs with different underlying multisets where at least one
multiset has a repeated entry.  Distinct-entry multisets with equal signature
cannot overlap unless they are equal: if they share one element, the remaining
two entries have the same sum and product, hence the same two-element multiset.

Thus any moment-form h=3 proof must either bound or separately pay
`repeat_residue`; it cannot silently identify `M-trivial` with `72*T_3`.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_moment_bookkeeping_identity.py
```

Expected digest:

```text
H3_MOMENT_BOOKKEEPING_IDENTITY_PASS
```
