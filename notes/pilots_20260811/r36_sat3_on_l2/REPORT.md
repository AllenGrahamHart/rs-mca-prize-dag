All four deliverables executed, four clean ramguard runs. Here is the full REPORT text.

---

# REPORT — r36_sat3_on_l2 (round 36)

## VERDICT (first)

**THE (SAT3) LAYER IS NO LONGER VACUOUS AT `m = 2`. `T >= 1` IS ACHIEVED — AND `T = 2` OVER THE REAL DOMAIN `mu_32`, BY EXACT CONSTRUCTION, ON CERTIFIED `e = m = 2` OBJECTS, ON TWO FIELDS.** The round's T-record is `T = 2` over `mu_32` (both supported slopes made **finite**, `{0,1}`, by Möbius normalisation) and `T = 3` over a bespoke 32-set (37 instances at `q=97`, 89 at `q=193`). Round 35 measured `T = 0` on all twelve of its witnesses and its designed-domain instrument ran with **zero input** (`r35_l2_gate/REPORT.md:32`); that instrument now has input.

The route was **not** a search. I found a **closed-form rational parametrization of the entire `(L2)` stratum at `m = 2`**:

```text
L*Q_0 = f^2 - kg ,   L*Q_1 = fg + hk ,   L*Q_2 = g^2 + hf
        <=>   L*Q_z = det( [[f, k],[g, f]] + z*[[g, f],[-h, g]] )
```
with `deg f,g,h,k <= 4`, `L` linear with root `ell`, subject to **exactly two conditions at the single point `ell`**: `f(ell)^2 = k(ell)g(ell)` and `g(ell)^2 = -h(ell)f(ell)` (the third, `f(ell)g(ell) = -h(ell)k(ell)`, is implied except where `f(ell)=g(ell)=0`). Both directions are four lines of algebra, and the converse substitution kills `E1` and `E2` **identically**. Consequences, in order of what they change:

1. **The hit rate goes from `1/q` to `1`.** Anchor 1's inversion needed `det M(B) = 0`, one condition, rate `0.0179`/`0.0047` (`r35_l2_gate/REPORT.md:13`). Mine solves that condition in closed form: pick `ell`, pick `f,g,h` freely, set one coefficient of `k` and one of `h`. **266,239 objects at `q=97` and 167,421 at `q=193` in 95 s each** (`d3_results.txt:26,37`). That is another factor `q` on top of anchor 1's `q^4`, i.e. `q^5` over blind search.
2. **Prescription is free on one member.** Because `Q_0 = (f^2-kg)/L`, prescribing `Q_0 = prod_{a in S_0}(x-a)` with `S_0 ⊂ mu_32` reduces to a **square root mod `g`** — so `T >= 1` over the true multiplicative domain is achieved **by construction, not by search** (12 certified objects, `d1_results.txt:23,35,37,39,51,53`).
3. **`T = 2` over `mu_32` is an exact algebraic solve, not a lottery.** Prescribing `Q_2` too becomes `L*Q_2 == g^2 (mod f)`, solved **exactly over all `C(32,7) = 3,365,856` subsets** by meet-in-the-middle in `F_q[x]/(f)`: 46 solutions in 10 configurations at `q=97`, 13 in 22 at `q=193`, of which 4 and 1 survive `s = 0` (`d2_results.txt:10-12,36-38`).
4. **`det M(B) = 0` is a resultant.** `det M(B) = 0` **iff** `f^2-kg`, `fg+hk`, `g^2+hf` have a common root in `P^1` — verified **1200/1200** on random `B`, two fields, with no exceptions in either direction (`d3_results.txt:64-65`). A `24 x 24` determinant is replaced by one gcd of three degree-8 polynomials. **This is the round's fourth instrument in the D3 sense.**
5. **The banked instrument that predicted `m=2` REALIZABLE flips sign.** `rh_sat3_realizability/REPORT.md:193-198` prices `(SAT3)` with `excess(m) = 12m^2-24m-1-O`, negative **only** at `m in {1,2}` (`-13`, `-1`), and conjectures on that basis that "`(SAT3)` is realizable exactly for `m <= 2`" (`:200`). Its parameter count uses the **ambient** curve dimension `4m(m+1)-1 = 23`. But `(ERC2)` (**PROVED**, `rate_half_ca_hankel_exceptional_root_charge/statement.md:3,73`) closes `1 <= e <= m-1`, so `(SAT3)` **forces** `e = m`, i.e. the curve must lie on the `(L2)` good component, of dimension **18** — anchor 1's measurement (`r35_l2_gate/REPORT.md:131`), re-derived independently here (`d1_results.txt:16-17`). Correcting `23 -> 18`: `params 64 -> 59`, `excess = +4 - O`, i.e. **`+4` at `O=0` and `+3` at `O=1`** (`d4_results.txt`, section B). **The banked ledger's only negative cell at `m >= 2` becomes positive.**

**What did NOT happen: no `T = rho+2 = 9`, no `T >= 4` at all, no `T >= 3` over `mu_32`, no emptiness theorem, no `m >= 3`, and no statement at `q ~ 2^128`.** And the wall I hit at `T = 3` is **algorithmic, not arithmetic**: the corrected first moment is `+62.5` bits at `T=3` **at every field tested** (`d4_results.txt:9,12,15,18,21`), so `T=3` objects over `mu_32` are abundant and I simply have no third exact solve.

---

## MISSES FIRST

