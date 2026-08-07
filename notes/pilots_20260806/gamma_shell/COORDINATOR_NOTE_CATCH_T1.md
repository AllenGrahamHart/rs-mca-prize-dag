# Coordinator note (2026-08-07, round-22 CATCH-T1): a prose ambiguity in PROOFS.md

PROOFS.md:196-199 reads "the 8 accidents land on the 8 STRUCTURAL
shells" at (64,8), p=193. The 8 is a count of accident-occupied
SHELLS (toy_shell.out prints shells: total=8 struct=8 acc=8); the
round-22 bb_nu_transport pilot's exhaustive census (two independent
counters) finds 16 ACCIDENTS on those 8 shells (and 16 on 8 disjoint
odd shells at p=577). The banked ARTIFACT is correct; the prose is
ambiguous (shells vs accidents). No banked verdict is affected — the
theorems use the shell counts. Every column of the banked table was
re-verified exactly in the round-22 replay, including acc=0 at
p in {257,449,641} and all five (32,8) cells. Also CATCH-T2, for
future auditors: S(34) = C(128,63)/128 = 2^117.1491 (structural,
v=34) and M(128,62) = 2^117.0820 (unconditioned, v=35) are DIFFERENT
objects 0.067 bits apart — do not infer an off-by-one from the
near-collision. Source: notes/pilots_20260807/bb_nu_transport/.
