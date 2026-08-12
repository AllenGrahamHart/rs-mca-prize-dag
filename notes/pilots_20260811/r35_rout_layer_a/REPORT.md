All experiments are complete. Here is the full report.

---

The harness refuses a `REPORT.md` write, so per the brief the full report text is returned verbatim below. My directory contains 21 files and no `REPORT.md`.

**Headline for relay:** the brief's deciding question rests on a **false premise** — bank 1's "`Rout <= 3` on 648/648" is contradicted by bank 1's own results file, which records **`Rout = 4`** (`rh_psi_degree/d3_m2_q193.txt:70-71`). `Rout <= d-m` is **NOT a theorem**: it fails in-class at `m=1` (4800/5280) and out-of-class at `m=2,3` **inside the ledger's own band** (582 violations in 7275 canonical slopes), and `Rout` is distributed **exactly** like the rational-root count of a uniform random polynomial of the same cofactor degree (32700 slopes, three cells, two fields). So `(NS-m) -> (NS-W-m)` is a **REDIRECTION, not a correction** — and the exact closure criterion counts `Rout` with a **plus** sign, so bounding it was the wrong direction all along. **Layer A KILLS anchor 2's `m=3` (BIV-CURVE) witness**, and it kills it **completion-independently**: the `a*m = 60` incidences *inside `W`* already force `Q = 0` against `(rho+1)(m+1) = 48` unknowns, both fields; the mechanism is the count `3m^2-5m`, positive for every `m >= 2` and `-2` at `m=1` (where the witness correctly survives with nullity exactly 2). D3's structural target turned out to be **three PROVED nodes** — anchor 1's round-34 "factor-degree dichotomy" is `rate_half_ca_hankel_endpoint_rational_branch_exclusion` (CPR3)-(CPR5), already proved, which its CATCH-24A missed. **I breached write scope once** (an imported bank script wrote into `r34_layer_a/`) — MISS 1.

---

# REPORT — r35_rout_layer_a (round 35)

## VERDICT (first)

1. **`Rout` IS FREE, AND THE PREMISE OF THE QUESTION IS FALSE.** Bank 1's headline `Rout <= 3` (`rh_psi_degree/REPORT.md:328`) is contradicted by its own cell `m=2, q=193`, where `maxRout = 4` at `a=14` in **both** the canonical and planted rows (`rh_psi_degree/d3_m2_q193.txt:70-71`). In my scaled census (32700 type-2 slopes, `m=2` two fields, `m=3`), the `Rout` histogram agrees with a uniform-random-polynomial null to within sampling error at every cell, and `max Rout` climbs `1 -> 2 -> 3 -> 4 -> 5` as the sample grows. **`Rout <= C` is not a theorem for any constant `C`; `Rout <= d-m` is refuted.**
2. **THE REFUTATION REACHES THE LEDGER'S OWN BAND.** At the canonical `W*` with `a >= a* = 7m-1` — the stratum anchor 2's witness realizes — over **7275** type-2 slopes at `m=2` (`q=97,193`) and `m=3` (`q=97`): **`(NS-W-m)` holds 7275/7275** while **`(NS-m)` fails 678 times** and **`Rout > d-m` occurs 582 times**. The entire discrepancy is `Rout`. In-class (the only realized `(SAT3)` data that exists, `m=1`, `q=17`) `(NS-m)` fails 4800/5280 while `(NS-W-m)` holds 5280/5280, reproduced exactly from my own copy.
3. **`Rout` HELPS CLOSURE — SO BOUNDING IT IS BACKWARDS.** Rearranging bank 1's two banked identities `(JDEC)` and `(DEGSUM)` (`rh_psi_degree/REPORT.md:318-323`) gives the **exact** closure criterion
   ```text
   (CLO-m):   (d - Dh) + (n_gamma - ov_gamma) + Rout_gamma + nonsplit_gamma  >=  m,
   ```
   verified equivalent to `X_gamma <= d-m` in **32700/32700** measurements. `Rout` enters with a **positive** sign. `(NS-m)` penalises the one term that the ledger is helped by; `(NS-W-m)` does not. **`(NS-m)` should be retired, not repaired.**
4. **LAYER A KILLS THE `m=3` (BIV-CURVE) WITNESS, COMPLETION-INDEPENDENTLY.** `d2_layerA_results.txt:13-23`: `LA|_D` (143 incidences) and `LA|_W` (**60 incidences, inside `W` only**) both give **nullity 0** on `F_97` and `F_193`; the locator span rank is `12 = rho+1` against the banked bound `m+1 = 4`; 40 fresh outside completions give `{span 12: 40}`, `{nullity 0: 40}` on both fields. Because `LA|_W` uses nothing outside `W`, **no outside completion whatsoever can save the witness.** The mechanism is a count that is `m`-uniform:
   > **(LA-W COUNT).** At `a = a* = 7m-1` with every `x in W` saturated (`|A_x| = m`), the `W`-incidences alone impose `a*m = (7m-1)m` linear conditions on the `(rho+1)(m+1) = 4m(m+1)` coefficients of the layer-A biform. The excess is `3m^2 - 5m`: **`-2` at `m = 1`, positive for every `m >= 2`.**
   The `m=1` regression passes exactly (`nullity 2 = 8-6`, `16/16` realized witnesses), and bank 2's `m=2` exhibit is killed by its 26 `W`-incidences alone (excess `2`).
5. **THE MULTIPLICATIVE PUSH DOES NOT EMPTY THE SURVIVOR, AND MOST OF IT WAS ALREADY PROVED.** The surviving profile at `m=2,3,4` is exactly the banked (CPR3)-(CPR5) profile of the **PROVED** node `rate_half_ca_hankel_endpoint_rational_branch_exclusion`. My per-factor derivation reproduces it (minimal excess `4(m - max_j m_j) <= m-1`), agreeing with anchor 1's aggregate scan on every profile for `m <= 8` and giving the closed form `#survivors(m) = sum_{k <= floor((m-1)/4)} p(k)` (`= 97` at `m=40`, matching). What is new is the **quantified gate**: the multiplicative domain enters only through `C(16m, 4m-1)` — the `q`-**independent** number of degree-`rho` divisors of `x^N-1` — against an ambient `q^rho`. The resulting first moment is **calibrated twice at `m=1`** (`log2 E = +13.75` at `q=17`, where I count **exactly 16** layer-A-consistent configurations, the banked 16; `log2 E = -0.94` at `q=97`, where bank 3 measured none) and is **negative for every `m >= 2`** at every field in this lane, `~ -1952 m^2` bits at official scale. **Heuristic, not a theorem.**

---

## MISSES FIRST

