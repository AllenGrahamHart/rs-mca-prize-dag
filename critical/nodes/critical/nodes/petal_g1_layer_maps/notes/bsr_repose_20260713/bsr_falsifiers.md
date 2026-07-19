# bsr_falsifiers — pre-registered falsifiers for the branch-split re-pose
# (#101/#126 discipline: each states WHERE it is executable and whether it
# can fire at all; dead falsifiers are declared dead, not kept as decoration)

## Clause (P) — primitive branch (TARGET; these are the live kill-shots)

- **F(P)-1 [census excess].** An aperiodic FLOOR-BAND (d >= ell(t_ch - 2))
  full-petal contributor family at scaled official-like rows whose necessary
  weighted chart census exceeds (121/128) n^6, sustained across scales.
  EXECUTABLE: complete enumeration at n <= 32 any prime q = 1 mod n (the
  cg/ccd machinery, hours); engineered plants + first-moment extrapolation
  at n = 64..128 (Modal shards, the ccd stage-3 pattern). The odd-lift family
  CANNOT fire this one (floor-band cap 993 at (128,64) — bsr_check P3), so a
  firing family must beat the split-point mechanism: pre-registered
  expectation is NO FIRE at rho <= 1/4 (floor band empty of odd lifts,
  measured 0 at (32,12,97)) and the z <= 1 stratum only at rho = 1/2.
- **F(P)-2 [coverage escape].** A floor-band aperiodic full-petal
  contributor admitted by the band definition but covered by no legal
  (D0,R0) chart. EXECUTABLE at n <= 32 (complete; same machinery).
- **F(P)-3 [band tripwire — fires by ARITHMETIC, no run].** Pin P1 resolved
  to the wide/per-member band d >= ell(m-2) with no odd-lift carve-out.
  Then clause (P) is FALSE at (128, 64), every q:
  C(63,32) = 916312070471295267 ~ 2^59.7 > (121/128) 128^6 ~ 2^41.3
  (bsr_check P3 PASS on the inequality; the family is real — 6012 of 6435
  supply realized and verified end-to-end at (32,16,97)). This falsifier is
  SATISFIABLE and its firing condition is a maintainer DECISION, hence it is
  registered as a decision-gate, not a search task.

## Clause (D) — periodic branch (proposed PROVED; tripwires, not kill-shots)

- **F(D)-1 [coverage].** A chart word u1 with a realized consumed-band class
  (y_nf in S', |S'| in {k'+1, k'+2}) covered by no chart of the DD-atlas.
  STATUS: unsatisfiable as stated (a realized class's member IS a
  DD-interpolant; its minimal chart is in the atlas by construction).
  Retained as an AUDIT TRIPWIRE against implementation drift: executable
  verbatim at n' <= 32, any prime = 1 mod 2n', by complete enumeration
  (bsr_check P4 runs it at three cells; #137 nonemptiness asserted so a
  wrong-normalization vacuous pass cannot masquerade).
- **F(D)-2 [column excess].** |A'_{a'}(u1)| > 719 * Q_2(2a') at an in-scope
  cell. STATUS: unsatisfiable in scope (needs a'/(n'-a') > 719; grid max
  1.00196 — bsr_check P5). The satisfiable neighbors that MUST trip (and do,
  bsr_check P6): C_col = 1 (216 banked trips) and the shifted column
  C(n'-1, a'+2) (350 banked trips). Any future checker for clause (D) must
  include both mutations or is vacuous.
- **F(D)-3 [normalization vacuity, #137].** A clause-(D) checker reporting
  an EMPTY census at (16,8,97,consec), (32,16,97,geom5) or (32,12,97,geom5)
  — the banked pins are 3/63/47. Executable in seconds; wired into
  bsr_check P3.

## Gate (Lemma COL supplier) — premise guards

- **F(G)-1 [premise breach].** Any census cell at a consumed profile with
  classes > C(n/M, A/M). Would refute the stabilizer partition theorem or
  interpolation uniqueness — i.e. it guards PROVED upstream, and its firing
  escalates to petal_g2_support_forcing, not just the gate. Executable at
  every future census run (bsr_check P1 sweeps all 514 banked profile
  cells: zero).
- **F(G)-2 [seam].** A consumer charging a non-OWN cell (A > A_own; the
  widest-ALL cells h -> n'-1 where n/(n-A) is unbounded) against the gate.
  Executable by wiring audit (grep), and numerically at n >= 2^11 where the
  #101 excess first becomes arithmetic-reachable — THAT falsifier now lives
  HERE (at the seam), not at the gate's consumed cells.
- **F(G)-3 [landing].** First-scale dominance failing at an official shape
  in the dyadic_profile_evaluation M <= t extension, or the QA.22 re-run
  showing the 719-weighted extended ledger not absorbed by imgfib's reserve.
  Executable NOW as exact bigint for s <= ~24 and lgamma beyond (bsr_check
  P5 pattern); the extension worker owns the full grid.

## Cross-cutting mutation ladder (every future verifier must trip all four)

MC1 C_col = 1; MC2 shifted column; MC3 corrupted u1 (S2 identity + banked
pin break); MC4 the OLD (121/128) n^6 budget line at the g1a instances
(must FAIL — reproducing the falsification distinguishes the old and new
forms). bsr_check P6: 4/4 trip.
