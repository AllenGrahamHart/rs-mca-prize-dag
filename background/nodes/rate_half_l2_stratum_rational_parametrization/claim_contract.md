# Claim contract

- **Claim:** at `m = 2`, the map `(f,g,h,k,L) -> (Q_0,Q_1,Q_2)` defined by
  `L*Q_0 = f^2-kg`, `L*Q_1 = fg+hk`, `L*Q_2 = g^2+hf` (subject to exactly
  two conditions at the root of `L`) is a birational parametrization of
  the entire `e = m = 2` (L2) stratum with image dimension exactly 18; the
  determinantal form (DET) and the two syzygies (SYZ) hold identically
  (over Z, hence over every field); (RES) forward direction proved.
- **Dependencies:** the round-35 (L2) witness machinery (the pencil model
  and the (D-B) criterion); elementary polynomial algebra.
- **Output:** the construction instrument of the (SAT3)-on-(L2) lane (hit
  rate 1), the exact scope of the third condition (`f(ell) = g(ell) = 0`
  exception), the (RES) status split, and the dimension 18.
- **Consumer:** `rate_half_band_crossing_location`; the round-38
  scale-elimination `T = 3` achievement runs through this parametrization.
- **Nonclaims:** the (RES) converse (MEASURED only, 1200/1200); no
  `m >= 3` statement; birationality's finite-fibre halves are measured
  (40/40 per field), not proved; nothing about whether the `T`-ladder
  continues past the banked values.
- **Falsifier:** a member of the (L2) stratum not in the image; a
  counterexample to (DET)/(SYZ) (excluded — proved symbolically); a
  gcd != 1 quadruple with det M(B) != 0 (would break the measured (RES)
  converse).
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_l2_stratum_rational_parametrization/verify.py`
  and the symbolic + recertification audit `verify_audit.py`.
