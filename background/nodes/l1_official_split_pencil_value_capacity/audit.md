# Audit - L1 official split-pencil value capacity

1. Fibers for distinct values are disjoint as sets, not merely disjoint after
   a first-owner convention.
2. Every counted member has exactly `p` roots because it is monic of degree
   `p` and fully split with distinct roots.
3. The count uses ordinary integer cardinalities; the identity `p=0` inside
   the field is irrelevant.
4. The official strict inequality `p>n/24` is what turns `floor(n/p)` into
   23 rather than 24.
5. The pair count is unordered. An oriented ledger may use the corresponding
   cap `23*22=506`.
6. Normalizing `Q(0)=0` removes the constant-shift ambiguity without changing
   any fiber.
7. No computation or heuristic estimate is load-bearing.
8. The result removes `(b,c)` only after `Q` is fixed; it does not count the
   surviving perturbations.
9. Polynomial division is over `F[T][Z]` and is valid because `P-T` is monic
   in `Z`; no factorization of the ambient field is assumed.
10. The weighted degree bound counts `T` with weight `p`, so every eliminant
    coefficient has `T`-degree at most `floor(n/p)<=23`.
11. A common remainder root lies in `F`: divisibility puts every root of
    `P-beta` in `H`, and then `beta=P(x)`.
12. Squarefreeness of `G_Q` uses squarefreeness of `Z^n-alpha`; the latter
    holds because the characteristic is odd and `n` is a power of two.
13. The rank test is one-way. Rank at most `m-1` does not by itself prove
    that the coefficient polynomials have a common quadratic factor.
14. The low-complement argument uses `m=2`; it is not asserted for
    `n>=3p`.
15. In the band `2p<=n<3p`, the complement degree `s=n-2p` is positive for
    an odd characteristic and a power-of-two domain order.
16. The leading-gap contradiction uses strict `r+s<p`. Equality is retained
    in the surviving band.
17. The factor `G_Q(P)` has nonleading degree at most `p+r`; cancellation can
    only lower it and cannot invalidate the proof.
18. The complement map is injective only for unordered pairs; changing
    `delta` to `-delta` swaps the two fibers.
19. The constant in `D=R^2+c` is nonzero for a genuine pair, since otherwise
    the square would not be a squarefree divisor of the domain polynomial.
20. The uniqueness proof uses odd characteristic through the leading
    coefficient two in `R_1+R_2`.
21. The raw `binom(n,n-2p)` cap can still be exponentially too large. The
    theorem's main use is the square-quotient compiler and removal of an
    independent `Q` axis.
22. Polynomial abc is applied only after dividing the exact common power
    `Z^(2nu)`; the reduced three terms are pairwise coprime.
23. The characteristic-`p` exception is load-bearing. The reduced identity
    in the `F_9` fixture consists entirely of cubes, so applying the
    characteristic-zero abc conclusion would be false.
24. Frobenius degeneracy gives `p|(n-2nu)`; together with
    `0<2nu<=s<p` this forces `2nu=s`, not merely a congruence.
25. Squarefreeness of the complement turns the p-th power in `(8)` into the
    degree bound `s<=2`.
26. The exact `n/2` count is by antipodal complements, not by arbitrary
    two-point subsets.
27. The explicit family concerns only widths `t=p` and depths `p,p+1`.
