# Audit

1. This node is a LEDGER: its own status is TARGET (the exact value), and
   every component carries its own status in an explicit table — two
   REFUTED rows included. Nothing here upgrades the floor to unconditional
   or the cap to algebraic.
2. The re-draft was a recorded pre-condition (the draft predated the
   refutation by hours); the draft's still-valid PROVED arithmetic is
   carried verbatim, and everything U-conditional was rewritten, not
   patched.
3. `verify.py` replays the banked arithmetic including the new round-37/38
   constants; `verify_audit.py` shares no code path — alternate integer
   decompositions, a float-free binary-digit log2 extractor (which also
   pinned down that the banked six-decimal figure is the ROUNDING of
   39.9772799..., not the floor), factorial-based binomials, and a fresh
   delta grid for the exchange optimum.
4. The C3 `T = 19` exhibit and the `17.17x` margin are cited with their
   banked provenance and deliberately not recomputed (they need the
   round-38 census machinery, not arithmetic).
5. The mu_26 in-normal-form cap 18 is recomputed from the exchange law and
   matches the banked correction of the round-37 census (T = 17 was
   search-limited); the audit asserts the cited outside-form T = 19
   EXCEEDS it, which is the normal-form-conditionality claim in one
   inequality.
6. Edge character: evidence only. The node discharges no requirement; it
   exists so the far-CA residual map has a single citable home off A1.
