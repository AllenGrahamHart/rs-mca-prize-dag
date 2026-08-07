# PRE-REGISTRATION — MYSTERY 4 (crossing): BB's method shape -> the accident UPPER bound / nu(A) (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: the named crux of the
crossing mystery is an UPPER bound on accidents in the break region.
THEOREM BB's proof concentrates accidents into 256 shells — a LOWER-
bound construction. The question: does BB's METHOD (shell
concentration) transport to an upper bound — either on accidents
directly or on the M-route's nu(A)? This is a method transport, NOT
an inequality transfer.

## 0. Sources (quote verbatim first)
- notes/pilots_20260806/gamma_shell/ — THEOREM BB (the 72.065-bit
  proved budget-break), LEMMA SL / THEOREM SM / THEOREM AC, the
  shell structure (256 shells), the break-region row description
  (a_L >= k+2^34+1; safe side w=2^35).
- notes/pilots_20260806/crossing_gap/ — the gap analysis banked in
  round 20.
- critical/nodes/rate_half_list_adjacent_crossing/statement.md —
  the THEOREM BB addendum (threshold relocation, consumers are
  existence/determination-shaped; the crux stated).
- notes/pilots_20260807/red_closability_probes/REPORT.md — PROBE
  2's countermodel (L_1 = 6 > B* = 5 >= B_C = 5 at RS[F_5,|D|=4,
  k=2]): the WARNING of record. L_1 -> B_C is NOT a transfer. Any
  transported bound must name its functional and prove its own
  inequality; quoting BB's inequality for a different functional is
  the exact mistake the countermodel kills.
- The M-route and nu(A): locate the definition in the crossing
  lane's nodes/notes (grep for nu(A) / M-route in critical/nodes
  and notes/pilots_20260806/); quote it with file:line before
  using it.

## 1. Deliverables
- (D1) THE METHOD ANATOMY: decompose BB's proof into its named
  steps (shell decomposition, concentration, counting). For each
  step, state what it PROVES (direction, functional, row region)
  — a table, applies/fails-because per step, against the upper-
  bound target. The round-19 discipline: exact hypothesis matching,
  no vibes.
- (D2) THE TRANSPORT ATTEMPT: if some steps survive (D1), derive
  the candidate upper bound at toy rows (2-power grids; small
  tower rows e >= 3 with delta_a = 1 to match BB's region) and
  VERIFY numerically: compute true accident counts exhaustively at
  toy scale and compare against the candidate bound. A bound that
  fails at a toy row is dead — report the cell.
- (D3) THE nu(A) VARIANT: same exercise for the M-route's nu(A) —
  does shell concentration bound nu(A) above? If nu(A)'s definition
  makes the transport type-mismatch (like L_1 vs B_C), say so
  immediately and name what WOULD bound it.
- (D4) THE HONEST REMAINDER: whichever way (D2)/(D3) land, state
  exactly what the crossing mystery still needs: the crux
  restated with whatever was gained, and the next decisive test.

## 2. Falsifiers / honesty
- Pre-register (before computing) the toy-row test cells and the
  acceptance rule for a candidate bound.
- If the method does not transport, a clean NO with the exact
  step-level gap is the deliverable — do not manufacture a
  conditional bound from unverified steps.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/bb_nu_transport/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6); no shift-0 cells where
  shifts exist (CATCH-19B). Name every measured functional
  (CATCH-19C). Verbatim quotes with file:line. No REPORT.md — your
  final message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2487
  (the "ROUND 22 LAUNCHED" marker); do not read the other round-22
  pilot dirs (l1_ell_sweep, ge_floor_falsifier, f2_rlocality);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.

# PILOT REGISTRATIONS

Appended 2026-08-07 by the Opus pilot BEFORE any computation. Sources
read first: gamma_shell/{REPORT,PROOFS}.md, crossing_gap/REPORT.md,
red_closability_probes/{REPORT,PROOFS}.md, the crossing node's
statement addendum (:4077-4095), and the M-route nodes
(averaged_slope_conversion, unsafe_crossing_family_instantiation,
averaged_occupancy_clean_anchor_first_moment_route_cut). Nothing
below has been computed yet.

