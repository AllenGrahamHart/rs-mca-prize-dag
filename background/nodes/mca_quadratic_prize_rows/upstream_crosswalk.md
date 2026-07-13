# Upstream crosswalk and scope audit

## Source

- repository: `przchojecki/rs-mca`
- pinned commit: `9262f63cf093a7510a2df435f220390f59e2bcd5`
- manuscript: `experimental/rs_mca_thresholds.tex`
- labels: `thm:quadratic-mean-overlap`, `prop:universal-tangent-floor`,
  `cor:prize-window-compiler`, `thm:intro-prize-rows`, and
  `prop:proth-row-check`

## Independent checks

The local proof was reconstructed from the definitions and audited in both
directions:

1. the large-overlap collapse counts actual distinct slopes, not supports;
2. Cauchy-Schwarz forces such an overlap under the printed quadratic
   inequality;
3. the parity-column construction supplies the matching `r+1` slopes;
4. the Proth witnesses prove the four printed field orders prime;
5. exact division by `2^128` gives the integer bad-slope budget;
6. adjacent signs of `F_(n,k)` place `B-1` inside and `B` outside the proved
   quadratic range;
7. closed-ball rounding gives a safe grid maximum `(B-1)/n` and an unsafe
   real supremum `B/n`.

The verifier independently checks the four large certificates, exhausts the
proof arithmetic for all `2<=n<=80`, and exactly enumerates the syndrome-line
MCA numerator for a small MDS toy.

## DAG interpretation

This packet is evidence for `mca_grand` and realizes the roadmap's exact
finite-MCA milestone on four particular eligible codes. It is not a logical
replacement for the canonical root, whose quantifier covers the separately
frozen near-capacity/corridor rows. No edge to `rate_half_band_closure` is
claimed: that node fixes a different 256-bit razor row and also contains an
ordinary-list obligation.
