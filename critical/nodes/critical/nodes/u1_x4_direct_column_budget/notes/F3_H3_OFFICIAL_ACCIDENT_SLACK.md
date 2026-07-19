# F3 h=3 official-row accident constant slack

Status: PROVED ARITHMETIC RETARGETING LEDGER, NOT `H3-ACT`.

This packet records an official-row relaxation of the h=3 accident constant.
It does not prove any activation bound.

## Statement

The per-row accident compiler uses

```text
T_3 <= toral + n^2/72 + C n^2.
```

Every official row has `n=2^s`, so `3` does not divide `n` and the toral term
vanishes.  Therefore, on an official row,

```text
T_3 < n^3
```

is implied by

```text
C < n - 1/72.
```

The tight official row is the first one, `n=2^13=8192`.  Hence the largest
uniform integer constant accepted by this arithmetic compiler on all official
rows is

```text
C_official_max = 8191.
```

The current h=3 route targets `H3-ACT(16)`, which is much stronger than the
official-row arithmetic requires.

## Useful Constants

At the first official row:

```text
C=16    gives floor(T_3/n^3 * 10^6) = 1954 ppm;
C=4096  gives floor(T_3/n^3 * 10^6) = 500001 ppm;
C=8191  gives floor(T_3/n^3 * 10^6) = 999879 ppm.
```

Thus a future official-row-only bridge can safely retarget from `H3-ACT(16)` to
any fixed `H3-ACT(C)` with `C <= 8191`.  The midpoint `C=4096` leaves about a
factor-two first-row margin while relaxing the activation budget by a factor
`256` relative to `16`.

## Role

This does not change the already-banked `H3-ACT(16)` interfaces.  It gives a
weaker official-row target that may be easier to prove or certify:

```text
prove H3-ACT(4096) or H3-ACT(8191) on official rows only,
```

or retune the rank-capacity/bridge budgets with one of those constants.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_official_accident_slack.py
```

Expected digest:

```text
H3_OFFICIAL_ACCIDENT_SLACK_PASS
```
