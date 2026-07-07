# Fleet run on upstream's two pre-registered falsifiers (2026-07-07)

Pre-PR work item 3 (THREE_VS_SEVEN.md). Scripts + raw JSONs:
`fleet/q_sp_fleet_modal.py`, `fleet/q_followup_modal.py` (Modal, exact
int64 DP with checksums; float64 extension validated on an exact row).
Their objects replayed from V13: Φ_{m,w} prefix map (Newton-equivalent
power-sum DP, w < p), sp_w(w+1; D') top shift-pair stratum
(thm:capg-second-moment), falsifiers per their own text ("a
counterexample... either produces a super-polynomial primitive prefix
fiber, refuting (Q), or a super-polynomial primitive aperiodic residual
family").

## 0. VALIDATION GATE — their printed calibration replayed digit-exact

    (17,16,8)  w=1,2,3: 1.0012, 1.2126, 2.6722   (printed 1.0012, 1.21, 2.67)
    (41,20,10) w=1,2,3: 1.0022, 1.2101, 4.1034   (printed 1.0022, 1.21, 4.10)
    Poisson row: max 11, mean 2.681               (printed max 11, mean 2.7)

## 1. (Q) — NO KILL; their dense-bulk prediction extended three scales

max/mean − 1 in the dense bulk (w = 2, m = N/2, geometry N/√p ≈ 3–5):

    (17,16):   2.1e-1        (41,20):   2.1e-1
    (101,50):  2.9e-6        (257,64):  ~9e-9 (their row)
    (577,96):  6.1e-13       (1153,128): ≤ 1e-15 (float measurement floor)

Collapse toward 1 accelerating with scale — the opposite of a kill. Their
falsifiable prediction ("any violation must place a super-polynomial
fiber inside the dense bulk of a primitive scale") is consistent with
every point we can reach, now including three scales beyond their
printed table. Checksums: int64 rows exact (Σ fib = C(N,m), and the
overflow guard CAUGHT the two rows exceeding int64 — rerun in float64
with zero relative checksum error and validated against the exact
(101,50,25,2) row).

## 2. (SP) — NO KILL; primitive shift-pair mass at model scale

sp_2(3; D)/model (model = C(N,3)C(N−3,3)/p²) across the ladder:
1.270, 1.084, 1.037, 1.009, 1.037, 0.955 (p = 17 → 1153) — monotone-ish
collapse to 1. Depth 3: 1.374, 1.876, 1.035 (p = 17, 41, 101) — small-N
inflation dying at scale. (−1)-dilation pullback pairs (the
quotient-pullback contamination) bounded ≤ 64/500-scale at w = 2 and
zero at w = 3 — the primitive part IS the bulk of the count and sits at
model scale.

## 3. THE DATUM — raw mode-at-null fails by NULL-SUPPRESSION at (41,20,10,2)

Their one binding red (Q atom) has two candidate forms
(prob:capfr1-mode-null): mode-at-null (N_w(z) ≤ N_w(0) ∀z, quotient
rungs separated) OR exchange-compression. Our fleet found, twice
(exact DP + independent exhaustive enumeration):

    (p,N,m,w) = (41,20,10,2), D = μ_20 ⊂ F_41 (the quadratic residues):
    N(0,0) = 66;  N(11,0) = 133 = max;  mean = 109.9.

Structure of the datum:
- the max is UNREMARKABLE: 133 = mean + 2.2σ, BELOW the Poisson-expected
  max (≈ 150 over 41² = 1681 cells). The max-fiber (Q) bound is fine
  here (κ = 1.21).
- the NULL fiber is the anomaly: 66 = mean − 4.2σ — suppressed 4σ into
  the bottom tail. Mode-at-null fails not by a spike but by null
  suppression.
- the argmax fiber carries NO obvious quotient structure: 0 coset-union
  members, 0 dilation-stable members (classifier output; "contains some
  μ_2 coset" is not structure — 99.45% of random subsets do).
- the whole line (μ_20·11, 0) carries uniform 133s (consistent with
  dilation equivariance fib(γz₁, γ²z₂) = fib(z), orbit size 20 —
  cross-check passes).
- row-arithmetic-specific: the sibling half-group row (101,50,25,2)
  (also p = 2N+1) has null = max to 1e-12 — the suppression is finer
  than the p = 2N+1 pattern; explanation OPEN.

Consequence FOR THEIR program (correspondence PR content): the datum
discriminates their two routes — at rows like (41,20,10) the
mode-at-null form is false raw and can only be rescued if their rung
ledger charges the (·,0)-line (which one of their rungs?); the
exchange-compression route and the max-fiber target are untouched. At
their binding row (M31 list, max ≤ 8.42× mean needed) null-suppression
would be HELPFUL if it recurs — the atom bound binds the max, not the
null. Either way this is a form-level calibration datum their program
does not currently print.

## 4. Banking

- Upstream DAG (their nodes, per the node-local rule): EXTERNAL-FLEET
  evidence tags added to up_q_atom_finite (calibration replay + ladder
  extension + the mode-at-null datum) and up_sp_from_q (SP census at
  model scale).
- Our side: no floor status change (their objects, not ours); the
  bridge-relevant pointer lives in THREE_VS_SEVEN.md's falsifiability
  section.
- Verdict for the PR: we arrive bearing evidence FOR their two
  falsifier targets (no kills, three new scales) plus one
  route-discriminating datum they don't have.
