The harness refused the `REPORT.md` write (subagent report-file restriction). Returning the full report text verbatim, as instructed.

---

# REPORT — rh_overlap_cap (round 31)

## VERDICT (first)

**The round's target inequality is not open. It is FALSE — and it was false for a reason that is already PROVED in this repository.** The "one inequality" that round 29 named as the safe half of RH-AC — *a pairwise-overlap cap below `a^2/n` at `sigma = 2^34`* — asks for something strictly stronger than the ceiling that column-farness itself imposes, and that ceiling is **attained**. Three independent strands, in the order they should be read:

1. **OBJECT SLIP (CATCH-24C, the headline).** T5's cap constant is `k-1`, defined in the round-29 registrations as "*the MDS pairwise cap on codeword agreement*" (`notes/pilots_20260810/list_profile_bound/PREREG.md:135`). The object T3 needs bounded is `|A_lam cap A_mu|` for two CA-bad slopes of a **column-far pair** — by T1(ii) that is the joint agreement of the *received pair* with a *codeword pair*, not the agreement of two codewords. Its correct ceiling is **`a-1`**, and that is banked twice over: `(AP3)`'s `s+t-r >= 1` (`background/nodes/rate_half_far_ca_anchor_pencil_normal_form/statement.md:33-34`) and the KEY LEMMA's graded consequence (`background/nodes/xr_band_key_lemma_pencil_mass/statement.md:57-61`). At the razor `a-1 = 1,116,691,496,959` and `k-1 = 1,099,511,627,775`: **T5's constant is `2^34 = 17,179,869,184` too small.**

