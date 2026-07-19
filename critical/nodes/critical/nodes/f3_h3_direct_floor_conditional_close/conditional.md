# Conditional packet

- **route:** C36' -> [trace-zero payment, REPAIRED envelope A_3^0 <= R^2 <=
  I^2/36 < (4/9)n^(4/3); catch #71] + [splitting-reduction bijection
  A_3^nz <= N_3to1/36] -> T_3 <= n^2/72 + n(A_3^0 + A_3^nz) <
  n^2/72 + (4/9)n^(7/3) + (n/36)(36n^2 - 16n^(4/3) - n/2) = n^3 EXACTLY.
- **verified:** fresh-context audit 2026-07-10 (32 exact checks, 2 mutation
  controls, counterexample to the unrepaired envelope banked:
  ../u1_x4_direct_column_budget/notes/cx_amber_audit_20260710.py).
- **re-surgery:** C36' falsified; the repaired envelope breached (a
  {P,-P}-class miscount at any row); the splitting bijection's 2-group /
  nonzero-trace hypotheses violated by a convention change.