1. **MY T-RECORD IS NOT A CAMPAIGN T-RECORD, AND I NEARLY SHIPPED IT AS ONE.** `rh_sat3_realizability/REPORT.md:52` reports **`T = 4` at `m = 2,3,4`, two fields each**, and `rh_psi_degree/d3_m2_q97.txt:73` and `d3_m2_q193.txt:73` both print "`max T over pencils = 3 (rho+2 = 9)`". My `T = 2` over `mu_32` is **below both**. What is new is the **class**: every one of those banked objects has `e = 1` (`rh_sat3_realizability/REPORT.md:50`), which `(ERC2)` already closes (`exceptional_root_charge/statement.md:73`, PROVED), and `rh_psi_degree`'s census does not certify `e` at all. **My claim is therefore only: the first `T >= 1` on an object certified `e = m = 2` — the sole class `(SAT3)` can inhabit.** Stated first, before any number.
2. **(QPACK) — MY REGISTERED (X6) — IS BANKED VERBATIM, AND SO IS ITS CONSEQUENCE.** `saturation_rigidity/statement.md:49-50` reads "Every `Q_Z(x)` is a nonzero parameter polynomial of degree at most `m`, so `d_x<=m`", i.e. my derivation word for word; `(SAT4)` `sum_x(m-d_x)=1+O<=m` is `:53`; `(SAT5)` is `:59`; and "at every such point … all its parameter roots are distinct finite members of `Z`" — my packing consequence — is `:62-65`. **P14 fired at 0.80 and it was right.** My `7T <= 2|D| = 64 => T <= 9` is banked arithmetic, not a discovery.
3. **MY REGISTERED LEDGER (X4)/(X5) DOUBLE-COUNTED `PGL_2` AND WAS WRONG BY `3 log2 q`.** I registered `expected dim{T>=t} = 15-6t` and `log2 E = 15 log2 q + ...`, quotienting by `PGL_2` **and** still counting the slope set freely. The correct exponent is `18-6T`; the correct ledger is `18 log2 q + log2 C(q+1,T) + T[log2 C(32,7) - 7 log2 q]`, giving `-61.34` at `T=9,q=97`, not my registered `-81.1`. **R7(c) pre-registered exactly this failure mode and it fired.** The corrected gap to anchor 2 is `2 log2 q = 13.20` bits, **not** the 33 I registered — and it reproduces `-48.14` exactly at all five fields (`d4_results.txt:10,13,16,19,22`).
4. **THE D3 MECHANISM I INTENDED TO NAME IS BANKED, IN MORE DETAIL THAN I HAD IT.** `rh_sat3_realizability/REPORT.md:206` already states the `m=2` `(SAT3)` design as "a 9-vertex multigraph of 31 edges with degrees `7^8, 6` (**this design exists**)" plus, per edge, a point `x` with `c_1(x) = -(a+b)c_2(x)`, `c_0(x) = ab c_2(x)` — which is precisely my packing/eigenvalue picture. My addition is only (i) that those edges are the **generalized eigenvalues of the `2x2` pencil** `P(x)+zR(x)`, and (ii) the measured occupancy. **Not a new mechanism.**
5. **`T = 2` OVER `mu_32` USES `z = 0` AND `z = infinity`, AND I HAD TO NORMALISE TO DEFEND IT.** Raw, the doubly-prescribed witnesses have `T_fin = 1` and `T_P1 = 2` (`d2_results.txt:31,56`). I pre-registered Z9 to headline the smaller. I then applied `Z = W/(1-W)` (`y_0' = y_0`, `y_1' = y_1-y_0`, `Q'_0=Q_0`, `Q'_1=Q_1-2Q_0`, `Q'_2=Q_0-Q_1+Q_2`) and **re-certified from scratch**: supported finite slopes `{0,1}`, both fields (`d3_results.txt:12-13,19-20`). The claim is safe, but it required a step I had not registered.
6. **MY `T = 3` IS OVER A BESPOKE 32-SET AND HAS ZERO POWER FOR `(SAT3)`.** Z1 was registered in advance and I hold to it: `T=3` objects have `T = 1` over `mu_32` (`d3_results.txt:36,47`). The endpoint's domain is `mu_N`; a designed non-multiplicative set is a **relaxation**, and I do not merge the columns anywhere.
7. **PART A's IDENTITY TEST RAN ON 5 AND 1 SAMPLES.** Random `B` yields a linear `L` only at rate `~1/q`, so the direct `E1&E2 == 0` check saw `5/5` and `1/1` (`d1_results.txt:6,10`) — a **tiny** sample. The load-bearing evidence is elsewhere: 80 objects with `nullity M(B) = 1` (`d1_results.txt:16-17`), 1200/1200 on the refined criterion (`d3_results.txt:64-65`), and the algebra itself.
8. **9 OF EVERY 10 EXACT `mu_32` SOLUTIONS ARE DEGENERATE AND I CANNOT PREDICT WHICH.** Of 46 exact `S_2` solutions at `q=97`, 42 are rejected with `s in {1,2,3,4}` in a rigid pattern — `s=k` gives `nullity = 2k`, `generic rank = k`, `deg<=1 kernel = 16-2k` (`d2_results.txt:13-16`). I report the pattern; I have no criterion that predicts `s=0` in advance, so the yield is empirical.
9. **THE MEASURED SPLIT RATE UNDERSHOOTS MY REGISTERED (X8) BY 15-27%.** Predicted `q/7! = 0.0192`/`0.0383`, measured `0.0141`/`0.0332` (`d3_results.txt:27,38`). Inside my registered 3x falsifier, so (X8) stands, but the deficit is real and unexplained.
10. **I DID NOT ATTEMPT `T = 3` OVER `mu_32`, AND THE COUNT SAYS IT IS THERE.** `log2 E(T=3) = +62.5` at `q = 97, 193, 257, 641, 769` — **the `T=3` cell is exactly `q`-independent** (the exponent `18-6T` vanishes at `T=3`). So absence of `T=3` over `mu_32` in this round is **absence where none was sought**, not evidence.
11. **NO `(SAT2)/(SAT4)/(SAT5)` TABLE.** At `T = 2` the deficit identity is not in force (`(SAT4)` is stated under `(SAT3)`, `statement.md:50`). Measured instead: `sum_x d_x = 14` over the two supported slopes with histogram `{0:18, 1:14}` (`d2_results.txt:32,57`) — i.e. **no domain point is doubled yet**, against the 31-of-32 that `(SAT3)` demands. I report that rather than printing a vacuous table.
12. **F1/(NEWCAP) IS STILL AT ZERO POWER.** With `T = 2` there is exactly **one** supported pair, so `a* = w* = |S_0 u S_2|` is a single number (`14`, since `|S_0 ∩ S_2| = 0`, `d2_results.txt:21,46`) — a one-sample statistic, not a minimum over a family. `7m-1 = 13 < 14`. **This does not test F1.**

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every recursive grep carried, **at the search level**, `--exclude-dir=r36_lawcount_geom --exclude-dir=r36_hrlow --exclude-dir=r36_m4_nonsplit --exclude-dir=pilots_20260802 --exclude-dir=prize-codex-1 --exclude-dir=prize-codex-2 --exclude-dir=prize-codex-3 --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json`, over `background/`, `critical/`, `notes/`. Hyphenated and infixed variants were searched explicitly (`value confinement`/`value-confinement`/`flat supply`/`flat-supply`; `designed domain`/`designed-domain`/`bespoke`; `determinantal representation`/`determinantal-representation`/`adjugate`; `rational parametriz`/`parametris`/`rationally parametriz`; `d_x <= m`/`d_x<=m`/`d_x \le m`; `f^2 - kg`/`f^2-kg`/`g^2+hf`/`fg+hk`).

