# PREREG — r38_urate_genericity (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r37_urand/REPORT.md` (round 37)
2. `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md`

## Mandate

R-URATE + R-GENERICITY — the two finite lemmas that pin the
far-CA count. Round 37 refuted Statement U and re-priced
B_ca^far(k+2^34) = r+1 + Theta(n/rho): the constructive floor
r+1+126 needs R-GENERICITY (the engineering matrix has full rank
j(rho+1) at razor parameters and a kernel vector exists meeting
the four open side-conditions — each held 60/60 at every
reachable cell); the matching cap needs R-URATE (the exchange
rate rho is tight: T_rand <= 2(r+1)/rho, a rank statement on the
j(rho+1) x (2(r+1)+j) incidence matrix). Both are self-contained
linear algebra over F_q[x]. YOUR JOB: prove them — or find the
structured rank-drop that breaks them (which would mean MORE
U-rand slopes than the cap, moving the count again). SECONDARY:
the carrier-exhaustiveness residue (is (X-x_0)P(X^2) the ONLY
parity-collapsing carrier at odd r? — closes R-USYM completely).

## Deliverables

**D1 — THE MATRIX, STRUCTURED.** The engineering system: rows =
j blocks of (rho+1) evaluations lambda_i Z_{Y_i}(x) + e_0(x) +
gamma_i e_1(x) = 0 on A_i; unknowns = (e_0,e_1) on W (2(r+1)
values) + lambda_1..j. Its structure: Vandermonde-like blocks
glued along the shared (e_0,e_1) columns. Derive when it has
full rank: transversality of the A_i (pairwise intersections?),
the Z_{Y_i} nonvanishing pattern, char conditions. A CLEAN
sufficient condition (e.g. "the A_i pairwise intersect in
< rho+1 points and the Y_i are distinct") provable by a
Vandermonde/exchange argument would BE R-GENERICITY's rank half.

**D2 — R-URATE.** The cap direction: show no configuration of
j > (2(r+1)-1)/rho codeword-mediated slopes is consistent — i.e.
the joint system for j slopes ALWAYS has only the zero solution
past the cap (the pilot's kernel arithmetic says dim would go
negative; the gap is whether NON-minimal-spend or mixed-spend
configurations evade the count — the rho-1 law is
spend-independent, so derive the joint version: j slopes at
arbitrary spends cost SUM of what? prove the additivity or find
the discount). If additivity holds, R-URATE follows and
B_ca^far(k+2^34) = r+1 + 126 EXACTLY (modulo D1's half).

**D3 — THE SIDE-CONDITIONS + THE CARRIER RESIDUE.** (a) The four
genericity side-conditions (lambda_i != 0; chi injective on W;
gamma_i off the fibre slopes; column-farness): show each is a
nonempty Zariski-open on the kernel (or exhibit the failure).
Measure at 2-3 more cells to tighten the 60/60. (b) The
carrier-exhaustiveness question: classify error supports T with
e_1/e_0 = x^2 whose parity collapse survives — is the
(X-x_0)P(X^2) family everything at odd r? A completeness lemma
closes R-USYM; a new carrier re-opens it (then measure its
threshold).

**D4 — VERDICT.** The far-CA pin's status (unconditional /
still-modulo-what); misses first; cross-pilot flag (do NOT read
siblings). Faithfulness conditions mandatory on all cells.

## Blind priors to register

P(D1's rank half proved), P(R-URATE's additivity holds),
P(the +126 becomes unconditional this round), P(a new carrier
exists), P(the count moves AGAIN (cap broken)).
