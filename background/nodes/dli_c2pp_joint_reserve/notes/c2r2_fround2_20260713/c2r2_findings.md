# C2'' F-ROUND 2 — FINDINGS (catches c2r2-C1 .. c2r2-C5)

Fresh-context falsification worker, F-round 2, 2026-07-13. Node
`dli_c2pp_joint_reserve`. Evidence only; nothing here proves C2'', B-WEAK, or
the DLI target. Repo untouched (READ-ONLY).

## c2r2-C1 — F-b SCORED for the first time; the reserve is barely touched

M1 explicitly DEFERRED F-b ("needs the packet transport arithmetic"; printed
only an unscored bulk-charge diagnostic). Round 2 scores it using the packet
arithmetic pinned in `m4_assembly_verifier.py::gate_calibration` (lines
402-417) and confirmed in `m4a_findings.md` l.42: a replayable tower is one
junction ratio `x` stacked over 33 junctions, charge `x^33`, firing iff
`x^33 > 2^21` (exact Fraction). The surviving three-part shape stacks the
clause-(ii) BULK ratio and prices accidents ABSOLUTELY (once, q-independent).

Result over ALL 56 rows (8 n=32 calibration + 48 n=64): worst BULK = 1.066159
(n=32 t=3 q=193) → 1.066159^33 = **2^3.05**; worst absolute accident charge
2^0.0009; total worst tower charge **2^3.0508 = 14.53 % of the 21-bit
reserve** — ~18 bits (85 %) of margin unused. F-b NOT fired.

Load-bearing check (mutation MUT-i): scoring the SAME transport on the
coset-stripped-but-not-accident-priced ratio fires immediately (2.8742^33 =
2^50.26 at n=32 t=4 q=97). So the gap between "fires" and "clears with 85 %
margin" is exactly the clause-(iii) accident pricing — it is doing real work,
not cosmetic. The 2.874^33 / 2.752^33 values are the pose's banked
per-junction-uniform NOT-falsifier, correctly excluded.

## c2r2-C2 — the coset-stripped, accident-priced BULK is empirically ≡ 1 across 8 octaves / 2 depths

The clause-(ii) object carries essentially zero signal at n=64. Over t=2
octaves 7–14 (q 193 → 17729, widened one octave beyond M1) and t=3 octaves
7–9, every bulk ratio is 1.000 to <1e-3; the largest departure anywhere at
n=64 is 1.0007 (the new octave-14 q=17729) and 1.0019 (M1 q=7937). All of the
raw junction ratio — up to 8.40x (n=32 q=32801) — lives in the coset column
(clause i, exact accounting) and orbit-quantized accidents (clause iii). A flat
bulk gives octave-slope s_j ≈ 1/(j+0.5) which DECREASES (0.1333 → 0.0690 over
j=7..14), so F-a's kill (super-polylog growth at ≥2 depths) is structurally
out of reach unless the bulk itself departs from 1 — which it does not, wider
than M1. This is the central empirical support for clause (ii).

## c2r2-C3 — ZERO accidents even at theta = 1; the rare window is anti-correlated (strengthening of clause iii)

Across all 48 n=64 rows, NO k>=1 class is flagged an accident at theta = 2 —
and the theta spot-check plus the local theta=1 probe show 0 accident cells
down to theta = 1: the k=3 rare weight-3 window has conditional mean ≤
mean-field for every census row (anti-correlated, not merely sub-threshold).
The window-law Poisson test therefore sees X=0, T=0 (p = 0.0237, two-sided, on
34 rows). This is STRONGER than clause (iii)'s theta=2 pricing requires — the
accident budget it charges against the reserve is, empirically, not even
populated at these shapes. (Consistent with the n=32 calibration where the four
accident classes were exact orbit multiples 128/128/64/128, window-priced.)

## c2r2-C4 — HONEST DEFERRALS (compute-bound; not cleared)

Round 2 is a genuine but bounded extension. NOT run, explicitly deferred, and
NOT to be read as cleared:
- F-a "deeper" 3rd depth t=4 (q=193, g=2 4-D grid, ~194 direction chunks) —
  M1's own p3 stretch, off by default; the F-a kill formally needs ≥2 depths
  and both M1 and R2 tested exactly 2. R2 went WIDER (t=2 to octave 14) not
  DEEPER. A true 3rd-depth test remains open.
- F-a t=3 octave-10 (q=1153, ~385 chunks) — t=3 octave range unchanged from M1.
- F-c 40+ row census — each new fixed-shape row needs q>10369 (30+ chunks);
  R2 reached 34 rows (>30, armed), not the larger census.
The deferrals are compute, not evidence: nothing observed suggests any would
fire (bulk ≡1 wider, window anti-correlated), but they are unproven here.

## c2r2-C5 — PROCESS: full-grid routing must key on q^t, caught pre-launch

The Round-2 planner initially sized the full-grid-vs-shard decision with
`q^(g+1)*33` (the PER-DIRECTION grid), not the TRUE full grid `q^t*33`. For a
high-q t=2 row this mis-classifies a 36 GB full grid as 3.9e5 cells and routes
it to a single 16 GB full-grid worker → OOM. Caught by a dry-run chunk-count
sanity check BEFORE any Modal spend and fixed (route on `q^t*33`; shard g=t-2).
Guidance for future rounds: always print the realized grid bytes per worker in
the dry run and assert < worker memory.

## Verdict inputs (banked)

- All positive controls (local 8-row + GM 0.967; modal shard-0; modal t=3 q=193)
  and all three required-to-trip mutation controls PASS.
- No pre-registered falsifier fired within the scope run.
- Nonemptiness asserted throughout (sum(an)=3^32, projection exact-division,
  n_null>0, ≥30 census rows before the F-c read, ≥5 positive bulk rows for GM).
