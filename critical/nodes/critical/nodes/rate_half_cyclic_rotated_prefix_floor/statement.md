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

## OPTIMIZED RE-INSTANTIATION (wave-10 audited, 2026-07-18; c=2^33, d=1 — the k+2^34 reach)


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

For the prize-max rate-half row, take

```text
n=2^41,       k=2^40,
c=2^33,       N=256,
d=1,          m=129,
s=c-1.
```

Then `(CR1)` is the field-independent integer

```text
L_cyc = ceil(C(255,129)/256) > 2^238,
```

and `(CR2)` has excess

```text
sigma_cyc = dc+s = 2^34-1 = 17,179,869,183.              (CR3)
```

Since `q<2^256`, the prize list threshold satisfies
`floor(q/2^128)<2^128<L_cyc`. Thus ordinary and constant common-support
interleaved lists are unsafe at `k+sigma_cyc`; radius monotonicity gives the
full interval

```text
1 <= sigma <= 2^34-1.                                    (CR4)
```

Equivalently, the general cap criterion

```text
N q^d < 2^128 C(N-1,m)                                   (CR5)
```

holds at the artificial endpoint `q=2^256` with more than `114` bits of
margin.

Among maximal-prefix instances `s=c-1` of `(CR1)` whose lower bound is
certified uniformly by checking `(CR5)` at `q=2^256`, this is the unique
largest agreement excess. This extremality is only for the printed cyclic
construction and cap-uniform criterion; it is not an upper bound on arbitrary
received words.

This theorem makes no MCA/CA claim and no safe-side list claim.

## Historical specialization

The earlier choice `c=2^22`, `d=2048`, `s=c-1` reached excess
`8,594,128,895`. It remains valid but is strictly superseded by `(CR3)`.
