# SUPPORT-5 / E1-FAMILY DEFICIT — pilot report (Opus 5, 2026-08-03)

(Coordinator-persisted; write harness-blocked. Replay: ramguard local
--full -> 168 checks, 0 FAIL, 0/17 falsifiers; PREREG pre-dated, with
an honest pre-run amendment A1 correcting a self-inconsistent row.)

## VERDICT: EXISTS — machine-verified fixtures, including at the E1 pin

Gate-clean all-escape-1 systems with dim Ann >= 1: PF1 (q=11,k=3,h=4,
V=4: dim Ann 1, charge 3.25, FULL BAND GATE PASSED — all four
escape-1 rays live at agreement exactly A); PF2 (q=29,k=15,V=10:
dim Ann 1, rank 19 = 2m-1, CHARGE 1.9 < 2); PF3 = THE RECORD'S OWN E1
PIN (q=31,k=19,h=4,V=12): dim Ann 1, rank 21 = 2m-1, CHARGE 1.75;
PF4 (dim Ann 3); PF5. Plus PROP 0: private (mult-1) escape points
give dim Ann >= #private FOR FREE (PF8: V=12 consecutive supports,
deficient for EVERY slope tuple, charge 1.833).

## Proved

THEOREM E1-RED: dim Ann = nullity of a (V-2)(h-1) x 2s system +
#mult-1 points (three-way machine-checked). THEOREM E1-PENCIL: blocks
= V fibres of one degree-s pencil + Mobius-matched slopes gives
dim Ann = 2s-h+1 >= 1 across the whole gate window ceil(h/2) <= s <=
h-2 — every gate-clean E1 shape admits a deficit. THEOREM D becomes
TIGHT (first tight family, 5 fixtures at equality). Consistency with
THEOREM F exact (the complete-block shape sits one condition higher;
the +1 is the escaped point's freed equation). THEOREM E1-CLASS at
2s = h: deficit iff pencil+Mobius — EXHAUSTIVELY decided at the
smallest shape (680,400 cases: 1,680 deficits, 0 unexplained; both
controls exhaustive). Why 820+434 prior tuples missed it: fixed
consecutive supports — the collapse pilot's 5.2 blindness verbatim.

## Upstream consequences (surfaced)

1. escape1_realizability implication 4 REFUTED (pure escape-1
   counterexamples CAN be realisable; PF1 full-gate).
2. Its sharp open question CLOSED affirmatively at the allowed pin.
3. THEOREM D tight.
4. lb flag-6 attack surface DISSOLVES: the deficit is a SUPPORT-4
   phenomenon (PF1 basis profile {4:3}; the broken step is
   "L <= C_{intersection}" — c_a in C_{S_a} holds only for its own a).
5. LEMMA R near-vacuous on systems with private points (mult >= 2
   hypothesis does real work; write it down).
6. The heart must exclude these beyond gate-clean + LEMMA R; m = V
   suffices for charge defeat at dim Ann = 1.

## Flags: 5 upstream addenda owed; E1-CLASS proved at 2s = h only
(2s > h argued-not-proved; existence unaffected); toy q <= 37 but the
construction is a formula at any scale (s | q-1); full gate verified
on PF1 only (PF2/PF3 = the standing COMPUTE REQUEST); PROP 0 is a
re-reading; consumed-not-rederived list in the message; compute law
kept; PREREG amendment A1 recorded honestly.
