# PRE-REGISTRATION — (O1) ADVERSARY on GENERATING rows: is the surviving F2 claim true at zero margin?

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. ADVERSARIAL lens: round 17
proved (O1) FALSE on non-generating admissible rows; the surviving
claim lives exclusively on generating rows (k = ord_n(p) = e), where
LEMMA 3 is EXACTLY SATURATED (margin 1.000). Your mandate: try to
break (O1) there too. A refutation on generating rows would make
mystery 2 false as posed regardless of the pending scope answer —
decisive either way for the Przemek note.

## 0. The state of record (sources; quote verbatim)

- notes/pilots_20260806/f2_adm/{REPORT.md, PROOFS.md} — THEOREM
  ADM-B (ratio = k/e nested / max(2,k)/e new-part, exact and
  scale-free; k = e => LEMMA 3 degenerates to Corollary 1.1's
  unconditional floor "and certifies nothing"), LEMMAS ADM-1/2/3,
  the exact dim L, the ladder at the witness row
  (p = 18446735827372343297, q = p^4, k = e = 4), the K1
  cancellation shortfall numbers, CATCH-6 (the coset domain).
- notes/pilots_20260804/f2_opening/PROOFS.md — (O1) as stated,
  LEMMA 3's derivation, what "certify" means in the chain.
- notes/pilots_20260804/f2_sl1_powersums/PROOFS.md — Z(L), the mass
  bounds, the random-subspace baseline.
- notes/pilots_20260806/t_naming/REPORT.md — the two live values of
  the Lambda parity convention (CATCH-E); your attack must state
  which reading each step uses and hold under BOTH or say which one
  it needs.

## 1. Pre-registered attack lines (run in this order; verdict each)

- **(V1) THE ZERO-MARGIN ATTACK.** At k = e the necessary condition
  holds with equality. Equality means ANY strict loss anywhere in
  the chain (a positive-entropy defect, a constant > 1, an o(n) that
  is really Theta(n)) kills (O1). Inventory the chain's steps on a
  generating row and hunt for one strict loss. Each candidate loss
  must be verified exact (is it truly lossless?) or exhibited as
  strictly lossy with the size of the loss.
- **(V2) THE COSET ATTACK.** f2_adm CATCH-6: the rules-level domain
  is a coset g·mu_n and the antipodal law fails off-subgroup. Does
  (O1) on the COSET domain lose a constant at generating rows? If
  the coset costs anything at zero margin, (O1) is false on the
  rules-level object even where it holds on the subgroup.
- **(V3) THE Z_1 LOWER-BOUND ATTACK.** (O1) at the moving rungs
  equals SL-1b' (Z_1 ternary mass of the explicit GRS code). Attack
  from below: construct ternary relations — CHECK FIRST whether the
  DLI stronger sibling applies: f2_sl1b found
  dli_wcl_newton_short_window_exclusion proves SL-1 STRONGER
  (wt >= 2R+1) under char > w, which FAILED on the KoalaBear tower
  (p ~ 2^31 < w) but on admissible rows p >= 2^39 (p ~ 2^64 at
  prize-max) — the hypothesis may now HOLD for the relevant weight
  range. If it applies, it CONSTRAINS your attack (and is a
  generative gift: cite it exactly, with the 6 counterexamples
  showing char > w is necessary). Then: does a ternary kernel
  element of weight in [2R+1, S] exist by counting/structure? An
  explicit family with Z_1 >= 2^{c·m} for any c > 0 refutes (O1) at
  zero margin.
- **(V4) THE EMPTY-CLASS SWEEP.** f2_adm CATCH-4 found one vacuous
  admissibility class. Enumerate ALL generating admissible classes
  (k = e, each e in {1,2,3,4,6} with v_2(e) <= 2 — note e = 3, 6
  need ord odd parts; derive exactly which (e_p, e) are generating
  AND non-empty, with a prime witness or a proof of emptiness each).
  If generating rows are EMPTY at prize-max (n = 2^41), (O1)'s
  surviving scope is vacuous — check this FIRST, it would decide
  everything (f2_adm's witness has k = e = 4, so at least one class
  is non-empty; verify its primality yourself, do not inherit).

## 2. Pre-registered falsifiers / honesty clauses

- Attacks that fail must be reported as SURVIVED-with-margin (state
  what the attack needed and by how much it missed), never silently
  dropped. The surviving minimal form of (O1) after all four attacks
  is the deliverable if no attack lands.
- Any successful attack needs a self-contained ramguard-tiny
  reproduction script and an exact statement of which (O1) reading
  (Lambda parity, window reading, coset vs subgroup) it kills.
- No attack may consume the t-naming identification (refuted); use
  the interval and both parity readings.

## 3. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/o1_generating_adversary/. Never edit
  dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/z1_ternary_mass/ (sibling this round —
  it works the same object generatively; independence required).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. Includes file patching
  and JSON peeking (three round-17 pilots breached exactly there).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.
