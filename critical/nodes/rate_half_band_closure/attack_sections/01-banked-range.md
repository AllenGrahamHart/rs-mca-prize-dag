
## Banked range

Put

```text
N=2^41,       k=R=2^40,       B=floor(q/2^128).
```

For every admissible `2^128<q<2^167`, the adjacent agreement is proved to be

```text
a_RH(q)=N-B+1.
```

At the same candidate, the sparse MCA layer and the adjacent unsafe witness
are already paid through `B<=2^39+1`. The only missing condition for the two
next budgets is therefore

```text
B_ca^far(N-B+1)<=B.                                  (K5-CA)
```

By `rate_half_residual_prime_field_collapse`, every admissible field in these
two budget intervals is a prime field `F_p`, with `p>2^167` and
`2^41 | p-1`. Extension-field cases must not be allocated.