| object | in-repo prior | verdict |
|---|---|---|
| **`d_x <= m`; `7T <= 2\|D\|`; `T <= rho+2`; the near-perfect double packing** (my registered (X6)) | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:49-50` (`d_x<=m`, same one-line proof), `:53` `(SAT4)`, `:59` `(SAT5)`, `:62-65` (roots distinct finite members of `Z`) | **BANKED VERBATIM. Not mine.** MISS 2. |
| **the `m=2` (SAT3) design as a 9-vertex 31-edge multigraph with per-edge point conditions** | `notes/pilots_20260811/rh_sat3_realizability/REPORT.md:206` ("this design exists — `K_9` minus a 2-path and 3 disjoint edges") | **BANKED, and in more detail than I had it.** MISS 4. My addition: it is the generalized-eigenvalue structure of a `2x2` pencil. |
| **`(SAT3)` forces `e = m`** | `background/nodes/rate_half_ca_hankel_exceptional_root_charge/statement.md:3` (**PROVED**), `:21` `(ERC2)`, `:73` ("this entire parameter-degree range is closed") | **BANKED AND PROVED.** It is the hinge of my D3 correction, quoted not derived. |
| **the `(SAT3)` realizability ledger `excess = 12m^2-24m-1-O` and the `m<=2` conjecture** | `rh_sat3_realizability/REPORT.md:193-198`, `:200` | **banked.** New here: it uses the **ambient** `4m(m+1)-1 = 23` where `(ERC2)` forces the `(L2)` component's **18**; the corrected `m=2` cell is `+4-O`, not `-1-O`. |
| `T = 4` at `m=2,3,4`; `max T over pencils = 3` at `m=2` | `rh_sat3_realizability/REPORT.md:52`; `rh_psi_degree/d3_m2_q97.txt:73`, `d3_m2_q193.txt:73` | **BANKED AND HIGHER THAN MY RECORD** — but at `e=1` (`:50`) or with `e` uncertified. MISS 1. |
| the `C(16m,4m-1)` first-moment gate and its `m=1` double calibration | `r35_rout_layer_a/REPORT.md:25`, `:242`, `:258-263` | **banked — it is anchor 2's, explicitly not mine.** I change one input (`20 -> 18`) and re-derive `-48.14 - 2 log2 q`. |
| `det M(B)=0` as the `(L2)` existence condition; the `24x24` squareness; good component dim 18 | `r35_l2_gate/REPORT.md:13,131,149` | **banked — it is my mandate's premise.** New: that condition **is a resultant**, and dim 18 falls out of `19+1-2` independently. |
| the `2x2` determinantal form `L Q_z = det(P+zR)` | greps for `adjugate`, `determinantal representation`: only `rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization` (the `A=1` lane, contracted adjugate `= lambda q q^T`) and `l1_fpc5_tpetal_joint_owner_split_pencil/statement.md:57` (a **scalar** determinantal representation, different lane/object) | **claimed new in this lane; MEDIUM confidence.** P15 registered 0.55; the near-miss nodes are `A=1` and `l1`, not `A=3`. |
| **the closed-form rational parametrization of the `(L2)` stratum** (`L Q_0 = f^2-kg`, …, two conditions at `ell`) | greps for `rational parametriz`/`parametris`/`f^2-kg`/`g^2+hf`/`fg+hk` over `background/`, `critical/`, `notes/`: **zero hits** (only two audit lines warning that structure is *not* a rational parametrization) | **claimed new.** |
| **`det M(B)=0 <=> gcd(f^2-kg, fg+hk, g^2+hf) != 1`** | same greps; `r35_l2_gate` states the determinant, never a resultant form | **claimed new.** Verified 1200/1200, two fields. |
| "value-confinement / flat supply" as the named wall | `critical/nodes/rate_half_band_crossing_location/statement.md:3303,3688,3862`; `r35_bivcurve_m4/REPORT.md:5,291` | **banked as the `(BIV-CURVE)`-lane law.** My round did **not** hit it (see D3); I do not claim it. |
| the designed-domain question having zero input | `r35_l2_gate/REPORT.md:32`, `:281` | **banked as an open miss.** This round supplies the input. |

---

## D1 — THE `B -> SPLITTING` MAP, STRUCTURED

### D1.1 The parametrization (registered as (X1); verified)

Eliminating between anchor 1's `E1: Q_2f-Q_1g-Q_0h=0`, `E2: Q_1f-Q_0g-Q_2k=0`: multiply `E1` by `f` and substitute `E2` to get `Q_2(f^2-kg) = Q_0(g^2+hf)`. With `gcd(Q_0,Q_2)=1` and `deg Q_0 = 7`, `deg(f^2-kg) <= 8`, this forces `f^2-kg = Q_0 L` with `deg L <= 1`, then `g^2+hf = Q_2 L`, then (from `E1`, dividing by `g`) `fg+hk = Q_1 L`. **Converse:** substituting the three formulas into `E1` and `E2` gives `0` identically. So

> **(PAR).** With `L` linear of root `ell`, the map `(f,g,h,k,L) |-> (Q_0,Q_1,Q_2) = ((f^2-kg)/L, (fg+hk)/L, (g^2+hf)/L)` is a **birational parametrization of the `(L2)` stratum at `m=2`**, subject to exactly two conditions at `ell`. Equivalently `L Q_z = det([[f,k],[g,f]] + z[[g,f],[-h,g]])`.

Measured: `E1 & E2` identically zero `5/5` (`q=97`) and `1/1` (`q=193`) on linear-`L` draws, with `nullity(36x32) >= 1` on all of them (`d1_results.txt:6-7,10-11`); `nullity M(B) = 1` on `{(1,40)}` per field and `nullity Phi = 1` on `{(1,40)}` per field (`d1_results.txt:16-17`), so **`B -> Q` and `Q -> B` are both single-valued up to scale**.

### D1.2 Dimension (registered as (X2)) — 18, independently

`(f,g,h,k)` is 20 coordinates, `ell` adds 1, the two conditions at `ell` remove 2: **19 affine = 18 projective**, and the fibre is finite by `d1_results.txt:16-17`. **Exactly anchor 1's good-component dimension 18** (`r35_l2_gate/REPORT.md:131`), reached by a completely different route. Two-field confirmation.

### D1.3 What prescribing split locators COSTS in `B`-space — the exact ledger

- Over `mu_32`, "member `z` splits over `D`" is a **`C(32,7)`-point locus in `P^7`**: codimension 7, with a `q`-independent multiplicity `C(32,7) = 3,365,856 = 2^21.68`.
- Counting `(object, slope-set)` pairs: `log2 E(T) = 18 log2 q + log2 C(q+1,T) + T[log2 C(32,7) - 7 log2 q]`. The `log2 q` exponent is **`18 - 6T`**.

```text
 q     T=1     T=2     T=3     T=4     T=5     T=6     T=7     T=9
 97  +100.9  +82.0   +62.5   +42.5   +22.2    +1.7   -19.1   -61.3
