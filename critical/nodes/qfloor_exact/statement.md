# qfloor_exact

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Let `D <= F_p^*` have order `n`, let `C = RS[F_p,D,k]` with
`k = rho n`, and let `N' | n` satisfy `rho N' in Z`. Put

```text
ell' = rho N' + 1,   sigma = n/N',   Q = D^sigma.
```

If `p = 1 mod n` and

```text
p > (2 ell')^(N'/2),
```

then the canonical line `x^(k+sigma) + z x^k` at radius
`1-rho-1/N'` has exactly `Acl(N',ell')` distinct quotient-value slopes.

This theorem is prime-field and above-threshold. It makes no claim for an
extension-field row, for a row below the norm threshold, or for a different
agreement endpoint without an explicit monotonicity calculation.
