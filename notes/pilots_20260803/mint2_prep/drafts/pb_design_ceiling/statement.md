# pb_design_ceiling

- **status:** PROVED
- **closure:** proof
- **scope:** the ceiling is a rank inequality, valid at every scale; its
  hypothesis (**ray-block independence**) is load-bearing and is NOT
  automatic — a realised, spread, zero-collision counterexample to the
  unconditional reading is exhibited and machine-replayed here. The
  six-row table is exact integer arithmetic at the pinned official
  parameters. The forcedness corollary is arithmetic on top of the
  proved (prescribed-slope) form only.
- **provenance:** P-B (H4) hunt pilot,
  `notes/pilots_20260802/pb_h4_hunt/{REPORT.md:14,29,31,47,48, FABLE_AUDIT.md:9-14,48}`
  (`expC.py` stages `lemma`/`rank`/`plant`/`orbit`/`extend`, checkpoints
  `EXPC_lemma.json` 1599/1599, `EXPC_rank.json`, `EXPC_plant.json`,
  `EXPC_orbit.json`, `EXPC_extend.json`, `OFFICIAL.json`), consumed at
  `notes/pilots_20260802/rowc_window/FABLE_AUDIT.md:29-35` and named in
  the P-B TARGET's scope addendum (`dag.json`, `xr_lowcore_spread_heart`,
  2026-08-02 bundle clause (c)).
- **SUBTRACTION (hard law 5) — read before citing this node.** The rank
  MECHANISM is already banked and is **cited, not re-derived**:
  - **(L1)** `dim C_S = |S|-K`, `dim(C_S ^ C_T) = max(0, |S^T|-K)` —
    proved verbatim at
    `background/nodes/xr_two_slope_cost_theorem/proof.md:7-23`
    (statement `:23-25`). The P-B lane's "L1 lemma" **is this lemma**
    (symbol `K` here, `k` there); it is NOT re-minted.
  - **(L2)** `RS_K x RS_K` lies in every condition kernel, so a
    non-degenerate realisation forces `rank <= 2(n-K)-1` — proved at
    `background/nodes/xr_two_slope_cost_theorem/proof.md:96-108`.
  - the **per-ray ceiling** `V <= (2(n-k)-1)/h` and the six-row values
    `307/358/639 / 383/447/959` are banked at
    `background/nodes/xr_two_slope_cost_theorem/{statement.md:74-91, proof.md:110-136}`.

  **What is NEW here** is only: the P-B (single-support, spread-family)
  gauge; the explicit independence hypothesis with its machine
  refutation; the free-slope per-support form and its honest status; and
  the **forcedness corollary** against the P-B budget `8n^3`.

## Setting

`RS_K` on a domain `D` of `n` distinct points of `F_q`; `A = K + h` the
selected support size; `r := n - K`. For `|S| >= K`,
`C_S = {c : supp(c) inside S, c _|_ RS_K}`, `dim C_S = |S| - K = h` for
`|S| = A` (L1).

A **received pair** is `(u,v) in F_q^n x F_q^n`. A **witness** (P-B's
object; `pb_h4_hunt/core.py:4-13`) is a support `S`, `|S| = A`, together
with a slope `z` such that `(u + z v)|_S in RS_K|_S`; equivalently

```text
(R_{S,z})   <c, u> + z <c, v> = 0    for every c in C_S      (h rows).
```

The row block is `G_z(C_S) = {(c, zc) : c in C_S}`, `dim = h`. A
**ray** is a pair `(z, S)`. A family `{(z_a, S_a)}_{a=1..M}` is **spread**
iff `|S_a ^ S_b| <= K-1` for all `a != b`.

**Lemma 0 (transversality — CORRECTED; one line from banked L1).**
`C_{S_a} ^ C_{S_b} = 0` **iff `|S_a ^ S_b| <= K`**. Consequently

```text
spread  (all cores <= K-1)   ==>   pairwise transversality,
```

and **the converse is FALSE**: pairs at core exactly `K` are transverse
without being spread. *(The P-B lane states this as an equivalence —
"spread <=> pairwise-transverse condition spaces (dual distance K+1)",
`pb_h4_hunt/REPORT.md:29`. As written that is one-directional; the exact
equivalence is with `<= K`. The gap is the core-exactly-`K` stratum,
which is `Gamma_hi` for the P-B budget, so the distinction is
load-bearing for the lane. Corrected here, with machine witnesses — see
AUDIT_CHECKLIST F3.a. It is a corollary of the banked lemma, not a new
lemma, and is minted INLINE rather than as a separate node — F0.a.)*