193  +112.8  +87.9   +62.5   +36.6   +10.4   -16.1   -42.8   -96.9
257  +117.8  +90.4   +62.5   +34.1    +5.4   -23.5   -52.7  -111.7
641  +133.6  +98.3   +62.5   +26.2   -10.4   -47.3   -84.3  -159.1
769  +136.7  +99.9   +62.5   +24.6   -13.5   -52.0   -90.6  -168.5
```
(`d4_results.txt:8-22`.) **Three exact readings:**

1. **`T = 3` is the `q`-invariant cell** — `+62.5` bits at every field, because `18-6T = 0` at `T=3`. `T <= 2` grows with `q`; `T >= 4` is suppressed by `q^{6T-18}`. **The dimension threshold of the `(SAT3)`-on-`(L2)` problem sits exactly at `T = 3`**, which is where my measured record also sits.
2. **The gate is `13.20` bits sharper than anchor 2's at `q=97`** (and `2 log2 q` at every field), because the `(L2)` component has 18 dimensions where anchor 2 used the biform's `(m+1)(rho+1)-4 = 20`. Reproduces `-48.14, -81.67, -95.67, -140.41, -149.33` exactly by adding `2 log2 q` (`d4_results.txt:10,13,16,19,22`).
3. **Over a bespoke 32-set the ledger has no dimension threshold below `T=5`**: "splits over `F_q`" is a **constant** `1/7! = 1/5040`, not a codimension, so the exponent is `18+T > 0` for all `T`. The bespoke route is limited only by sampling until `7T > 32` bites at `T = 5` (my registered (X7)).

### D1.4 Where the supply must come from — the `m=1` analogue, answered

At `m=1` anchor 2's coherence was `16 = 16` (`r35_rout_layer_a/REPORT.md:25`). **The `m=2` analogue is the `ell`-fibre**: the entire obstruction to being an `(L2)` object is *two conditions at one point*, so the parametrization leaves `Q_0` (resp. `Q_2`) as a **free degree-7 form up to a square-root condition mod `g`**. That is why the supply is coherent for one member (free), still coherent for two (an exact solve with `C(32,7)/q^3 = 3.69` expected solutions per configuration at `q=97`, measured `46/10 = 4.6`; `0.47` predicted at `q=193`, measured `13/22 = 0.59` — `d2_results.txt:10,36`), and **incoherent from three on**, where I have no exact solve. My registered (X9) predicted exactly this shape and it held.

---

## D2 — THE DESIGNED SEARCH

### D2.1 Structured construction, not random draws

**Route A (one prescription, rate ~1).** `S_0 ⊂ mu_32`, `Q_0 = prod(x-a)`; pick `ell`; pick 4 points `r_j` where `L Q_0` is a nonzero square; `g = prod(x-r_j)`; `f = interp(r_j, ±sqrt(L(r_j)Q_0(r_j))) + c g`; `k = (f^2-LQ_0)/g` (degree `<= 4` automatically); `h(ell) = -g(ell)^2/f(ell)` with 4 free coefficients; `Q_2 = (g^2+hf)/L`, `Q_1 = (fg+hk)/L`. **6 of 6 attempts fully certified at `q=97`, 6 of 7 at `q=193`** (`d1_results.txt:23,39`).

**Route B (double prescription, exact).** With `Q_0`, `g`, `f`, `k` fixed, `Q_2 = beta prod_{S_2}(x-b)` requires `L Q_2 == g^2 (mod f)` — a **proportionality in the 4-dimensional ring `F_q[x]/(f)`**, i.e. 3 conditions on `C(32,7)` subsets. Solved **exactly and exhaustively** by meet-in-the-middle: split `mu_32` into halves, tabulate `nrm(v u^{-1})` on the smaller side and `nrm(u)` on the larger, for all seven size splits. No sampling; every solution is found.

### D2.2 The headline objects (reproducible, fully certified against the ORIGINAL `36x32` system)

`q = 97`, the doubly-prescribed witness (`d2_results.txt:18-33`):

```text
S_0 = [30,33,51,63,69,77,85] ⊂ mu_32      S_2 = [8,12,18,27,45,52,78] ⊂ mu_32
f=[42,3,81,6,89]  g=[71,19,15,60,1]  h=[5,40,44,0,6]  k=[24,46,52,68,63]  L=[53,1]
Q_0=[78,63,82,85,33,58,77,1]   Q_1=[75,9,93,12,8,88,15,79]   Q_2=[46,93,4,16,76,49,28,50]
y_0=[27,56,11,6,39,43,74,62,47,5,47,52,66,62,81,81]
y_1=[9,76,44,51,3,76,93,68,66,20,37,43,86,74,68,1]
```

| certified property | required | measured (`q=97` / `q=193`) |
|---|---|---|
| `deg(Q_0,Q_1,Q_2)` | `(7,7,7)` | **(7,7,7)** / **(7,7,7)** |
| separation rank `(RNC2)` | `m+1 = 3` | **3** / **3** |
| `s = deg gcd(Q_0,Q_1,Q_2)` `(SAT1)` | `0` | **0** / **0** |
| `nullity(36x32)` | `>= 1` | **1** / **1** |
| `M(Z)Q_Z = 0` entrywise, from scratch | true | **true** / **true** |
| generic rank of `M(Z)` | `rho = 7` | **7** / **7** |
| rank-drop divisor `delta = rho-3e` | one reduced point | **`z=89`, rank 6, none at infinity** / **`z=110`, rank 6, none at infinity** |
| kernel vectors of parameter degree `<= 1` | `0` (else `e < m`) | **0** / **0** |
| **minimal index `e`** | **`m = 2`** | **2** / **2** |
| **`T` over `mu_32`** | — | **2** / **2** |

Möbius-normalised to two **finite** supported slopes `{0,1}` and **re-certified from scratch** — same table, `drops z=[15]` / `z=[154]`, `deg<=1 kernel = 0` (`d3_results.txt:8-20`).

### D2.3 The bespoke-domain push

266,239 objects at `q=97` and 167,421 at `q=193`, each with `Q_0` prescribed split, `T_bespoke` counted as `#{z in P^1 : Q_z has 7 distinct F_q-roots}` (`d3_results.txt:26-47`):