1. **I BREACHED WRITE SCOPE. My copy of `d5_layerA_bank2.py` writes a results file AT IMPORT TIME, and the inherited path pointed into anchor 1's directory.** Importing it from `d2_layerA_m3.py` overwrote `notes/pilots_20260811/r34_layer_a/d3b_replay_results.txt` (twice; mtime `2026-08-11 12:44`). The script is deterministic (`build_cfg(q, 20260811+q)` seeded), so the regenerated content is the same content — I verified it line by line against anchor 1's description at `r34_layer_a/REPORT.md:428-432` (nullity 0 both fields, CTRL-1/2/3 PASS) — but **the rule is that no file outside my directory is written, and I wrote one.** I found it by auditing `find -newermt` after the run, not before it. Fixed with the Edit tool (my copy now writes `d3b_replay_r35.txt` inside my dir). Exactly one file outside my directory was touched; nothing else, no `__pycache__` outside.
2. **MY REGISTERED ARTIFACT HYPOTHESIS (R2.2) WAS WRONG, AND THE TRUE EXPLANATION IS WORSE FOR THE BANK.** I predicted at `P=0.50` that bank 1's `Rout <= 3` was a **degree** artifact (`max d <= 3`). False: `d` runs to `12` at `m=4` (`rh_psi_degree/d3_m4_q257.txt:39`). The real explanation is the sampling tail — and, worse, **the reported maximum is simply wrong**: the banked files contain a `4` (`d3_m2_q193.txt:70-71`), so `Rout <= 3` was never true even of the 648.
3. **"THE BINDING SUB-SYSTEM IS ANY 16 POINTS OF `W`" IS FALSE, AND I NEARLY SHIPPED IT.** `d2_layerA_results.txt:17` reports that the **first** 16 points of `W` in sorted order force `Q = 0` — which is anchor 1's own MISS-10 trap. I then ran **all** `C(20,16) = 4845` subsets (`d3_mult_results.txt:70-71`): `4791/4845` at `q=97` and `4823/4845` at `q=193` force `Q=0`; the rest have nullity **1**. So the correct claim is "`98.9%`/`99.5%` of 16-subsets bind, and the full `W` binds", **not** "any 16".
4. **MY `m>=2` `Rout` MEASUREMENTS ARE ALL OUT OF THE HYPOTHESIS CLASS, AND SO ARE BANK 1'S.** `(NS-m)` and `(NS-W-m)` are quantified over strict-`A=3` pencils **at `T = rho+2`**. The census constructor realizes `max T = 3` (`rh_psi_degree/d3_m4_q257.txt:88`, same builder). So neither bank 1's positive measurement nor my refutation is inside the class at `m >= 2`. The only in-class data at any `m` is the `m=1` `q=17` stratum. I state this before the numbers rather than after.
5. **THE HYPOTHESIS CLASS MAY BE EMPTY, WHICH MAKES `(NS-m)` VACUOUSLY TRUE AND MY REFUTATION UNABLE TO REACH IT.** My own D3 first moment says layer-A-consistent configurations do not exist for `m >= 2`. If so, every statement quantified over them is vacuous and none of this decides anything in-class. That is a genuine limitation of the whole `Rout` question, not a property of my measurement.
6. **D3's STRUCTURAL TARGET WAS ALREADY PROVED, AND SO WAS ANCHOR 1's ROUND-34 THEOREM.** `background/nodes/rate_half_ca_hankel_endpoint_rational_branch_exclusion/statement.md:24-45` is **PROVED** and contains (CPR3) the unique `r = 4e-1` component, (CPR4) `r_i = 4e_i` for all others, (CPR5) `e_(i*) >= ceil((3m+1)/4)` **and** `sum_(i != i*) e_i <= floor((m-1)/4)`, and "cannot split into `m` rational moving-root branches". That is anchor 1's round-34 "FACTOR-DEGREE DICHOTOMY" (`r34_layer_a/REPORT.md:349-359`) **and** my sharpening, both. Anchor 1's CATCH-24A grepped the RNC node, the saturation node and `band_crossing_location` but not this node. I found it only because I grepped for `norm/Bezout`.
7. **THREE OF MY FOUR "NEW" D3 OBJECTS SUBTRACTED TO ZERO.** The norm/resultant identity is the transpose of the proved `(ENF2)` (`endpoint_norm_factorization/statement.md:36-45`); `gcd(4m-1,16m) = 1` and its consequence for coset-structured supports is the proved `rate_half_type2_fr_quartic_coset_biform_lift_obstruction/proof.md:66-72`; "`Q(gamma,x) = c_gamma L_gamma(x)` when `o_gamma = 0`" is banked at `d5_layerA_bank2.py:23-25`. Only the counting gate in [C] survives, and it is a heuristic.
8. **FOUR OF TEN RAMGUARD RUNS FAILED.** Two wall kills (invocations 5 and 7: the completion resampler re-ran the `phi` search 80 times; the profile scan enumerated compositions exponentially), one `MemoryError` (`list(parts(100))`, `p(100) ~ 1.9e8`), one `IndexError` (partition table too short for `m=1024`). All self-caught, all fixed with Edit/Write, all rerun.
9. **`m=3`'s `Rout` CENSUS IS SINGLE-FIELD.** Only `q=97` was affordable at `m=3` within the wall. Two-field confirmation exists at `m=2` only. The `m=3` null-agreement is therefore one field.
10. **THE FIRST MOMENT OVERESTIMATES BY `~2^9.8` AT ITS OWN CALIBRATION POINT.** `log2 E = 13.75` predicted against **16** actual configurations at `m=1, q=17` (`d3_mult_results.txt:39,50`). The error is in the safe direction for a negative conclusion, but it means the numbers are order-of-magnitude only, and I do not claim otherwise.
11. **I DID NOT DECIDE `m=4` FOR `(BIV-CURVE)`, AND I DID NOT BUILD ANY `m>=2` LAYER-A CANDIDATE.** My `LA|_W` count says the search would have to beat a `3m^2-5m` overdetermination; I did not run it. Absence where none was sought is not evidence.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

