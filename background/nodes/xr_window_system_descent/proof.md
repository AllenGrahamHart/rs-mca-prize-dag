# Proof

## Window Lemma

If `f` agrees with `u` on `H\T`, then `E_T(u-f)` vanishes on all of
`H`, hence is divisible by `X^n-1`. Therefore

```text
uE_T mod (X^n-1) = fE_T,
```

whose degree is `<k+r'=n-d`; the top `d` coefficients vanish.
Conversely, if those coefficients vanish, the same remainder has
degree `<n-d` and is divisible by `E_T`, because both `uE_T` and
`X^n-1` are. Its quotient has degree `<k` and agrees with `u` off
`T`. Uniqueness follows from interpolation on `k+d>=k` points. Apply
the argument separately to `u` and `v` for the joint system.

## Descent

A subset of `mu_n` is a union of `mu_M`-cosets if and only if its
monic locator is invariant under `X -> zeta X` for every
`zeta in mu_M`; equivalently it is `G(X^M)`. In the coefficient of
degree `j` of `uG(X^M)`, only coefficients of `u` congruent to `j`
modulo `M` occur. Thus the equations split by residue class. Retaining
one class and writing `Y=X^M` gives exactly the quotient instance,
including a bijection of its monic divisors. This is an algebraic
bijection, not a counting heuristic.

## Rank

A dependence among the `d` Toeplitz rows is a linear recurrence of
order at most `d-1` across the complete syndrome segment
`u_k,...,u_{n-1}`. Since `n-k>=2d` in the stated band, the usual
Berlekamp-Massey correspondence gives an error locator of degree at
most `d-1`. Hence `u` is within distance `d-1` of `RS_k`, so it has a
codeword agreement at least `n-d+1>A`, contradicting the tangent gate.
The rank is therefore `d`. On `E_T=G(X^M)`, the matrix is block
diagonal by residue classes; the one-class quotient block has rank
`d/M`, and any nonzero extra block has positive rank. This proves only
the stated single-word ranks. Stacking the `u` and `v` systems need
not double rank.

## Liveness

For individually residue-supported words, an extra agreement in one
quotient fiber solves an equation `x^(b-a)=c` inside a `mu_M`-coset.
It therefore contributes either zero or
`g=gcd(M,b-a)` points. There are at most
`m=(n-k-d)/M` available quotient fibers outside the core. Exact-`A`
liveness requires `h-d` extra points. Because `M` is a power of two,
`g` is a power of two; because `M|d` and `h` is odd, `h-d` is odd.
Thus `g=1` and `h-d<=m`, which is `(L)`. The official-row endpoint
arithmetic is checked exactly by `verify.py`; monotonicity between
successive multiples of `M` reduces each scale to its largest allowed
depth.
