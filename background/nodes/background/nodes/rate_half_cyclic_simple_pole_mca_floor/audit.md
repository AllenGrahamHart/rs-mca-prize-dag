# Independent trigger audit

The prize threshold requires more than `q/2^128` bad slopes, not a list larger
than `q/k`. For the quantitative simple-pole conversion the exact guaranteed
bad-slope numerator is

```text
M_q = ceil(L_q(q-n)/(q-n+kL_q)).
```

At the cap proxy `q=2^256`, exact integer arithmetic gives

```text
log2 L_q  = 203.079624489...
log2 M_q  = 203.079438398...
log2(q/2^128) = 128.
```

Thus the collision charge is about `0.0001861` bits and the bad-slope margin
is about `75.0794` bits. Simultaneously `L_q<(q-n)/k`, so this instance is a
direct counterexample to treating the clean deep-list trigger as necessary.
It is not a counterexample to the trigger theorem, which states only a
sufficient condition for the stronger floor of order `1/(2k)`.

The independent verifier works backward from the exact prize inequality,
checks the required list threshold and the integer bad-slope numerator, audits
the uniform endpoint bounds, and checks the logical DAG edge. It also verifies
that the maximal legal residual prefix reaches `sigma_max=8,594,128,895` and
strictly contains the former proposed safe agreement `sigma*+1`. It uses no
floating-point value in an assertion.
