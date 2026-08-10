# REPORT — rh_transport_dictionary (round 31)

# VERDICT — the (t,M) dictionary exists and has five entries; it kills round-29's "+115 bits" as a scale artifact, and it lands the whole supply lane on the LIST side, where an audited guard forbids the transport that would have made it matter

**The one-line dictionary.** Round 29 read the razor as `t = M` (excess =
coset scale). The banked primary text says otherwise, and by exactly one:
the qcore construction requires **`sigma < M`**, and its extremal case is
`sigma = M - 1`
(`background/nodes/ww_lower_witnesses/proof.md:18`: "Put `M=n/N` and
`sigma=M-1`. Then `M|k`, `k/M=rho*N<=N-1`, and `1<=sigma<M`"). That
off-by-one is load-bearing: the razor's own crossing index sits at
`sigma = 2^34`, one step past the cliff where the qcore's admissible `M`
must double.

---

## MISSES FIRST

1. **My headline "new" supply number is a RE-DERIVATION — CATCH-24A fires
   against my own result.** I derived that at the razor's index
   `sigma = 2^34` the coset-lifted product word supplies
   `C(128,65)/128 = 2^117.14907` codewords, 57.48 bits above the
   qcore-family value at that index. The quantity `C(N,N/2+1)/N` is
   already in-repo, and its razor-scale reading is already banked:
   `notes/literature_map_20260726/target_mappings.json:838` — "at
   q ~ 2^256 the minimum power-of-two N with `C(N,N/2+1)/N > B*` is
   N=256, i.e. c=2^33 and sigma <= 2^34-1 — exactly our banked
   (RHL-LB)". That sentence already contains my conclusion (N=128 fails
   to reach `B*`). `C(128,65)` itself is banked at
   `background/nodes/rate_half_multiplicative_amplification_floor/proof.md:26`
   ("the maximum over `e>=34` occurs at `e=34`, where `N_e=128`, and
   equals `C(128,65)`"). What survives as mine: the exact value at the
   exact index, the 57.48-bit comparison against the qcore family there,
   and the small-scale verification of the mechanism.

2. **My registered reading R-A of the `C(127,64)` puzzle is WRONG in its
   arithmetic.** I registered `n' = n/M = 256`, hence `n = 2^42`. The
   razor is `n = 2^41`, `n/M = 128`. The plateau is `C(N-1, k/M)` with
   `N = 128`, not `C(n'/2-1, n'/4)` with `n' = 256`. My registered R-C
   had the right SHAPE (`C(n'-1, n'/2)`, `n' = 128`) but I labelled it a
   SUBSET count; the banked object is a LIST count.

3. **My registered LAW-QUOT was right as a mechanism and wrong as an
   identification.** The coset-invariant reduction to `(n/M, t'=1)` is
   real, is the round-29 Theorem A lifted, and I verified it exactly at
   three scales — but it is NOT the banked razor plateau. The banked
   plateau is a different family (`k/M` full cosets **plus a partial
   coset of size sigma**, which is not coset-invariant at all).

4. **P4 (lift-gain) MISS in direction of magnitude.** I registered
   `P(G(97)=0) = 0.60` — i.e. that the coset lift gains nothing
   structural. It gains: at `n=16, sigma=2` the lifted product word's
   exact list is **9**, of which exactly **7** are the coset-union sets
   (`= C(8,5)/8`, the quotient Theorem-A count) and **2** are genuine
   non-coset extras that survive to `q = 1000033`
   (`data/struct_n16_s2.json`). The gain is small but structural, not
   field noise.

5. **P8 probability was too low and P2/P6 were not tested.** I priced
   `P(C(127,64) resolves) = 0.45`; it resolves completely, and the
   resolution was available in one grep. P2 (maximiser class at n=8)
   and P6 (the `gcd(a',n')` refinement at `(24,4)`) were displaced by
   the object correction; P6's mechanism was however confirmed
   incidentally at `(20,2)` (see D3).

6. **One measurement DIED and is not in the ledger.** The second
   structure-dominated field for the key cell — exact global max at
   `n=12, sigma=2, q=61` — crashed with `MemoryError` in pass 2
   (`data/batch3.log`), was relaunched with a higher collection
   threshold, and its outcome is recorded in `data/batch5.log`. The
   `q=37` value stands alone as the structure-dominated exact global
   measurement at `sigma = 2`.

7. **DO-NOT-INHERIT honoured, and it bit.** I read the corrections
   before quoting: the round-28 "same fate likely" line is falsified
   (`critical/nodes/rate_half_band_crossing_location/statement.md:393`)
   and the ratio transport is refuted with the "0.1451 -> ~217 units"
   line flagged DO NOT QUOTE (same file, `:324`-`:335`). Neither is
   used anywhere below.

---

## D1 — THE FAITHFUL MODEL, POSED (registered pre-measurement, then corrected by measurement)

Registered before any measurement (`PREREG.md`, §R1): a supply model is
`(t,M)`-faithful iff it fixes and preserves (Q1) the word quantifier,
(Q2) the counting unit, (Q3) the level of the comparison, (Q4) the
normalization, (Q5) the excess law. The measurement forced **two more
axes** that no registration of mine anticipated:

* **(Q6) THE SLACK AXIS.** `deg Y - a` is not a nuisance parameter; it is
  where the entire supply surplus lives. Measured exactly: at
  `n=8, sigma=1` the max over ALL words per slack stratum is
  `{delta=0: 3, delta=1: 5, delta=2: 7}` (`data/global_n8_q41.json`,
  `q=41`, `q=73` identical) — the qcore/plateau value 3 is exactly the
  **minimal-slack** maximum, and the whole surplus is the climb to
  maximal slack. Same shape at `n=12, sigma=1`:
  `{0:61, 1:45, 2:52, 3:60, 4:66}` (`data/global_n12_q13.json`).
  The banked razor witness `Y = X^k L_T0` has `deg Y = k + sigma = a`,
  i.e. **slack 0** — the razor's banked supply lives in the one stratum
  where the cap is tight.
* **(Q7) THE OBJECT AXIS.** Round 29's `F_LIST` is, verbatim, the list-side
  object: `L_1(a)=max_u #{c in C: agr(c,u)>=a}`
  (`critical/nodes/rate_half_list_adjacent_crossing/statement_sections/00-live-contract-and-base-reductions.md:12`).
  It is NOT `B_mca`/`B_ca^far`, the object the razor's open content needs,
  and an audited guard forbids identifying them
  (`notes/literature_map_20260726/target_mappings.json:838`: "The node's
  own audited GUARD forbids reusing the list threshold q/2^128 as an MCA
  surrogate").

**First test case, as registered — the `C(127,64)` puzzle: RESOLVED.**
The banked plateau is the qcore count `C(N-1, k/M)`
(`critical/nodes/qcore/node.json:12`: "quotient cores produce at least
`C(n/M - 1, k/M)` codewords at agreement `k + sigma` whenever `M | k` and
`sigma < M`") with `n = 2^41`, `k = 2^40`, `M = 2^34`, `N = 128`,
`k/M = 64`. I re-derived the row from the banked exact integers rather
than assuming it (`data/razor_arithmetic.json`): `a^2/n = 567,069,900,800`
exactly (matches `2^39+2^34+2^27`), `GAP_FISHER = 532,441,726,975`
(matches), open-bracket width `532,575,944,704` (matches) — all three
banked constants reproduce **only** at `n = 2^41`.

And the reason round 29 could not match it: **the model's PLATEAU IS the
razor's qcore formula at `M = 2`, `sigma = 1`.** Verified as an exact
integer identity at `n = 8,16,32,64,128,256,512`
(`data/razor_arithmetic.json`, `identity_PLATEAU_is_QCORE_at_sigma_1`,
all `equal: true`):

```text
PLATEAU(n) = C(n/2-1, n/4) = C(n/M-1, k/M) with M = 2 = QCORE(n, sigma=1).
```

So `n_model = 256` reproduces `C(127,64)` because `n_model = 2N`; the
match is between two *different* points of one family — the model sits at
`(M,sigma) = (2,1)`, the razor at `(2^34, 2^34-1)`. The plateau agreed;
nothing else did.

---

## D2 — SMALL-t EXACT MEASUREMENTS

Three independent instruments, all exact integers, all in `scratch/`:

| instrument | object | method |
|---|---|---|
| `td_global.py` | `L_1(a)` = max over **ALL** received words | syndrome buckets over normalized weight-`<=m` error patterns; two-pass coarse counter for flat RAM; slack read off the syndrome |
| `td_delta0.py` | max over **minimal-slack** words | max bucket of `A -> (e_1(A),..,e_sigma(A))` over `F_q` |
| `td_c0.py` | the same in **characteristic zero** | same bucket, keys reduced modulo `Phi_n` in `Z[zeta_n]` (exact integers) |
| `td_scan.py` / `td_struct.py` | explicit words | exact `F_LIST`, `F_SUBSET`, agreement profile, agreement sets |

**Two escape tests, both green, both by a different algorithm from
round 29's.** `L_1` at `n=8, sigma=1` is **7** at `q = 17, 41, 73`
(`data/global_n8_q*.json`) — round 29's exhaustive value. The best
two-term word at `n=16, sigma=1` is `X^15 + cX^8` with
`F_LIST = F_SUBSET = 715` and flat profile `{9:715}`
(`data/scan_n16_q97.json`) — round 29's Theorem A word and count,
recovered by polynomial-remainder search instead of their Lagrange
criterion.

### D2.1 — the minimal-slack (qcore) stratum, in characteristic zero

The banked cap claim is char-0: "within the coset/dressing/perturbation
universe the char-0 supply is capped at the plateau (Lam-Leung +
NESTING…)" (`critical/nodes/rate_half_band_closure/node.json:9`). Exact
cyclotomic measurement (`data/char0_n*.json`):

| n | sigma | char-0 slack-0 max | QCORE `C(N-1,k/M)` | verdict |
|---|---|---|---|---|
| 8 | 1 | **3** | 3 | tight |
| 8 | 2,3 | **1** | 1 | tight |
| 16 | 1 | **35** | 35 | tight |
| 16 | 2 | **3** | 3 | tight |
| 16 | 3 | **3** | 3 | tight |
| 12 | 1 | **12** | 10 | **cap violated, +2** |
| 12 | 2 | **3** | 3 | tight |
| 20 | 1 | **128** | 126 | **cap violated, +2** |
| 20 | 2 | **10** | 3 | **cap violated, x3.33** |
| 20 | 3 | **4** | 3 | **cap violated, +1** |

**The dichotomy is exactly the 2-power condition.** At `n = 8, 16` (and
`n=24`, a non-2-power, the violation explodes to `34248` vs `462` at
`sigma=1`, `data/delta0_n24_q1000033.json`) the pattern is: the char-0
minimal-slack cap is *exactly* `C(N-1,k/M)` when `n` is a power of two,
and fails when `n` has an odd prime factor — precisely the Lam–Leung
vanishing-sum boundary the banked cap invokes, and precisely the domain
hypothesis the banked proof records
(`background/nodes/ww_lower_witnesses/proof.md:66`: "the construction
lives on a 2-POWER MULTIPLICATIVE evaluation domain D … the coset
structure is load-bearing"). **The razor is at `n = 2^41`, inside the
tight regime.** This is a positive, independent confirmation of the
banked THEOREM CAP in the stratum where the banked witness lives.

### D2.2 — exact global maxima over ALL received words

`data/global_n*.json`. `avg = C(n,a)/q^sigma` is the pigeonhole floor;
a cell is *structure-dominated* (razor-like) when `avg << 1`.

| n | q | sigma | a | m | `L_1(a)` exact | QCORE | avg | max at slack |
|---|---|---|---|---|---|---|---|---|
| 8 | 17/41/73 | 1 | 5 | 3 | **7** | 3 | 3.29/1.37/0.77 | `m-1` (max) |
| 8 | any | 2,3 | 6,7 | 2,1 | **1** | 1 | <0.1 | — |
| 12 | 13 | 1 | 7 | 5 | **66** | 10 | 60.9 | `m-1` (max) |
| 12 | 13 | 2 | 8 | 4 | **6** | 3 | 2.93 | 2,3 |
| 12 | 37 | 2 | 8 | 4 | **5** | 3 | **0.36** | `m-1` (max) |
| 16 | 17,97 | 4,5,6,7 | 12..15 | 4..1 | **1** | 1 | <0.03 | — |

`L_1 = 7 = C(8,5)/8` and `L_1 = 66 = C(12,7)/12` are Theorem A's value
**exactly** — so at `sigma = 1` Theorem A is not merely a lower bound
inside a one-bit bracket, it is the exact maximum at two scales (round 29
had this only at `n=8`). Theorem B's `2C(n,a)/n` (14, 132) is not
attained.

**The decisive cell** is `n=12, sigma=2, q=37`: the first exact global
maximum at `sigma >= 2` in a structure-dominated field. `L_1 = 5`,
against `C(n,a)/n = 41.25` (what a naive Theorem-A transport would
predict) and `C(n,a)/n^sigma = 3.44` (the Graham–Sloane-shaped guess) and
`QCORE = 3`. **Theorem A's `C(n,a)/n` law does NOT survive to
`sigma = 2`: it overshoots the true maximum by a factor 8.**

### D2.3 — zero power, declared

* `n = 16, sigma in {1,2,3}` exact global: **DEAD** — the syndrome census
  costs `C(16,5)*q^4 >= 2.9e8` normalized patterns at `q=17` for
  `sigma=3` and `8.4e9` for `sigma=2`. No exact global maximum exists
  in this report at a 2-power scale with `sigma >= 2`. Everything I say
  about 2-power `sigma>=2` maxima is a **lower bound** (explicit words)
  plus an exact **minimal-slack** maximum.
* `n = 32` in any stratum: dead (`C(32,18) = 4.7e8` subsets).
* Word families: `td_scan` covers one- and two-term words only. A
  three-term maximiser would be invisible to it; at `n=12, sigma=2` the
  two-term best is 4 while the true global maximum is 5, so the two-term
  family is provably NOT exhaustive.

---

## D3 — THE TRANSPORT LAW

**It does not generalize as round 29 hoped, and the reason is structural.**
For a received word of degree `d`, a codeword `f` is listed iff
`Y - f = L_A h` with `|A| = a`, `deg h = d - a`; matching the top
`sigma + 1` coefficients is `sigma` conditions on `A` after normalization.
At `sigma = 1` there is exactly one condition and it is the **cyclic**
one (`prod A` prescribed, `n` classes, `q`-independent) — that is the
whole content of Theorem A, and why the answer is `C(n,a)/n`. At
`sigma >= 2` the additional conditions are `F_q`-valued, not cyclic, and
the count collapses toward the pigeonhole `C(n,a)/q^{sigma-1}/n`. The
only families that survive the collapse are those in which the *coset
structure absorbs the extra conditions*. There are exactly two, and they
differ by one:

```text
QCORE(n,sigma)  = C(N-1, k/M),   N = n/M,  M = least admissible scale with M >  sigma
                  [agreement = k/M full cosets + ONE PARTIAL coset of size sigma]
CPW(n,sigma)    = PSUM(N', k/M'+1), N' = n/M', M' = least admissible scale with M' >= sigma
                  [agreement = k/M'+1 FULL cosets, prescribed product; = Theorem A at the quotient]
PSUM(N,a') = C(N,a')/N exactly when gcd(a',N)=1, strictly larger otherwise.
```

**Both verified at small scale, exactly.**

* CPW at `n=16, sigma=2` (`M'=2`, `N'=8`, `a'=5`): predicted
  `C(8,5)/8 = 7`. The lifted word `X^{14}+cX^{8}` (`= X^{n-M}+cX^{n/2}`)
  and `X^{15}+cX^{9}` both give `F_LIST = 9` with flat profile `{10:9}`
  (`data/scan_n16_q97.json`), and dumping the agreement sets
  (`data/struct_n16_s2.json`) shows **exactly 7 of the 9 are unions of
  `mu_2`-cosets** — the predicted quotient Theorem-A family — plus 2
  non-coset extras. Registered P7 predicted `SURPLUS(16,2) = 1.222 bits
  = SURPLUS(8,1)`: measured coset part `7/3`, **exactly 1.222 bits. HIT.**
* CPW at `n=20, sigma=2` (`M'=2`, `N'=10`, `a'=6`): the lifted word
  `X^{18}+X^{10}` gives `F_LIST = 20` at `q = 1000081` and 164 at
  `q = 41` (pigeonhole-inflated), vs `C(10,6)/10 = 21`
  (`data/lifted_productword_n20.json`). The shortfall of 1 is the
  registered `gcd` refinement: `gcd(a',N') = gcd(6,10) = 2 != 1`, so the
  prescribed-product classes are *not* equidistributed and `c = 1`
  selects a below-average class. **Mechanism HIT, normalization exactly
  as registered in R2.**
* QCORE: verified as the exact char-0 minimal-slack maximum at every
  2-power cell measured (D2.1).

**The law's one-line consequence.** `QCORE` and `CPW` disagree only when
`sigma` is *itself* an admissible coset scale — for a dyadic domain,
only when `sigma` is a power of two dividing `k`. **The razor's index
`sigma = 2^34` is exactly such a point**, and it is the point at which
`a_RH` is bracketed from below
(`critical/nodes/rate_half_band_crossing_location/statement.md:302`:
"a_RH(q) = k + 2^34 + O(1)"). The exact ladder at the razor row
(`data/razor_arithmetic.json`):

| sigma | QCORE (M > sigma) | CPW (M >= sigma) | max |
|---|---|---|---|
| `2^34 - 1` | `C(127,64) = 2^123.17143` | `C(128,65)/128 = 2^117.14907` | qcore, `2^123.17` |
| `2^34` | `C(63,32) = 2^59.66862` | `C(128,65)/128 = 2^117.14907` | **CPW, `2^117.15`** |

so the qcore cliff at the razor is **63.503 bits**, and the CPW cuts the
drop at the crossing index to **6.022 bits** — the CPW value stands
**57.480 bits** above the qcore family at `sigma = 2^34`. `C(128,65)/128
= 184,239,584,937,908,329,739,504,521,356,773,475` is an exact integer
(`gcd(65,128) = 1`, so Theorem A's rotation argument is exact here with
no `PSUM` correction).

**Against the need** (`2^127.90..2^128.00`,
`critical/nodes/rate_half_band_closure/node.json:9`): CPW at the crossing
index is **10.751..10.851 bits short**. It does not fire anything. See
the miss list — this number is a re-derivation of banked content.

---

## D4 — THE RAZOR VERDICT, HONESTLY SCOPED

**1. Round 29's "+115 bits over-satisfaction" is a scale artifact, and
the correct figure at the razor's own scale is not 115 but `1.1e12`.**
Evaluating the same `sigma = 1` law at the razor's own `n = 2^41` gives
surplus `1,099,511,627,735.5` bits over `QCORE(n,1)`
(`data/razor_arithmetic.json`, `sigma1_law_at_razor_scale`) against
`120.49` bits at `n_model = 256`. A quantity that changes by ten orders
of magnitude when you change `n` at fixed `sigma` was never transportable
in either direction; the model's `n = 2N` choice fixed the plateau and
let the supply float.

**2. The faithful transport does not over-satisfy — it falls short, and
the direction of round 29's model critique inverts.** At the razor's
index the best coset-family supply is `2^117.15`, i.e. below the need and
below the banked plateau. Every measured `sigma >= 2` cell agrees in
direction: the `sigma = 1` surplus dies. At fixed `sigma = 2`, the CPW
count grows polynomially in `N` while `QCORE` grows exponentially
(`n=8: 1 vs 1`; `n=16: 9 vs 3`; `n=32` would be `? vs 35`;
`n=64: ? vs 6435`), so at large `n` the qcore family dominates every
2-term word — the opposite of the `sigma = 1` picture where `C(n,a)/n`
(`~2^n`) always beats the plateau (`~2^{n/2}`).

**3. The lane is on the LIST side, and the transport that would make it
matter is forbidden.** `F_LIST` is `L_1`
(`…/00-live-contract-and-base-reductions.md:12`), and on that side the
crossing floor at `sigma = 2^34 - 1` is already PROVED: "the proved
cyclically rotated prefix floor gives `L_1(k+17,179,869,183)>B*`, so any
valid crossing satisfies `a_L(C)>=k+2^34`" (same file, `:31`-`:41`,
`(RHL-LB)`). The razor's open content in
`rate_half_band_crossing_location` is the MCA/CA object, and the audited
guard forbids using the list threshold as an MCA surrogate
(`notes/literature_map_20260726/target_mappings.json:838`). **So the
supply lane round 29 opened cannot reach the open content without a
CA/MCA conversion — that conversion, not `(t,M)`, is the missing
dictionary entry.**

**4. What the small-`sigma` window licenses about `sigma = 2^34` — the
extrapolation gap, stated exactly.**

| axis | measured window | razor | gap |
|---|---|---|---|
| `n` | 8 – 24 | `2^41` | `2^37` |
| `sigma` | 1 – 7 | `2^34` | `2^33` |
| `sigma/n` (relative excess) | `1/24` – `7/16` | `2^-7` | `x5.3` from the closest cell |
| `m/n` (slack budget) | `1/3` at the key cell | `0.4922` | `x1.5` |
| `q` | 13 – `10^6` | `< 2^256` | `2^236` |
| regime (`C(n,a)` vs `q^sigma`) | structure-dominated at large `q` | structure-dominated by `2^{2.2e12}` | **same regime** |

The last row is the only one that transports cleanly, and it is worth
stating: at the razor, `log2(C(n,a)/q^sigma) = -2.199e12`
(`data/razor_arithmetic.json`), so the pigeonhole term is absent by an
astronomical margin, exactly as in my large-`q` cells. Everything I
measured about *structural* (char-0) supply is therefore in the razor's
own regime; everything I measured about small-`q` inflation is not.

**5. Pre-registered falsifiers for the law (armed now).**
* **F-CAP.** The char-0 minimal-slack maximum equals `C(N-1,k/M)` for
  every 2-power `n`. FIRES on any 2-power cell where the exact
  cyclotomic bucket exceeds it. (Untested at `n >= 32`: `C(32,17)` = 565M
  subsets — priced, not run.)
* **F-CPW.** For dyadic `n` and `sigma = M'` an admissible scale, the
  best explicit supply is `PSUM(n/M', k/M'+1)`. FIRES on any explicit
  word at such a cell with `F_LIST > PSUM + (measured sporadic excess)`;
  the measured sporadic excess is `+2` at `(16,2)` and `+2` at `(12,1)`,
  so a jump of order `PSUM` itself would be needed to break the law.
* **F-SIGMA1.** `L_1(k+1) = C(n,a)/n` exactly (not merely within
  Theorem B's factor 2). Verified at `n = 8` (3 fields) and `n = 12`.
  FIRES at any `n` where the exact global maximum differs.
* **F-OBJECT.** If a proved CA/MCA conversion lands, the entire supply
  ladder above transports to `rate_half_band_crossing_location` and
  `sigma = 2^34`'s supply becomes `2^117.15` rather than `2^59.67`
  there — a 57.5-bit change in the gap anatomy at the crossing index.

**6. Zero-power declarations.**
* **No exact global maximum at any 2-power `n` with `2 <= sigma <= n/2-4`
  exists in this report.** The `sigma >= 2` global maxima I have are at
  `n = 12` (not a 2-power, and its char-0 minimal-slack cap is itself
  violated by Lam–Leung) and at degenerate cells (`m <= 4`, where
  `2a - n > k-1` forces `L_1 = 1`). Any claim that the `sigma >= 2`
  surplus over `QCORE`/`CPW` is bounded at 2-power scales is
  **unsupported by measurement**; my window sees only the `+2` sporadics.
* **Nothing here measures `B_mca`, `B_ca^far`, `S_sparse` or the tangent
  column.** Zero power on the razor's actual open content.
* **Nothing here measures `q`-dependence at cryptographic `q`.** My
  largest field is `10^6`; the structure/pigeonhole separation is
  verified, the arithmetic of `2^256` is not.
* **The `c` bracket is untouched.** I make no claim about
  `a_RH = k + 2^34 + c`; the consumer bar (`c = 0` is the only value
  serving `adjacency_closing`,
  `critical/nodes/rate_half_band_crossing_location/statement.md:320`) is
  quoted, not moved.

---

## Novelty subtraction (CATCH-24A, run before every claim above)

Own-repo greps (`critical/`, `background/`, `notes/`, `tools/`,
excluding `prize-codex-*` and the quarantined ledger):

* `"C(128,65)"` — 5 hits, incl.
  `background/nodes/rate_half_multiplicative_amplification_floor/proof.md:26`
  and `background/nodes/quotient_row_subjohnson_bound/sjb_findings.md:44`.
  **The binomial is banked.**
* `"C(128,65)/"`, `"C(N,N/2+1)/N"` — 1 hit,
  `notes/literature_map_20260726/target_mappings.json:838`. **The divided
  form and its razor reading are banked.** My headline is a
  re-derivation; reported as miss 1.
* `"prescribed product"`, `"Graham-Sloane"`, `"product word"` — hits only
  in round-29's `slack_recursion/` files and the round-29 addendum at
  `critical/nodes/rate_half_band_crossing_location/statement.md`. The
  Theorem A object is round 29's, credited as such throughout.
* `"C(63,32)"` — banked, but in the `petal_g1` kill arithmetic
  (`critical/nodes/petal_g1_layer_maps/notes/cp_packet_20260713/cp_findings.md:31`),
  not as the razor's `sigma = 2^34` supply. The identification of
  `C(63,32)` as the qcore-family value **at the crossing index** is not
  in-repo as far as these greps reach.

**What I claim as new, after subtraction:** (i) the `PLATEAU = QCORE at
(M,sigma)=(2,1)` integer identity, which explains the `C(127,64)`
coincidence exactly; (ii) the `sigma < M` vs `sigma <= M'` one-step
distinction between the two coset families and the observation that they
separate exactly at powers of two, i.e. exactly at the razor's index;
(iii) the char-0 exactness of the minimal-slack cap at 2-power `n` with
its Lam–Leung failure off the 2-powers, measured; (iv) `L_1 = C(n,a)/n`
exactly (not just within a factor 2) at `n = 8, 12`; (v) the exact global
`sigma = 2` datum `L_1 = 5` refuting the `C(n,a)/n` transport by a factor
8; (vi) the slack axis as the location of the entire surplus. Claim
strength: (i)–(ii) are exact integer identities; (iii)–(vi) are exact
measurements inside a small window with the extrapolation gap tabled above.

---

## Predictions vs outcomes (registered in `PREREG.md` §R3, before any measurement)

| # | registered | outcome |
|---|---|---|
| P1 | `L_1(8,1) = 7` at `q=17,41` | **HIT** tol 0 (also `q=73`) |
| P2 | maximisers = product-word class, profile `{5:7}` | **HIT in kind** at `n=8,16` (`{9:715}` flat); the `n=8` census structure not separately dumped |
| P3 | invariant reduction `(16,2) -> (8,1)` exact | **HIT** — 7 of the 9 listed codewords are exactly the quotient family |
| P4 | lift-gain `G(97)=0` w.p. 0.6, `G(17) in [1,120]` | **MISS** — gain is `+2` and structural (survives `q=10^6`) |
| P5 | every coset-faithful point `= PSUM(n',a')` exactly | **PARTIAL** — equals `PSUM` plus a small sporadic excess (`+2` at `(16,2)`, `-1` at `(20,2)` because `c=1` picks a below-max class) |
| P6 | `gcd` refinement matters when `gcd(a',N)!=1` | **HIT** (at `(20,2)`, not the registered `(24,4)`) |
| P7 | `SURPLUS(16,2) = 1.222 bits = SURPLUS(8,1)` | **HIT** tol 0 on the coset part (`7/3`) |
| P8 | `P(C(127,64) resolves) = 0.45`, R-A most likely | **MISS on the reading** (R-A's `n=2^42` is wrong; R-C's shape is right); the puzzle resolves completely |
| P9 | razor surplus `= +120.49` bits, unfaithfulness in Q1/Q2 | **MISS on the number** (the faithful figure is a 10.75-bit *deficit*); **HIT on the direction** — the unfaithfulness is indeed not in `t`, it is in the quantifier/unit, and specifically in Q6 (slack) and Q7 (object), which I did not register |
| P10 | supply at `sigma>=2` is `q`-dependent, at `sigma=1` not | **HIT** — `sigma=1`: 7/7/7 at `q=17/41/73`; `sigma=2` at `n=16`: 32/5/3 at `q=17/97/10^6`, the excess decaying to the structural 3 |

Registered fallback rule R5.1 ("if the measurements refute LAW-QUOT,
report the refutation as the headline and do not rescue the law by
re-reading the quantifier") did not need to fire — LAW-QUOT survived as a
mechanism; R5.2 and R5.3 (zero-power declarations) both fired and are
honoured in D2.3 and D4.6.

---

## Compliance

**COMPUTE LAW.** 45 interpreter invocations, every single one under
`tools/ramguard` from the repo root with a literal `--`: 10 under
`tiny` (JSON peeks, prime/qcore tables, result tabulations, one
independent cross-check of a suspicious count) and 35 under `local`
(all measurement runs), of which 10 ran inside five backgrounded
wrappers with per-cell JSON checkpointing. **Zero bare `python3`
invocations.** `RAMGUARD_TIMEOUT` was used and is documented here: `280`
for the batched foreground ladders (to stay under the profile wall while
running several cells per call), `1800` for the `n=12`/`n=20`/`n=24`
background batches, `2400` for the `n=16` two-term scans, `900` for the
`n=20` lifted-word test, and `5400` for the two `n=12, q=61` attempts.
No run hit its wall. **One run hit its RAM ceiling and died**
(`n=12, q=61`, `MemoryError` in the collection pass,
`data/batch3.log`) — disclosed in miss 6, relaunched with a higher
collection threshold (`data/batch5.log`), and no number in this report
depends on it. Stdlib only; no Modal, no network, no git, no subagents.

**RAM DISCIPLINE.** `dag.json` was never opened (node shards + grep only,
per the write-path rule). Reads were file-at-a-time, and the two large
statement files were read in offset windows, never whole. The global
instrument uses a saturating `array('B')` coarse counter plus a
threshold-gated second pass precisely so no bucket table is ever
materialised at `q^{n-k}` scale; the one time that discipline was
violated by too low a threshold, the cgroup killed the run (above).

**QUARANTINE.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never
opened at any line — it appeared in one `grep -rl` file listing and in
one persisted grep output, and was excluded by an explicit filter in
every subsequent grep. The sibling round-31 directories
`rh_overlap_cap`, `rh_type2_stratum`, `rh_e_axis_audit` were never read;
they appeared only as names in one `ls` of the shared parent
`notes/pilots_20260810/`. No path containing `prize-codex-` was read,
written, or listed; every grep filtered it explicitly. Round-29
`slack_recursion` files were read as the two named anchors only; I wrote
my own instruments rather than copying their scratch scripts, so no
banked script was executed.

**WRITE SCOPE.** Every write landed inside
`notes/pilots_20260810/rh_transport_dictionary/` — `PREREG.md`
(registrations appended under `## Pilot registrations` **before** any
computation and before any read beyond the two anchors), this
`REPORT.md`, `scratch/` (6 scripts: `td_core.py`, `td_delta0.py`,
`td_global.py`, `td_c0.py`, `td_scan.py`, `td_struct.py`, `td_razor.py`),
and `data/` (28 JSON result files + 5 batch logs). No `dag/`, `nodes/`,
`critical/`, `background/` or `tools/` file was modified; no git
operation of any kind was run.

**BLIND PRIORS.** §R0–R6 of `PREREG.md` (the faithfulness definition, the
candidate law shapes, P1–P10 with windows, four falsifiers, five fallback
rules and the route prices) were written after reading only
`slack_recursion/REPORT.md` and `slack_recursion/MINT_PACKAGE.md`, and
before the first grep, the first node read and the first computation.
The outcomes table above was written afterwards and is labelled as such.
Misses are reported first.
