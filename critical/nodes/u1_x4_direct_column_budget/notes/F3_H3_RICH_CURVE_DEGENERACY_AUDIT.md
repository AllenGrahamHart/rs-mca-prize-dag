# F3 h=3 rich-curve degeneracy audit

Status: PROVED AUDIT / T1 HYPOTHESIS REPAIR, NOT THE RICH-CURVE THEOREM.

This is a T1 packet from `notes/codex_briefs/F3_FLIP_20260708.md`.  The
denominator compiler proves the arithmetic degree bound for substituted
degree-2 rational maps, but the planned rich-curve Stepanov theorem also needs
an explicit nondegeneracy hypothesis.  Without it the broad statement

```text
for all degree-2 rational maps r_1,r_2,r_3, sum T(z) <= C (h |Z|)^alpha,
alpha < 1
```

is false.

## Pre-registration

Question:

```text
Can the T1 rich-curve theorem be stated for arbitrary degree-2 rational maps,
or do collapsed H-membership conditions already violate any alpha < 1 bound?
```

Success criterion:

- exhibit a degree-1 subfamily inside the advertised degree-2 class;
- compute its exact `H`-point count for several rows;
- identify the missing exclusion needed before coefficient-count and
  nonvanishing work can be meaningful.

Failure criterion:

- the exhibited family does not actually have `h` simultaneous `H`-points;
- the family is outside the rational-map class covered by the T1 wording.

## Counterexample to the overbroad T1 wording

Let `H = mu_h <= F_p^*` with `h | p-1`.  Take

```text
r_1(X) = X,       r_2(X) = c_2 X,       r_3(X) = c_3 X,
```

with `c_2,c_3 in H`.  Then

```text
r_i(X) in H for all i    <=>    X in H.
```

So the simultaneous incidence count is exactly

```text
T = h.
```

For a one-curve family `|Z| = 1`, any estimate

```text
T <= C h^alpha,       alpha < 1
```

fails for large `h`.  This is not a finite-field accident: the three
membership conditions have collapsed to the same subgroup condition because
the ratios `r_i/r_1` are constants in `H`.

The same issue also explains why a nonvanishing lemma cannot be stated only in
terms of numerator/denominator degrees.  The substituted auxiliary polynomial
may vanish on a large one-condition subgroup cut unless the curve family has
been quotiented by, or explicitly excludes, these multiplicative-dependence
degeneracies.

## Required T1 repair

The rich-curve theorem should carry an exclusion such as:

```text
No nonempty subcollection of the active rational maps is multiplicatively
dependent modulo constants in H and h-th powers in F_p(X)^*.
```

For the F3 signature curves this abstract condition should be replaced by the
node-local geometric list:

- the toral `(0,0)` signature / `mu_3`-coset degeneration;
- the `3 | q-1` rational-line degenerations visible in the hyperbola normal
  form;
- any curve where two or more of the three `H`-membership conditions differ
  only by an `H`-constant factor.

After these cells are paid or excluded, the next T1 packet can attempt the
real coefficient-count/nonvanishing lemma.  The denominator compiler remains
valid; this audit only prevents using it with an overbroad theorem statement.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_audit.py
```

Expected digest:

```text
H3_RICH_CURVE_DEGENERACY_AUDIT_PASS
```
