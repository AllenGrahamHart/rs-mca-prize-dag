# Proof

Throughout, `zeta = zeta_2N` is a primitive `2N`-th root of unity; the
roots of `x^N+1` are `zeta^j` for the `N` odd residues `j (mod 2N)`,
and `Norm(f) = prod_{j odd mod 2N} f(zeta^j)`.

## Claim 1 (doubling embedding)

Let `N = 2M` and `f = iota g`, i.e. `f(x) = g(x^2)`. The coefficient
vector of `f` is that of `g` spread onto even indices, so ternariness
and weight are preserved. For the norm:
`zeta_2N^2 = zeta_N`, and as `j` runs over the odd residues mod `2N`
(there are `N` of them), `j mod N` runs over the odd residues mod `N`
(each hit exactly twice, since `zeta_N^{j+N} = zeta_N^j`). Hence

```text
Norm_N(f) = prod_{j odd mod 2N} g(zeta_N^j)
          = prod_{i odd mod N} g(zeta_N^i)^2
          = Norm_M(g)^2,
```

because `zeta_N = zeta_2M` and the odd residues mod `N = 2M` index
exactly the roots of `y^M + 1`. The corollary
`maxnorm(N,w) >= maxnorm(N/2,w)^2` follows by taking `g` to be a
lower-level argmax. QED

## Claim 2 (AM-GM ceiling)

Complex conjugation pairs the roots (`conj(zeta^j) = zeta^{2N-j}`, and
`j` odd iff `2N-j` odd, with `j != 2N-j` since `N >= 2`), so the `N`
factors of `Norm(f)` fall into `N/2` conjugate pairs and

```text
Norm(f) = prod_{pairs} |f(zeta^j)|^2 >= 0.
```

Negacyclic Parseval: the vectors `(zeta^{ji})_{i<N}` for the `N` odd
`j` are the rows of a scaled-unitary matrix (`sum_i zeta^{(j-j')i} = 0`
for `j != j'` odd, since `zeta^{j-j'}` is a nontrivial `2N`-th root of
unity whose order does not divide... precisely: `j - j'` is even and
nonzero mod `2N`, so `zeta^{j-j'}` is a nontrivial `N`-th root of
unity, and the geometric sum over `i < N` vanishes). Hence

```text
sum_{j odd mod 2N} |f(zeta^j)|^2 = N * ||f||_2^2 = N w
```

for ternary weight-`w` `f`. The `N/2` pair-values `P_j = |f(zeta^j)|^2`
therefore satisfy `sum P_j = Nw/2`, mean `w`, and AM-GM gives
`Norm(f) = prod P_j <= w^(N/2)`.

Lower bound: `x^N + 1 = Phi_2N` is irreducible over `Q`, and a nonzero
`f` of degree `< N` is not divisible by it, so no `f(zeta^j)` vanishes;
`Norm(f)` is a nonzero integer, and being non-negative it is `>= 1`.
QED

## Claim 3 (saturating family)

Base cases, exhaustive (replayed in `verify.py`): at `N = 4`,
`maxnorm = 1, 4, 9` at `w = 1, 2, 3`, attained by `1`, `1 + x^2`,
`1 + x - x^2` (up to symmetry) — each equal to `w^2 = w^(N/2)`. At
`N = 8`, `maxnorm(8,7) = 2401 = 7^4`, attained by
`[1,1,1,-1,-1,1,-1,0]`.

Induction on the power of two: if `maxnorm(M,w) = w^(M/2)` then
`maxnorm(2M,w) >= w^M` by Claim 1 and `maxnorm(2M,w) <= w^M` by
Claim 2, so equality holds at `2M`, with witness `iota` of the level-`M`
witness. QED

## Claim 4 (router threshold)

Suppose an admissible `q > w^(N/2)` carries a ternary relation of some
weight `w' <= w`. By the router there is a ternary `f` of weight `w'`
with `q | Norm(f)`. By Claim 2, `1 <= Norm(f) <= (w')^(N/2)
<= w^(N/2) < q`, so `q` cannot divide `Norm(f)`. Contradiction.

At `2N = 8`: `maxnorm(4,w) <= 9` for every `w` (exhaustive; also
`w^2 <= 9` for `w <= 3` and the full-weight value is `8`), while the
smallest prime `== 1 (mod 8)` is `17 > 9`. So the exceptional census at
`2N = 8` is empty. QED
