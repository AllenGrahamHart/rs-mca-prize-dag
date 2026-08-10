# Repeated-BC cell-3 `BC-` genus-two tower locus

- **status:** PROVED
- **field:** `F_2130706433`
- **scope:** all four source-root-sign rows in role cell 3 with repeated `BC` sign `-1`

Put `iota=16711679`, so `iota^2=-1`. For root signs
`epsilon=(epsilon_1,epsilon_2)`, the complete guarded common locus from the
compact-locus parent is exactly

```text
t = epsilon_1 epsilon_2 r^2,
F(b,c) = 0,
(bc-1)(epsilon_1 epsilon_2 r^2+epsilon_1 iota)
  -(epsilon_2 iota+1)r(c-b) = 0,
```

where

```text
F(b,c) = b^3c^3+b^2c^4+3b^2c^3-2b^2c^2-2b^2c-b^2
         -bc^4-2bc^3-2bc^2+3bc+b+c.
```

The curve `F=0` has the guarded birational model

```text
y = (c+1)/(c-1),
q = ((b+1)/(b-1))/y,
y^2 = N(q)/D(q),
N(q)=q^3+2q^2+q+4,
D(q)=q^3+6q^2+q.
```

Equivalently, with `w=D(q)y`, its smooth projective model is
`w^2=N(q)D(q)`. The degree-six polynomial `ND` is squarefree over the audit
field, so this is a genus-two curve. Over its function field, `r` is a
quadratic extension:

```text
r^2 = epsilon_1(iota+epsilon_2)(c-b)/(bc-1) r
      -epsilon_2 iota.
```

This describes only the common locus. The seven outside records, their
pairings, other owner blocks, the complete `433-1b -> O0b` route, and both
Prize conclusions remain open.

## Falsifier

A guarded common point violating either displayed equation, a point of the
two-equation tower ideal violating a compact equation, or a repeated factor
of `N(q)D(q)` in the audit field.
