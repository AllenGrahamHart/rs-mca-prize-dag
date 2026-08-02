# dli_c1_ternary_relation_norm_sandwich

- **status:** PROVED
- **closure:** proof

## Setting

`N` a power of two, `R_N = Z[x]/(x^N+1) ~ Z[zeta_2N]` (with `x^N+1` the
cyclotomic polynomial `Phi_2N`, irreducible). A polynomial `f` is
*ternary of weight w* if its coefficients lie in `{-1,0,1}` with exactly
`w` nonzero. `Norm(f) = Res(f, x^N+1) = det` of multiplication by `f`
on `R_N`. A prime `q` is *admissible* if `q == 1 (mod 2N)`; by the
banked relation-side router (2026-08-01 C1 pilot,
`notes/pilots_20260802/c1_doubling_orbits/`), an admissible `q` carries
a ternary weight-`w` relation on an order-`2N` root `omega` in `F_q^*`
iff `q | Norm(f)` for some ternary `f` of weight `w`; `Norm(f)` is
`q`-independent. Write `maxnorm(N,w)` for the maximum of `Norm(f)` over
ternary `f` of weight `w`.

## Statement (all four claims PROVED)

1. **Doubling embedding.** For `N = 2M`, the map
   `iota: g(y) -> g(x^2)` embeds `R_M -> R_N`, preserves ternariness
   and weight, and squares the norm:
   `Norm_N(iota g) = Norm_M(g)^2`. Hence
   `maxnorm(N,w) >= maxnorm(N/2,w)^2` for every `w`.
2. **AM-GM ceiling.** For every NONZERO ternary `f` of weight `w`:
   `1 <= Norm(f) <= w^(N/2)`.
3. **Saturating family.** `maxnorm(N,w) = w^(N/2)` for
   `w in {1,2,3}` at every `N >= 4`, and for `w = 7` at every
   `N >= 8` (all `N` powers of two). Witnesses: iterated `iota`-images
   of the exhaustive argmaxes at `N=4` (`w<=3`) and `N=8` (`w=7`,
   argmax `[1,1,1,-1,-1,1,-1,0]`, norm `7^4 = 2401`).
4. **Unconditional router threshold.** Any admissible prime
   `q > w^(N/2)` carries NO ternary relation of weight `<= w`. In
   particular at `2N = 8` no admissible prime carries any ternary
   relation at all (`maxnorm = 9 < 17 = ` smallest admissible prime).

## Explicitly NOT claimed (context)

The repaired doubling law `maxnorm(N,w) = maxnorm(N/2,w)^2` for
`w <= N/2 - 1` is VERIFIED at four ladder points for `w <= 6`
(exhaustive through `2N = 64`) but is a CONJECTURE in general — the
"imprimitivity conjecture" (the norm-maximising ternary `f` is
`iota`-imprimitive below `w = N/2`), recorded in
`notes/pilots_20260802/c1_norm_ladder/`. The one-constant
`c_w^(N/4)`-from-the-bottom law is REFUTED there (`w=4`: 196 vs 64;
`w=8`: 14760962 vs 2176^2), and `c_6 = sqrt(1154)` shows the stable
base need not be rational.

**[2026-08-02 CORRECTION OF RECORD: the imprimitivity conjecture is
REFUTED.]** Exhaustive at `2N = 64, w = 11 <= N/2 - 1`:
`maxnorm = 34921634364102721 = 186873311^2 >
184497889^2 = maxnorm(2N=32, 11)^2`, ratio 1.0259, argmax primitive
(support {0,1,2,6,7,9,11,12,16,17,18}, mixed parity), coordinator-
replayed by sympy resultant. Certified primitive beats also at
`w = 12, 14, 15, 16` (lower bounds); the doubling law HOLDS
exhaustively at `2N = 64` for `w <= 10` and at `2N = 128` for
`w <= 6` (+ `w = 7` by this node's sandwich). Break weights are
`3, 7, 10` at `N = 8, 16, 32` — NOT `N/2` in general. None of the
four PROVED claims above is affected. See
`notes/pilots_20260802/c1_imprimitivity/{REPORT,FABLE_AUDIT}.md`.

## Provenance

Discovered and exhaustively instrumented by the 2026-08-02 C1
norm-ladder pilot (`notes/pilots_20260802/c1_norm_ladder/REPORT.md`,
coordinator audit in `FABLE_AUDIT.md` alongside). Verifier:
`verify.py` in this node (exhaustive Lemma checks at `N = 4, 8`;
sandwich witness replay to `N = 16, 32`; router spot checks).
