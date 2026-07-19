# F3 h=3 repeat singleton-hitting stress

Status: FINITE STRESS EVIDENCE, NOT A THEOREM.

The hitting exception scan falsifies the fixed-`2` cover, but it does not
falsify the stronger-looking star phenomenon:

```text
tau_coord <= 1
```

for boundary-style rows.  This packet records a bounded stress test for that
specific target.

## Payoff

The coordinate-hitting compiler gives

```text
repeat_residue <= (72 tau_coord + 18)n^2.
```

Therefore a singleton-hitting theorem would imply

```text
repeat_residue <= 90n^2.
```

This is below `n^3` for every `n > 90`, hence for every official row
`n=2^s`, `13 <= s <= 41`.

## Bounded Scan

The script scans boundary-style primes `p >= n^2`, `p = 1 mod n`, in the
following windows:

```text
n=16:  first 200 such primes
n=32:  first 200 such primes
n=64:  first 200 such primes
n=128: first 120 such primes
n=256: first 80 such primes
```

It raises an error if any active row has `tau_coord > 1`.

Observed summary:

```text
n=16  nonzero_rows=1 max_row=p=337,B=6,edges=1,tau=1,hit=191
n=32  nonzero_rows=1 max_row=p=2017,B=6,edges=1,tau=1,hit=459
n=64  nonzero_rows=5 max_row=p=65537,B=24,edges=4,tau=1,hit=2
n=128 nonzero_rows=3 max_row=p=65537,B=48,edges=8,tau=1,hit=2
n=256 nonzero_rows=6 max_row=p=65537,B=48,edges=8,tau=1,hit=2
```

No row in this bounded scan has `tau_coord > 1`.

## Role in h=3

The correct next theorem target is now sharply stated:

```text
H3-STAR-HITTING:
  prove tau_coord <= 1 in the boundary-style regime,
```

or find the first `tau_coord > 1` obstruction and replace this by a sublinear
hitting theorem.  The current evidence supports the star target, while the
exception scan shows that the star center cannot be fixed in advance as `2`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_singleton_hitting_stress.py
```

Expected digest:

```text
H3_REPEAT_SINGLETON_HITTING_STRESS_PASS
```
