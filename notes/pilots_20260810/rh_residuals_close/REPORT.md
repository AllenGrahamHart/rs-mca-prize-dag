# REPORT — rh_residuals_close (round 32)

## VERDICT (first)

**Neither budget closes. Status unchanged.** What changed is that two of
the three residuals are now *named to the integer* and one is *retired*:

- **Residual (i) is ONE INTEGER at the official profile, not "1 or 3".**
  Exhaustively certified (not sampled, not binary-searched):
  `w* = 733007751851 = (2^41+1)/3` is the **only** value of `w*` in the
  whole window `[4m+2, 8m-2] = [549755813890, 1099511627774]` covered by
  neither instrument — for `O = 0, 1, m/2, m-2` alike. There `(AO1)`
  returns `549755813889 = rho+2` **exactly** (deficit 1) and T4's
  hypothesis fails by **exactly one point** (`2s = a*+1`, `RIG = -2`).
- **Residual (i) is now FENCED against the incidence-only route**, the
  same way the wave-57 node fences residual (ii): I exhibit an explicit
  set system at `m = 2` (same residue class `m = 2 mod 3`, same
  `RIG = -2`) satisfying *every* banked incidence axiom at the gap
  integer `a* = 11` with `T = rho+2` — block sizes, `d_x <= e`, the exact
  saturation deficit, `(OV)`, `(C2)`. Its type-2 blocks are the **vertex
  stars of `K_7`** on the 21 outside points. So residuals (i) and (ii)
  are the **same frontier**: both need algebra, not counting.
- **Residual (iii) `m = 1` is NOT open and NOT closable — it is a PROVED
  counterexample**, `background/nodes/rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence`
  (status PROVED, `statement.md:3`). The exhaustion the brief asks for
  was already run there. I replayed it by a **completely independent
  route** (support configurations, not locator coefficient lines) and
  reproduce it exactly: **16 configurations, one per omitted domain
  point, `T = 5` each**, with `(M1F3)` among them.
- **NEW, and the round's one genuinely new fact: the `m=1` failure is a
  `q = 17` artifact.** Exhaustive census at **ten** admissible fields
  (`q = 17, 97, 113, 193, 241, 257, 337, 353, 401, 433`; all satisfy
  `16 | q-1`): **16 configurations at `q = 17` and ZERO at the other
  nine.** The banked node is a `q = 17` statement only; nothing in-repo
  records any `q`-dependence (CATCH-24A grep below returns nothing).
- **D4, the flagged inference discharged: the T3 skip fraction is
  `19518/21832 = 0.894009`.** `critical/nodes/rate_half_band_crossing_location/statement.md:663`
  says "the skip fraction was NOT measured — flagged inference, not a
  claim". It is now measured. The inference was right and is stronger
  than stated: at `a = 5` — the cell where `M_max = 17` against
  `n-a+1 = 4`, i.e. exactly where a cap is most needed — the guard
  passes **0 times out of 5842**. T3 is 100% vacuous there.

---

## MISSES FIRST

1. **I accused the round-29 anchor of an untested claim, and the
   accusation was FALSE.** I registered (R2/P2) that round 29's
   "gap `∈ {1,3}`, never 0" was untested at `m ≡ 0 mod 3` because its
   REPORT's four examples (`m = 2,4,8,40`) contain none. The **results
   file does**: `notes/pilots_20260810/collinearity_object/d3_coverage_results.txt:20,22,25,28,...`
   tabulates `m = 3,6,9,12,15,18,24,36,39`. I registered a CATCH from a
   summary without opening the underlying table. Withdrawn.
2. **P2 also missed numerically.** I predicted gap size `2` at
   `m ≡ 0 mod 3`; it is `1`. And I predicted size `1` uniformly at
   `m ≡ 2 mod 3`; `m = 5` gives `3` and `m = 8` gives `2`. Correct law
   (verified `m ∈ [1,300]`): size `3` iff `m ≡ 1 mod 3`, else `1`, with
   exactly three exceptions `m ∈ {1, 5, 8}`.
3. **P5 arithmetic slip, twice.** I registered "T4 fails by 2 points,
   i.e. `RIG = -3`" and "the difference polynomial is
   `sigma_W * (quadratic)`". Measured: `2s - a* = 1`, so `RIG = -2` and
   the difference is `sigma_W * (LINEAR)` — one degree past the `q=17`
   fence's `sigma_W * (constant)`, not two. The "fails by one point"
   half is right; the two consequences I derived from it were both off
   by one.
4. **Residual (i) did NOT close.** Registered `P = 0.25`; resolved NO. I
   did not extend either instrument. What I produced is the exact
   obstruction plus a fence showing the obstruction is *not* removable
   by the incidence axioms — which is progress of a different kind and
   I do not dress it up as a closure.
5. **My whole planned D2 was a REPLAY of a PROVED node, and I did not
   know that when I registered.** R3 registered a search design as if
   the `m=1` exhaustion were open. It is banked
   (`..._strict_m1_corefree_five_slope_route_fence`, PROVED, complete
   locator-line census, `statement.md:51-56`). CATCH-24A caught it
   before I claimed anything. My contribution is a second independent
   route to the same 16 objects plus the `q`-ladder — not the census.
6. **A mislabelled check in my own results file, flagged not silently
   fixed.** `d1c_fence_results.txt` prints, at `m = 2`,
   `MEAN <= MAX feasible: False` — while part (B) of the *same file*
   constructs an explicit system satisfying everything. The check is
   wrong, not the feasibility: it compares the **top** of the range
   `sum_{type-2}|S ∩ W| ∈ {7,8}` against the max as if `8` were forced,
   whereas the realized value is `7` (the saturation-deficit point sits
   inside `W`). Reported as a mislabel, per the round-29 precedent.
