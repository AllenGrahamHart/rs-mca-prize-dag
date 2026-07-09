# F3 h=3 repeat-residue boundary compiler

Status: PROVED ARITHMETIC COMPILER, NOT A REPEAT-RESIDUE BOUND.

This packet refines the repeat-entry residue in the h=3 ordered-triple moment
identity.  The residue is not dropped; it is reduced to a boundary ledger:
distinct triples whose `(sum x, sum x^2)` signature also supports a repeated
multiset.

## Pre-registration

Question:

```text
Can the repeat_residue term be expressed and bounded by a smaller repeated
signature boundary?
```

Success criterion:

- classify repeated-entry multisets with fixed `(sum, sumsq)` in characteristic
  not `2` or `3`;
- prove that their ordered multiplicity per signature is at most `6`;
- derive an exact formula for `repeat_residue`;
- isolate the remaining open boundary term.

Failure criterion:

- assert that `repeat_residue` vanishes;
- hide the distinct-triple boundary inside a numerical constant;
- use row-specific structure not present in the algebraic identity.

## Repeated signatures

Let `sigma(x) = (sum x_i, sum x_i^2)`.

Repeated multisets have two types:

```text
(a,a,a)          ordered weight 1,
(a,a,b), a != b  ordered weight 3.
```

Triple repeats do not collide with distinct double repeats in characteristic
not `2,3`.  If a double repeat has the same sum as `(a,a,a)`, write it as

```text
(a+t, a+t, a-2t).
```

The sum of squares differs from `3a^2` by `6t^2`, hence `t=0`.

For double repeats, set `D(a,b)=(a,a,b)` with `a != b`.  If
`D(c,d)` has the same signature, sum equality gives

```text
c = a+t,    d = b-2t.
```

The sum-of-squares equality is

```text
2t(2a - 2b + 3t)=0.
```

Thus either `(c,d)=(a,b)`, or

```text
c = (a+2b)/3,    d = (4a-b)/3.
```

This second solution is an involution, and it has no fixed point when
`a != b`.

Consequently, for each signature `sigma`, the repeated ordered weight
`R_sigma` is one of:

```text
0, 1, 3, 6.
```

Also, if `Q_sigma` is the sum of squares of the repeated multiset ordering
weights over the signature, then `Q_sigma <= 18`.

## Residue Formula

For each signature `sigma`, define:

```text
D_sigma = ordered weight of distinct-entry multisets with signature sigma,
R_sigma = ordered weight of repeated-entry multisets with signature sigma,
Q_sigma = sum of squared ordering weights of repeated-entry multisets.
```

The h=3 moment packet defined `repeat_residue` as the contribution of
same-signature ordered multiset-pairs with different underlying multisets and
with at least one repeated side.  Therefore signature by signature,

```text
repeat_residue_sigma = 2 D_sigma R_sigma + R_sigma^2 - Q_sigma.
```

The two mixed terms count distinct-repeat and repeat-distinct pairs.  The last
term counts repeat-repeat pairs with unequal underlying multisets.

Let

```text
D_boundary = sum_{sigma: R_sigma>0} D_sigma,
Z_repeat   = #{sigma: R_sigma>0}.
```

Since `R_sigma <= 6` and `R_sigma^2 - Q_sigma <= 18`,

```text
repeat_residue <= 12 D_boundary + 18 Z_repeat.
```

This is the useful reduction.  It does not yet prove that `D_boundary` is
small enough for the h=3 moment route.  It says exactly what the next moment
proof has to bound: distinct-entry triples lying over repeated signatures.

## Role in h=3

The h=3 moment identity is now:

```text
M = trivial + 72 T_3 + repeat_residue,
repeat_residue <= 12 D_boundary + 18 Z_repeat.
```

Thus a moment-form proof can close the residue by proving a boundary estimate
for `D_boundary`; it cannot replace the residue by an unexplained error term.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_residue_boundary_compiler.py
```

Expected digest:

```text
H3_REPEAT_RESIDUE_BOUNDARY_COMPILER_PASS
```