```text
 q    objects   T=1      T=2    T=3   record |union of root sets| (must be <=32)
 97   266239   244063   3690     37     3     20
193   167421   156141   5386     89     3     19
```
Both records certified in full (`s=0`, nullity 1, `M(Z)Q_Z=0`, generic rank 7, one rank-6 drop, `deg<=1` kernel `0`). Both have `|union| < 21 = 3*7`, i.e. **root sharing between supported members already occurs spontaneously** — the very mechanism `(SAT4)` demands at scale. Both have `T = 1` over `mu_32` (`d3_results.txt:36,47`).

**Does the designed domain beat `mu_32`? YES, by the factor I registered.** `T >= 1`: bespoke costs `1/7! = 1/5040`, `mu_32` costs `C(32,7)/q^7 = 5.19e-8`; ratio `q^7/(7! C(32,7)) = 3.8e3` at `q=97`. Measured, `T >= 2` per object: `3727/266239 = 0.0140` bespoke versus **zero** in 120 unprescribed objects over `mu_32` (`d1_results.txt:56,58`). **P3 resolves YES.**

---

## D3 — THE OBSTRUCTION SIDE

### D3.1 No wall was hit — and that is the finding

`T = 3` over `mu_32` sits at `+62.5` bits at **every** field. So the failure to reach it is **my algorithm's**, not arithmetic's: I have exact solves for one and two prescriptions and none for three. **P4 (value-confinement) resolves NO for the range I reached** — the `(BIV-CURVE)` flat-supply law (`critical/nodes/rate_half_band_crossing_location/statement.md:3688`, `r35_bivcurve_m4/REPORT.md:5`) never engaged, because value-level supply was never the binding resource below `T = 4`.

### D3.2 The wall that the count does predict, named and measured

The ledger turns negative at `T = 7` (`q=97`) and `T = 6` (`q>=193`), and the mechanism is **concentration, not supply**. Each `x in D` carries the quadratic `q_x(z) = Q_0(x)+zQ_1(x)+z^2Q_2(x)`, whose roots are the **generalized eigenvalues of the `2x2` pencil `P(x)+zR(x)`**; `(SAT3)` demands that all 32 of those pencils have rational eigenvalues **and** that all 63 of them lie in one 9-element alphabet. Measured on 120 random `(L2)` objects per field (`d3_results.txt:53-60`):

```text
 q    slot occupancy sum_x d_x /64   #distinct slopes carrying a root   max_z #roots in mu_32
 97   mean 32.4, max 49, min 21      mean 27.7, min 17                  {1:3, 2:82, 3:31, 4:4}
193   mean 32.6, max 48, min 18      mean 30.1, min 18                  {1:13, 2:92, 3:15}
```
`(SAT3)` needs occupancy `63` concentrated on `<= 9` slopes with **every** slope at exactly 7. Random objects deliver about **half the occupancy spread over three times too many slopes**, and the best single slope reaches 4 of the 7 roots needed. **The obstruction is arithmetic eigenvalue-confinement of a `2x2` polynomial matrix pencil** — the same species as value-confinement, a different mechanism, and (MISS 4) its combinatorial shadow is already banked at `rh_sat3_realizability/REPORT.md:206`.

### D3.3 THE FOURTH INSTRUMENT — an exact constraint on `det M(B) = 0`

> **(RES).** `det M(B) = 0` **iff** `f^2-kg`, `fg+hk`, `g^2+hf` have a common root in `P^1(F_q)` (the point at infinity counting as "all three of degree `<= 7`").

Verified **1200/1200**, two fields, joint histogram `[((False,False),594),((True,True),6)]` at `q=97` and `[((False,False),596),((True,True),4)]` at `q=193` (`d3_results.txt:64-65`). The naive two-condition form (`f(ell)^2=k(ell)g(ell)`, `g(ell)^2=-h(ell)f(ell)`) is **not** sufficient: it fails exactly when `f(ell)=g(ell)=0`, which my first pass measured as 5 false positives at `q=97` (`d1_results.txt:9`) before I refined it — a self-caught error, reported.

### D3.4 The instrument that changes the board: the banked ledger's `m=2` cell flips

`(ERC2)` is **PROVED** and closes `1 <= e <= m-1` (`exceptional_root_charge/statement.md:3,73`), so `(SAT3)` forces `e = m` and the curve must lie on the `(L2)` good component. `rh_sat3_realizability/REPORT.md:193-198` prices the curve at the **ambient** `4m(m+1)-1 = 23`:

```text
 banked:    params(2) = 23 + 9 + 32 = 64 ,  conds = 63 - O ,  excess = -1 - O   (underdetermined)
 corrected: params(2) = 18 + 9 + 32 = 59 ,  conds = 63 - O ,  excess = +4 - O   (overdetermined)
```
with `O <= delta = m-1 = 1` by `(SAT2)` (`saturation_rigidity/statement.md:33`), so the corrected excess is `+4` or `+3` (`d4_results.txt`, section B). **The one banked instrument that predicted `(SAT3)` REALIZABLE at `m=2` — and conjectured on that basis that `m <= 2` is exactly the realizable range (`:200`) — has its sole `m>=2` negative cell flipped by a dimension that anchor 1 measured and I re-derived.** Per my registered R4(iv), a counting excess **refutes nothing**; what it does is remove the disagreement between that ledger and the brief's three instruments, all of which now point the same way at `m = 2`. *(The corrected `+4` numerically coincides with round 34's `+4 = 4m^2-7m+2`; the provenances are different and I flag the coincidence rather than build on it.)*

### D3.5 Where the `m=1` mechanism's death bites the `B`-design

The `m=1` mechanism (disjoint coset locators, the R4 fence) is banked-dead at `m >= 2`. In `B`-coordinates the bite is exact and visible: at `m=1` a locator is a **line in `P^3`** meeting the `C(16,3)` split cubics (`r35_rout_layer_a/REPORT.md:253`), so five disjoint-support members cost nothing extra; at `m=2` the members are the **eigenvalues of `P(x)+zR(x)`**, and disjointness is *forbidden* beyond `T=4` by `7T <= 32`. `(SAT3)` at `m=2` therefore needs 31 of 32 points **doubled** — a structure with no `m=1` shadow at all, since at `m=1` `d_x <= 1` makes doubling impossible by definition. **The `m=1` fence does not fail at `m=2`; it becomes inapplicable, and what replaces it is a packing problem the `m=1` case cannot pose.**

---

## D4 — VERDICT

