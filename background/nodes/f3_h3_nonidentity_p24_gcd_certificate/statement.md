# H3 nonidentity P24 gcd certificate

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence/router)
- **dependency:** `f3_h3_unordered_product_cutoff12_candidate_compiler`

Let `p=1 mod n`, where `n=2^s`, and reduce the unordered and diagonal
shifted-product polynomials to `F_p[T]`. Put

```text
G_12=gcd(Ucal_n^[0],Ucal_n^[1],...,Ucal_n^[12]),
G_12^neq=G_12/(T-1)^ord_(T-1)(G_12),
H_D=gcd(Delta_n,Delta_n^[1]),                       (P24G1)
```

with every gcd monic. Then the following are equivalent:

```text
max_(t!=1) P(t)<=24,
G_12^neq divides H_D.                              (P24G2)
```

More precisely, at every target `t`,

```text
ord_t(G_12)=max(U(t)-12,0),
ord_t(H_D)=max(D(t)-1,0),                          (P24G3)
```

where `P(t)=2U(t)-D(t)` and `0<=D(t)<=2`. Thus every root retained by
`G_12^neq` is harmless exactly when it has the sole boundary profile

```text
U(t)=13,       D(t)=2,       P(t)=24.              (P24G4)
```

A row certificate consists of monic gcd/divisor-plus-Bezout certificates for
`G_12`, the exact removed identity valuation, `H_D`, and the divisibility in
`(P24G2)`. It need not enumerate targets or materialize ordered product
pairs. This theorem supplies the exact checker contract; it does not construct
`Ucal_n` efficiently, list candidate primes, or prove the divisibility at any
official row.
