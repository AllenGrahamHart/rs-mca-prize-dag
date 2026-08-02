# Fable audit of the F2A.5 slice-coefficient pilot — 2026-08-02

**Verdict: ACCEPTED.** Both verification suites replayed green on my
side under `tools/ramguard local`: `verify_slice.py` 11/11
(`F2A5_VALIDATION_ALL_PASS`) and `mode_and_coset.py verify` 3/3
(C1 phase identity, C2 death dichotomy over 124 modes, C3 coset
containment). The pilot answers its pre-registered questions cleanly:
F1 not triggered (but every cheap structure ruled out), F2 not
triggered in the blindness sense (visibility established at exactly the
2^(-n/6) scale), F3 triggered conditionally on a named window class.
The main finding — the Delta-parity inversion — is a course correction
binding on the adopted F2A plan and has been recorded as a dated
amendment in `BRIEF5_ADVERSARIAL_AUDIT_SUMMARY.md`.

## Independent verification record

- Replayed both suites myself (this session, exact, ramguard local).
- Hand-derived the subgroup argument behind the three-way split: in
  Z/2p (p odd prime) the proper subgroups are {0}, {0,p}, 2Z/2p. Any
  even element with nonzero mod-p part generates 2Z/2p (order p, p
  prime), so when the Delta_i are not all congruent mod p,
  D = <Delta_i - Delta_j> contains 2Z/2p and Ann(D) can contain at most
  {0, p}; k = p is the unique odd death candidate, and
  p*Delta mod 2p = 0 or p according to Delta's parity — giving exactly
  the all-even / all-odd / mixed trichotomy. Sound.
- Checked the odd-Delta slice floors against log2 p: 4.5207 vs 4.5236
  (p=23), 5.3550 vs 5.3576 (p=41), 6.0627 vs 6.0661 (p=67), 6.6473 vs
  6.6582 (p=101). Floor law confirmed to 3-4 decimals at every prime.
- Checked the fence-reversal arithmetic: sqrt(C(60,30)) = 2^28.357,
  matching the dossier's fence constant; official-scale thresholds
  3*log2(2^31) = 93 and 43*log2(2^31) ~ 1333. Consistent.
- Spot-checked internal consistency of the phase law
  (arg r_i(k) = pi*k*Delta_i/p from omega = e^{i*pi/p}) and of V7's
  tie-in to the audited F2A.2 alignment (rel err 1.7e-14, float-level
  as expected for a cross-implementation comparison of exact objects).

## Findings adopted (binding on the F2A lane)

1. **Sharp Law A does not survive b-resolution.** Fixed-b reachability
   is governed by the difference subgroup D, not the sumset. The
   F2A.2 reachability audit must be re-run on D — worker-shaped
   follow-up, queued for the next worker-goal update.
2. **The F2A.4 compiler criterion is inverted at fixed b.** The
   exceptional-owner list is Ann(D), strictly larger than Ann(G); the
   k=p pair-contraction "health" criterion from resonance.py selects
   exactly the windows that are fatal at fixed b (slice floor 1/p via
   hhat_p(p) = 2). No F2A.4 compiler work may start from the
   full-window ranking.
3. **Shape of the eventual slice-coefficient theorem** (three
   structural constraints, all with exact witnesses): window-specific
   with a parity-inhomogeneity hypothesis (parity-homogeneous
   coordinate subsets — reachable at every frequency, ~half the
   coordinates — floor the slice at 1/p); phase-SPREAD formulation,
   never alignment against a fixed direction (V9 witness: common
   rotation kills alignment-based contraction exactly); normalised by
   log2 C(n,b), not n (integrality: eta_n <= H(b/n)).
4. **The black hole re-characterised: precision, not blindness.** The
   extremal hidden modulation is uniquely the parity (Parseval
   uniqueness, exact at n <= 4), fences (i) and (ii) are one object,
   and slicing sees it at exactly the 2^(-n/6) scale — but any theorem
   controlling weights coarser than the target itself still cannot
   close the bound. The 2^24-2^32 adversarial margins quantify this.
5. **Budget reality.** The 1/3-per-rung budget is marginal on generic
   windows (slopes 0.26-0.36 straddling 1/3, negative intercepts to 5
   bits) and dead on parity-homogeneous windows past n > 3 log2 p. The
   1/43 calibration clears with ~13x margin on generic windows. PP5.0
   still gates which number is normative.

## Caveats kept (verbatim from the pilot, endorsed)

- Cancellation slopes ride the balanced-weight integer proxy; the
  structural laws (coset confinement, hhat_p(p)=2, death dichotomy,
  |e_b(p)| = E_b) are exact with true weights. The 1/p floor's
  ATTAINMENT rests on the proxy.
- p <= 101; official p ~ 2^31 is a four-decade extrapolation of laws
  exactly constant over the measured range.
- Single descent j=1; tower functoriality untested (inherited F2A.2
  gap). Nothing here is mintable — PP5.0 and the F2A.1 seam are still
  the unproven upstream gates, unchanged.

## Posture

The F2A exploratory GO stands, amended by findings 1-3 above. Next
concrete asks, in order: (a) PP5.0 seam (unchanged, still Gate-0);
(b) re-run the reachability audit on D (worker-shaped); (c) draft the
b-resolved slice-coefficient theorem statement under the three
structural constraints and hand it to Pro for an adversarial round
BEFORE any node is proposed — the parity-inhomogeneity hypothesis is
exactly the kind of clause their fixtures are good at breaking.
Relay package for Pro: this REPORT.md + the amendment block in
BRIEF5_ADVERSARIAL_AUDIT_SUMMARY.md.
