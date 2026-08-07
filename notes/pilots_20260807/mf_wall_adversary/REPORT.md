# REPORT — mf_wall_adversary (persisted verbatim by the coordinator from the session transcript, task a3bd03c1db3a0035a, 2026-08-07)

All experiments are in. Final artifacts are in place; two long-tail runs were killed by the 5-minute wall (reported as gaps below).

---

# REPORT — round 23b, `mf_wall_adversary`: the (MF) one-wall classification, attacked

Registrations were appended to `notes/pilots_20260807/mf_wall_adversary/PREREG.md:110-394` **before** the first compute run. Everything below is measured against them.

## 0. THE POWER CONTROL, FIRST (S4)

### S4-P0 — the two mandated coarse controls: round-23 test PASSES

The round-23 test is the shape-pun: does statement **(MF)** — `fpc5_diag/REPORT.md:62`, *"Count monic degree-`d` locators split on `C` inside a linear flat of projective dimension `e = 2d+1-t·ell` whose codimension is exactly `sigma`"* — specialize?

- **Mystery 6, clause (b)** has no linear flat at all. Its object is a combinatorial box: `l1_mixed_petal_amplification/statement_addenda/06-round21-growing-petal-repose.md:9-11` — ``#core kept a &lt;= Lambda := 2*ell + b - 2 … BOX = Theta(C(k-1,Lambda) * C(t*ell,Lambda)) = Theta(n^{2*Lambda})``. Clause (a) is *"proved by unconditional counting"* (`:32`); clause (b) is *"the open target … it is not a counting fact"* (`:34-36`).
- **WCL slot (1,6)** is a zero-event Diophantine obligation: `dli_wcl_slot_1_6_emptiness/statement.md:7-9` — *"no reduced signed weight-6 polynomial vanishes at an order-512 root … Zero-event obligation."* No flat, no first moment.

(MF) cannot instantiate on either. **The round-23 test separates both mandated controls.** But that bar is low, and both controls sit outside (MF)'s instantiation range — so passing them proves only that the test is not literally vacuous.

### S4-P1 — the HARD control (my addition): the round-23 test **FAILS**

I registered a control *inside* (MF)'s range: red 1 vs its **PROVED** sibling `l1_fpc5_ratequarter_m4_t2_payment`, which is closed with an absolute bound in eight lines (`proof.md`: `2ell&gt;k-1` ⇒ two codewords agreeing on a touched pair coincide ⇒ `6+4=10`). Exact integer scan at `k = 2^40` (`s4_power.py`):

| (MF) clause | red 1 (rate half, **OPEN**) | rate quarter (**PROVED, bound 10**) |
|---|---|---|
| `codim = sigma` identically | TRUE, all rows | TRUE, all rows |
| `sigma &gt; 0` | not always (see self-correction 4) | **TRUE, always** |
| `e` grows linearly in `n` | max `e = 549,755,813,887 = 0.25 n` | max `e = 879,609,302,219 = 0.20 n` |
| first moment below 1 | sharp cell `2^(-7.948e12)` | **always**, worst row `2^(-9.2359e12)` |
| **`t*ell &gt; N` (over-determination)** | **FALSE, all rows** | **TRUE, all rows** |

My `-7.948e12` at the sharp official cell reproduces round 23's number exactly (replication gate).

**The PROVED sibling satisfies every clause of (MF), with strictly better margins on two of them.** A test that groups an eight-line-proved problem with an open one has no evidential power for the user's mandate. **The round-23 shape-pun test fails the power control.** The only clause that separates them — `t*ell &gt; N` — is (MF)-expressible but is not part of (MF).

### S4-P2 — power control on the cap-4 *instrument*: the instrument HAS power, and W1 is FALSIFIED

Registered W1: is the cap a function of the (MF) parameters alone? Identical `(q, d, N, pool, dim)`, split-only in both arms, `ell=4, q=97`, 25 configs each:

