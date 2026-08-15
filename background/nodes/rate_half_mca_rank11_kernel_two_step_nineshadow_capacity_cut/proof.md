# Proof

The predecessor closes `10<=K'<=17608`, so only the 494 rows
`17609<=K'<=18102` require a new certificate.  Normalize the corank counts by
the residual-record floor and write them as `x_1,...,x_9`.

On every new row the exact optimum has the same active set:

- the individual corank-one cap binds;
- the full-containment resource binds;
- every two-step hierarchy inequality `H_3,...,H_9` binds;
- the rank-preserving nine-shadow resource is slack;
- all nine corank variables are positive and all other individual caps are
  slack.

Write `A_d=C(d+2,2)C(67472+d,2)/C(K'-d-9,2)` and
`Q_d=C(11-d,2)`.  Set `f_1=f_2=1` and recursively

```text
f_d=(Q_d/A_d) f_(d-2).
```

The odd chain is fixed by `x_1=cap_1`.  The full-containment equality then
determines the even-chain base `x_2`; all other variables are
`x_d=f_d x_1` or `f_d x_2` according to parity.  Exact replay checks primal
feasibility on all 494 rows.

For optimality, the primary replay solves the nine exact complementary-
slackness equations for the nonnegative multipliers of the containment
resource, the corank-one cap, and `H_3,...,H_9`.  Its dual objective equals
the displayed primal value on every row.  Thus strong duality certifies the
exact capacity.

At `K'=18101`, demand exceeds floored capacity by

```text
33462159928103132226516704640419847248244116666500998762314.
```

At `K'=18102`, capacity exceeds demand by

```text
275016496133605602641019628236447268989861205055439981187167.
```

The independent audit derives the dual multipliers by backward odd/even
recurrences rather than Gaussian elimination.
