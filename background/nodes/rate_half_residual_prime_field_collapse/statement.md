# Rate-half residual prime-field collapse

- **status:** PROVED
- **closure:** proof plus exact integer certificate
- **consumer:** `rate_half_band_closure`
- **dependency:** `rate_half_ca_hankel_minimal_index_budget`

Let

```text
N=2^41,       q=p^f,
B=floor(q/2^128) in {2^39,2^39+1},
N divides q-1,                                            (RPFC1)
```

where `p` is prime and `f>=1`. Then

```text
f=1.                                                      (RPFC2)
```

Thus every field in either unresolved rate-half residual budget is a prime
field. In particular,

```text
p=q>2^167>N,                                              (RPFC3)
```

so the characteristic exceeds the evaluation-domain size and every degree
in the Hankel and pair-Lagrange reductions.

Before the exact finite exclusion, LTE already forces

```text
f in {1,2,3,4},                                          (RPFC4)

f odd  ==> p=1 mod 2^41,
f=2    ==> p^2=1 mod 2^41,
f=4    ==> p^4=1 mod 2^41.                               (RPFC5)
```

For `f=2`, the two budget intervals contain respectively `24` and `22`
integers satisfying `(RPFC5)`; every one has the nontrivial divisor printed
in `quadratic_candidate_factors.tsv`. For `f=3` and `f=4`, neither interval
contains any integer in an admissible residue class. These statements are
complete exact interval censuses, not probable-prime tests.
