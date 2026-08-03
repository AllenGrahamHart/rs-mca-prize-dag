# Statement

## Claim (KBP1B3-DE-P12-1)

On the guarded positive deployed 433-1b role-cell-3 branch, every atlas case
with a missing parallel `DE` record, `xi in {0,1,2}`, and canonical matching
index 12 is empty for all source and target signs. Matching 12 is

```text
((0,5),(1,2),(3,4))
= (de,sigma_c cf), (second_de,df), (sigma_o ef,bf).
```

The raw scope is

```text
3 missing copies * 1 matching * 4 source signs * 4 target lanes
= 48 raw cases.
```

Sixteen exact source rows at `xi in {0,2}` fix `sigma_c` and cover both
`sigma_o` lanes, paying 32 cases. Exact parallel-copy transport from
`xi=0` pays the 16 `xi=1` cases.

No other matching, missing role, complete cell-3 exclusion, rate-half band,
LIST, MCA, or Prize result is claimed.
