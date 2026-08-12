# Audit

1. The mechanism is proved as an identity (parity pairing + the residue
   identity), then checked directly: the verifier confirms the odd-row
   collapse on all 1158 covering even locators it scans, as sets.
2. The count (CNT) is derived and then tested against all six banked cells,
   including a negative control: `C(m-1, r/2-1)` is asserted NOT to match
   when `off != 1`, so the correction to the banked form is itself under
   test.
3. `verify.py` scans with syndrome vectors and Hankel matrices;
   `verify_audit.py` shares no code path — weights via `1/P'(x)`, pencil
   conditions as direct functionals with pointwise sigma, covering counts
   by enumeration, and fresh fields at the rho = 2 cells.
4. Wiring-audit catch: the rho >= 3 zero-count is GENERIC in `q`, not
   field-uniform — the audit found the accidental covering solution at H4
   over `q = 1009` at the predicted `~165/q` rate (recorded in
   `certificate.json`). The statement now carries the qualifier explicitly;
   the razor kill's surplus (`2^33 - 1` conditions) is untouched.
5. The MISS-2 guard is enforced in both verifiers: locator counts and
   distinct-slope counts are asserted separately at H3 (330 vs 329), and
   the slope sub-count is only checked at the banked field, where it is
   structural.
6. The draft's rho >= 3 symmetric-T gap was closed by rounds 37-38 after
   drafting; the wired statement records the closure instead of the gap,
   with pointers to both A1 addenda.
7. No numerical survival evidence is promoted; the exhibits sit at
   `r > R/2` by construction and the statement says exactly what shape
   they fence.
