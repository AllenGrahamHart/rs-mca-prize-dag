The harness refused the `REPORT.md` write (subagent policy), so per the brief I return the full report text verbatim below. The directory contains 19 files and no `REPORT.md`.

**Headline for relay:** `(FR)` is **true and proved in one line** — but only once the quantifier over `W` is fixed (`W` = a *minimising pair union*), and it does **not** close residual (ii): the factor goes `9/4 -> 7/4` over the band (`9/4 -> 9/8` at the banked evaluation point `a=7m-1`), with the argmax moving to `a=(20m-2)/3` and a missing factor of exactly `8/5`. The wave-57 fence's own set system satisfies `(FR)` at every one of its 32896 canonical joint supports (`max = 115 <= 2m = 128`). Separately, realizable `m=3,4` pencils violate the *arbitrary-`W`* `(FR)` in the non-minimum-weight stratum.

---

# REPORT — rh_fr_algebraic (round 32)

## VERDICT (first)

**`(FR)` is TRUE and PROVED — in one line, with no algebra at all — but only after the quantifier over `W` is fixed; and it does NOT close residual (ii).** Three results, in decreasing order of how much they move the board:

1. **`(FR)` is a theorem at the CANONICAL joint support.** If `W* = S_g u S_h` is the union of a pair *minimising* the union, `a* = |W*|`, then for every supported slope `gamma`, `|S_gamma ^ W*| <= 4rho - 2a* - 2o_gamma - o_g - o_h`, which at `a* = 7m-1` is `<= 2m-2 <= 2m`. Proof: `|S_gamma ^ S_g| = u_gamma+u_g-|S_gamma u S_g| <= u_gamma+u_g-a*`, twice. **This uses only cardinalities** — no `f_gamma`, no pencil, no apolar equation. The wave-57 fence is not an obstruction to it; the fence's `W` is an arbitrary `a`-set, and the `(AO1)` prover is entitled to choose `W` (`notes/pilots_20260810/apolar_origin/PREREG.md:163`: *"`W` = a joint support (e.g. `S_gamma u S_gamma'`)"*).
2. **`(FR)` for an ARBITRARY joint support is FALSE for realizable pencils, already at `m=3`** — 8/64 realizable `m=3` pencils and 17-18/72 realizable `m=4` pencils carry a **non-minimum-weight** (`j>=1`) type-2 slope with `|S_gamma ^ W| > 2m` at a legitimate joint support `W = S_1 u S_2`, exceeding `3m-3` as well. Two fields each. The fence's `m=64` combinatorial witness therefore has realizable analogues eleven scales below it — **but with `T=3`, not `T=rho+2`; the `(SAT3)` hypothesis is NOT exercised and this is not a refutation of `(FR)` as the brief states it.**
3. **The residual (ii) factor improves `9/4 -> 7/4`, not `9/4 -> 1`.** At the banked evaluation point `a = 7m-1` the factor halves exactly, `2.250000 -> 1.125000` (`AO1: 1236950581233 -> 618475290624` at `m = 2^37`). But the argmax over the open band **moves** from `a = 7m-1` to `a = (20m-2)/3`, where `(FR)` buys nothing, and the factor there is `7/4`. The open `w*` band `(16m/3, 7m-1]` is **unchanged to the integer** (`a <= 339` closes at `m=64`, both before and after). **Neither budget moves; residual (ii) stays open.**

The exact remaining need, named to the constant: closure requires `|S_gamma ^ W| <= a/4` (`= rho - (floor((N-a)e/(T-T_1))+1)` exactly); what is proved is `min(a-(4m+2), 4rho-2a)`; at the argmax those are `5m/3` needed against `8m/3` proved — **a missing factor of exactly `8/5`**, converged to `1.6000` at `m = 2^20` and `m = 2^37` (`d4_verdict_results.txt`).

---

## MISSES FIRST

1. **I DID NOT ANSWER D1 AS ASKED.** The brief asked whether the `m=64` fence system is realizable as an actual pencil configuration. **I do not know, and I have neither a realization nor a refutation.** My blind prior `P(realizable) = 0.06` is **UNRESOLVED**, not scored. What I did instead was show the question does not matter for the route — a different result, and I am not going to dress a pivot up as an answer.

2. **I ALMOST SHIPPED A FALSE ROUTE-FENCE, AND CAUGHT IT MYSELF.** Mid-session I derived what looked like a first-order negative: since `(SAT4)` is an *identity* under `(SAT3)` (`background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:50-53`: *"Under `(SAT3)` the exact deficit identity"*), the spend budget `sum_(type-2) p_gamma = (N-a)e - def_out` is tight to within `1+O <= m`, so `min p <= mean p` and therefore — I concluded — *no* per-slope floor can ever refute `T=rho+2` by counting, making the whole `(FR)` program vacuous. **That conclusion is WRONG.** `min <= mean` holds *in the hypothetical configuration*; a proven floor that *exceeds* the mean is exactly what refutes it. I caught the error by testing it against the banked `a <= 16m/3` closure, which the false claim contradicted. The surviving true content is the much weaker and already-known statement that the floor must beat the **mean** spend `(N-a)e/T_2 ~ 9m/4`, not the MDS spend `R+1-a = m+2` (`d2_budget_results.txt` section 5). Had I not checked, I would have banked a fence that kills a live route.

3. **My registered mechanism was RIGHT AND UNNECESSARY.** PREREG R2 registered `(FIB)` + `(OV+)` (the fibre partition of `W` by the `2`-space `V = <c_0,c_1>`, plus the observation that `(v_gamma, z_g)` is a representation pair for any `g != gamma`) and predicted the corollary *"`T_1 = 2` => `|S_gamma ^ W| <= 2m-2`"*. That corollary is exactly what happens — but the `T_1 = 2` hypothesis, which I registered as **the residual wall**, is **free**: it holds automatically when `W` is chosen as a pair union, because `g` and `h` are then type-1 by construction. The entire fibre apparatus is dispensable for the ledger. I registered an algebraic mechanism for a combinatorial fact.

4. **P4.1 is a PARTIAL MISS at `m=2` for an arithmetic reason I should have seen at registration time.** I registered that the planted-`W` maximum would *exceed* `2m` and *reach* `4m-4`. It reaches `4m-4` exactly at all three scales and both fields (`4, 8, 12`) — but at `m=2`, `4m-4 = 4 = 2m`, so exceeding is arithmetically impossible there (`0/60` at both fields). The window had no discriminating power at the smallest scale and I should have registered `m>=3`.

5. **THE CENSUS CANNOT TOUCH `(SAT3)` — carried forward from round 31 and still true.** Every one of the 420 pencils has `T = 3`; `(SAT3)` needs `T = rho+2` (`9, 13, 17` at `m=2,3,4`; `2^39+1` officially). Quoting round 31 verbatim: *"The census has zero power over the failure configuration ... Nothing measured this round bears on the extremal configuration"* (`notes/pilots_20260810/rh_type2_stratum/REPORT.md:219`). My finding 2 inherits this in full: it refutes the **`W`-quantifier**, not `(FR)` under `(SAT3)`.

6. **`(NEWCAP)` is `(SAT3)`-conditional and so is every ledger row here.** *"(NEWCAP) is CONDITIONAL on `(SAT3)` (`T = rho+2`). It is not a theorem about arbitrary strict-`A=3` pencils"* (`rh_type2_stratum/REPORT.md:54`). My `a* <= 7m-1` re-derivation inherits it. My `(FR)` theorem itself does **not** (it needs no saturation at all) — but every use of it inside the ledger does.

7. **The `(EQ)` converse gap carries forward untouched.** *"The converse needs `n_0 = n_gamma` ... which I did **not** prove ... that is a **sampled** check, not a proof"* (`rh_type2_stratum/REPORT.md:44`). I used `j = wt(kappa)-(R+1)` directly from the decoder and never relied on the converse, so I neither closed nor weakened it.

8. **My first `a`-sweep was WRONG at small `a` and I shipped a corrected rerun.** I fixed the `(AO1)` first term at `2`, which is valid only for `a >= 6m-1`; below that the banked `min(m+1, floor(a/(a-rho)), floor((am+O)/rho))` is larger. The bad pass printed `ratio 0.7578` at `a = 4m+2` (true value `1.0000`) and a closure threshold of `341` (true `339`). Both scripts were patched and rerun; the headline numbers (`7/4` at `20m/3`, `9/8` at `7m-1`) sit at `a >= 6m-1` and were unaffected. The stale numbers do not appear in any results file.

9. **`(FR)` at `2m` was never going to close residual (ii), and the brief's framing said it would.** *"Target: `<= 2m + O(1)`, which closes residual (ii) to a factor `~1`"* (the brief). The arithmetic: at `a = 7m-1`, `X <= 2m` gives `p >= 2m-1` and `CAP ~ 4.5m` against `rho+1 = 4m` — a factor `9/8`, not `~1`; and the argmax moves off `7m-1` entirely. This is a correction to the mandate, not a result of mine.

10. **One ramguard FAILURE.** Invocation 11 (`d4_verdict.py`, `tiny`) was killed at the 60 s wall — I had written an `O(3m)` sweep and run it at `m = 2^37`. Rewritten with an analytic candidate set (plus a full-sweep control for `m <= 1024`) and rerun. Reported, not hidden.

---

## CATCH-24A — own-repo subtraction, run BEFORE the novelty claims

| object | in-repo prior | verdict |
|---|---|---|
| `W` may be taken to be `S_gamma u S_gamma'` | `notes/pilots_20260810/apolar_origin/PREREG.md:163` *"`W` = a joint support (e.g. `S_gamma u S_gamma'`), `a=\|W\|`"* | **BANKED — and it is the whole of my theorem's hypothesis.** My contribution is *using the freedom*, i.e. noticing that the `(FR)` quantifier over `W` was never fixed. |
| `\|S_gamma ^ S_gamma'\| <= 2rho - w*` (pairwise) | `rh_type2_stratum/REPORT.md:188` *"`(OV)` gives exactly this statement pairwise, against one other locator set at a time (`\|S_gamma ^ S_gamma'\| <= 2rho - w* ~ m`). What is missing is the same statement **against all of `W` at once**"* | **BANKED.** The step "apply it twice, to a `W` that is a union of two locator sets" is the only new move. |
| `(OV)` every-pair quantifier | `rh_type2_stratum/REPORT.md:15`; replayed to primary text at `critical/nodes/rate_half_band_crossing_location/statement.md:563-566` | banked |
| `a* <= 7m-1` (`(NEWCAP)`) | `critical/nodes/rate_half_band_crossing_location/statement.md:567-573` | **BANKED.** I re-derived it exactly for `m in {2,3,4,8,64,1024}` and all `O in [0,m-1]` (`d2_budget_results.txt` section 1) and observed that it bounds the **mean** pair union, hence also the **minimum** pair union — which is what my `W*` needs. That reading is a re-use, not a new bound. |
| `n_gamma`, `z_gamma = c_0+gamma c_1` | `apolar_origin/PREREG.md:165-166` | banked |
| the fibre partition `sum_(g in P^1) n_g = a` and `supp(z_g) = W \ F_g` | greps over `critical/`, `background/`, `notes/` for `partition of W`, `fibre`, `sum n_gamma` returned **no prior** in this lane; the nearest is `critical/nodes/rate_half_band_crossing_location/statement.md:497` (*"`G = S_1 u S_2` and the complements are pairwise-disjoint fibres of a degree-`k` map"*), which is T4's fibre argument in the `{P_S}` collineation picture, a different object | claimed as new **in this lane**, and immediately demoted to a footnote by MISS 3 |
| `(C2)` bound `\|S_gamma ^ W\| <= a-n_gamma-(R-r+1)` | `apolar_origin/PREREG.md:181-186` | banked. **New observation:** at `a = 7m-1` this reads exactly `3m-3-n_gamma`, so the fence's `max = 3m-3` **saturates the banked type-2 bound to the unit**. The fence is the extremal object of `(C2)`, not an anomaly beyond it. |
| the parameter-degree rigidity `deg_Z Q_Z(x) = m`, roots distinct and in `Z` | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:62-69` | **BANKED** — this is the `P_x(Z) = lambda_x prod_(gamma in A_x)(Z-gamma)(Z-mu(x))` rigidity I re-derived in D2; I claim only the `(Z-mu(x))` factor (the `W`-side root) on top of it |
| `16m/3` closure ceiling, `a_max/m -> 16/3` | `notes/pilots_20260810/apolar_origin/REPORT.md:61`; `d6_stratum.py:63-64` | banked; my sweep reproduces `a_max(8) = 42` and `a_max(64) = 339` |
| the `9/4` and the `1236950581231` cap | `critical/nodes/rate_half_band_crossing_location/statement.md:574-580` | banked; reproduced digit-for-digit |
| "`9/4` may be the CEILING of the combinatorial route; the next instrument is algebraic" | `critical/nodes/rate_half_band_crossing_location/statement.md:589-596`; `rh_type2_stratum/REPORT.md:188` | **REFUTED IN PART.** The combinatorial route was not at its ceiling: a purely cardinality-level move takes `9/4` to `7/4` (and to `9/8` at the banked evaluation point). The caution was reasonable and it was wrong. |
| fence scope line *"Any positive `(FR)` theorem must use information absent from the set-system axioms, such as the generalized locator polynomials `f_gamma`, the common syndrome pencil, or the apolar Hankel equations"* | `background/nodes/rate_half_type2_fr_incidence_only_route_fence/statement.md:40-43` | **CORRECT IN LETTER, MISLEADING IN EMPHASIS.** The needed extra information is indeed absent from the fence's axiom list — but it is *"`W` is the union of two of the blocks"*, a **set-system axiom**, not `f_gamma`/pencil/apolar data. Flagged for the node's audit; see D1. |

