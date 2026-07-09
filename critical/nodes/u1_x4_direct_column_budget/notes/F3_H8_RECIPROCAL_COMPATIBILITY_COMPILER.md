# F3 h=8 reciprocal compatibility compiler

Status: SYMBOLIC COMPILER / X83 INTERFACE, NOT AN h=8 CERTIFICATE.

This packet combines the h=8 triangular x83 obstruction equations with the
reciprocal coefficient relations for supports in roots of unity.  It is the
h=8 analogue of the h=5 reciprocal compatibility surface.

## Reciprocal Rows

For the 16-support locator

```text
L_R(X)=X^16+c15 X^15+...+c0,
```

the triangular compiler gives

```text
D_j E_j = -D_j c_j + P_j(c8,c9,...,c15),      j=1,...,7.
```

Since the support lies in `mu_64`, the locator coefficients satisfy

```text
c_j = delta * conjugate(c_{16-j}),
```

where `delta=c0` is the support product, and there is also the central row

```text
c8 = delta * bar_c8.
```

Thus every h=8 x83 survivor satisfies

```text
P_j = D_j delta * bar_c(16-j),       j=1,...,7.
```

The replay verifies the row profiles:

```text
E1: D=33554432 bar=bar_c15 terms=140 top_total=15
E2: D=16777216 bar=bar_c14 terms=115 top_total=14
E3: D=4194304  bar=bar_c13 terms=89  top_total=13
E4: D=2097152  bar=bar_c12 terms=70  top_total=12
E5: D=262144   bar=bar_c11 terms=52  top_total=11
E6: D=131072   bar=bar_c10 terms=40  top_total=10
E7: D=32768    bar=bar_c9  terms=29  top_total=9
```

## Delta-Free Compatibility

Using `E7` as the base row, eliminate `delta` from the other six rows:

```text
Cj7 := D_7 bar_c9 P_j - D_j bar_c(16-j) P_7 = 0,
       j=1,...,6.
```

The replay verifies:

```text
C17: terms=169 total=16 top_total=15 bar_total=1
C27: terms=144 total=15 top_total=14 bar_total=1
C37: terms=118 total=14 top_total=13 bar_total=1
C47: terms=99  total=13 top_total=12 bar_total=1
C57: terms=81  total=12 top_total=11 bar_total=1
C67: terms=69  total=11 top_total=10 bar_total=1
```

The central coefficient gives one more delta-free row:

```text
C87 := D_7 bar_c9 c8 - P_7 bar_c8 = 0,
```

with profile:

```text
C87: terms=30 total=10 top_total=9 bar_total=1.
```

So the primitive h=8 x83 obstruction can be attacked as seven explicit
delta-free reciprocal compatibility equations, all linear in the reciprocal
bar variables and with maximum total degree `16`.

## Role In h=8

This is still a necessary surface, not a proof of emptiness.  Combined with
`F3_H8_X83_TRIANGULAR_OBSTRUCTION.md`, `F3_H8_X83_PARITY_REDUCTION.md`, and
the support root constraints, it gives a sharper target for a future symbolic
obstruction-key join:

```text
non-antipodal x83 survivor
  => triangular low-key graph
  => at least one high odd locator coefficient nonzero
  => seven reciprocal compatibility equations with shared delta eliminated.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_reciprocal_compatibility_compiler.py
```

Expected digest:

```text
H8_RECIPROCAL_COMPATIBILITY_COMPILER_PASS
```
