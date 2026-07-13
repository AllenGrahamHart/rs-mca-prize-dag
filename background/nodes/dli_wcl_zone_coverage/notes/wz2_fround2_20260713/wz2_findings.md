# wz2_findings.md — F-round 2 catches and structural findings (local numbering wz2-C1..C8)

- **wz2-C1 (MAJOR, spec-level: deduped-C1' fails EXACTLY at the banked
  accident row — the M3 interface is internally inconsistent).** The M3
  CORRECTED POSE defines `W_cl` "after ... first-owner de-duplication of
  multiplier shadows and level lifts" and then uses the SAME symbol both
  in the zone bound `W_cl <= 1/32` and in the C1' allowance
  `E_L <= 1 + 4 r_L (1 + W_cl)`. Dedup only shrinks the ledger: it HELPS
  the zone bound and TIGHTENS the allowance. Under the canonical spec
  (`wz2_dedup_spec.md`, defaults ratified provisionally), the banked row
  `(L=1, q=7937)` goes `W_cl = 236 -> W_canon = 8` (lift pass: 3 orbits
  owned by the ADMISSIBLE `N=16` companion — a companion no banked
  artifact ever priced; shadow pass: 1240 exact ternary-multiplier links
  collapse the remaining 164 orbits), and the EXACT rational check gives
  `E - 1 > 4 r (1 + 8)`, i.e. `K'_dedup = 6.5019 > 4`: **C1' with the
  pose's own deduped ledger is refuted at analogue scale** (the other 7
  audited banked rows survive; c1audit app
  ap-pm0Q3Xmwm2820HjzBjmHvx). Banked M2's survival was for the RAW
  ledger only. Consequence: the corrected M3 pose cannot stand as
  written — either WCL-ZONE must price the RAW primitive ledger (drop
  the dedup phrase from the zone predicate; the assembly then needs
  `W_raw <= 1/32`), or C1' must be re-posed with the deduped ledger,
  which is now REFUTED in its literal `K' <= 4` form. Pre-declared NK-5:
  this is a finding about the pose interface, not a WCL-ZONE kill. It is
  the concrete payoff of the #191/wz-C2 debt: the missing dedup spec was
  hiding an inconsistency in the node's own downstream assembly.
- **wz2-C2 (family-B trend resolved: turnover, O(1) correlation
  factor).** With b15 (K=384) and b16 (K=384) added, the round-1
  monotone rho sequence 1.615 -> 2.395 -> 4.648 continues 3.62 -> 0.00:
  monotonicity breaks at b15 and b16 is EMPTY (0/384 vs 0.106 null
  expectation). The b14-deep diagnostic (K=96: 3 witnesses, rho 6.71,
  P ~ 1.1%) shows the b14 octave is genuinely the family's richest, but
  the enrichment is bounded and does not persist upward. Witness-level
  mechanism: each of the 4 known witnesses is a single w=7 generic orbit
  whose orbit-level P(level-2 | level-1) is ~ 1/200..1/415 vs null 1/q —
  individually ~1% coincidences; the family-wide aggregate excess over
  the volume null is ~ 2x with no scale growth. This lands on the
  benign branch of round-1 wz-C4: a constant O(1) level-correlation
  factor, official prediction (~2^-500 at L=2 emptiness levels)
  unaffected.
- **wz2-C3 (positive lemma: NO fixed integer vector is officially
  forced, at any level).** Round 1 excluded pure odd subgroup-sum
  relations; this round's pre-registration (section 1(a)) proves the
  full fixed-vector exclusion: for official `n'_L = 512L` with
  `m = odd(L)`, forcing levels `1..L` requires `Phi_{512L/g} | P` for
  every `g | m` (take `2l-1 = g`, `l = (g+1)/2 <= L`), and those are
  exactly the cyclotomic factors of `z^{256L}+1` with degree sum `256L`,
  so `P = 0` in the ring. Corollary: the analogue forced families
  (wz2-C4) do NOT transport, and any official mixed-channel kill must be
  q-DEPENDENT — which saturation statistics, not key recurrence, detect.