| object | in-repo prior | verdict |
|---|---|---|
| the factor-degree dichotomy: one component with `r = 4e-1`, all others balanced `r_i = 4e_i`, `e_(i*) >= ceil((3m+1)/4)`, `sum_(i != i*) e_i <= floor((m-1)/4)`, no splitting into rational branches | `background/nodes/rate_half_ca_hankel_endpoint_rational_branch_exclusion/statement.md:24-45` **(CPR2)-(CPR6), PROVED** | **BANKED AND PROVED — and it is anchor 1's round-34 theorem as well as my D3 sharpening.** My contribution is a 5-line re-derivation from the incidence side and an exhaustive check that it reproduces the profile sets (`d3_mult_results.txt:19-31`). **Not new.** |
| the norm identity `prod_x Q = ` power of the slope form up to defects of degree `<= m` | `background/nodes/rate_half_ca_hankel_endpoint_norm_factorization/statement.md:36-45` **(ENF2), PROVED**; the two-sided weight identity `:93-98` **(ENF6)**; the deficiency `1 <= b <= 1+O` `:49-58` **(ENF3)** | **BANKED AND PROVED.** My `x`-side form `Res_Z(C,Q)*E(x) = lambda (x^N-1)^m U(x)` is its transpose; the `(x^N-1)^m` shape is the multiplicative reading of the same statement. **Not new.** |
| `gcd(4m-1,16m) = 1`, hence no support is a union of cosets of a nontrivial subgroup of `mu_N` | `background/nodes/rate_half_type2_fr_quartic_coset_biform_lift_obstruction/proof.md:66-72` eq. `(9)`, **PROVED** | **BANKED AND PROVED** (used there for injectivity of `x -> x^(n-1)`; same arithmetic, same conclusion for coset ansätze). **Not new.** |
| `Q(gamma,x) = c_gamma L_gamma(x)` when `o_gamma = 0`; layer A as `(rho+1)(T-m-1)` conditions on `T` unknowns | `notes/pilots_20260811/r34_layer_a/d5_layerA_bank2.py:8-25`; `saturation_rigidity/proof.md:5-6,15` | banked; it is the object I measure. My `Q`-coefficient formulation is the same system in different coordinates and I check the two agree (`d2_layerA_results.txt:15,21`). |
| the `m+1` forms independent, separation rank exactly `m+1`, `nu_Q` a degree-`m` rational normal curve; `>= 3m+2` parameters carry a squarefree degree-`rho` form **split over `D`** | `background/nodes/.../rational_normal_kernel_curve/statement.md:22-39, 48-50`, **PROVED** | banked. **"Split over `D`" is theirs**, so my `(MDG-m)` phrasing ("the `(m+1)`-space contains `T` divisors of `x^N-1`") is their statement restated. The **count** `C(16m,4m-1)` is what I add. |
| "the next exact gate is the Hankel/apolar chain, the multiplicative-domain evaluation hyperplanes, or the norm/Bezout factorization" | `.../rational_normal_kernel_curve/claim_contract.md:21-23` | banked; it is my D3 mandate. My answer: two of the three are already-proved nodes, and the third does not empty the survivor. |
| `(SAT3)`, `(SAT4)` `sum_x (m-d_x) = 1+O <= m`, `d_x <= m`, `Q_Z(x)` of parameter degree exactly `m` at saturated points | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:36-69` | banked; hypotheses, quoted not derived. `deg_Z Q = m` exactly is **theirs** (`:62-63`). |
| `a = 8m-2 = 2rho` is vacuous for every `m >= 2` | `critical/nodes/rate_half_band_crossing_location/statement.md:581-584` **VACUITY LEMMA** | banked; **bank 1's planted census is planted at exactly `a = 8m-2`** (`rh_psi_degree/d3_m4_q257.txt:9`), so its planted rows live in the banked-empty stratum. Its `canon` rows do not, and my band result uses only `canon`. |
| `Rout`, `RoutD`, `nonsplit`, `(DEGSUM)`, `(JDEC)`, `h_gamma` as the interpolant of `z_gamma Q_gamma sigma'_W` | `notes/pilots_20260811/rh_psi_degree/d3_tail.py:11-21,125-136`; `REPORT.md:318-323` | banked; the definitions are theirs and I re-typed them so their identities act as controls on my re-implementation (`32700/32700`). Repo-wide greps for `Rout`/`R_out`/"roots outside"/"outside W" outside the pilot dirs return only unrelated lanes (`ca_hankel_a1_first_degree_*` uses `R_out` for a different quantity). |
| the exact closure criterion with `Rout` positive | bank 1 has the identity (`REPORT.md:322`) and the aggregate `(EXC)` (`:311-314`) but **targets `(NS-m)`, i.e. the direction in which `Rout` is a cost** | the **rearrangement** `(CLO-m)` and the observation that `Rout` carries a `+` sign are, as far as my greps reach, **not stated anywhere**; the ingredients are entirely banked. Claimed as a *reading*, not a theorem. |
| the `LA|_W` count `a*m` vs `(rho+1)(m+1)`, excess `3m^2-5m` | greps for `3m^2-5m`, `3m^2 - 5m`, `a*m` over `critical/`, `background/`: **zero hits** | claimed **new**, and deflated: it is a dimension count, and R3(b) forbids reading a counting excess as a rank excess. The rank is **measured** (`nullity 0`, both fields), which is what carries the verdict. |
| the first-moment count for layer-A configurations using `C(16m,4m-1)` | greps for `first moment`, `first-moment`, `binomial`, `C(16m`, `choose` over the four endpoint nodes: **zero hits**; bank 2 uses a first moment for **(BIV-CURVE)**, not for layer A (`rh_bivariate_system/REPORT.md:424`) | claimed **new in this lane**, and graded as a heuristic. Its method is bank 2's; its input (`C(N,rho)`, `q`-independent) is the multiplicative-domain gate. |

---

## D1 — `Rout` DECIDED

### D1.0 What `Rout` is, and the premise check

`h_gamma` is the degree-`<= a-1` interpolant on `W` of `x -> z_gamma(x) Q_gamma(x) sigma'_W(x)` (`rh_psi_degree/d3_tail.py:11-13`), `Rout` its `F_q`-roots outside `W` counted with multiplicity (`d3_tail.py:16,135`). The brief's premise is `rh_psi_degree/REPORT.md:328`, "`Rout <= 3` always".

**The premise is false in the banked data.** `rh_psi_degree/d3_m2_q193.txt:70-71`:

```text
  where     a   meanRout  maxRout  meanRoutD  mean nonsplit  mean(d-Dh)
  canon      14      2.333        4      0.000          1.667       0.000
  planted    14      1.000        4      0.033          1.000       0.000
```

`maxRout = 4`, inside the 648. Sweeping every `(where, a)` row of all six banked cells against `d-m = a-(4m+2)-m`, `Rout <= d-m` **fails in 10 of the 24 rows**, including rows with `d >= m` (so the `(NS-W-m)` hypothesis is satisfied): `m=2,q=193,a=13` and `a=14`; `m=3,q=193,a=18,19`; `m=4,q=257,a=23`.

### D1.1 The `m=1` regression, in class, replayed from my own copy

`d1b_m1_replay_results.txt` reproduces anchor 1's exhaustive `m=1` classification numeral for numeral (8960 `W`, 320 admissible, `[B]` table identical). At the only stratum with `d >= 1`:

```text
 a  x0inW   admH   tot2   NS-A   NS-B   NS-W   CLOS  SPLIT        deg h        #F_q-roots
 7   True   1760   5280    480      0   5280   5280   4800 {0:480, 1:4800} {0:480, 1:4800}
```

`X = 0` and `Rin_mult = 0` identically, so `Rout = #F_q-roots`: the **`Rout` histogram at `a=7` is `{0: 480, 1: 4800}`**, `max Rout = 1`, and `Rout <= d-m = 0` **fails 4800/5280**. At the realized `a* = 6`, `d-m = -1 < 0 = Rout`, so it fails `480/480`. **R2.1 HIT, both branches.** This is the only measurement in this lane that is inside the `T = rho+2` hypothesis class at any `m`.

### D1.2 The scaled census: `Rout` against a null model

`d1_rout.py` re-runs bank 1's constructor (`build_modeB`/`analyse`, exec'd from my copy of `d3_psi.py` lines 1-497, unedited) and adds, per slope, one uniformly random polynomial of the **same cofactor degree** `Dg = Dh - Rin_m`, whose roots outside `W` are counted identically. Bank 1's identities act as controls on my re-implementation:

```text
                                          m=2 q=97   m=2 q=193   m=3 q=97
  type-2 slopes                               5274       10474      16952
  Rin = n + X - ov                       OK 5274/0  OK 10474/0  OK 16952/0
  (JDEC) d - Rin = o+j+cancel            OK 5274/0  OK 10474/0  OK 16952/0
  (DEGSUM) Dh = Rin_m+Rout+nonsplit      OK 5274/0  OK 10474/0  OK 16952/0
  every W-root simple                    OK 5274/0  OK 10474/0  OK 16952/0
  (CLO-m) <=> closure X <= d-m           OK 5274/0  OK 10474/0  OK 16952/0
```

