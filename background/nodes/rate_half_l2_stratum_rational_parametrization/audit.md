# Audit

1. The status carries the (RES) split explicitly: the biconditional is NOT
   claimed at PROVED, because the coordinator hand-check list covers the
   forward direction only; the backward direction is a 1200/1200
   measurement. This was the drafting pilot's forced correction and it is
   preserved verbatim.
2. `verify.py` checks (DET)/(SYZ) on 120 draws over two fields and settles
   the third-condition implication EXHAUSTIVELY over `F_13^4` (144
   exception tuples, all `f = g = 0`, matching `(q-1)^2`);
   `verify_audit.py` goes further: (DET) and both syzygies are proved
   SYMBOLICALLY over `Z[f,g,h,k,z]`, which covers every field at once and
   upgrades those two components from sampled to identity-proved.
3. The banked witness is recertified twice by genuinely different code:
   the draft verifier re-derives it inside its own framework; the audit
   derives `Q_j` by exact division per (PAR) and certifies the pencil with
   the coordinator's round-38 elimination path (nullity 1, generic rank 7,
   single drop `z = 89 -> 6`, full rank at infinity, no deg<=1 kernel).
4. The T = 3 scope bullet was stale at wiring (round 38 achieved it); the
   statement now records the closure with its mechanism (scale
   elimination, NOT a third exact solve — round 37 proved no third exact
   solve exists) so the ladder's history remains readable.
5. The `f(ell) = g(ell) = 0` exception is nonempty and exhibited — the
   two-conditions claim is scoped, not absolute.
6. Edge character: evidence only; no requirement discharged.
