# F3 h=3 private-divisor full-rank refutation

Status: REFUTED OVERSTRONG `RC-RANK` ROUTE; MACHINE-VERIFIED CONTROL.

This packet kills a tempting but false shortcut for the remaining h=3
rank-form nonvanishing gate.  Private zeros/poles for `X,r_1,r_2,r_3` are not
enough to prove full coefficient-rank injectivity of the substitution map.

## Pre-registration

Candidate criterion:

```text
If X, r_1, r_2, r_3 each has a private zero or pole where the other three
maps are regular nonzero, then the monomials

    X^a r_1^(h b_1) r_2^(h b_2) r_3^(h b_3)

are linearly independent on the full A B^3 coefficient box.
```

Success criterion for refutation:

- exhibit a curve with the private-divisor pattern;
- compute the exact cleared substitution rank;
- show that the rank is strictly below `A B^3`.

Failure criterion:

- the curve does not actually have private divisors;
- the rank is full;
- the refutation is confused with failure of the weaker `RC-RANK` target.

## Counterexample

The replay works over

```text
p=769, h=32, A=5, B=4, D=1.
```

Use

```text
r_1 = (X-2)/(X-3),
r_2 = (X-5)/(X-7),
r_3 = (X-11)/(X-13).
```

Then `X,r_1,r_2,r_3` have private zeros at

```text
0, 2, 5, 11.
```

However the exact cleared substitution rank is

```text
rank = 293 < A B^3 = 320.
```

Thus the full-rank private-divisor criterion is false.

This does not refute the actual rank target in this toy row: the
`RC-RED(13)` condition count is only

```text
13 D (A + D) = 78,
```

so the weaker rank target still holds:

```text
78 < 293.
```

## Consequence

The remaining `RC-RANK` theorem cannot be proved merely by assigning private
divisors to the four generators.  It needs either:

- a genuine lower bound on the substitution image rank after degeneracy
  repairs; or
- a sharper confluent/residue argument that controls cancellation inside the
  private-divisor leading terms.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_divisor_full_rank_refutation.py
```

Expected digest:

```text
H3_PRIVATE_DIVISOR_FULL_RANK_REFUTATION_PASS
```
