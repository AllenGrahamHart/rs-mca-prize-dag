# L-D core-count pilot — REPORT (2026-08-03)

(Persisted by the coordinator from the pilot's final message; REPORT.md
write harness-blocked. Pilot: Opus 5. Replay: ramguard local ->
ALL CHECKS PASS; falsifiers F1-F8 pre-registered, outcomes as listed.)

## VERDICT — two, because L-D has two inequivalent readings and the ratified note stated the wrong one

1. L-D AS LITERALLY WORDED — REFUTED (machine-verified). "(k+d)-subsets
   Z with A(Z)=B(Z)=0", with or without the L_P>=2 filter, is false —
   by 2^6.4e10 against a 2^81.4 budget at prize 1/4.
2. L-D IN ITS INTENDED (MAXIMAL/LEDGER) READING — OBSTRUCTED,
   obstruction named and ALREADY BANKED: with cores = FULL joint
   agreement sets, L-D IS the ledger's N_d, and route (1) reproduces
   step-for-step the banked notes/pilots_20260802/xr_band_occupancy/
   THEOREM 2 reduction. No new bound.
3. PARTIAL exact boundary: V* = 1.16600n (RowC) / 1.16619n (prize) vs
   the granted-both-lemmas 1.25n (prize 1/4) — a factor 1.072 gap; and
   banked PROPOSITION 5 says the slope side cannot close AT ALL
   (needs |Gamma_band| <= 1.32n^2, n/6 stronger than the open P-B
   budget).

## Key content

FIBER IDENTITY (proved): for |Z| = k+d, A(Z)=B(Z)=0 iff the unique
codeword pair (P,Q) = (I_Z(u), I_Z(v)) has Z <= W(P,Q); hence
RAW_d = SUM_{e>=d} MAX_e * C(k+e, k+d) — the raw subset count
explodes combinatorially (RAW_1 = 334 = 4 + C(11,7) on the fixture).
The L filter is monotone under subsets — powerless (330 > 272).
The consolidation note's "pairwise <= k-1" holds for MAXIMAL cores of
DISTINCT pairs only; raw subsets of one deep W share up to k+d-1
points (fixture: overlap 6 = k). Upstream nodes are CLEAN (they
define N_d via codeword pairs / maximal joint agreement); the defect
is confined to CONSOLIDATION.md sections 2 and 4.

REFUTING FIXTURE: n=20, k=6, h=6, A=12, q=101, d=1, budget 272; a
cascade-tier codeword pair (joint agreement exactly 11) + two exact-A
live slopes with unique maximisers; RAW_1 = 334 > 272; with L>=2:
330 > 272; N_1 (maximal, L>=2) = 0 — the intended reading untouched.

PER-ROW: a SINGLE band pair at depth d+3 breaks RAW_1 at all three
prize rows (depth d+3 well inside the band proper, h-2 ~ 2^33); the
0.68n^2 budget is VACUOUS at the three RowC rows (their own
requirement ~6.4e61) — only the prize rows are obligations.

ROUTE (1) = BANKED (hard law 5): per-slope multiplicity = punctured
[A,k] MDS list size at agreement k+d (THEOREM 2); N_d <= min_z
#{c : agr(c, w_z) >= k+d}; partial linear space + Gamma_band/2
(THEOREM 4); the dimension count is banked DEAD; the agreement-counts
leg ("codewords near u and v separately") is REFUTED machinery —
xr_band_key_lemma_pencil_mass's explicit non-claim (worst-case lists
2^130-2^197); COROLLARY I.1 bounds pencil SLOPES near a codeword,
never CODEWORDS near a word. The banked terminus: the binding half =
"some pencil member has <= 0.80/0.686/0.660 n^2 codewords at
agreement >= tau = k + ceil(h/2)" — tau ~ 1.008k-1.016k, 25-50% of
Johnson: the species of positive target #1.

## Recommended corrections (surfaced)

(1) L-D wording -> "codeword pairs whose joint agreement set has size
EXACTLY k+d" (maximal); (2) section 2's final sentence -> cores of
DISTINCT pairs; (3) cite xr_band_occupancy THEOREM 2/4 + PROPOSITION
5 and the DEAD dimension count; flag RowC vacuity.

## Falsifiers (pre-registered): F1 FIRED, F2 FIRED, F3 held (N_1=0),
F4 held (334=334), F5 held, F6 FIRED (overlap 6=k), F7 CONFIRMED
(route banked), F8 consistent.

## Flags: RowC vacuity; fixture h even (mechanism only; the rows carry
the arithmetic); fixture at cascade tier (in scope for the column;
prize rows refuted from inside the band proper, g*=3); N_1=510 is a
consistency-checked formula, not derived; no node changed.