2. **ATTAINMENT (new, and the round's deliverable).** The ceiling is reached. **LB1**, below, constructs a column-far pair at the razor row whose CA-bad slope set is a single T1-line of exactly `r+1 = 1,082,331,758,593` slopes, **every pairwise overlap exactly `a-1`**, with a unique witness per slope. Existence is by a counting argument with margin `2,181,843,386,113` in `log2` at the razor slice and `670,014,898,009` at the bottom of the widened quantifier `q > 2^167` (`d4_lb1.py`). The same object is verified **exhaustively** at the round-29 validation cell and by sampling at six more cells over three scales.

3. **SELF-DEFEAT.** `a-1 > a^2/n` for **every** `2 <= a <= n-2` (exact integer test: the largest `a` with `a^2-na+n < 0` is `n-2`, `d4_lb1.py`). So no cap below `a^2/n` exists at **any** agreement in the open bracket — the route is dead on the whole bracket `[k+2^34, 3n/4)`, not merely at `sigma = 2^34`.

**What replaces it, and it is worth more than the dead route:**

> **LB1 (unconditional lower bound).** For the razor row and every `a` in the open bracket, `B_ca^far(a) >= n-a+1 = r+1`.

Consequences, all exact: the banked upper bound `T <= r+1` (`background/nodes/rate_half_ca_hankel_minimal_index_budget/statement.md:55-61`, domain `r <= 2^39-2`) is **TIGHT — `B_ca^far(n-r) = r+1` exactly throughout its proved domain**; at `a = 3n/4`, LB1 gives `>= 2^39+1 = 549,755,813,889`, matching the D4-precision-fix budget `B_ca^far(3n/4) <= 2^39+1` (`critical/nodes/rate_half_band_closure/statement.md:484`) **exactly**, so **the residual budget `2^39` is unattainable at `a = 3n/4`** and the "one slope past the provable incidence limit" is a real slope, not proof slack; and at `sigma = 2^34`, `B_ca^far(k+2^34) >= 1,082,331,758,593 = 2^39.9773`, leaving **88.02 bits** to the `2^128` budget. The campaign had **no** lower bound on `B_ca^far` at the safe index before this.

**Neither half of RH-AC closes. Status unchanged.** Three named residuals below.

---

## MISSES FIRST

1. **PR-7 MISS, and it is the same slip I audit round 29 for.** I registered that the refutation construction would succeed at every cell with `GAP_FISHER = (k-1) - a^2/n > 0` and **fail at (8,4,5)**. It **succeeds at (8,4,5)** — 5,111,260 witnesses out of 6,232,100 configurations (`d2_maxcore_results.txt:5-13`). My registration used `GAP_ALG = (k-1) - a^2/n`; the operative gap is `GAP_FAR = (a-1) - a^2/n = +7/8 > 0` there. I registered the wrong cap in exactly the way I then caught round 29 registering it. Disclosed as my own error, found by my own exact table.
2. **R3(C) is BACKWARDS.** I registered "big cores force SHORT lines". `T1(iv)`'s bound `(n-e)/(a-e)` is **monotone increasing** in `e` (derivative `(n-a)/(a-e)^2 > 0`). The numeric sub-claim is right (`m_P <= 1 + n/a = 193/65`, floor `2`, at `e = a^2/n` exactly — PR-4 HIT) but the qualitative reading is wrong: bigger cores permit **longer** lines, up to `n-a+1`. LB1 is precisely that end of the range. My registered dichotomy engine does not exist.
3. **PR-11 MISS (partial).** I predicted **0** node files consuming T3/T5. Correct for `node.json` shards (**0**, grep below) but wrong for statement text: T1-T5 are banked verbatim in a *critical* node, `critical/nodes/rate_half_band_crossing_location/statement.md:351-378`, as the round-29 addendum. The dead route is therefore **already in a critical node's statement**, which raises the stakes of this correction from "a pilot report is wrong" to "a critical node names a false object as its next step".
4. **PR-10 MISS (partial).** Predicted 0 nodes stating the `a^2/n` cap as a target — same miss as (3): `statement.md:370-374` states it as *"THE NAMED NEXT OBJECT"*. The other half (the MDS-Johnson threshold is banked) HIT.
5. **My headline is a corollary of a PROVED node, not a discovery.** CATCH-24A fires hard: `xr_band_key_lemma_pencil_mass` (PROVED) already says "*distinct pencil members share a common agreement `a`-set iff a joint-explanation event of size `a` exists there*" (`statement.md:57-58`) — i.e. for a column-far pair the pairwise overlap is `<= a-1`. **The cap I say T5 got wrong was already banked correctly elsewhere in the repo.** My additive content is the audit, the attainment (LB1), and the consequences — not the cap.
6. **My R3(B) is banked too.** The observation that the *mean* pairwise overlap of `M` `a`-subsets is `a^2/n`, hence a cap below it is a strictly stronger statement than the list bound it serves, is inside the Johnson anchor's own proof: `background/nodes/rate_half_list_integer_johnson_safe_anchor/proof.md:62-73` — "*expected total pair intersection is binom(ell,2) a^2/n ... This rules out every agreement below `a_0` for every budget.*" Claimed as a re-derivation.
7. **The `(16,8,9,17)` cell returned a NEGATIVE and I have ZERO POWER over it.** 0 hits in 9,353 samples (`d3_ladder_results.txt`). A sampled negative is not a non-existence proof, and I do not report it as one. `(16,8,10)` was **NOT MEASURED** (wall budget).
8. **PART A NOT MEASURED.** I planned to replay round-29's 21,832-configuration census with a skip counter for the T3 guard (`notes/pilots_20260810/list_profile_bound/d2_sunflower.py:181`, `if theta * n < a * a:` — when the hypothesis fails the entire T3 test is silently skipped). It was dropped for wall budget. What I state below about that census being largely vacuous is a **structural inference from PART B, not a measurement**, and I flag it as such.
9. **LB1's razor step is a proof I wrote, not a machine-checked one.** Its *arithmetic* is machine-checked (`d4_lb1.py`); its combinatorics are verified exhaustively only at `(8,4,17)` and by sampling elsewhere. If the counting argument has a hole, the razor claim falls and only the scaled-cell refutations survive — which would still kill the route as a *mechanism*, but not at the razor row.
10. **Registered but NOT MEASURED:** `RATIO_CAP` monotonicity along `s=1` beyond `k=6` (PR-8's `k=8` entry rests on the arithmetic table, not on a measured witness, because `(16,8,9)` returned no witness).

---

## D4 — CONSUMER CHECK (taken FIRST, per registered route order R4)

**What consumes the cap, quoted.**

- `critical/nodes/rate_half_band_crossing_location/statement.md:358-362`: "*T3 FISHER SUB-STRATUM (pairwise overlaps <= theta < a^2/n give #slopes <= (a-theta)/(a^2/n - theta): at sigma = 2^34, <= 32 with 123 bits margin at theta = n/4; <= 2^39-2^27+1 with 89 bits at theta = a^2/n - 1)*"
- `…/statement.md:370-374`: "*THE NAMED NEXT OBJECT IS SUPERSEDED AND SHARPENED: not "an upper bound on the max list profile" but **a pairwise-overlap cap below a^2/n = 2^39 + 2^34 + 2^27 (exact integer) at sigma = 2^34** — the moment it lands, T3 closes (UB-far) with 89 bits of margin.*"
- `…/statement.md:352-355` fixes the sets: "*T1 SUNFLOWER RIGIDITY (bad-slope pairs partition into lines; all pairwise intersections on a line coincide; petals disjoint; m_P <= 1 + r/(a - e_P))*".

**Which overlap notion, over WHICH set, at which sigma — answered.** The sets are `A_lam = Agr(f_1 + lam f_2, c_lam)`, `|A_lam| >= a`, for the CA-bad slopes of one **column-far** received pair at radius `r = n-a`; "pairwise" is over that slope set; `sigma = 2^34`, so `a = k+2^34 = 1,116,691,496,960`, `n = 2^41`, `r = 2^40-2^34`. The overlap is `A_lam cap A_mu = E_P`, the T1 core.

**Column-farness, quoted operationally.** The pair is column-far at radius `r` iff its column distance to `C^2` exceeds `r` (`background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md:28-34`, `(HS2)`), i.e. **iff no codeword pair `(p_0,p_1)` agrees with `(f_1,f_2)` on `>= n-r = a` common coordinates**. The executable form is round-29's own test, `notes/pilots_20260810/list_profile_bound/d2_sunflower.py:108-112`: `for S,…: if _drops(y1,S,lead) and _drops(y2,S,lead): return False`.

**The consumer bar and the object DIVERGE — this is the CATCH-24C firing.** On `E_P` we have `f_2 = v` and `f_1 = u` for the codeword pair `v = (c_lam - c_mu)/(lam - mu)`, `u = c_lam - lam v` (round-29's own T1 derivation, `list_profile_bound/REPORT.md:57`). So `E_P` **is** a codeword-pair joint agreement and column-farness caps it at `a-1` — nothing in the setting caps it at `k-1`. `c_lam` and `c_mu` agree only on `Z(v)`, which is not `E_P`. The `k-1` cap is the correct cap for a *different* object — the ordinary single-word list (`Agr(z,c_i) cap Agr(z,c_j) subset Agr(c_i,c_j)`), which is exactly what `rate_half_list_integer_johnson_safe_anchor` bounds. Round 29 had already flagged that that node "*bounds L_1, not B_ca^far*" (`statement.md:346-347`) — and then transported its cap constant into the `B_ca^far` object anyway.

**Second consumer defect: "they end together" is false.** `statement.md:368-370` asserts "*ratio 0.999748. The open bracket IS the region where the MDS pairwise-overlap cap exceeds the Fisher threshold; they end together.*" Measured (`d1_exact.py`):

| quantity | vanishes at | `a/n` |
|---|---|---|
| `GAP_ALG = (k-1) - a^2/n` | `a = 1,554,944,255,988` | 0.7071068 |
| `BRACKET = 3n/4 - a` | `a = 1,649,267,441,664` | 0.75 |

They differ by **94,323,185,676** — the same integer round-29's own D2 attributes to the integer-Johnson anchor (PR-1 HIT, exact). At the bracket top `GAP_ALG(3n/4) = -137,438,953,473`, already negative. The `0.999748` is the identity **`GAP_ALG = BRACKET - 1 - sigma^2/(2k)`** evaluated where `sigma^2/(2k) = 2^27` happens to be small — a local coincidence at one `sigma`, not a structural identity. **With the correct cap the coincidence evaporates: `GAP_FAR/BRACKET = 1.032006`.**

**Do D1-D3 attack THAT object?** Yes: every configuration in D1-D3 is a column-far pair at radius `r = n-a`, its slopes are CA-bad by the `dist(f_1+lam f_2, C) <= r` test, and the measured overlap is `|A_lam cap A_mu|` under a witness assignment (at `(8,4,17)` minimised over **all** 46,656 witness assignments, `d2_maxcore_results.txt:44-46`).

**PR-11/PR-10 grep result (CATCH-24A, own repo first).** `grep -rln "GAP_FISHER|pairwise-overlap cap|FISHER SUB-STRATUM" critical/nodes background/nodes` returns **exactly one file**: `critical/nodes/rate_half_band_crossing_location/statement.md`. `grep -c GAP_FISHER …/node.json` = **0**. So the false object lives in one critical node's statement text and in no `node.json` shard.

---

## D1 — THE EXTREMAL STRUCTURE (exact)

**Setup (normal form).** Translating by a codeword pair — legitimate, and the same normalisation the rider reduction uses (`background/nodes/rate_half_far_ca_rider_reduction/statement.md:22-24`) — write `f_1 = d_1`, `f_2 = d_2` and let `E = Z(d_1) cap Z(d_2)` be the core, `T = D \ E`. Then for `j in T` with `d_2(j) != 0` the coordinate `j` belongs to `A_lam` for exactly **one** `lam = -d_1(j)/d_2(j)`, and to none if `d_2(j) = 0 != d_1(j)`. This re-derives T1(iii) (petals disjoint) in one line and shows the whole configuration is the pair `(E, W)` with `W = span(d_1,d_2)` a 2-dimensional space, everything being `GL_2`-invariant.

**THE CEILING (banked, quoted above).** `2a-n <= e_P <= a-1`, the upper end being column-farness itself.

**THE EXTREMISER — LB1 (new).**

> **LB1.** Let `C = RS[F_q,D,k]`, `n = |D|`, `k < a <= n-1`, `r = n-a`, and suppose
> ```
> n < (a-k-1) * log2 q .                                   (LB1-C)
> ```
> Pick `E subset D` with `|E| = a-1`, `T = D\E` (`|T| = r+1`), set `d_2 = 1_T` and `d_1(j) = -lam_j` on `T`, `0` on `E`, with the `lam_j` distinct and nonzero. Then for all but a `2^n q^{k-a}(1+q^{1+k-a})`-fraction of such `lam`-assignments the pair `(d_1,d_2)` is **column-far at radius `r`**, its finite CA-bad slope set is **exactly `{lam_j}`**, of size `r+1`, each with the **unique** witness `0` and agreement set `A_{lam_j} = E cup {j}` of size exactly `a`; hence **every pairwise overlap equals `a-1` exactly**, and `T1(iv)` is tight (`m_P <= 1 + r/(a-e_P) = r+1`).

*Proof sketch (the counting).* Column-closeness at `S`, `|S| = a`, splits as `U_0 = S cap E`, `U_1 = S cap T`; on `U_0` both codewords vanish, on `U_1` we need `p_1 = 1` and `p_0 = -lam`. Since `|S| = a > k` and `C` is MDS, `p_1` is determined by `(U_0,U_1)` alone (independent of `lam`), and `p_0` ranges over the codewords vanishing on `U_0`, a space of dimension `max(0, k-|U_0|)`, which pins `lam|_{U_1}`. So the bad `lam` count is at most `q^{k-|U_0|} q^{|T|-|U_1|} = q^{k-a} q^{|T|}` per `(U_0,U_1)`, and there are at most `2^{|E|} 2^{|T|} = 2^n` such pairs. The same count with one extra factor `q` (the choice of slope) excludes any spurious witness `c != 0`, giving `(LB1-C)`. ∎

**`(LB1-C)` at the razor** (`d4_lb1.py`, exact integers, `a-k-1 = 17,179,869,183`):

| `log2 q >=` | `(a-k-1) log2 q` | margin over `n` |
|---|---|---|
| 128 | 2,199,023,255,424 | **−128 (FAILS)** |
| 129 | 2,216,203,124,607 | +17,179,869,055 |
| **167** | 2,869,038,153,561 | **+670,014,898,009** |
| 255 | 4,380,866,641,665 | +2,181,843,386,113 |

The widened RH-AC quantifier is `q > 2^167`, so **LB1 applies at every row RH-AC is posed over**, and fails only just below `2^129`.

**Delta against the cap: there is none — the sign is wrong.** `max overlap = a-1 = 1,116,691,496,959` versus the Fisher threshold `a^2/n = 2^39+2^34+2^27 = 567,069,900,800`. The cap must be beaten by a factor **1.969231** (PR-3 HIT, registered window `[1.9692,1.9693]`), and by **1.938935** even against T5's own (too small) constant (PR-2 HIT, registered `[1.9389,1.9390]`). The requested `delta > 0` does not exist; the honest `delta` is **negative**, `-549,621,596,159`.

**Why the pencils-only input of T4 does not help — the round's irony.** The brief's premise was to attack the cap "*WITH the pencils-only structure in hand*". The extremal violator **is a single pencil**: one T1-line carrying all `r+1` slopes. Pencil structure is not a constraint here, it is the construction.

**Consistency against a banked identity (independent check).** LB1's configuration has `Z_v = E`, `|Z_v| = a-1`, so THEOREM I' applies (`xr_band_key_lemma_pencil_mass/statement.md:41-46`): `sum_z agr(0,w_z) = q e(0) + (n-|Z_v|)`. LB1 gives `(r+1)a + (q-r-1)(a-1) = q(a-1) + (r+1)`, and `n-(a-1) = r+1` **exactly** (`d4_lb1.py`). COROLLARY I.1's `floor(n/a) = 1` and I.2's pairwise disjointness are not violated because LB1's `v` has `a-1` zeros, so THEOREM I (which needs `v` nowhere zero) does not apply — LB1 sits exactly in the `I'` regime, and it is the extremiser of that identity: it makes `|Z_v|` as large as column-farness permits, and the residual mass `n - |Z_v| = r+1` **is** the slope count.

---

## D2 — SUBCLASS PROOFS, AND WHAT REMAINS

**S1 (single-line subclass — unconditional, but an immediate corollary, not new).** If the CA-bad slope set of a column-far pair lies on one T1-line, then by `T1(iv)` `B_ca^far <= 1 + r/(a-e_P) <= n-a+1 = 1,082,331,758,593 = 2^39.9773`, i.e. **88.02 bits under the `2^128` budget** (PR-5 HIT, window `[88.0,88.1]`). *Scope:* one line only. *Falsifier:* a column-far pair whose bad slopes lie on a single line and number more than `n-a+1`. LB1 shows this bound is **attained**, so the subclass is settled exactly: `sup = n-a+1`.

**S2 (bounded line-degree — a residual, and it is banked as T2).** Anchoring at any bad slope `lam_0` with error weight `s`, `B <= 1 + sum_{P} r/(a-e_P) <= 1 + t*r` where `t` is the number of lines through `lam_0`, so **`t <= 2^128/r = 2^88.0227` suffices** (PR-6 HIT). But in the banked anchor coordinates a line through `lam_0` **is** a codeword `p` with `|Agr(f_2,p) \ E_0| = a - u_p`, `u_p = s+t_p-r >= 1` (`(AP2)/(AP3)`), so `LINE-DEGREE = |L(f_2, a-s)|` — a single-word list size at agreement `>= 2a-n = 2^35`. That is **exactly T2's bottleneck restated**; I claim a dictionary, not a new instrument. CATCH-24A subtraction against myself.

**S3 (the Fisher stratum, delimited exactly — new as far as I can grep).** The dictionary `e_P = n-s-t_P`, `a-e_P = s+t_P-r in [1,s]` converts T3's hypothesis into a statement about the *anchor error weight*:

> **S3.** If a column-far pair with `>= 2` CA-bad slopes satisfies T3's hypothesis (all pairwise overlaps `< a^2/n`), then **every** CA-bad slope has error weight `s > a(n-a)/n = 2^39 - 2^27 = 549,621,596,160`, equivalently `s/r > a/n = 65/128 = 0.5078125`.

So T3 is **empty on 50.78% of the admissible `s`-range** and one single CA-bad slope of agreement `>= n - (2^39-2^27) = 1,649,401,659,392` (`= 3n/4 + 2^27`) kills its hypothesis outright. This is a necessary condition only; the converse is not claimed. *Falsifier:* a column-far pair with all overlaps `< a^2/n` and one bad slope of weight `s <= 2^39-2^27`.

**Named residuals handed forward (unchanged status, RH-AC still open):**

- **R-LINEDEGREE.** Bound the number of T1-lines through one bad slope by `2^88`. Equivalent to `|L(f_2, a-s)| <= 2^88` — the banked T2/(RR2) bottleneck; **not** softened by anything this round found.
- **R-SECONDLEVEL.** The cores through a fixed slope live in `A_{lam_0}` (ground `a`) with `|E_i| >= 2a-n = 2^35`; the second-level Fisher threshold is `(2a-n)^2/a = 2^36/65 = 2^29.9776` against the MDS core-core cap `k-1` — short by a factor **1040.0**, versus the first level's 1.9692 (PR-9 HIT: `a/(2a-n) = 65/2 = 32.5` exactly; disjoint cores would give `t <= 32`). **The second level is ~2^10 farther away than the first, so it is not the cheaper door.**
- **R-UPPERBOUND.** With the cap route dead, the only remaining shape for the safe half at `sigma = 2^34` is an upper bound that uses the code, not the overlap statistics. LB1 tells you the target it must clear: `B_ca^far(k+2^34) in [1,082,331,758,593, 2^128)`.

---

## D3 — THE SCALED SEARCH

**Pre-registration.** The extrapolation was registered in `PREREG.md` (R5, PR-7, PR-8) **before any run**: cells, fields, predicted `GAP_FISHER`, and the two-sided prediction. `BUDGET` (below) is **not** pre-registered — it was derived from LB1's counting argument after `d1_exact.py` ran, and is reported as a diagnostic, disclosed.

`BUDGET := (a-k) log2 q - log2 C(n,a)` is the small-scale analogue of LB1's `(LB1-C)`. Every measured cell has **negative** budget; the razor has `+2,181,843,386,368`. **The scaled cells therefore sit in the regime where LB1 is *hardest*, and they exhibit the extremal object anyway** (`d3_ladder_results.txt`, `d2_maxcore_results.txt`):

| cell `(n,k,a,q)` | `a^2/n` | `a-1` | `GAP_ALG` | `GAP_FAR` | BUDGET | witness | density |
|---|---|---|---|---|---|---|---|
| (8,4,5,17) | 3.1250 | 4 | −0.1250 | **+0.8750** | −1.72 | **YES** (exhaustive) | 0.8202 |
| (8,4,5,41) | 3.1250 | 4 | −0.1250 | +0.8750 | −0.45 | YES | 0.9907 |
| (8,4,6,17) | 4.5000 | 5 | −1.5000 | +0.5000 | +3.37 | **YES** (exhaustive) | 0.9902 |
| (8,4,7,17) | 6.1250 | 6 | −3.1250 | **−0.1250** | — | **no** (exhaustive, and correctly so) | — |
| (10,5,6,11) | 3.6000 | 5 | +0.4000 | +1.4000 | −4.25 | YES | 0.1185 |
| (10,5,6,31) | 3.6000 | 5 | +0.4000 | +1.4000 | −2.76 | YES | 0.7802 |
| (12,6,7,13) | 4.0833 | 6 | +0.9167 | +1.9167 | −5.93 | YES | 0.0100 |
| (12,6,7,37) | 4.0833 | 6 | +0.9167 | +1.9167 | −4.42 | YES | 0.5900 |
| (16,8,9,17) | 5.0625 | 8 | +1.9375 | +2.9375 | −9.39 | **no** (0/9,353, sampled) | 0.0000 |
| (16,8,10,17) | 6.2500 | 9 | +0.7500 | +2.7500 | — | **NOT MEASURED** | — |

*(exhaustive rows are from `d2_maxcore.py`, which enumerates every `(E,W)` at the maximal core; the density there is `5,111,260/6,232,100` at `a=5` and `17,024/17,192` at `a=6`.)*

**Is the 0.999748 gap real headroom or a bound-pair artifact? It is a bound-pair artifact, twice over.** (i) The `k-1` half of the pair is the wrong cap (D4); (ii) the near-unit ratio is the identity `GAP_ALG = BRACKET - 1 - sigma^2/(2k)` evaluated where `sigma^2/(2k)` is negligible. There is no headroom: the true gap has the opposite sign.

**Three-scale trend, exact.** `RATIO_CAP = 2k(k-1)/(k+s)^2`: `1.1111 (k=5) < 1.2245 (k=6) < 1.3827 (k=8)`, rising to **1.938935** at the razor and `-> 2` as `k -> inf` with `s = o(k)` (PR-8 HIT, closed form verified against the razor value). `RATIO_FAR = (a-1)/(a^2/n)` rises the same way to **1.969231**. **The refutation gets *stronger* with scale, monotonically, on both cap readings** — the opposite of the "scaled cells are structurally incapable" verdict that decommissioned the ladder in round 29, because this question is about a *ratio at a single agreement*, not about a bracket interior width.

**A structural fact the exhaustive census produced.** At the maximal core `e = a-1` the three counts coincide exactly (`d2_maxcore_results.txt:8-10`): column-far ⟹ core exactly `E` ⟹ `>= 2` bad slopes. Both implications are theorems, not coincidences: a common zero at `j in T` makes `S = E cup {j}` a joint-explanation event of size `a` (hence column-close); and each `j in T` kills exactly one direction of `W`, with all `|T| >= 2` directions equal only if that direction were `0`. **So at the maximal core, *every* column-far configuration is a cap violator whenever `(a-1)n > a^2`.**

**Witness verified end-to-end at `(8,4,17)`, `a=5`** (`d2_maxcore_results.txt:38-47`): `E = {0,1,2,3}`, `d_1 = (0,0,0,0,1,0,0,0)`, `d_2 = (0,0,0,0,0,1,1,2)`; `column_far = True`; 16 finite CA-bad slopes; **`THETA_MIN` minimised over all 46,656 witness assignments `= 4 > a^2/n = 3.125`**. So the hypothesis fails under *every* legal witness choice, not just the natural one — the refutation is not an artifact of witness selection.

**Inference (not a measurement, flagged).** Round-29's T3 validation guards the entire test behind `if theta * n < a * a:` (`d2_sunflower.py:181`), and its targeted generator plants a core of size `a0-1 = a-1` (`d2_sunflower.py:206-227`) — exactly the maximal-core family whose `theta = a-1 = 4 >= 3.125`. On those configurations the T3 test is **skipped, silently**, so "0 violations of T3 across 21,832 column-far configurations" (`crossing_location/statement.md:351-352`) is consistent with T3's hypothesis being false on most of the census. **I did not measure the skip fraction** (miss 8); the structural reason is stated, the number is not claimed.

---

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| PR-1 | `94,323,185,676` exact | **HIT** exact |
| PR-2 | `RATIO_CAP in [1.9389,1.9390]`, `->2` | **HIT** 1.938935 |
| PR-3 | `RATIO_FAR in [1.9692,1.9693]` | **HIT** 1.969231 |
| PR-4 | `m_P <= 2` at `e = a^2/n` | **HIT** (`193/65`, floor 2) — but my qualitative gloss was backwards, miss 2 |
| PR-5 | single-line margin `[88.0,88.1]` bits | **HIT** 88.0227, `n-a+1 = 1,082,331,758,593` |
| PR-6 | `T_MAX = 2^88.02` | **HIT** |
| PR-7 | witness at every `GAP_ALG>0` cell; none at (8,4,5) | **HIT / MISS** — witnesses at (10,5,6) and (12,6,7); (8,4,5) **also** has witnesses (miss 1); (16,8,9) no witness found (zero power) |
| PR-8 | `1.1111<1.2245<1.3827`; closed form | **HIT** exact |
| PR-9 | `(2a-n)^2/a = 2^36/65`, `a/(2a-n)=65/2` | **HIT** exact |
| PR-10 | Johnson banked; 0 nodes state the cap | **HIT / MISS** (miss 4) |
| PR-11 | 0 node files consume T3/T5 | **MISS** — 0 `node.json`, 1 `statement.md` (miss 3) |
| PR-12 | `a(n-a)/n + 1 = 549,621,596,161` | **HIT** exact |
| PR-13 | *(miss-likely)* neither half of RH-AC closes; hand forward LINE-DEGREE | **HIT as a registered miss** — and LINE-DEGREE turned out to be banked T2 |
| R1 | P(refuted)=0.75, P(proved)=0.05 | refuted; **but the prior was informed by the anchors' own text and is not independent evidence** |

---

## CATCH-24A SUBTRACTIONS (own-repo greps run before every novelty claim)

1. **The `a-1` cap is BANKED** — `xr_band_key_lemma_pencil_mass/statement.md:57-61` (KEY LEMMA graded consequence) and `rate_half_far_ca_anchor_pencil_normal_form/statement.md:33-34` (`(AP3)`: `s+t-r >= 1`). Not mine.
2. **The `a^2/n`-is-the-mean observation is BANKED** — `rate_half_list_integer_johnson_safe_anchor/proof.md:62-73`.
3. **The species "route-sufficiency refutation by exhibiting objects compatible with the overlap data" is BANKED in another lane** — `l1_fpc5_ratehalf_m4_t2_distance_only_no_go/statement.md:43-46` ("*No support-distance-only argument can yield the required fixed polynomial bound*"). Its Scope explicitly disclaims constructing a received word; **LB1 does construct one**, which is the difference.
4. **Explicit column-far lower-bound witnesses exist in-repo** — `rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence/statement.md:30-49` (an `m=1`, `N=16`, `r=3` pair with 5 finite supported slopes, i.e. `> r+1 = 4`). Prior art for the *species*; LB1 is the general-`r`, all-scales, maximal-core version and is the first at the razor row.
5. **The upper bound `T <= r+1` is BANKED** (`rate_half_ca_hankel_minimal_index_budget/statement.md:55-61`); what is new is that LB1 makes it **tight**.
6. **T2 / LINE-DEGREE** — my S2 is the banked stratified rider in other coordinates. Claimed as a dictionary.

**Genuinely additive this round:** the D4 object-slip audit and the "they end together" correction; **LB1** and its `(LB1-C)` admissibility; the tightness corollaries (`B_ca^far(n-r) = r+1`; `B_ca^far(3n/4) = 2^39+1`, so budget `2^39` is unattainable there); **S3**'s exact delimitation of T3's stratum; and the exhaustive maximal-core census.

---

## ZERO-POWER DECLARATIONS

- **Constructions refute caps; they never establish them.** Every witness number here is a **lower** bound on the true maximum overlap. I report no constructed maximum as an upper bound.
- **Sampled negatives have no power.** `(16,8,9,17)` returned 0 hits in 9,353 samples; that is **not** a non-existence proof, and `(16,8,10)` was not measured at all.
- **No exhaustive search over far pairs is inside the compute law** at any cell beyond `n_s = 8`: the `(E,W)` space is `C(n,a-1) * [n-a+1 choose 2]_q`, already `>= 2.5e8` at `(10,5,6,11)`. The `(8,4,17)` results are exhaustive over `(E,W)` at the **maximal core only**; smaller cores were not enumerated (and are not needed — the maximum is what is at issue).
- **No mean, random-word, or density quantity enters any verdict.** The `density` column is descriptive only; the refutation rests on the exhibited witnesses and on LB1.
- **`BUDGET` is a heuristic diagnostic**, not pre-registered, and is *sufficient-not-necessary*: it is negative at 8 of 8 measured cells and witnesses exist at 7 of them.
- **Two-field confirmation** was used at every scaled cell where a structural claim is made (`q in {17,41}`, `{11,31}`, `{13,37}`); single-field numbers are controls.
- **LB1's razor step is a human proof** (miss 9).

---

## COMPLIANCE

Brief read first; the two named anchors (`list_profile_bound/REPORT.md`, `collinearity_object/REPORT.md`) read next and **nothing else** before the registrations R0-R8 (priors, expected extremal shape, expected scaled-gap trend, functionals, cell grid, PR-1..PR-13 with numeric windows, zero-power declarations, compliance plan) were appended to `notes/pilots_20260810/rh_overlap_cap/PREREG.md` with the Edit tool — **before any grep, any `ls`, and any interpreter invocation**. No post-hoc edits to the registrations; `BUDGET` is disclosed in-line as un-registered.

**COMPUTE LAW: 5 interpreter invocations, 5 under `tools/ramguard`, 0 breaches, 0 bare `python3`.** Each was `tools/ramguard tiny|local -- python3 …` run from the repo root with a literal `--` and an explicit `RAMGUARD_TIMEOUT`: (1) `d1_exact.py` *tiny*/60s; (2) `d2_maxcore.py` v1 *local*/290s — produced only its header inside the wall and was superseded; (3) `d2_maxcore.py` v2 (kernel-marking rewrite) *local*/280s, completed in 90.3s; (4) `d3_ladder.py` *local*/280s, completed at its own 250s wall guard with the last two cells declared NOT MEASURED; (5) `d4_lb1.py` *tiny*/60s. Stdlib only (`itertools`, `random`, `fractions`, `math`, `time`); no Modal, no network, no git, no subagents.

**BANKED SCRIPTS: none were run.** I re-implemented the round-29 primitives (`build` / `drops` / `column_far` / `codewords_at`) inside my own `d2_maxcore.py` from reading `d2_sunflower.py`; no scratch copy was executed and no banked file was opened for writing. *Scope note:* those helpers are ported from round-29's **post-bugfix** code, so a residual error there would propagate into my PART B census — the structural cross-check (column-far ⟹ core exactly `E` ⟹ `>=2` bad slopes, proved independently above) is the guard against that.

**RAM DISCIPLINE:** file-at-a-time reads; **`dag.json` never opened**; node facts taken from `critical/nodes/*/` and `background/nodes/*/` shards plus grep; no bulk loads; the two long runs backgrounded with progressive checkpointing to `d2_maxcore_results.txt` and `d3_ladder_results.txt`; one run re-scoped after a wall hit (disclosed, misses 7/8) rather than extended.

**QUARANTINE HELD TOTALLY:** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened at any line; the three sibling round-31 directories (`rh_type2_stratum`, `rh_transport_dictionary`, `rh_e_axis_audit`) never read and never listed — `notes/pilots_20260810/` itself was never listed, only the two directories I am entitled to; no path containing `prize-codex-` was touched, read, or globbed.

**WRITE SCOPE:** every write is inside `notes/pilots_20260810/rh_overlap_cap/` — `PREREG.md` (registrations appended), `d1_exact.py`, `d2_maxcore.py`, `d2_maxcore_results.txt`, `d3_ladder.py`, `d3_ladder_results.txt`, `d4_lb1.py`. **`REPORT.md` itself could NOT be written: the harness refused the write** ("Subagents should return findings as text, not write report files"), so this report is returned verbatim as the final message per the brief's fallback clause, and the pilot directory contains the scripts and results files but no `REPORT.md`. **No `dag/`, `critical/`, `background/`, `nodes/` or `tools/` file was edited**; no git operation of any kind; no stray files created outside the pilot directory. AUDIT-AND-DRAFT respected: **no node surgery is applied here.** The two corrections that touch a critical node's statement text (T5's cap constant, and "they end together") are **flagged for the coordinator, not applied.**
