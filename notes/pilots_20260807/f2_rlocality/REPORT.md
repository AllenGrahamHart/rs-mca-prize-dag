# REPORT — f2_rlocality (persisted verbatim by the coordinator from the session transcript, task a147942949e1e2b9a, 2026-08-07)

All work is complete: 47 PASS / 0 FAIL across four verifier logs, everything inside the pilot directory.

---

# THE 8.60 R-LOCALITY DEFICIT — PILOT REPORT (mystery 2 / F2, round 22)

**Opus 5, 2026-08-07.** Files (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/f2_rlocality/`): `PREREG.md` (coordinator brief + my registrations §A–F, appended before any computation), `PROOFS.md`, `rl_lib.py`, `lp_lib.py`, `verify_d1.py`, `verify_d2.py`, `verify_d3.py`, `verify_d3b.py`, `VERIFY_D1.txt`, `VERIFY_D2.txt`, `VERIFY_D3.txt`, `VERIFY_D3B.txt`, `VERIFY_LOG.txt` (concatenation, **47 PASS, 0 FAIL**). No REPORT.md. No `__pycache__` left. Nothing outside the pilot dir touched; no git writes; no Modal; every `python3` through `tools/ramguard local -- python3 …` from repo root. Quarantine honoured (CAMPAIGN_LEDGER not opened; no other round-22 pilot dir read). No subagents dispatched.

## HEADLINE

**The 8.60 is arithmetically correct and structurally meaningful — but it is a `c = 1` constant, and the node attaches it to the binding layer `c*`. At `c*` the deficit is 6.3130. And at `c = 1`, where 8.60 was computed, R-locality's true cost is *exactly 1* — I proved it by exact LP, and the bank already proved it (tail_count THEOREM 12). Two forced corrections flagged. The *conclusion* survives intact: the deficit is structural, with a floor of 6.21 (k=R) / 3.48 (k=2R) at the binding layer — and the banked instrument is already within 1.7% of it.**

## 0. Sources, quoted verbatim

`background/nodes/f2_z1_mass_knife_edge/statement.md:80-84`:
```
80	Both standard supplies killed with computed thresholds (Z-2
81	moments: p &lt;= 8.30 = Corollary 8; interpolation: no p at all,
82	position entropy H(1/L) &gt; 1/L); the common cause: every supplied
83	input is R-LOCAL, short by the factor log2 p / log2(e log2 p) =
84	8.60; the Fourier escape is circular.
```
`notes/pilots_20260806/tail_count/PROOFS.md:437-448`:
```
437	&gt; **THE STRUCTURAL DEFICIT, stated exactly.** All three inputs are
438	&gt; `R`-local: each certifies only statements about `R` coordinates at a
439	&gt; time. A tail bound at level `2^{-cS}` derived from `k`-local information
440	&gt; costs at least `~k` bits of exponent per certificate and `k &lt;= R = S/L`,
441	&gt; so the best exponent any `R`-local argument can reach is `O(R log(...)) =
442	&gt; O(S log2(e L)/L) = 0.116 S` at `L = 64`, against the required `c* S =
443	&gt; 0.443 S`. **The gap is the factor `L / log2(e L) = 8.60`, and `L/log2 L`
444	&gt; is exactly the shape that makes COROLLARY 8's threshold `log2 p =
445	&gt; O(log log p)`.** This is why route (b)'s two supplies and this pilot's
446	&gt; third all land on the same wall: they are not three arguments, they are
447	&gt; three readings of `R`-wise independence, and `R`-wise independence is
448	&gt; `log2 p` times too weak — by exactly the saturation constant.
```
`notes/pilots_20260806/tern_route_b/PROOFS.md:405-411` (COROLLARY 8): "*Theorem 7 reaches `2^{o(S)}` iff the bracket at `k = R` beats `S/R`, i.e. … iff `log2( e log2 p ) &gt;= log2 p`. Solving: **`log2 p &lt;= 3.0529`, i.e. `p &lt;= 8.30`.***"
Row (`tern_route_b/PROOFS.md:58-61`): `p = 18446735827372343297`, `S = 2^38`, `R = 4294967340`, `log2 p = 63.999999355`, `R/S = 1/log2 p`.

## 1. (D1) THE DEFICIT MADE EXACT

**THEOREM RL-1.** `8.599036 = L/log2(eL) = 1/I_INSTR(1) = DEF_INSTR(1)`, and it is *exactly* the multiplicative failure margin of COROLLARY 8's inequality: `log2(eL) = 7.442695` against `L = 63.999999`, ratio `8.599036`. (`log2(eL) = log2 L + log2 e = 6 + 1.442695`.)

`I_INSTR(c)` = the exponent per `S` certified by the one executable instrument (LEMMA 5 AM-GM → `V_1` → Z-2 moment `N_k ≤ (2k-1)!!|H|^k` → Chebyshev, `k ≤ R`), i.e. tail_count THEOREM 11's bracket.

**THE THREE NUMBERS the node carries as one:**

| quantity | value | what it is |
|---|---|---|
| `DEF_INSTR(1) = 1/I_INSTR(1)` | **8.5990** | deficit at `c = 1` — the node's 8.60 |
| `c*/I_INSTR(1)` | **3.8068** | the ratio the node's own sentence computes (`0.443/0.116`) |
| `DEF_INSTR(c*)` | **6.3130** | the deficit **at the binding layer** |

`I_INSTR(1) = 0.116292` (the node's "0.116 S"); `I_INSTR(c*) = 0.070124`, not 0.116, because `η_{c*} = 2^{c*} − 1 = 0.359141 &lt; 1`. Line `:448` supplies a *fourth* number, `log2 p = 64`, also unequal to 8.60.

&gt; ### CATCH-RL1 — LAYER ERROR (forced correction, FLAGGED, node NOT edited)
&gt; Three things ride on it:
&gt; 1. **The layer is wrong**: the binding-layer constant is **6.3130**, not 8.5990.
&gt; 2. **The quoted sentence is internally inconsistent**: it states `0.116 S` achieved vs `0.443 S` required, then names the gap `8.60`; `0.443/0.116 = 3.81`. The `0.116` is `I_INSTR(1)`; the `0.443` is the requirement at `c*` — two layers, divided.
&gt; 3. **At `c = 1` there is no deficit at all** (§3 below, and tail_count THEOREM 12 already proves that layer by a purely `R`-local interpolation argument).

**THEOREM RL-2 — the four-factor decomposition.** `DEF_INSTR(c) = THETA·AMGM·GAUSS·CAP`, with `THETA = c/I_FLAT(c)` (layer), `AMGM = I_FLAT/J_FLAT(η_c)` (LEMMA 5 linearization), `GAUSS = J_FLAT/(log2(e)η²)` (the `(2k-1)!!` moment shape), `CAP = log2(e)η²L/log2(eη²L)` (the cap `k ≤ R`). The identity telescopes; the content is that each factor is the loss of one separately identifiable inequality.

```
 c = 1  :  0.015625 x  1.000000 x 44.361419 x 12.405786 = 8.599036
 c = c* :  1.000000 x  2.299041 x  1.034793 x  2.653612 = 6.313028
```

- `THETA(c*) = 1.000000` exactly — COROLLARY ZM's zero margin, re-measured from a fresh code path (`I_FLAT(c*) = 0.4426950409 = c*`).
- `AMGM(1) = 1.000000` exactly: at `c = 1` the true event `{cost = 0}` and the relaxed event `{V_1 = |H|}` are the *same* event (`all c_s = 0`). AM-GM's loss is a bulk phenomenon (2.299 at `c*`, 13.07 at `c = 0.15`).
- **At `c = 1` the dominant loss is `GAUSS = 44.36`, not locality.** So `8.60` is mostly a statement about *Chebyshev at an endpoint*, scaled by the criterion's own `1/64` slack there.
- **At `c*` the lossiest single step is the LOCALITY CAP, 2.654** (AMGM 2.299 second, GAUSS 1.035 nearly free).

`min_c DEF_INSTR(c) = 5.9692` at `c = 0.298`; the instrument is *worst* where the criterion is *slackest*.

## 2. (D2) THE SHARPENING ATTEMPTS — none beats the banked instrument

Licensing controls first: my own from-scratch row construction reproduces the banked `Z_1 = 1.250000` (G1) and `9.387207` (G4) of `tern_route_b/PROOFS.md:124-127`, and character form vs cost form agree to `2.7e-13`.

| attempt | exponent at `c*` | deficit | verdict |
|---|---|---|---|
| **banked instrument** (AM-GM + Z-2 + Chebyshev, `k ≤ R`) | 0.070124 | **6.313** | best |
| **A2** truncated centred moment on the cost sum, `k = R` | 0.049218 | 8.995 | FAILS |
| **A1** type / binomial-moment (Sanov) bound, `k = R` | 0.006917 | 64.000 | FAILS |
| **A3** repaired THEOREM 10 | 0.001710 | 258.883 | FAILS |

- **A1** is exactly `kmul·I_FLAT(c)/L`; since `I_FLAT(c*) = c*`, the deficit is *exactly* `L/kmul` = 64.000 / 32.000. It throws away the lower-order marginals.
- **A2** at `k = 2R` would give deficit 5.353 — but that is **not licensed**: expanding `d` in additive characters, a `k`-th moment consumes `l1` weight `k·J`; `k·J ≤ 2R` with `k = 2R` forces `J = 1`, i.e. keep only the `j = 1` harmonic, which *is* `V_1`, which *is* LEMMA 5's route. **At the licensed radius the "new" instrument collapses onto the banked one.**
- **A4** (`k &gt; R`): `N_k` computed exactly via `N_k = p^{-R}Σ_u V_1(u)^{2k}`. First failure at exactly `k = R+1` on all three rows — G1 `N_3 = 80800 &gt; 61440`, G4 `N_3 = 527360 &gt; 491520`, G2 `N_2 = 1104 &gt; 768` (the banked value, reproduced independently). **The cap is sharp.**
- **A5**: the deficit is a function of `R/S` alone (2.379 at `R/S = 1/4` → 10.325 at `1/128`), but saturation pins `R/S = 1/log2 p` — Z-NOGO acting one level up.

&gt; ### CATCH-RL2 — POSITION ENTROPY IS AN ARTEFACT (forced correction, FLAGGED, node NOT edited)
&gt; `statement.md:81-82` and tail_count THEOREM 10 record the interpolation supply as dying **at every `p`**, diagnosed as "position entropy `H(1/L) &gt; 1/L`". That union bound (`|U_c| ≤ C(S,R)m^R`) is not the right `R`-local instrument. `R`-wise uniformity gives *exactly* `E[C(N_A,R)] = C(S,R)ρ^R`, hence `Pr[N_A ≥ m] ≤ C(S,R)ρ^R/C(m,R)` — **the `C(S,R)` cancels against `C(m,R)`** and the residue is `O(δ/L)`, not `H(1/L)`.
&gt; Measured at `c*`: banked exponent **−0.094651** (dead) → repaired **+0.001710** (alive), with a threshold at every `log2 p ≥ 3.06`. **The "dies at EVERY `p` / no threshold in `p`" verdict and the `H(1/L) &gt; 1/L` diagnosis should be withdrawn — but the route is still dead numerically (deficit 258.9). The correction changes the diagnosis (the wall is locality, not position entropy), not the ledger.**

## 3. (D3) THE FORMALIZED CLASS AND ITS FLOOR

**DEFINITION.** A bound on `Pr_u[cost(u) ≤ (1−c)S]` is **`k`-LOCAL** iff it holds for *every* random vector on `F_p^S` whose every `k`-subset marginal is uniform on `F_p^k`. It quantifies over the **locality radius `k`**, the **moment order** (derived, `≤ k`), and the **window length** (which enters only through *which* `k`-wise marginals are uniform). `OPT_k(c)` = max tail probability over the class; `I_LOC_k = −(1/S)log2 OPT_k`; `FLOOR_k(c) = c/I_LOC_k(c)` — **no `k`-LOCAL argument has deficit below this**.

The object's supply is **bracketed by `k = R` and `k = 2R`**: the MDS value code is exactly `R`-wise independent (dual distance `R+1`); THEOREM Z-2 adds `l1`-restricted moment matching to order `2R`, strictly weaker than `2R`-wise uniformity.

Two proved reductions make it computable: **LEMMA RL-4** (symmetrisation: exchangeable + sign-symmetric ⇒ a law on the folded count vector ⇒ an exact LP) and **LEMMA RL-5** (LIFTING: any `k`-wise-independent Bernoulli(`ρ`) pattern lifts to a `k`-wise-uniform law on `F_p^S` with the same `Pr[all coordinates in A]`, so `OPT_k(c) ≥ OPTPAT_k(ρ(1−c),S)`, a two-bin LP). Solved with a from-scratch two-phase simplex (scipy.optimize does not import inside the ramguard wall limit); smoke-tested against a textbook optimum and the closed form `OPTPAT_1 = ρ`.

**(a) EXACT full LP at G1 (`p = 17, S = 8, R = 2`; 12870 states, 46 rows):**
```
   c        OPT_{k=R}   TRUE(GRS)   FLOOR_R   DEF_INSTR(L=4.09)
   0.2000  3.2180e-01  3.4602e-03    0.9781      6.2696
   0.3000  2.7303e-01  3.4602e-03    1.2815      3.8921
   0.4427  2.1332e-01  3.4602e-03    1.5889      2.3790   &lt;- c*
   0.6000  1.5354e-01  3.4602e-03    1.7756      1.5689
   0.8000  8.4921e-02  3.4602e-03    1.7989      1.2532
   1.0000  3.4602e-03  3.4602e-03    0.9786      1.1766   &lt;- = 17^{-2} EXACTLY
```
&gt; **P9, THE SHARPEST FINDING.** `OPT_R(1) = 17^{-2} = p^{-R}` **exactly**, so `FLOOR_R(1) = 0.9786 ≤ 1`: **R-locality costs nothing at `c = 1`** — the very layer where 8.60 lives, and the layer tail_count THEOREM 12 already proves. Radius sweep: `OPT_k(1) = p^{-k}` exactly for every `k` (measured `17^{-2}`, `17^{-3}`; one-line matching upper bound via `E[C(N_0,k)]`). So `I_LOC_k(1) = kL/S`, which at `k = R` is `1 + Δ/S` — **the `c = 1` requirement is met on the nose by pure R-locality, with the knife-edge constant `Δ` as the entire margin.**

Exact toy floors at `c*`: `FLOOR_2 = 1.5889`, `FLOOR_3 = 1.3062` (monotone in the radius, as it must be); `k = 2R = 4` (496 rows) **NOT COMPUTED** — exceeded the wall limit, never estimated. Second exact row `p = 41`: `FLOOR_R(c*) = 2.7651`. Sanity control passes: `OPT_R(c) ≥` the true GRS tail at every layer.

**(b) Official-row lifted floor (ASYMPTOTIC EVIDENCE, not a theorem).** `ρ(1−c*) = 0.383070`. The exact pattern LP at moderate `S` converges to the closed form from below in the exponent — at fixed `k = 4` the excess falls `+17.2%, +14.9%, +12.9%, +11.5%` as `S = 32…256`; at fixed ratio `k/S = 1/8` the exact exponent rises `0.326807 → 0.346514` toward `0.383137`. So the closed form is the `S→∞` limit, which is what applies at `S = 2^38`:
```
   FLOOR_R  (lifted, k = R)   =  6.2063
   DEF_INSTR(c*)              =  6.3130     (+1.7%)
   FLOOR_2R (lifted, k = 2R)  =  3.4848     (headroom factor 1.81)
```

**VERDICT.** `8.60` is not the binding-layer deficit and is not a floor for the class. But **the deficit is structural**: the floor is `≥ 3.48` at `c*`, and `3.48 &gt; 1`. The banked instrument is **essentially optimal for what R-wise independence alone allows (+1.7%)**, with at most a **1.81×** gain available — and only if Z-2's `2R`-order information could be turned into a genuine `2R`-wise tail bound, which A2 shows collapses back to `V_1`. **What is wrong in the bank is the number and its layer, not the conclusion.**

## 4. (D4) THE WEAKEST NON-LOCAL INPUT

**Required statement**: for one interval `A ⊂ F_p` with `ρ = ρ(1−c*) = 0.3831` and some `δ &gt; 0`,
```
#{ u : #{ s : f_u(ζ^s) ∈ A } ≥ (1−δ)S }  ≤  p^R · 2^{−c* S + o(S)} .
```
i.e. **"no codeword of the GRS value code `C*` is unusually smooth"** — tail_count THEOREM 9's structure theorem read as an obligation. It is non-local because (i) it quantifies over `Θ(S)` coordinates at once, so no `k = O(R)` certificate supplies it; (ii) it is about *individual* `u`, which is exactly the shape Weil would have given (`tern_route_b/PROOFS.md:301-317`, vacuous by 26.000 bits); (iii) it is `2^{o(S)}`-tight, so nothing that loses a constant per coordinate survives.

**Nothing in the bank supplies it.** The two nearest candidates, named honestly: the **constant-weight Z-FLOOR cell (crossing side)** — already the standing lead at `statement.md:87-88`, and the only banked object quantifying over all `S` coordinates at once; and an **ensemble average over the five generating classes** (`f2_o1_status_split` Addendum 3), which would need a concentration statement a five-element family cannot give.

**And a sharpening that makes the gap worse.** `f2_repose` R2(v) records the finite target `Z(L) ≤ 1 + N^3`, i.e. `Z_1 ∈ [2^{17.98}, 2^{22.75}]` — a 4.77-bit window. Under that reading the criterion's `o(S)` is not `o(S)` but `≤ 22.75` bits absolute against `S = 2.75e11`. **Every constant here is a multiplicative deficit on a `Θ(S)` exponent; a 4.77-bit window leaves room for none of them. The non-local input must be essentially exact, not merely `2^{o(S)}`.**

## 5. Registered predictions vs outcomes

**HIT (14):** P1 (8.5990), P2 (8.60 = `DEF_INSTR(1)` = COROLLARY 8's margin), P3 (6.3130 vs 6.32±0.03), P4 (`I_INSTR(c*)=0.070124` vs 0.0701±0.0005), P5 (`(1/64, 1.000, 44.36, 12.41)`), P6 (`(1.000, 2.299, 1.035, 2.654)`), P7 (CAP is lossiest at `c*`), P8 (5.969 @ 0.298 vs 5.97±0.10 @ 0.30), A1 (0.00692/0.01383; FAILS), A2 (deficit 8.995 vs 8.6±0.7; FAILS), A3 (cancellation + 0.00171 vs 0.0017±0.0005), A4, A5, A6, P9, P10 (6.206/3.485 vs 6.2±0.4 / 3.5±0.3), P11 (+1.7% &lt; 5%), P12 first clause (LP solvable; `c=1` gives `p^{-R}` to 1e-9).
**NOT TESTED:** P12 second clause (full LP exceeds the lifted pattern value) — the LIFTING LEMMA's hypothesis (`|A|` a prime power `≥ S`) fails at `p = 17`, so the comparison is not licensed at toy scale.
**UNRESOLVED (reported, not absorbed):** **P13** — the `L`-dependence of `FLOOR_k`. The exact full LP has `C(S+(p−1)/2,(p−1)/2)` states and is infeasible past `p ≈ 41`; two rows (`L = 4.09, 5.36`, both `R/S = 0.25`, `S ≤ 8`) cannot fit a law.
**MISSES:** none of the numeric bands was missed.

## 6. Self-corrections (all stated plainly)

1. **`CAP` was registered for the `k = R` branch only.** When `η² ≤ 1/L` (i.e. `c ≤ 0.16993` at `L = 64`) the free optimum `k = η²S` already satisfies `k ≤ R` and the cap factor is exactly 1. Caught by the product failing at `c = 0.15` (9.035 vs 8.660). Both registered layers (`c*`, `c = 1`) are in the `k = R` branch, so no registered prediction was affected. Recorded in `rl_lib.py`.
2. **A missing factor `L` in the A2 moment-bound argument** (`θ ln2 · t · e/k` with `k = kmul·S/L` carries an `L`; the code omitted it). Caught because the exponent came out negative. Before the fix A2 read "vacuous"; after, 0.049218.
3. **Sign error in my simplex return** (`−T[m,−1]` instead of `T[m,−1]`). Caught by the textbook smoke test returning −36.
4. **Pattern-LP rows with `OPT &lt; 1e-7` discarded** as below my float simplex's reliable range — they visibly broke monotonicity (`(192,12)` and `(256,16)` gave exponents *below* smaller-`S` rows), which is how they were caught. The convergence claim rests only on reliable rows.
5. **Direction of PROPOSITION RL-6 corrected in PROOFS.** The Hermite polynomial is *dual*-feasible, so it bounds `OPTPAT` from above and approximates the lifted floor from above at finite `S`; only the exact pattern-LP value is a valid lower bound on the class floor. Official-row numbers are labelled ASYMPTOTIC EVIDENCE; the only EXACT floor here is the G1 full LP.
6. **`k = 2R` full LP at G1 NOT COMPUTED** (496×12870 exceeds the 5-minute wall with my solver). Reported as not computed, never estimated.
7. **A2's truncation was initially described as "necessary"**; after correction 2 it is merely helpful (+12.9% on the exponent).

## 7. Honest labels and what is NOT claimed

Criterion / route / factor stay distinct throughout: **nothing here bears on whether the tail-count criterion is true** — only on what `k`-local instruments can certify. No status flip, no closure claim. The G1 floors are EXACT but toy-scale (EVIDENCE); the official-row floors are ASYMPTOTIC (evidence, not theorems uniform in the row); the calibration clause (`statement.md:92-98`) is honoured — no toy is evidence about `Z_1` at the official row, and toys here verify identities and LP optima only. Grid rules held: `S = 2^{e_p−1}` so `2N` is a 2-power (CATCH-Z6, asserted in code); `Λ = {1,3,…,2R−1}` so exponent 0 never occurs (CATCH-19B, asserted in code); every measured functional is named in PREREG §A (CATCH-19C). **Two forced corrections (CATCH-RL1, CATCH-RL2) are flagged for the coordinator; I did not edit the node.**
