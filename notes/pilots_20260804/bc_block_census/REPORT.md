(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Sanity check: all four verifiers replayed from scratch — **34,332 exact checks, 0 failures**; the FR positive control reproduces round-14's audited `gate_max = 29`. REPORT.md is harness-blocked, so the report follows in full.

---

# REPORT — bc_block_census pilot (round 15)

**node:** `xr_band_forced_commonroot_syzygy_count` · **obligation:** `(BC)`, adopted at `../fr_fiber_rigidity/FABLE_AUDIT.md` · **replay:** 4 verifiers, **34,332 exact checks, 0 failures** (theory 33,995 · fixture 102 · dlocal 8 · sweep 227)

## VERDICT

**(BC) is REFUTED as a uniform bound, and its round-14 evidence is withdrawn as a pigeonhole artifact.** The route is closed on all three attack axes.

1. **BC-F1a FIRES.** A fully admissible fixture with `|Bset| = 4 &gt; 2` exists — 4 shapes, every clause of the round-14 witness stack plus an **exhaustive** tangent gate.
2. **BC-F3 does NOT fire, and that is the point.** At the round-14 pinning `n = 3d+k-(sigma+1)`, `|Tau| &gt;= 2` is *impossible*: the pigeonhole misses by **exactly `t-1 &gt;= 1`, identically in `(h,k)`**. The eight round-14 runs read `|Bset| = 2` because `|Tau| = 1` was **forced**, not because blocks are scarce.
3. **BC-F6 FIRES (the honest negative).** Reuse is a **free parameter** at `|Tau| = 2`. **BC-F5 does not fire** — the gate does not separate reuse from no-reuse.
4. **BC-F7 does NOT fire.** No regime split: identical behaviour above and below Johnson. Route 3 dead.
5. **BC-F9 does NOT fire, closing route 2.** At every prize row `K := k-ell` exceeds `e` by **55–112x**, so `RS_K -&gt; F_q^D` is surjective and *all* `C(e,r)/2` partitions are realised.

**Route 4: ZERO `(WTB)` strata close. `s &lt;= 11/11/10` is NOT paid, in any regime containing a prize row.**

## THE REUSE LAW (the measurement the audit asked for)

```
R = 2|Tau|/|Bset| is NOT determined by (u,v,P,Q,D,gate). At |Tau| = 2 both
extremes are fully admissible:  R = 2 (|Bset| = 2)  and  R = 1 (|Bset| = 2|Tau| = 4).
The tangent gate is INDIFFERENT to the choice, above and below Johnson.
```

| shape | k/K/n/q | Johnson | reuse | noreuse | gate |
|---|---|---|---|---|---|
| A2-above | 5/2/60/61 | ABOVE | `|Bset|`=2, R=2.0 | `|Bset|`=**4**, R=1.0 | holds, exhaustive |
| A1-above | 4/1/60/61 | ABOVE | 2, R=2.0 | **4**, R=1.0 | holds, exhaustive |
| B1-below | 4/1/213/853 | BELOW | 2, R=2.0 | **4**, R=1.0 | holds, exhaustive |
| B2-below | 5/2/183/367 | BELOW | 2, R=2.0 | **4**, R=1.0 | holds, exhaustive |

*Why:* at each `x in D` the pair `(u_x,v_x)` is two scalars and prescribing one target's slope at `x` is one affine condition — two targets consume both dof, so both partitions are freely choosable; only from the *third* target is anything forced.

**Structural law confirmed (BC-F2 does not fire):** at `sigma=0` blocks partition `D`, so sharing one block forces sharing both — `|Bset| = 2·#partitions` in 8/8 fixtures and all 226 sweeps; no two targets ever shared exactly one block.

## NEW LAYER (machine-verified)

- **(CORE-LENS)** — off-`D` companion of the round-14 LENS: `Core_tau subset H\D` and `Core_tau = {x in H\D : tau(x) = m_x}`. Maximality is *itself* an agreement condition; the object is two punctured agreement problems on complementary point sets.
- **(2-TARGET)** — `|Tau| &gt;= 2` requires `n &gt;= k + 2d + ell + 1 + e`; at the round-14 pinning `margin = -(t-1)` identically (15,090 triples + both named shapes).
- **(PACK)** — `|Tau| &lt;= C(n-e,K)/C(k+d,K)`; same `prod(N-j)/prod(w+j)` shape as `(P4F4)`/`(WTB)`, their trivial case.
- **(D-LOCAL CEILING)** — `|Bset| &lt;= 2·#partitions(Tau_D)`, dropping the core condition; where route 2 lives or dies.

## ROUTE 2 — where the list count dies

Per-slope packing bound `C(e,K)/C(r,K)` = 2/4/10 at `K`=1/2/3; **measured max blocks per slope = 1** in every case. Exhaustive `D`-local sweep over **226 configurations**: `#partitions` histogram `K=2 {1:38, 2:188}`, `K=3 {1:2, 2:4}` — **never exceeds 2**. So at `K &lt; e`, `|Bset| &lt;= 4 &lt;&lt; X`. But:

| row | rate | `K` | `e` | `K/e` | `K&lt;e`? |
|---|---|---|---|---|---|
| 1/4,1/8 | 1/4 | 548,528,680,376 | 4,908,534,050 | **111** | NO |
| 1/4,1/8 | 1/8 | 273,650,773,432 | 4,908,534,050 | **55** | NO |
| 1/16 | 1/16 | 136,825,386,716 | 2,454,267,026 | **55** | NO |

All **1716 = C(14,7)/2** partitions verified realised when `K &gt;= e`. Route 2 fails at the rows by 55–112x — not an epsilon: the punctured code is the *entire* space `F_q^D`.

## CATCH (recorded in PREREG before computing)

The brief's `(BC)` formula counts **ordered pairs** `(nu,tau)`, which by `(TKS2)` is identically `2|Tau|` — making `(BC)` *literally equivalent* to `|Tau| &lt;= X/2`, the statement the lane exists to prove. Only the consumer's distinct-block definition is non-circular; that is the one used throughout.

## MACHINERY (offered to mint)

**Bucketed slope-free tangent gate.** (a) *Bucketing*: split `T` into `g` buckets with `g(k-1) &lt; need`; enumerating `k`-subsets inside buckets is exhaustive. (b) *Slope-freeness*: `U_nu` is linear in `(alpha,beta)`, so residuals `R_u,R_v` settle every slope at once — one histogram replaces the `P^1` loop. **Positive control on the audited round-14 witness:** reproduces `gate_max_agreement = 29` exactly using **20 subsets vs round-14's 52,360** (2,618x), and at threshold `A-1` correctly *finds* the over-agreement (not vacuously passing).

## FLAGS

- **The round-14 `|Bset| = 2` should be withdrawn, not just kept EMPIRICAL** — it is consistent with any reuse law whatsoever.
- **`(BC)` should not remain the leaf's obligation of record.** At the rows it is equivalent to the counting problem it was introduced to solve. The non-circular residual is the *off-`D`* statement `|{x in H\D : tau(x) = m_x}| = k+d` — which routes to the mu_n anti-concentration terminal the round-14 audit already named.
- **Stopped short, stated not papered over:** `|Tau| &gt;= 3` with distinct partitions needs `K &gt;= e`, hence `k &gt;= 17`, where the gate's bucket count collapses to `g = 1` and exhaustive verification is infeasible at toy scale. **BC-F1b is established at `|Tau| = 2` only**; the `M &gt;= 3` construction is NOT claimed.
- Toy shapes are all `P = X^3`, `ell = 3`, `sigma = 0`, `t = 2`. **`sigma &gt; 0` untested** — there blocks no longer partition `D` and the `(REUSE LAW)` statement itself changes.
- No status flip proposed.

## FILES (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/bc_block_census/`)

`PREREG.md` · `theory.py`+`theory.json` (33,995 checks) · `fixture.py`+`fixture.json` (102) · `dlocal.py`+`dlocal.json` (8) · `sweep.py`+`sweep.json` (227). REPORT.md blocked — this message is the report.

result: (BC) block census REFUTED as a uniform bound — round-14's |Bset|=2 was a forced pigeonhole (|Tau|&lt;=1, margin exactly -(t-1)), reuse is a free parameter at |Tau|=2 with |Bset|=2|Tau|=4 passing an exhaustive tangent gate above and below Johnson, and the list-count route dies at every prize row where k-ell exceeds e by 55-112x; zero (WTB) strata close; 34,332 checks, 0 failures.