7. **`d3_ledger_results.txt` D3.6 prints `2^89.0000` for the far-CA
   headroom.** That is a `bit_length` artifact of my own print. The
   correct figure is **88.02 bits**
   (`notes/pilots_20260810/rh_overlap_cap/REPORT.md:21`). Flagged.
8. **My D1.3 binary search was unsound as written.** It assumed the
   `(AO1)` closure band is contiguous. At `m = 8` it is **not** — and I
   only discovered that because my own re-derivation disagreed with the
   banked table (see CATCH below). I repaired it with a complete
   divisor-block certificate (`d1b_holes.py`), which is why the official
   single-integer claim is a certificate and not a search result.
9. **The D3.3 shares `1/3 + 5/12 + 1/4` are ASYMPTOTIC, not exact.**
   `549755813885` is not divisible by 3, 12 or 4; the exact widths are
   `183251937961 / 1 / 229064922452 / 137438953471`. My registered
   phrasing (and the anchors') should be read as limits.
10. **A live risk against my own D1 conclusion, stated because it may
    kill it.** I claim "T4's *conclusion* at `a*` would close residual
    (i) with a `5/3` margin". T4's conclusion is a bound on a
    **collinear** family of reciprocal locators. Collinearity of the
    `{P_{S_gamma}}` needs `kappa_gamma|_W` to lie in the 2-space
    `span{z_0, z_1}`, i.e. `v_gamma|_W = 0`, i.e.
    `S_gamma ∩ W = {}`. At the `q=17` fence that holds
    (`apolar_origin/REPORT.md:53`: "`|S n W| <= 0` **with equality**"),
    but at `a*` the profile forces `|S_gamma ∩ W| = (4m-5)/3 - o_gamma
    > 0` for every `m >= 2`. **If the collinearity transport needs
    disjointness, then "T4 at `RIG = -2`" is not sufficient and residual
    (i) is deeper than I priced it.** I did not resolve this; it is the
    first follow-up.
11. **QUARANTINE BREACH, disclosed.** One recursive grep (for
    "wave-57") was rooted at `notes/` without `--exclude-dir`, and it
    **printed four matching lines of
    `notes/pilots_20260802/CAMPAIGN_LEDGER.md` to me**, one of which
    named a round-32 sibling's mandate. This is worse than round 31's
    M7 (traversal without surfacing): content was surfaced. Nothing in
    this report derives from those lines, and every subsequent grep
    carried `--exclude-dir=pilots_20260802` plus the three sibling
    directories. Recorded as a breach, not a near-miss.
12. **Zero replay-identity evidence for D1/D2/D3** — those are my own
    scripts. The one escape replay I ran (D4) is byte-identical and
    reproduces `21,832 / 0 violations` exactly.

---

## CATCH-24A — own-repo subtraction, run BEFORE every claim

| object | in-repo prior | verdict |
|---|---|---|
| the `m=1` five-slope exhaustion | `background/nodes/rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence/statement.md:51-56` — "the maximum number on a core-free affine coefficient line is exactly five. There are exactly `16` such five-lines, one for each omitted domain point" | **PROVED, BANKED.** My D2 is an independent replay, not a discovery. |
| `(M1F3)` the five triples | same node, `statement.md:35-39` | banked; I reproduce it as a `zeta`-shift |
| the `(AO1)` formula | `notes/pilots_20260810/apolar_origin/PREREG.md:197-198` | banked |
| T4's hypothesis `2s <= a-1` and its `w* >= ceil((16m+3)/3)` reading | `notes/pilots_20260810/collinearity_object/REPORT.md:21,25` | banked |
| the `w*` window `[4m+2, 8m-2]` | `notes/pilots_20260810/collinearity_object/d3_coverage_results.txt:18` | banked |
| the gap "1 or 3 integers per `m`" | `collinearity_object/REPORT.md:93`; `rh_type2_stratum/REPORT.md:190`; `critical/nodes/rate_half_band_crossing_location/statement.md:516-517` | banked — and **CONTRADICTED at `m=8`** (below) |
| `(NEWCAP)` `w* <= 7m-1`, cap `1236950581231`, factor `9/4` | `rh_type2_stratum/REPORT.md:19,28`; `crossing_location/statement.md:571-579` | banked; I re-derive the integers and add one precision nit |
| the incidence-only fence for `(FR)` | `background/nodes/rate_half_type2_fr_incidence_only_route_fence/statement.md:8-37` (PROVED) | banked — **my D1c is its transport to residual (i)**, a new instance of a banked method |
| LB1, `B_ca^far(3n/4) >= 2^39+1` | `notes/pilots_20260810/rh_overlap_cap/REPORT.md:19,21`; `crossing_location/statement.md:653-654` | banked |
| RPFC territory `q ∈ [2^167, 2^167+2^129)` | `background/nodes/rate_half_residual_prime_field_collapse/statement.md:11-20`; `rh_e_axis_audit/REPORT.md:47` | banked |
| the T3 guard's vacuity | `rh_overlap_cap/REPORT.md:155` and `crossing_location/statement.md:660-663` — "**I did not measure the skip fraction**", "flagged inference, not a claim" | **inference banked, NUMBER NOT.** My `0.894009` is the first measurement. |
| the gap integer `733007751851 = (2^41+1)/3` | grep over `notes/ critical/ background/` for `733007751851`, `(2^41+1)/3`, `16m+1)/3` returns **nothing** | **NEW** |
| any `q`-dependence of the `m=1` fence | grep for `q=97`/`q = 97` in the fence node and in `crossing_location` returns **nothing** | **NEW** |
| the `K_7`-vertex-star set system at `a*` | no prior; the wave-57 fence uses a "quartic-difference-family" at `a = 7m-1` (`crossing_location/statement.md:773`) | **NEW instance**, banked method |

---

## D1 — RESIDUAL (i), THE TILING GAP

### The two coverage statements, quoted

> **apolar `(AO1)`** — `notes/pilots_20260810/apolar_origin/PREREG.md:197-198`:
> `T <= min( m+1, floor(a/(a-rho)), floor((a m + O)/rho) ) + floor( ((N-a) m) / ((R+1) - a) ) , a < R+1.`

> **T4** — `notes/pilots_20260810/collinearity_object/REPORT.md:25`:
> "the hypothesis `2s <= a-1` (with `s = R+1-a = 8m+1-a`) reads
> `w* >= ⌈(16m+3)/3⌉` — the top TWO THIRDS of the admissible `w*` window".

Window: `w* ∈ [4m+2, 8m-2]`
(`collinearity_object/d3_coverage_results.txt:18`).

### D1.1 — my own re-derivation vs the banked table: 25/26, and the one disagreement is real

`d1_gap.py` reproduces round 29's gap table on **25 of 26** rows. The
disagreement is `m = 8`:

| | `m=8` |
|---|---|
| banked (`d3_coverage_results.txt:26`) | apolar band `[34..42]`, GAP `{43}` |
| mine | closure set `[34..40] ∪ {42}`, GAP **`{41, 43}`** |

`AO1(8, 41) = 33 > 32 = rho+1` (`T1cap = floor(41/10) = 4`, `CAP = 29`)
while `AO1(8, 42) = 32 <= 32` (`T1cap = floor(42/11) = 3`, `CAP = 29`).
**The `(AO1)` closure band is not always an interval** — it has a hole
exactly where `floor(a/(a-rho))` steps from 4 to 3, i.e. at
`a = floor(4rho/3)`. The banked table prints the band as a range and so
hides `w* = 41`. Consequence for the ledger: the banked "gap is 1 or 3
integers per `m`" is **false at `m = 8`** (it is 2 there), and any future
claim of the form "the band is `[4m+2 .. a_max]`" needs the hole test.

### D1.2 — the gap law

Verified `m ∈ [1,300]` (`d1_gap_results.txt` D1.2):

```
m = 0 mod 3 : gap = { 16m/3 }                                     (size 1)
m = 1 mod 3 : gap = { (16m-4)/3, (16m-1)/3, (16m+2)/3 }           (size 3)
m = 2 mod 3 : gap = { (16m+1)/3 }                                 (size 1)
exceptions  : m = 1 (window degenerate), m = 5 (size 3), m = 8 (size 2)
```

### D1.3 — the official profile, certified exhaustively

`m = 2^37 ≡ 2 mod 3`, so the gap is a **single integer**:

```
(AO1) closure band = [549755813890 .. 733007751850]
GAP                = { 733007751851 }  = (2^41+1)/3
T4 band            = [733007751852 .. 1099511627774]
```

This is **not** a binary-search artifact. `d1b_holes.py` enumerates the
`1,482,906` divisor blocks of `rho` (on each block `j(a) = floor(a/(a-rho))`
is constant, the third term of the min is nondecreasing and `CAP` is
nondecreasing, so `AO1` is nondecreasing and the block top decides the
block) and returns the **complete** uncovered set below the T4 threshold:

```
O = 0        : { 733007751851 }
O = 1        : { 733007751851 }
O = m/2      : { 733007751851 }
O = m-2      : { 733007751851 }
```

(At `O = m-1` the band's own bottom `a = 4m+2` stops closing —
`AO1 = rho+2` — which is apolar's registered P7; the tiling statement is
an `O <= m-2` statement.)

### D1.4 — what the gap integer is, exactly

At `a* = 733007751851`:

| quantity | value |
|---|---|
| `s = R+1-a*` | `366503875926 = (8m+2)/3` |
| `2s - a*` | `1` (T4 needs `<= -1`) |
| `RIG = a*-1-2s` | `-2` |
| `T1cap = floor(a*/(a*-rho))` | `3` |
| `CAP = floor((N-a*)m/s)` | `549755813886 = 4m-2` |
| `(AO1)` | `549755813889 = rho+2` |
| deficit vs `rho+1` | **1** |
| `AO1(a*-1)` | `549755813888 = rho+1` (closes) |

So the gap integer carries the **same signature as the `q=17` fence**:
the bound fails by exactly one slope.

### D1.5 — what is FORCED there, and the exact size of the missing step

Under `(SAT3)` `T = rho+2` at `a = a*`:

```
T_1 = 3                       FORCED (T1cap = 3 and T_2 <= CAP = 4m-2 = T-3)
T_2 = 549755813886 = 4m-2     FORCED EXACTLY
outside capacity (N-a*)e    = 201487636602392382799872
minimum type-2 spend T_2*s  = 201487636602071691908436
total excess sum eps_gamma <= 320690891436          = (7m+4)/3
#{minimum-weight type-2}   >= 229064922450          = (5m-10)/3
```

T4's conclusion (`M <= e+1 = m+1 = 137438953473`) would contradict that
with **margin `91625968977`, ratio `1.6667 = 5/3`**. So:

> **The gap integer needs a cap of `(5m-10)/3` on the number of
> minimum-weight type-2 slopes. T4 delivers `m+1`, which is `5/3`
> stronger than required. The only thing missing is T4's hypothesis, and
> it is missing by exactly one point of `W`.**

Equivalently (P6, registered blind and HIT): a **one-unit** improvement of
the per-slope spend floor (`p_gamma >= s+1` for every type-2 slope, i.e.
no minimum-weight type-2 slope at `a*`) closes it, because the required
floor is `s + (7m+4)/(12m-6) < s+1`.

`(NEWCAP)` does not help: `a* = 733007751851 < 7m-1 = 962072674303` for
every `m` (checked `m ∈ [1,300]` and at official scale). The `w*` ceiling
that *would* close residual (i) is `733007751850`, requiring a
strengthening of `(NEWCAP)` by the factor `21/16 = 1.3125` exactly — and
such a ceiling would kill residual (ii) at the same time.

### D1.6 — THE OBSTRUCTION, and why counting cannot remove it

The T4 algebra at `a*`: two degree-`2s` polynomials agreeing on the `a*`
points of `W`, with `2s = a*+1`, differ by `sigma_W * Q` with
`deg Q <= 1`. At `RIG >= 0` the difference is `0`; at the `q=17` fence
(`RIG = -1`, `2s = a`) it is `sigma_W * (constant)` — measured `4 sigma_W`
(`collinearity_object/REPORT.md:29`); **at the official gap integer it is
`sigma_W * (linear)`.** That single linear factor is residual (i).

**Can counting alone remove it? No.** `d1c_fence.py` exhibits, at `m = 2`
(the smallest scale in the official residue class, with the same
`RIG = -2`), an explicit set system at the gap integer `a* = 11` with
`T = rho+2 = 9`:

```
W          = {0..10}                                    (|W| = a* = 11)
type-1 (2) : {4,5,6,7,8,9,10} , {0,1,2,3,8,9,10}        (S subset W)
type-2 (7) : vertex stars of K_7 on the 21 outside points,
             each plus one distinct W-point:
             {0,11,12,13,14,15,16} {1,11,17,18,19,20,21} {2,12,17,22,23,24,25}
             {3,13,18,22,26,27,28} {4,14,19,23,26,29,30} {5,15,20,24,27,29,31}
             {6,16,21,25,28,30,31}
```

Verified in the results file: `|S_gamma| = rho = 7` for all 9 blocks;
`max d_x = 2 = e`; `sum_x (e-d_x) = 1` (so `O = 0`); type-1 blocks inside
`W`; every type-2 spend `|S \ W| = 6 = s` exactly (all minimum-weight);
`min |S ∪ S'| = 11 = w*` so `(OV)` holds for **every** pair; the incidence
identity `sum_{pairs}|S ∩ S'| = sum_x C(d_x,2) = 31 = 31`; `max` pairwise
overlap `3 = 2rho-a`. **Every banked incidence axiom is satisfied at the
gap integer with `T = rho+2`.**

> **Fence (residual (i) analogue of the wave-57 node).** No proof using
> only block sizes, `d_x <= e`, the exact saturation deficit `(SAT4)`,
> the pairwise union `(OV)` and the MDS spend floor `(C2)` can exclude
> `w* = a*`. Residual (i) is an **algebraic** residual, exactly like
> residual (ii).

Integer feasibility of the same necessary conditions also holds at
`m = 8, 32, 2^37` (`d1c_fence_results.txt` part A) — but that is
feasibility of *necessary* conditions, **not** a construction, and I
name it as such: over-reading exactly such a certificate is what round 31
self-falsified (`rh_type2_stratum/REPORT.md` MISS 2).

---

## D2 — RESIDUAL (iii), `m = 1`

### The answer to the brief's question: NO, and for a reason the brief did not anticipate

`m = 1` is **not closable by exhaustion, because the exhaustion has been
done and it produces witnesses.** `background/nodes/rate_half_ca_hankel_strict_m1_corefree_five_slope_route_fence`
is **PROVED** (`statement.md:3`) and already contains the complete census
(`statement.md:51-56`): "Among all `C(16,3)=560` monic split cubic
locators over `D`, the maximum number on a core-free affine coefficient
line is exactly five. There are exactly `16` such five-lines, one for each
omitted domain point." Residual (iii) is therefore **not an open gap** —
it is a permanent exclusion, and the correct bookkeeping is to reclassify
it from "open residual" to "proved counterexample, quarantined by `m`".

### Independent replay (the evidence round 31 lacked)

`d2_m1.py` censuses **support configurations** rather than locator
coefficient lines — a different object, a different search. Set-up
(all of it forced, not assumed):

- `(C4)` `O <= delta = m-1 = 0` forces `|S_gamma| = rho = 3` for all five.
- **Pairwise disjointness is PROVED, not assumed** (I registered it as a
  banked hypothesis `d_x <= e = 1`; it is in fact a theorem here): if
  `S_1 ∩ S_2 != {}` then `|S_1 ∪ S_2 ∪ S_i| <= 8 < 9 = d(K)`, so
  `kappa_i = 0` and every support lies inside `W = S_1 ∪ S_2`,
  `|W| <= 5`; then `sum_{x∈W} #{i : x ∉ S_i} = 5(|W|-3)` must be
  `<= |W|` (each coordinate functional vanishes at one projective point),
  i.e. `10 <= 5` at `|W| = 5` and `5 <= 4` at `|W| = 4` — both false;
  `|W| = 3` is excluded by column-farness (`(C1)`).
- With disjointness, `Z_i = S_1 ∪ S_2 ∪ S_i` has 9 points, the shortened
  code has dimension `|Z|-R = 1`, so `kappa_i = lambda/sigma'_{Z_i}` and
  five slopes are simultaneously supported **iff** three pairwise
  disjoint candidate triples share the same normalized restrictions to
  `S_1` and to `S_2`. That is the search, and it is exact.

Result at `q = 17` (`d2_m1_q17.txt`): 10,010 `(S_1,S_2)` pairs (35 orbit
representatives x 286), 120 candidates each — **5 configurations up to the
`zeta`-shift symmetry, 16 in full, one per omitted domain point,
`T = 5` for every one** (verified by an independent full `P^1(F_17)`
scan of all 18 slopes), and `(M1F3)` is among them as a `zeta`-shift.
**This reproduces the PROVED node exactly, by a disjoint route.**

### The new fact: the fence is a `q = 17` artifact

| `q` | `16 \| q-1` | configurations (full orbit) |
|---|---|---|
| **17** | yes | **16** |
| 97 | yes | **0** |
| 113 | yes | **0** |
| 193 | yes | **0** |
| 241 | yes | **0** |
| 257 | yes | **0** |
| 337 | yes | **0** |
| 353 | yes | **0** |
| 401 | yes | **0** |
| 433 | yes | **0** |

Each row is an exhaustive census (same 10,010 x 120 sweep), ~2.7 s per
field. `q = 17` is the unique admissible field with `D = F_q^*` (the whole
multiplicative group); at every other admissible `q`, `D = mu_16` is a
proper subgroup. This matches — and upgrades from sampled to exhaustive —
round 29's `RIG = -1` decay measurement ("`0.0938` non-pencil families per
random `W` at `q=17`, `0.0000` at `q ∈ {97,113,193,241,65537}`",
`collinearity_object/REPORT.md:29`): the `m=1` fence **is** a `RIG = -1`
sporadic, and those die with `q`.

