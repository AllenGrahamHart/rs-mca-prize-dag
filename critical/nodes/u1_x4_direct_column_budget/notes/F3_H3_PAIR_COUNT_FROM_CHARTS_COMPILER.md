# F3 h=3 pair-count from charts compiler

Status: CONDITIONAL LOCAL-TO-PAIR COMPILER, NOT `H3-ACT`.

This packet makes explicit why the h=3 bridge needs more than a linear
incidence bound.  The rich-curve chart count controls ordered triples in a
same-`(e1,e2)` fiber.  Activated shape-pairs are unordered pairs of such
triples, so the local contribution is quadratic in the local fiber size.  A
future proof must therefore provide either a max-fiber cap, a dyadic level-set
bound, or an equivalent rank-capacity batching theorem.

## Pre-registration

Question:

```text
Given chart counts T_z for repaired h=3 conic charts, what exact arithmetic
turns them into a bound for activated triple-pairs?
```

Success criterion:

- use the already-banked identities `R_z = T_z + epsilon_z` and
  `P_z = R_z(R_z-6)/72`;
- state a sufficient pair-count bound using total chart mass and max chart
  mass;
- replay the formulas on finite subgroup rows;
- keep the result explicitly conditional on a future global bridge/level-set
  theorem.

Failure criterion:

- treat a linear bound on `sum T_z` alone as enough;
- ignore the possible vertical point `epsilon_z`;
- promote this local arithmetic compiler to `H3-ACT`.

## Compiler

For each repaired same-`(e1,e2)` conic chart `z`, let:

```text
T_z = finite affine chart count with U_z(t),V_z(t),W_z(t) in H,
epsilon_z in {0,1} = vertical/projective point contribution,
R_z = T_z + epsilon_z = ordered same-fiber triple count.
```

The local fiber-count bridge gives:

```text
N_z = R_z / 6,
P_z = binom(N_z,2) = R_z(R_z-6)/72.
```

Thus for any collection of charts:

```text
P_total = sum_z P_z.
```

If a future theorem gives

```text
T_z <= M       for every z,
sum_z T_z <= S,
number of charts <= Z,
```

then, since `R_z <= M+1` and `sum_z R_z <= S+Z`,

```text
P_total <= (M+1)(S+Z)/72.
```

Consequently, for the h=3 activation target, a sufficient chart-level condition
for a normalized chart ledger is:

```text
(M+1)(S+Z) <= 1152 n       =>       P_total <= 16 n.
```

This is only a local-to-pair compiler.  It does not prove that all activated
normalized shape-pairs can be represented by such a chart ledger with the
printed `S,M,Z`; that is still the global bridge/rank-capacity problem.

## Interpretation

The current reduced-condition/rank compiler gives a linear bound on `sum_z T_z`
for a repaired chart family.  This packet shows the exact missing ingredient:
a linear chart-sum bound alone does not control activated pairs unless a
max-fiber or level-set bound is also supplied.

The future h=3 theorem can now be phrased more sharply:

```text
RC-RANK + bridge/level-set theorem producing S,M,Z with
(M+1)(S+Z) <= 1152 n
  => H3-ACT(16).
```

The existing `H3-BRIDGE-RANKCAP` interface is one way to package that
bridge/level-set theorem.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_pair_count_from_charts_compiler.py
```

Expected digest:

```text
H3_PAIR_COUNT_FROM_CHARTS_COMPILER_PASS
```
