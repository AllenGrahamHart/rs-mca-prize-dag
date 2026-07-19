# Proof — petal_g1_layer_maps, clause (P) (the node's full remaining content)

Banked 2026-07-13. Worker packet: `notes/cp_packet_20260713/`
(cp_statement.md = theorem + pins + consumed-hypotheses table;
cp_proof.md = Lemmas A–C + atlas theorem + complement analysis; this
file is the condensed artifact of record). Fresh-context adversarial
audit: SOUND, zero mathematical defects (cpa_report.md, 16-row
link-by-link table; cpa_findings.md catches #172–#176; cpa_checks.py
independent battery, 37 PASS 0 FAIL).

## Statement (as posed; layout-anchored — pin #168)

At the official rows, the APERIODIC top-band atlas supply at the FLOOR
BAND `d >= 2(t_ch - 2)` admits a word-independent chart atlas whose
weighted census is at most `(121/128) n^6`.

## Proof skeleton

**Lemma A (band boundary).** On even-`k` two-power rows the floor band
admits odd lifts iff `z0 = (k/2 - 1) - (t_ch - 2) >= 0`, operationally
`2k >= n - 2`; in scope this collapses to `2k >= n` by parity. (The
formerly printed `2k >= n - 1` is the odd-`k` formalization artifact —
catch #175; out-of-scope divergence witnessed at (10,4,11).)

**Lemma B (support rigidity — the engine).** Floor band + full-petal +
`|S| >= k+1` force: core agreements `j <= J = k + 3 - 2 t_ch`, and
touched petals `m in {t_ch - 1, t_ch}`. Sharp: the corner
`(j = J, m = t_ch - 1)` sits at `|S| = k+1` exactly, via the identity
`J + 2(t_ch - 1) = k + 1`; the stratum `m = t_ch - 2` is arithmetically
impossible. (Audit: exhaustively verified over 1770 layout shapes,
`n <= 64`, both `k` parities, `b0 <= 1`; zero violations.)

**Case rates <= 1/4 (official n = 2^42, 2^43, 2^44).** There `J < 0`
(J = 3 - 2^41, 3 - 6·2^40, 3 - 14·2^40), so the floor band is EMPTY for
ALL contributors — not only the #145 hazard family. Clause (P) holds
with the empty atlas. In-vivo confirmation: complete census at
(16,4,97) = 51 contributor classes, zero floor-band; emptiness at rates
1/4, 1/8, 1/16 for all s = 13..44.

**Case rate 1/2 (official n = 2^41).** `J = 3` at every row size. The
explicit atlas `{(D0, R) : D0 in Z, |D0| >= 2(t_ch - 2), R in B}` (full
petal set per chart, legal K4 band, `|R0| < ell`, both retained
flavors) covers every floor-band full-petal contributor — aperiodic and
periodic — by Lemma B; its weighted census is exactly
`N_max = 2 (t_ch + 1) S_3(k - 1) ~ n^4 / 96`. At `n = 2^41`:
`log2 N_max = 157.4150` against budget `log2((121/128) n^6) = 245.9189`
— margin `2^88.5`; verified for all rate-1/2 rows `s = 3..44` (worst
margin `2^12` at `s = 3`).

**Per-chart K4 line, word-free.** Within an atlas chart a contributor
class is determined by its touched petal set (`<= t_ch + 1` options),
so the K4 `m + 1` bound holds for these charts by support counting
alone — no layer-map/dictionary transport is consumed, and the atlas is
word-independent (received-word uniformity dissolves at the floor
band).

**Layout anchoring (#168, load-bearing).** The clause is proved for the
LAYOUT-ANCHORED band. The audit verified every consumer (petal_growth
pin P1, K4's charts, the census gate's layout-free support band)
consumes exactly this semantics. The layout-existential reading is
FALSE: core re-basing places every `|S| = k+1` lift inside a tailored
layout's floor band (witness: a z=7, d=0 lift becomes d*=14 floor-band;
kill arithmetic `C(63,32) = 2^59.67 > (121/128)·128^6 = 2^41.92`).

**Hazard separation.** Both banked hazards obey `j <= 3`: the #145
odd-lift mass enters only at `z <= z0` (the banked 993 + 31 = 1024 caps
at (128,64) embed in `N_max = 2,754,048`), and the #138 exponential
periodic mass sits at large `j`, never floor-band. The #153
both-subfamilies cap is the LIFT-family account (catch #170); the
full-band account is the rigidity census.

## Verification record

- `notes/cp_packet_20260713/cp_verify.py`: 62 PASS 0 FAIL (ramguard
  tiny; stages P1–P7; complete brute cross-validation at (16,8,97) and
  non-coset layouts; banked pins 8/53/48/0 reproduced; fresh
  never-banked cell (32,16,257,geom3); dual-method lift-census
  agreement; 4 REQUIRED-TO-TRIP mutations; exact bigint grid
  s = 3..44; #174 lift-nonemptiness repair applied at banking).
- `notes/cp_packet_20260713/cpa_checks.py` (independent audit battery):
  37 PASS 0 FAIL — Lemma B exhaustive (1770 shapes); independent
  censuses via the k-subset method, Lagrange-only interpolation, and a
  functional lift test reproduce 10/83/51-0 exactly; quotient-side
  recount agrees set-exactly; new mutations NM1–NM3 all trip.

## Scope and standing tripwires

Top band, full-petal, official rows, layout-anchored. Mixed-petal and
below-top are petal_growth's separate obligations (#171 note there;
mixed-petal floor mass is 4x full-petal at the smallest cell — catch
#176 — and is explicitly out of scope). TRIPWIRE (P)-3: a maintainer P1
wide-resolution re-opens the clause (pre-registered re-surgery
criterion).
