# L1 Mersenne HNF m=8 aggregate norm-gcd compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** fixed univariate `d` endpoints on every official `m=8` row

Let `p` be an official characteristic, let `K/F_p` contain `mu_8`, and let
`P(X) in F_p[X]`. Then

```text
product_(zeta in mu_8)(X^(p+1)-zeta)=X^(8(p+1))-1. (ANG1)
```

Consequently

```text
gcd_(F_p[X])(P,X^(8(p+1))-1)=1                     (ANG2)
```

if and only if

```text
gcd_(K[X])(P,X^(p+1)-zeta)=1
for every zeta in mu_8.                             (ANG3)
```

Thus a fixed univariate norm endpoint needs four aggregate gcd rows, one per
official prime, rather than 32 color rows. A nonunit aggregate gcd is only a
hit router: split it by `zeta` over `K` and apply all remaining packet
conditions. No aggregate or individual gcd verdict is asserted here.