**Consequence for the ledger.** The fence node's conclusion
(`statement.md:58-63`) — "no argument using only root incidence,
core-freeness, split fibers, or the Hankel equations can close the
official endpoint **uniformly in `m`**" — can be sharpened to
**"uniformly in `(m,q)`"**: a `q`-hypothesis alone (`q >= 97`, or
`D != F_q^*`) already removes the only banked witness. The official
territory is `q ∈ [2^167, 2^167+2^129)`. *(Scope: ten fields, all
`<= 433`. This is a measurement, not a theorem; see zero-power 3.)*

### On the brief's parenthetical

"the ONLY admissible field forcing `m = 1`" inverts the implication.
`q = 17` **forces** `m = 1` (`N = 16m | q-1 = 16`), which is
`collinearity_object/REPORT.md:29`'s reading; but `m = 1` does not force
`q = 17` — `16 | q-1` holds at `q = 97, 113, 193, 241, ...` too. That is
precisely why the ladder above was worth running.

---

## D3 — THE LEDGER RECONCILIATION

All integers recomputed in `d3_ledger.py`, not copied.

### The two budgets and the `q`-axis

`B*(q) = floor(q/2^128)`; budget `b` is met exactly when `q >= 2^128 b`.

| region | `q` range | `B*(q)` | meaning |
|---|---|---|---|
| **S1** sliver | `[2^167, 2^167+2^128)` | `549755813888 = 2^39` | only budget 1 available |
| **S2** | `[2^167+2^128, 2^167+2^129)` | `549755813889 = 2^39+1` | budget 2 available |
| **S3** | `[2^167+2^129, 2^256)` | `>= 2^39+2` | above the residual budget set |

