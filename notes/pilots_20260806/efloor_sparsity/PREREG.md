# PRE-REGISTRATION — E_floor SPARSITY (hybrid): prove the sparsity half of CC, and attack it

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. HYBRID mandate: half the
pilot proves (sparsity of the exceptional floor class), half attacks
(construct the DENSEST floor families you can — the truth is wherever
the two meet). This is the repo's long-named pair-coprimality open
lemma in its round-17 sharpened form.

## 0. The object (round-17 es_coprimality, banked)

```
E_floor = { S : some odd p | N_odd(I_S) has |Z_w^odd(p)|·log2 p <= (n/4)·log2 r' }
```
CC-sparsity: |E_floor|/#orbits -> 0 as w grows (measured: 0.9934+
coprimality rates at w >= 3, exactly 1.00000 at the crossing shape).
THEOREM CS makes E_floor membership REQUIRE a small bad prime
(p below the CS3 floor); the measured residual bad primes at
a = 0, w >= 3, n = 32 are ONLY {3,7,17,47,97,193,257,353,449}.

The lineage (quote both): the pair-coprimality open lemma
(critical/nodes/u1_x4_direct_column_budget/notes/F3_SHALLOW_LADDER.md:200-202,
"ONE open lemma (pair-coprimality / norm-gate sparsity) stands
between the data and the theorem — shared verbatim with F2's
accident story") and CATCH-17B (the u2c empirical credit was never
banked mathematics — this pilot is the debt coming due).

## 1. Source surfaces (read ALL first; quote verbatim)

- notes/pilots_20260806/es_coprimality/{REPORT.md, PROOFS.md,
  cop_lib.py} — THEOREM CS, LEMMA TWO/STRAT, the E_floor
  definition, the rate table, the bad-prime lists, the HNF norm
  machinery (reuse it; it is banked).
- notes/pilots_20260806/es_boundary_adversary/REPORT.md — the
  witnesses (three of five are E_floor members: (47), (23), (463)
  rows) and the census method.
- background/nodes/dli_wcl_weight3_ambient_exclusion/proof.md +
  weight4 sibling — the banked resultant/bad-prime method and its
  PROVED exclusions (subtract; these may already prove small-w
  floor emptiness in their regime).
- critical/nodes/u2c_giant_tnull_dichotomy — the consumer whose
  empirical credit this lemma would convert to mathematics.

## 2. Pre-registered deliverables