> **`(SAT3)`-ON-`(L2)` IS NO LONGER VACUOUS AT `m=2`.** `T = 2` over the true domain `mu_32`, on `e = m = 2` objects certified entrywise against `M(Z)Q_Z = 0`, with both supported slopes finite, on two fields, by **exact algebraic solve** — plus `T = 3` over a bespoke 32-set (126 instances, two fields). The route is a **closed-form rational parametrization of the whole `(L2)` stratum**, hit rate `1` against anchor 1's `1/q`, with `det M(B)=0` identified as a **resultant**. **The `T = rho+2 = 9` class is untouched: no witness, no emptiness proof, and the class-emptiness question is now supported by three instruments plus a fourth, none of them a mechanism.**

**T-record of the round with provenance.** `T_mu32 = 2` (exact double prescription, `d2_results.txt:12,38`; Möbius-normalised to finite slopes `{0,1}`, `d3_results.txt:13,20`); `T_bespoke = 3` (search over 433,660 objects, `d3_results.txt:26,37`); `T` over `mu_32` for random `(L2)` objects `= 0` in 120 objects, reproducing anchor 1 (`d1_results.txt:56,58`).

**F1/(NEWCAP) status: still zero power** (MISS 12). One supported pair, `a* = 14 > 7m-1 = 13`, a single sample.

**Class-emptiness picture after the round.** Instruments now pointing at emptiness at `m >= 2`: (i) round 34's searched negative; (ii) the corrected TCAP ledger `+3..+5`; (iii) anchor 2's `C(16m,4m-1)` first moment, **sharpened here by `2 log2 q`** to `-61.3` bits at `q=97`; (iv) **new:** the `(SAT3)` realizability ledger's `m=2` cell, flipped from `-1` to `+4-O` by the mandatory `e=m` dimension. **Still not a mechanism**, and the round's positive half shows why counting is untrustworthy here: the same ledger says `T=3` over `mu_32` is abundant at `+62.5` bits, `q`-independently, and I could not build one.

**Handoff, priority order (recommendations only — AUDIT-AND-DRAFT, nothing applied).**
1. **Re-price `rh_sat3_realizability`'s conjecture.** Its `m<=2` realizability prediction rests on a parameter count that omits the `(ERC2)`-mandatory `e=m` constraint. With dimension 18 the `m=2` cell is `+4-O`. **Its CONJECTURE at `:200` should be re-posed as `m <= 1`, or the ledger re-derived on the `(L2)` component.** This is the highest-value board item of the round.
2. **Bank the parametrization as a node.** `L Q_0 = f^2-kg`, `L Q_1 = fg+hk`, `L Q_2 = g^2+hf` with two conditions at `ell`; `L Q_z = det(P+zR)`; `det M(B)=0 <=> gcd(f^2-kg, fg+hk, g^2+hf) != 1`. It is provable in four lines, it is witness-checkable, and it makes the `(L2)` layer free at `m=2` in the strongest sense (rate 1).
3. **The next exact solve is the third prescription.** `T=3` over `mu_32` is at `+62.5` bits at every field. The missing step is an exact solve for a third split member given `Q_0`, `Q_2` — the analogue of the `L Q_2 == g^2 (mod f)` proportionality. That, and only that, is what stands between this round and `T=4`.
4. **Do not spend compute on blind `(L2)` search at `m=2` at all.** Blind is `q^-5`, anchor 1's inversion `q^-1`, this round's parametrization `1`.
5. **`m >= 3` is untouched.** The parametrization is `m=2`-specific (it uses `deg(f^2-kg) <= 8 = deg Q_0 + 1`); at `m >= 3` the elimination does not close.

**Cross-pilot flag (self-contained; I read no sibling `r36_*` directory).**

> At `m=2` the `e=m` Hankel-pencil stratum admits a **closed-form rational parametrization**: `L Q_0 = f^2-kg`, `L Q_1 = fg+hk`, `L Q_2 = g^2+hf` with `deg f,g,h,k <= 4`, `L` linear, subject to exactly two conditions at the root of `L`; equivalently `L Q_z = det([[f,k],[g,f]] + z[[g,f],[-h,g]])`. Consequences transportable to any lane holding such a pencil: (a) membership is decided by a **gcd**, `det M(B)=0 <=> gcd(f^2-kg, fg+hk, g^2+hf) != 1` (1200/1200, two fields); (b) prescribing one totally-split member costs only a **square root mod `g`**, and a second costs one **proportionality in `F_q[x]/(f)`**, so split-locator prescription is an exact solve, not a search; (c) the members' roots at a domain point are the **generalized eigenvalues of a `2x2` polynomial pencil**, so "T supported slopes" is an eigenvalue-confinement problem; (d) any parameter count for a `T = rho+2` configuration must price the curve at the `e=m` component's dimension (**18** at `m=2`), not the ambient `4m(m+1)-1 = 23` — a 5-unit correction that flips the sign of at least one banked ledger's only negative `m>=2` cell.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| **(X1)** the parametrization + its two `ell`-conditions | **VERIFIED, and it is the round.** `E1&E2 == 0` on every linear-`L` draw; `nullity M(B)=1` `{(1,40)}` per field. **Corrected:** the two conditions are not sufficient when `f(ell)=g(ell)=0` — refined to (RES), 1200/1200 |
| **(X2)** dimension `= 18` | **HIT exactly** — `19+1-2 = 18` with finite fibres both ways, matching anchor 1 by an independent route |
| **(X3)** prescribing `Q_0` split is free (square root mod `g`); `T>=1` over `mu_32` by construction | **HIT** — 12 certified objects, `T=1` over `mu_32`, both fields |
| **(X4)** `expected dim{T>=t} = 15-6t`, threshold at `T=2` | **RESOLVED WRONG** — the exponent is `18-6T`; threshold at `T=3`. `PGL_2` double-count (MISS 3) |
| **(X5)** `log2 E` with 15 dims; gap to anchor 2 `= 33` bits | **RESOLVED WRONG in the same way** — 18 dims, gap `= 2 log2 q = 13.20` bits; the corrected ledger reproduces anchor 2 exactly at five fields |
| **(X6)** (QPACK) `d_x <= 2`, `7T <= 64`, `T <= 9` | **DERIVED and then SUBTRACTED** — banked verbatim at `saturation_rigidity/statement.md:49-50,53,59,62-65` (MISS 2). P14 = 0.80 was right |
| **(X7)** `T >= 5` requires root sharing (`7T > 32`) | **VERIFIED as arithmetic; NOT TESTED at `T>=5`** (max reached 3). Sharing already appears at `T=3` (`\|union\| = 20 < 21`, `19 < 21`) |
| **(X8)** bespoke beats `mu_32` by `q^7/(7!C(32,7)) = 3.8e3`; split rate `(q+1)/5040` | **HIT within the registered 3x falsifier** — measured `0.0141` vs `0.0192`, `0.0332` vs `0.0383` (MISS 9); anchor 1's `T=0` confirmed consistent with the random law (`0/5820`, `4/11580` vs `1/5040`) |
| **(X9)** supply coherent at `t=1`, partial at `t=2`, incoherent from `t=3` | **HIT** — free, exact-solvable, and no solve respectively |
| **P1** `T = rho+2 = 9` witness `= 0.02` | **resolved NO** |
| **P2** `T >= 1` achieved at all `= 0.93` | **HIT** — 19 certified objects with `T >= 1` |
| **P3** designed-domain route beats `mu_32` `= 0.80` | **HIT** — factor `3.8e3` derived, `0.0140` vs `0` measured |
| **P4** the wall is value-confinement `= 0.30` | **resolved NO** — no wall was hit; the count says `T=3` over `mu_32` is abundant |
| **P5** expected max `T` this round `= 3` | **HIT exactly** (bespoke). **P5a** `max T` over `mu_32` `= 1` → **BEATEN, `= 2`**. **P5b** bespoke `= 3` → **HIT** |
| **P6** (X1) verifies with no correction `= 0.70` | **partial** — verified, but needed the `f(ell)=g(ell)=0` refinement |
| **P7** dimension `= 18` `= 0.75` | **HIT** |
| **P8** `T>=1` over `mu_32` by construction `= 0.85` | **HIT** |
| **P9** `T>=2` bespoke `= 0.60` | **HIT** — 3690 and 5386 instances |
| **P10** `T>=2` over `mu_32` `= 0.25` | **HIT** — the round's headline |
| **P11** `T>=3` any domain `= 0.15` | **HIT** (bespoke only) |
| **P12** wall is packing rather than value-confinement `= 0.45` | **partial** — no wall reached; the predicted wall is eigenvalue-confinement/packing, and its combinatorial form is banked (MISS 4) |
| **P13** the `33`-bit gap verifies `= 0.65` | **resolved NO** — `13.20` bits (MISS 3) |
| **P14** `d_x <= m` already banked `= 0.80` | **HIT** |
| **P15** the `2x2` determinantal form already banked `= 0.55` | **resolved NO in this lane** — nearest priors are `A=1` adjugate and an `l1` scalar determinantal representation |
| **P16** a fourth instrument `= 0.35` | **HIT** — (RES), plus the `+4-O` repricing |
| **P17** at least one ramguard run fails `= 0.70` | **resolved NO** — four invocations, four clean exits |