`S1 ∪ S2 = [2^167, 2^167+2^129)` is exactly `(RPFC1)`'s territory
(`background/nodes/rate_half_residual_prime_field_collapse/statement.md:11-20`,
PROVED), i.e. the **only** part of the pose `(2^167, 2^256)` on which
"`q` prime" is a theorem — a fraction `2^-127` of the pose
(`rh_e_axis_audit/REPORT.md` §1). `S1` is exactly half of the RPFC
territory and `2^-128` of the pose.

### The `w*`-axis: the window splits into four pieces, exactly

Window `[4m+2, 8m-2] = [549755813890, 1099511627774]`, width
`549755813885`.

| piece | range | width | share | status |
|---|---|---|---|---|
| `(AO1)` closed | `[549755813890 .. 733007751850]` | `183251937961` | `-> 1/3` | **PROVED** (apolar, `O <= m-2`) |
| **residual (i)** | `[733007751851 .. 733007751851]` | `1` | one integer | **OPEN**, incidence-fenced (D1c) |
| **residual (ii)** | `[733007751852 .. 962072674303]` | `229064922452` | `-> 5/12` | **OPEN**, `9/4`, incidence-fenced (wave-57) |
| dead by `(NEWCAP)` | `[962072674304 .. 1099511627774]` | `137438953471` | `-> 1/4` | **DEAD** (round 31, conditional on `(SAT3)`) |

