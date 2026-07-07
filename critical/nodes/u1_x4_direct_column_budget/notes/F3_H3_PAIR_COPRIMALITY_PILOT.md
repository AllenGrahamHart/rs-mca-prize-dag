# F3 h=3 pair-coprimality pilot (Terminal C, 2026-07-08)

Status: PRE-REGISTERED PILOT.  This is evidence for Terminal C, not the full
all-shapes `n=96` census and not a proof.

## Pre-registration

Terminal C target:

> For non-toral h=3 shapes `sigma=(A,B)` in `mu_n`, the two char-zero
> obstruction norms `N(E1(sigma))` and `N(E2(sigma))` generically share no
> rational prime `p = 1 mod n`.  Equivalently, a shape should rarely activate
> at more than one such prime.

Pilot falsifier:

- enumerate every non-toral activated shape that appears in the banked
  `n=96` prime ladder;
- evaluate each activated shape at every prime in that ladder;
- a shape activating at two distinct primes is a direct counterexample to the
  strongest naive pair-coprimality form on this ladder.

Scope:

- `n=96`;
- prime `q = 1 mod 96` entries in the banked dichotomy ladder:
  `9601, 13249, 18433, 26113, 36097, 42337, 46273`;
- shapes are normalized up to dilation and side swap.

This pilot only tests shapes that actually appear in the ladder.  It does not
enumerate all normalized exponent shapes at `n=96`; that remains the full Modal
Terminal C census.

Catch banked: the inherited `QS` list in `f3_h3_dichotomy_modal.py` includes
`23233` and `27649`, which are `1 mod 96` but composite.  This pilot filters to
the actual prime rows above.

## Replay

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
```

Expected digest:

```text
H3_PAIR_COPRIMALITY_PILOT_PASS
```

## Result

Replay passed locally in under two seconds.

Activated shapes:

```text
q=9601:  [0, 15, 39] | [7, 31, 48]
q=13249: [0, 10, 48] | [38, 81, 91]
q=18433: [0, 3, 82]  | [35, 54, 79]
q=26113,36097,42337,46273: none
```

Cross-prime activation check:

```text
[0, 15, 39 | 7, 31, 48]     activates only at 9601
[0, 10, 48 | 38, 81, 91]    activates only at 13249
[0, 3, 82 | 35, 54, 79]     activates only at 18433
```

Verdict: no repeated activation among the observed activated shapes in the
prime ladder.  This supports the pair-coprimality heuristic at the observed
shape level, but does not replace the full all-shapes `n=96` Modal census.
