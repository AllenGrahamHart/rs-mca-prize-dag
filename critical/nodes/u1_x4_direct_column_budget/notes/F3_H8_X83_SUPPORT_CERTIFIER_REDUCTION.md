# F3 h=8 x83 support-certifier reduction

Status: PROVED REDUCTION / MACHINE-VERIFIED ON BANKED H8 N64 ROWS.

This packet closes a bookkeeping gap in the h=8 n=64 residual plan.  The x83
obstruction gate is naturally a statement about a 16-point support `R`, while
the direct-column certificates count anchored left/right h=8 trades.  The
reduction below proves that this support-level gate is sufficient: any x83
full-zero support canonically splits into the two trade sides.

## Pre-registration

Question:

```text
If a future certifier enumerates h=8 n=64 supports and proves that no
non-antipodal support is x83 full-zero, is that enough to replace the blind
left/right signature join?
```

Success criterion:

- prove the algebraic support-to-trade reduction;
- verify it on every paid h=8 square-lift support already banked at
  `p in {193, 4289, 262337}`;
- include a nonzero-control support that is rejected by the x83 classifier;
- state exactly what future certificate remains.

Failure criterion:

- a banked paid support is x83 full-zero but does not split into two h=8 trade
  sides;
- the reduction depends on storing the `binom(63,7)` blind left table;
- the packet promotes the h=8 n=64 partial rows without a non-antipodal support
  certificate.

## Reduction

Let `R` be a 16-subset of `H = mu_64`, and let

```text
L_R(X) = product_{r in R} (X-r)
```

be its monic locator polynomial.  The x83 forced-root recursion determines the
unique monic degree-8 polynomial `S_R(X)` whose square matches the top nine
coefficients of `L_R(X)`.

If all seven low x83 obstructions vanish and

```text
lambda = S_R(X)^2 - L_R(X)
```

is a nonzero square in `F_p`, then

```text
L_R(X) = S_R(X)^2 - alpha^2
       = (S_R(X) - alpha)(S_R(X) + alpha)
```

for either square root `alpha^2 = lambda`.  Since `L_R` is squarefree and split
over `H`, the roots of `S_R-alpha` and `S_R+alpha` form two disjoint 8-subsets
`P,Q` of `R`.  The two monic degree-8 locators differ only in their constant
term, so `P` and `Q` have equal `e_1..e_7` and unequal `e_8`.  Thus `R` carries
an h=8 trade.

Conversely, if disjoint h=8 sets `P,Q` have equal `e_1..e_7` and unequal
`e_8`, their monic locators differ only in their constant term.  Writing

```text
S = (L_P + L_Q)/2
alpha = (L_Q(0) - L_P(0))/2
```

gives

```text
L_P L_Q = S^2 - alpha^2.
```

Therefore the x83 support condition is equivalent to the existence of the
left/right trade split, with no blind signature join required after a support is
classified.

## Machine replay

The verifier replays the reduction on the already-paid h=8 square-lift supports
at:

```text
p=193:    15 x83 full-zero supports, including low-field nontoral h4 quotients
p=4289:   7 x83 full-zero supports
p=262337: 7 x83 full-zero supports
```

Each support is split by evaluating `S_R` on its roots and separating the
`+alpha` and `-alpha` fibers.  The replay checks that both fibers have size 8,
partition the support, and have equal elementary signatures through `e_7` with
unequal `e_8`.

It also checks that the fixed nonzero-control support `{0,1,...,15}` is rejected
by the x83 classifier at each prime.

## Remaining h=8 certifier target

The h=8 n=64 residual can now be stated support-first:

```text
Enumerate or otherwise certify every non-antipodal 16-support R in mu_64 with
0 in R.  Prove either that R is not x83 full-zero, or that its canonical
S_R +/- alpha split is a paid quotient/norm-gate event.
```

This is still open.  The point of this packet is narrower: a support-level x83
certificate is a sound replacement for the oversized blind left/right join.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_support_certifier_reduction.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py
```

Expected digests:

```text
H8_X83_SUPPORT_CERTIFIER_REDUCTION_PASS
H8_RESIDUAL_FRONTIER_AUDIT_PASS
```