**Ray-block independence.** The family is **independent** iff

```text
dim ( sum_{a=1..M} G_{z_a}(C_{S_a}) ) = M h,
```

i.e. the `Mh` rows `(R_{S_a,z_a})` are linearly independent. **Spread does
NOT imply independent** (Theorem 3).

## Statement

1. **THEOREM 1 (design ceiling, prescribed slopes — PROVED).** Let
   `{(z_a, S_a)}_{a=1..M}` be **independent** and realised by a pair
   `(u,v) NOT in RS_K x RS_K`. Then

   ```text
   M h <= 2(n-K) - 1 = 2r - 1,      i.e.   M <= (2r-1)/h.
   ```

   Exact six-row values `floor((2r-1)/h)` (recomputed by the verifier):

   ```text
   RowC  1/4, 1/8, 1/16 :  307 / 358 / 639
   prize 1/4, 1/8, 1/16 :  383 / 447 / 959
   ```

   (Row pins: RowC `n = 1024`, `K = 256/128/64`, `h = 5/5/3`; prize
   `n = 2^41`, `K = 2^39/2^38/2^37`, `h = 2^33+1 / 2^33+1 / 2^32+1`.)
2. **COROLLARY (forcedness of any P-B counterexample — PROVED).** A P-B
   counterexample is a realised family with more than `8n^3` members
   (`|Gamma_lo| > 8n^3`, the TARGET's budget). By Theorem 1 at most
   `floor((2r-1)/h) <= 959` of its members can carry independent
   condition blocks — **at most ~960 at every one of the six official
   rows**, against budgets `8n^3 = 2^33` (RowC) and `2^126` (prize).
   Hence

   ```text
   #independent / #members  <=  960 / 8n^3  <=  2^-23.68 ,
   ```

   so **any P-B counterexample is at least `1 - 2^-23` FORCED**: all but
   a `2^-23`-fraction of its members have condition blocks implied by the
   others. Per-row margins (bits below budget, `lg(8n^3) - lg(ceiling)`),
   computed from the **proved** prescribed-slope ceiling:
   `24.74 / 24.52 / 23.68` (RowC) and `117.42 / 117.20 / 116.09` (prize).
   *(The pilot quotes `2^23.1 .. 2^117.4`, computed from the free-slope
   number `383/447/959`; those are `24.42 / 24.20 / 23.09` on the RowC
   triple. The proved form gives the slightly BETTER margins above.
   Either way the headline `<= ~960` and `>= 1 - 2^-23` stand — see
   AUDIT_CHECKLIST F3.b.)*
3. **THEOREM 2 (the free-slope form — NOT PROVED, recorded).** With
   slopes free, each witness is `h-1` determinantal conditions (the
   `2 x h` syndrome matrix has rank `<= 1`), which SUGGESTS
   `M <= (2r-1)/(h-1)` = `383/447/959` on **both** triples. This is the
   number the pilot headlines (`pb_h4_hunt/REPORT.md:14`), and its own
   source calls it "the determinantal count" / "the true ceiling SHOULD
   be" (`expC.py:19-21, 352-364`). **It is a dimension heuristic, not a
   theorem**: the general-position step (that the `M` determinantal loci
   meet properly) is exactly what Theorem 3 refutes in the independent
   reading. The banked node's proved table contains
   `floor((2r-1)/(2h-2)) = 191/223/479` (the per-DATUM form, a datum
   being two supports), not `floor((2r-1)/(h-1))`; and note
   `2 * 191 = 382 != 383`, so the two are not the same integer.
   **The forcedness corollary above does NOT use this form** — it is
   derived from Theorem 1 alone, and the headline `<= 960` and
   `1 - 2^-23` survive under either reading (both maxima are 959).
4. **THEOREM 3 (the independence hypothesis is necessary — REFUTATION,
   PROVED by exhibit).** At `n = 20`, `q = 41`, `K = 4`, `h = 3`
   (`A = 7`, `r = 16`, `2r = 32`), the monomial pencil
   `U = X^A`, `V = -X^{A-1}` on `D = mu_20` has a `mu_20`-invariant
   witness set which contains a **full orbit of `M = 20` supports** that
   is
   - **spread** (max pairwise core `3 = K-1`, so **zero
     self-collision**), and
   - **realised** by the non-degenerate pair `(u,v)`, with condition
     rank `31 = 2r - 1` out of `M h = 60` rows (deficit `29`), carrying
     `20` distinct slopes.

   So `M = 20` exceeds the prescribed-slope ceiling `10` and the
   free-slope ceiling `15`. **The ceiling bounds only families whose
   conditions are independently imposable, never realised families as
   such**; and **"rank deficit forces self-collision" is FALSE**
   (`pb_h4_hunt/REPORT.md:14, 29, 48`: "F2 — FIRES, decisively"). The
   saving observation, recorded not claimed: that class buys **deficit
   without excess** (40 witnesses against a mean supply of 46.1).

## Explicitly NOT claimed (context)

- **No P-B bound.** Nothing here bounds `|Gamma_lo|`. The pilot is
  explicit: "Nothing here is proved about P-B; the ceilings, L1, the
  dichotomy, and the exhaustive maxima are exact; the discharge of (H4)
  is not" (`pb_h4_hunt/REPORT.md:63`).
- **The ceiling does NOT discharge (H4)** and must never be cited as a
  lane-closer (Theorem 3).
- **L1 is NOT minted here** — it is banked (see SUBTRACTION above). Any
  consumer wanting the shortened-dual lemma must cite
  `xr_two_slope_cost_theorem`.
- **The free-slope ceiling is NOT claimed** (Theorem 2), and it was NOT
  attained in the pilot's own extension test (`EXPC_extend.json`:
  `max_greedy_spread = 12` against a free ceiling of `15`).
