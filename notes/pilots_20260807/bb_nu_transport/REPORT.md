# REPORT — bb_nu_transport (persisted verbatim by the coordinator from the session transcript, task a965b8abce47de57b, 2026-08-07)

Sanity check complete: full suite re-runs clean (1550 checks / 0 failures, exit 0), the fail-closed control exits 1, `find -newermt '-3 hours'` outside my directory returns empty, no `dag.json`/`nodes/`/`tools/` edit, no git, no Modal, no status flip. Report follows.

---

# BB → THE ACCIDENT UPPER BOUND / nu(A): METHOD TRANSPORT (round 22, mystery 4)

**Verdict: BB's METHOD does NOT transport — its three quantitative steps are all strictly lower-bound-directed, and one of them (shell concentration) is the source of the difficulty, not a tool against it. But BB's *scaffolding* transports, and it yields the first UPPER bound of record on `Acc_deep`: unconditional, `p`-free, and below `B*` for every `v ≥ 35`. For `nu(A)` the answer is sharper than a type mismatch: it is a SIGN mismatch, and I prove the anti-transport.**

Artifacts (all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/bb_nu_transport/`): `PREREG.md` (§P0–P9 appended before any computation), `PROOFS.md`, `transport.py`, `full_run.out`, `failclosed.out`. **1550 checks, 0 failures.**

## D1 — THE METHOD ANATOMY: nine steps, graded

Target functional: `Acc_deep := max_gamma #{deep-stratum accidents in shell gamma}`, direction **UPPER**. BB's target is the same object, direction **LOWER**.

| # | step | what it PROVES | direction | applies / fails-because |
|---|---|---|---|---|
| BB-1 | LEMMA DS/FREE | deep stratum ↔ `S' ⊆ Z/n_a`, `\|S'\|=r'_a=L-2`, one condition | bijection | **APPLIES** — bijections are direction-free |
| BB-2 | LEMMA SL | `sig(S) = 2^a·σ'(S') mod n` | exact identity | **APPLIES** |
| BB-3 | THEOREM SM(1) | the stratum meets ≤ `2L` of the `n` shells | upper bound on the shell *support size* | **FAILS** — this is a lower-bound instrument for the max. Concentration is what makes the max LARGE; it is anti-monotone for the target |
| BB-4 | THEOREM SM(2) | structural per-shell count `= C(L,r'_a/2)/L` **exactly** | exact, two-sided | **APPLIES** — the only genuinely two-sided quantitative step BB has |
| BB-5 | LEMMA MULT | `#{(x,y)∈D²: x−y=eps} = 2^{L-2-U}` | exact | **APPLIES**, but is only ever used inside BB-7 |
| BB-6 | LEMMA TC | fibre over `eps` = `C(L−U,(r'_a−U)/2)` | exact | **APPLIES** as a per-fibre cap |
| BB-7 | THEOREM AC | `P ≥ \|D\|²/Q − \|D\|` | strictly LOWER | **FAILS** — Cauchy–Schwarz in this form has no reverse; upper-bounding `P` needs max-fibre control |
| BB-8 | pigeonhole | `max-shell ≥ N_acc/2L` | strictly LOWER | **FAILS** — `max ≤ mean` is false |
| BB-9 | (REALISE) | `L_1(k+w) ≥ X_w(γ)` for **every** γ (`c` free) | quantifier | **APPLIES**, but *raises* the obligation: an upper bound must hold for every γ |

**Registered prediction P1 (6 transport / 3 fail): HELD exactly, and the three failures are precisely the three steps carrying all of BB's quantitative power.** Every occurrence of `Q` in BB enters through BB-7, so the scaffolding cannot manufacture a `1/Q` factor. What an accident upper bound needs is the *opposite* of BB's engine — an equidistribution/spreading statement.

This is why the round-21 warning of record bites here in a second way. Quoting `notes/pilots_20260807/red_closability_probes/REPORT.md:37`: *"at `a=2`, `L_1 = 6 &gt; B* = 5 &gt;= B_C = 5` — so `L_1(a) &gt; B*` does **not** imply `B_C(a) &gt; B*`."* I did not transfer BB's inequality. Every bound below names its own functional and carries its own one-line proof.

## D2 — THE TRANSPORT ATTEMPT: what the surviving steps do give

**PROPOSITION U1 (from BB-1 alone).** `Xdeep(γ) ≤ C(2L, L−2) = C(n_a, r'_a)` for every γ.

**PROPOSITION U2 (from BB-1 + BB-2).** With `M(N,m) := max_γ #{S'⊆Z/N : |S'|=m, σ'(S')≡γ}`,
```
Xdeep(γ)  &lt;=  M(2L, L−2)  =  ( C(2L,L−2) + C(L,(L−2)/2) ) / (2L),   attained at ODD γ.
```
Proof: BB-2 says the shell index is `σ'(S') mod 2L`; drop only the relation `p_1(S')=0`. The closed form is the Ramanathan/Lehmer roots-of-unity count with `gcd(2L, L−2) = 2`, so the `d=2` Ramanujan term survives with `c_2(γ)=(−1)^γ`.

**Subtraction (hard law 5), done and disclosed.** The counting identity is *banked and already used in this lane* — verbatim `notes/pilots_20260806/gamma_shell/PROOFS.md:173-175`: *"`gcd(n/M, r'/M) = gcd(128, 63) = 1` at `v = 34`, for which the number of `m`-subsets of `Z/N` with prescribed sum mod `N` is EXACTLY `C(N,m)/N` (the Ramanathan/Lehmer count; only the `d = 1` term survives)"*. That is the **coprime** case on the **structural sub-family**. U2 is the `gcd=2` case on the **unconditioned superset**. The parity split is likewise banked qualitatively (`gamma_shell/PROOFS.md:162-164`, SM(3)); U2's "odd γ" is its quantitative refinement. **Novelty label: LOW — a one-line corollary of banked instruments.** Its value is that it is the *first upper bound of record* on this quantity and it is below `B*`. A dispatched subtraction sweep found nothing equivalent anywhere; the repo instead names this exact gap three times, e.g. `gamma_shell/PROOFS.md:565-568`: *"**No UPPER bound on the shell population** anywhere. THEOREM AC is a lower bound; the safe side needs an upper bound and does not have one."*

**Toy verification** (exhaustive, no lemma used; MITM over all `C(2L,L−2)` subsets, plus an independent brute force at `L ≤ 8`, plus a third structurally independent LEMMA-TC recount):

| cell | L | p | N_acc | Amax | Xmax | Occ | U1 | U2 | U2 slack | p |
|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 17…97 | 0 | 0 | 1 | 0 | ok | ok | 4.00 | — |
| B | 8 | 17 | 416 | 30 | 30 | 16 | ok | ok | 16.80 | 17 |
| B | 8 | 97 | 80 | 8 | 9 | 16 | ok | ok | 56.00 | 97 |
| B | 8 | 113 | 16 | 2 | 7 | 8 | ok | ok | 72.00 | 113 |
| B | 8 | 193 | 16 | 2 | 9 | 8 | ok | ok | 56.00 | 193 |
| B | 8 | 241 | 0 | 0 | 7 | 0 | ok | ok | 72.00 | 241 |
| C | 16 | 97 | 4848608 | 151930 | 151930 | 32 | ok | ok | **96.97** | 97 |
| C | 16 | 193 | 2432064 | 76308 | 76411 | 32 | ok | ok | **192.81** | 193 |
| C | 16 | 257 | 1823616 | 57366 | 57366 | 32 | ok | ok | **256.82** | 257 |
| C | 16 | 353 | 1332800 | 41876 | 42139 | 32 | ok | ok | **349.62** | 353 |
| C | 16 | 449 | 1042272 | 32888 | 32969 | 32 | ok | ok | **446.87** | 449 |
| C | 16 | 577 | 808256 | 25620 | 25620 | 32 | ok | ok | **575.05** | 577 |
| C | 16 | 641 | 744128 | 23962 | 24677 | 32 | ok | ok | **597.02** | 641 |

All cells are 2-power grids with `p ≡ 1 mod 2L` (`δ_a = 1`, matching BB's break region). **The measured U2 loss factor tracks `Q = p` to within a few percent** — machine-checked. That is exactly what U2 throws away: the relation condition.

**At the prize row (exact integers; witness row `p = 3·2^41+1`, `e=6`, `q=p^6`, `B* = 242251802232021244567343686397347233808 = 2^127.5098`, all reproduced not assumed):**

```
  v    L    2L   r'_a  S(v)=struct/shell  C(2L,r'_a)   M(2L,r'_a)   U2 vs B*
  34  128  256   126   2^117.1491         2^251.6279   2^243.6279   above B*  (VACUOUS)
  35   64  128    62   2^54.6242          2^124.0820   2^117.0820   BELOW B*
  36   32   64    30   2^24.0755          2^60.4910    2^54.4910    BELOW B*
  37   16   32    14   2^9.4818           2^28.8125    2^23.8125    BELOW B*
  38    8   16     6   2^2.8074           2^12.9672    2^8.9773     BELOW B*
  39    4    8     2   2^0.0000           2^4.8074     2^2.0000     BELOW B*

C(128,62) =   22510727468777163197263097882136686400   (2^124.0820)   margin +3.4278 bits
M(128,62) =  175865058349821587492501468423454912      (2^117.0820)   margin +10.4278 bits
```

**COROLLARY U2-ROW.** At the witness row, `Xdeep(γ) ≤ 2^117.0820` for every γ at `w = 2^35`, margin **+10.4278 bits** below `B*`; vacuous at `v = 34`, consistent with THEOREM BB proving the budget genuinely breaks there.

**U2 has one thing BB does not: it contains no `p` and no `δ_a`.** It therefore applies at the `e = 1` prime rows that `gamma_shell/REPORT.md:91` records as *"Prime rows untouched, and unreachable by this method at any `v` in the bracket."* Its price is a budget threshold; coverage of the live `e=1` window `log2 p ∈ [129.5849625, 256)`: **0.00% (v=34), 8.64% (35), 58.15% (36), 82.42% (37), 94.15% (38), 99.67% (39)**.

## D3 — THE nu(A) VARIANT: a SIGN mismatch, and I prove the anti-transport

Type mismatch first: `X_w(γ)` is a deterministic count at one adversarially chosen received word; `nu(A)` is a first-moment functional over random received **pairs** whose max-over-instances step is *already internal* to `averaged_slope_conversion` (*"Since `Y(A)` is integer-valued, not every pair can have `Y(A)&lt;=B-1`; hence one pair has `Y(A)&gt;=B`"*, `critical/nodes/averaged_slope_conversion/proof.md`). So BB-8 is not a missing ingredient — the M route owns its own copy.

But the decisive fact is a **sign**. `E[N(A)]=|A|(1-q^(-t))q^(1-t)` (same file) depends on `A` **only through `|A|`**. Every structural property of `A` enters `nu(A)` only via `C_t(A)`, which carries a **minus** sign. Concentration produces collisions; collisions are what `C_t(A)` measures.

&gt; **THEOREM AT (anti-transport).** With `N = Σ_z X_z`, `Y = #{z : X_z&gt;0}` and `RHS := N − (1/2)Σ_z X_z(X_z−1)` the exact right-hand side of `averaged_slope_conversion` (so `nu(A) = E[RHS]`):
&gt; `RHS ≤ (3/2)N − N²/(2Y)`. Hence `Y ≤ N/3 ⇒ RHS ≤ 0 ⇒ nu(A) ≤ 0 &lt; B*`. Under uniform concentration by `κ = N/Y`, `RHS = N(3−κ)/2` exactly.

Verified exhaustively over **all** occupancy vectors with `N ≤ 14` in exact `Fraction` arithmetic, 0 failures; the largest concentration ratio admitting `RHS &gt; 0` is `14/5 = 2.8 &lt; 3`, so the threshold constant is exactly **3**.

**The number that settles it:** BB's deep-stratum concentration factor is `2^33` (256 shells of `2^41`). `κ = 2^33` gives `RHS = N(3 − 2^33)/2 &lt; 0` for every `N ≥ 1`. **Shell concentration does not bound `nu(A)` — it destroys it.** The round-21 lead (`red_closability_probes/PROOFS.md:417-421`: *"BB's *method* … is the same shape the node's `M` route needs"*) is, read as a positive lead, **backwards**: the shapes are opposed. What would bound `nu(A)` below is large `|A|` plus a **proved anti-concentration/spreading** certificate keeping `C_t(A)` small — the negation of BB's conclusion — plus the node's payload hypotheses (post-paid ownership, exact strict-overlap profile, ambient MCA slope field, first-match ownership).

## D4 — THE HONEST REMAINDER

**Gained:** `Acc_deep`, one of the three terms in gamma_shell's re-pose `X_w(γ) ≤ S(v) + Acc_deep + Acc_shallow`, now has an unconditional `p`-free upper bound below `B*` for `v ≥ 35`. `S(v)` was already exact (BB-4).

**Not gained, precisely:**
1. **`Acc_shallow` and aperiodic `S` are untouched and unreachable by this argument** — U1/U2 use periodicity, and only the deepest stratum is periodic. **This is NOT a safe-side certificate, and by (REALISE) it does not bound `L_1(k+w)`.**
2. **U2 is 42.6 bits lossy** at `v=35`: proved cap `2^117.08` vs heuristic truth `≈2^74.50`, which brackets `+1.436` bits above gamma_shell's banked proved floor `2^73.061` (registered prediction P6.6, HELD).

**The next decisive test.** Sharpening `Acc_deep` requires an **upper** bound on the weight enumerator of `R = {eps ∈ {0,±1}^L : Σ eps_j θ^j = 0}`, since `A_deep(γ) ≤ Σ_{eps∈R\{0}} C(L−U,(r'_a−U)/2)` (BB-6, direction-free). Measured exhaustively: `#R ≈ 3^L/Q` to within 0.3% at `L=16` (`p=97`: `#R = 443777` vs `3^16/97 = 443780.6`), `U_min ∈ {3,4}`. The lattice-point count proving `#R ≲ 3^L/Q` is controlled by the **minimum `l1` weight** of a nonzero relation — i.e. exactly `critical/nodes/integer_code_distance_cert` / Z-1/Z-2, which round-21 PROBE 1 found permanently stuck at `ell = 1`. **The crossing safe side and that round-21 red land on the same missing instrument.**

**A second banked route, named not pursued:** LEMMA Y/MW (`notes/pilots_20260804/crossing_w2_opening/REPORT.md:118`) proves `W_w ⊆ BCH_w`, with **equality when `w ≤ p`**, and `p ≥ 2^39+1 &gt; w` at every official razor row. So `X_w(γ)` *is* a constant-weight-with-prescribed-`sig` count in a cyclic code of designed distance `w` — an upper bound there would bound **all** strata, `Acc_shallow` included. That lane files it as anchor A5 (*"THE HEART"*, OPEN, external).

**Crux restated:** the deep-stratum term is now supplied; the crux is `Acc_shallow` + aperiodic `S`, i.e. a constant-weight population cap for `BCH_w` in a prescribed `sig` class.

## Predictions vs outcomes

| reg. | prediction | outcome |
|---|---|---|
| P1 | 6 steps transport / 3 fail (BB-3,7,8) | **HELD exactly** |
| P6.1/P6.2 | U1, U2 hold at every cell; closed form exact, max at odd γ | **HELD** (verified vs exact DP at L=4,8,16,32,64) |
| **P6.3** | **(U3) `Amax ≤ N_acc/L` FALSIFIED at some cell** | **FALSIFIED PREDICTION — (U3) held at all 17 cells**, worst `R3 = 1.0000` exactly (CELL-B p=113, p=193). Per registered falsifier F2 I label (U3) **HEURISTIC**, do not claim provability, and do not use it. (It would buy nothing anyway: combined with U1 it gives `2·M(2L,L−2)`, one bit worse than U2.) |
| P6.4 | `log2 C(128,62)=124.08±0.05`, `log2 M=117.08±0.05`, margins ~3.4 / ~10.4 | **HELD**: 124.0820, 117.0820, +3.4278, +10.4278 |
| P6.5 | U2 prime-row coverage monotone in v, 0% at v=34, &lt;10% at v=35 | **HELD**: 0.00% / 8.64% |
| P6.6 | `log2 M − log2 p = 74.5±0.1`, within 2 bits above banked 73.061 | **HELD**: 74.4970, gap +1.4360 |
| P7.1–P7.4 | nu(A) type mismatch; sign mismatch decisive; THEOREM AT with constant exactly 3 | **HELD**, constant is 3 |

## Catches and self-corrections

- **CATCH-T1 (banked prose).** `gamma_shell/PROOFS.md:196-199` reads *"the 8 accidents land on the 8 STRUCTURAL shells"* at `(64,8)`, `p=193`. The **8** is a count of accident-occupied **shells**: the artifact `gamma_shell/toy_shell.out` prints `shells: total=8 struct=8 acc=8`, and my exhaustive census (two independent counters) finds **16** accidents on those 8 shells, and 16 on 8 disjoint odd shells at `p=577`. I re-verified every column of that banked table exactly, including `acc=0` at `p∈{257,449,641}` and at all five `(32,8)` cells. **The banked artifact is correct; the prose is ambiguous.** No banked verdict is affected — the theorem uses the shell counts. *Self-correction: my first `dict` stage encoded the prose reading and FAILED 2/2. The failure was mine; investigating it is what located the ambiguity.*
- **CATCH-T2 (a 0.067-bit collision that misleads).** `S(34) = C(128,63)/128 = 2^117.1491` (banked, v=34, structural) vs my `M(128,62) = 2^117.0820` (new, v=35, unconditioned); and `C(128,63) = 2^124.1491` vs `C(128,62) = 2^124.0820`. Exactly `66/63` apart. Different objects at different `v`. My subtraction subagent inferred from this collision that I had an off-by-one in `(L−2)/2`; **I do not** — at v=35, `L=64`, so the second Ramanujan term is `C(64,31)`; at v=34, `L=128`, it is `C(128,63)`, the banked `|W^struct|`. Machine-checked that all four integers are distinct. Flagging so no auditor repeats the inference.
- **CATCH-T3 (my own defect).** My first `E[N(A)]` check wrote `q**(1-t)`, a **float** in Python for `t&gt;1`; the exact-`Fraction` comparison failed 3/3. Repaired to `Fraction(1, q**(t-1))`. Found by my own gate, reported not buried.
- **Minor, mine:** my PREREG §P0 attributes the token `Acc_deep` to the crossing node; the node actually carries the prose *"an ACCIDENT UPPER BOUND on shell populations"* (`statement.md:4088`). `Acc_deep` appears only in `gamma_shell/`.

## Rule compliance

COMPUTE LAW: every `python3` invocation went through `tools/ramguard tiny|local -- python3` from the repo root; all four files were authored with the harness Write/Edit tools (which run no shell and no python), so there was no bare-`python3` patching. No `dag.json`, `nodes/`, or `tools/` edit; no git; no Modal; no status flip; no closure claim. QUARANTINE honoured: `CAMPAIGN_LEDGER.md` never opened by me, the clause was passed verbatim to the single search subagent I dispatched (which reported quoting only lines 2144–2155 and 2257–2258, both before the 2487 marker), and the three sibling round-22 pilot dirs were never read. Fail-closed proven not asserted.

**result:** BB's method does NOT transport to an accident upper bound — its three quantitative steps (SM(1) concentration, THEOREM AC's Cauchy–Schwarz, the max≥mean pigeonhole) are all strictly lower-bound-directed, and concentration is the *source* of the difficulty rather than a tool against it; but BB's scaffolding (LEMMA DS bijection + LEMMA SL identity) transports and yields the first upper bound of record, `Acc_deep ≤ M(2L,L−2) = (C(2L,L−2)+C(L,(L−2)/2))/(2L)`, unconditional and `p`-free, `= 2^117.0820 &lt; B* = 2^127.5098` at the witness row for `w = 2^35` (+10.43 bits, exact integers) and below `B*` throughout `v ∈ [35,39]`, covering 8.6%→99.7% of the live `e=1` prime window that BB provably cannot reach — verified against exhaustive toy censuses at 17 cells with three independent counters (1550 checks / 0 failures, fail-closed exits 1); for the M route the answer is a proved anti-transport (THEOREM AT: concentration by κ ≥ 3 forces `nu(A) ≤ 0`, and BB's κ is 2^33), so shell concentration destroys `nu(A)` rather than supplying it; my prediction that the naive equidistribution transport (U3) would be falsified was itself FALSIFIED and U3 is labelled heuristic and unused; the crux is now `Acc_shallow` + aperiodic `S`, with the sharp deep-stratum bound gated by the same ternary minimum-distance instrument that round-21 PROBE 1 found stuck at `ell = 1`.
