# The anticode branch of rank eleven: rank-one paid, rich-flat terminal

- **status:** PROVED (three stacked payments/route cuts; zero deployed
  ledger movement; rank eleven itself remains unpaid)
- **source:** upstream PRs `#1171` (head `a3fc2d5ae`), `#1172` (head
  `193b7bf99`), `#1173` (one commit on `#1172`), all scottdhughes,
  2026-08-15, stacked on the `#1168` head `6a5dcda`.
- **wired:** 2026-08-17 coordinator sweep; every envelope identity
  independently recomputed (`verify.py`).
- **consumer:** `rate_half_band_crossing_location` (evidence).

## The three results (post-near affine-error-rank-11 family)

1. **`#1171` — anticode classification.** Writing each actual
   minimizing pair as a `2 x s` coefficient matrix (`s <= 10`), every
   pairwise-rank-one family falls into exactly two bilinear clique
   geometries: fixed right factor (one affine correction ray) or fixed
   left factor (one affine correction space, dimension `<= 10`).
   The fixed-right branch is paid uniformly: the common-core-aware ray
   count over all `1048576` legal core sizes has exact maximum
   `8147918` at universal core `K-1` (their own hostile-scope audit
   caught and repaired the identically-zero-error import defect).
   Fixed-left properness gives `<= 1031` selected slopes per
   arrangement, else an explicit positive-dimensional affine-linear
   correction component is emitted.
2. **`#1172` — the rank-one branch is PAID.** At support-margin cutoff
   `tau = 439`: low rank-one branch `32215263489919749` + high-margin
   tail `242314927584173240` + near add-back `134944` =
   `274530191074227933`, slack `450537037167154`; cutoff `438` is over
   budget by `96628092421444`, so `439` is the first paying cutoff;
   the envelope minimum is `81826485385525648` at `tau = 3608`.
   NEW RESIDUAL: every over-budget rank-11 line forces two low-margin
   pair types with `rank(M_e - M_f) = 2`, `|H_e|, |H_f| >= 1115609`,
   `|H_e cap H_f| >= 134066` — the endpoint-difference polynomials
   share a squarefree deployed locator of degree `>= 134066`.
3. **`#1173` — anchored rich flats.** Anchoring one low-margin record
   and partitioning by the row space of the coefficient-matrix
   difference: rank-one groups paid by the `#1171` cap, rank-two by
   the dimension-two interleaved pair-list cap, provided no proper
   annihilator flat is heavy. At the optimized cell
   `(tau, h) = (1547, 42452)`: rank-one `60010642445729852` + rank-two
   `146093034425737644` + anchor `982651` + high tail
   `68875044016173272` + near `134944` = `274978720888758363`, slack
   `2007222636724`; `h = 42453` is over budget by `17108854816460`,
   and `42452` is the global maximum payable threshold (attained at
   cutoffs 1547-1549). TERMINAL: every over-budget line emits a
   represented row space `U` (rank 1 or 2) inside a strictly larger
   direction subspace `W <= C'` whose every polynomial vanishes on
   `>= 42453` common actual columns — the HEAVY RICH FLAT.

## Program connection (coordinator analysis, banked with this import)

Scott's stack and the local K'-ladder are complementary
stratifications of the same `#1168` residual: by pair-difference rank
(algebraic) versus by component row `K'` (geometric). Their residuals
converge on three objects:

- the `#1172` shared-locator edges (`deg >= 134066` common squarefree
  factor) are the exact use case of the banked common-core shortening
  adapter (`rate_half_kb_common_core_shortening_adapter_staircase_import`;
  applied to rank-11 seeds in
  `rate_half_mca_rank11_order32_common_support_cancellation`):
  many edges sharing one locator factor shorten into ONE correction
  plane — Scott's own "shortened correction plane" horn;
- the `#1173` heavy rich flats (`>= 42453` common vanishing columns)
  are high-deficiency carrier objects — the K'-ladder's carrier
  atlas/trichotomy machinery speaks their language;
- both stacks' remaining "chronology-safe" obligations are priced by
  the `#1169` acceptance contract.

No collision: the local relative correction-ray payment
(`rate_half_mca_rank11_relative_core_interpolant_ray_payment`, H_C
frame, per-direction bound) and `#1171`'s global pair-difference ray
cap are different objects in different frames.

## Scope

Zero active-v4 movement; rank eleven unpaid; the structural clauses
are upstream-reviewed (independent math + certificate reviews GREEN on
each packet); this node independently replays every envelope identity
and wall constant.

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_mca_rank11_anticode_branch_payments_import/verify.py
```
