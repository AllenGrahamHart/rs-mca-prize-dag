# Fable audit of the C1 norm-ladder pilot — 2026-08-02

**Verdict: ACCEPTED.** F1 fired exactly as a falsifier should: the
c_w^(N/4) law AS STATED is dead (two exact failures, both at w = the
lower ring dimension), and the repair arrived with proofs. F2 did not
fire: the router survives as a finiteness tool with a complete census at
2N=32 (23,194 exceptional primes, all enumerated). The two lemmas are
the real result and are being MINTED as a background node
(`dli_c1_ternary_relation_norm_sandwich`) — see below.

## Independent verification record

- Replayed `scripts/norm_core.py` self-test and the independent sympy
  audit path (`scripts/verify.py`): 38 argmaxes + 131 census witnesses,
  0 failures, this session, under ramguard local.
- Inspected `results/ladder.json`: Lemma A checked exhaustively at
  M=2,4,8 (9 + 81 + 6561 embeddings, 0 violations); the sandwich
  closures at 2N=64 w=7 and 2N=128 w in {1,2,3,7} present with exact
  values (7^16 = 33232930569601; 3^32 = 1853020188851841;
  7^32 = 1104427674243920646305299201 — all re-checked by me).
- Hand-derived BOTH lemmas:
  Lemma A: for f = g(x^2), f_e = g and f_o = 0, so the field-norm
  descent f(x)f(-x) = (f_e^2 - y f_o^2)(x^2) gives g^2 one level down,
  and Norm_N(f) = Norm_M(g^2) = Norm_M(g)^2. Sound.
  Lemma B: the eigenvalues of mult-by-f on Z[x]/(x^N+1) are f(zeta^j)
  over the N odd residues j mod 2N, in N/2 conjugate pairs, so
  Norm(f) = prod |f(zeta^j)|^2 >= 0; negacyclic Parseval gives
  sum_j |f(zeta^j)|^2 = N ||f||^2 = Nw, so the N/2 pair-values sum to
  Nw/2 with mean w, and AM-GM caps the product at w^(N/2). Sound.
  Nonvanishing: x^N+1 = Phi_2N is irreducible, and a nonzero f of
  degree < N cannot be divisible by it, so Norm(f) >= 1 for nonzero f.
- Checked the arithmetic of both F1 failures (196/64 = 49/16;
  14760962/4734976 = 7380481/2367488), the saturation values, the
  2N=32 full-weight factorisation 2311094272 = 2^15 * 70529, and the
  U-freeness/d0=+1 reduction argument (domain, unit u != 1 =>
  f(u-1) = 0 forces f = 0). All sound.
- The 2N=16 census (11 primes, identical minimal weights) and the
  2N=32 w<=4 and w<=5 censuses close the loop with the PRIOR pilot's
  independent router implementation — two agents, two code paths, same
  answers.

## Findings adopted (binding on the C1 lane)

1. **The lane's next-theorem target is RESTATED.** Not "prove
   c_w^(N/4)" (false as stated, and c_6 = sqrt(1154) shows the base
   need not be rational) but the IMPRIMITIVITY CONJECTURE: for
   w <= N/2 - 1 the norm-maximising ternary f in Z[zeta_2N] is
   imprimitive (= iota of a lower-level polynomial). That single
   statement implies the entire stable-range doubling law by induction
   with Lemma A'. Observable signature confirmed at every level: the
   argmax is even-supported exactly up to the break weight.
2. **Unconditional router threshold, now a theorem** (minted): any
   admissible prime q > w^(N/2) carries no ternary relation of weight
   <= w, at every power-of-two level — Lemma B alone, no enumeration.
   With the saturating family {1,2,3,7} this is exact (the threshold
   is attained); elsewhere it is an upper fence.
3. **Orbit counts closed.** n_w^U = C(N,w) 2^w / (2N) exactly (free
   action, proved); n_w^G by Burnside, tabulated. The ledger's A_j
   multiplicities need no further estimation.
4. **The 70529 coincidence recorded**: the dynamics pilot's
   hard-regime champion prime is exactly the odd part of the global
   maximum norm at 2N=32 (2311094272 = 2^15 * 70529) and the
   full-weight P_N sequence (1, 17, 70529) consists of admissible
   primes. Flagged to the ledger lane as a lead, not a theorem.
5. **Census discipline**: exceptional-density is a few percent and
   declining (5/49 at w<=3 to 1422/24845 at w<=7 at 2N=32) — the
   router's finiteness framing stands quantitatively.

## Caveats kept (endorsed)

- 2N=64 above w=7 untested (w=8 probe consistent with the repaired law
  but non-exhaustive, honestly reported as such).
- The repaired law is VERIFIED (4 ladder points, w<=6) not proved for
  w in {4,5,6}; only >= (Lemma A') and {1,2,3,7} are theorems.
- c_9 = 79 rests on one ladder point.
- The census certifies attained-norm divisors; sympy factoring is
  exact but the sampled-witness recheck covers 50 of 23,194 at
  2N=32 w>=8 (all covered by the independent Bareiss path).

## Mint

`background/nodes/dli_c1_ternary_relation_norm_sandwich/` — statement,
proof, verify.py (exhaustive Lemma A at M=2,4; exhaustive Lemma B +
weight-max table at N=4,8; sandwich witness replay to N=16 and N=32 by
Bareiss; router-threshold spot checks), ev edge into
`dli_c1r3_gated_envelope_bound` (open TARGET, same consumer as the
sibling doubling-coboundary node). The imprimitivity conjecture is NOT
part of the minted statement (recorded here and in the report as the
lane's next target).
