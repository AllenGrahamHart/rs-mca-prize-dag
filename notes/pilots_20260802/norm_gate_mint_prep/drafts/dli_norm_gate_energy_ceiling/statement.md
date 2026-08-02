# dli_norm_gate_energy_ceiling

- **status:** PROVED
- **closure:** proof
- **scope:** every NONZERO integer-coefficient element of
  `Z[zeta_n] = Z[x]/(x^h+1)`, `n = 2^s >= 4`, `h = phi(n) = n/2`. No
  ternariness, no weight restriction, no hypothesis on `q`.
- **provenance:** the ceiling is the banked
  `dli_c1_ternary_relation_norm_sandwich` **Claim 2** with the weight `w`
  replaced by the ENERGY `E = sum_i a_i^2`; the banked proof never used
  ternariness. Generalization identified, instrumented and cross-checked by
  the 2026-08-02 norm-gate pilot
  (`notes/pilots_20260802/dli_norm_gate/{REPORT,FABLE_AUDIT}.md`, lemma LN4;
  router LN5).

## Setting

`n = 2^s` with `s >= 2`, `h = phi(n) = n/2`,
`Z[zeta_n] = Z[x]/(x^h + 1)`, `Norm(alpha) = det(mult by alpha)
= prod_{j odd mod n} alpha(zeta_n^j)`. For
`alpha = sum_{i < h} a_i zeta_n^i` with `a_i in Z` define the **energy**

```text
E(alpha) = sum_{i < h} a_i^2 .
```

For a **ternary** `alpha` of weight `w` (all `a_i in {-1,0,1}`, exactly `w`
nonzero) `E = w`, so every statement below specializes to the banked one.

**Junction router setting (C2'' tower).** At junction `j` the root order is
`h_j = n/2^j`, the ambient ring is `Z[zeta_{h_j}]` of degree
`phi(h_j) = h_{j+1} =: N_j`, the constraint block is `U_j` with
`o = L_j = |U_j|`, and the skew element is
`delta = sum_{i < N_j} d_i zeta_{h_j}^i` with `|d_i| <= c_i` on the
effective (unsaturated) support `S_j`; at `j = 0` the domain is
`{+-1}^{S_0}`, so `E(delta) = |S_0|` exactly.

## Statement (both claims PROVED)

1. **LN4 (energy ceiling).** For every NONZERO
   `alpha = sum_{i<h} a_i zeta_n^i` with integer `a_i`:

   ```text
   1 <= Norm(alpha) <= E(alpha)^{h/2},      E(alpha) = sum_i a_i^2 .
   ```

   In particular `Norm(alpha) >= 0` always, and the ternary case
   `Norm <= w^{h/2}` is the banked sandwich Claim 2. **Ternariness is never
   used**: the only input is `sum_i a_i^2`, via negacyclic Parseval and
   AM-GM on the `h/2` conjugate-pair values.
2. **LN5 (junction router).** Fix a junction with root order `h_j`,
   degree `N_j = phi(h_j)`, block size `o = L_j`, and let `q` be admissible
   (`h_j | q - 1`, `q` odd). Combining LN4 with `q^{L_j} | Norm(delta) != 0`
   (`dli_norm_gate_forward_and_ofold`, Claim 3), every nonzero junction-`j`
   skew solution `delta` satisfies

   ```text
   q^{L_j} <= Norm(delta) <= E(delta)^{N_j/2},
   ```

   equivalently `E(delta) >= min{ E in Z_{>0} : E^{N_j/2} >= q^{L_j} }`.
   **Contrapositive (the router).** If `E^{N_j/2} < q^{L_j}` then NO nonzero
   junction-`j` skew solution of energy `<= E` exists; in particular a state
   whose entire admissible skew domain has `sum_{i in S_j} c_i^2 <= E` admits
   no nonzero solution at all. (Whether that also forces the junction's local
   ratio `rho_j` to vanish depends on whether the domain contains `d = 0`;
   that refinement is stated, with its scope, in
   `dli_official_support_forcing` Claim 4 and is NOT asserted here.)
   At the official uniform ratio `N_j = 256 L_j` the criterion collapses to
   `q <= E^128`, independently of `j` — that consequence and its official
   pricing are `dli_official_support_forcing`, not this node.

## Explicitly NOT claimed (context)

- **No lower bound beyond `1`.** LN4 says `Norm >= 1`; nothing here bounds
  `Norm` from below in terms of `E`. The exact per-weight maxima
  `maxnorm(N,w)` are the banked C1 ladder, and the "repaired doubling law"
  `maxnorm(N,w) = maxnorm(N/2,w)^2` in the stable range is a REFUTED
  conjecture in general (see the sandwich node's correction of record and
  `notes/pilots_20260802/c1_imprimitivity/`). This node uses only the AM-GM
  ceiling, which is unconditional.
- **Sharpness is a banked fact, not a claim here.** The ceiling is attained
  exactly at `w in {1,2,3}` (all `N >= 4`) and `w = 7` (all `N >= 8`) —
  banked sandwich Claim 3. The verifier reproduces those maxima; it does
  not re-prove the saturating family.
- **No claim that the router is the only obstruction.** A junction can be
  empty for reasons the norm gate does not see (alignment beyond
  divisibility, count bounds); LN5 is a one-sided exclusion.
- **No claim about which weights are reachable at the open WCL slots.**
  The associated fence law (`q > w^128` unconditional, `q > c_w^64` under
  the C1 doubling law, both independent of the window index) is recorded in
  the provenance pilot §5 and is a candidate separate node; it is NOT
  asserted here.

## Falsifier

A nonzero integer vector `a` of length `h = 2^{s-1}` with
`Norm(a) > (sum_i a_i^2)^{h/2}` or `Norm(a) <= 0`; or a junction-`j` skew
solution with `E^{N_j/2} < q^{L_j}`.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers, no
third-party imports). Checks: the exact integer form of negacyclic Parseval
(391,250 vectors) and the trace orthogonality behind it; the ceiling
exhaustively over `[-3,3]^4`, over all ternary vectors at `h = 8`, and on
4,000 deterministic `[-4,4]^8` samples; reproduction of the banked
per-weight maxima at `2N = 8, 16` (complete) and `2N = 32` (`w <= 3`
exhaustive, `w = 4,5,6` by the banked doubling witnesses); non-ternary
witnesses attaining the ceiling; the `256:1` collapse `q^o <= E^{128 o}`
`<=>` `q <= E^128` as an exact integer equivalence; and the LN5 router at
the real junction `(n,t,q,j) = (32,8,97,0)`, where all 4,992 ternary skews
of support `<= 3` are confirmed empty as predicted.
