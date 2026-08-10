# REPORT.md — apolar_origin (round 28) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a408f7a74c40910fa, 2026-08-10. Pilot: Opus. No edits.

## REPORT — apolar_origin (round 28)

## VERDICT (first)

**The named theorem did NOT land — at neither budget, and not on the sharp face `e=m` in full.** Both wave-10 residual budgets `{2^39, 2^39+1}` remain open and their status is unchanged. What landed is a *mechanism* plus three genuine theorems and one per-stratum closure covering asymptotically **one third** of the admissible parameter range of the strict `e=m` endpoint.

The payoff chain re-derives correctly from primary text, with one precision catch: closing budget `2^39+1` extends the bracket top from `q &gt;= 2^169` to **`q &gt;= 2^167 + 2^128`**, not to "all `q &gt; 2^167`" as the crossing-location node and the round-27 report both phrase it. The uncovered sliver `(2^167, 2^167+2^128)` has `B* = 2^39` exactly, where the improved far-CA cap `2^39+1` still exceeds `B*`. Relative size `2^-39`; the 2-bit extension figure survives (`2^169/(2^167+2^128) = 4.000000` exactly).

## MISSES FIRST

**CATCH-24A (own-repo grep before any "missing ingredient" claim) — the apolar origin is not missing, and my D1 mechanism is a PORT, not an invention:**

- `background/nodes/rate_half_ca_hankel_minimal_index_budget` already names `Q_Z` "the apolar generator" and states the proof uses the divided-power apolar action with the syndrome Hankel matrix as *the literal catalecticant*.
- `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve` (PROVED) already gives the degree-`m` rational normal kernel curve and already names the residual gate verbatim: "a rigidity theorem for this rational normal kernel curve together with its Hankel/apolar origin".
- `background/nodes/rate_half_ca_hankel_endpoint_norm_factorization` (PROVED) already holds the norm-power identity `J R = H^rho S` and the product-code reading `(ENF6)`.
- **Decisive:** `background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_minimal_support_uniqueness` and `..._quotient_minimal_support_packing` (both PROVED) already run *exactly my species of argument* — minimum-weight-coset uniqueness, disjoint cancellation sets, `(QMU5) floor(2e/(h-1))` packing, and `(QMP1) lambda_h = 2h-2e-4` MDS intersection bounds — on the `A=1` core-one exceptional-only quotient face. My contribution is porting it to the **full strict `A=3` pencil** (not a core quotient) and the two-code dichotomy, not inventing it.
- `background/nodes/rate_half_ca_hankel_distance_three_e1_hankel_design_route_fence` (PROVED) is a *second* design-vs-Hankel fence the brief did not name.
- The `m=1` fence's own statement already says the failure survives "even after imposing core-freeness and **the full Hankel/apolar origin**" — so "add the apolar origin" was never going to be sufficient by itself, and it was not.

**Registered prediction misses:**

- **P6 width MISS (bound better than registered).** I registered the `(AO1)` closing `a`-window width in `[1,4]` for `m in [2,40]`. Measured widths run `3 .. 52` and grow linearly; the window is `[rho+1, ~16m/3]`. Registered floor and ceiling both wrong.
- **P6 `m=1` MISS (nominal).** I registered width `0` at `m=1`; nominal width is `2` (`a in [4,5]`). It is `0` *effective* once the separately-proved `w* &gt;= 4m+2` is imposed — the fence's `w*=6` is outside. Reported as a partial miss with the correction.
- **A2 FALSIFIED at every field.** I registered the mean collinear-triple count per `W` as `C(120,3)/q^4` (3.36 at `q=17`, `&lt;=0.05` at `q&gt;=97`). Measured: **840.000 at `q = 17, 97, 113, 193, 241` alike** — flat in `q`. My heuristic was simply wrong; the count is dominated by a field-independent structured family. This miss produced the session's best structural finding (below).
- **A3' MISS low.** Corrected sporadic rate at `q=17`: registered `[0.5, 12]`, measured `0.167` per `W` (1 sporadic triple in 6 sampled `W`). Direction right, magnitude ~3x low.
- **P8 PARTIAL / NOT RUN as posed.** I did not run a genuine `m=2` realizable-pencil search for `T = rho+2 = 9`; I ran the weaker `(AO2)` line search (120 random lines per `W`, max collinear `= 2`, need `6`). The arithmetic half of P8 is exact (`9*7 = 63 &gt; 32`).
- **P10 (registered in advance) HIT as a miss:** the uniform theorem did not land.

