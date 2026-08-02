# DRAFT: the b-resolved slice coefficient theorem (F2 lane) — for Pro's adversarial round

**Status: DRAFT, not a node, not minted, not claimed.** Compiled by
Fable 2026-08-02 from the two banked F2 structure pilots
(`notes/pilots_20260802/f2_slice_coefficients/` = F2A.5,
`notes/pilots_20260802/f2_parity_boundary/` = F2A.5b; both
coordinator-replayed, 11/11 + 3/3 and 8/8 exact validations). The ask
to Pro is at the end. Nothing here is mintable until PP5.0 freezes the
budget and this survives an adversarial round.

## Setting (established, exact)

Single descent j = 1, q = p^2, p an odd prime. Each window coordinate
i carries sigma_i^± = s_i^± + p·u_i^± in Z/2p and the invariant
Delta_i = sigma_i^+ − sigma_i^− in Z/2p. With base = Σ_i sigma_i^−,
omega = e^{i·pi/p}, and hhat_p the carry DFT (odd modes only,
hhat_p(p) = 2), the b-resolved slice statistic satisfies EXACTLY
(law P1, verified in Z[zeta_p]):

    V_b = (1/2p) Σ_{k odd} hhat_p(k) · omega^{k·base}
              · e_b(omega^{k·Delta_1}, ..., omega^{k·Delta_n}).

rho_b = |V_b| / C(n,b) is the slice cancellation ratio; beta = b/n;
r = beta/(1−beta). L1 mass: M_p = (1/2p) Σ_{k odd} |hhat_p(k)| =
(2 ln2/pi)·log2(p) + 0.9626 + o(1) (residual 1e−4 at measured p;
identical to the F2A.2 carry-DFT L1 constant, two independent
derivations).

## The theorem (candidate statement)

**Hypothesis (H-spread).** For eta > 0, say the window is eta-spread
at slice fraction beta if

    min over odd k, 1 <= k < 2p of  Lambda_k(beta)  >=  eta,  where
    Lambda_k(beta) = −(1/n) · max_{psi} Σ_i log2( |1 + r·e^{i(pi·k·Delta_i/p + psi)}| / (1+r) ).

Lambda_k >= 0 always, with equality iff mode k is slice-dead; the
max over psi makes the condition rotation-invariant (phase-SPREAD,
never alignment — the F2A.5 V9 witness forces this).

**Checkable surrogate (H-flat).** It suffices that
max_{k odd} |R_k| <= 1 − eta·ln2/(beta(1−beta)), where
R_k = (1/n) Σ_i omega^{k·Delta_i}. This surrogate is asymptotically
SHARP (measured eta/flat → beta(1−beta)/ln2 to 0.7%). Parity
inhomogeneity is exactly the single frequency k = p of this condition
(|R_p| = 1 − 2·beta_min): necessary, and refuted as sufficient (the
adjacent-pair killer: beta_min = 1/2 with rho_b = 1 exactly).

**Conclusion.** If the window is eta-spread at b, then

    −log2 rho_b  >=  n·eta − log2 M_p − log2 kappa(n,b),
    kappa(n,b) = (1+r)^n r^{−b} / C(n,b) = O(sqrt n).

Mechanism of proof (proxy level, established): the Cauchy bound
|e_b(omega^{k·Delta})| <= kappa(n,b)·C(n,b)·2^{−n·Lambda_k(beta)}
per mode (proved inequality; median slack 13x on 1500 measured rows),
then the triangle inequality over modes with total mass M_p. Startup
deficit at official p ~ 2^31, n = 1024: log2 M_p + log2 kappa ≈ 9
bits.

## The two budget variants (PP5.0 decides which is normative)

- **Variant 1/3** (eta = 1/3 per rung): hard ceiling Lambda_max(beta)
  = log2(1/max(beta, 1−beta)) makes this IMPOSSIBLE outside beta in
  [0.2063, 0.7937]; empirically only ~15% of windows clear it even at
  strong flatness (flat >= 0.60 still leaves worst eta ≈ 0.25). As a
  uniform per-window theorem this variant is NOT viable; it could
  survive only with an additional window-selection mechanism upstream.
- **Variant 1/43** (eta = 1/43 ≈ 0.0233, the weak-margin block
  calibration): needs flat >= 0.0860 (asymptotically sharp threshold);
  97%+ of measured windows clear; the parity floor alone would clear
  it for beta_min >= 0.02197. Viable as a uniform theorem under
  (H-flat).

## Known killers the hypothesis must exclude (all with exact certificates)

adjacent-pair (beta_min = 1/2, rho = 1 exactly, universal at every
frequency via the multiplicity law {1,...,p−1}); arc-w families;
few-value windows; coset-trivial (total death, every b); the hidden
modulation w = 1 + 2^{−n/6}·eps (visible at slice resolution but
demanding target-level precision); the Hamming-slice fence (full-window
theorems vacuous at fixed b). All are inside (H-flat)'s excluded region
— that is the design criterion the two pilots converged on.

## The three gaps between this draft and the lane's target (explicit)

1. **Proxy gap**: the Cauchy/certificate machinery is exact at the
   balanced-weight integer proxy; true-weight magnitudes are verified
   only at n <= 12, p <= 23 (the structural laws — P1, the death
   dichotomy, hhat_p(p) = 2 — are weight-general; the killers are
   proxy-independent).
2. **Seam gap**: PP5.0 (the consumer composition law) and the F2A.1
   orientation-cube seam are unproven upstream; this theorem prices a
   single rung and nothing composes it yet.
3. **Tower gap**: single descent j = 1 only; functoriality across
   rungs untested.

## The ask to Pro

(a) Attack (H-spread)/(H-flat) as a hypothesis: find a window class
inside the hypothesis that still kills the conclusion (the pilots'
adversarial climb found none, but it is a weak local search), or show
the surrogate's sharpness breaks at true weights. (b) FREEZE PP5.0's
composition law first and tell us which budget is normative — 1/3
makes this theorem shape unviable as stated; 1/43 makes it viable;
anything between moves the flat threshold. (c) If (H-flat) survives:
what upstream mechanism (if any) guarantees the DEPLOYED windows of
the actual F2 tower satisfy it — or is a window-selection step now a
required part of the F2 architecture? That last question is the lane's
new heart.
