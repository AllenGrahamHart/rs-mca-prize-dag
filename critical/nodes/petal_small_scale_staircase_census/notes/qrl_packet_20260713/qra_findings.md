# qra_findings — independent replay audit of qrl_packet_20260713 (running log)

Auditor: fresh-context packet auditor, 2026-07-13. Compute law: Modal-only.

## Hand-derivation links (no machine needed; re-derived from scratch in-transcript)

- L0 CRUX (Lemma 0): VERIFIED. Official rows: k = 2^{s-c} (c in 1..4, s>=13) so k
  is dyadic and even; M dyadic <= k => M | k. Scale-M class: S = union of full
  M-fibers (stabilizer partition, PROVED G2 flip) => M | A. Contributor: A >= k+sigma
  = k+1 > k strictly (sigma=1 excludes A=k). M|A, M|k, A>k => A >= k+M => a = A/M >=
  k'+1, k' = k/M integral. No interpolation-degenerate cell a = k' exists.
- L0 corollary 1 (edge band empty): VERIFIED. A = k+1 is odd (k even), M >= 2 even
  cannot divide it. (General sigma in [1,M-1] would also work: k < k+sigma < k+M.)
- L0 corollary 2 (multiplicity 1): VERIFIED. Two deg<k' codewords sharing an exact
  support S', |S'| = a >= k'+1 > k'-1+1, agree on >= k' points => equal. a >= k'
  would already suffice; packet's a >= k'+1 is stronger. Same argument at original
  row (A >= k+1 => support determines codeword) => banked "multiplicity 1
  everywhere" is a theorem; class count = codeword count. Exact argument in
  qrl_proof.md Lemma 0 is correct as written.
- T1 single-word injection: VERIFIED. list -> exact supports injective (mult-1 at
  a >= k'+1) -> size-a subsets of Z_{n'}: L_P <= C(n',a). Field-free.
- T1 class-level ESP-free transport: VERIFIED. class member -> S injective (A > k
  mult-1 at ORIGINAL row); S union of full K_M-fibers => S <-> S/K bijective,
  |S/K| = A/M; needs only M | n (covers M-not-dividing-k scales). Does NOT consume
  descent or ESP at all; aperiodicity of S/K available from descent's final
  paragraph but not needed for the count. Clean.
- T2 Johnson instantiation: VERIFIED against Paper D v13 source (cap25_cap_v13_raw.tex
  line 6221, thm:capf-johnson-list): stated for arbitrary finite Omega, kappa-
  intersecting family; quotient row qualifies with kappa = k'-1, n_0 = n', s = a;
  bound n'(a-k'+1)/(a^2-(k'-1)n') when a^2 > (k'-1)n'; floor legal (L integer);
  <= n'^2 since denominator >= 1 (integers) and (a-k'+1) <= n'... (N-d <= ell,
  N <= ell). Complete-list superset of the aperiodic exact-size-a list: OK.
  Cell form A^2 > (k-M)n: algebraically identical. VERIFIED.
- T2 ESP transport arithmetic: RE-DERIVED. D = (q-r)^2 - Lq >= q(q-2r-L);
  with L <= n'^2, r <= n'-1, q >= n^2 = M^2 n'^2 >= 4n'^2: D >= q(3n'^2-2n'+2) > 0.
  Factor q(q-r-1)/D <= (q-r-1)/(q-2r-L), decreasing in q (derivative sign
  -(r+L-1) < 0), worst at q = 4n'^2: <= 4n'^2/(3n'^2-2n') = 4n'/(3n'-2) <= 2 for
  n' >= 2. Output <= 2n'^2 <= (63/64)n'^6 for n' >= 2 (128 <= 63 n'^4). VERIFIED.
  Descent hypotheses at T2 cells: n' >= 64 => M <= n/64 < n/16 <= k, dyadic => M|k;
  char F odd (q ≡ 1 mod n, n even, q prime > 2); M | A. All met.
- T3 one-fiber lemma: VERIFIED. c(S) = M => S nonempty union of full M-fibers
  (group theory: orbits of Stab_H(S), holds for any M | n); a shared full fiber
  = M >= k common agreement points with U => two such codewords agree on >= k
  points => equal (deg < k); first-fiber map injective into n/M fibers. 3 lines,
  sound. Scales M in (k,t]: exactly M = 2k (rho=1/8), M in {2k,4k} (rho=1/16):
  n' in {4,8}, 29 x 3 = 87 pairs; ALSO covered class-TOTAL by T1 binomial sums
  (2^4, 2^8 << caps). Catch #111 closure: VERIFIED.
- Tools-checked-not-applicable section: consistent with node statements read
  (top_band_residual_free_johnson and retained_zero need chart data; deep-regime
  is almost-every-prime + extras-shaped, catch #110 reasoning verified; deep
  window arithmetic n' < 2s at q = n^2 correct, sliver = (n'=64, s>=33) = 36 pairs).

## Machine-verified links (Modal runs; anchor + independent audit below)

(appended as runs complete)
- ANCHOR (Modal): banked path-repaired qrl_verify.py replays green — stdout
  bit-identical to banked qrl_verify_output.txt, regenerated coverage table
  bit-identical to banked qrl_coverage_table.md. exit=0, peak 55MB.
  (Also replayed bit-identically LOCALLY pre-protocol-change at 13.4MB/0.54s.)
