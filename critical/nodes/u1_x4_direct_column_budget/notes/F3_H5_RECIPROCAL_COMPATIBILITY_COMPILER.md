# F3 h=5 reciprocal compatibility compiler

Status: SYMBOLIC COMPILER / NORM-GATE INTERFACE, NOT AN h=5 CLOSURE.

This packet sharpens the h=5 x83 norm-gate target.  The triangular low-key
equations give four reciprocal identities with a shared support product
`delta`; eliminating that shared `delta` gives three explicit compatibility
equations on the high locator coefficients and their conjugates.

## Reciprocal Rows

For the 10-support locator

```text
L_R(X)=X^10+l9 X^9+...+l1 X+l0,
```

the triangular compiler gives

```text
D_j E_j = -D_j l_j + P_j(l5,l6,l7,l8,l9),      j=1..4.
```

Since the support lies in `mu_n`,

```text
l_j = delta * conjugate(l_{10-j}).
```

Thus every h=5 x83 survivor satisfies

```text
P_j = D_j delta * bar_l_{10-j},       j=1..4.
```

The replay verifies the following exact profiles for `P_j`:

```text
E1: D=16384, bar=bar_l9, terms=22, top_total=9
E2: D=16384, bar=bar_l8, terms=18, top_total=8
E3: D=256,   bar=bar_l7, terms=13, top_total=7
E4: D=512,   bar=bar_l6, terms=10, top_total=6
```

## Delta-Free Compatibility

Using `E4` as the base row, eliminate `delta` from the other three rows:

```text
Cj4 := D_4 bar_l6 P_j - D_j bar_l(10-j) P_4 = 0,
       j=1,2,3.
```

The replay verifies:

```text
C14: terms=32, total=10, top_total=9, bar_total=1
C24: terms=28, total=9,  top_total=8, bar_total=1
C34: terms=23, total=8,  top_total=7, bar_total=1
```

So the symbolic h=5 norm-gate obstruction can be attacked as three explicit
delta-free reciprocal compatibility equations plus one remaining equation that
recovers `delta`.

This still does not prove the h=5 branch empty.  It gives the next algebraic
surface that a norm-gate incompatibility proof or certificate family should
target.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_reciprocal_compatibility_compiler.py
```

Expected digest:

```text
H5_RECIPROCAL_COMPATIBILITY_COMPILER_PASS
```