| arm | NSPLIT mean | **MAXPACK max** | max pair overlap | clique max |
|---|---|---|---|---|
| guarded congruence kernel | 21.96 | **4** (23×4, 2×3) | **1** = `ell-3` | 6 |
| uniformly random flat | 24.12 | **5** (20×4, 5×5) | **2** | 11 |

**W1 FALSIFIED** as registered (max differs by 1). The cap is *structure-specific*, not (MF)-parametric. Per my own pre-registration (`PREREG.md:151-154`): *"the handle then supports neither unification nor separation and must be withdrawn as evidence."*

### Redesign (mandatory, since the round-23 test failed S4-P1)

I replaced the OBJECT-only test with the round-19 three-gate test (`PREREG.md:130-146`), where **METHOD** = *the missing theorem is the same*. Applied to the controls: the PROVED sibling's METHOD failure is **empty** (over-determination never invokes a packing bound) → separated; mystery 6 and WCL have no flat → separated. **The repaired test passes all three power controls**, so conclusions below may be drawn from it.

---

## 1. Separation attempts vs their registered escapes

### S1 (cap-4 mechanism) — premise CONFIRMED, separation **DISSOLVED**

The exact packing ledger (`ledger.py`): an `m`-packing is forbidden by the pairwise overlap cap iff `C(m,2)*lam &lt; m*j - N`.

| red | cell | `j` | `N` | proved cap | ledger permits | **MEASURED** |
|---|---|---|---|---|---|---|
| 1 | `ell=4,5,6,8,12,20` | `2ell-3` | `5ell-5` | `2(ell-3)` and sharpened `ell-3` | **never forbids** | **4** |
| 2 | LS6 (3,1,1) | 5 | 11 | `h=1` | 2 | **2** |
| 2 | LS6 (3,2,1) | 5 | 12 | `h=1` | 3 | **3** |
| 2 | LS6 (4,1,1) | 7 | 15 | `h=2` | 3 | **3** |
| 2 | LS6 (4,2,1) | 7 | **16** | `h=2` | **never forbids** | **3** |
| 2 | LS6 (4,3,1) | 7 | **17** | `h=2` | **never forbids** | **3** |

Red 1's cap is indeed *not* packing arithmetic — as registered. **But so is red 2's.** Round 23's claim (`REPORT.md:162`) that *"The measured cap is the proved cap — the pair-determinant instrument is tight here"* is a coincidence of the single cell `(4,1,1)`: move `b` by one, the bound goes vacuous, and the cap does not move. The asymmetry I registered as my separation candidate **does not exist**. ESCAPE-S1′ (a `t=2`-specific proof mechanism) was **not** established: my derived `ell=4` projective-plane rigidity (a 5-packing needs all `C(5,2)=10` pairs to share exactly one root, all distinct ⇒ 5 chart points in general position with all 10 connecting lines carrying a root) explains `ell=4` exactly, but **fails at `ell=5,6`**, where the ledger has growing slack and the cap holds anyway.

### The **ell = 4,5,6 exact decision** (S1's adjudicator, delivered at scope)

Round 23 brute-forced `q^(ell-2)` chart points and therefore **sampled** at `ell=5` (3e5 of 2,048,383) and timed out at `ell&gt;=6`. I ported the `ls6_bucket.py` last-coordinate bucketing to the m4_t2 chart, making the full chart exactly enumerable. All runs: full exact-contributor filters (primitivity + untouched-petal nonagreement), all flats gcd-trivial (so `l1_fpc5_ratehalf_m4_t2_sharp_gcd_triviality` (GT2) holds), **BB exhaustive**:

