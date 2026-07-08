# F3 Flip Log 2026-07-08

## Initial stage: T3 h=2 constant campaign

Stage selected: T3 constant optimization for the already-proved h=2 in-house
chain.  This is independent of the harder T1 rich-curve proof and immediately
shrinks the finite midrange that would need exact certificates if the in-house
chain were used without the external Cochrane--Pinner import.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_RICH_COSET_OPTIMIZED.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_optimized.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_optimized.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_stepanov.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_per_row_accident_pose.py
```

Digest:

```text
H2_RICH_COSET_OPTIMIZED_PASS
H2_HBK_CONDITIONAL_COMPILER_PASS
H2_RICH_COSET_STEPANOV_PASS
H3_PER_ROW_ACCIDENT_POSE_PASS
```

Result: the same rich-coset Stepanov proof now has exact floor bookkeeping with
`K=66` instead of the old conservative `K=129`.  The propagated in-house h=2
constant improves from

```text
E(H) <= 83851 h^(5/2)
```

to

```text
E(H) <= 22111 h^(5/2).
```

The h=2 `T_2 < h^3` crossover moves from `7030990201/64` to
`488896321/64`, i.e. integer `h >= 7,639,006`.  Therefore the in-house h=2
chain covers all official power-of-two rows from `2^23` upward; only
`2^13` through `2^22` remain a finite midrange if the external import is not
used.

Next step: start T1 with a rich-curve denominator-clearing and coefficient
count packet, or continue T3 by estimating exact-census cost for the h=2
midrange rows `2^13..2^22`.

## T1 groundwork: rich-curve denominator compiler

Stage selected: T1 denominator clearing for degree-2 rational signature-curve
maps.  This isolates the first arithmetic obligation in the rich-curve
Stepanov route before attempting the nonvanishing and family coefficient-count
steps.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_RICH_CURVE_DENOMINATOR_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py
```

Digest:

```text
H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS
```

Result: for `r_i=P_i/Q_i` with `deg P_i, deg Q_i <= 2` and auxiliary
`Phi(X,Y_1,Y_2,Y_3)` with `deg_X < A`, `deg_{Y_i} < B`, the clearing
denominator

```text
Q_1^{h(B-1)} Q_2^{h(B-1)} Q_3^{h(B-1)}
```

turns `Phi(X,r_1^h,r_2^h,r_3^h)` into a polynomial of degree at most

```text
(A - 1) + 6 h (B - 1).
```

The verifier checks the identity exactly over finite fields for 60 deterministic
degree-2 rational-map cases.  This does not prove T1; it pins the degree input
for the eventual multiplicity contradiction.

Next step: T1 coefficient-count/nonvanishing packet for this cleared
four-variable auxiliary polynomial, or T3 h=2 midrange certificate-cost table.
