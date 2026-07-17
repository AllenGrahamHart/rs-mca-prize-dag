# Rate-half cyclically rotated prefix floor

- **status:** see `dag.json` (single source of truth)
- **consumer:** rate-half list adjacency
- **object:** ordinary and common-support interleaved Reed-Solomon lists

Let `F` be a finite field of size `q`, let `D` be a multiplicative coset of
order `n`, and put

```text
C = RS[F,D,n/2].
```

Let `c` divide `n/2`, put `N=n/c`, and fix an `s`-subset `T_0` of one
`c`-point fiber of `x -> x^c`, where `0<s<c`. For

```text
1 <= d <= N/2-1,                 m=N/2+d,
```

there is a received word with at least

```text
ceil(C(N-1,m)/(N q^(d-1)))                              (CR1)
```

distinct codewords agreeing on exactly

```text
n/2+d*c+s.                                               (CR2)
```

The same lower bound holds for every constant common-support interleaving
arity: repeat the received word and each codeword diagonally.

For the rate-half cap row

```text
n=2^41, k=2^40, sigma*=8,592,912,738,
c=2^22, d=2048, s=2,978,146,
N=524,288, m=264,192,
```

the agreement in `(CR2)` is `k+sigma*`. It is ordinary-list and interleaved-
list unsafe whenever

```text
N q^d < 2^128 C(N-1,m).                                  (CR3)
```

Condition `(CR3)` holds even at `q=2^256`, and hence for every admissible
field under the official cap `q<2^256`. Radius monotonicity propagates the
witness through the full residual band

```text
2^33 < sigma <= sigma*.
```

This theorem makes no MCA/CA claim and no safe-side list claim.

## MAXIMAL-PREFIX INSTANTIATION (wave-9 audited, 2026-07-17)

The s = c-1 instantiation: the cyclic construction's count is
s-INDEPENDENT, so the maximal prefix realizes the same deep list at
excess sigma_max = sigma_0 = 8,594,128,895 — the proved unsafe band is
1 <= sigma <= sigma_max (superseding the former sigma* upper end as the
proved reach; sigma* history preserved above). Verifier updated to the
pin version (cap arithmetic with the old_sigma+1 <= sigma assert).
