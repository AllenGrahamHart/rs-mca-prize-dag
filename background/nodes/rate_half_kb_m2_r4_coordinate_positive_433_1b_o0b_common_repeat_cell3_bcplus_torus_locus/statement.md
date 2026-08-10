# Repeated-BC cell-3 BC+ torus locus

- **status:** PROVED
- **scope:** all four source-root-sign rows in role cell 3 with repeated BC sign `+1`

Work over `F_p`, where

```text
p = 2130706433,
iota = 16711679,
iota^2 = -1.
```

For root signs `epsilon=(epsilon_1,epsilon_2)`, the complete guarded common
locus from the compact-locus parent has the parameterization

```text
t = epsilon_1 epsilon_2 r^2,
c = u,
b = -u^-3,
H_epsilon(r,u)
  = u r^2
    - epsilon_1 (iota+epsilon_2)(u^2+1)r
    + epsilon_2 iota u
  = 0.
```

More precisely, guarded reduction of the original compact ideal gives the
first three parameter relations. After substitution and denominator
clearing, the exact monic gcd of the three remaining compact equations is

```text
r^2 (u^2-1)^2 H_epsilon(r,u).
```

The factors `r` and `u^2-1` are excluded by the inherited source/target
guards. After division by the displayed full gcd, the three primitive
equations generate the unit ideal after saturation by the transformed full
guard. Thus no additional guarded component exists. This completes all four
root-sign rows.

This does not append any of the seven outside source records, prove outside
compatibility or incompatibility, close `433-1b/O0b`, close the positive
route, K3, LIST, MCA, or either Prize result.

## Falsifier

A guarded common point violating one of the parameter relations, a mismatch
in the displayed gcd, a guarded zero of the residual primitive ideal, or a
guarded point on `H_epsilon=0` failing one of the compact equations.