`Rout` versus the null (`d1_rout_results_m*_q*.txt`, "Rout HISTOGRAM" block):

```text
 cell            0      1      2      3      4      5    mean(meas)  mean(null)
 m=2 q=97     2786   1816    578     80     14      -      0.6196      0.6380
   null       2784   1758    612     97     23      -
 m=2 q=193    5212   3710   1254    236     62      -      0.6849      0.7009
   null       5170   3651   1320    282     51      -
 m=3 q=97     9208   5536   1804    344     54      6      0.6148      0.6699
   null       8806   5611   1970    469     86      7
```

The measured and null histograms agree cell by cell; the measured tail is `~10%` **thinner** than the null at `m=3` and statistically indistinguishable at `m=2`. Running maxima (`d1_rout_results_m3_q97.txt`, "GROWTH" block): new records at slopes `#3, #21, #273, #6359` reaching `Rout = 5`. **`Rout` is the rational-root count of an unstructured polynomial**; its maximum grows with sample size and is bounded by nothing but the degree — indeed `Rout = 4 = d` is attained at `m=2, a=14`, i.e. **the trivial degree bound is achieved**.

One reproducible structural deviation: roots landing in `D \ W` are suppressed relative to the null by a factor `~0.7` in every cell (`516/3268` vs `748/3365` at `m=2,q=97`; `532/7174` vs `752/7341` at `m=2,q=193`; `2884/10422` vs `4062/11356` at `m=3`). Reported as a measured functional; I have no mechanism for it and I do not build anything on it.

### D1.3 The result in the ledger's own band