Widths sum to `549755813885` exactly. `a = 8m-2` (where the old `5.04e22`
was evaluated) is inside the dead piece and is separately **vacuous** for
`m >= 2` (`crossing_location/statement.md:583-587`).

### The budget x region table

| budget | region | what is PROVED | what is OPEN | what is DEAD |
|---|---|---|---|---|
| `2^39` (`rho+1`) | `S1` (`B* = 2^39`), far-CA side, `a = 3n/4` | — | — | **DEAD by LB1**: `B_ca^far(3n/4) >= n-a+1 = 549755813889 = 2^39+1`, exceeding the budget by exactly `1` (`rh_overlap_cap/REPORT.md:21`; `crossing_location/statement.md:653-654`) |
| `2^39` | `S1`, far-CA side, `a = k+2^34` | `B_ca^far(k+2^34) >= 1082331758593 = 2^39.9773` (LB1), i.e. **88.02 bits** under the `2^128` budget | the upper bound at the safe index (R-UPPERBOUND) | the T3/Fisher closure route (`crossing_location/statement.md:640-643`) |
| `2^39` | `S1`, apolar/type-2 side | `w* ∈ [4m+2, 733007751850]` closed by `(AO1)`; `w* > 7m-1` dead by `(NEWCAP)`; structured collinear families capped at `M <= m+1` | **`w* = 733007751851` (residual (i)) and `w* ∈ [733007751852, 962072674303]` (residual (ii))** | `a = 8m-2` vacuous for `m >= 2` |
| `2^39+1` (`rho+2`) | `S2`, `S3` | budget met by `B*(q)` for all `q >= 2^167+2^128` | same two `w*` residuals — the type-2 side does not distinguish the budgets: `(AO1)` at `a*` returns `rho+2`, one slope over `rho+1` | — |
| both | `m = 1` row | the `T = rho+2 = 5` configuration EXISTS (16 of them) at `q = 17` — PROVED counterexample | nothing | **`m = 1` is retired as a residual**; and it is empty at `q ∈ {97,...,433}` (this round) |

