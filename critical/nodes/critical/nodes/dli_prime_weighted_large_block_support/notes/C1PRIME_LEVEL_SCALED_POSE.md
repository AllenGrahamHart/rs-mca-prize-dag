# C1' level-scaled pose and M2 preregistration

- **status:** survived M2; candidate route statement, not a DAG premise
- **purpose:** DLI route item M2
- **pose time:** before computing any M2 primitive-ledger ratio

## Candidate statement

Let `(q,n'=2N,L)` be a generated prime-field full-half-section row with
`q=1 mod n'`, `2^N>=q^L`, and `N>=16L`. Put

```text
T(lambda) = product_(y=0)^(N-1) cos^2(pi a_y(lambda)/q),
E = 1 + sum_(lambda!=0) T(lambda),
r = q^L/2^N.
```

For a reduced primitive signed vanisher orbit `O` of weight `w`, charge its
full signed-shift orbit at mass `2N*2^-w`. Define the level-scaled ledger

```text
w_max(L) = L+5,
W_cl(q,N,L) = sum_(primitive O, L+1<=w(O)<=L+5) 2N*2^-w(O).
```

The candidate C1' inequality is

```text
E-1 <= 4 r (1+W_cl).                              (C1')
```

This is the literal level-scaled version of the banked calibration: its old
row had `L=2` and enumerated weights `3..7`. A fixed absolute `w_max=7` is not
the candidate because it leaves the ledger empty at almost every production
level. The production tower has `N=256L`, so it lies inside the posed aspect
range.

## M2 out-of-sample round

The exact full signed-vanisher spectra in `m1_dli_m1_results.json` were
generated before this pose. They determine `E` by the proved identity

```text
E = (q^L/2^N) * (1 + sum_w signed_count(w)*2^-w).
```

M2 independently enumerates and primitive-filters only the low-weight orbits
needed for `W_cl`. The row set is frozen before those ratios are computed:

```text
L=1, N=32: q in {193,449,769,1409,3137,5569,7937,12289}
L=2, N=32: q in {193,257,449,577}
```

The first set spans the M1 octave range and deliberately includes the observed
orbit-quantized accident row `q=7937`. The second set changes the field scale
at the calibrated depth. All rows satisfy the balance and generated-field
conditions.

## Preregistered read

- **KILL:** any exact row with `E-1 > 4r(1+W_cl)`.
- **SURVIVE:** all twelve rows satisfy C1'.
- **integrity failure:** incomplete signed-shift orbits, a primitive-filter
  discrepancy, missing M1 spectrum data, or a row outside the frozen scope.

Survival makes C1' eligible for further proof work under the F-round rule. It
does not prove C1', B-WEAK, or the DLI node, and it does not by itself justify
DAG surgery.

## M2 outcome

All twelve rows survived. The largest ratio was `K'=0.246909432...` at the
preselected accident row `(L,q)=(1,7937)`. Removing the primitive ledger makes
that row fail, confirming that the repair is substantive. Independent exact
audit: `verify_m2_c1prime_result.py`.
