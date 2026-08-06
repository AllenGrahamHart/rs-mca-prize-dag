(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Sanity check clean: all controls re-pass (C-c norm engine vs the banked engineered prime, C-a/C-b Burnside counts, P1 symbolic identity), and 8 artifacts are in place under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/c1_sharpest_leaf/`. REPORT.md was harness-blocked, so the report follows here.

# Round 14, Mystery 3 — junction-0 / C1–C2'' lane

Pre-registration at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/c1_sharpest_leaf/PREREG.md` (written before any computation). Repo HEAD `5884c5d8`.

## HEADLINE

Sharpest leaf = `dli_wcl_slot_1_5_emptiness`. Attacking it produced a **decisive negative on the lane's last surviving named route**: the `Delta` (Nullstellensatz certificate) route is infeasible at the *smallest* of the ten slots, hence at all ten. Any certified `Delta_1` is divisible by every supporting characteristic; those number ~7.5 million, giving `log2|Delta_1| &gt;= 4.4e8` bits (~55 MB just to write the integer down). The pre-registered infeasibility threshold was `10^7` bits — missed by **43.9x**, needing 97.72% of prime mass to collide against a measured 7%.

Route status for the ten leaves:

| route | status | source |
|---|---|---|
| max-norm gate (WCL fence) | DEAD — all open slots `w&gt;=5`; `23^64 = 2^289.5 &gt; 2^256` | banked, `notes/pilots_20260802/dli_norm_gate/REPORT.md:63-69` |
| count / Minkowski 2nd minimum | DEAD — LAT1 minima law; `kappa&lt;=1.507` vs needed `[3.97,8.73]` | banked, `notes/pilots_20260802/wcl_count_bounds/REPORT.md:6-42` |
| direct ambient norm census | alive **only** at `(1,5)`; dies at `(1,7)` | banked fence + this pilot's sizing |
| **`Delta` sparse certificate** | **DEAD — this pilot** | new |

**Eight of the ten junction-0 leaves now have no viable route at all.**

Countervailing good news: the census route was fenced in 2026-07-13 as too expensive, and **that call is stale** — `(1,5)` alone costs ~65–130 CPU-hours, not "millions of norms" of pain.

## 1. LANE MAP

`dli_wcl_zone_coverage` (CONDITIONAL) `requires` exactly ten leaves, all `status: TARGET`, all `requires: []` (pure unproved leaves), all in `critical/nodes/` — with PROVED classifiers in `background/nodes/`:

| slot | classifier (all PROVED) | base vars |
|---|---|---:|
| (1,5) | `odd_next_boundary_square_divisor_descent`: `Y A^2-(bY+1)^2 \| Y^256-1`, `deg A=2` | **3** |
| (1,6) | `ell1_weight6_even_norm_divisor_descent`: `E^2-YB^2 \| Y^256-1` | 5 |
| (1,7) | `extended_six_slot_sparse_divisor_endpoints`: `YA^2-B^2 \| Y^256-1` | 5 |
| (1,8) | same: `E^2-YB^2 \| Y^256-1`, `deg E=4` | 7 |
| (2,7) | `odd_next_boundary...`: `\| Y^512-1`, `deg A=3` | 4 |
| (2,8) / (2,9) | `extended_six_slot...` `\| Y^512-1` | 6 / 6 |
| (4,9) | `ell4_weight9_quartic_divisor_descent`: `Y A^2-1 \| Y^1024-1` | 4 |
| (4,10) / (4,11) | `ell4_weight10/11_..._descent` `\| Y^1024-1` | 6 / 6 |

**Minimal set = all ten, with no proper subset**, because the requirement is structurally forced to be zero-event. Machine-checked exactly this round: one primitive weight-`w` orbit at level dimension `ell` contributes `512*ell/2^w`; worst case `w=ell+7` gives `4*ell/2^ell` = **2, 2, 1** at `ell = 1, 2, 4` — every one exceeding the `W_cl &lt;= 1/32` budget by 32–64x. Newton empties `ell&gt;=8` outright. So a single relation anywhere in any live window blows the budget; no majorant, counting, or density argument has slack to exploit, and slots cannot be traded off.

**The r3 window extension is the fault line.** Widening `[L+1,L+5] -&gt; [L+1,L+7]` (2026-07-21) is exactly what turned a four-slot residual `{(1,5),(1,6),(2,7),(4,9)}` into ten. The six *added* slots are precisely the ones with no route (census class counts `6.4e9` to `1.5e22`). The four original ones are the tractable ones.

**C1-ZERO/SWIF-4** (the consumer's other half) is not a DAG node. Banked correction: *literal SWIF-4 may be FALSE while C1-ZERO is TRUE*; its proposed spine CERP-512 was retired same-day. Surviving: `dli_c1_l1_block_owner_ledger` (PROVED — C1-ZERO at `L=1` is *exactly* `sum_j (A_j - 15*2^(4j)/q) &lt;= 3+1/q`, an identity that bounds nothing).

## 2. VERDICT ON `(1,5)`

**Controls, all PASS before any claim.** C-c: my norm engine reproduced the banked engineered weight-6 witness exactly (`...252866 = 2q`, `q` prime, 256-bit, `v_2(q-1)=9`). C-a/C-b: independent Burnside recomputation of all four class counts (`254 / 24,979 / 2,296,920 / 185,569,028`) in 6 s. P1: coefficient identity symbolic, all six coefficients.

**P2 (supporting-prime lemma) — PROVED and verified constructively.** Every odd prime `p | Res(X^256+1,P)` is a supporting characteristic: `gcd(P, X^256+1) != 1` over `F_p` gives `w` with `w^256=-1`, hence exact order 512. End-to-end machine check (`verify_delta_premise.py`): for each such prime the script finds `w`, applies the banked dilation (`nu=205`), reads `(a0,a1,b)` off the `OND4` shape, forms `G`, and checks `Y^256 == 1 mod G`. **61/61 PASS**, primes from `7681` to `8.34e58`; the `gcd` form passed 68/68.

**P3 — the verdict.** Since banked theory binds *every* valid `Delta` ("Every finite characteristic supporting the corresponding WCL relation divides any certified `Delta_ell`"), `Delta_1` is divisible by the lcm of all 2,296,920 class radicals. Measured on 68 classes (60 fully factored): norms mean 202 bits, 3.27 distinct primes/class, 191.1 prime-mass bits/class, 56.7% carrying a `&gt;=100`-bit prime. Extrapolated: `log2|Delta_1| &gt;= 4.39e8` bits, ~7.5e6 prime factors. Robust floor using only effectively-unshareable `&gt;=2^100` primes: `1.30e8` bits — still 13x past threshold on its own. **`Delta` route dead.**

**Why this was inevitable (worth banking).** The divisor condition `G | Y^N-1` lives over `F_q-bar`; the official gate `v_2(q-1) &gt;= 41` is a condition on the *prime field*, invisible to the geometry since `mu_512 subset F_q-bar` for every odd `q`. So any ideal-theoretic reduction is intrinsically **v_2-blind**, and the gate can only be applied after factoring a prime list. The lane law's prescription "slots need v_2-aware certificates" therefore necessarily means *the census* — `Delta` is just the census multiplied together, strictly worse.

**P5 falsifier watch — negative, margin quantified.** Zero eligible primes. Max `v_2(p-1)` observed = **20**, which moves the weight-5 record from the banked 17. Ladder: 18 (w=3), 29 (w=4), 17 (w=5, 256 rows), **20** (w=5, this pilot). Heuristic risk that the *complete* census finds a gate-eligible prime: ~0.09%.

**P4 census cost (EMPIRICAL).** 0.37 s median / 2.04 s mean per class in pure-Python sympy; 12% need real ECM/QS. Full `(1,5)`: 1,300 CPU-hours here, **~65–130 CPU-hours** with PARI/FLINT. Family sizing: `(1,6)` ~10^4 CPU-h (possible), `(1,7)` ~10^6 (infeasible), `(1,8)` onward hopeless.

## 3. COMPUTE REQUEST — CR-W5-ELL1

Closes `dli_wcl_slot_1_5_emptiness` only (TARGET → PROVED); promotes nothing else. Continue the banked weight-3/4 template verbatim: partition all `140,952,784,896` reduced signed weight-5 words into the **2,296,920** affine-Galois classes under `e -&gt; ae+b mod 512`, `a` odd; per class take exact `Res(X^256+1,P)` by the iterated relative norm `alpha(X)alpha(-X)` (8 halvings, engine validated by C-c); factor completely with recursive Pocklington certification; report any prime `p &lt; 2^256` with `v_2(p-1) &gt;= 41`. Verifier: independent orbit-partition reconstruction plus CRT recomputation modulo enough certified 31-bit split primes to exceed `2*5^256`, made exact by `0 &lt;= Res &lt;= 5^256`. **Cost 65–130 CPU-hours (~2 h on 64 workers)**; ~7.5e6 factor records; certificate ~450 MB gzipped (~90x the banked weight-4 artifact) — shard by orbit-key range. Falsifier: one eligible prime, which refutes `(1,5)` and kills the ten-slot program — a result of equal value. Recommend gating on anchor A1 first.

## 4. RANKED NEXT ANCHORS

- **A1. Audit the C1'-r3 window extension `+5 -&gt; +7`.** Highest leverage by a wide margin, and cheap (a derivation audit, no compute). It created the six unroutable slots. Why 7? Is it tight or a lossy overshoot? A rollback takes the leaf set from ten (8 unroutable) to four (1 closable now, 3 with small classifiers).
- **A2. Re-pose WCL-ZONE to avoid per-slot zero-event obligations.** The `1/32` constant is load-bearing (§1: zero slack). Brief-1 notes the ten-slot route delivers `W_ext = 0`, *stronger* than what the assembly uses — quantify that gap; it may be pure overkill.
- **A3. Run CR-W5-ELL1.** Only slot any known method can close. Gate on A1.
- **A4. The unrun large-deviation falsifier** (`wcl_count_bounds/REPORT.md:58-62`). My sample supplies the calibration it lacked (`v_2` median 9, max 20; gate 41 = 21 more doublings). Cheap; a hit kills `(1,5)`.
- **A5. Re-price the board:** with 8/10 slots unroutable, the slot half of the consumer is the *harder* half, contrary to the Brief-1 framing that calls it "already mechanical".
- **A6 (recorded negative, do not repeat).** The single-equation `Phi` reformulation of `(1,5)` is **dominated**: 8.5x fewer classes (~269k vs 2.30M) but degree-8 amplification pushes norms from ~2^200 to ~2^1326. Derived and discarded this round.

## 5. FLAGS

1. **Board legibility:** all 23 `background/nodes/dli_wcl_*` are PROVED while all ten obligations sit in `critical/nodes/` — a background-only survey reads as fully green.
2. **Stale text** in `dli_wcl_zone_coverage/statement.md`: three mutually inconsistent leaf-set claims layered by date (six → four → ten); only the ten-slot reading matches the edges.
3. **A `refutes` edge points at a PROVED node it also feeds:** `dli_c1_ternary_relation_norm_sandwich` → `dli_norm_gate_energy_ceiling`, while the ceiling cites that node as its proof source. Likely meant for the doubling-law conjecture.
4. **Schema drift:** `dli_wcl_ell4_weight10/11_*` carry `gate: "all"` and no `closure` key, unlike the other 21.
5. **Route-fence line** `weight5_orbit_route_fence.md:50-56` needs a note that `(1,5)` alone is now measured at ~100 CPU-hours.
6. `__pycache__` committed in six `background/nodes/dli_wcl_*` dirs.

## 6. WHAT I DID NOT CLAIM

Not a proof or refutation of `(1,5)` — it stays TARGET. Not a theorem that `Delta_1` is large: the *premise* (P2) is proved and machine-verified, but the *count* of distinct supporting primes is an extrapolation from 68 classes, labeled EMPIRICAL; it survives 44x pessimism but is not a proof. The banked divisor-descent theorems are correct — only their deferred closing step is shown unexecutable. No statement about the other nine slots, WCL-ZONE, C1', C2'', C1-ZERO, or either Prize target.

result: Junction-0 lane mapped (ten TARGET slot leaves, minimal set = all ten, zero-event forced); attacked the sharpest leaf (1,5) and killed the lane's last named route — the `Delta` certificate route is infeasible (`log2|Delta_1| &gt;= 4.4e8` bits vs a 10^7 pre-registered threshold), leaving 8/10 leaves with no viable route, while the (1,5) census is re-priced from "too expensive" to ~65–130 CPU-hours and filed as CR-W5-ELL1.