## DELIVERABLES

All under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/apolar_origin/`:

- `PREREG.md` — brief + my registrations (M0 grep gate, R0–R5, P1–P10) appended with Edit **before any interpreter run**; two clearly-marked post-registration addenda (A1–A4), each appended before the run it predicts.
- `e1_real.txt`, `e2_cyclo.txt` — escape replays from scratch copies, **both byte-identical** to the round-27 banked results.
- `d1_charC.py` + `d1_charC_results.txt` — characterization `C` measured on the `m=1` fence and on all three realizable cyclotomic solutions.
- `d2_scan.py` + `d2_scan_results.txt` — P4/P5/P6/P7, plus the R3/R4 arithmetic.
- `d3_collinear.py` + `d3_collinear_results.txt` — the extremal normal form `(AO2)`, first (falsified) field census.
- `d5_sporadic.py` + `d5_sporadic_results.txt` — the corrected structured/sporadic census.
- `d6_stratum.py` + `d6_stratum_results.txt` — uniqueness legality on both official profiles; `w*` window; the closed sub-stratum priced.
- `d4_payoff.py` + `d4_payoff_results.txt` — D4 re-derivation from primary text.

## WHAT LANDED

**(1) The mechanism, stated exactly (D1).** Put `K = {c in F^D : sum_x c_x x^i = 0, i&lt;R}`, the `[N, N-R, R+1]` MDS kernel code, and `K' = {psi : sum_x psi_x x^i = 0, i&lt;=R-r-1}`, `[N, N-R+r, R-r+1]` MDS. The apolarity relation `M_r(y_0+Zy_1)Q(Z)=0` is *literally* `sum_x (c_{0,x}+Z c_{1,x}) x^i Q(Z;x) = 0`, i.e. the `F[Z]`-word `Psi(Z) = ((c_{0,x}+Zc_{1,x})Q(Z;x))_x` is a codeword of `K'` of `Z`-degree `&lt;= e+1`. Consequences, all measured and all holding:

- **(C0)** every supported slope's locator root set `S_gamma` is the support of the *unique* minimum-weight representative of the coset `y(gamma)+K` — legal because `2 rho &lt; d(K) = R+1` on **both** official profiles (margins exactly 3 and 1).
- **(C1) injectivity:** `gamma |-&gt; S_gamma` is injective on supported slopes (two equal supports of size `&lt;= r` would make the pair jointly supported on `&lt;= r` points, i.e. not column-far).
- **(C2) dichotomy** relative to any joint support `W`, `a=|W|`: type-1 (`S_gamma = W\K_gamma`) or type-2 (`|S_gamma \ W| &gt;= R+1-a+n_gamma`).
- **(C3)** type-1 slopes are the common roots of `Psi(Z)`, so `T_1 &lt;= e+1`.

**(2) `C` separates the two banked certificates with no linear algebra (P3, P4 — both exact).** On the `m=1` fence: `S_gamma` = the five `(M1F3)` triples, pairwise disjoint, `w* = 6`, `T_1 = 2`, `T_2 = 3`, every type-2 slope meeting `|S\W| &gt;= R+1-a = 3` and `|S n W| &lt;= 0` **with equality**; `(AO1) = 5 = rho+2`. On the `N=28` design 9-line: the type-2 requirement is `|S\W| &gt;= 15-6 = 9 &gt; 3 = |S|`, contradiction margin exactly `6`, `T` forced to `2` — matching round-27's measured `nullity = 0` **without touching the Hankel system**.

**(3) Cyclotomic exclusion at OFFICIAL scale, uniform in `q` (R3, new).** By `(C1)`, if the supported root sets are cosets of a fixed `mu_rho &lt;= mu_N` then `T &lt;= N/rho`. At the official `A=1` half-distance profile (`rho = 2^39`, `N = 2^41`) this is `T &lt;= 4`, against a target of `2^39+1` — margin `549,755,813,885`. At the strict `A=3` profile the family is empty (`16m mod (4m-1) = 4 != 0`). **Round-27's single field-independent structural threat to budget `2^39+1` is therefore dead at the official parameters, by proof rather than by small-scale census.** `(C1)` also reproduces the round-27 cyclotomic law on 7/7 rows: over-target rows have `design T &gt; N/rho` (repeated supports, hence not column-far, hence nullity 0); at-or-below-target rows have distinct supports and positive nullity.

**(4) The `w*` window (new).** An unsupported generic-rank slope has coset weight `&gt;= R+1-rho = 4m+2` (else its minimal LFSR polynomial would divide a split locator and the slope would be supported), and `w* &lt;= |S_i u S_j| &lt;= 2rho`. So `w*` is forced into `[4m+2, 8m-2]`. This *kills* the naive clean case `w* &lt;= rho+1`, which is empty — a self-correction, see below.

**(5) The per-stratum closure (the bankable partial).** With `(AO1) = min(e+1, floor(a/(a-rho)), floor((a e + O)/rho)) + floor((N-a)e/(R+1-a))` at `a = w*`:

&gt; **`T &lt;= rho+1` on the strict `e=m` endpoint whenever `O = 0`, `m &gt;= 2`, and `w* &lt;= a_max(m)`,** where `a_max(m)/m -&gt; 16/3`. Measured: `m=2` closes `{10}`; `m=8` closes `[34,42]`; `m=2^20` closes `[4194306, 5592403]` — asymptotically exactly **1/3** of the admissible `w*` range `[4m+2, 8m-2]`.

The `m=1` control is exact: at `m=1` the `w*` window degenerates to `{6}` and the closed set is **empty** — the fence sits precisely outside, by hypothesis `m &gt;= 2` (and `q = 17` forces `m = 1`, since `N = 16m | q-1 = 16`; this is the brief's required explicit exclusion). The **unclosed** stratum is large-`w*`, and that is where the average configuration sits: `sum_x C(d_x,2)` forces mean `|S_i n S_j| ~ m-1`, i.e. mean `|S_i u S_j| ~ 7m-1 &gt; 16m/3`. So this closure does not move either budget's status.

**(6) The extremal normal form and the `q=17` artifact, explained (post-registration).** In the extremal type-2 case (`n_gamma=0`, `S_gamma n W = {}`, `a+rho = R+1`), `kappa_gamma = z_gamma - v_gamma` is a *minimum-weight* codeword of the MDS code `K`, hence explicit: `kappa_x = 1/sigma'_{W u S}(x)`. Restricting to `W`,

