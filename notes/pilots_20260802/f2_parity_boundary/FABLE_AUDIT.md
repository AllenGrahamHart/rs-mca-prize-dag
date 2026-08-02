# Fable audit of the F2A.5b parity-boundary pilot — 2026-08-02

**Verdict: ACCEPTED.** The reconnaissance did exactly what it was sent
to do and the answer overturns the working plan: the
parity-inhomogeneity hypothesis I adopted after F2A.5 is the WRONG
invariant. The correct one is spectral flatness of the Delta multiset
over ALL odd modes — (H-spread), with (H-flat) as the checkable
surrogate — of which parity is the single frequency k = p. All three
pre-registered falsifiers fired, each informatively.

## Independent verification record

- Replayed `verify_boundary.py` this session: 8/8 exact PASS
  (Delta-only DP == sigma DP; the mode law P1 in Z[zeta_p]; the
  Krawtchouk specialisation at k = p with hhat_p(p) = 2; total death
  at all-equal Delta; the two-branch Lambda_p closed form to 4e-16;
  the Cauchy bound on 1500 rows; the Fourier surrogate with min slack
  exactly 0; certificate soundness on 232 rows).
- Hand-verified the adjacent-pair killer MECHANISM: with Delta taking
  two adjacent values, the k = 1 phases sit pi/p apart — the mode is
  NEAR-dead (|R_1| ~ 1 - (pi/p)^2/8) — and k = 1 carries O(1) DFT
  mass (~2/pi) versus 1/p at k = p. So maximal parity balance buys
  nothing: the damage lives at the opposite end of the spectrum. The
  eta_inf ~ 0.33/p^2 tail and the n >> p^2 crossover follow from the
  same arithmetic; at official p ~ 2^31 that is ~7e-20. Sound, and
  obvious only in hindsight.
- Hand-checked: the multiplicity law makes the killer universal
  (values with multiplicities {1,...,p-1} guarantee adjacent-pair
  windows of size ~2(p-2) at every frequency); the Lambda ceiling
  arithmetic (eta = 1/3 impossible outside beta in [0.2063, 0.7937] =
  [1 - 2^{-1/3}, 2^{-1/3}]); and the cross-pilot consistency of
  M_p = (2ln2/pi)log2 p + 0.9626 with F2A.2's carry-DFT
  L1 = (2/pi)ln p + 0.9625 — the same constant measured by two
  independent pilots through different formalisms.
- The calibration discipline held: the adversarial climb was gated on
  reproducing the known all-odd killer, and the true-weight exact
  check (n <= 12, p <= 23) confirms the killers are proxy-independent
  (rho = 1 exactly).

## Findings adopted (binding on the F2 lane)

1. **The theorem hypothesis is (H-spread)/(H-flat), not parity.** The
   parity clause mis-ranks windows by 25+ bits and admits an
   eta = 0 killer at maximal parity balance. The drafted clause (with
   its three structural notes: rotation-invariance; non-uniformity
   over k — near-dead k=1 is ~p times worse than dead k=p; the hard
   Lambda ceiling) goes into my theorem draft verbatim as the
   candidate hypothesis, then to Pro's adversarial round.
2. **PP5.0 is now load-bearing on the BUDGET, not just the seam.**
   F3 fires for 1/3 (only ~15% of windows clear it even under strong
   flatness; the ceiling makes it impossible outside central slices)
   but NOT for 1/43 (97%+ clear under modest flatness, threshold
   flat >= 0.086, asymptotically sharp). Whether the composition law
   needs 1/3 or 1/43 per rung decides whether the slice-coefficient
   theorem shape is viable at all. This sharpens the Gate-0 ask to
   Pro: freeze the composition law FIRST.
3. **Mutation battery additions**: the adjacent-pair window (the
   canonical non-parity killer, universal at every frequency), arc
   and few-value families, coset_trivial (total death), all with
   exact certificates. Any future F2 hypothesis clause must kill all
   of these or carry them as explicit exclusions.
4. **The quantitative ladder is now exact where it matters
   model-free**: the k=p Krawtchouk floor needs no proxy, so the
   parity-clause margin table at official p (1/3 dies at n > 93 for
   parity-homogeneous; 1/43 at n > 1333) is exact arithmetic — it
   retires the earlier approximate thresholds.
5. **Startup deficit pinned**: ~9 bits at official p, n = 1024 — the
   constant any certificate must clear before the linear term earns.

## Caveats kept (endorsed)

- Cancellation magnitudes at scale ride the balanced-weight proxy
  (killers proxy-independent; structural laws weight-general).
- Official-scale claims enter only through the model-free Krawtchouk
  floor and the analytic M_p slope — the cleanest extrapolation
  posture of any F2 pilot so far — but the adjacent-pair persistence
  at official scale still rests on the multiplicity law (verified to
  p = 199) and the n >> p^2 scaling (measured to n/p^2 = 124).
- The climb is a weak local search; eta = 0 global optimality is
  attained by construction, not by search.
- Nothing mintable: PP5.0 and the F2A.1 seam remain the unproven
  upstream gates, unchanged.

## Next action (mine)

Draft the b-resolved slice-coefficient theorem statement with
(H-spread)/(H-flat) as hypothesis and BOTH budget variants (1/3 and
1/43) displayed, package with this REPORT and the F2A.5 report for
Pro's adversarial round. No node until Pro has attacked the clause
and PP5.0 has frozen the budget.