| cell | configs | NSPLIT mean/max | **MAXPACK** | max pair overlap | round-23 ESCAPE-RH(a) `4(ell-2)` |
|---|---|---|---|---|---|
| `ell=4, q=97` | **300** | 21.64 / 34 | **4** (296×4, 4×3) | **1** = `ell-3` | 8 — not fired |
| `ell=4, q=193` | 1 | 167 / 167 | **4** | 1 | 8 — not fired |
| `ell=5, q=127` | **25** | 70.68 / 79 | **4 in all 25** | **2** = `ell-3` | 12 — not fired |
| `ell=6, q=127` | 3 (seeds 11/22/33) | 49 / 40 / 41 | **4, 4, 4** | **3** = `ell-3` | 16 — not fired |

**My registered prediction P-W2 (that the cap would exceed 4 at `ell=5`) is FALSIFIED.** W2 is **CONFIRMED** on a far stronger test than round 23 could run. ESCAPE-RH(b) (doubling `4→5→6`) does not fire. The sharpened cap `|D∩D'| &lt;= ell-3` is achieved exactly at every `ell` — an independent confirmation of round 23's derived sharpening on new witnesses.

**New mechanism datum — BUDGET ELASTICITY** (MAXPACK as the core budget runs `N … N+5`):

| cell | curve |
|---|---|
| `ell=4, q=97` | `[4, 5, 5, 6, 6, ·]` |
| `ell=4, q=193` | `[4, 4, 5, 5, 6, 6]` |
| `ell=5, q=127` | `[4, 5, 5, 5, 6, 6]` |
| `ell=6, q=127` | `[4,4,4,4,5,5]` / `[4,4,4,5,5,5]` / `[4,4,4,5,5,5]` |

The cap is **soft**: one to four extra core points break it. It stiffens with `ell` (`+1 → +1 → +3/+4`) — the opposite of my prediction, and evidence that the cap is a real structural property rather than a knife-edge, but *not* one derivable from (MF).

### S2 (instrument cross-response) — ESCAPE **DID NOT FIRE**

`CAPDEF = (ledger permission) - (measured cap)`. At matched "ledger vacuous" parameters: red 1 (every `ell`) `CAPDEF = ∞` with cap 4; red 2 at `(4,2,1)`/`(4,3,1)` `CAPDEF = ∞` with cap 3. Both caps are invariant under exactly the parameter that moves the ledger. The cap phenomenon **transfers** under the (MF) dictionary. **No separation.**

### W3 (red 2's owner concentration) — **FALSIFIED** as an (MF)-parametric fact

Replication first: `(4,1,1), q=101`, full 1,030,301-point chart, 25 trials — atom mean **38.48** (round 23: 39.16), MAXPACK **3**, owner histogram `g=0: 53.6% / g=1: 37.1% / g=2: 9.3%` (round 23: 52.4/35.1/12.5). Stable across `b`: `g=0` = 52.8% / 52.0% / 52.6% at `b=1,2,3`.

Reference: for two independent uniform `j`-subsets of `[N]` with `N=15, j=7`, `P(g=0) = 0.0012`; conditioned on the proved cap `g &lt;= h = 2`, `P(g=0) = 0.0058`. **Measured 53.6% is ~92x the conditioned reference and ~440x the unconditioned one.** The trivial-owner concentration is structural, not (MF)-predicted.

### S3 (upstream + fourth faces) — the upstream face has **zero** discriminating power; the fourth face is the strongest match

**Face A — `prob:capfr1-master-flatness`.** No formal statement exists inside the prize repo (37 mentions, all bare labels/pointers; `upstream_dag/dag.json` has no node for it). The statement is in the sibling checkout `rs-mca/tex/cs25_cap_v13_2.tex:9253-9259`:

&gt; *"Find an explicit polynomial `P` such that, for every affine subspace `A` of the monic degree-`j` polynomial space over `B` of codimension `s`, after quotient and common-divisor components have been removed, `|A ∩ Dloc_j(D)| &lt;= P(n)(binom(n,j)|B|^{-s} + 1)`."*

