# Proof

For a row `K'=K`, put

```text
n=1048576+K,       m=67472+K,       q=K-10,
R_min=274980728111260126.
```

## Kernel capacity

Retain the uniform corank-one cap, every canonical-basis corank-two-through-
eight cap and extension factor, and the corank-nine endpoint.  Their sum is
the exact `K_cap(K)` used by the verifier.

## Full-rank capacity

For every core `9<=j<K`, evaluate the integral heavy-owner chart exactly and
put

```text
G(K)=C(n,9) max_j chart(K,j).
```

Every maximum on `24<=K<=41` occurs at `j=K-1`; the verifier nevertheless
scans every core.

For supports two through five, let `S_c` be the saturated structured cap and
`D_c` the completion-defect cap.  For supports six through nine, let `U_c`
be the universal completion cap.  With

```text
d_c=C(11-c,2),
P_U=sum_(c=6)^9 d_c U_c,
P(K)=P_U+max(sum_(c=2)^5 d_c S_c,
             sum_(c=2)^5 d_c D_c),
```

the full-deficit shadow ledger gives

```text
F_cap(K)=floor((G(K)+R_min P(K))/55).               (1)
```

Thus complete component capacity is `K_cap(K)+F_cap(K)`.  Compare it with

```text
D(K)=ceil((990810934/10^9) R_min C(m,11)).          (2)
```

Exact integer evaluation of (1)-(2) gives positive gaps on every row
`24<=K<=40`.  After clearing `55*10^9`, both the coefficient of the actual
record count and the full cross at `R_min` are positive on those rows.
Hence the contradiction persists for every admissible record population.

At `K=41` the record coefficient remains positive but the cross at
`R_min` is negative, producing the displayed method wall.  No statement
about the actual component family at that row follows.
