# Proof

## 1. Complete normalization

Profile `(1,2,0)` has one folded coefficient in `{+2,-2}` and two distinct
folded coefficients in `{+1,-1}`. Multiply by a sign and a power of `zeta` so
that the coefficient of magnitude two is `+2` at exponent zero. Both factors
are cyclotomic units, so this preserves norm divisibility. Folding the two
remaining exponents across `zeta^(i+256)=-zeta^i` gives uniquely, up to
interchanging the singleton terms,

```text
F(X)=2+epsilon X^a+delta X^b,
1<=a<b<=255,       epsilon,delta in {+1,-1}.
```

This is exactly `4 binom(255,2)=129540` states.

## 2. Exact Galois quotient

The Galois group of `Q(zeta_512)` is the 256 odd residues modulo 512. For
each odd `u`, replace `(a,b)` by `(ua,ub) mod 512`, fold exponents at 256 with
the corresponding sign change, and sort the two singleton terms. This action
preserves `|Norm(F(zeta))|`.

The deterministic orbit partition in `verify.py` has 748 representatives and
orbit-size histogram

```text
2:2, 4:4, 8:10, 16:22, 32:46, 64:94, 128:190, 256:380.
```

The weighted sum is 129540, so no normalized state is omitted.

## 3. Exact norms

Since `Phi_512(X)=X^256+1`, for each representative

```text
R(F)=|Res_X(X^256+1,F(X))|=|Norm(F(zeta))|.
```

All 748 resultants are nonzero and yield 746 distinct norms. The canonical
row stream has SHA-256

```text
83b6b8c7bc1686177e7abd68c0328769a6360d3d0e12f6e3524ec8df32403ea7.
```

`verify.py` computes the stream with SymPy exact integer resultants and uses
every norm directly in the interval test. The independent FLINT replay in
`notes/flint_replay_modal.py` recomputes all resultants and the interval
screen, obtaining the same row and screen digests.

## 4. Interval divisor certificate

The only possible pair-feasible primes lie in

```text
I_C=[2^250,2^250+2^128-1],
I_P=[B_P 2^128,(B_P+1)2^128-1],
B_P=317494674775468773183020924238786383963.
```

Fix a norm `R` and one interval `[L,U]`. If a prime `p` in that interval
divides `R`, then `m=R/p` is an integer in

```text
ceil(R/U) <= m <= floor(R/L).                   (1)
```

Conversely, every such divisor `m` produces the only possible quotient
`p=R/m`. Thus enumerating the integers in (1) is an exact divisor test, not a
factorization heuristic.

Across the 746 distinct norms and two intervals, the 1492 windows contain
only four integers in total; the maximum width is one. Only one candidate
cofactor divides:

```text
state      = (1,129,-1,-1)
cofactor   = 64
quotient   = 1809251394333065553493296640760748560212660422383773476608139978364764028928
quotient mod 512 = 0.
```

The quotient is greater than 512 and divisible by 512, hence composite; it is
also not `1 mod 512`. The other three possible cofactors do not divide their
norms. Therefore no prime in either named interval with `p=1 mod 512` divides
any representative norm.

The collision-norm criterion excludes profile `(1,2,0)`. The folded-L2
classification says that `(1,2,0)` and `(0,4,0)` exhaust `N=512,s=2`, and the
four-singleton theorem excludes the latter. Hence every surviving collision
has `s>=3`.
