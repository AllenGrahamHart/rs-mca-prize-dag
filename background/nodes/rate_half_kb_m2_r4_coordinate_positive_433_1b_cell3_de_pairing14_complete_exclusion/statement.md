# Statement

## Claim (KBP1B3-DE-P14-1)

On the guarded positive deployed 433-1b role-cell-3 branch, every atlas case
with a missing parallel `DE` record

```text
xi in {0,1,2}, pairing index 14,
epsilon in {+-1}^2, sigma in {+-1}^2
```

is empty. Canonical matching 14 is

```text
((0,5),(1,4),(2,3))
= (de,sigma_c cf), (second_de,bf), (df,sigma_o ef).
```

The raw scope contains

```text
3 missing copies * 1 matching * 4 source signs * 4 target lanes
= 48 raw cases.
```

Sixteen exact source rows at `xi in {0,2}` fix `sigma_c` and cover both
`sigma_o` lanes, paying 32 cases. Exact parallel-copy transport from
`xi=0` pays the 16 `xi=1` cases.

No other matching, missing role, complete cell-3 exclusion, rate-half band,
LIST, MCA, or Prize result is claimed.
