# UNIFIED PENCIL BOUND — PRE-REGISTRATION
Opus 5 proof pilot, 2026-08-03 17:48 UTC.
WRITTEN BEFORE ANY COMPUTATION IN THIS PILOT. No verify.py exists yet.
(A prior run of this pilot was killed by a crash before creating any
files; nothing was salvageable, so this is a clean re-registration.)

## THE ANCHOR (ratified statement under test)

For a FULL-GATE admissible received pair (u,v) on n evaluation points,
the number of live slopes whose selected supports are PENCIL-STRUCTURED
(complement blocks = fibres of one polynomial pencil, possibly plus a
common core) is <= C n, with explicit C.

## Definitions of record (fixed here, not adjustable after computing)

Row2(n,k,h,q), A = k+h, m = |U|-k, R = n-k.
* FULL GATE := s4lib.gate_report(row,u,v)["FULL_GATE"] (below_cascade,
  globally_generic, tangent_free_finite_slopes, tangent_free_v_direction,
  v_nonvanishing, kpacking_ok).
* LIVE slope z in P^1(F_q) := max agreement of w_z = u + z*v with the RS
  code equals EXACTLY A. Selected support S_z := the agreement set.
* Complement block A_z := U \ S_z, U := union of selected supports.
* A set F of live slopes is PENCIL-STRUCTURED with core A_0 and degree s
  iff there is a 2-dimensional space W = <w,w'> of polys of degree <= s
  and distinct parameters c_z in P^1 with A_z = A_0 disjoint-union B_z,
  B_z = {x in U : (w - c_z w')(x) = 0}, |B_z| = s, B_z pairwise disjoint.
* L_pencil := # live slopes lying in some pencil-structured family of
  size >= 3. (Size <= 2 is EXCLUDED BY DEFINITION and the reason is
  registered as Q0 below.)

## Q0 (registered before computing, as a definitional claim)

CLAIM Q0: any two disjoint equal-size blocks B_1,B_2 are fibres of a
common pencil (w = monic poly with root set B_1, w' = with root set B_2;
c=0 and c=inf). Hence "pencil-structured" is VACUOUS at family size 2
and the anchor is only meaningful for families of size >= 3.
PREDICTION: TRUE.
FALSIFIER UPB-F0: an equal-size disjoint pair not realisable as two
fibres of a degree-s pencil.

## Pre-registered questions, predictions, falsifiers

Q1 (INJECTIVITY). Under the FULL GATE, distinct live slopes have
DISTINCT selected supports.
PREDICTION: TRUE. Reason to be checked: if z != z' share support S then
v|_S and u|_S both lie in C_S, so max_joint_agreement >= |S| = A, which
violates globally_generic (maxJ <= A-1).
FALSIFIER UPB-F1: a FULL-GATE (u,v) with two live slopes sharing a
selected support.

Q2 (BLOCK SIZE >= 2). For gate-clean admissible systems the block size
s = |A_z| - |A_0| satisfies s >= 2.
PREDICTION: TRUE for h >= 4; UNDECIDED (flagged) for h <= 3.
FALSIFIER UPB-F2: a gate-clean admissible pencil-structured family with
s = 1 (which would give up to n live slopes from ONE pencil and force
C >= 1).

Q3 (ONE PENCIL, exact). For a single pencil-structured family with core
A_0, degree s, V live slopes: |A_0| + V*s <= |U| <= n, hence
V <= (n - |A_0|)/s <= n/2.
PREDICTION: TRUE; tight at s=2, |A_0|=0.
FALSIFIER UPB-F3: a single-pencil FULL-GATE family with V > n/2.
CALIBRATION (pre-registered numbers): Zfib11 has V=11, n=22 => V = n/2
EXACTLY (so C >= 1/2 and Q3 is tight). PF2 has V=10, n=25 => V = 2n/5.

Q4 (ESCAPE VARIANTS). For escape-1 families U also contains the escape
set Y, |Y| = V (private) or ceil(V/2) (matched), so
n >= |A_0| + V*s + |Y| gives V <= 2n/5 (matched, s=2) and V <= n/3
(private, s=2).
PREDICTION: TRUE; tight at PF2 (V=10, n=25, matched, s=2).
FALSIFIER UPB-F4: an escape-1 FULL-GATE family violating these.

Q5 (TWO PENCILS SHARE <= 2 FIBRES). Distinct pencils P != P' have at
most 2 common fibres.
PREDICTION: TRUE (3 common fibres span a 2-dim space equal to both).
FALSIFIER UPB-F5: two distinct pencils (poly_span_dim of the union >= 3)
with 3 common fibres.

Q6 (THEOREM F ACROSS PENCILS — THE REAL QUESTION). If pencil P has >= 3
live fibre-rays for (u,v), THEOREM F pins the realiser class of P. Let
M := # distinct pencils each carrying >= 3 live slopes for the SAME
FULL-GATE (u,v).
PRE-REGISTERED BRANCHES (I commit to reporting whichever occurs):
  (a) M <= 1 always  => L_pencil <= n/2, C = 1/2.
  (b) M bounded by an absolute constant M_0 => C = M_0/2.
  (c) M unbounded but the block-union still forces L_pencil <= C n.
  (d) EXPLICIT MULTI-PENCIL COUNTEREXAMPLE with L_pencil > n.
PREDICTION (registered): branch (c) — I expect M can exceed 1, but the
blocks are distinct subsets of U (Q1) and I expect the disjointness
inside each pencil plus the gate's pairwise/triple conditions to hold
the total near n/2. I explicitly register that I may be WRONG here.
FALSIFIER UPB-F6: a FULL-GATE (u,v) with two DISTINCT pencils each
carrying >= 3 live slopes AND total pencil-structured live slopes > n/2.

Q7 (THE HEADLINE FALSIFIER). A FULL-GATE admissible pair (u,v) with
MORE THAN n live pencil-structured slopes across pencils.
PREDICTION: DOES NOT EXIST.
FALSIFIER UPB-F7: exhibit one. This REFUTES the anchor as stated.

Q8 (RANK / ROW ACCOUNTING). Each live slope contributes h condition
rows; total rank <= 2R - 1 under the gate (v_nonvanishing kills one
direction); THEOREM B floor rank >= 3h; THEOREM D ceiling rank <= 2m.
PREDICTION: rank <= 2m and rank <= 2R-1 both hold on every fixture; the
per-slope row count does NOT by itself give a linear-in-n slope bound
(the rows are massively dependent) — so this channel CALIBRATES but does
not prove the anchor.
FALSIFIER UPB-F8: a fixture with rank > 2m or rank > 2R-1.

Q9 (TOY EXHAUSTIVE MULTI-PENCIL SEARCH). At toy scale (q <= 31, small
n,k,h) exhaustively search block configurations admitting >= 2 pencils
with >= 3 live slopes each.
PREDICTION: such configurations exist COMBINATORIALLY but fail either
the gate or realisability (no FULL-GATE (u,v)).
FALSIFIER UPB-F9: a realisable, FULL-GATE multi-pencil configuration.

Q10 (CONSTANT). The explicit constant.
PREDICTION: C = 1/2 on the single-pencil class, and I will report the
best PROVED C across pencils. If I cannot close (2), I report PARTIAL
with the exact boundary rather than inflating C.
FALSIFIER UPB-F10: any FULL-GATE fixture beating the C I finally report.

## Compute law
tools/ramguard tiny|local -- python3 ...  from repo root, literal --.
No Modal, no network. All sibling machinery imported READ-ONLY.

## Honesty rules for this pilot
Any in-run amendment is appended below with a timestamp and the reason,
never by editing the text above. Fixture-level surprises are reported
even when they do not fire a registered falsifier.
