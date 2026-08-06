# Official exact-slice t-null extras budget

- **status:** TARGET
- **closure:** open

Let `N=2^41`, `K=rho N`, and let the official exact-list depth be

```text
t_XR=min{t>=0 : t log2(q) >= log2 binom(N,N-K-t)+128}.
```

After the quotient, dihedral, boundary, rate-dependent near-tail, and already
priced trade classes in the `x4` ledger are removed, prove

```text
# {non-coset-union t_XR-null blocks and unpriced trade families} <= N^3.
```

This is the exact consumer statement previously hidden inside
`u2c_giant_tnull_dichotomy`. It is not supplied by the generated-field-
guarded full-subset F2 terminal, because the proved route cut gives
`t_XR log2|F_p(mu_N)|<N` on every official row.

The proved near-tail widths are `15,14,13,12` at rates
`1/2,1/4,1/8,1/16`. Thus the unpaid lower half-band starts at
`t_XR+16,t_XR+15,t_XR+14,t_XR+13`, respectively.
