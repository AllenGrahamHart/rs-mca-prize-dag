# GOAL: Adversarial attack on the pinned DLI-CLOSE target

Read FIRST: `nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md`
(the pinned target, its three verified-equivalent displays, the weight-split
architecture, and the counterexample pre-emption record). Your mission is to
BREAK it before Pro is asked to prove it. Fresh worktree from latest master,
own branch, Modal < 60s per run, checkpoint JSON, ledger with replay commands
at `experiments/dli_gap_attack/ledger.md`.

## The object

Section X = {zeta^i : 0 <= i < n/2} in mu_n over PRIME q ≡ 1 (mod n), n = 2^s.
An ODD-TRADE of weight w: nonzero d in {-1,0,+1}^X, w nonzero entries, with
sum_y d_y x_y^r = 0 for every odd r <= 2L-1. Target claims W = sum 2^{-w} <= 3;
the danger zone is the GAP: L < w <= w*(q,L) where the random model predicts
ZERO trades (w* = max{w : C(N,w) 2^w <= q^L 2^{-10}}).

## Attacks, in priority order

1. **Gap-trade hunt at scale.** MITM census for odd-trades in the random-empty
   regime, more rows and higher weights than the local pass (which was clean at
   5 rows down to expected 7e-4): sweep n in {32,64,128,256}, L in {2,3,4,5},
   q chosen so the window is CLOSED (C(N,w)2^w << q^L for the weights you can
   reach), weights as high as MITM allows. ANY hit at a window-closed row is a
   structural falsifier — verify it end-to-end (re-derive, check section
   membership, disjointness, all odd moments) before reporting.
2. **The rotation-engineered family specifically.** Construct P with all odd
   moments <= 2L-1 vanishing EXCEPT one (r0), then Q = zeta^{2k} P with
   2k*r0 ≡ 0 (mod n), P and Q disjoint subsets of the section. The pinned doc
   flags this as the most plausible structured family; build it directly rather
   than waiting for the census to stumble on it. Also try: unions of two
   near-trades with cancelling defects; trades supported on arithmetic
   progressions of section indices; Gauss-sum / quadratic-character sign
   patterns.
3. **The tail constant.** At rows where w > w* is reachable, measure the ratio
   N_w / (C(N,w) 2^w q^{-L}) (true weight-w trade count vs random model).
   The tail route needs this <= K absolute. If the ratio grows with any
   parameter, that kills the combinatorial tail route (the analytic route may
   survive — say which).
4. **The analytic margin.** For the D3 route: exhaustively (all lambda != 0 at
   toy q) compute the worst-case per-lambda sum of log2 cos^2(pi a_y/q) over the
   section, normalized per coordinate. The route needs <= -1 bit/coordinate;
   the circle average is -2. Map the worst lambda's margin across rows and
   scales — if some lambda family approaches -1, find its structure.
5. **Level-independence.** The pinned doc flags "central tower measure is a
   product across levels" as an explicit unproved hypothesis. Attack it: do the
   levels' coordinate sets or domain assignments couple anywhere in the packet
   framing (read the b2b/packet notes)? A coupling that breaks E[prod] = prod E
   is a fatal architecture finding — report loudly.
6. **Identity replication.** Verify D1 = D2 = D3 at 3+ new rows (guards against
   a wrong closed form poisoning everything downstream).

## Discipline

- Verify every counterexample against the REAL object (known traps: proxy
  objects, degenerate samples, accidental small-q windows — compute the
  expected random count for every hit and report observed/expected).
- "Not found" only counts with coverage stated (rows, weights, method).
- If a structural family IS found: do NOT re-pose anything; record the verified
  family + its count law and stop that thread (the owner re-poses per the
  failure-conversion section of the pinned doc).

## Report

Ledger table: attack | rows/weights covered | result | replay command.
End with: FALSIFIER-CANDIDATES (verified, with expected-vs-observed), tail-ratio
table, worst-lambda margin table, level-independence verdict.