- **(S1, generative) SMALL-PRIME EXCLUSION.** For a FIXED small
  prime p (start p = 3, then 7, 17), characterize/bound the S with
  p | N_odd(I_S) at given (n, r', w): this is the F_p-solution count
  of the reduced window system — a fixed-characteristic question the
  banked weight3/weight4 exclusions may already partially cover.
  Target theorem shape: for each fixed p, the density of
  {S : p | N_odd(I_S)} among orbits is <= f(p, w) with
  sum_p f(p, w) -> 0 as w grows (a union bound over the FINITE
  bad-prime range that CS3 leaves alive). If provable even for
  p = 3 alone, it is the first sparsity theorem.
- **(S2, adversarial) DENSEST FLOOR FAMILIES.** Construct S families
  maximizing bad-prime membership: coset-near unions, arithmetic-
  progression supports, LEMMA-STRAT-boundary structures. Measure
  their density contribution exactly. The goal: locate the TRUE
  decay rate of |E_floor|/#orbits in w and n, and find whether any
  family gives a NON-vanishing density (which would refute
  CC-sparsity — report as a catch with witnesses, per the falsifier
  below).
- **(S3) The n-asymptotic.** The round-17 measurement is n <= 32
  only. Extend the exact census to n = 64 at the feasible (r', w)
  corner under ramguard-local (pre-register the reachable grid
  first; if n = 64 is out of reach in 5-minute chunks, say exactly
  what was reached — round 16 left an honest unreached-n = 64 flag;
  close it or re-flag it honestly).
- **(S4) The u2c conversion statement.** State exactly what
  (S1)-form theorem would convert u2c's 1440-trial empirical credit
  into mathematics, and how far this pilot got toward it.

## 3. Pre-registered falsifiers / honesty clauses

- A constructed family with non-vanishing floor density refutes
  CC-sparsity as posed — campaign-relevant catch, report with
  reproduction script; the round-17 conditional (K5) then needs
  re-scoping, not silent repair.
- (S1) bounds must be proved for the stated p, not extrapolated
  across primes; the union bound must use the PROVED CS3 floor for
  its range, cited exactly.
- n = 64 nulls from unreached regimes are not evidence (round-16
  rule).

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/efloor_sparsity/. Never edit dag.json, node
  shards, tools/, or push. Do NOT read
  notes/pilots_20260806/crossing_low_w/ (sibling this round).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. Includes file patching
  and JSON peeking (three round-17 pilots breached exactly there).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# PILOT APPENDIX — registrations E0-E9 (appended 2026-08-06, BEFORE any computation)

Opus round-18 pilot, `notes/pilots_20260806/efloor_sparsity/`. Everything
below is written before a single line of my own code has been run. Nothing
in this file is edited after the first computation; corrections are appended
with a dated `[AMENDED]` tag.

## E0. Scope, reuse, subtraction

I reuse, and do NOT re-claim:

- the census identity, verbatim from
  `notes/pilots_20260806/es_boundary_adversary/es_lib.py:23-28` (quoted at
  `es_coprimality/PROOFS.md:27-33`):
  ```
      S is a solution in characteristic p for SOME choice of primitive n-th
      root of unity in F_{p^delta}
        <=>  some prime P | p contains every x_s
        <=>  gcd( Phi_n, V_1, ..., V_{w-1} )  has degree >= 1  in F_p[X]
        <=>  p | N(I_S),   I_S = (x_1, ..., x_{w-1}) <= O_K.
  ```
- LEMMA Y (cyclic-code framing), BANKED round 14, verbatim from
  `notes/pilots_20260804/mun_anticoncentration/PREREG.md:53-61`:
  ```
  - **(U1)** The crossing count is exactly a constant-weight count in an
    explicit p-ary cyclic code:
    W_w = { x in {0,1}^n <= F_p^n : wt(x) = r',  x in C(n, p, Z_w) }
    where `C(n,p,Z_w)` is the cyclic code of length `n` over `F_p` with
    defining zero set `Z_w` = the p-cyclotomic closure of `{1,...,w-1}`
    mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.
    This is LEMMA Y, BANKED round 14 — cited, not claimed.
  ```
- THEOREM CS / LEMMA STRAT / LEMMA TWO / LEMMA Z as stated in
  `es_coprimality/PROOFS.md` §2-§4, and `cop_lib.py`'s exact HNF ideal
  norm as the independent oracle.

**Subtraction performed before registering (hard law 5).** The banked
`dli_wcl_weight3_ambient_exclusion` / `weight4` nodes prove *`v_2(q-1)>=41`
gate emptiness by exhaustive resultant factorization at n=512, weights 3
and 4*; they contain **no fixed-small-prime statement and no density
statement**. The only fixed-prime exclusion in that family is `{2,3,17,19}`
in `dli_wcl_ell4_weight9_inversion_symmetric_exclusion` (an elimination
exception list, not a density theorem). Nothing in `critical/`,
`background/`, `notes/`, `archive/` proves or measures a fixed-prime
divisibility density for `N(I_S)`. I also record that the naive density
heuristic was **already refuted in-repo** — `mun_anticoncentration/
REPORT.md:102`: *"(ACC) REFUTED — and the truth is better."* — so I
register only ONE-SIDED UPPER bounds, never the heuristic as an estimate.

## E1. (S1) THEOREM SP-COVER — the statement I will try to prove

> **THEOREM SP-COVER (registered).** Let `n = 2^m`, `p` odd,
> `<p> <= (Z/n)^*`. Suppose every coset of `<p>` in `(Z/n)^*` contains an
> ODD integer `s` with `1 <= s <= w-1`. Then for every `S <= Z/n` with
> `strat(S) = 0`, `p` does not divide `N(I_S)`.

> **THEOREM SP-UNIFORM (registered).** With `j_p := v_2(p^2-1)`: if
> `w >= 2^{j_p}` then `p | N(I_S)` forces `strat(S) >= 1`. Contrapositive:
> a bad prime at stratum `a = 0` satisfies `2^{v_2(p^2-1)} > w`, hence
> `p^2 - 1 >= 2^{v_2(p^2-1)} > w`, i.e. **`p > sqrt(w+1)`.**

Define `w_cov(p,n) = 1 + min{ W : {odd s, 1<=s<=W} covers (Z/n)^*/<p> }`.

**Registered numerical predictions (falsifiable, exhaustive checks):**

- **(P1)** For `p in {3,5,7,17}` and `n in {16,32}`: exhaustively over all
  `S` with `strat(S)=0`, no `S` has `p | N(I_S)` once `w >= w_cov(p,n)`.
  *Falsifier: a single witness. If found, SP-COVER is FALSE and I report it
  as a refutation of my own theorem.*
- **(P2) SHARPNESS.** At `w = w_cov(p,n) - 1` there EXISTS a `strat(S)=0`
  witness with `p | N(I_S)` (checked for `p in {3,5}`, `n in {16,32}`).
  *If no witness exists the threshold is not sharp and I will say so.*
- **(P3)** I predict `w_cov(3,2^m) = 6` and `w_cov(5,2^m) = 4` for every
  `m >= 3` (n-uniform), and therefore that the round-17 residual bad-prime
  list `{3,7,17,47,97,193,257,353,449}` at `a=0` contains **3 only for
  `w <= 5`** and (if 5 ever appears) **5 only for `w <= 3`**.
- **(P4)** Independent-oracle agreement: my `F_p` syndrome route and
  `cop_lib.ideal_norm` (integer HNF) agree on `p | N(I_S)` on every fixture
  tested. *Falsifier: one disagreement.*

## E2. (S1) THEOREM SPD — the density bound I will try to prove

> **THEOREM SPD (registered).** Fix odd `p`, `n = 2^m`, `w`, `r'`, put
> `theta = r'/n`, `D = |Z_w|`, `e = n/(2 delta)`,
> `gamma = sqrt(1 - 2 theta(1-theta)(1-cos(2 pi/p)))`, and let `d` be a
> lower bound for the minimum distance of the DUAL of the cyclic code
> `C(n,p,Z_w)`. Then
> ```
> #{S : |S| = r', p | N(I_S)} / C(n,r')  <=  (n+1) * e * ( p^{-D} + gamma^d ).
> ```
> with `d >= n/D` available from the BCH bound applied to the dual.

Registered honesty clause: I expect SPD to be **non-vacuous only for small
`p` and small `|Z_w|`**, and I register NOW that I expect it to be
SUBSUMED by SP-UNIFORM whenever `w > sqrt(n)`. I will report the exact
regime where it adds something, and if it adds nothing I will say so.

## E3. (S1) Registered CATCH candidate — is `E_floor` a tautology?

Claim to be checked and proved/refuted: **given THEOREM CS,
`E_floor = { S : N_odd(I_S) > 1 }` exactly** (on `strat(S)=0`), because CS
*derives* the floor inequality for every `p | N(I_S)`. If so, the
decomposition `E = E_strat u E_floor` is a restatement, not a reduction,
and "CC-sparsity" is exactly as hard as the original open lemma.
*Machine check: over every census row, `strat(S)=0 & N_odd>1` implies the
floor predicate `cs_floor_ok` holds for some odd `p | N_odd`.*

## E4. (S1/S4) Registered prize-row computation

Compute, from the crossing-row constants quoted at
`es_coprimality/PROOFS.md:341`, whether SP-COVER bites at official rows:
official rows require `v_2(q-1) >= 41`, so `j_q = v_2(q^2-1) >= 42` and
SP-COVER needs `w >= 2^42`, while the bracket caps at `w = 2^39`.
**I register the prediction that SP-COVER is VACUOUS at every official
prize row**, and that the two exclusions (SP from below, CS from above)
do NOT meet. I will report the exact gap in `log2 w`.

## E5. (S2, adversarial) The families I will construct and measure

For each family `F` at `(n,r',w)` I measure exactly: `|F|`, the internal
floor density `|F n E_floor|/|F|` (restricted to `strat=0`), the global
contribution `|F n E_floor|/C(n,r')`, and the number of window conditions
that vanish identically.

- **F1 quarter-shift:** `S = T u (T + n/4)`, `T n (T+n/4) = empty`
  (kills every `x_s` with `s = 2 mod 4`).
- **F2 general 2-shift:** `S = T u (T + n/2^j)`, `2 <= j <= m-1`.
- **F3 symmetric:** `S = -S` (real-subfield collapse).
- **F4 multiplier-invariant:** `uS = S` for odd `u` of small order.
- **F5 AP / near-AP supports:** `S = {a, a+d, ..., a+(r'-1)d}` and APs
  with one element displaced.
- **F6 coset-near unions:** `S = (union of mu_M-cosets) symmdiff (small set)`.
- **F7 antipodal-loaded:** `S` maximizing `a_{n/2}(S)` at fixed `r'`.

> **PRE-REGISTERED FALSIFIER (campaign-relevant).** If some family `F`
> has `|F n E_floor| / C(n,r')` bounded away from 0 as `n` grows (at fixed
> `r'/n`, `w >= 3`), CC-sparsity as posed is REFUTED and I report it as a
> catch with reproduction script and explicit witnesses.

Registered expectation (so it cannot be retro-fitted): I expect **no**
family to refute; I expect a quantitative TRADE-OFF LAW — every family that
kills `k` window conditions pays an exponential-in-`n` price in `|F|` —
and I will report the measured exchange rate.

## E6. (S3) The n = 64 grid, pre-registered as REACHABLE before running

Round 16's honest flag, verbatim, `es_boundary_adversary/REPORT.md:106`:
> **n=64 was registered in my grid and never executed.** A null from an
> unreached regime is not evidence.

My reachable grid (each cell must complete inside `tools/ramguard local`,
5 min; anything not completed is reported as UNREACHED, never as a null):

- **(G1) PRIMARY, meet-in-the-middle exact per-prime census at n = 64:**
  `p in {3,5,7,17}`, `r' in {4,5,6}`, `w in {2,...,10}`; exact
  `#{S : |S|=r', p | N(I_S)}` split by `strat`. MITM over two 32-coordinate
  halves with an `F_p` syndrome, exact, no sampling.
- **(G2) STRETCH:** the same at `n = 128` for `r' in {4,5}` and/or `n=64`,
  `r' in {7,8}`.
- **(G3) all-characteristic exact census at n = 64** via `cop_lib.ideal_norm`
  for `r' <= 4`, `w <= 5`, over affine orbits (the round-17 orbit
  convention: `S ~ cS + b`, `c` odd, `verify_cop.py:373-377`). `r' = 5` is
  registered as STRETCH.
- **(G4)** exact all-weight (not fixed-weight) counts at `n = 32` by MITM
  over `2^16 + 2^16` half-vectors, to compare against SPD.

## E7. (S4) The u2c conversion statement

I will state exactly which (S1)-shaped theorem would convert the 1440-trial
empirical credit at `critical/nodes/u2c_giant_tnull_dichotomy/node.json:8`
into mathematics, and measure how far this pilot gets, with no rounding up.

## E8. Honesty clauses

- Every check script is fail-closed: a permanent stage injects a false
  check and must exit nonzero.
- COMPUTE LAW: every invocation of `python3` goes through
  `tools/ramguard tiny|local -- python3 ...` with a literal `--`, including
  file patching and JSON peeking. I register that I will report any breach
  of my own, as round 17 did.
- Unreached regimes are reported as unreached. No null from an unrun cell.
- Every statement relied on is quoted verbatim with `file:line`.

## E9. Registered expectations (anti-retrofit)

1. SP-COVER will be TRUE and SHARP at the tested rows.
2. No adversarial family will refute CC-sparsity.
3. The union bound over the CS3-alive range will **NOT** close: I expect a
   surviving middle band `sqrt(w) < p <= r'^{n/(4 ceil((w-1)/2))}`, and I
   register in advance that this is the honest outcome of (S1), not a
   proof of CC-sparsity.