```
z_gamma|_W  ~  P_S := [ 1/(sigma'_W(x) sigma_S(x)) ]_{x in W}  in  P^(a-1),
```

so **extremal type-2 slopes are exactly the points of the "reciprocal-locator" set `{P_S}` lying on the pencil line.** Two facts, both measured:

- **Structured lines exist over every field:** for any `(rho+1)`-subset `U` of `D\W`, `P_{U\{u}} = [A - uB]`, so those `rho+1` points are always collinear (verified: exactly 4 at `m=1`, exactly 8 at `m=2`). They are **killed by the banked counting layer**: their supports give `d_x = rho`, against `d_x &lt;= e = m`, and `4m-1 &gt; m` always. This is why the flat `840 = C(10,4)*C(4,3)` count appears at every field.
- **Everything else is sporadic and dies with `q`:** measured sporadic collinear triples per random `W` — `q=17`: `0.167`; `q = 97, 113, 193, 241`: `0.000` (0 over 24 samples). And the fence's *own* `W = {1,2,3,5,7,11}` at `q=17` has **exactly one** sporadic triple, which is exactly its three type-2 supports `{(4,6,16),(8,10,15),(9,12,13)}` (A4 hit, window `[1,30]`).

So the `m=1`/`q=17` violation is now mechanically located: it is a *sporadic* collinearity of the reciprocal-locator point set that `q=17` happens to supply. At official scale the residual asks for `~3m` sporadically collinear points in `P^{4m+1}` over `q &gt; 2^167` — heuristically `q^{-(3m-2)4m}`, i.e. nil. **That is a heuristic, not a proof, and I flag it as such.**

