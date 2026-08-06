# FABLE_AUDIT — o1_generating_adversary (round 18, pilot 1 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED, MAINTAINER-LEVEL —
three attacks fail with exact margins (the coset costs a factor of 1;
the generating scope is exactly three non-empty Lucas-certified
classes; no ternary construction reaches the floor), but the
zero-margin attack LANDS CONDITIONALLY: at k = e, LEMMA 3's
requirement IS the balance t·L >= n, so (O1)'s truth is decided by
the ENSEMBLE CALIBRATION — survives under the full-subset (C)
reading with <= 184 bits of slack; FALSE by 2^{Theta(n)} under the
exact fixed-slice (T*) reading. The 0.0044% "agreement" banked twice
(f2_tq_pin CATCH-4, t_naming CATCH-C) is the SIGN OF (O1) at zero
margin.**

Replay: verify.py 187/187 exit 0, digest O1_GEN_ADVERSARY_ALL_PASS
(coordinator re-run under ramguard local). Anchor spot-checks:
f2_deployed_windows/REPORT.md:55 verbatim-exact ("codim_j =
min(m_j, t/2)" — CATCH-H's second leg, the lane's own t/2).
COORDINATOR INDEPENDENT CHECK of THEOREM G1's core: (Z/2^41)^* is
Z/2 x Z/2^39, so every element order is a 2-power — k = e forces
e in {1,2,4}; e in {3,5,6} can never generate. Confirmed by my own
group theory.

ADOPTED:
- **THEOREM G1/G2** (the surviving scope: exactly three generating
  classes, all non-empty, primality established twice including
  Lucas p-1 CERTIFICATES — proofs, not tests). CATCH-F.
- **THEOREM C1** (exact coset invariance of (O1) — the attack
  needed a constant, got a factor of 1, verified by a disjoint
  group-ring route reproducing the banked 3856). HALF OF f2_adm
  CATCH-6 CLOSES (the coset gap is confined to the parity/descent
  machinery); f2_adm CATCH-1 is coset-robust. Addendum to the
  f2_adm audit written this bank.
- **THEOREM D1** (the DLI wt >= 2R+1 law APPLIES on every
  admissible row — p > m always, by the elementary e_p case split;
  the first row family where char > w holds; the tower verdict
  reversed by the field cap). The crosswalk's first dividend —
  found by the ADVERSARY, blind to the z1 sibling that was asked
  the same question generatively; reconcile at z1's bank. Its
  limit honestly priced: (M3) stays vacuous (23.9x -> 11.96x).
- **THEOREM Z2 + CATCH-A (maintainer)**: the ensemble dichotomy.
  The coordinator's reading of the state: mystery 2's (O1) on its
  surviving scope now hinges on a 2x2 of unpinned conventions
  (Lambda parity x ensemble calibration), and the internally-forced
  cell — reading A (CATCH-H: forced by the proved K1/K2/G
  trichotomy + the lane's own t/2 statement) plus the slice
  ensemble (CATCH-G: the (O1)=>(O2) fence itself demands the
  slice) — is exactly the cell where (O1) is FALSE by 2^{Theta(n)}.
  Stated of record: THE LANE'S OWN INTERNAL LOGIC POINTS AT THE
  FALSE CELL; only a maintainer ruling that the intended reading
  differs can restore (O1) on generating rows. This joins the
  Przemek queue as scope question #3 (with generation and parity),
  now the sharpest of the three.
- **THE MINIMAL SURVIVING FORM** banked verbatim (the exact
  E[T] = 2^{n/2}·Z_1^e identity with the three-class scope and the
  two named unpinned conditions) — this is the statement the
  Przemek note should carry.
- CATCH-B accepted (f2_adm D3's "margin 1.000" is reading-A-only;
  under B two classes flip REFUTED -> SATURATED; addendum to the
  f2_adm audit). CATCH-C accepted (my brief's "any strict loss
  kills" was too strong — the o(n) absorbs sub-Theta losses; brief
  defect, mine). CATCH-G banked (THEOREM B' vacuous at every moving
  rung; the fence loses Theta(n) against the b-resolved scale).
  CATCH-H banked as an UPGRADE of t_naming CATCH-E (internal-
  consistency force, not intent — CATCH-E stays open; addendum to
  the t_naming audit).

HONEST RESIDUALS accepted: nothing bounds Z_1 (the terminal is
untouched — the z1 sibling owns it); the kill is conditional on two
maintainer-decidable choices, neither chosen; the ensemble question
vs t_naming N3's wrong-t flag disclosed (coordinator's judgment: it
is a genuinely different question — which ensemble calibrates
t_F2's OWN balance — not a t_XR substitution; a maintainer may
still rule otherwise); the third consecutive weak-prereg
self-report (registrations written after reading the record) —
noted as a systematic property of derivation-style pilots, priced
into how much the prereg ritual is trusted on such pilots.
DRAFT-ONLY confirmed; z1 sibling never read.