Round-19 gates: **quantifiers** — upstream is `∀` affine subspace, `∀` codimension, with **no growth clause**; (MF) fixes a dimension/codimension relation, so (MF) is an **instance**, not the same statement (round 23's *"this is not a family resemblance, it is one statement"*, `REPORT.md:64`, over-reaches). **Coefficient class** — upstream normalizes by `|B|^{-s}` (base field); FPC5 computes `q^{-sigma}` (ambient); the repo's own transcription at `f2_selector_face_primitive_reduction/statement.md:35` writes `q^s`. **Unresolved mismatch.** **Count** — upstream counts `|A ∩ Dloc_j(D)|`; FPC5 counts a filtered subset plus an aggregation upstream does not supply.

Discriminating power, demonstrated not asserted: the **PROVED** rate-quarter sibling is an instance (S4-P1), and the **PROVED** `l1_rootfree_rational_q_projective_packing` is an instance. **A test that PROVED nodes pass cannot certify a wall.** My registered P-UP holds.

**Face B — the L1 root-free rational-Q cell** (`l1_rootfree_rational_q_projective_packing`, status **PROVED**). OBJECT: `V = span(G, W_1 F[X]_&lt;d)`, `dim P(V) = d = k-r`, codim `w`, counting `P(V) ∩ Dloc_j(H')` — a **congruence flat**, same object class. **Partial mismatch that matters:** its modulus `W_1` is *root-free on the domain* (`gcd(Wbar_1, Omega')=1`), whereas FPC5's modulus `L_0L_1L_2` has **all** its roots in the evaluation domain — which is exactly what creates FPC5's guard. REGIME: **match** — paid for fixed `d` and `d=o(n)` by `(PC4)`, open exactly at `d=Theta(n)` (`statement.md:58-59`: *"It can be exponential when `d=Theta(n)`"*), which is FPC5's regime. METHOD: **match** — the proved instrument is the identical anticode bound, `floor(binom(n',d)/binom(j,d))` (`:41`) versus FPC5's `floor(binom(k-1+b,2s+1)/binom(ell+2s,2s+1))` (JD3), failing the same way. **This is the strongest same-wall evidence in the repo, and round 23 did not run it.**

**Face C (found, not registered)** — `f_global_packing_step/statement.md:12,23-25` carries the *same formula* `#leaf &lt;= binom(n_leaf,r_leaf)/binom(j_leaf,r_leaf)` and names the *same* failure: *"The theorem must absorb the `n^r`-type numerators; a polynomial number of states does not suffice when each state has a dimension-dependent exponent."*

---

## 2. D1 — the claim made falsifiable

