# Identity-prefix clean-anchor route classification

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Put `M=floor(q/2^t)` and

```text
R(M,k) = binom(M+1,2) k.
```

The pair-root premise in `identity_prefix_flexible_budget_unsafe_floor` is
`R(M,k)<q-n`. Since

```text
M 2^t <= q < (M+1) 2^t,
```

it is impossible whenever `M k >= 2^(t+1)`, and it holds uniformly over the
whole budget interval whenever `R(M,k)<M 2^t-n`.

Apply this router at the six clean-rate candidate predecessors used by the
critical DAG. Five rows are impossible for the identity-prefix route already
at the pair-root premise:

| row | rate | `n` | `k` | predecessor `m` | verdict |
|---|---:|---:|---:|---:|---|
| RowC | `1/4` | `1024` | `256` | `260` | pair-root impossible |
| RowC | `1/8` | `1024` | `128` | `132` | pair-root impossible |
| prize | `1/4` | `2^41` | `2^39` | `558345748480` | pair-root impossible |
| prize | `1/8` | `2^41` | `2^38` | `283467841536` | pair-root impossible |
| prize | `1/16` | `2^41` | `2^37` | `141733920768` | pair-root impossible |

Here RowC uses `M=2^122`, the prize anchors use

```text
M = 317494674775468773183020924238786383963,
```

and `t=128` throughout.

The sole surviving clean anchor is RowC rate `1/16`, with
`(n,k,m,w)=(1024,64,66,1)`. Its pair-root premise holds throughout the
RowC budget interval. If `D` is proved to lie in a field of order `b`, the
prefix premise holds exactly when

```text
b <= 194309137781254382992506402317422272798923813601398339285841609906262.
```

Under that explicit subfield hypothesis the identity-prefix theorem supplies
a `V` payload. Taking `b=q` cannot pass, because every RowC-budget field has
`q>=2^250`, above the 227-bit cutoff.

This classifies one sufficient route. Failure of the route is not safety and
does not refute a quotient, direct-value, or averaged-occupancy payload.
