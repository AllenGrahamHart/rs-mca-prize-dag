# Literature-map audit — maelcar PRs #1145–#1148 (przchojecki/rs-mca)

Date: 2026-08-03. Auditor: Opus audit pilot (round-10 pilot 1).
Author under audit: **maelcar** = Manuel Elías Rey-Álvarez Zafiria.
Access: read-only `gh`. Nothing pushed, commented, or written upstream.
Working dir: `notes/pilots_20260803/maelcar_audit/` only.

Gate discharged: `notes/PR_SWEEP_20260803.md:25-28` ("ACTION REQUIRED
before our next L1 or LIST/M31 move"). Nothing below is adopted into
`dag.json`; every unreplayed item is labelled.

---

## 0. Replay ledger (what I actually ran)

All under `tools/ramguard local -- python3`. C++ primaries skipped per
compute law and recorded as **UNREPLAYED**.

| # | artifact | result | what it really proves |
|---|---|---|---|
| 1145 | `audit_p04cu_exact_five_witness_family.py` | **PASS** | recomputes the named witness spectrum, petal values, core profile, deletion minimality, H-stabiliser, all 6 padded rows |
| 1145 | `audit_p04cv_parity_and_exceptional_profiles.py` | **PASS** | recomputes 250/2 dichotomy, both exceptional profiles, parity transport on 2 states |
| 1146 | `audit_p04cw_parity_uniform_S6_theorem.py` | **PASS** (83 s) | recomputes `S_3(P|Q^2)` for **every** terminal state, asserts `max == 10`; 252 line states, 241 five states, 483 profiles |
| 1147 | `verify_p06b3w_decorated_product_line.py` | **PASS** | symbolic identity + `Res_a(L,R) = (r-1)^2 (r-t)^2` |
| 1147 | `audit_p06b3v_cubic_divisor_and_product_cells.py` | **PASS** | reproduces recorded JSON exactly (T = 0, 9, 1; max K = 2, 2) |
| 1147 | **`replay_1147_counterexample.py` (MINE, from scratch)** | **PASS** | independent reimplementation; reproduces their n=128 counterexample exactly |
| 1148 | `C_verify_SP01zxab_full_affine_hull_synthesis.py` | **PASS** (46 ms) | *aggregation only* — recomputes no sieve |
| 1148 | `A_/B_ SP01zxaa_Schur_power_profile.py` | **PASS** (20 s each) | genuine linear algebra from the fixture; profile (16, 136, 509) |
| 1148 | `A_/B_ SP01zxaa_rational_bidegree_barrier.py` | **PASS** | 13,234 determinant / rank checks |
| 1148 | `A_/B_ SP01zxa9_principal_Cauchy_route_cut.py` | **PASS** | 4x4 minor witnesses on all 509 rows |
| — | **`handcheck_1145.py` (MINE)** | **6/6 PASS** | independent structural checks, below |
| — | **`reconcile_1147_vs_our_h4_census.py` (MINE)** | **exact** | bridges their `T_sm` to our banked census |
| — | **`t4_ladder_vs_sol_target_4.py` (MINE)** | — | evaluates **our** SOL_TARGET_4 on their row |

UNREPLAYED (C++ / HPC): the #1145 `p04cu` spectrum census; the #1146
SymPy `derive_*` reduction stages; **all** #1148 partition sieves
(10.69 billion normals); #1147's `max C_r = 5789`.

---

## 1. PR #1145 — L1 `ell = 11` exact-five onset + six-fibre certificates

### (a) What is claimed

`p = 331`, `H <= F_p^*` of order `ell = 11`, `Gamma = sum_{a in A} gamma_a X^a`
with `A subset {1..10}`, `|A| = 5`, all `gamma_a != 0`.

1. Exact **envelopes** `(S_6,S_7,S_8,S_9) = (20,22,24,27)` over `F_331`;
   census visits 2,509,920 projective four-root kernel rows, 2,472,120 keep
   five-coordinate support, no rank-deficient cell; vectors outside have
   fibre cap `<= 3`.
2. Witness `A = {1,3,5,7,9}`, `gamma = (1,15,45,179,176)`, spectrum
   `5^2 3^2 2^4 1^22`; primitive divisibility-minimal anchors at
   `tau = 6,7,8`; padding gives a listed word in every positive-defect row
   `(tau,m) in {(6,8),(6,9),(6,10),(7,9),(7,10),(8,10)}`. Hence **every**
   prime-field, background-free, `ell=11`, exact-five, positive-defect row
   with `tau >= 6` is non-vacuous.
3. Support dichotomy: of 252 supports, 250 have `g_A = 1`; the only
   `g_A = 2` supports are `{1,3,5,7,9}`, `{2,4,6,8,10}`. Parity transport
   `S_{2h}(Gamma) = 2 S_h(P|Q^2)`.
4. Six-fibre: the normalized 6x6 cyclotomic norm table has prime divisors
   `= 1 mod 11` only `23, 67, 199, 419`; `23, 67` have fewer than 11
   quotient labels so cannot realize the geometry; censuses at 199, 419
   satisfy the target bound.

**Nonclaims (theirs, explicit):** the four `tau = 5` rows are not settled;
the 250 `g_A = 1` supports are not globally classified; no extension field,
arbitrary background, whole-ImgFib, or list-grand conclusion.

### (b) Subtraction against our record — BOTH WAYS: **empty**

Our repo contains **nothing** in this lane. No `S_k` object of this kind, no
`mu_11`, no `F_p^*/mu_11`, no `p = 1 mod 11` statement, no `F_199/F_331/F_419`
fixture. The only occurrences of any of their strings are our own PR-sweep
minute written today.

- **Nothing of theirs closes or reprices any node of ours.** Our open L1
  items (`imgfib` CONDITIONAL, `l1_mixed_petal_amplification` TARGET,
  `petal_mixed_amplification` TARGET) are asymptotic, at official rows, and
  bind in the **sub-Johnson** range `s^2 <= n(k-1)`. A fixed-`ell`,
  fixed-shape, small-prime constant does not touch them.
- **Nothing of ours dominates theirs**, with one open check: our
  `l1_program_frontier` **Theorem J** (PROVED) is uniform in `n, k, q` —
  strictly more uniform than "all `p = 1 mod 11`". *Action:* translate their
  row to `(n,k,s)` and test `s^2 > n(k-1)`. If super-Johnson we cover the
  bound (never the sharpness); if sub-Johnson we cover nothing.

> **FALSE-FRIEND FLAG.** `background/nodes/dli_wcl_ell4_weight11_quintic_divisor_descent/`
> (PROVED) contains `11`, "quintic", cyclotomic roots and a Bezout-flavoured
> normalisation — but it is **`ell = 4`, weight `= 11`, over `mu_2048`**, a
> different object. Same for `notes/ell4_uniform_form_20260727.md`. Do **not**
> score either as prior coverage of `ell = 11`.

### (c) Trust: **VERIFIED** (non-vacuity) / **PLAUSIBLE-UNREPLAYED** (census)

Both auditors PASS locally and the `cu` auditor genuinely **recomputes** the
witness spectrum from `gamma` (`Counter{1:22, 2:4, 3:2, 5:2}`), not merely
reads it. But it only **asserts** the certificate's envelope field equals
`[20,22,24,27]`; the census behind it is C++-only.

My six independent hand-checks (`handcheck_1145.py`) **all PASS**:

- 252 = 250 + 2 dichotomy, and the two `g_A = 2` supports, recomputed.
- **AGL(1,11) has exactly 6 orbits on 6-subsets of Z/11** — matching their 6
  representatives. This is what makes the six-fibre reduction finite, and it
  is independently confirmed.
- The recorded 6x6 norm table's prime divisors are `{2,3,5,23,67,199,419}`;
  those `= 1 mod 11` are exactly `{23,67,199,419}`. `q = (p-1)/11` is 2 and 6
  for `p = 23, 67`, both `< 11` — the exclusion is valid arithmetic.
- **Census enumeration law.** I derived `rows = 252 * (C(11,4)*q + 60)` and it
  holds **exactly** at all three primes (199/331/419), with a
  **prime-independent** 37,800 degenerate rows in every case. This is a strong
  integrity signal for the unreplayed C++ census (a miscount would almost
  certainly break the fit).

**FLAG — presentation, LOW.** Note §3 reads
`"p = 199: S_6 = 20, profile 6^1 2^8 1^9"` as if one state. That profile has
`S_6 = 16`, not 20. The `20` is the **census envelope**; the profile is the
**max-fibre** state (certificate fields are literally `max_fibre_*`). Under
the intended reading everything is consistent — but a careless reader gets a
false statement. Same at `p = 419`.

**FLAG — scope, MEDIUM.** The envelope `(20,22,24,27)` has *increasing*
increments `(2,2,3)`, so **no single state attains all four**; it is a per-`h`
maximum over the family. Their own witness gives `(20,22,24,25)`. Never cite
`(20,22,24,27)` as one state's spectrum.

Minor: three padded rows sit **exactly** at the listing threshold
(`agreement == threshold` at `(6,8), (6,9), (6,10)`). Tight but valid.

### (d) Impact on our lanes

None forced. If we ever enter `ell = 11`, cite this as the fixture of record
and cite the sharp constant from #1146. Guard against the `ell4_weight11`
false friend being scored as coverage.

---

## 2. PR #1146 — sharp prime-uniform parity `S_6` bound

### (a) What is claimed

For **every** prime `p = 1 mod 11` and **every** reduced quintic
`P = c1 Z + ... + c5 Z^5` with all `c_i != 0`:

```
S_3(P | Q^2) <= 10,      Q = F_p^*/mu_11,  Q^2 = image of squaring
```

sharp; hence `S_6(Gamma) <= 20` for **both** parity supports, with equality
over `F_199` at `P = Z + 115Z^2 + 41Z^3 + 28Z^4 + 146Z^5`.
Two branches (four-fibre: 465 cells, 602 candidate primes, 24,720
specializations, 252 states in 29 primes; five-fibre: 630 cells, 80 primes,
21,150 specializations, 241 states in 24 primes).

**Nonclaims (theirs):** exactly the two parity supports — not the 250
`g_A = 1` supports, not extension fields, not arbitrary backgrounds, not
ImgFib, not the global list bound.

### (b) Subtraction — **empty both ways** (as #1145)

Two findings that neither PR states, extracted from #1145's certificate:

> **Their result covers the EXTREMAL case.** At **both** `p = 199` and
> `p = 419` the recorded census gives `gcd1_maxima = 18,21,24,27` and
> `gcd2_maxima = 20,22,24,27`. So `S_6 = 20` is attained **only** on the two
> parity supports; the 250 `g_A = 1` supports come in at **18**. #1146 proves
> the binding case, and the "remaining 250" are empirically not binding for
> `S_6`. This materially raises the value of the PR.

> **COUNTERWEIGHT FLAG — do not over-cite.** #1145's certificate field
> `remaining_global_obligations[0]` asks to prove **`S6 <= 21`** for the
> `g_A = 1` supports — *not* `<= 20`. So the global statement their programme
> would yield is `S_6 <= 21`, not `S_6 <= 20`. **Never cite "S_6 <= 20 for
> ell=11 exact-five" as a global fact.** It is proved for 2 of 252 supports.

### (c) Trust: **VERIFIED** (terminal) / **PLAUSIBLE-UNREPLAYED** (reduction)

The independent scalar auditor is the real thing: 83 s of recomputation, and
it asserts `maximum == 10` after **recomputing** `S_3` on `Q^2` for every
terminal state (line 283), `even_s6 <= 20` per state (281), the transport
identity `S_6 = 2 S_3` (203), anchor rank 4, exact-five support, quotient-label
injectivity, the Bezout norm prime factorizations (36–39), and a SHA-256 of
the rendered artifact (29).

**What I did NOT verify:** the *reduction/exhaustiveness* — that every
`(p,P)` with `S_3 > 10` must appear among the audited cells. That lives in the
SymPy `derive_*` stages plus prose. The auditor does confirm
`characteristic_zero_nontrivial_rows` is empty for both filters.

Hand-checks all pass: `465 = C(30,2) + 30` (unordered pairs with repetition
over the 30 four-root classes); `630 = 42 x 15`; and the `F_199` equality
witness verifies end-to-end — `|Q| = 18 = (199-1)/11`, `|Q^2| = 9 = |Q|/2`,
spectrum `4^2 2^2 1^5` gives `S_3 = 10`, doubling to `4^4 2^4 1^10` gives
`S_6 = 20`.

### (d) Impact

Cite as the sharp constant if we enter `ell = 11`. No node of ours moves.

---

## 3. PR #1147 — Paper-D cubic + product-line reductions ★ prize-relevant

### (a) What is claimed

`H = mu_n(F_p)`, `n = 2^s >= 8`, `T_sm(H)` = unordered common-scale orbits of
smooth disjoint quartic trades.

1. Cubic-divisor identity `(X-1)Q(X) = (X-r)P(X) - (1-r)P(1)` with the affine
   coefficient transform; **`sum_{r in H\{1}} C_r = 32 T_sm`**.
2. **`sum_{d != e} K(d,e) = 8 T_sm`**. Hence `T_sm <= n^2/2` is equivalent to
   either `sum C_r <= 16 n^2` or `sum K <= 4 n^2`.
3. Decorated product line with `Res_a(L,R) = (r-1)^2 (r-t)^2` (never doubly
   degenerate); `9 sum C_r = 288 T_sm`.
4. Rows `(16,17,0,0)`, `(32,97,9,2)`, `(32,193,1,2)`.
5. **Counterexample:** at `n = 128, p = 257`, `T_sm = 22476`, `max K = 26`,
   `max C_r = 5789` — so pointwise `K(d,e) <= 4` is false without a
   large-characteristic hypothesis; "the global target itself fails outside
   the active regime."

**Nonclaims (theirs):** the active-characteristic aggregate energy inequality
stays open; this closes no Paper-D row.

### (b) Subtraction — our exposure is **ZERO**, and there is a **bridge**

**We never assumed a pointwise `K(d,e) <= 4`.** Zero hits for `K(d,e)`,
`K_{d,e}`, `kappa(d,e)`, `T_sm`, `C_r`, "smooth quartic", "quartic trade"
across all 1770 `dag.json` nodes, `critical/`, `background/`, `experiments/`,
`formal/`, `orbit/`, `upstream_dag/`. `git log --all -S` confirms these
strings entered the repo only via today's PR-sweep minute. None of the 18
Paper-D-touching nodes consumes a pointwise cap.

Our actual Paper-D cap constants are a different object: the universal cap
reserve `eta = 2^-9` (`2^-10` at rate 1/16) in `cap_theorem` (PROVED), and
the v13.2 census-floor constants in `v13_2_discrete_subfield_census_guard`
(PROVED). No cap constant of ours has value 4.

**Precedent, not damage:** we independently reached the same
pointwise-to-aggregate conclusion in another lane.
`critical/nodes/u1_x4_direct_column_budget/notes/F3_IDENTIFICATION.md` §3
rejects the max-fibre (pointwise) form as "hopelessly lossy" and requires the
collision-census form; `background/nodes/f3_h3_mobius_overlap_cap35/frontier.md:16`
records "The pointwise cap was replaced on the critical path by the weaker
weighted node". Their finding **confirms our instinct**.

**★ BRIDGE — the highest-value item in this audit.** Their `T_sm` *is* our
SOL_TARGET_4 shallow collision census, restricted and normalized. Proved
exactly at `(32,97)` (`reconcile_1147_vs_our_h4_census.py`):

```
our banked (32,4,97): 792 = 2 x 396          [F3_IDENTIFICATION.md:21]
  396 unordered matched disjoint pairs   <- reproduced exactly
  396 = 288 smooth + 108 non-smooth
  288 smooth = 9 free shift-orbits of size 32 = their T_sm = 9   MATCH
```

Matching `e1,e2,e3` is matching `p_1,p_2,p_3` (Newton), i.e. **our `T_4`
matching condition**. With free orbits `T_4^{smooth,ordered} = 2n T_sm`, so

> **their Paper-D smooth target `T_sm <= n^2/2` is exactly our SOL_TARGET_4
> bound `T_4 <= C N^3` with `C = 1`, restricted to the smooth locus.**
> Same conjecture, different currency.

**OVERCLAIM FLAG — MEDIUM.** `9 sum C_r = 288 T_sm` is **not** an independent
third currency: it is `9 x` identity (1). In their own auditor the decorated
counter increments exactly 9 times per cubic record (the `3 x 3` loop over the
two residual cubics' roots), so the `288T` assertion is **vacuous** given the
`32T` assertion already checked two lines earlier. There are **two**
independent currencies, not three. The genuine content of §2 is the
product-line identity and the non-degeneracy resultant, both of which do check
out symbolically.

Minor: the note writes `sum_{d,e in H, d != e}` but the auditor never enforces
`d != e`; it sums all occupied cells.

### (c) Trust: **VERIFIED** — the strongest package of the four

Both their Python artifacts replay clean, reproducing the recorded JSON
exactly. But **the counterexample — the headline claim — is in no certificate
and no Python auditor.** It exists only as C++ and as prose in the note. It is
also the most prize-relevant claim in the batch, so I reimplemented it from
scratch from their note's definitions:

- validated my implementation against **both** of their certified rows —
  `(32,97) -> T_sm = 9, max K = 2` and `(32,193) -> T_sm = 1, max K = 2`,
  both **exact matches**;
- then ran `n = 128, p = 257`:

```
  smooth disjoint matched pairs : 2876928
  all orbits free               : yes
  T_sm = 2876928 / 128          : 22476     (their claim: 22476)  MATCH
  sum K = 8 T_sm = 179808       : confirmed
  max K(d,e)                    : 26        (their claim: 26)     MATCH
```

**Their counterexample is VERIFIED by independent replay.** So is their scope
statement: `T_sm = 22476 > n^2/2 = 8192`, i.e. the Paper-D target itself fails
at that row — the counterexample lives **outside** the active regime, and does
**not** refute a pointwise cap *within* it.

Residual gap: `max C_r = 5789` — my replay computes product cells, not
cross-ratio multiplicities. **PLAUSIBLE-UNREPLAYED.**

### (d) Impact — a real one, on **our own** conjecture

Their row is an **admissible row of SOL_TARGET_4**: `q = 257` is an odd prime
`> 4`, `N = 128` is a power of two, `128 | 256`. And our conjecture
(`SOL_TARGET_4_H4_COLLISION_CENSUS.md:26-28`) says "for **all** `(q,N)` as
above" — it carries **no `q`-vs-`N` hypothesis**. So I evaluated our own `T_4`:

```
densest admissible row per N        T_4        N^3      T_4/N^3
  N= 16 q= 17                       252       4096       0.0615
  N= 32 q= 97                       792      32768       0.0242   <- our banked 792, exact
  N= 64 q=193                     42672     262144       0.1628
  N=128 q=257                   6022240    2097152       2.8716
```

Resolving `q` from `N`: **`T_4/N^3` decays with the index `(q-1)/N`** to a
stable floor (~0.0017 at `N=32`, ~0.0016 at `N=64`) — consistent with our
structured-family classification at large `q`. **But at fixed small index it
grows fast:**

```
  index 3: (32,97) -> (64,193)    implies T_4 ~ N^5.75
  index 2: (8,17)  -> (128,257)   implies T_4 ~ N^5.38
```

> **FLAG — SOL_TARGET_4 is at risk as literally stated.** Either it needs an
> index / `q`-vs-`N` hypothesis, or it is false at bounded index. Two
> independent small-index families both indicate an exponent near `N^5.4-5.8`,
> far above `N^3`.
>
> **This is evidence, not a falsification**: two-point exponent estimates at
> small `N`. The decisive test is `N = 256, q = 769` (index 3), needing
> `C(256,4) = 174,792,640` quartets — a C++ / large-memory job, not feasible
> under our ramguard budget.

---

## 4. PR #1148 — M31 affine syndrome-locator hull rigidity

### (a) What is claimed

Over `F_p`, `p = 2^31 - 1`, in the punctured M31 rank-two fixture, with
`F_0..F_15` its sixteen known monic degree-479 split syndrome locators:

```
Aff(F_0,...,F_15) INTERSECT {degree-479 locators split on the
                             1,023-point fixture domain} = {F_0,...,F_15}
```

proved by classifying all `2^16 - 1 = 65,535` nonempty coefficient supports
(2–3 sparse census; 4–8 support-specific sieves; 9–16 two support-parametric
sieves over `26,333` supports). Sieves process 10,694,457,224 and
10,694,457,231 admissible projective normals; all row sets full rank, all
split margins positive, min dense margin 10. Route cuts: no rational
`P_a/Q_b` with `a+b <= 12` on any of 509 core rows; Schur profile
`(16,136,509)` — square maximal, cube fills ambient — so not GRS / not
low-product-dimension.

**Nonclaims (theirs, explicit and important):** does **not** prove every split
locator in the full syndrome section lies in the hull; no complete fixture-list
equality; no typed first-match deployment; no Paper-D row.

### (b) Subtraction

> **CORRECTION TO THE BRIEF.** `kb_*` in our tree means **KoalaBear**
> (`p = 2130706433`), **not** kernel-basis. There are **zero** `kb_*M31*`
> nodes and zero M31 content in any `rate_half_kb_*` node. The premise "our
> `kb_*` M31 exports built on these sixteen locators" **has no referent**. Our
> kernel-basis programme is `notes/kernel_basis/` with K1–K5 / WP1–WP7 labels.

**We do not have their fixture.** No sixteen M31 locators, no affine hull of
them, no 65,535 sweep anywhere in our record.

**Same ambient family, different fixture — adjudicated.** Their fixture (read
from `SP01zxa_quadratic_cover_pair_input.txt`): `p = 2^31-1`, **509**-point
core, **16** locators supplied as 14 principal + 2 distinguished (indices 5
and 11 carry the degenerate parameter pairs `(1,0)` and `(2,0)`, matching
their "fourteen plus two pencil"), degree **479**, domain **1,023**. Ours:

| | domain | support/degree | core | objects |
|---|---|---|---|---|
| theirs (#1148) | 1,023 | 479 | 509 | 16 |
| `l1_m31_t64_quotient_prefix_intercept_fence` (PROVED, #1048) | 1,022 | 479 | 415 | 7 |
| `l1_m31_depth32_uniform_intercept_counterexample` (PROVED, #1102) | 1,022 | 479 | — | 1,237 |

Same degree 479 and the same `~1023`-point M31 quotient-profile family;
**different specific fixture**. So: **no duplication, but a strong citation /
adjacency duty.**

**Apparent tension — resolved.** Our
`l1_m31_fixed_support_divisor_direction_cap_route_cut` (PROVED) exhibits a
**6-dimensional** space containing **67,449 split** divisors — the opposite
direction to "15-dim hull has only 16 split members". **No contradiction:**
ours is degree 4,980 at `N = 1,053,557` (rank-seven proper-G terminal); theirs
is degree 479 at 1,023. Different regimes. But the principle survives and
matters: in our M31 lane, *"low-dimensional implies few split members" is
FALSE as a dimension-driven principle*, so their result cannot be lifted off
its fixture. They concede fixture-specificity.

**★ DOMINATION — the decisive item.**
`background/nodes/rate_half_list_chamber_affine_rank_bridge/` (**PROVED**,
route fence) is precisely the audit their PR presupposes, and we already
proved **it does not fire**: locator-side geometry and codeword/affine-side
counts are different objects and "this repo contains no map between them";
0/13 chambers killed. A classification of which members of a **locator** affine
hull split is a locator-side statement. **It moves no list count, no row, and
no chamber unless it ships an explicit incidence-to-codeword map. Demand that
map before pricing anything.**

Also: `upstream_gfv4_affine_span_list_compiler` (PROVED) at direction
dimension 15 on our M31 row gives a cap `~7.5 x 10^17` — numerically vacuous
against 16 vertices. We do not already have their bite; they do not duplicate
the compiler.

**GRS/Schur — their direction is the safe one.** We own
`rate_half_ca_hankel_..._non_grs_route_fence` (PROVED): a self-dual `[8,4,5]`
MDS code over `F_11` with Schur-square dimension 7 that is **not** GRS —
"general Schur-square rigidity is insufficient". That fence kills arguments of
the form *"Schur matches GRS therefore hidden GRS"*. Theirs runs the other way
(`dim C^(2) = 136` maximal, vs `2k-1 = 31` for GRS, therefore **not** GRS), so
**our fence does not kill it.** Confirmed by replay.

**Author precedent:** registry has maelcar at #1015–#1018 classified
ANALOGY_ONLY + citation duty. And our house verdict on exhaustive `2^16`
sweeps (`SOL_TARGET_2`): "a complete finite sweep can be true and
information-free."

### (c) Trust: **VERIFIED** (route cuts) / **UNREPLAYED** (the sieves)

All six Python verifiers PASS locally, and the Schur pair is genuine work —
20 s each of linear algebra **from the fixture**, by two different methods
(pivot-based primary; Horner-from-reconstructed-coefficients independent),
both returning `(16,136,509)`. I hand-verified `136 = C(17,2) = k(k+1)/2`, so
the Schur square is **maximal**, and a dim-16 GRS would give `2k-1 = 31` — the
route cut is structurally valid. I also hand-verified
`sum_{s=9}^{16} C(16,s) = 26,333`, `C(16,8) = 12,870`, `2^16-1 = 65,535`.

**But the synthesis is aggregation, not proof.** `C_verify...synthesis.py`
runs in 46 ms and recomputes **no sieve**: it checks support counts equal
`C(16,s)`, margins `> 0`, "no new split locator", primary/audit histogram
agreement, and the arithmetic. **All 10.69 billion normals are C++/HPC and
UNREPLAYED.** The theorem rests on those.

> **FLAG — MEDIUM, unexplained numeric mismatch.** The primary and independent
> dense sieves report **different** normals totals: **10,694,457,224** vs
> **10,694,457,231**, differing by **7**. Their synthesis verifier asserts
> equality of the four classification histograms but **deliberately does not
> compare the normals totals** (it sums them into two separate fields). The
> note does not explain the gap. Plausibly a core-order enumeration
> convention — but it is unexplained and silently tolerated by their own
> verifier. **ASK.**

**FLAG — definitional.** "509 core rows" and "fourteen principal locator
values" are used in §3 against a 1,023-point domain and 16 locators, without
definition. I recovered the 14+2 split from the fixture file; the note never
states it.

### (d) Impact on our lanes

1. Cite this fixture as **adjacent but distinct** from our t64 / depth32 M31
   records; do not merge.
2. Do **not** price it against `rate_half_list_adjacent_crossing` (TARGET)
   without the locator-to-codeword map our own route fence proved absent.
3. Do **not** read it as contradicting our 6-dim / 67,449-split route cut —
   different regime.

---

## 5. Collision / adoption table

| their claim | our nearest record | relation | verdict |
|---|---|---|---|
| #1145 envelope `(20,22,24,27)` at `F_331` | — (nothing) | no overlap | **new to us**; adopt only as cited fixture |
| #1145 non-vacuity `tau >= 6` | — | no overlap | **new**, VERIFIED |
| #1145 250/2 dichotomy, six-fibre finiteness | — | no overlap | **new**, hand-VERIFIED |
| #1146 `S_3(P|Q^2) <= 10` sharp | `l1_program_frontier` Thm J (PROVED), uniform in `n,k,q` | possible partial domination — **open check** | terminal VERIFIED; reduction UNREPLAYED |
| #1147 `sum C_r = 32 T_sm`, `sum K = 8 T_sm` | — | no overlap | **new**, VERIFIED |
| #1147 `9 sum C_r = 288 T_sm` | — | **not independent** (= 9x the first) | **overclaim**, flag |
| #1147 pointwise `K(d,e) <= 4` counterexample | **nothing of ours assumes it** (0 hits / 1770 nodes) | zero exposure; *confirms* our own pointwise→aggregate precedent | **VERIFIED by my replay** |
| #1147 `T_sm` | `SOL_TARGET_4` `T_4(q,N) <= C N^3` | **same conjecture**, different currency (bridge proved exactly) | **★ adopt the bridge** |
| #1148 hull rigidity (locator side) | `rate_half_list_chamber_affine_rank_bridge` (PROVED fence) | **our fence dominates its applicability** | route cuts VERIFIED; sieves UNREPLAYED |
| #1148 sixteen degree-479 M31 locators | `l1_m31_t64_...` (7), `l1_m31_depth32_...` (1,237) | same family, **different fixture** | citation duty, no duplication |
| #1148 Schur non-GRS cut | `..._non_grs_route_fence` (PROVED) | their direction is the safe one | survives our fence |
| #1148 "low-dim ⇒ few split" | `l1_m31_fixed_support_divisor_direction_cap_route_cut` (PROVED, 6-dim / 67,449 split) | different regime, **no contradiction**; but blocks any lift | fixture-specific only |

---

## 6. Action list for our lanes

**Paper-D / SOL_TARGET_4 (highest priority)**

1. **Reprice SOL_TARGET_4.** Our `T_4(q,N) <= C N^3` has **no `q`-vs-`N`
   hypothesis** and my ladder shows `T_4/N^3` reaching **2.87** at `(128,257)`
   with implied exponent `N^5.4-5.8` along two fixed-small-index families.
   Either add an index hypothesis or expect falsification.
2. **Run the decisive row** `N = 256, q = 769` (index 3), `C(256,4) = 174.8M` —
   needs C++ or a large-memory box. This settles item 1.
3. **Adopt the bridge** `T_4^{smooth,ordered} = 2n T_sm` (free orbits) into the
   SOL_TARGET_4 note, with the exact `(32,97)` reconciliation. Their aggregate
   energy inequality, if it ever closes, is a **direct input** to our target.
4. Ask maelcar for the `max C_r = 5789` witness (unreplayed) and note publicly
   that `288T` is `9x` the first identity.

**L1**

5. Task #9 (`X1 <-> L1` note): record that `ell = 11` exact-five is **not our
   lane** and that `dli_wcl_ell4_weight11...` must not be scored as coverage.
6. Run the **Theorem J check**: translate #1146's row to `(n,k,s)`, test
   `s^2 > n(k-1)`. Determines whether we partially dominate.
7. If we ever cite #1146: say **"for the two parity supports"**, never
   "for ell=11 exact-five". Their own residual obligation for the other 250 is
   `S6 <= 21`, not `<= 20`.

**LIST / M31**

8. Before any M31 move, cite #1148 as adjacent-distinct; do **not** price it
   without the locator-to-codeword map (`rate_half_list_chamber_affine_rank_bridge`).
9. Ask about the **7-normal discrepancy** between primary and independent
   dense sieves.
10. Registry: maelcar's four PRs added; lane tags L1 (x2), Paper-D, LIST/M31.

---

## 7. Flags raised (not guessed)

| # | PR | severity | flag |
|---|---|---|---|
| F1 | 1147 | MEDIUM | `9 sum C_r = 288 T_sm` presented as a third exact currency; it is `9x` the first, and its verifier assertion is vacuous given the first |
| F2 | 1147 | MEDIUM | the headline counterexample is in **no JSON certificate and no Python auditor** — C++/prose only (I replayed it independently; it holds) |
| F3 | 1147 | LOW | note writes `d != e` under the sum; the auditor never enforces it |
| F4 | 1148 | MEDIUM | primary vs independent dense sieves differ by **7** normals (10,694,457,224 vs ...231), unexplained; their synthesis silently does not compare them |
| F5 | 1148 | MEDIUM | "509 core rows", "fourteen principal locator values" undefined against a 1,023-point domain / 16 locators |
| F6 | 1148 | LOW | the 65,535-support synthesis is **aggregation**; the entire mathematical load (10.69e9 normals) is unreplayed C++ |
| F7 | 1145 | MEDIUM | envelope `(20,22,24,27)` is a per-`h` maximum over the family — increments increase, so no single state attains it |
| F8 | 1145 | LOW | `"p = 199: S_6 = 20, profile 6^1 2^8 1^9"` conflates the census envelope with the max-**fibre** state (that profile has `S_6 = 16`) |
| F9 | 1146 | MEDIUM | headline "S_6 <= 20 sharp" holds for **2 of 252** supports; their own residual obligation for the other 250 is `S6 <= 21` |
| F10 | ours | **HIGH** | **SOL_TARGET_4 has no `q`-vs-`N` hypothesis and looks false at bounded index** — surfaced by auditing their row |
| F11 | brief | — | `kb_*` = KoalaBear, not kernel-basis; no `kb_*M31*` node exists; the brief's premise had no referent |

---

## 8. Overall verdicts

| PR | lane | verdict | one line |
|---|---|---|---|
| **#1145** | L1 | **VERIFIED** (non-vacuity) / **PLAUSIBLE-UNREPLAYED** (census) | genuinely new to us; census unreplayed but passes a strong enumeration-law integrity check I derived independently |
| **#1146** | L1 | **VERIFIED** (terminal) / **PLAUSIBLE-UNREPLAYED** (reduction) | sharp constant on the extremal supports; scope is narrower than the title suggests |
| **#1147** | Paper-D | **VERIFIED** | strongest package; zero exposure for us; one overclaim; **and it exposed a live risk to our own SOL_TARGET_4** |
| **#1148** | LIST/M31 | **VERIFIED** (route cuts) / **UNREPLAYED** (sieves) | high hygiene, fixture-specific, and our own PROVED route fence blocks it from pricing any chamber |

No claim above is adopted into `dag.json`. Every unreplayed item is labelled.