## P0. The nine named steps of BB (the anatomy I will grade)

  BB-1  LEMMA DS / LEMMA FREE  (imported, crossing_dsa_refutation):
        deep stratum a = v-1 bijects with S' subseteq Z/n_a,
        |S'| = r'_a = L-2, single condition p_1(S') = 0, no side
        conditions.
  BB-2  LEMMA SL (sig-lift): sig(S) = 2^a sigma'(S') mod n.
  BB-3  THEOREM SM(1) CONCENTRATION: the deep stratum occupies at
        most 2L = n_a of the n shells.
  BB-4  THEOREM SM(2) STRUCTURAL EQUIDISTRIBUTION: exactly
        C(L, r'_a/2)/L per structural shell (Ramanathan/Lehmer,
        needs gcd(L, r'_a/2) = 1).
  BB-5  LEMMA MULT: #{(x,y) in D^2 : x-y = eps} = 2^{L-2-U} exactly.
  BB-6  LEMMA TC: fibre size C(L-U, (r'_a-U)/2) exactly.
  BB-7  THEOREM AC: Cauchy-Schwarz, P >= |D|^2/Q - |D|.
  BB-8  PIGEONHOLE: max-shell >= N_acc / 2L.
  BB-9  (REALISE): every shell is realised (c is free), so
        L_1(k+w) >= X_w(gamma) for every gamma.

## P1. PREDICTION (step directions)

Exactly BB-3, BB-7, BB-8 FAIL to transport to an UPPER bound
(each is strictly lower-bound-directed for the max-shell
functional); the other six (BB-1, BB-2, BB-4, BB-5, BB-6, BB-9)
transport, because each is an exact identity/bijection or a
"for every shell" quantifier. Predicted split: 6 transport,
3 fail. I predict further that BB-3, BB-7, BB-8 carry ALL of BB's
quantitative power, so what survives is scaffolding only.

## P2. Named functionals (CATCH-19C)

On the reduced deep stratum (S' subseteq Z/n_a, n_a = 2L,
|S'| = r'_a = L-2, theta of order 2L in F_Q, Q = p^{delta_a},
relation Sum_{j in S'} theta^j = 0, eps_j = 1[j in S'] -
1[j+L in S'], shell index gamma = sigma'(S') mod 2L):

  Xdeep(g)  := #{S' : relation holds, sigma' == g mod 2L}
  Sstruct(g):= #{S' : eps = 0, sigma' == g}
  A_deep(g) := Xdeep(g) - Sstruct(g)            (ACCIDENTS per shell)
  Amax      := max_g A_deep(g)
  Xmax      := max_g Xdeep(g)
  N_acc     := Sum_g A_deep(g)
  Occ       := #{g : A_deep(g) > 0}
  R2        := Amax * 2L / N_acc      (spread vs all 2L shells)
  R3        := Amax * L  / N_acc      (spread vs L shells, one parity)
  M(N,m)    := max_g #{S' subseteq Z/N : |S'| = m, sigma' == g mod N}
               (the UNCONDITIONED prescribed-sum maximum)

## P3. The candidate upper bounds (registered before testing)

  (U1) CANDIDATE-CAP-TRIVIAL:  Xmax <= C(2L, L-2).
  (U2) CANDIDATE-CAP-SHELL:    Xmax <= M(2L, L-2).
       Predicted closed form, from the Ramanathan/Lehmer count with
       gcd(2L, L-2) = 2:
         M(2L, L-2) = ( C(2L, L-2) + C(L, (L-2)/2) ) / (2L),
       attained at ODD g.  (U2) uses BB-1 and BB-2 only.
  (U3) CANDIDATE-NAIVE-TRANSPORT: Amax <= N_acc / L, i.e. R3 <= 1.
       This is the naive transport of BB-4 (structural
       equidistribution) + SM(4) (a fibre spreads over <= L shells
       of one parity) to the ACCIDENT family. It has NO proof.

## P4. ACCEPTANCE RULE for a candidate upper bound

ACCEPT U as a bound of record iff ALL THREE hold:
  (a) PROOF: U follows from steps graded "transports" in P1, with
      the derivation written out; no step graded "fails" may appear.
  (b) TOY: U holds at EVERY registered toy cell (below), against
      exhaustively computed true counts.
  (c) NON-VACUOUS: at the witness row (p = 3*2^41+1, e = 6, q = p^6,
      B* = floor(q/2^128)) U evaluates strictly BELOW B* at some
      v in [35, 39].
A candidate failing (a) is a heuristic, reported as such and NOT
used. A candidate failing (b) is DEAD, and I report the exact
failing cell. A candidate passing (a)+(b) but failing (c) is
"proved but vacuous" and is reported as such, not as a win.

## P5. Toy test cells (registered; 2-power grids, CATCH-Z6)

All cells have n_a = 2L a 2-power and p == 1 mod 2L, so
delta_a = 1 and Q = p -- matching BB's break region
(delta_a = 1, e >= 3). Exhaustive, no sampling.

  CELL-A  L =  4 (2L =  8, r'_a =  2), p in {17, 41, 73, 89, 97}
          realised at (n,w) = (32,8): m=5, v=3, a=2.
  CELL-B  L =  8 (2L = 16, r'_a =  6), p in {17, 97, 113, 193, 241}
          realised at (n,w) = (64,8): m=6, v=3, a=2.
  CELL-C  L = 16 (2L = 32, r'_a = 14), p in {97, 193, 257, 353, 449,
          577, 641}
          realised at (n,w) = (64,4): m=6, v=2, a=1 -- the same shape
          gamma_shell's `pipeline` gate used, so its banked numbers
          are a cross-check.

Method: exhaustive meet-in-the-middle over ALL C(2L, L-2) subsets
S' (independent of any lemma), giving the FULL per-shell profile;
the structural profile computed separately and subtracted. At
CELL-A and CELL-B I additionally run a plain brute force over all
subsets as an independent second counter.

## P6. Numeric predictions (registered)

  P6.1  (U1) holds at every cell (it is a superset count) --
        a null test, run anyway as a harness check.
  P6.2  (U2) holds at every cell, and M(2L,L-2) matches the closed
        form of P3 exactly at every cell, attained at odd g.
  P6.3  (U3) is FALSIFIED: at least one registered cell has
        R3 > 1. I expect the failure at CELL-A or CELL-B, where a
        single eps-fibre can dominate and lands in one parity class
        (gamma_shell's (64,8) cell already shows one-parity
        occupancy at p = 193 and p = 577).
  P6.4  At the witness row, v = 35 (L = 64, 2L = 128, r'_a = 62):
        log2 C(128,62) = 124.08 +- 0.05 and
        log2 M(128,62)  = 117.08 +- 0.05, against
        log2 B* = 127.5098. So (U1) margin ~3.4 bits and (U2)
        margin ~10.4 bits -- BOTH non-vacuous, (U2) by ~7 bits more.
  P6.5  (U2) is p-INDEPENDENT, hence it also covers the e = 1 PRIME
        rows that BB provably cannot reach. I predict the v-indexed
        threshold log2 q >= 128 + log2 M(2^{42-v}, 2^{41-v}-2) covers
        a strictly growing fraction of the live prime-row window
        [129.5849625, 256) as v grows from 35 to 39, and covers
        LESS than 10% of it at v = 35.
  P6.6  (U2) is lossy by the missing 1/Q factor: I predict
        log2 M(128,62) - log2 p = 117.08 - 42.585 = 74.5 +- 0.1,
        which should sit within 2 bits ABOVE gamma_shell's banked
        PROVED lower bound log2 max-shell = 73.061 at w = 2^35.
        If it does NOT bracket, one of the two is wrong and I say so.

## P7. The nu(A) registrations (D3)

Definition of record, verbatim
`critical/nodes/averaged_slope_conversion/statement.md:19-29`, and
the first moment verbatim `.../proof.md`:
`E[N(A)]=|A|(1-q^(-t))q^(1-t)`.

  P7.1  PREDICTION: TYPE MISMATCH, and worse than the L_1/B_C one.
        BB's output is a DETERMINISTIC count at one adversarially
        chosen received word; nu(A) is a FIRST-MOMENT functional
        over uniformly random received pairs whose max-over-
        instances step is already internal to
        averaged_slope_conversion. So BB-8 (pigeonhole) is not a
        missing ingredient of the M-route -- the M-route already
        owns its own copy of it.
  P7.2  PREDICTION (the SIGN test, decisive): E[N(A)] depends on A
        only through |A|; the ONLY structural lever is C_t(A), which
        enters nu(A) with a MINUS sign. Concentration increases
        collisions, hence increases C_t(A), hence DECREASES nu(A).
        So BB's engine is not merely inapplicable to nu(A) -- it is
        the negation of what nu(A) needs.
  P7.3  REGISTERED CANDIDATE THEOREM AT (anti-transport), to be
        verified exhaustively at toy scale: writing N = Sum_z X_z and
        Y = #{z : X_z > 0}, the conversion's own RHS obeys
          N - (1/2) Sum_z X_z(X_z - 1) <= (3/2)N - N^2/(2Y),
        by Cauchy-Schwarz over the Y occupied slopes. Hence any
        family whose contributions concentrate into Y <= N/3
        distinct slopes has conversion-RHS <= 0, so nu(A) <= 0 < B*
        whenever that holds pointwise. PREDICTION: verified with 0
        failures over an exhaustive enumeration of occupancy vectors,
        and the threshold constant is exactly 3 (a family must
        occupy MORE than a third of the slopes it touches).
  P7.4  PREDICTION: I will NOT be able to name a mechanism by which
        BB supplies an M payload, and the honest D3 output is a
        named anti-transport plus a list of what WOULD bound nu(A)
        below (large |A| with provably small C_t(A) -- i.e. an
        ANTI-concentration / spreading certificate).

## P8. Falsifiers I will honour

  F1. If (U2)'s closed form disagrees with the exhaustive M(2L,L-2)
      at any cell, (U2) is retracted and the cell is reported.
  F2. If (U3) HOLDS at every cell, I must say so and must NOT claim
      it is provable -- absence of a counterexample at L <= 16 is
      not a proof, and I will label it heuristic.
  F3. If (U1)/(U2) at the witness row do NOT come in below B* at any
      v in [35,39], the deliverable is a clean NO and I say the
      crux is untouched.
  F4. If P6.6's bracket fails, I report the discrepancy against the
      banked gamma_shell number rather than adjusting my own.
  F5. If THEOREM AT's threshold constant is not 3, I print the true
      constant.

## P9. Scope limits I state up front

(U1)/(U2) bound the DEEP STRATUM ONLY (a = v-1). Acc_shallow
(strata a < v-1) and aperiodic S are NOT bounded by anything here,
and the trivial cap cannot reach them: it uses periodicity, and only
the deepest stratum is periodic. So nothing here is a safe-side
certificate; at most it discharges one of the three terms in
gamma_shell's re-pose `X_w(gamma) <= S(v) + Acc_deep + Acc_shallow`.
I will not report otherwise.
