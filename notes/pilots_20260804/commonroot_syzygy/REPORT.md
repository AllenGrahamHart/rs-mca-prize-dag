(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Sanity check: both verifiers re-run clean from the repo root under `ramguard tiny` (41,077 exact checks), writes confined to the pilot directory, and `(WTB)` reproduces the eight published `(P4F4)` cap integers exactly. Re-read the ask: PREREG was written before any code ran, all six falsifiers were pre-registered and none fired.

result: commonroot_syzygy pilot NARROWED the SL-2 active-defect leaf — proved the single shared two-block ledger (WTB) the burn-down asked for, and proved a hard no-go: the affine-dimension ladder caps at s=11,11,10 (block budget X=118/136 collapses to exactly 0 at s=12/11, failing even for a single block), so the whole incidence-counting family is exhausted and the only missing input is now a nameable rigidity conjecture (FR).

## Files (all absolute)

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/commonroot_syzygy/PREREG.md`
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/commonroot_syzygy/ledger.py` + `ledger.json` — 40,704 checks
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/commonroot_syzygy/census.py` + `census.json` — 373 checks

---

# REPORT — commonroot_syzygy pilot (round 13)

**node:** `xr_band_forced_commonroot_syzygy_count` (critical, TARGET) · **verdict: NARROWED**, no status flip · **41,077 exact checks** · all runs `tools/ramguard tiny`, no Modal/network, exact integer arithmetic in every load-bearing comparison.

## 0. Correction to the brief

The brief described this as a fresh wave-46 red needing a gcd/resultant shared-root census on THEOREM R. That is **stale**: the leaf carries **15 PROVED supplier routers** (`background/nodes/xr_deficient_window_*` plus `xr_window_divisor_maximality_filter`), and the Berlekamp-Massey/forced-structure layer is discharged upstream in `xr_window_system_descent` and `xr_deficient_window_primitive_pade_pencil_router`. Attacking as posed would have re-derived banked work (hard law 5). I attacked the residual actually named in the node and in the closing burn-down of `notes/work_cycles/roadmap_r3/14-rate-half-20260730-20260803.md:5984`: *"replace profile partitioning with one weighted two-block ledger that pays near-packed profiles, then determine whether the same block census can be iterated at higher affine dimensions."* Both halves are answered; the second **in the negative with an exact constant**.

## 1. (WTB) — the shared two-block ledger [P1 confirmed]

For any `D`-local family at the tuple-incidence boundary with hull dimension `s&gt;=2`, **arbitrary and possibly mixed** fiber profiles, with `Bset` the set of distinct realised selected blocks:

```
2|Tau ∩ plane| &lt;= 3|Bset|
|Tau| · prod_(j=3)^s (w+j)  &lt;=  (3/2)|Bset| · prod_(j=0)^(s-3)(N-j)
```

Proof: at `r=2ell+1` every block has `v&gt;=3` distinct `phi` values (parts `&lt;=ell`; machine-checked for `ell=1..399`, with sharpness that `v=2` first becomes possible exactly at `r=2ell`), so every block contains a distinct-`phi` triple and `(CRE1)` at `m=2` caps its owners at 3; count `(target, block)` incidences two ways using the two-block router.

**Honestly scoped, as pre-registered:** this is the abstraction of the double count already inside `(P4F4)`, with `6t` replaced by `|Bset|`. Its content is that it takes a **single** budget for a mixed family — profile-local allowances are never summed. It reproduces the eight published `(P4F4)` cap integers exactly at `|Bset|=6t`. Verified exhaustively over all `2^15` families on the `(5,2)` incidence system and `2^14` on `(6,2)`, with a load-bearing negative control (my first control was vacuous — no block in `(5,2)` can reach 4 owners — so I moved to `(6,2)` where the cap genuinely bites).

## 2. The exact block budget X [P2 confirmed]

| rates | s | sigma | t | 6t | **X** | headroom |
|---|--:|--:|--:|--:|--:|--:|
| 1/4,1/8 | 11 | 5 | 2..7 | 12..42 | **118** | 9x → 2x |
| 1/16 | 10 | 1 | 2..3 | 12..18 | **136** | 11x → 7x |

`X` is independent of `t`, satisfies `X &gt;= 6t` on every entry `(P4F4)` marks paid, and is the exact threshold (`X` pays, `X+1` does not — asserted everywhere). **Decisive fact: `X ~ 10^2` while `ell ~ 1.2e9`.** Only an `O(10^2)` currency fits the budget.

## 3. THE NO-GO — the dimension ladder is capped [P6 refuted as posed]

| s | 9 | 10 | 11 | 12 |
|---|--:|--:|--:|--:|
| X, rates 1/4,1/8 | 10,504,211 | 35,249 | **118** | **0** |
| X, rate 1/16 | 81,424 | **136** | **0** | 0 |

`X` collapses by exactly `N/w = 297` (resp. `596`) per dimension — each extra dimension trades a factor `w+j` for `N-j`. **Asserted, not printed**, at every row and tail: at `s=12` (rates 1/4,1/8) and `s=11` (rate 1/16), `X=0` and **even `|Bset|=1` exceeds the budget**. So no block-scarcity theorem whatsoever reaches the next dimension — not a sharper census, not perfect rigidity. `(P4F4)` pays `s=11,11,10`; `s&gt;=12,12,11` is now proved unreachable by this family.

## 4. The whole (CRE2) tuple family is exhausted

| block profile | m=2 | m=3 | m&gt;=4 |
|---|---|---|---|
| packed `(ell,ell,1)`, v=3 | over budget `~1e9` | `T_4=0`, vacuous | vacuous |
| `(ell,ell-1,1,1)`, v=4 | over budget `~1e8` | over budget `~1e15` | vacuous |

Deeper cuts do not help: `T_(m+1)` grows like `ell^2` while `C(e,m+1)` grows like `ell^(m+1)`, so the coefficient worsens by `~ell` per step while the lift improves only by `~300`. With §3 this bounds every `(APT1)/(FSP6)/(FSP7)/(CRE2)/(P4F4)` variant — **block scarcity is the only member still in range**.

## 5. Near-packed extension [P4 confirmed, modest] + a new exception

The census `beta(mu,pi_1,pi_2) = Σ over fiber-intersection vectors realising pi_1 that admit a disjoint pi_2 mate, of prod_i C(mu_i,m_i)` is validated against exhaustive brute-force subset enumeration at `ell=3` on packed, non-packed and split strata (every case exact).

**Extension obtained:** `beta = 6t` holds for an *arbitrary* tail fiber structure, not just the `t` singleton fibers `(P4F4)` states — verified at tails `(1,1)`, `(1,1,1)`, `(2,2)`, `(2,1,1)`, `(2,2,1)`, and at the official rows for every admissible `t`.

**Exception found by this pilot:** if a tail fiber *reaches* size `ell` it becomes a fifth full fiber and the `6t` rigidity fails outright — at `ell=3, t=4`, tail `(3,1)`, the census gives `beta=100`, not `24` (brute-force confirmed). The official rows are protected only by the hypothesis `ell &gt; sigma+2 &gt;= t`.

## 6. The exact residual boundary [P5 confirmed]

Any block taking `m` points from a fiber of size `f` with `0&lt;m&lt;f` costs a factor `C(f,m) &gt;= f` (unimodality, verified exhaustively for `f&lt;200`), so **any stratum splitting a fiber of size `&gt; X` is unpayable**. The residual is non-empty and I exhibit it: on the packed `D`, both blocks with profile `pi = (ell, ell-1, 1, 1)` (sums to `r`, all parts `&lt;=ell`, `v=4`), `B_1 = F_1 ∪ (ell-1 of F_2) ∪ (1 of F_3) ∪ (1 tail point)` with the mirror mate — the two-block closure **is** satisfiable. Census validated by brute force at `ell=3` (`beta = 432, 756, 1080` for `t=2,3,4`); at the official rows `beta = 72,281,119,501,125,798,912` (rates 1/4,1/8, t=2), i.e. **`~1e18 × X`**. Several other natural split profiles, e.g. `(ell,ell-1,2)`, are *empty* — recorded so the boundary is exact rather than assumed.

## 7. What this hands the campaign

1. **`s &gt;= 12,12,11` needs a different mechanism.** The signed support-moment / exchange-compression interface of `xr_window_divisor_maximality_filter` is the only candidate on the board, and it must beat a factor `~300` per dimension, not a constant.
2. **At `s &lt;= 11,11,10` the only missing input is now nameable:**
   &gt; **(FR) fiber-rigidity conjecture.** At the tuple-incidence boundary, every selected block is a union of full `phi`-fibers of `D` together with at most one further point.

   `(FR)` gives `beta &lt;= 6t &lt;= 42 &lt; X`, closing every stratum at `s &lt;= 11,11,10` with the single `(WTB)` budget, mixed profiles included. Without it §6 shows counting alone provably cannot. **(FR) is the correct home for the brief's forced-common-root instinct** — it is exactly the claim that rank deficiency forces the selected agreement geometry onto complete pencil fibers, where THEOREM R-style arguments plausibly bite. Recommended as the next named obligation, replacing "count the mixed profiles".

## 8. Prediction ledger

P1 confirmed (also honestly scoped as a repackaging) · P2 confirmed (118/136) · P3 confirmed vs brute force on all strata · P4 confirmed but modest, plus one new exception · P5 confirmed with explicit exhibit · **P6 refuted as posed** (capped, not an open-ended interval). Falsifiers F1–F6 all cleared; none fired.

## 9. Flags

- **No status flip.** Node stays `TARGET`. `(WTB)` is a proved lemma but pays nothing new without `(FR)`.
- **Hypothesis flag.** `ell &gt; sigma+2` in `xr_deficient_window_packed_four_fiber_plane_payment` is load-bearing (§5) — not a defect, the node asserts it, but it must appear in any restatement.
- **Scope flag.** The `s`-ladder cap `s &lt;= 11,11,10` applies to `(APT1)`, `(FSP6)`, `(FSP7)`, `(CRE2)` and `(P4F4)` alike; any future plan proposing "iterate the census upward" should be rejected on sight.
- **No empirical laws.** Every number is exact integer arithmetic. The only inductive step is the choice of catalogue strata in §5–§6, which is a selection of exhibits, not a claim of exhaustiveness over all profiles.