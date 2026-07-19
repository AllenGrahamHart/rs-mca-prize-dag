# Proof

The four split-pencil triangle identities include

```text
A_2b_01+A_0b_12=A_1b_02,                            (1)
A_3b_01+A_0b_13=A_1b_03,                            (2)
A_3b_12+A_1b_23=A_2b_13.                            (3)
```

Multiply `(PG1)` by the nonzero polynomial `A_1`. Use `(3)` in the first
term, `(1)` in the second, and `(2)` in the third:

```text
A_1(b_01b_23-b_02b_13+b_03b_12)
 =b_01(A_2b_13-A_3b_12)
  -(A_2b_01+A_0b_12)b_13
  +(A_3b_01+A_0b_13)b_12
 =0.
```

The polynomial ring is an integral domain and `A_1` is nonzero, proving
`(PG1)`.

The minors of the two printed rows are immediate for pairs containing `0`
or `1`. The `23` minor is

```text
-b_12b_03+b_13b_02=b_01b_23
```

by `(PG1)`, proving the minor statement. Equations `(1)--(2)` are precisely
the last two coordinates of `(PG2)`; its first two coordinates are
identities.

From `(1)--(2)`, `N_2=b_01A_2` and `N_3=b_01A_3`. The preceding normal form
gives

```text
Lambda_D=R A_0A_1A_2A_3.
```

Multiplying the two expressions for `N_2,N_3` and substituting this partition
identity proves `(PG3)`. Finally the six-type table has
`n_1+n_2+n_4` equal to `4,4,6,8,3,5`, respectively, so `deg R<=8`. QED.