---

## ZERO-POWER DECLARATIONS

1. **Z1 honoured and load-bearing.** `T = 3` is over a **bespoke 32-set**, not `mu_32`, and has **zero power** for `(SAT3)`, the strict endpoint, or the official row. The two columns are never merged; the bespoke record objects have `T = 1` over `mu_32`.
2. **Z2 honoured.** Reaching `T = 2` rather than `9` proves nothing about emptiness. The corrected first moment says `T <= 6` cells are positive at `q=97`; my record is a **sample maximum over the constructions I ran**, never a bound (R4(i)).
3. **Every `T` reported comes with its full distribution** (R4(ii)): `{1:244063, 2:3690, 3:37}` and `{1:156141, 2:5386, 3:89}`; `T` over `mu_32` `= [1,1,1,1,1,1]` per field for route A and `{2:4}`/`{2:1}` for route B.
4. **R4(iii) honoured:** a witness has full power (existence is witness-checkable), a null has power only against the rate sampled. **My 120-object `mu_32` null has zero power** — the expected count there is `5820 x 5.19e-8 = 3e-4`.
5. **R4(iv) honoured:** no counting excess carries an emptiness verdict. The `+4-O` repricing of `rh_sat3_realizability` is explicitly **not** an exclusion; it removes a disagreement, nothing more. The `18-6T` threshold is a heuristic with the `pb_design_ceiling/proof.md:125` blind spot.
6. **Z9 discharged by construction, not by convention** — the `T=2` objects were Möbius-normalised to two finite slopes and re-certified, so the `z = infinity` bookkeeping question cannot affect the claim.
7. **`a* = 14` is a single sample on a single supported pair**, not a minimum over a family; **F1/(NEWCAP) remains at zero power** (MISS 12).
8. **`(SAT2)/(SAT4)/(SAT5)` are not verified, they are inapplicable at `T=2`.** I report `sum_x d_x = 14` with histogram `{0:18, 1:14}` instead of a vacuous table.
9. **Two fields only** (`97, 193`) for everything except the ledger arithmetic (five fields). No lift to `Z`, no geometric irreducibility, **no statement at `q ~ 2^128`**.
10. **Nothing here bears on `m >= 3`** — the elimination that produces (PAR) uses `deg(f^2-kg) <= deg Q_0 + 1`, which is `m=2`-specific — **nor on `Rout`, the `9/4` or `7/4` ledgers, FR-canonical, or layer A.**
11. **`s != 0` degeneracy yield is empirical**: 42 of 46 exact `mu_32` solutions at `q=97` were rejected. I have no predictive criterion (MISS 8).

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, rho=4m-1=7, N=16m=32, R=16, A=3, e, s, delta=rho-3e, T_target=rho+2=9`; `deg Q_j`; `s = deg gcd(Q_0,Q_1,Q_2)`; separation rank `(RNC2)`; `nullity(36x32)`; entrywise `M(Z)Q_Z = 0`; generic rank `max_z rank M_r(y_0+zy_1)`; the finite rank-drop set with its rank and the rank at infinity; the degree-`<=1` kernel dimension (the `e<=1` filter); `y_0, y_1` recovered as the `36x32` kernel. **New here:** the parametrization coordinates `(f,g,h,k,L,ell)` and the two `ell`-conditions; `L = gcd(f^2-kg, fg+hk, g^2+hf)` and its degree; the **joint histogram of `det M(B)=0` against the gcd criterion** (1200 draws, two fields); `nullity M(B)` and `nullity Phi` (fibre dimensions both ways); the **construction hit rate** (rate-1 vs `1/q`); the number of **exact `S_2` solutions per configuration** against `C(32,7)/q^3`; `T_fin`, `T_P1` and `T` over `mu_32` and over a bespoke 32-set, separately; the **`T_bespoke` histogram over 433,660 objects**; `|union of supported root sets|` (the domain-admissibility check); the per-slope **root-count histogram over `mu_32`** and `max_z` of it; the **slot occupancy `sum_x d_x` out of `2|D| = 64`** and the **number of distinct slopes carrying a root** (the concentration functional); `d_x` histogram at the supported slopes; the **Möbius-transformed pencil** `(y_0, y_1-y_0)`, `(Q_0, Q_1-2Q_0, Q_0-Q_1+Q_2)` and its re-certification; the corrected first-moment ledger `18 log2 q + log2 C(q+1,T) + T[log2 C(32,7) - 7 log2 q]` at five fields and its `18-6T` exponent; the corrected `(SAT3)` realizability excess `+4-O`. **Registered but NOT measured:** any `T >= 4` (none built); `T = 3` over `mu_32` (no exact solve — MISS 10); `(SAT2)/(SAT4)/(SAT5)` (inapplicable at `T=2`); the endpoint's `a*` over supported pairs beyond one pair; anything at `m >= 3`.

---

## COMPLIANCE

**Registrations.** `R0` (notation from the anchors alone), `R1` (execution order), nine falsifiable derivations `(X1)-(X9)` **each with its falsifier**, seventeen numeric priors `P1-P17` including the five the brief demands and the **expected-max-`T` number (3)**, the four-clause MISS-2 mean-vs-max guard `R4`, nine zero-power pre-declarations `R5`, the subtraction plan `R6` with hyphenated/infixed variants, and the expected misses `R7` were appended to `PREREG.md` under `## Pilot registrations` with the **Edit tool**, after reading **exactly** the two named anchors and **before any other read, any grep, any `ls`, and any interpreter invocation**. **No post-registration addenda**; the three registration errors (`(X4)`/`(X5)`'s `PGL_2` double-count, `(X1)`'s missing `f(ell)=g(ell)=0` exception, `P5a`) are reported as misses, not edited. Execution followed `R1` (D1 → D2 → D3 → D4) exactly.