- **Gauge-invariance scope correction (carried, not proved here).**
  Strip/genericity gates read off the WORDS are vacuous under degree-`<K`
  gauge; they must be stated on `(alpha, beta)` modulo `RS_K`
  (`pb_h4_hunt/REPORT.md:23`, adopted at `FABLE_AUDIT.md:37-40`). This
  node's statement is gauge-safe because it speaks only of `C_S` and the
  condition rows, both of which are `RS_K`-quotient objects.
- **No claim that the design space is exhausted.** The pencil-model
  exhaustion is a `2h`-dimensional slice of the `2(n-K)`-dimensional word
  model — "the single largest gap in the 'no other geometry' claim"
  (`pb_h4_hunt/REPORT.md:57`).
- **The SELECTOR CATCH is not resolved here**: `Gamma_lo = 0` for
  split-fibre is a joint identity-plus-support-keyed-selector statement,
  not an identity consequence (`pb_h4_hunt/REPORT.md:43`,
  `FABLE_AUDIT.md:26-36`). See `pb_block_dichotomy`.

## Falsifier

An independent, non-degenerately realised family with `Mh > 2(n-K)-1`;
or an exact-integer failure of the six-row table; or a demonstration that
the exhibited `mu_20`-orbit is not spread / not realised / not of size 20
(which would restore the unconditional reading of Theorem 1).

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, no reads outside this directory —
all pins inlined, provenance paths in comments only). Checks: (A) a fresh
replay of banked L1 (`dim(C_S ^ C_T) = max(0,|S^T|-K)`) at four shapes,
matching `EXPC_lemma.json`'s 1599/1599 pattern; (B) Lemma 0 (spread iff
pairwise transverse); (C) the rank law `rank = min(Mh, 2r)` on random
spread prescribed-slope families and the attainment pattern of
`EXPC_rank.json` (`M = 10` leaves a non-codeword solution, `M = 11` does
not); (D) the six-row ceiling table as exact integers, both the proved
`floor((2r-1)/h)` and — labelled NOT-PROVED — `floor((2r-1)/(h-1))` and
`floor((2r-1)/(2h-2))`, including the `2*191 != 383` observation;
(E) the forcedness arithmetic (`8n^3`, `<= 960`, the six bit-margins);
(F) THEOREM 3 rebuilt from scratch — the monomial pencil, ALL 77,520
`7`-subsets scanned exhaustively, the orbit decomposition, spreadness,
distinct slopes, and the rank `31` of `60` against `2r = 32`.
