## MCA O0b `FFF` generic-system route cut (2026-08-17)

### Exact result

The monolithic generic extension by `q5,q7,q6` validated its ten base and
three necessary input equations, but did not complete a Groebner basis in
300 seconds:

```text
INPUT_COMPLETE 10 13
Modal app: ap-WmwCjoXxq9zHBUxYo4xL44
result:    INCOMPLETE_TIMEOUT
```

No basis, unit claim, or dimension was produced. The result SHA-256 is
`13cc45ebcda366c4a659e032f3ea63bddddc2267dc2877f3574d250ca4c84ef5`.
Granting the same monolithic computation a larger wall is not the selected
route.

### Incremental route

The base algebra has dimension eight, while `q5` is quadratic in `s` and
`q7` is quadratic in `E`. First normal-form `q5` modulo the certified base
basis and compute the resulting finite extension. Import that exact basis
for `q7`, then adjoin `q6` only at the final stage. Each stage retains its
own coefficient denominators and quotient dimension.

### Proof boundary

The timeout changes no DAG status. An incremental generic unit would still
need a specialization certificate exposing every transformation pivot,
followed by all exceptional fibers.
