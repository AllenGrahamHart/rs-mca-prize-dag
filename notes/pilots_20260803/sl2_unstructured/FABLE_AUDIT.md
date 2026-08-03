# Coordinator audit — SL-2 unstructured exclusion pilot

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — PARTIAL accepted;
a real scope gap in a banked theorem found AND closed in one pilot;
the occupancy question reduces to SL-2-RES (a pure divisor-counting
statement).**

Replay: algebra.py + descent.py rerun clean (677 total checks, the
single failure is the pilot's deliberately-recorded mis-specified
PREREG item L3 — corrected forms pass; the honest-recording pattern).

ADOPTED:
- **THE CATCH (F2 fired)**: BP(1)'s "structured => 2-power depth" is
  scoped to M = 2^ceil(log2 d) >= d ONLY; sub-depth coset scales
  M | d, M < d are NON-EMPTY inside the band proper at all three
  prize rows (up to M = 2^31), and the largest lands on the
  quotient's cascade tier. "The structured half is proved excluded"
  was too broad — my r3.2 wording inherited it.
- **THE CLOSURE**: THEOREM L (liveness/parity exclusion: separately
  M-periodic (u,v) with h odd force M <= cap_d, killing
  M = 2^21..2^31 unconditionally); the remaining M = 2^1..2^20 carry
  >= 3.09e5-bit first-moment margins (heuristic-grade, flagged).
- **NEW PROVED MACHINERY**: LEMMA W (window system for a general
  word: cores <-> monic divisors of X^n - 1 on a codim <= 2d affine
  subspace — the RIGHT coordinates for the whole problem); THEOREM D
  (exact descent bijection; SETTLES definitions item 6's "syndromes
  descend" adjudication affirmatively for the window system);
  THEOREM R (full Toeplitz rank on the gated class via
  Berlekamp-Massey — no linear degeneracy is ever available; any
  blow-up must be arithmetic). P3-EVASION recorded (mixed-class
  pencils evade the strip filter; THEOREM L is what actually excludes
  the descent class).
- **SL-2-RES** (the residual, one statement): aperiodic band-proper
  core count <= 0.68 n^2, equivalently: how many monic degree-r'
  divisors of X^n - 1 lie on a codimension-2d affine subspace? Must
  carry h ODD and q >= 2^209 (both load-bearing: the h-even control
  fails twice over; the q-pin has 41.5 bits of headroom at the
  binding row).

Decisions: (1) dated addendum APPLIED to xr_mc_depth_quantization
(BP(1) scope + the THEOREM L closure); (2) mint of
xr_window_system_descent (W + D + L + R) QUEUED for the next
mint-prep round; (3) SL-2-RES as the Pro brief when Pro resumes — the
divisor-counting form is exactly brief-shaped. Routes 1-2 quantified
dead (packing 2^1.7e12 over budget; the counting route dies at
N = 1/rate). Subtraction clean.

## Codex maximality correction (2026-08-03)

The theorem-grade W/D/R/L content above survives, but lines 33-35 do
not give an equivalent formulation of selected occupancy as written.
The window equations count RAW `(k+d)` interpolation sets. If a maximal
pair has full core size `k+e`, it contributes
`binom(k+e,k+d)` degree-`n-k-d` locators. Thus

```text
RAW_d = sum_{e>=d} MAX_e binom(k+e,k+d),
```

and one deeper pair can swamp the `0.68n^2` raw-divisor threshold while
contributing zero to `N_d`. This is the same raw-subset defect already
certified in `ld_core_count` (`RAW_1=334>272`, selected maximal
`N_1=0`). Also, Theorem R proves rank `d` for each single-word window
matrix; it does not prove that the stacked joint system has codimension
exactly `2d`.

The corrected residual is
`xr_band_maximal_window_divisor_count`: degree-`n-k-d` locators in the
joint window intersection whose reconstructed pair has full core
exactly `H\T`, has `L_P>=2` under first-match selection, and survives
the strips. Its scope includes small-scale mixed-class quotient
patterns as well as non-coset aperiodic systems. First-moment margins
remain evidence only.
