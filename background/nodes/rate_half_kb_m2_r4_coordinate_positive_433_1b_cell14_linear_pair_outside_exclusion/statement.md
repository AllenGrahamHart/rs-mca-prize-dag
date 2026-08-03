# KoalaBear m2 r4 positive 433-1b cell-14 linear-pair outside exclusion

- **status:** PROVED
- **scope:** the guarded principal quadratic-cover branch of deployed positive
  `433-1b -> O0a` role cell `14`
- **dependencies:** the cell-14 quadratic-curve structure, the signed outside
  atlas, and the complete-fiber Vieta compiler

## Claim `(KBP1B14-LPAIR-1)`

Write the seven signed outside product records as

```text
y = (de,de,-de,df,sigma_o ef,bf,sigma_c cf).       (KBP1B14-LP-1)
```

For every source-sign pair, every signed target lane
`(sigma_c,sigma_o)`, and every complete outside assignment in which

1. the missing record is one of `y_0,y_1,y_2`; and
2. the two residual records among `y_0,y_1,y_2` form one of the three
   Vieta pairs,

the guarded cell-14 outside system is empty over the deployed field
`F_2130706433`.

There are three missing-record choices and three perfect matchings with the
required residual pair for each of the `4 x 4` source-sign/target-lane rows.
Thus the claim excludes exactly

```text
4 * 4 * 3 * 3 = 144                              (KBP1B14-LP-2)
```

of the `4*4*7*15=1680` raw cell-14 outside cases.

This theorem does not exclude the remaining `1536` outside cases, close role
cell `14`, close `433-1b -> O0a`, or prove K3, LIST, MCA, or either Prize
problem.

## Falsifier

A guarded deployed-field zero of any one of the 144 printed outside systems,
an omitted parameter-boundary factor, or a failure of the exact Cartesian
coverage count.
