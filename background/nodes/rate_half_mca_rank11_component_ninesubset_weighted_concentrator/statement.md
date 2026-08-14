# Component nine-subset weighted concentrator

- **status:** PROVED
- **scope:** the dominant typed lane in the residual rank-eleven component
  incidence family

For `n'=1048576+K'`, `m'=67472+K'`, and
`N_min=274980728111260126`, there is one fixed nine-subset `B` such that

```text
W_B >=ceil((495405467/10^9) N_min
           *C(m',9)*C(m'-9,2)/C(n',9)).             (WC1)
```

Here `W_B` counts pairs `(gamma,T)`, with multiplicity in `T`, for which
`gamma` is a retained record in one fixed component lane and `T` is a
component eleven-subset containing `B`.

At `K'=10`, the right side is `5868470021012020`. Since one record has at
most `C(m'-9,2)` such extensions, (WC1) also recovers the existing
`2578110` distinct-record floor.

## Nonclaim

The theorem retains incidence weight; it does not pay the fixed chart or
identify records across different nine-subsets.