**Reading of the table.** Every open cell reduces to the same two `w*`
residuals, and both of those are now fenced against incidence-only
arguments. The far-CA side contributes one **dead** cell (budget `2^39`
at the bracket top) which the type-2 side does not know about — LB1 and
`(OV)`/`(NEWCAP)` live on different objects
(`rh_overlap_cap/FABLE_AUDIT.md:78-81`) and neither implies the other.

### A precision nit on `9/4`

`crossing_location/statement.md:579` reads "**residual factor 9/4
exactly**". Exactly:

```
a_max = 7m-1              cap = floor((N-a)m/s) = 9m-17 = 1236950581231
AO1   = cap + 2 = 9m-15 = 1236950581233        rho+1 = 4m = 549755813888
ratio = (9m-15)/(4m) = 9/4 - 15/(4m) = 2.249999999973  (9/4 - 2.728e-11)
```

The banked **integers** are right to the digit; the **ratio** is `9/4`
asymptotically and is strictly below it. Same class of nit as round 29's
"`4 - 7.28e-12` (`4.000000` to six decimals, **not exactly 4**)".

---

## D4 — THE T3-GUARD SKIP FRACTION

Escape replay first: the scratch copy of
`notes/pilots_20260810/list_profile_bound/d2_sunflower.py`
(md5 `b0273c8a365fea7ce93575c2a734aca5`, verified against the original,
original never executed in place) reproduces **identically**:
`{5: 5842, 6: 7990, 7: 8000}` = **21,832** column-far configurations,
`M_max = 17 / 7 / 2`, **0 violations**.

Instrumented (counters only; no original logic altered):

```
total column-far configurations : 21832
T3 test ACTUALLY APPLIED        : 2314
T3 test SKIPPED                 : 19518
SKIP FRACTION                   : 19518/21832 = 0.894009
```

| `a` | total | skipped (`M<2`) | reached guard | guard passed | guard failed | test fired | `a^2/n` |
|---|---|---|---|---|---|---|---|
| 5 | 5842 | 0 | 5842 | **0** | 5842 | 0 | 3.1250 |
| 6 | 7990 | 3564 | 4426 | 2306 | 2120 | 0 | 4.5000 |
| 7 | 8000 | 7992 | 8 | 8 | 0 | 0 | 6.1250 |

The inference at `crossing_location/statement.md:660-663` is **confirmed
and is stronger than it was stated**:

- At `a = 5` the guard passes **0 times out of 5842**: `theta = 4` in
  every single configuration and `4 * 8 = 32 >= 25 = a^2`. T3 is
  **100% vacuous at `a = 5`** — the cell whose observed `M_max = 17`
  most exceeds `n-a+1 = 4`, i.e. exactly where a cap is needed.
- At `a = 7`, `7992/8000` configurations never reach the guard at all
  (`M < 2`), and on the 8 that do, `bound = 8.0` against `M = 2` —
  margin `6`, pure slack.
- The **only** non-vacuous content in the whole census is at `a = 6`:
  2306 applications, all with `theta = 4` and `bound = 4.0`, of which
  **19 have `M = 4 = bound` exactly** (margin `0.0000`). So T3 is
  exercised at equality on `19/21832 = 0.087%` of the census and is
  slack or absent on the rest.

Registered blind: `0.85`, window `[0.55, 0.99]`, qualitative call
"largely vacuous" at `P = 0.75`. **Measured `0.894009` — HIT**, and the
`P = 0.20` sub-branch "exactly 1.0000" resolved NO.