- INDEPENDENT AUDIT (Modal, qra_audit.py, 57MB, exit clean after exhibit fix):
  A) window arithmetic exact: max_a C(n',a) <= cap for n' in {2..32}, fails at 64
     (C(64,32)=1832624140942590534 > 67645734912); edge cells C(n',a<=6) <= n'^6/720;
     Johnson floor <= n'^2 on 5 full windows; ESP output <= 2L exact sweep incl.
     boundary q=4n'^2. ALL PASS.
  B) Lemma-0 arithmetic over all 2900 pairs (M<=k => M|k; A>=k+M; edge band
     indivisible; 87 M-in-(k,t] pairs). ALL PASS.
  C) coverage table: independent regeneration matches ALL 116 rows (open/proved
     j-ranges, M=2 and n'=64 a-bands); 464/2436/36 counts; band rule EXHAUSTIVE
     for n' <= 4096 + boundary probes beyond; P1-own singleton claim (open iff
     k'>=8; 29 exceptions all (rho=1/16,n'=64)). ALL PASS.
  D) SUM-VS-MAX SEAM (catch #113 material): ledger hypothesis is per-scale
     CLASS-TOTAL; under widest ALL-band reading the T1 per-cell bounds sum to
     1,846,943,453 (rho=1/2) and 4,279,934,123 (rho=1/4) at n'=32 > cap =
     1,056,964,608; even T1+T2 combined: 1,739,366,153 / 1,266,218,809 > cap.
     n' <= 16 closes class-TOTAL for all rho (T1 alone); n'=32 closes for
     rho in {1/8,1/16} (T1+T2). Packet's per-cell claims TRUE; the transport
     sentence "T1 ... transports to the ledger's class-level form directly"
     overreaches at n'=32 under the unresolved-P1 ALL reading.
  E) catch #109 exhibit D = -4,535,124,828,922,838,079 EXACT MATCH; per-s
     thresholds match packet row-for-row. NEW (catch #115 material): at the
     packet's own threshold pair (s=21, M=2^14, n'=128, rho=1/2) minted strength
     L = cap gives D > 0 (transports) but ESP output = 64.00 x cap — catch
     #109's repair option (a) strength floor min((63/64)n'^6, q-2n') is
     necessary-not-sufficient; corrected sufficient pin VERIFIED on a
     4000-point exact sweep: L <= min((63/128)n'^6, (q-3n')/2) => D>0 AND
     output <= (63/64)n'^6.
  F) banked ground truth: 514 profile cells independently re-checked (M|A,
     2<=M<=t, A>=k+1, A>=k+M when M|k, edge empty at even k, multiplicity 1,
     <= C(n',a), <= cap); tightest cell (8,3,17) fp0_edge (2,4) ratio 2/3. PASS.
- GROUND TRUTH FROM SCRATCH (Modal, qra_groundtruth.py, 54MB): all 26 banked
  p=17 records ((8,3,17) x20, (8,4,17) x6; 156 profile tables) reproduced
  EXACTLY by full 17^3/17^4 polynomial enumeration with independent stabilizer/
  classification/profile code (only build_word imported, definitional).
  Independent descent at (8,4,17): my own fiber transform satisfies the
  reconstruction identity at all points; codewords descend to even/odd
  coefficient split; aperiodic exact L_P <= C(n',a) <= cap at all 24 cells;
  scale-2 classes inject into aperiodic S/K; descent inequality holds.
- MUTATION TESTS (Modal, qra_mutations.py, 56MB): MUT-A (T1 window widened to
  n'=64) FAILS as required; MUT-B (band-rule 7->6) FAILS on the pointwise
  cross-check; MUT-C (banked cell classes 4->7) FAILS with VIOLATION line +
  restore control green; MUT-D coverage-table corruption caught by anchor
  byte-diff (table regenerated, not read). STATIC (catch #114 material): the
  packet verifier's built-in "MUTATION M2" is a TAUTOLOGY (check(comb+1 >
  comb)) — it never feeds the tampered value through the S4 predicate; the
  real tamper (MUT-C) shows S4 itself has teeth, so the packet's underlying
  checker is sound and only the self-test line overclaims.

## VERDICT: SOUND-WITH-REPAIRS (two named repairs, catches #113-#115)

All three proved windows (T1/T2/T3), Lemma 0 + both corollaries, the 116-row
coverage table, the 464/2436/87/36 counts, catches #109-#111's arithmetic, the
514-cell ground-truth consistency, and the verifier all replay clean and
independently. The verifier survives real mutations (window widened, band rule
corrupted, banked cell tampered). Ground truth reproduced from scratch at all
26 exhaustive p=17 points.

R1 (catch #113, quantifier seam): qrl_proof.md's "T1 ... transports to the
ledger's class-level form directly" is per-CELL true but the
intrinsic_scale_geometric_ledger hypothesis is per-scale CLASS-TOTAL; under the
unresolved-P1 ALL reading, class-total is closed by T1 alone only for n' <= 16,
by T1+T2 at n'=32 only for rho in {1/8,1/16}; NOT closed at n'=32 for rho in
{1/2,1/4} (exact: 1,846,943,453 / 1,266,218,809 > 1,056,964,608). Repair = pin
the band (own-band single cell a=k'+1 per scale, matching the packet's own P1
reading) or add the explicit per-scale supplier map.
R2 (catch #114): replace the verifier's tautological M2 self-test with a real
tampered-record run (MUT-C pattern).
Catch #115: catch #109's repair option (a) strength floor is necessary-not-
sufficient (transportability != consumability; 64x-cap exhibit at s=21,
M=2^14); successor red must carry L <= min((63/128)n'^6, (q-3n')/2).

Footnotes (not catches): verifier docstring "17^4 states" overstates S5's
actual 2x17^2 control (conservative direction); "EXACT at 4/7" vs dag's "four
banked rate-half cells" is a wording reconciliation; deep-regime marker eps->0
needs eps < 1/32 for the s>=33 sliver (immaterial, window unconsumable per #110).
