# Proof

Fix a support `S`. Suppose distinct slopes `z_1,z_2` are explained on `S`
by codewords `p_1,p_2`:

```text
u+z_i v=p_i on S.                                        (1)
```

Subtracting and solving the two equations gives codewords

```text
v=(p_1-p_2)/(z_1-z_2),
u=(z_1 p_2-z_2 p_1)/(z_1-z_2)
```

that explain `(u,v)` simultaneously on `S`. Hence a support-wise
noncontained slope cannot share its fixed support with another such slope.
Counting supports over the active range `B-k<c` and applying a union bound
proves `(QSF1)`. This argument also shows why the support sum is conservative:
different supports may map to the same slope.

The clean-row witness cells are

```text
row       rate   n       k       A              c       B
RowC      1/4    2^10    256     261            8       261
RowC      1/8    2^10    128     133            8       135
RowC      1/16   2^10    64      67             16      79
prize     1/4    2^41    2^39    558345748481   2^34    A
prize     1/8    2^41    2^38    283467841537   2^34    A
prize     1/16   2^41    2^37    141733920769   2^33    A.
```

Each cell is active because `B-k<c`. The three RowC summands can be evaluated
directly and have binary logarithms approximately `141.22`, `122.66`, and
`127.47`, all above `log_2 B*=122`.

At each prize cell, `B=A=k+t<k+c`, `floor(B/c)=k/c`, and the residual
binomial is `C(n-k,t)`. Here `4<=t<=(n-k)/2`, so

```text
C(n-k,t)>=C(n-k,4)>B*.
```

The last strict inequality is exact integer arithmetic; it avoids
materializing the enormous official binomial. Multiplication by the positive
profile binomial preserves it. The verifier checks all six active witnesses
and independently replays the existing fixed-threshold budget inequality

```text
B_quot_ub(A)+(n-A+1)+16n^3<=B*.
```

The contrast is the claimed fence. The fixed-threshold ledger fits, but the
active threshold-union support ledger does not. No lower bound on the
actual distinct-slope image follows from an oversized upper bound. QED.