---

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| R1a | `P(residual (i) closes) = 0.25` | **resolved NO** (registered miss-likely); the 0.92 branch "name the gap exactly" **HIT** |
| R1b | `P(m=1 closes by exhaustion) = 0.45`; feasible `0.80`; empty `0.30`; "vacuous for the prize" `0.55` | feasible **HIT** (2.7 s/field); empty **MISS at `q=17`** (16 witnesses), **HIT at 9 other fields**; "vacuous for the prize" **resolved YES** |
| R1c | skip fraction `0.85`, window `[0.55,0.99]`; vacuous `0.75`; `P(=1.0) = 0.20` | **HIT `0.894009`**; vacuous **HIT**; `=1.0` **NO** |
| P1 | AO1 closes `a <= (16m-2)/3`, T4 from `(16m+4)/3`, single gap at `m ≡ 2 mod 3` | **HIT at the official profile**; the closed form for `a_max` fails at `m = 5, 8` |
| P2 | gap size a function of `m mod 3`; **2** at `m ≡ 0`; round 29 never tested `m ≡ 0` | **DOUBLE MISS** — it is 1 at `m ≡ 0`, and round 29 did test it (miss 1) |
| P3 | official gap `= (2^41+1)/3 = 733007751851` | **HIT exact** |
| P4 | `AO1(a*) = rho+2`, `CAP = 4m-2`, `T1cap = 3`; `AO1(a*-1) = rho+1` | **HIT exact, all four** |
| P5 | `2s-(a-1) = 2`, so `RIG = -3`, difference `sigma_W * (quadratic)` | **PARTIAL MISS** — `2s = a*+1`, `RIG = -2`, difference `sigma_W * (linear)` |
| P6 | a one-unit spend-floor gain closes it; needed floor `< s+1` | **HIT** — needed `s + (7m+4)/(12m-6)`, excess `<= (7m+4)/3`, min-weight count `>= (5m-10)/3` |
| P7 | `(NEWCAP)` does not remove the gap; required strengthening `21/16` | **HIT exact** |
| P8 | exhaustion completes under `RAMGUARD_TIMEOUT=290` | **HIT** (2.7 s) |
| P9 | matching groups `> 0` at `q=17` (0.70); `(M1F3)` among them (0.55) | **HIT / HIT** (as a `zeta`-shift) |
| P10 | `q=17` is not the only field with `m=1`; the brief's phrasing needs checking | **HIT** — the implication is `q=17 => m=1`, not the converse |
| P11 | LB1 gives at least one DEAD cell (0.6); table 4-12 rows | **HIT** — budget `2^39` dead at `a = 3n/4`; table has 5 rows |
| P12 | at least one cross-round inconsistency (0.5) | **HIT, three**: the `m=8` gap (2 not 1-or-3), the "`9/4` exactly" ratio, and the banded-interval notation that hides the hole |

---

## ZERO-POWER DECLARATIONS

1. **Everything in D1 inherits `(AO1)`, `(SAT1)-(SAT4)` and T4's
   hypothesis wholesale.** It is exact integer arithmetic *on those
   formulas*; it has zero power over whether the formulas are right.
   If `(AO1)`'s third term or the `(C2)` spend floor is wrong, the whole
   gap analysis moves with it.
2. **The `m = 2` incidence fence is ONE scale.** The wave-57 node made a
   point of exhibiting its counterexample at `m = 64` so it could not be
   dismissed as a small-scale anomaly; mine is at `m = 2`. For
   `m = 8, 32, 2^37` I have only integer feasibility of the necessary
   conditions, which proves nothing about existence.
3. **The `q`-ladder in D2 is ten fields, all `<= 433`.** "The `m=1`
   failure exists only at `q=17`" is a measurement over that ladder, not
   a theorem, and it has **zero power** over the official territory
   `q ∈ [2^167, 2^167+2^129)` except by analogy. It also has zero power
   over `m >= 2`: `m=1` and the official profile are different rows.
4. **Closing or retiring `m = 1` moves NEITHER budget.** The official
   profile is `m = 2^37`; no instrument in this stack is inductive in
   `m`. Residual (iii)'s retirement is bookkeeping, not progress on the
   budgets, and I state that against my own D2.
5. **The T3 skip fraction is a property of one census's configuration
   grid**, not of the mathematics. A high skip fraction weakens that
   census's validation of T3 and nothing else; T3's own status is
   already settled elsewhere (`crossing_location/statement.md:640-643`,
   the route is dead on the whole bracket).
6. **D1.5's "T4's conclusion would close it with 5/3 of room" is
   conditional on the collinearity transport**, which I could not verify
   at `a*` (miss 10). If that transport needs `S_gamma ∩ W = {}`, the
   sentence is void.
7. **Round 29's "`F_COLL = s+1` down to `RIG = -6`" is sampled**
   (`N ∈ {16,32}`, 64 random `W` per cell). It makes `RIG = -2` look
   safe; it is not evidence, and I give it no theorem status anywhere
   above.
8. **No claim here decays in `q`** except D2's, which is explicitly a
   `q`-ladder measurement.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, R=8m, R1=R+1, rho=4m-1, e=m, delta=m-1, A=3`;
`a = w*`, `s = R1-a`, `RIG = a-1-2s`; `T1cap(m,a,O)`, `CAP(m,a)`,
`AO1 = T1cap+CAP`; `j(a) = floor(a/(a-rho))` and its divisor blocks
(new here — the vehicle for the exhaustive hole certificate);
`a_max(m)` = top of the `(AO1)` closure band; `thr(m) = ceil((16m+3)/3)`;
`GAP(m,O)` = the complete uncovered set; `d_x`, `O = sum o_gamma`,
`p_gamma = |S_gamma \ W|`, `eps_gamma = p_gamma - s` (new label for
round 31's `j` under `n_0 = 0`); `#{min-weight type-2}`;
`sum_x C(d_x,2)`, `Lmin(O)`; `sigma_S(x)`, `sigma'_Z(x)` and the
normalized restrictions used as the `m=1` matching key (new);
`B*(q) = floor(q/2^128)`; T3's `theta`, guard `theta*n < a*a`, bound
`(a-theta)/(a^2/n - theta)`, and the **skip fraction** (new).
Registered but **not measured**: the collinearity transport of T4 at
`a*` (miss 10) — declared, not dressed up.

