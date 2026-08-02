# Fable audit of the crossing one-packet pilot — 2026-08-02

**Verdict: ACCEPTED.** The lane's first pilot delivers exactly what the
exploratory GO authorized: PK1 (the split-section inverse
classification at its smallest instance) is PROVED with an exact
q-free packet, ceiling, fence, closed-form template, automatic
exactness guard, and exhaustively-verified inverse maximality; the
PK2 scope theorem shows the q-free phenomenon is codimension-one ONLY
(w=2 is q-dependent, certified across 20 fields); the M1-M9 mutation
suite is built; and the contract-requirements report unblocks my
succinct-contract draft.

## Independent verification record

- Replayed ALL THREE suites this session: verify_packet_theorem.py
  (1002 checks, PK1_VERIFICATION_PASS), verify_mutations.py (46,
  MUTATION_SUITE_PASS), verify_inverse_scan.py (17, INVERSE_SCAN_PASS,
  under RAMGUARD_TIMEOUT=25m).
- Hand-verified the proof's load-bearing lemmas: the ceiling (m_0 = 0
  impossible — all locator roots in F^*); the automatic exactness
  guard (W(x) = c/x != 0 on T); the equidistribution (gcd(r,n)=1
  makes omega -> omega^r an automorphism, so the mu_n-action is
  transitive on the target coset with equivariant product map — each
  fibre exactly C(n,r)/n); the conservation pin (70 - 5*7 = 35 at
  n=8, matching the measured census); the official-row applicability
  (gcd(2^40 - 1, 2^41) = 1).
- The verification design is strong: PK1's censuses are brute-forced
  independently of the proof (every k-subset interpolated), across
  four characteristics including non-prime fields, with ZERO slack —
  equality, not bounds.
- Subtraction discipline (hard law 5) was done BY the pilot and
  checks out: the lower-bound half is the rotated-prefix floor's d=1
  pigeonhole at its excluded boundary (upstream #1101); the genuinely
  new content is the UPPER half (exactness, ceiling, template, q-free
  index family) + PK2 + the inverse maximality.

## Findings adopted

1. **The replacement framing survives its first test — with a sharp
   scope boundary.** The q-free packet is real, provable, and unique
   among rank-one sections; and it exists ONLY at agreement k+1
   (PK2: w >= 2 carries a vanishing-subset-sum clause, characteristic-
   dependent, and the official regime C(n,r)/q ~ 2^(2^41) is the
   q-dependent regime). Lane consequence: the inverse-classification
   program must either live at w=1 (no frontier movement — the packet
   prices at ZERO on the ledger) or confront q-dependence head-on at
   w >= 2. That is the re-posed lane question for Pro.
2. **The contract draft is UNBLOCKED and its requirements are
   concrete**: symbolic-count primitive with inequality-derivation
   chains (mandatory — counts have 2^41 bits at the razor row);
   guarded-vs-raw pinned (21 vs 7); operational q-independence defined
   via index families replayed in two characteristics; the
   descriptor-collision rule (affine target mandatory — M1);
   the B*=0 pin discharged by this word class budget-uniformly.
   I draft the contract now (see
   notes/pro_briefs_20260801/responses/CROSSING_SUCCINCT_CONTRACT_DRAFT.md).
3. **Mint candidate (deferred to the next boundary):** PK1 as a
   background node with the fast verifier (verify_packet_theorem.py
   trimmed; the 25-minute inverse scan stays pilot-side). Zero
   frontier movement, but it is the lane's first complete packet
   theorem and the calibration instance for the contract.
4. **Mutation suite adopted** into the lane's standing battery (M1-M9,
   each self-contained): notably M5 re-certifies the retired
   PE-envelope fence live, and M9 is the succinctness killer that
   shapes the contract's class-restriction.

## Caveats kept (endorsed)

- PK1 is a single-word theorem; U(q)/S(q) unchanged.
- The general-n inverse threshold ("guarded fibre > runner-up ==>
  pure-product") is conjectural — an inverse character-sum theorem,
  not attempted; exhaustive only at n=8 (+ two-support n=16).
- The official-regime q-dependence claim at w=2 rests on a counting
  heuristic (exact fact: no q-free formula exists, certified).
- Field scope: split multiplicative-coset domains only.
