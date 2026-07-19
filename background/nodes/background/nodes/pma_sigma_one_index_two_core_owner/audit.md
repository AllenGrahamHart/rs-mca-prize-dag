# Audit - PMA sigma-one index-two near-core owner

## Checks

1. **Source-level predicate.** `A_P` is the full agreement set against the
   original received word. No PMA chart data enters the owner.
2. **Enough interpolation points.** When the core contributes fewer than `k`
   points, listedness supplies at least `q_e+1` outside agreements; retaining
   `q_e` reaches exactly `k` points.
3. **Injectivity, not candidate counting.** Two codewords with one owner agree
   with the same word on at least `k` points, so Reed-Solomon uniqueness applies.
4. **Disjoint payment.** `QOWN_core4` is applied only after `QOWN_per`; the
   combined inequality adds disjoint first-match classes.
5. **Correct scale.** The owner uses the two size-`n/2` cosets. It does not
   claim that these trivial-stabilizer agreement sets are periodic.
6. **Exact finite absorption.** The proof bounds the owner by `Q_2(k+2)` and
   combines it with the sharper `4(1+2^-690)Q_2+3` periodic count. It does not
   reuse the full `719Q_2` bound twice.
7. **Construction subsumption.** The reciprocal-quadratic family visibly
   contains `G\({b} union D)` in every full agreement set, with four misses.
8. **Finite/asymptotic firewall.** Only the interpolation formula is general;
   the `Q_2` absorption is stated on the official `sigma=1` grid.

## Mutation guard

The verifier constructs two distinct degree-`<4` polynomials that agree with
one word on the same three-point near-core but on disjoint outside pairs. If
the owner retains `q_e-1` outside points, the owners collide. Retaining the
printed `q_e` separates them and supplies four interpolation points.

## Nonclaims

The theorem does not prove a bound on the post-owner diffuse incidence,
`d>=4`, chart composition, or the asymptotic residual. It removes the explicit
reciprocal-quadratic obstruction from those obligations; it does not close
`pma_wide_residual`.