**Compute law — NO BREACH.** **Four interpreter invocations, all four `tools/ramguard <profile> -- python3 …` from the repo root with the literal `--`**: three `local` (`RAMGUARD_TIMEOUT=290, 290, 295` — inside the 5-minute profile ceiling, not an extension) for `d1_param.py`, `d2_mu32.py`, `d3_push.py`, and one `tiny` (`RAMGUARD_TIMEOUT=55`) for `d4_ledger.py`. **Zero bare `python3` for any purpose** — no file patching, no string replacement, no probes, no heredocs. Stdlib only (`random`, `time`, `math`); no third-party imports, no Modal, no network, no git, **no subagents**. **Ramguard status: four clean exits, no memory event, no wall kill** (P17 resolved NO). The two long runs were self-budgeted with `time.time()` caps (95 s per field) precisely to avoid a wall kill.

**Write discipline.** No `sed -i`, `awk -i`, `perl -i`, `tee`, or shell redirection onto any file; no in-place shell stream edit anywhere. The single `PREREG.md` edit used the **Edit** tool; all four scripts were created with the **Write** tool; each script created and overwrote only its own results file, as the constraint permits. The two bounded reads that used `sed -n` were **read-only** (`-n`, no `-i`).

**Imported-script rule — NOT ENGAGED, and stated rather than assumed.** I imported and executed **no** banked script. All four scripts are mine, written from scratch; the poly/linear-algebra helpers are duplicated into each file rather than imported, specifically so that no import can write at import time. Banked material was read **only** as data (`rh_psi_degree/d3_m2_q97.txt`, `d3_m2_q193.txt`, `d3_m4_q257.txt`, `rh_sat3_realizability/REPORT.md`, `d1_m1_results.txt`) via `grep -n` and one bounded `sed -n` window.

**RAM discipline.** `dag.json` **never opened**; every recursive grep carried `--exclude=dag.json`. `critical/nodes/rate_half_band_crossing_location/statement.md` (>3300 lines) was touched **only** through `grep -n` output lines, never read as a file. `saturation_rigidity/statement.md` was read in one 45-line window; `rh_sat3_realizability/REPORT.md` in one 10-line window plus greps. Largest object materialised: the `36x32` elimination and the `26,333`-element meet-in-the-middle table; every driver writes its own results file.

**Quarantine — clean.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened and never appeared in any tool output**. **No sibling `r36_*` directory was opened, read, listed or traversed**, and **`notes/pilots_20260811/` was never `ls`-ed** — the sibling names came from `CONSTRAINTS.md`, as intended, and every listing I ran named an explicit path (`ls -d background/nodes/*exceptional_root_charge*`). Every recursive grep carried `--exclude-dir=r36_lawcount_geom --exclude-dir=r36_hrlow --exclude-dir=r36_m4_nonsplit --exclude-dir=pilots_20260802 --exclude-dir=prize-codex-{1,2,3} --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json` **at the search level**, never as output filtering. No path containing `prize-codex-` was touched. The `r35_*`, `r34_*` and `rh_*` directories were read as explicitly permitted.

**Write scope.** Every write is inside `notes/pilots_20260811/r36_sat3_on_l2/`: `PREREG.md` (registrations appended), `d1_param.py` + `d1_results.txt`, `d2_mu32.py` + `d2_results.txt`, `d3_push.py` + `d3_results.txt`, `d4_ledger.py` + `d4_results.txt`, plus a `__pycache__`-free tree (no imports between my scripts). **No `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; the session scratchpad was not used; nothing went to `/tmp`.** **AUDIT-AND-DRAFT respected:** every board and node recommendation in D4 is posed for coordinator triage and **nothing outside my directory was altered**. `REPORT.md` is not written — per the brief's fallback clause this report is returned verbatim as my final message.

**Method discipline.** CATCH-24A greps ran **before** every novelty claim, including hyphenated and infixed variants, and produced **eleven live subtractions, four of them load-bearing**: my registered (X6) is banked verbatim in `(SAT4)`'s own statement; the D3 design mechanism is banked in a readable pilot with more detail than I had; my T-record is **below** two banked T's (which are out of class); and a **PROVED** node `(ERC2)` is the hinge that turns a banked realizability ledger's `m=2` verdict from `-1` to `+4-O`. Every quantifier claim carries a `file:line` or a results-file citation with its denominator. Every max-quantified claim carries a zero-power declaration. **Two-field confirmation (`F_97`/`F_193`) for every structural claim** — the parametrization, the fibre dimensions, the gcd criterion, both `T=1` and `T=2` constructions, the Möbius normalisation, the bespoke record, and the packing measurements — with the five-field ledger arithmetic declared as arithmetic, not measurement. **MISSES FIRST**, and the round's own self-corrections — that my T-record is not a campaign record, that my headline packing derivation was already banked, that my registered ledger double-counted `PGL_2`, and that my registered criterion needed a refinement my own data caught — are reported as falsifications of my own work, in that order, before any result.
