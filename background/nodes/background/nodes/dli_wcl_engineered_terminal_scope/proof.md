# Proof certificate

`experiments/prize_resolution/dli_wcl_engineered_norm_modal.py` computes

```text
Res(X^256+1, 1-X^33+X^40-X^136-X^143+X^145)
```

with FLINT and factors the resulting integer with PARI/GP. The result is
banked in `dli_wcl_engineered_norm_result.json`. Modal runs
`ap-sQe3iaZpCshibpYUnjWHyn`, `ap-IOvzGbkFXcgP7DNzJzo7IV`, and the final
certificate runs `ap-Rhe4kS4Qku4OHLGqmNWrat` and
`ap-T5Ocgo15fQ557Vbce77Dx7` independently recovered the same
norm and factorization.

Remote replay:

```text
tools/ramguard modal -- ~/.venvs/modal/bin/modal run \
  background/nodes/dli_wcl_engineered_terminal_scope/notes/verify_norm_remote.py
```

The final artifact includes a recursive Pocklington certificate for the
256-bit factor. Every leaf below `10000` is checked by trial division; at each
other node the certificate completely factors `n-1`, recursively proves its
prime factors, and supplies a Pocklington witness for every distinct factor.
The local verifier checks the full tree with exact modular arithmetic.

It also reconstructs the norm as `2q`, derives a primitive root from the
certified factorization of `q-1`, verifies that the induced `omega` has exact
order `512`, and finds the odd Galois dilation for which `P(omega^a)=0 mod q`.
Finally the same factorization
gives `q-1=2^9 m` with `m` odd. Hence the relation reaches the terminal split
and cannot reach the ambient `2^41` split.
