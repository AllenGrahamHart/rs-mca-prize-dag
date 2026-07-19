# Conditional proof: arbitrary-arity list closure

- **status:** CONDITIONAL
- **predicate node:** `list_adjacency_closing` (only its `m=1` instance)
- **proved bridge:** `list_subsqrt_interleaving_collapse`

Fix an admissible row, write `q=|F|` and
`B*=floor(q/2^128)`, and grant the base adjacent crossing

```text
L_1(a0) > B* >= L_1(a0+1).
```

The official cap `q<2^256` gives

```text
(B*)^2 <= q^2/2^256 < q.
```

At the safe agreement `a0+1`, the base maximum obeys
`L_1(a0+1)<=B*`, hence `L_1(a0+1)^2<q`. The proved
`list_subsqrt_interleaving_collapse` theorem therefore gives, for every
`m>=1`,

```text
L_m(a0+1)=L_1(a0+1)<=B*.
```

At `a0`, choose a base received word with more than `B*` agreeing codewords.
Repeating that received word in every row and diagonally embedding each
codeword gives more than `B*` interleaved tuples with the same common
agreement support. Thus

```text
L_m(a0)>=L_1(a0)>B*.
```

Both inequalities hold at the same adjacent pair for every `m`. This proves
the claimed implication. The codegree, support-census, and extension-field
packets remain valid independent tools, but are not hypotheses of this close.

## WAVE-11 ADDENDUM (2026-07-18)

The B* in {1,2} branches are now UNCONDITIONALLY delivered at every
common-support arity m >= 1 (rate_half_list_low_budget_all_arity_
crossing, PROVED; ev-wired). No status change — the larger-budget
branches remain as posed.
