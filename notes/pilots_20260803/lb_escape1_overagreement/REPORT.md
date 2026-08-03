# L-B: ESCAPE-1 OVER-AGREEMENT — pilot report (Opus 5, 2026-08-03)

(Persisted by the coordinator; REPORT.md write harness-blocked.
Replay: ramguard local -> 237 checks, 0 FAIL, exactly 1 of 10
pre-registered falsifiers fired (LB-F2); PREREG pre-dated.)

## VERDICT — PARTIAL with exact boundary, plus one refutation

1. L-B's CONCLUSION (V_1 = 0) PROVED on the group-fibre/pencil-block
   class — every realisable admissible family the campaign knows
   (E1P, Zfib11, X0/X1p bases, all group-fibre systems).
2. L-B's stated MECHANISM REFUTED (LB-F2, 5 fixtures): an escape-1
   core ray CAN be exact-A. Over-agreement is forced only when the
   escaped point is PRIVATE (multiplicity 1); at multiplicity 2 the
   ray sits at agreement exactly A.
3. DICHOTOMY THEOREM (proved): L-B holds at a ray iff a forced
   over-agreement point exists (some Psi_y == 0 on the realiser
   space); else (all Psi_y != 0, q > (n-A)+n+1) a nondegenerate
   exact-A realiser EXISTS. No weaker argument can prove L-B.
4. NEW DEPENDENCY: L-A => L-B. Residual open statement = exactly
   L-A. Drop L-B as an independent target.

## Proved content

LEMMA P (private-point freedom): a multiplicity-1 escaped point
contributes one free equation; dim Ann(peeled) = dim Ann + 1.
THEOREM F (fibre rigidity, 16/16 machine-checked): for V >= 3
distinct fibres of x -> x^d over a subgroup H, the ray condition is a
QUADRATIC in the fibre parameter c_a; three distinct parameters pin
Ann completely (dim Ann = max(0, d - max(0, h-d))), independent of V.
COROLLARY F1: the E1P over-agreement phenomenon (520 samples) is now
a THEOREM — the extra agreement point is exactly the removed point
(12/12 draws confirm prediction P1). COROLLARY F2 (corrected in-run;
one conjecture retracted honestly): repairing from inside the block
also forces over-agreement (measured dim Ann up to 3 — the
realisability-kill conjecture was false, the over-agreement proof
replaced it). LEMMA V4: complete block systems have multiplicity
V-1; escape needs r >= V-3 perturbed rays, all forced over-agreeing;
<= 3 survive; LEMMA B empties the core. THEOREM G: >= 3 live
group-fibre rays => every core ray escape 0, V_1 = 0.

## The refutation (LB-F2)

X1p(17,6,4): escapes (1,1,1,0), rank/2m/dimAnn = 19/22/3, agreement
profile (14,12,12,12) — the two mult-2 escape-1 rays sit at EXACTLY
A = 12. Also X1p(13,4,3) and the new SWAP family (3 fixtures).
The conclusion still survived every fixture: the forced ray dies,
V drops 4 -> 3, LEMMA B empties the core, tangent-freeness fails.

## Flag-6 sibling question (all-escape-1 deficit): still NO, explained

31 shapes x 434 tuples, no deficit; every such shape has 4-wise
intersection < k+2, so the S4-5/S4-6 pencil picture forbids support-4
relations — a deficit needs support >= 5. Attack surface named.

## Flags

LB-F2 fired (mechanism refuted, conclusion intact). In-run retraction
recorded. Toy scale q <= 43. THEOREM G's "no undesigned live slope"
verified per fixture, not general. DICHOTOMY counting needs
q > 2n+1-A (comfortable at prize rows). COMPUTE REQUEST inherited:
wiring the complement-enumeration oracle into occlib.measure decides
LB-F1 at m >= 9. Consumed not re-derived: LEMMA R/B, THEOREM D,
U1/U2, collapse 1/1'', S4-5/6, occlib semantics.