---

## D1 — EXCLUDING THE FENCE SYSTEM

**Answer: I cannot exclude it, and it does not need to be excluded.**

**Independent replay first** (`d1_fence.py`, my own coset/bitmask code, not the node's `verify.py`): rebuilding the quartic-difference-family blocks from `proof.md:3-53` over `F_257` reproduces every banked number — `257` blocks of size `rho=255`; `sum_x(m-d_x) = 1`; `max_(g!=h)|S_g ^ S_h| = 63 = m-1`; `min_(g!=h)|S_g u S_h| = 447 = a`; the `SHA-256`-checked mask has `|W| = 447`, `min_gamma|S_gamma \ W| = 66 = m+2`, `max_gamma|S_gamma ^ W| = 189 = 3m-3` at the unique maximiser `gamma = 0` (`d1_fence_results.txt`).

**Three structural facts about the fence's `W` that the node does not state:**

- **No block lies inside `W`** (`max|S ^ W| = 189 < 255`), so the fence's `W` has `T_1 = 0`: *not one* of its `257` slopes is type-1 for it.
- **`W` is not any pair union** — checked against all `C(257,2) = 32896` unions: `False`.
- The fence saturates the banked `(C2)` bound exactly: `a - n_gamma - (R-r+1) = 447 - 0 - 258 = 189`. The fence is the extremal object of `(C2)`, and its `min|S \ W| = m+2` is exactly the MDS floor `R+1-a`. Nothing in it exceeds the banked layer; it *attains* it.

**THE D1 CORE — the same set system at a canonical `W`.** For every one of the `32896` pair unions `W* = S_g u S_h` of the fence's own blocks,

```text
max_gamma |S_gamma ^ (S_g u S_h)| = 115   (attained at the pair (0,1)),
115 <= 2(m-1) = 126 <= 2m = 128 << 3m-3 = 189.
```

`115` is the maximum over **all** pairs, exhaustively — not a sample. So the fence's `(FR)` violation is entirely an artifact of the `W`-quantifier: its `189` lives at an `a`-set that no pair of its own blocks spans, while at every canonical choice the same system obeys `(FR)` with margin `13`.

**Consequence for the node.** The fence's theorem is true as stated and its scope line is true in letter; but its suggested moral — that a positive `(FR)` needs `f_gamma`, the syndrome pencil, or apolarity (`statement.md:40-43`) — is **not** what the missing axiom turned out to be. Recommended (coordinator-gated, I applied nothing): add to the node an addendum recording that the axiom list omits *"`W = S_g u S_h` for two of the blocks"*, that adding it makes `|S_gamma ^ W| <= 2(2rho-a)` immediate, and that the fence's own system then satisfies `(FR)` with `max = 115`.

**What I did NOT do:** I did not attempt a Hankel realization of the `m=64` system and I make no claim about its realizability in either direction. The D1 question as posed is **still open** and is now, in my judgement, **not worth answering** — see D4.

---

## D2 — THE `(FR)` THEOREM AND THE EXACT LEDGER

### D2.1 The theorem (elementary; needs no saturation hypothesis)

> **Theorem (FR-canonical).** Let a strict-`A=3` pencil have supported slopes with locator sets `S_gamma`, `|S_gamma| = u_gamma = rho-o_gamma`. Put `a* = min_(g != h) |S_g u S_h|` and fix a minimising pair `(g,h)`; let `W* = S_g u S_h`, so `|W*| = a*` and `W*` is a joint support in the sense of `apolar_origin/PREREG.md:163`. Then for every supported `gamma !in {g,h}`
>
> ```text
> |S_gamma ^ W*| <= (u_gamma+u_g-a*) + (u_gamma+u_h-a*)
>                 = 4rho - 2a* - 2o_gamma - o_g - o_h .
> ```
>
> In particular at `a* = 7m-1` and `O = 0`: **`|S_gamma ^ W*| <= 2m-2`**, and `p_gamma = |S_gamma \ W*| >= 2a* - 3rho >= 2m+1`.
>
> *Proof.* `|S_gamma ^ S_g| = u_gamma + u_g - |S_gamma u S_g|` and `|S_gamma u S_g| >= a*` by minimality of `a*`; same for `h`; and `S_gamma ^ W* = (S_gamma ^ S_g) u (S_gamma ^ S_h)`. QED.

Two hypotheses matter and I state them loudly: **(a) `W` is a pair union** — without it the statement is false, and false *realizably* (D3); **(b) `a*` is the minimum over pairs** — the bound degrades as `4rho-2a*`, so it is worth `2m` only near the top of the `w*` band.

`a* <= 7m-1` is banked: `(NEWCAP)` bounds the **mean** pair union, hence the minimum (`critical/nodes/rate_half_band_crossing_location/statement.md:567-573`); re-derived exactly here for `m in {2,3,4,8,64,1024}` over all `O in [0,m-1]`, always `= 7m-1` and always attained at `O=0` (`d2_budget_results.txt` section 1).

### D2.2 Why the case analysis over `W` collapses

The prover has two admissible `W`s: the true minimum joint support (`|W| = w*`, floor `R+1-w*` from `(C2)`) and `W*` (`|W| = a* >= w*`, floor `max(R+1-a*, 2a*-3rho)`). `CAP(a) = floor((N-a)e/p)` is increasing in `a`, so the first option only improves as `w*` falls; the adversary therefore sets `w* = a*` and the whole problem is the **one-parameter sweep in `a = w* = a*`**. No fibre theory, no `T_1` case split, nothing conditional. (If `w* < a*` then the minimum joint support is *not* a pair union, and one can show it then has `T_1 <= 1`; that branch is real but the adversary never chooses it.)

### D2.3 The exact ledger (`d2_budget_results.txt`, `d4_verdict_results.txt`)

At `m = 2^37`, exact integers:

| `a` | | banked | sharpened |
|---|---|---|---|
| `7m-1 = 962072674303` | `X <=` | `412316860413` | `274877906942 = 2m-2` |
| | `p >=` | `137438953474 = m+2` | `274877906945 = 2m+1` |
| | `AO1` | `1236950581233` | `618475290624` |
| | factor vs `rho+1 = 2^39` | `2.250000` | **`1.125000`** |
| `(20m-2)/3 = 916259689812` | `X <=` | `366503875922` | `366503875922` (unchanged) |
| | `AO1` | `962072674294` | `962072674294` |
| | factor | `1.750000` | **`1.750000`** |

**Worst case over the whole open band: `9/4 -> 7/4`.** The argmax moves from the top of the band to the crossing `a = (20m-2)/3` where the `(C2)` bound `a-(4m+2)` and the `(FR)` bound `4rho-2a` are equal at `(8m-8)/3`. The closure threshold is `a <= 339` at `m=64` **before and after** — `(FR)` does not widen the closed sub-stratum by one integer, it only lowers the factor inside the open one.

### D2.4 What the apolar/algebraic layer actually says (the honest dictionary)

I did derive the algebraic objects the brief asked for; they did not beat the one-line bound, and I report them as a dictionary rather than as a result.

- **`(C2)` is a degree count.** The shortened apolarity code `K'|_W` (`K' = [16m, 12m-1, 4m+2]` MDS, `apolar_origin/PREREG.md:156-157`) is `{(h(x)/sigma'_W(x))_(x in W) : deg h <= a-(R-r+2)}`, so `psi_gamma = z_gamma . Q_gamma|_W` is a polynomial `h_gamma` of degree `<= a-(4m+2)` whose roots in `W` are exactly `F_gamma u (S_gamma ^ W)`. **`(C2)` = "a nonzero polynomial has at most its degree many roots",** and `(FR)` at `2m` = "`h_gamma` has at most `~2m` roots although its degree allows `3m-3`". At `a = 7m-1` the mean weight of `psi_gamma` over the `T` slopes is `~21m^2/(4m+1) ~ 5.25m` against the `5m-1` that `(FR)` needs — so unlike the spend count, this instrument is **not** excluded by `min <= mean`; it has `~5%` headroom. That is where I would send the next algebraic attack.
- **The bivariate rigidity.** With `Psi(Z) = ((c_(0,x)+Z c_(1,x)) Q(Z;x))_x in K'[Z]`, `deg_Z <= e+1` (`(C3)`, `apolar_origin/PREREG.md:187-190`) and the banked saturation rigidity (`...saturation_rigidity/statement.md:62-69`: at the `>= 15N/16` saturated points `Q_Z(x)` has parameter degree exactly `m` with distinct roots in `Z`), each coordinate is **forced**: `P_x(Z) = lambda_x prod_(gamma in A_x)(Z-gamma) . (Z-mu(x))` for `x in W`, where `A_x = {gamma : x in S_gamma}` (`|A_x| = d_x`) and `mu(x)` is the fibre slope. The realizability system is then `(m+2)(4m+1)` linear conditions on the `a = 7m-1` unknowns `lambda_x` — overdetermined by a factor `~O(m)`. **I did not solve or exploit it**; I record it as the precise shape of the remaining algebra.
- **`(FIB)`/`(OV+)`** (PREREG R2): `W` is partitioned by `mu: W -> P^1`, `sum_(g in P^1) n_g = a`, `supp(z_g) = W \ F_g`; and for every supported `gamma` and every `g != gamma`, `(v_gamma, z_g)` is a `D`-representation of the syndrome pair, so `w* <= |S_gamma u supp(z_g)|`, i.e. **`n_g - |S_gamma ^ F_g| <= p_gamma`**. Verified `5049 / 5049` with zero violations across six census cells. It yields `|S_gamma ^ W| <= 2rho - n_((1)) - n_((2))`, which reproduces `2m-2` when the two largest fibres carry `>= 6m-2` of the `a = 7m-1` mass — automatic when `T_1 = 2`, and vacuous otherwise. **Superseded by D2.1** (MISS 3).

---

## D3 — THE SMALL-SCALE REALIZABILITY CENSUS

Machinery: `d3_frcensus.py`, whose **lines 1-345 are a byte-identical scratch copy** of `notes/pilots_20260810/rh_type2_stratum/d3_census.py` (verified by `diff`; Berlekamp-Massey + Vandermonde + nullspace + `analyse`), with a new driver. Round 31's MISS 3 was that it carried *no replay-identity evidence*; this round the decoder core is literally the same bytes and reproduces round 31's structural numbers (`T = 3` in every pencil, `w*` minimality violations `0`, `(C2)` violations `0`).

Construction: round-31 MODE B — plant a third slope with prescribed `p = |S_3 \ W|` at `a in {8m-2, 6m}`; then **re-run the analysis in the basis of a minimising pair** to obtain the canonical `W*` and its fibres. Six cells, `m in {2,3,4}`, two fields each (`16m | q-1`), `420` pencils.

| `m` | `q` | pencils | planted-`W` max `X` | `> 2m` | `> 3m-3` | `j>=1` only: max `X` | `> 2m` | canonical-`W*` max `X` | `(FR)` viol. |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 97 | 60 | `4` | `0/60` | `12/60` | — | — | `2` | `0` |
| 2 | 193 | 60 | `4` | `0/60` | `11/60` | — | — | `2` | `0` |
| 3 | 97 | 72 | `8` | `16/72` | `16/72` | `7` | `8/64` | `4` | `0` |
| 3 | 193 | 72 | `8` | `16/72` | `16/72` | `7` | `8/64` | `4` | `0` |
| 4 | 193 | 78 | `12` | `24/78` | `17/78` | `11` | `18/72` | `6` | `0` |
| 4 | 257 | 78 | `12` | `23/78` | `18/78` | `11` | `17/72` | `6` | `0` |

Reference values: `2m = 4,6,8`; `3m-3 = 3,6,9`; `4m-4 = 4,8,12`; `4m-5 = 3,7,11`.

**Reading, in order of importance.**

1. **The planted-`W` maximum is exactly `rho-(R+1-a) = 4m-4` at every scale and both fields**, and restricted to the mandate's stratum (`j >= 1`, non-minimum-weight) exactly `4m-5`. Both exceed `2m` for `m >= 3` and exceed `3m-3` too. **So realizable violations of the arbitrary-`W` `(FR)` exist at `m=3`, not just at the fence's `m=64`, and they are in the non-minimum-weight stratum.** Caveat, load-bearing: `T = 3`, so `(SAT3)` is untested (MISS 5).
2. **At the canonical `W*`, zero violations of anything, in every cell:** `(FIB)` `420/420`; `(OV+)` `5049/5049`; `(C2)` `420/420`; `(FR)` `420/420`. The measured canonical maxima `2, 4, 6` sit strictly below both `2m` and `3m-3`, and track the analytic envelope `min(a*-(4m+2), 2(2rho-a*))` closely — tight at both ends of the `a*` range (`a* = 2rho` forces `X = 0`, measured `0`; small `a*` forces `X = a*-(4m+2)`, measured equal at `a*=16,17,18` for `m=3`).
3. **`T_1 = 2` at the canonical `W*` in `420/420` pencils** — as predicted (P4.5), and now understood as forced rather than empirical.
4. **The measured maxima exceed the closure threshold `need_X`** in the mid-range (`m=3`, `a*=18`: measured `4`, threshold `2`; `m=4`, `a*=24`: measured `6`, threshold `4`). This is the small-scale shadow of the `8/5` gap in D4 — **but the threshold formula assumes `T = rho+2`, which these configurations violate, so this is suggestive and has ZERO probative power.**

---

## D4 — VERDICT

**Residual (ii) does not close. `(FR)` is proved, at `2m-2`, and it is not enough.** The full ledger over the band, exact integers (`d4_verdict_results.txt`):

```text
   m         worst a (old)   factor_old    worst a (new)  factor_new   a/m     X_proved     X_needed    gap
   2                    13     1.37500                12     1.25000  6.0000          2            1  2.0000
   3                    20     1.50000                19     1.33333  6.3333          5            3  1.6667
   4                    27     1.62500                26     1.43750  6.5000          8            4  2.0000
   8                    55     1.87500                52     1.50000  6.5000         18           11  1.6364
  64                   447     2.19141               426     1.72266  6.6562        168          104  1.6154
1024                  7167     2.24634              6826     1.74829  6.6660       2728         1704  1.6009
2^20               7340031     2.25000           6990506     1.75000  6.6667    2796200      1747624  1.6000
2^37         962072674303     2.25000      916259689812     1.75000  6.6667 366503875922 229064922451  1.6000
```

**The named missing ingredient, exactly.** Closure needs `|S_gamma ^ W| <= rho - (floor((N-a)e/(T-T_1)) + 1)`, i.e. `~a/4`, throughout `a in (16m/3, 7m-1]`. Proved: `min(a-(4m+2), 4rho-2a)`. The two meet at `a = (20m-2)/3` where the requirement is `5m/3` and the proof gives `8m/3`: **a factor of `8/5`, exactly, in the limit.** Equivalently, in the per-slope spend: `p >= 9m/4` needed, `p >= 4m/3` proved at the argmax.

**Falsifiers, pre-registered here.**

- **F1 (kills D2.1):** a strict-`A=3` pencil, a pair `(g,h)` minimising `|S_g u S_h| = a*`, and a supported `gamma` with `|S_gamma ^ (S_g u S_h)| > 4rho - 2a* - 2o_gamma - o_g - o_h`. Exercised `420/420` with zero hits; it is a two-line identity, so a hit means my arithmetic is wrong.
- **F2 (kills the ledger, not the theorem):** a configuration with `T = rho+2` and `a* > 7m-1`, i.e. a `(NEWCAP)` violation. **NOT EXERCISED** — the census never reaches `T > 3`. Live, inherited from round 31 (`rh_type2_stratum/REPORT.md:168`, F1 there).
- **F3 (would close residual (ii)):** a proof that `|S_gamma ^ W*| <= a*/4` on `(16m/3, 7m-1]`, or that `a* <= 16m/3 + O(1)` (which would collapse the open band into the banked closed one). Either is worth more than everything above.
- **F4 (would kill `(FR)` outright):** a realizable `T = rho+2` pencil where the minimum pair union `a*` and the minimum joint support `w*` differ, with `w* < a*` and no two large fibres. My D2.2 argument says the adversary gains nothing there; a counterexample would break the case collapse.

**Where the next instrument should go.** Not to the spend count — its budget is an identity under `(SAT4)` (`...saturation_rigidity/statement.md:50-53`) and every per-slope floor is capped by the mean `9m/4`, which is exactly the `1.0` line. The live instrument is **D2.4's degree count**: `psi_gamma` has mean weight `5.25m` against the `5m-1` that `(FR)`-at-the-threshold needs, so the max-vs-mean step there is *not* self-defeating; and the bivariate system `P_x(Z) = lambda_x prod_(A_x)(Z-gamma)(Z-mu(x))` is overdetermined by a factor `O(m)`, entirely unexploited.

---

## PREDICTIONS vs OUTCOMES

| | registered (PREREG R1/R3/R4) | outcome |
|---|---|---|
| R1 `P(fence realizable) = 0.06` | — | **UNRESOLVED, not scored** (MISS 1) |
| R1 `P(unconditional (FR)) = 0.25` | — | **RESOLVED YES** — but by cardinalities, not algebra (MISS 3) |
| R1 `P(subclass only) = 0.65` | — | resolved NO (the subclass hypothesis turned out free) |
| R1 `P((FR) shown FALSE) = 0.03` | — | **resolved YES for the arbitrary-`W` form** (D3), NO under `(SAT3)` |
| R1 `P(honest wall) = 0.10` | — | resolved NO |
| R2 mechanism `(FIB)`+`(OV+)` | the killing constraint | **RIGHT OBJECT, UNNECESSARY** — verified `5049/5049`, then superseded |
| R2 corollary `T_1=2 => X <= 2m-2` | — | **HIT exactly**, and `T_1=2` is free at `W*` |
| R2 residual "`T_1 <= 1` is the wall" | — | **DISSOLVED** by the choice of `W` (MISS 3) |
| R2 "the fence is extremal for the MDS-only bound `p >= m+2`" | — | **HIT** — and better: it saturates `(C2)`'s `3m-3` to the unit |
| R3 fence integers `2064321 / 32896 / 62.75` mean intersection | — | **HIT** (max `63 = m-1`, min union `447`, `24769` minimising pairs) |
| R3 `(TR1')` does not kill the fence (`triple union ~576 >= 513`) | — | **HIT** (not the killer) |
| R3 `P(clean unconditional non-realizability) = 0.20` | — | resolved NO |
| R3 "D1 answer: not realizable UNLESS `T_1 <= 1`" | — | **MISS in form** — the fence's `W` has `T_1 = 0`, and the right answer was that `W` is not a pair union at all |
| P4.1 planted max `> 2m`, reaches `4m-4` | `0.75` | **PARTIAL** — reaches `4m-4` exactly at `m=2,3,4` both fields; exceeds `2m` only for `m>=3` (MISS 4) |
| P4.2 `(OV+)` zero violations | `0.85` | **HIT `5049/5049`** |
| P4.3 `(FR)` zero violations at `W*` | `0.85` | **HIT `420/420`** |
| P4.4 census cannot separate `2m` from `3m-3` | `0.85` | **HIT** — canonical maxima `2,4,6` are below both; at `m=3` the two bounds coincide |
| P4.5 `T_1 = 2` in `>= 90%` | `0.5` | **HIT `420/420 = 100%`** |
| P4.6 census never reaches `T = rho+2` | `0.9` | **HIT** — `T = 3` in all `420` |

---

## ZERO-POWER DECLARATIONS

1. **The census has zero power over `(SAT3)`.** `T = 3` in `420/420` pencils; the failure configuration needs `T = rho+2`. Nothing measured here bears on it, including finding 2 (the realizable arbitrary-`W` violations) and including the `need_X` comparison in D3 reading 4.
2. **Every maximum reported from the census is a max over a sample**, never exhaustive: it can falsify a bound, never establish one. The fence numbers (`115`, `189`, `63`) are the exception — those are exhaustive over all `32896` pairs and all `257` blocks.
3. **The realizability of the `m=64` fence system is UNMEASURED in both directions.** No search was run; absence of a realization here is not evidence.
4. **Nothing here decays in `q`.** Two fields per scale agree on every structural number, but two fields do not establish `q`-uniformity, and no claim is made at `q >= 2^167`.
5. **The `8/5` gap is a statement about THIS route** (the `(AO1)` spend count with the best `W` I can choose), not about the problem. I have no evidence that `|S_gamma ^ W*| <= a*/4` is true, and none that it is false.
6. **D2.4's `5.25m` mean-weight headroom is an average**, computed from the saturation identity, not a bound; I did not exhibit a single `psi_gamma` of weight below `5m`.
7. **`m=1` remains structurally disjoint from this stratum** (`critical/nodes/rate_half_band_crossing_location/statement.md:585-588`) and was not exercised.
8. **The `(EQ)` converse and `n_0 = n_gamma` remain sampled, not proved** (`rh_type2_stratum/REPORT.md:44`); nothing here depends on them, and nothing here improves them.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, rho=4m-1, R=8m, R1=R+1, e=m, T`, `S_gamma`, `u_gamma`, `o_gamma`, `O`, `d_x`, `W`, `a`, `n_gamma`, `z_gamma`, `kappa_gamma`, `p_gamma`, `j_gamma`, `X_gamma := |S_gamma ^ W|` (the mandate's quantity); **new here:** `a* :=` min pair union, `W* :=` a minimising pair union, `mu: W -> P^1` and its fibres `F_g`, `n_g`, `|G|`; `T_1(W)`; `need_X(a) := rho - (floor((N-a)e/(T-T_1))+1)`; the residual factor `(T1cap+CAP)/(rho+1)`; `gap := X_proved/X_needed`. Registered but **not measured**: `|G|` (the fibre count) — it appears in R2's derivation but the final theorem does not use it, so I never tabulated it; declared rather than quietly dropped.

---

## COMPLIANCE

**Registrations.** PREREG R0-R7 (notation incl. the new fibre objects; the three blind priors the brief demanded; the mechanism R2 stated as a falsifiable derivation; D1 predictions R3; the six census predictions R4 with numeric windows; the carried caveats R5; the subtraction plan R6; the route order R7) were appended with the Edit tool **after reading exactly the two named anchors and before any other read, any grep, and any interpreter invocation.** No post-registration addenda.

**Compute law.** **Sixteen interpreter invocations**, every one `tools/ramguard tiny|local -- python3 ...` from the repo root with the literal `--`: `tiny` x5 (`RAMGUARD_TIMEOUT` = default, 60, 120, 60, 60, 120) and `local` x11 (`RAMGUARD_TIMEOUT=290` each: 1 fence anatomy, 6 census cells, 4 census re-runs with the `j`-split). **Ramguard status: one FAILURE, reported** — invocation 11 (`d4_verdict.py`, `tiny`) hit the 60 s wall (an `O(3m)` sweep at `m = 2^37`); rewritten with an analytic candidate set plus a full-sweep control at `m <= 1024` and rerun. **Disclosed deviations:** (i) invocation 1 (a two-line version/`bit_count` probe) ran without an explicit `RAMGUARD_TIMEOUT`, taking the profile default — the brief asks for one per use and I did not set it on that one; (ii) two `tiny` runs carried `RAMGUARD_TIMEOUT=120`, above the profile's nominal 60 s, following the round-31 precedent — both finished in seconds. No bare `python3` at any point. Stdlib only; no third-party imports, no Modal, no network, no git.

**RAM discipline.** `dag.json` **never opened** (node shards + targeted greps only); file-at-a-time reads; the fence work used `1024`-bit integer masks rather than sets of tuples; the `m = 2^37` ledgers are closed-form integer arithmetic with no `O(N)` list ever materialised (the one time I violated that in spirit — the `O(3m)` sweep — ramguard killed it, which is the guard working); the census ran as ten separately checkpointed invocations each writing its own results file.

**Quarantine.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened at any line**. The three sibling round-32 directories (`rh_farca_upper`, `rh_haboeck_seam`, `rh_residuals_close`) were **never read and never listed**: every recursive grep over `notes/` carried explicit `--exclude-dir` filters for all three, `notes/pilots_20260810/` was never `ls`-ed, and all other greps were scoped to named files or to `critical/`/`background/`. No path containing `prize-codex-` was touched (filtered on every recursive grep). **No subagents were spawned.**

**Write scope.** Every write is inside `notes/pilots_20260810/rh_fr_algebraic/`: `PREREG.md` (registrations appended), `d1_fence.py` + `d1_fence_results.txt`, `d2_budget.py` + `d2_budget_results.txt`, `d3_frcensus.py` + `d3_driver.py` (the driver fragment) + six `d3_m*_q*.txt` + four `d3b_m*_q*.txt`, `d4_verdict.py` + `d4_verdict_results.txt`. **`REPORT.md` itself was REFUSED by the harness** ("Subagents should return findings as text, not write report files"), so this report is returned verbatim as the final message per the brief's fallback clause; the directory therefore contains 19 files and no `REPORT.md`. **No** `dag/`, `nodes/`, `critical/`, `background/` or `tools/` edits; no git operations; the session scratchpad was not used. The D1 recommendation for the fence node is written here as a recommendation only — **nothing was applied** (AUDIT-AND-DRAFT).

**Banked scripts.** `rh_type2_stratum/d3_census.py` was **copied into this directory before use** and its lines 1-345 are carried **byte-identically** (`diff` clean) as the decoder core of `d3_frcensus.py`; only the driver is new. The node verifier `background/nodes/rate_half_type2_fr_incidence_only_route_fence/verify.py` was **read but never executed**; `d1_fence.py` rebuilds the block system from the proof text with my own code, and independently reproduces every banked number.

**Method discipline.** Own-repo greps (CATCH-24A) preceded every novelty claim and produced **nine live subtractions**, two of which (`W = S_gamma u S_gamma'` as an admissible joint support; the pairwise `2rho-w*` bound) are the entire content of the main theorem and are reported as banked. Two-field confirmation at every census scale. Every quantifier claim above carries a `file:line`. Every max-quantified claim carries a zero-power declaration. The session's two self-caught errors (the false vacuity fence, MISS 2; the `T_1`-term sweep bug, MISS 8) are reported as errors, in the misses section, ahead of the results.