- **D1(a) — FALSIFIED.** Of the three round-23 handles: W1 falsified (cap not (MF)-parametric — a random flat with identical parameters reaches 5); W3 falsified (owner mass 92x the parametric reference); W2 confirmed. **The two quantitative handles that carry round 23's case are not expressible in (MF) terms and must be withdrawn as classification evidence.** They remain valid node-level findings.
- **D1(b) — FALSIFIED at the gate level, CONFIRMED at the METHOD level.** Each of the three round-23 named gates moves exactly one red: the `t`-petal overlap-cap lemma moves only red 3 (proved already at `t=2,3`); the `G=1` base-cover moves only red 2 (red 1 has no owner stratification — flat-wide gcd 1 is proved); the `ell=4` decision is local to red 1. Round 23's own cross-lane matrices already said this: `REPORT.md:129` (LS6 chart **FAILS** on red 1 — *"the m4_t2 guarded flat is a background-congruence kernel with no such multiplier"*), `:131` (prefix/shell machinery **FAILS** on red 1, applies to red 2), `:231` (all `M=4` constructions **FAIL** on red 3). Only a METHOD-level theorem moves ≥2.
- **D1(c)-STRONG — FALSIFIED, 1 of 3.** Feeding upstream master-flatness in as a black box:
  - **Red 2: DISCHARGED.** `statement.md:26` — *"There are fewer than `4n` such `(triple,a)` cells"* — and `:37` gives `binom(n,j)/Q^(j-r)&lt;2^(-3ell-4)`, so per-atom `≈ P(n)` and the sum over `&lt;4n` atoms is polynomial (modulo checking `P`'s degree against the 719-column exponent-6 allowance).
  - **Red 1: NOT discharged.** Upstream's per-flat `+1` term, summed over the background cells, is exactly what the node forbids in its own words — `l1_fpc5_ratehalf_m4_t2_payment/statement.md:34-35`: *"The exact set `R=Z_B(W_F)` is unique, but an independent sum over all `binom(b,r)` possible sets is not a polynomial payment."* With `b = ell-3 = Theta(n)`, that is `2^b · P(n)`.
  - **Red 3: NOT discharged** — the allocation across first-owned sources/owners survives, and 65% of it cannot even be posed (below).

## 3. Red 3 is only 35% certifiable

(MF) can only be instantiated where contributors are *proved* to inject into a linear flat: `t=2` (two-full-petal slice) and `t=3` (`pma_three_petal_mu_basis_reduction`). For `t&gt;=4` no such reduction exists — round 23's own matrix, `REPORT.md:229`: *"APPLIES ONLY at `t=3` | the `t&gt;=4` generalization does not exist"*. Re-running round 23's own Johnson sieve (`fpc5_exact.py` verbatim) and splitting the 408 residual rows (`red3_split.py`):

**142 / 408 rows (34.8%) instantiable; 266 / 408 (65.2%) NOT** — by rate: 1/2 → 72 vs 246; 1/4 → 56 vs 20; 1/8 → 14 vs 0. `t` reaches 16. On 65% of red 3's exposure the one-wall question is **not well-posed**.

---

## 4. VERDICT (graded; no promotion language — surfaced, not decided)

- **Reds 1 and 2: SAME WALL.** All three registered separation attempts (S1, S2, S3) failed, against a test that passed all three power controls. The wall, stated at METHOD level: *the anticode/packing bound gives an exponent that grows with the flat dimension; what is missing is a dimension-uniform max-to-mean bound for split locators in a growing-dimensional flat.* Both nodes say this in their own words — red 1 `statement.md:82-83` (*"Because the projective dimension grows with `ell`, the upstream fixed-dimensional split-flat bound does not close"*), red 2 `statement.md:42-43` (*"the live primitive issue is a sub-balance maximum-versus-average split-flat bound"*). What I could **not** reach: any `t=2`-specific mechanism for red 1's cap (my plane-rigidity argument dies at `ell&gt;=5`), and the strict `ell=4` finite decision as a *proof*.
- **Red 3: UNDECIDED.** Same wall on 142/408 rows; on 266/408 the object is not known to be a flat at all. **Named missing experiment:** the `t`-petal injection / overlap-cap lemma — *for distinct primitive members of the `t`-petal slice, `|Z(F) ∩ Z(F')| &lt;= e-1`* — the cofactor/syzygy determinant argument that already works verbatim at `t=2` and `t=3`. **Price:** one lemma, no compute; the sieve that consumes it is already written.
- **The round-23 evidence base is repriced, not overturned.** The statement-level shape-pun **fails** its power control (S4-P1) and does not meet the mandate. Both quantitative handles are non-(MF)-derivable and are withdrawn as classification evidence. What survives and is *strengthened*: the cap-4 is now exact (not sampled) at `ell = 4, 5, 6` over 329 configurations and three primes, with exhaustive branch-and-bound; the `codim = sigma` identity; the sharpened overlap cap `ell-3`, achieved tightly at every `ell`. What is *new* and is the strongest actual same-wall evidence: the METHOD match with `l1_rootfree_rational_q_projective_packing` (open exactly at `d=Theta(n)`, identical anticode formula) and `f_global_packing_step` (identical formula, identically named failure).

## 5. Self-corrections, stated plainly

1. **My registered prediction P-W2/H4 was wrong.** I derived that the `ell=4` cap came from projective-plane rigidity (unique connecting line) and predicted the cap would exceed 4 at `ell&gt;=5`. Exact enumeration at `ell=5` (25 configs) and `ell=6` (3 configs) gives 4 every time. My mechanism explains `ell=4` (confirmed by the `+1` budget elasticity) and **not** `ell&gt;=5`. The mechanism at `ell&gt;=5` remains unidentified.
2. **A result I reported to myself mid-run and then withdrew.** My first `ell=5` run gave MAXPACK **16** with max pair overlap **6**, which violates the proved cap `2s=4`. Cause: that arm was split-only (no primitivity / untouched-petal filters), so it admitted non-contributors; the branch-and-bound was also truncated (`all_bb_exhaustive: false`), so 16 was a lower bound on the wrong object. **Withdrawn — not a witness.** With the correct filters the identical cell gives 4 in all 25 configs, exhaustively.
3. **My registered S1 separation candidate dissolved** once I varied `b`: red 2's "Bonferroni-tight" cap is a single-cell coincidence.
4. **A scan artifact in my own output.** `s4_power.py` shows one red-1 row with `sigma = 0` and log2 first moment `+1.0676e12`. That is the formal codimension-zero endpoint, which `CONJECTURE_F_FALSE_GREEN_AUDIT_20260807.md:131` declares empty (*"Official source arithmetic makes the formal codimension-zero endpoint empty"*). So `first_moment_below_1_ALWAYS: false` for red 1 is my scan's artifact, not a finding, and does not weaken red 1's max-to-mean status.
5. **The strict `ell=4` finite decision is NOT delivered**, exactly as scoped in advance (`PREREG.md:352-364`): the configuration space after both available normalizations is ~5.6e10 at `q=37`. I delivered 300 exact configurations at `q=97` (vs round 23's 25) plus `q=193`, and the structure theorem — a 5-packing at `ell=4` exists iff the connection graph has a general-position `K_5`. Measured: `K_5` and `K_6` **do** occur (6 and 2 of 25 configs) but always with a collinear triple. **This is a search, not a proof. UNDECIDED.**
6. **Two runs did not complete** under the 5-minute wall and are honest gaps: the random-flat control at `ell=5` (so W1 rests on `ell=4` alone) and the `ell=4, q=389` config (so `ell=4` q-invariance rests on `q=97, 193` plus round 23's own `q=389` timeout).
7. **Scope note on sources:** one subagent read the upstream sibling checkout `/home/u2470931/smooth-read-solomin/rs-mca/` (read-only) because the formal upstream statement does not exist inside the prize repo. That path is outside the working directory but is not under quarantine; flagging rather than hiding.

## 6. Compliance and artifacts

Every `python3` invocation went through `tools/ramguard tiny|local -- python3 …` from the repo root, with the literal `--`. No `dag.json`, `nodes/`, or `tools/` edit; no git writes; no Modal; stdlib only. **Quarantine held:** I never opened `notes/pilots_20260802/CAMPAIGN_LEDGER.md` at all, never opened `notes/pilots_20260807/ge_lattice_cert`, and passed the clause verbatim to all three subagents.

All under `notes/pilots_20260807/mf_wall_adversary/`: `PREREG.md` (brief + my registrations, appended before compute); `s4_power.py` (S4-P1); `rh_bucket.py` (exact bucketed chart enumeration, guarded/random arms, gcd + overlap + budget-elasticity instrumentation); `ls6_probe.py` (red 2, + hypergeometric reference); `ledger.py` (exact packing ledger); `red3_split.py` (the 142/266 split); `out_ell4.jsonl`, `out_ell4_rand.jsonl`, `out_ell5.jsonl`, `out_ell5_full.jsonl`.
