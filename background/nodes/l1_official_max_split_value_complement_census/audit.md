# Audit - L1 official maximal split-value complement census

1. `u=n-hp` is the complement degree at actual value degree `h`; `s=n-mp`
   is reserved for maximal capacity.
2. The complement compiler applies for every `2<=h<=m`; only its
   maximal-capacity specialization is excluded by polynomial abc.
3. `m<p` is supplied by official arithmetic and is needed in the leading
   coefficient and Newton divisions.
4. `Q=0` is excluded before defining `j=p-deg Q`.
5. The first nonleading term of `G(P)` is from `P^h`; the next outer term is
   a full gap `p` below the leader.
6. The normalization `P(0)=0` is load-bearing for uniqueness from `C`.
7. The Vandermonde count is an upper bound on valid split complements, not a
   claim that every selected root set extends to one.
8. The denominator `binom(u,ell_h)` uses squarefreeness of `C` and disjoint
   families of determining root subsets; it is not a probabilistic factor.
9. For lower `h`, the exponent `u-d+p` can grow with `p` and is not silently
   called polynomial.
10. The outer polynomial is depressed only because `h` is invertible in
    characteristic `p`; this removes its degree-`h-1` term.
11. The two nonmonomial summands have the same exact zero valuation before
    Mason--Stothers is applied.
12. The radical bound for the lower outer part uses its full degree and does
    not assume squarefreeness.
13. Failure of the Mason inequality enters the characteristic-`p` exception;
    that branch is retained rather than discarded.
14. `C` is squarefree because it divides the squarefree domain binomial, and
    all its roots are nonzero.
15. At a complement root, Frobenius degeneracy gives the exact congruence
    `h e_c+1=0 mod p`; no equality of coefficients is inferred from it.
16. The least residue is computed as `e_0=-m^(-1) mod p`, and the atlas
    verifies the integer inequality `s e_0>p` on every row.
17. On `h<m`, the Frobenius arm is impossible because `u>p`; the resulting
    valuation bound is structural and not itself a count.
18. Lower split-value degrees and higher tail widths remain explicitly open.
