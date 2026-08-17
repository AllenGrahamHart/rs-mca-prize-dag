# Single completion carrier

- **status:** PROVED
- **correction dimension:** `10`

Let `V<=P_K` have dimension ten and empty common zero set. Fix
`2<=c<=9`. If an independent support-`c` deletion `A` of size `c-1`
attains exactly `M_c>0` minimal circuit completions, let `X_A` be that
completion set. Then

```text
D_A=A union X_A,             |D_A|=M_c+c-1,
W_A={f in V:f|_A=0},         dim W_A=11-c,           (SC)
```

and every polynomial in `W_A` vanishes on all of `D_A`. Consequently
`(D_A,W_A)` may be supplied to every proved fixed-union collision theorem,
without requiring a support-two carrier or a second support stratum.

## Falsifier

An independent attaining deletion whose completion lies outside its
evaluation span, a wrong carrier cardinality, or an annihilator dimension
different from `11-c`.
