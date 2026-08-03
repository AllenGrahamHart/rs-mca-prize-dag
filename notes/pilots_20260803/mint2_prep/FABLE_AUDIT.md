# Coordinator audit — mint-2 (F2 + P-B remainder)

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — all four packages
wired; the refusal accepted; three corrections to the record adopted.**

## Replay

All four verifiers coordinator-replayed under ramguard tiny in place
after the move (37 checks total, 0 FAIL), plus manifest-discovered
harness replay 4/4. `verify_prize_dag` + census PASS (242 = 179/38/25
unchanged; the four nodes are background).

## Hand-verification (the two reconstructed proofs, line-audited)

- **F2.b (parity-defect value):** step (b) hand-derived — with centred
  representatives, `kappa(a)kappa(a+t) = (-1)^t` off the overflow set
  and `(-1)^{t+1}` on it (the `-p` shift flips parity, p odd), and the
  overflow set `{M-t+1..M}` has exactly `t` elements, so
  `A(t) = (-1)^t (p-2t)`; `A(0) = p` anchors. Step (c): `{1..M}` is a
  half-system and a nonzero scaling of a half-system is a half-system,
  so `|A|` takes each `p-2t` once and `D = sum = M^2`. Evenness of `A`
  by the substitution `a -> a+t`. Correct; the 3,552-frequency
  exhaustive machine check corroborates, and the F2.c scope correction
  (`a_c b_c != 0`; the two parity-pure lines give `D = m`) is ADOPTED
  as the record.
- **F4 (block dichotomy, entirely pilot-written):** Claim 1's core
  arithmetic (`|G| + m|J^J'|`, spread iff `m >= h+1`) and Claim 2
  (`m <= h` puts the family in Gamma_hi) — checked. Claim 3's coset
  algebra: the reversed polynomial of `X^m - g^m` is `1 - g^m Y^m`;
  `m > h` kills it mod `Y^{h+1}` (one point, no live direction);
  `m <= h < 2m` kills the cross terms `Y^{2m}` so the motion is affine
  in the single scalar `sum g_j^m` — checked. Claim 4's chaining:
  `R_{S u T} = R_S R_T`, units, unit-multiplication maps lines to
  lines, and two `(a-1)`-sets differing in one element share
  `b - a >= 2` pool blocks, forcing one line (this is where the F4.c
  hypothesis correction `b >= a+2` is load-bearing) — checked, four
  lines, correct. The F4.b coordinate flag (e-coordinates are what the
  source's code computes; power-sum and elementary-symmetric collinearity
  differ in general, coincide for cosets) is ADOPTED.
- **F1 (antipodal):** LTE valuations (`v_2(p+1) = 1` from `p == 1 mod
  4`; odd squares `== 1 mod 8`), the gcd step (`n_j` a pure 2-power),
  and the inserted sigma-odd lemma (`sigma(-s) = -sigma(s)` in `Z/2p`,
  both branches checked) — all hand-verified. The strongest verified
  form was drafted clause for clause; nothing widened (F0.e confirmed
  by comparison against `tower.py:22-43`).

## Decisions (all the coordinator calls the pilot surfaced)

- **F0.a refusal ACCEPTED**: `pb_l1_lemma` is banked verbatim in
  `xr_two_slope_cost_theorem` (hard law 5); its P-B corollary lives
  inline as Lemma 0 of `pb_design_ceiling` (band-wave precedent).
- **F0.c ACCEPTED with one addition**: the F2 pair is wired now as
  background nodes; since reachability requires a route to the root, a
  `ref` edge `f2_parity_defect_certificate -> u2c_giant_tnull_dichotomy`
  was added — a CROSS-REFERENCE to the F2 flip campaign's kernel node
  (standing goal), NOT a logical dependency; proper `ev` edges follow
  when the slice-theorem/PP5.0 obligation is minted as a node.
- **Edge E.a DOWNGRADED to `ref`** (the certificate is logically
  self-contained; house convention reserves `req` for consumption).
- **F3.b ACCEPTED** (margins from the PROVED prescribed-slope ceiling;
  `OFFICIAL.json`'s differing figure is by design). **F3.c ACCEPTED**
  (free-slope form demoted to a recorded non-claim). **F3.d APPLIED**:
  dated addendum on `xr_two_slope_cost_theorem` making the corollary's
  independence hypothesis explicit, citing the `mu_20`-orbit witness.
- **Design-ceiling item 6**: the machine-fact form of Theorem 3's
  invariance sentence is ACCEPTED as recorded (the substitution scales
  `u`, `v` by different powers; the honest form is the checked fact).
- **F4.e**: the SELECTOR CATCH wording was checked against the P-B
  TARGET's 2026-08-02 addendum — consistent (the addendum's amendment
  already adopted the joint identity-plus-selector reading).
- **F0.f compute-law lapse** (one bare-python text substitution, no
  arithmetic of record): recorded; future pilot briefs will carry the
  standing reminder.

## Wired

4 nodes + 6 edges (2 internal ref, 1 req from the banked cost theorem,
2 ev into `xr_lowcore_spread_heart`, 1 campaign ref); dag 1768/4906;
manifest refreshed (2379 scripts).