- **wz2-C4 (odd-n' forced/semi-forced taxonomy confirmed exactly; the
  live mixed channel is the norm-divisor channel).** Across 108 odd-n'
  L=1 cells the forced primitive ledger is EXACTLY {orbit(Phi_{n'})}
  (raw mass 12 at n'=96, 24 at n'=192) — every other ternary
  Phi_{n'}-multiple in window is imprimitive, as the pre-hoc algebra
  predicted, with zero exceptions. At L>=2: tag-{Phi_{n'}} witnesses are
  EMPTY everywhere (their uncovered-level values have norms with prime
  factors only 2 and 3); ALL semi-forced witnesses are tag-{2-power
  factor} of EVEN weight 6 (mod-2 parity argument), each verified by an
  exact integer resultant divisible by q; no key recurs at even 2
  primes. Semi-forced band RATE is ~flat across scales (.125/.083/.125
  at O96L2) — flatness is the norm-divisor-statistics expectation for a
  FIXED candidate family (a fixed norm has prime divisors at roughly
  constant density per octave); the pre-registered "q^-u scaling" is the
  per-vector per-prime probability, not the band total. KILL-O2 (which
  demanded monotone INCREASE >= 2x) was the right anomaly detector and
  did not trip. Design note for any WCL certificate: at composite-n'
  rows the window ledger is governed by cyclotomic-factor-divisibility
  populations, and a certificate must price the norm-divisor incidences
  (finitely many per candidate vector, enumerable by resultants).
- **wz2-C5 (minimal-row lift ownership validated on data; RATIFY-6 is
  load-bearing).** F = Phi_96 is lift-owned by the (q, n'=48) companion
  at ALL b21/b23 cells and at NO b25 cell — exactly the balance
  condition `q <= 2^24` flipping; F192 is lift-owned at all 36 O192L1
  cells. The forced mass moves to its minimal ADMISSIBLE row exactly per
  the census "charge a coincidence once at its minimal level" — but
  whether a target orbit's mass is 12 or 0 depends on the C1'
  admissibility of a DIFFERENT row at the same q (RATIFY-6). The
  maintainer must ratify the admissibility gate before official
  certificates; both k=2 and k=3 lift identities are now data-validated
  (xcheck96: 96/96 D_3 images vanish).
- **wz2-C6 (the singular-source dedup path is real, not an edge
  case).** At every odd-n' L=1 cell the forced orbit's multiplication
  matrix is singular over Z (`F * Phi_32 = 0`), the round-7 division
  method is structurally inapplicable, and the canonical weight-<=3
  sweep path (spec D4) actually carried the dedup. Official rows with
  odd(L) > 1 have factoring rings, so an official certificate WILL hit
  this path: RATIFY-4 (bounded-weight sweep vs factor-wise division,
  Appendix A) is a substantive convention choice, not cosmetics.
- **wz2-C7 (ops catch: the 40k stdout return cap truncates large shard
  JSONs).** The first o96_l1 run (ap-4dvEAIixznuDzBb58rntoD, checks all
  green) emitted 131,910 bytes and lost the front of its JSON to
  `modal_run_script.py`'s stdout[-40000:] cap. Fixed by (i) printing an
  aggregates-first WZ2_AGG line and (ii) compressing the whitelisted
  degenerate-flag class to counts (`deg_tagged`), keeping full detail
  only for anomalous flags. Rerun ap-2f557BtiorTmwUvclQjaUn (28,990
  bytes) has identical checks. Corollary for future rounds: budget the
  JSON, print aggregates before the blob.
- **wz2-C8 (link-count convention: undirected vs directed).** The
  canonical module logs 9 undirected shadow links on C/b21 q=2100353
  where round 1 logged 10 directed accepts — SAME components, same
  owners, same W (44 -> 34); the round-1-convention replay reproduces
  10 exactly. Spec D3 counts undirected edges. Recorded so future
  censuses do not misread link counts as a discrepancy (#137 class).