**(7) The disjoint-support fence (R4).** A column-far pencil with pairwise-disjoint supported root sets needs both `A &lt;= rho` and `T rho &lt;= N`. At `A=3`, `T rho &lt;= N` reads `(4m+1)(4m-1) &lt;= 16m`: true **only at `m=1`**. The same test refutes the `N=28` 9-line via `A = 9 &gt; 3 = rho`. One criterion, both banked certificates.

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| P1 | `d1_realizability.py` scratch replay exact | **HIT** — byte-identical |
| P2 | `d1_cyclotomic_threat.py` scratch replay, 7/7 | **HIT** — byte-identical |
| P3 | fence under `C`: supports, disjoint, `w*=6`, `T_1=2`, `T_2=3`, `|S\W|=3` with equality, `(AO1)=5` | **HIT exact, all six numbers** |
| P4 | `N=28` 9-line refuted by `C`, margin 6, `T` forced to 2 | **HIT exact**, agrees with nullity 0 |
| P5 | cyclotomic law = `C1`, 7/7 sign agreement | **HIT 7/7** |
| P6 | closure at `a=4m+2, O=0` for all `m&gt;=2`; width in `[1,4]`; `m=1` width 0 | **split: closure HIT; width MISS (3..52); `m=1` nominal 2 / effective 0** |
| P7 | `(AO1)(m=2,a=10,O=1) = 9` | **HIT exact** |
| P8 | no `m=2` `T=9` witness; `63 &gt; 32` | **arithmetic HIT; search NOT RUN as posed** (weaker `(AO2)` search: max collinear 2, need 6) |
| P9 | `2^34` and `n=2^41` bracket-end caps; `(169,167)` pair | **HIT exact**, plus a precision correction (`2^167+2^128`) |
| P10 | partial landing, not the uniform theorem | **HIT (as a registered miss)** |
| A1 | fence's three type-2 supports exactly collinear | **HIT** |
| A2 | mean triples `~C(120,3)/q^4` | **FALSIFIED at every field (840 flat)** |
| A2' | structured line size exactly `rho+1`, `d_x = rho`, counting-excluded | **HIT** (4 at `m=1`, 8 at `m=2`) |
| A3' | sporadic: `q=17` in `[0.5,12]`; `q&gt;=97` in `[0,0.05]` | **MISS low at `q=17` (0.167); HIT at all `q&gt;=97` (0.000)** |
| A4 | `sporadic_trip(W_fence) in [1,30]`, random `W` ~0 | **HIT (=1, and it *is* the fence's triple)** |

## SELF-CORRECTIONS

1. **A vacuous first theorem, caught by my own bound.** My initial clean hook was "if `w* &lt;= rho+1` then `T &lt;= rho+1`". I then proved `w* &gt;= 4m+2 = rho+3` is *forced*, so that hook is empty. Replaced by the `(AO1)` bound and the `w*`-indexed stratum.
2. **A2's heuristic was simply wrong** and was falsified at every field before I could lean on it. I disclosed it, appended ADDENDUM 2 with the corrected model **before** re-running, and the miss is what produced the structured/sporadic dichotomy — the best finding of the session.
3. **P6's registered window was too pessimistic in both directions**; the `(AO1)` closure band is far wider than I predicted, and its `m=1` value needed the separate `w* &gt;= rho+3` fact to read correctly.
4. **The extremal normal form `(AO2)` was derived after computation began.** It is a consequence of the registered `C2`, not an independent hypothesis, and I registered it (with A1–A3) before running the experiment it predicts. Every number it produced is labelled post-registration.
5. **D4 precision catch against primary text.** `critical/nodes/rate_half_band_crossing_location/statement.md` line 65 and the round-27 report both say closing budget `2^39+1` extends the bracket top "to all `q &gt; 2^167`". Re-derivation from `rate_half_half_distance_safe_bracket` gives `q &gt;= 2^128 * (2^39+1) = 2^167 + 2^128`. The `2^169` figure itself reproduces **exactly** (`2^128 * n`, `n = 2^41`), as do the `2^34` lower-end cap (`rho &lt;= R-r = 2^34`) and the one-slope deficit (`4m+1` vs `rho+1`, difference exactly 1).
6. **I over-claimed nothing about m=2 realizability**: no genuine search was run there, and I say so rather than dressing up the `(AO2)` line search as one.

## MEASURED FUNCTIONALS (CATCH-19C)

`w(y)` = minimum weight of a `D`-representation of syndrome `y` (coset distance); `w*` = minimum joint support size of the pair, column-far iff `w* &gt; r`; `S_gamma` = support of the unique minimum-weight representative at slope `gamma`, `u_gamma = |S_gamma| = rho - o_gamma`; `n_gamma` = number of `x in W` with `c_{0,x}+gamma c_{1,x} = 0`; `d_x` = number of supported slopes whose locator vanishes at `x`; `O = sum_gamma (rho-u_gamma)`; `T`, `T_1`, `T_2` = supported / type-1 / type-2 slope counts; `(AO1)` = my `w*`-indexed replacement cap; `P_S` = the reciprocal-locator point `[1/(sigma'_W(x)sigma_S(x))]_{x in W}`; `struct(W)` / `spor(W)` = structured / sporadic collinear triple counts of `{P_S}`; `collin(W)` = max points of `{P_S}` on one line; `cap_ERC2`, `nullity`, `Tmax_cf` retained from round 27 for the replays.

## COMPLIANCE

Registrations (CATCH-24A grep gate M0, notation R0, characterization `C` = R1, route order R2 = (b) then (c) then (a), claims R3/R4, the explicit `m &gt;= 2` / `q = 17` exclusion R5, and predictions P1–P10 with numeric windows) were appended to `PREREG.md` with the **Edit tool before any interpreter run**; two post-registration addenda are marked as such and each precedes the experiment it predicts. Quarantine held: I never opened `notes/pilots_20260802/CAMPAIGN_LEDGER.md` at any line, and never read `ssparse_endpoints`, `maxscan_algorithm`, or `mca_safe_rewire`; no subagents were used, so the clause needed no propagation. Every interpreter invocation ran under `tools/ramguard tiny|local` from the repo root with `RAMGUARD_TIMEOUT` documented (120, 180, 280, 300, 600, 2400, 3000) — **no exceptions this session**, including the JSON-free file work; all authoring used Write/Edit. The two banked round-27 scripts were run only from **unmodified scratch copies** staged in the scratchpad, and both reproduced byte-identically. RAM discipline: file-at-a-time reads, `dag.json` never opened (node shards and grep only), no bulk loads, two long jobs backgrounded to results files, no cap hits. Draft-only respected: every write is inside `notes/pilots_20260810/apolar_origin/` (plus the session scratchpad); no `dag/`, `nodes/`, or `tools/` edits, no git, no Modal, stdlib only.
