# Official exact-slice t-null extras budget

- **status:** TARGET
- **closure:** open

Let `N=2^41`, `K=rho N`, and let the official exact-list depth be

```text
t_XR=min{t>=0 : t log2(q) >= log2 binom(N,N-K-t)+128}.
```

After the quotient, dihedral, boundary, near-tail, and already priced trade
classes in the `x4` ledger are removed, prove

```text
# {non-coset-union t_XR-null blocks and unpriced trade families} <= N^3.
```

This is the exact consumer statement previously hidden inside
`u2c_giant_tnull_dichotomy`. It is not supplied by the generated-field-
guarded full-subset F2 terminal, because the proved route cut gives
`t_XR log2|F_p(mu_N)|<N` on every official row.
