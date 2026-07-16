# DLI primitive matching truncation majorant

- **status:** PROVED
- **consumer:** `dli_prime_weighted_large_block_support`
- **dependencies:** `dli_full_spectrum_polymer_majorant`, the Newton
  short-window exclusion, the terminal weight-3/4 ambient exclusions, and
  the ell-two weight-five norm-gcd exclusion

At one DLI level, let the primitive signed relations have activities
`z(c)=2^(-|supp(c)|)`, total activity

```text
P=sum_c z(c),
```

and independence polynomial `I`. Suppose every primitive relation has support
at least `w_0`, and put

```text
K=floor(N/w_0),
Exp_K(x)=sum_(m=0)^K x^m/m!.
```

Then

```text
Z <= I <= (1+P/K)^K <= Exp_K(P).                 (MT1)
```

Consequently, for every raw primitive ledger `W_full>=P`,

```text
E_j <= r_j (1+W_full,j/K_j)^K_j.                 (MT2)
```

On the official production tower `N_j=256 ell_j`, the proved exclusions give

```text
ell=1:   w_0=5,          K=51,
ell=2:   w_0=6,          K=85,
ell=4:   w_0=9,          K=113,
ell>=8:  w_0=2ell+1,     K=floor(256ell/(2ell+1))<=127.  (MT3)
```

Thus the full marginal baseline follows from the strictly weaker pressure
budget

```text
sum_j K_j log(1+W_full,j/K_j)
  <=100 log(2)+t log(2^256/q).                    (MT4)
```

This replaces the fenced relaxation `I<=exp(W_full)` by the first rigorous
support-conflict correction. The intermediate truncated exponential remains
a valid but weaker bound. This node does not assert `(MT4)`, bound the full
raw ledgers, prove C2'', or close B-WEAK.