---

## COMPLIANCE

**Registrations.** R0-R7 (notation, the three blind priors the brief
demands, the gap arithmetic P1-P7 computed in-head and registered as
predictions, the `m=1` search design R3 with P8-P10, the D3 predictions
P11-P12, route order, eight zero-power declarations, compliance plan)
were appended to `PREREG.md` with the **Edit tool after reading exactly
the two named anchors and before any other read, any grep, any `ls`, and
any interpreter invocation**. No post-registration addenda.

**Compute law.** **Twenty interpreter invocations**, every one of the
form `tools/ramguard tiny|local -- python3 ...` from the repo root with
the literal `--` and an explicit `RAMGUARD_TIMEOUT`: `tiny` x7
(`RAMGUARD_TIMEOUT=120` each: five `d1_gap.py` runs, `d1c_fence.py`,
`d3_ledger.py`) and `local` x13 (`RAMGUARD_TIMEOUT=290` each:
`d1b_holes.py`, ten `d2_m1.py` field runs, the `d4_sunflower_scratch.py`
replay, `d4_skip.py`). **Ramguard status: no invocation was killed by the
guard; three exited non-zero on my own bugs and one of those was
guard-induced** — invocation 2 raised `MemoryError` under the `tiny`
256M profile while trying to enumerate the `5.5e11`-value window at
`m = 2^37` (the same failure mode round 31 reported); I replaced the
enumeration with a binary search and then with the divisor-block
certificate rather than raising the profile. The other two failures were
a `TypeError` and an `AssertionError`, both my own, both fixed.
**Disclosed deviation:** the seven `tiny` runs carried
`RAMGUARD_TIMEOUT=120` against the profile's nominal 60 s; the env var is
a documented ramguard feature (`tools/ramguard` usage text) and every one
of those runs finished in seconds, but I flag it exactly as round 31 did.
No bare `python3` at any point. Stdlib only; no third-party imports, no
Modal, no network, no git.

**RAM discipline.** `dag.json` **never opened** (node shards + `sed`
ranges + grep only); file-at-a-time reads with explicit line ranges on
every large file; the `m = 2^37` window never materialised (divisor
blocks, `1,482,906` of them, `O(1)` memory); the ten `m=1` field censuses
were run as ten separate checkpointed invocations each writing its own
results file.

**Quarantine — ONE BREACH, disclosed (miss 11).** A single recursive grep
for "wave-57" rooted at `notes/` **surfaced four lines of
`notes/pilots_20260802/CAMPAIGN_LEDGER.md`** to me. No content from those
lines is used anywhere in this report; every subsequent grep carried
`--exclude-dir=pilots_20260802` together with `rh_fr_algebraic`,
`rh_farca_upper`, `rh_haboeck_seam` and `rh_residuals_close`. The three
**round-32 sibling directories were never read and never listed**; no
`ls` of `notes/pilots_20260810/` was run. (I did see one *heading* naming
a round-32 sibling while reading `critical/nodes/rate_half_band_crossing_location/statement.md`
at line ~795, and stopped reading there; that file is a critical node,
not a sibling directory.) Round-31 and round-29 pilot directories were
read as the brief permits (`rh_overlap_cap`, `rh_e_axis_audit`,
`list_profile_bound`, `apolar_origin`, `collinearity_object`). No path
containing `prize-codex-` was touched. **No subagents were spawned**, so
the propagation clause was not needed.

**Write scope.** Every write is inside
`notes/pilots_20260810/rh_residuals_close/`: `PREREG.md` (registrations
appended), `d1_gap.py` + `d1_gap_results.txt`, `d1b_holes.py` +
`d1b_holes_results.txt`, `d1c_fence.py` + `d1c_fence_results.txt`,
`d2_m1.py` + ten `d2_m1_q*.txt`, `d3_ledger.py` +
`d3_ledger_results.txt`, `d4_sunflower_scratch.py` (byte-identical copy)
+ `d4_replay_results.txt`, `d4_skip.py` + `d4_skip_results.txt`, and this
`REPORT.md`. **No** `dag/`, `nodes/`, `critical/`, `background/` or
`tools/` edits; **no git operations of any kind**; the session scratchpad
was not used.

**Banked scripts.** `d2_sunflower.py` was copied into my directory and
**md5-verified against the original** (`b0273c8a365fea7ce93575c2a734aca5`,
identical) before running; the original was never executed in place and
never modified. The unmodified copy reproduced round 29's numbers
**identically** (`21,832 / 0 violations / M_max 17,7,2`); the
instrumented copy adds counters only. `d1_gap.py`, `d1b_holes.py`,
`d1c_fence.py`, `d2_m1.py`, `d3_ledger.py` are mine, written from
scratch.

**Method discipline.** CATCH-24A own-repo greps were run **before** every
novelty claim and produced the subtraction table above, including the one
that mattered most (the `m=1` exhaustion is a PROVED node, so my D2 is a
replay). Every quantifier claim carries a `file:line`. Every
max-quantified or sampled claim carries a zero-power declaration. Two of
this round's three self-corrections (the mislabelled feasibility check,
the `2^89` print artifact) are reported as mislabels in my own results
files rather than silently repaired, per the round-29 precedent, and the
one accusation I registered against an anchor is **withdrawn as false**
in miss 1.