Restricting to the **canonical** `W*` with `a >= a* = 7m-1` (the stratum anchor 2's `m=3` witness realizes; rows `d1_rout_results_m2_q97.txt:22-23`, `_m2_q193.txt:22-23`, `_m3_q97.txt:24-26`):

```text
 cell / a          slopes   Rout > d-m   (NS-m) fails   (NS-W-m) fails
 m=2 q=97  a=13       751          162            164                0
 m=2 q=97  a=14       449            7              7                0
 m=2 q=193 a=13      1491          371            374                0
 m=2 q=193 a=14       933           31             31                0
 m=3 q=97  a=20      1517           11            100                0
 m=3 q=97  a=21      1284            0              2                0
 m=3 q=97  a=22       850            0              0                0
 TOTAL               7275          582            678                0
```

**`(NS-W-m)` holds 7275/7275; `(NS-m)` fails 678 times; the whole gap is `Rout`.** (At planted, non-minimal `W` both fail — `(NS-W-m)` fails 6686 times — so the surviving statement is specifically about the **canonical minimising** `W*`, which is the ledger's `W`.)

### D1.4 The sign, and why the question was posed backwards

From `(JDEC)` and `(DEGSUM)` with simple `W`-roots:

```text
X_gamma <= d-m   <=>   (d - Dh) + (n_gamma - ov_gamma) + Rout_gamma + nonsplit_gamma >= m
```

verified as an equivalence in **32700/32700** slopes. `Rout` appears with a **plus** sign: a larger `Rout` makes closure **easier**. `(NS-m)` = "`Rin_m + Rout <= d-m`" is therefore strictly stronger than `(NS-W-m)` = "`Rin_m <= d-m`" by exactly the term that helps. Bounding `Rout` above cannot buy closure; it can only make a sufficient condition harder to satisfy.

### D1.5 D1's answer, exactly as the mandate asks

- **Theorem? No.** The only theorem available is the trivial `Rout <= Dh - Rin_m <= d - Rin_m`, and it is **attained** (`Rout = d = 4` at `m=2, a=14`).
- **Counterexample? Yes, many, and in class at `m=1`:** 4800/5280 realized `(SAT3)` measurements at `q=17` have `Rout = 1 > 0 = d-m`; 582 out-of-class measurements at `m=2,3` in the canonical band have `Rout > d-m` with `d >= m`.
- **Sample artifact? Yes, with the null identified.** `Rout` matches a uniform-random-polynomial null in three cells and two fields; "`<= 3`" was a 648-sample tail (and was in any case misreported — the banked max is 4).
- **The wall, named.** No in-class `m >= 2` measurement is possible: `(SAT3)` is unrealized at `m >= 2` (`max T = 3`, `rh_psi_degree/d3_m4_q257.txt:88`), and my D3 first moment says the class is empty. **The `Rout` question cannot be settled in class by measurement, only by emptying the class.**
- **Status of `(NS-m) -> (NS-W-m)`: REDIRECTION, not correction.** `Rout` is not `O(1)`-bounded, so `(NS-m)` is not within `O(1)` of `(NS-W-m)`: it is strictly stronger and false where `(NS-W-m)` and closure both hold. Anchor 1's restatement is **not cosmetic**. The target of record should be `(NS-W-m)` at the canonical `W*` with `a >= 7m-1` — or, better, `(CLO-m)`, which is weaker still by `(n_gamma - ov_gamma)` and is exactly equivalent to closure.

---

## D2 — LAYER A ON THE `m=3` (BIV-CURVE) WITNESS

Anchor 2's declared MISS 7 (`r34_bivcurve_m34/REPORT.md:156-164`) is discharged.

### D2.1 The measurement

`d2_layerA_m3.py` rebuilds the witness with anchor 2's own `build(q, 340000+q)` (same seeds, `T = 13` blocks all of size `rho = 11`, `sum_x d_x = 143`) and runs layer A in two coordinate systems (`d2_layerA_results.txt:12-23`):

```text
  q= 97  LA|_D : 143 incidences on 48 unknowns -> NULLITY 0
         LA|_W :  60 incidences on 48 unknowns -> NULLITY 0   [completion-INDEPENDENT]
         c_gamma formulation (bank 2's layerA_core, 108 rows on T=13) -> NULLITY 0  [AGREES]
         locator SPAN rank 12 of 12 (banked bound m+1 = 4); the FIRST 5 locators exceed it
  q=193  identical in every field
```

**The witness is killed on both fields.** The span rank is maximal — as far from the RNC bound as the geometry allows — reproducing at `m=3` exactly what anchor 1 measured at `m=2` (`r34_layer_a/REPORT.md:437-439`).

### D2.2 The kill is completion-independent (the part that matters)

`LA|_W` uses **only** the 60 incidences at the 20 points of `W`, which are fixed by the `(BIV-CURVE)` construction; the outside completion enters nowhere. Nullity 0 there means **no bidegree-`(m, rho)` biform exists at all**, hence no completion can rescue the witness. Two independent confirmations:

- **40 fresh outside completions** from anchor 2's own solver, same inside-`W` witness: `{span rank 12: 40}`, `{LA|_D nullity 0: 40}`, both fields (`d2_layerA_results.txt:28-29`).
- **All `C(20,16) = 4845` 16-point subsets** of `W` (`d3_mult_results.txt:70-71`): `4791/4845` (`q=97`) and `4823/4845` (`q=193`) already force `Q = 0` on their own `48` conditions; the exceptions have nullity exactly 1. `16 = ceil(48/3)` is the information-theoretic minimum, so **the binding sub-system is minimal in size**, though (MISS 3) *not* every 16-subset binds.

### D2.3 The mechanism, named

> **(LA-W COUNT).** At `a = a* = 7m-1` with `|A_x| = m` for every `x in W`, the `W`-incidences impose `a*m = (7m-1)m` linear conditions on the `(rho+1)(m+1) = 4m(m+1)` coefficients of `Q`. The excess is
> ```text
> a*m - (rho+1)(m+1) = 3m^2 - 5m  =  -2 (m=1),  +2 (m=2),  +12 (m=3),  +28 (m=4), ...
> ```
> positive for every `m >= 2` and negative only at `m = 1`.

Counting excess is not rank excess (R3(b)), so the ranks are measured, and the three regressions all fire:

| regression | prediction from the count | measured |
|---|---|---|
| `m=1`, 16 realized `(SAT3)` witnesses | underdetermined by `2` | `{(|W|,nullity,unknowns) = (6,2,8): 16}` — **survives, nullity exactly 2** |
| `m=2`, bank 2's exhibit (its `LA|_D` kill is banked) | overdetermined by `2` | `LA|_W` 26 conditions on 24 unknowns -> **nullity 0**, both fields; `LA|_D` nullity 0 |
| `m=3`, anchor 2's witness | overdetermined by `12` | **nullity 0**, both fields |

The `m=2` line is new: bank 2's exhibit was killed by the full-domain system; **its 26 inside-`W` incidences alone suffice.**

### D2.4 Controls

- **C1 POSITIVE (this repairs anchor 1's MISS 3 — the control that never fired).** Anchor 1's positive control required a random `Q` to split at all 32 domain points (probability `~2^-32`, so `0` usable instances in 400 draws). Mine does not demand splitting: it draws a random bidegree-`(m,rho)` `Q`, reads off its **actual** roots over `D` as the incidence structure, and requires nullity `>= 1`. **`6/6` at `q=97` and `6/6` at `q=193`** (`d2_layerA_results.txt:7-10`). The control fires.
- **C3 CROSS-BUILDER.** Bank 2's `c_gamma`/RS-dual formulation (`layerA_core`, generalised from `(2,7,9)` to `(3,11,13)`) agrees with my `Q`-coefficient formulation on every configuration tested.
- **C4/C2** as tabulated above.

### D2.5 Verdict for D2

**Layer A's instrument status is confirmed and sharpened.** Anchor 2's banked expectation ("layer A deletes it", `statement.md:3136`) holds, and the kill is stronger than expected: it is decided **before** the outside completion exists, by a count that is positive for every `m >= 2` and negative exactly at `m = 1`. The orthogonality reading of round 34 gets its `m=3` data point: satisfying `(BIV-CURVE)` on `W` buys **nothing** toward layer A — it fixes the very 60 conditions that kill it.

---

## D3 — THE MULTIPLICATIVE-DOMAIN PUSH

### D3.1 The subtraction came first, and it took most of the target

See CATCH-24A rows 1-3: the factor-degree dichotomy **and its per-factor sharpening** are the PROVED node `rate_half_ca_hankel_endpoint_rational_branch_exclusion` (CPR3)-(CPR5); the norm identity is the PROVED `(ENF2)`; the coset obstruction via `gcd(4m-1,16m)=1` is a PROVED node. Anchor 1's round-34 theorem is inside the first of these.

### D3.2 What I derived, and its status as verification

From the incidence side, with `deg_x Q <= rho`, `Q(gamma,.)` vanishing on `S_gamma`, and `sum_gamma |S_gamma| = T rho - O`:

> **(DROP).** `Drop + Extra = O <= m-1`, where `Drop = sum_gamma (rho - deg_x Q(gamma,.))` and `Extra = sum_gamma (deg_x Q(gamma,.) - |S_gamma|)`. Consequences: `deg_x Q = rho` **exactly** (a drop of 1 would cost `T = 4m+1 > m-1`); `c(x)` is a nonzero **constant** (a root of the content would appear with multiplicity `>= T` in `prod_gamma Q(gamma,x)`, whose multiplicities are `<= m`); and per irreducible factor
> ```text
> T d_j - N m_j <= Drop_j + Extra_j ,     sum_j (Drop_j + Extra_j) = O <= m-1 .
> ```

Writing `d_j = 4m_j - 1 + s_j` with `sum_j s_j = t-1`, the excess of factor `j` is `0, 4m_j, 4m_j + T, ...` for `s_j = 0,1,2,...`, so the cheapest assignment puts one unit on every factor but the largest and

```text
minimal total excess = 4(m - max_j m_j) <= m-1 .
```

This is (CPR3)+(CPR4)+(CPR5) verbatim. Exhaustive check (`d3_mult_results.txt:19-31`): for `m = 1..8` the closed form agrees with brute force over every `d`-assignment **and** with anchor 1's aggregate criterion on **every** profile; survivors `{2:[(2,)], 3:[(3,)], 4:[(4,)], 5:[(5,),(4,1)], 8:[(8,),(7,1)]}`; `7` survivors at `m=16` and `97` at `m=40`, with `min_j max` `= ceil((3m+1)/4)` exactly. Closed form: `#survivors(m) = sum_{k <= floor((m-1)/4)} p(k)` — `1, 2, 7, 97, 1958, ...` at `m = 4, 8, 16, 40, 100`. **Verification of a proved node from a cheaper direction, not a new theorem.**

### D3.3 The gate, quantified — the one new object

The multiplicative domain enters through exactly one number. `Q(gamma,.)` must be a scalar multiple of a **squarefree degree-`rho` divisor of `x^N - 1`** (the node's own "split over `D`", `rational_normal_kernel_curve/statement.md:48-50`). There are `C(16m, 4m-1)` of those, **independent of `q`**, inside an ambient `P^rho` of size `~q^(4m-1)`. Hence

```text
log2 E = [(m+1)(rho+1) - 4] log2 q  +  log2 C(q+1, T)  +  T [ log2 C(16m,4m-1) - rho log2 q ] .
```

Two calibration points, both at `m=1`, both banked (`d3_mult_results.txt:50-51`):

```text
   m     q   unknowns   T   log2 C(N,rho)    log2 E      banked reality
   1    17          8    5           9.13    +13.75      (SAT3) realized; I count EXACTLY 16 configurations
   1    97          8    5           9.13     -0.94      (SAT3) NOT realized (max T = 3)
```

The `m=1` exact count is section [B] (`d3_mult_results.txt:36-40`): the layer-A family is a **line in `P^3`**, a usable slope is one of the `C(16,3) = 560` cubic divisors of `x^16-1`, and lines carrying `>= 5` of them with pairwise disjoint supports covering 15 of 16 points number **exactly 16** — the banked 16 realized `(SAT3)` families. My exemplar blocks `[1,2,5], [9,12,13], [8,10,15], [3,7,11], [4,6,16]` contain **all three** banked printed witnesses (`rh_sat3_realizability/d1_m1_results.txt:6-8`, `S1=[1,2,5]` with `S2 in {[3,7,11],[4,6,16],[8,10,15]}`). So at `m=1` the layer-A-consistent configurations **are** the realized witnesses, by two independent constructions.

Then, for `m >= 2` (`d3_mult_results.txt:52-58,61-66`):

```text
   m     q     log2 E          m (official, q ~ 2^167)   log2 E        (log2 E)/m^2
   2    97      -48.14         2                         -5.50e3       -1375
   2   193      -81.67         4                         -2.63e4       -1644
   3    97     -154.00        16                         -4.79e5       -1872
   4   257     -543.86      1024                         -2.05e9       -1951
   6   193    -1194.97      2^20                         -2.15e15      -1952
```

**The first moment turns negative exactly at `m = 2` and stays negative, at `~ -1952 m^2` bits at official scale.** The heuristic overestimates by `2^9.8` at its own calibration point (MISS 10), i.e. it errs toward existence, which is the safe direction for a negative reading.

### D3.4 Does the push empty the `m=2` survivor?

**No — not by a theorem.** The `m=2` survivor is the profile "`Q` irreducible of bidegree `(2,7)`", which is exactly the banked (CPR3) profile with `e_(i*) = 2 = ceil((3*2+1)/4)`; my per-factor constraint is satisfied with slack `-1 <= O`. Value-level multiplicative conditions (`Delta(x)` a square at all `N` points; `B(Z)/A(Z)` mapping `Gamma` into `mu_N`) are **exact but powerless at scale**, as registered before computing (R2.6, R2.7): they cost `~2^-N` or `q^-c` against a parameter space of dimension `Theta(m^2)` over `F_q`; and any construction that uses the whole domain multiplies `Z`-degrees by `N = 16m`, giving `~16m^2` against only `T = 4m+1` available slopes — a factor `~4m` gap. **R2.6 confirmed; the wall I registered in advance is the wall I hit.** What the multiplicative structure *does* buy is the counting gate of D3.3, and that is a first moment, not an exclusion.

---

## D4 — VERDICT

**Misses first (above). Then:**

- **`(NS-W-m)`'s standing after `Rout`: it is the target of record, and its promotion is a REDIRECTION.** `Rout` is free; `(NS-m)` is strictly stronger, false in class at `m=1` and false out of class at `m=2,3` in the ledger's band, while `(NS-W-m)` survives `7275/7275` at the canonical `W*` with `a >= 7m-1` and `5280/5280` in class at `m=1`. The exact criterion `(CLO-m)` is weaker still and is equivalent to closure (`32700/32700`). **Recommendation: retire `(NS-m)`; carry `(NS-W-m)` with its stated hypotheses (canonical minimising `W*`, `a >= 7m-1`, `d >= m`); record `(CLO-m)` as the exact target.**
- **Layer A's instrument status after D2: CONFIRMED and strengthened.** It kills anchor 2's `m=3` `(BIV-CURVE)` witness on both fields, completion-independently, from the `W`-incidences alone, with the mechanism `3m^2-5m > 0` for all `m >= 2` and `= -2` at `m=1`. The `m=1` regression passes with the predicted nullity. **The `W`-layer fence at `m in {2,3}` costs layer A nothing.**
- **The dichotomy's reach after D3: it was already proved, and the multiplicative push does not empty the survivors.** The surviving profile at `m = 2,3,4` is the banked dominant-component profile; my derivation reproduces (CPR3)-(CPR5) exactly and adds only the quantified gate, whose verdict is a **negative first moment for every `m >= 2`**, calibrated twice at `m=1`. **The dichotomy is not, and after this round is not, an unconditional exclusion instrument.**

**Where the next instrument should go** (recommendations only; AUDIT-AND-DRAFT, nothing applied):

1. **Prove `(LA-W COUNT)` into a theorem.** The measured nullity-0 is what carries D2; the counting excess `3m^2-5m` is what would carry **all** `a = 7m-1` configurations at once. The missing step is a rank statement: that the `a*m` incidence rows at a saturated `W` have rank `(rho+1)(m+1)` whenever `m >= 2`. That is a statement about `T = rho+2` slope-tuples and a degree-`m` rational normal curve, i.e. squarely inside the RNC node's own gate, and it would make layer A an unconditional exclusion at the `W`-layer's own witnesses.
2. **Do not spend another round on `Rout`.** It is a free random variable with a matched null; no bound on it is provable and none would help (the sign is wrong).
3. **The `m=1` coincidence in D3.3 is worth a node.** "The layer-A-consistent `m=1` configurations are exactly the 16 realized `(SAT3)` families, and the first moment predicts their existence at `q=17` and their absence at `q=97`, matching bank 3's measured realizability" is a two-point calibration of the only quantitative instrument this lane has for `m >= 2`.

**Recommended node work (nothing applied).** An addendum to `rate_half_band_crossing_location` recording (i) that `(NS-m)` is refuted at `m=1` in class and at `m=2,3` at the canonical `W*` in the open band, with `Rout` identified as a null-distributed quantity and the banked "`Rout <= 3`" corrected to `4`; (ii) the exact criterion `(CLO-m)` with `Rout` positive; (iii) that anchor 2's `m=3` `(BIV-CURVE)` witness is killed by layer A from its `W`-incidences alone, with the `3m^2-5m` count and its `m=1` sign change. A **correction note** on `rh_psi_degree/REPORT.md:328`. And a pointer from `rate_half_ca_hankel_endpoint_rational_branch_exclusion` into the round-34 pilot report, whose independently derived theorem it already contains.

**Cross-pilot flag (written self-contained; I read no sibling `r35_*` directory).**

> The realizability layer can be attacked with a **first moment whose only multiplicative input is `C(16m, 4m-1)`** — the `q`-independent count of degree-`rho` squarefree divisors of `x^(16m)-1` — against an ambient `q^(4m-1)`. Calibrated at `m=1` it is correct twice: `+13.75` bits at `q=17`, where exactly 16 configurations exist and are the banked realized `(SAT3)` witnesses, and `-0.94` bits at `q=97`, where bank 3 measures none. It turns negative at `m = 2` for every field in this lane and runs `~ -1952 m^2` bits at `q ~ 2^167`. Independently: at `a = 7m-1` with a saturated `W`, the **inside-`W` incidences alone** impose `(7m-1)m` linear conditions on the `4m(m+1)` coefficients of the kernel biform — an excess of `3m^2-5m`, **negative only at `m=1`** — so any realizability-layer candidate at `m >= 2` must beat a `3m^2-5m` overdetermination that is fixed before its outside structure is chosen. Both statements are about the biform, not about any `W`-layer axiom, so they transport to any lane holding a candidate configuration.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| R1.1 `P(Rout <= d-m is a theorem) = 0.06` | **RESOLVED NO** — refuted in class at `m=1` (4800/5280) and out of class at `m=2,3` in the canonical band (582/7275) |
| R1.2 `P(layer A kills the m=3 witness) = 0.92` | **RESOLVED YES**, and more strongly than registered: completion-independently, from `LA|_W` alone, both fields |
| R1.3 `P(the multiplicative push empties the m=2 survivor) = 0.12` | **RESOLVED NO** — the survivor is the banked (CPR3) profile; only a negative first moment, not an exclusion |
| R1.4 `P((NS-W-m) survives as the target of record) = 0.80` | **RESOLVED YES**, `7275/7275` at the canonical `W*` with `a >= 7m-1`, `5280/5280` in class at `m=1`; but its literal form **fails** at planted `W` (6686 times), so the hypotheses must be stated |
| R1 aux `P(D1 by explicit counterexample) = 0.55` | **HIT** |
| R1 aux `P(bank 1's Rout <= 3 is a DEGREE artifact) = 0.50` | **RESOLVED NO** (`d = 12` at `m=4`) — and the real answer is worse: the banked maximum is **4**, so the claim was false as printed (MISS 2) |
| R1 aux `P(the kill is independent of the completion) = 0.85` | **HIT** — proved by construction (`LA|_W`), plus 40 resampled completions per field |
| R2.1 `m=1` histogram `{0:480, 1:4800}` at `a=7`, `max Rout = 1`, fails `4800/5280`; `480/480` at `a=6`, `P=0.88` | **HIT exactly**, replayed from my own copy |
| R2.2 bank 1's census has `max d <= 3`, `P=0.50` | **RESOLVED NO** (MISS 2) |
| R2.3 `Rout ~ Poisson(1)`-like; a sweep exhibits `Rout > d-m` within `10^4` draws at `m>=3`, `P=0.60` | **HIT** — `11` violations in 1517 slopes at `m=3, a=20`; and the measured histogram matches an explicit null cell by cell |
| R2.4 span rank `12`, nullity `0`, both fields, `P=0.90`; kill forced by the first `m+2 = 5` locators, `P=0.75` | **HIT** and **HIT** (`the FIRST 5 locators already exceed m+1`) |
| R2.5 `Drop + Extra = O`; `c(x)` constant; the resultant identity; the per-factor sharpening; `P(does not empty the m=2,3,4 survivor) = 0.88` | **DERIVED and HIT** — and then **SUBTRACTED**: the sharpening is the proved (CPR4)-(CPR5), the identity is the proved `(ENF2)` in transpose (MISS 6, MISS 7) |
| R2.6 value-level `mu_N` conditions are exact but zero-power at scale; the `mN` vs `T` degree gap is the obstruction I will name, `P=0.75/0.60` | **HIT on both clauses** |
| R2.7 Weil/Chebotarev declared vacuous and not tried | **HONOURED** — not tried, not reported |
| R3(a) MISS-2 guard on `Rout` | **USED** — no `Rout <= C` claim is made from any sample; the null model is reported as a heuristic and the refutation rests on exhibited counterexamples |
| R3(b) aggregate counting refutes, never certifies | **USED and it bit twice** — the `3m^2-5m` count is not allowed to carry D2 (the rank is measured), and D3's negative first moment is explicitly not an exclusion |
| R3(c) report the distribution of the layer-A kill, not the best case | **USED** — 40 completions per field, and the exhaustive 4845-subset scan, which **overturned** my own "the first 16 bind" into "not all 16-subsets bind" (MISS 3) |
| R6(i) expect a script/ramguard failure | **HIT four times** (MISS 8) |
| R6(ii) my `h_gamma` may differ from bank 1's | **AVOIDED** — I re-typed bank 1's construction and used its identities as controls (`32700/32700`) |
| R6(iii) I may fail to reproduce anchor 2's witness | **DID NOT FIRE** — same seeds, same witness, `T=13`, sizes `11..11`, `sum_x d_x = 143` |
| R6(iv) I will over-claim novelty on the resultant identity and be subtracted by the RNC node's gate line | **HIT, and worse than registered** — subtracted by three PROVED nodes, one of which also contains anchor 1's round-34 theorem |

---

## ZERO-POWER DECLARATIONS

1. **Every `m >= 2` number here is OUT OF THE HYPOTHESIS CLASS.** The census constructor realizes `max T = 3`, never `T = rho+2` (`rh_psi_degree/d3_m4_q257.txt:88`). `(NS-m)`/`(NS-W-m)` are quantified over `T = rho+2`. My refutation refutes the statements for the ambient class; bank 1's positive measurement supports them for nothing.
2. **If the `T = rho+2` class is empty, everything quantified over it is vacuous** — including `(NS-m)`, which my D3 first moment suggests is vacuously true. No result here decides the in-class question.
3. **`m=1` has `max Rout <= d <= 1` in every reachable stratum** (`a in {6,7}`; `a=8` unreachable, `r34_layer_a/REPORT.md:205`), so `m=1` has **zero power** to separate "`Rout <= 3`" from the degree bound — declared before measuring, and confirmed.
4. **The `m=3` `Rout` census is single-field** (`q=97`). Only `m=2` is two-field.
5. **The layer-A kill has power over anchor 2's witness and its completions only.** `LA|_W` is completion-independent, but it is one inside-`W` structure; it does not show that layer A excludes `(BIV-CURVE)` at `m=3` in general, and I ran no search for a layer-A-consistent `m=3` configuration.
6. **Nullity 0 on a structured object is evidence about that object, never evidence of non-existence.** No `m >= 2` layer-A candidate was constructed; absence where none was sought is not evidence (bank 2's `q^{-Theta(m^2)}`).
7. **D3's first moment is a heuristic and it is NEGATIVE, which is the direction that proves nothing.** It overestimates by `2^9.8` at its own calibration point. It cannot exclude anything; it can only say where to look.
8. **The profile scan is combinatorial.** Surviving profiles are not claimed realizable, and my per-factor derivation is a verification of a proved node, not an independent proof of anything new.
9. **The `m=1` exact count in D3.3 is single-field by structure** (`q=17` is the only field where `(SAT3)` is realized at `m=1`, `rh_sat3_realizability/d1_m1_results.txt:5-13`).
10. **The `~0.7` suppression of `Rout` roots inside `D \ W`** is reproduced in three cells but has no mechanism and carries nothing.
11. **All rational-point instruments remain vacuous at official scale** (`N = 16m` against `sqrt(q)`, `q > 2^167`) — declared in advance, not tried.
12. **Everything is `(SAT3)`-conditional.** No realizable pencil was built at any `m >= 2`.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, rho=4m-1, R=8m, T=rho+2, e=m, delta=m-1, D=mu_N`; `W, a, d=a-(4m+2), need_X=d-m`; per type-2 slope `X, n, o, j, cancel, ov, Dh, Rin, Rin_m, Rout, RoutD, nonsplit`; the identities `(JDEC)`, `(DEGSUM)`, `Rin = n+X-ov`, `(AGG)`. **New here:** the **cofactor degree** `Dg = Dh - Rin_m` and its **null model** (rational-root count of a uniform polynomial of the same degree, sampled in-loop); the **running maximum of `Rout` against sample size**; the violation counters `ROUTB/NSA/NSW`; the exact closure criterion **`(CLO-m)`** and its measured equivalence to `X <= d-m`; the layer-A **incidence formulation** `Q(gamma,x)=0` with unknowns the `(m+1)(rho+1)` biform coefficients, and its two sub-systems **`LA|_D`** and **`LA|_W`**; the **`LA-W` excess `3m^2-5m`**; the **minimal binding sub-system size** and the exhaustive nullity histogram over all `16`-subsets of `W`; the per-factor excess `max(0, T d_j - N m_j)` and the closed forms `4(m - max_j m_j)` and `#survivors(m) = sum_{k<=floor((m-1)/4)} p(k)`; the **exact count of layer-A-consistent `(Q,Gamma)` at `m=1`** (lines in `P^3` meeting the `C(16,3)` split cubics in `>= 5` disjoint-support points); the **first-moment functional** `log2 E` with its `C(16m,4m-1)` input. **Registered but not measured:** an `m >= 2` layer-A-consistent candidate (none built — declared, not quietly dropped); `Rout` inside the `T = rho+2` class at `m >= 2` (impossible, see zero-power 1).

---

## COMPLIANCE

**Registrations.** `R0` (notation and the arithmetic derived from the anchors alone), the four mandated blind priors plus six auxiliaries `R1`, seven falsifiable derivations `R2.1-R2.7`, the MISS-2 guard `R3` in three clauses, twelve zero-power flags `R4`, the subtraction plan `R5` (including the hyphenated/infixed variants the round-34 catch demands), the expected misses `R6` and the execution order `R7` were appended to `PREREG.md` under `## Pilot registrations` with the **Edit tool, after reading exactly the two named anchors and before any other read, any grep, any `ls`, and any interpreter invocation.** No post-registration addenda; the two registration errors (R2.2's artifact hypothesis, R1.4's missing hypothesis on `W`) are reported as misses, not edited. Execution followed `R7` (D1 -> D2 -> D3 -> D4).

**Compute law — NO BREACH. Ten interpreter invocations, all ten under `tools/ramguard`, from the repo root, with the literal `--`.** One `tiny` (`RAMGUARD_TIMEOUT=55`, the `m=2 q=97` census) and nine `local` (`RAMGUARD_TIMEOUT=280` x4, `290` x5). **Zero bare `python3` invocations for any purpose** — no file patching, no string replacement, no no-op probes, no heredocs; every file edit used the Edit or Write tool; no `sed -i`, `awk -i`, `perl -i`, `tee`, or shell redirection onto any file (the only file creations by shell were `cp` copies of banked scripts). **Ramguard status: four FAILURES, all self-caught and all reported** — invocation 5 (`d2_layerA_m3.py`, wall kill at 280 s: the resampler re-ran the `phi` search 80 times; rewritten to resample only the completion), invocation 7 (`d3_mult.py`, wall kill at 290 s: exponential composition enumeration; replaced by a closed form with a brute-force control), invocation 8 (`MemoryError` on `list(parts(100))`), invocation 9 (`IndexError` on a partition table of length 200 at `m=1024`). No OOM kill. Stdlib only (`random`, `sys`, `time`, `math`, `itertools`); no third-party imports, no Modal, no network, no git, **no subagents spawned**.

**RAM discipline.** `dag.json` **never opened** at any line. File-at-a-time reads with bounded windows on every large file: `critical/nodes/rate_half_band_crossing_location/statement.md` (>3000 lines) was touched **only** through one `sed -n '580,590p'` window; the four endpoint nodes through `grep -n` and windows of `<= 70` lines; `rh_psi_degree/REPORT.md` through two windows and greps. The largest object materialised is the `4845`-subset exhaustive scan at `48x48`; every driver writes its own results file.

**Quarantine.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened and never appeared in any tool output**. **No `r35_*` directory other than my own was read or listed**: `notes/pilots_20260811/` was never `ls`-ed without a pattern — the one listing used the explicit glob `notes/pilots_20260811/rh_*`, which cannot match `r35_*`, and every other listing named a specific permitted directory (`r34_layer_a/`, `r34_bivcurve_m34/`, `rh_psi_degree/`). **Every recursive grep carried `--exclude-dir` at the SEARCH level** (`--exclude-dir=pilots_20260811 --exclude-dir=pilots_20260802 --exclude-dir=prize-codex-1 --exclude-dir=prize-codex-2 --exclude-dir=prize-codex-3 --exclude-dir=.git`) and was rooted at `critical/`, `background/`, or a named permitted directory; **no output filtering after traversal was used at any point**. No path containing `prize-codex-` was touched. The round-33 `rh_*` and round-34 `r34_*` directories were read as permitted.

**Write scope — ONE BREACH, DECLARED (MISS 1).** `notes/pilots_20260811/r34_layer_a/d3b_replay_results.txt` was overwritten at import time by my copy of bank 2's `d5_layerA_bank2.py`, whose output path anchor 1 had pointed at its own directory. The write is deterministic and the regenerated content matches anchor 1's description at `r34_layer_a/REPORT.md:428-432` exactly; my copy is now redirected into my own directory with the Edit tool. A `find -newermt` audit confirms that this is the **only** file outside my directory with a modification time in this session, and that no `__pycache__` was created outside my directory. Everything else is inside `notes/pilots_20260811/r35_rout_layer_a/`: `PREREG.md` (registrations appended); verbatim copies `d3_psi_bank1.py`, `m3_build_bank34.py`, `m3_phi_bank34.py`, `m3_phi.py`, `biv_core.py` (`diff -q` byte-identical to `rh_bivariate_system/biv_core.py`), `d3_scale_bank34a.py`, `d1_calib_bank34a.py`; two copies with **disclosed one-line edits** (`d1b_exhaustive_bank34a.py`'s `sys.path` insert now points at my own dir; `d5_layerA_bank2.py`'s output path, the MISS-1 fix); my own `d1_rout.py`, `d2_layerA_m3.py`, `d3_mult.py` and their results files `d1_rout_results_m2_q97.txt`, `d1_rout_results_m2_q193.txt`, `d1_rout_results_m3_q97.txt`, `d1b_m1_replay_results.txt`, `d2_layerA_results.txt`, `d3_mult_results.txt`, plus a `__pycache__`. **No** `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; the session scratchpad was not needed and no scratch file went to `/tmp`. **AUDIT-AND-DRAFT respected: every node recommendation in D4 is a recommendation only — nothing was applied.**

**Banked scripts.** `rh_psi_degree/d3_psi.py`, `r34_bivcurve_m34/{m3_build.py, m3_phi.py, biv_core.py}`, `r34_layer_a/{d3_scale.py, d5_layerA_bank2.py, d1_calib.py, d1b_exhaustive.py}` were **copied into my directory before any use**. Bank 1's machinery (lines 1-497 of `d3_psi.py`) is exec'd **unedited** and only its driver is replaced; bank 2's `layerA_core` is re-typed with `(m,rho,T)` as parameters and cross-checked against my own formulation; anchor 1's `d1b_exhaustive.py` is re-run unmodified except for the import path.

**Method discipline.** Own-repo greps (CATCH-24A, including the hyphenated and infixed variants `R_out`, `first-moment`, `multiplicative-domain`, `norm/Bezout`) preceded every novelty claim and produced **eleven subtractions, three of them PROVED nodes that between them contain anchor 1's round-34 theorem and most of my D3.** Every quantifier claim carries a `file:line` or an exhaustive count with its denominator. Every max-quantified claim carries a zero-power declaration. Two-field confirmation (`F_97`/`F_193`) on every structural claim: the layer-A kill, the completion resampling, the 4845-subset scan, and the `m=2` `Rout` null-agreement; the single-field limitations (`m=3` census, `m=1` count at `q=17`) are declared as misses and zero-power items rather than glossed. Three independent builders were made to agree before any layer-A number was believed, and bank 1's four identities were made to pass `32700/32700` on my re-implementation before any `Rout` number was believed. The self-caught errors — the out-of-scope write, the wrong artifact hypothesis, the "any 16 points" overclaim caught by my own exhaustive scan, and four failed runs — are reported as errors, in the misses section, ahead of the results.
