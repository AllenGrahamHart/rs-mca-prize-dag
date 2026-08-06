(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

# PILOT REPORT — the t/q pin (mystery 2, round 16, `f2_tq_pin`)

**Opus 5, 2026-08-06.** Replay: `tools/ramguard tiny -- python3 notes/pilots_20260806/f2_tq_pin/verify.py` → **64 checks, 0 FAIL**, digest `F2_TQ_PIN_VERIFY_ALL_PASS`. Artifacts (all inside the pilot dir): `PREREG.md` (brief + my appendix Q1-Q7), `PROOFS.md`, `verify.py`, `VERIFY_LOG.txt`.

## HEADLINE

**The t catch resolves, and it resolves harder than posed.** `t = 7e10` is not a competing modelling choice — it is a **unit error**, recoverable only by dividing the banked window-bits product by the *characteristic* of a field that **no prize-admissible row possesses**. The rules freeze forbids it twice over. And the deeper finding: **the 16-rung KoalaBear tower is not a prize-admissible row at all.** `q_16 = p^{2^16}` exceeds `|F| < 2^256` by a factor of **7933x in bits**; the rules cap the tower at **two rungs**. So mystery 2's "discharged at rungs 1-13" headline was never a statement about an admissible field — and under every admissible `t` the correct band is **rungs 1-10**, or **1-9** under the stricter reading the campaign's own rules clause mandates.

## VERDICTS — pre-registered deliverables

**(P1) Provenance chain for q — DELIVERED, and it is a negative pin.** The freeze pins an *admissibility region and a quantifier*, not constants: `rules_freeze/statement.md:9` ("smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16}"), corroborated verbatim by `field_cap_check/statement.md:13` and bounded above by `official_row_primes_pinning/proof.md:25-33` ("These are admissibility and quantifier conditions, not a list of prescribed prime constants"). There is **no rules-level p, k, q, or t**. What the rules *do* force: (R1) the smooth domain is a subgroup of `F^*`, so `n | q-1`, so `q > n`; (R2) `L = log2 q < 256`; (R3) plan against the stricter reading on any ambiguity.

Applying these at the maximal rate-1/2 row (`n = 2^41`) with `q = p^e` and LTE gives the complete admissible region: **`v_2(e) <= 2`, `e <= 6`, `log2 p >= 39`, tower depth <= 2 rungs**. The KoalaBear `log2 p ≈ 31` base field is **inadmissible**. I also constructed an explicit admissible prize-max row to show this is not vacuous: `p = 18446735827372343297` (prime, `v_2(p-1) = 39`), `q = p^4`, `log2 q = 255.99997 < 256`, `v_2(q-1) = 41` so `2^41 | q-1` exactly, `ord_{2^41}(p) = 4`. On the L window: `L = 255.9` is self-labelled a **convention** at `xr_radius_arithmetic/proof.md:33`, not a rules citation — and it does not reconcile (see CATCH-2).

**(P2) Derivation of t — DELIVERED.** `t = |Lambda|`, the number of Newton conditions `p_l(S) = 0`, defined globally not per rung. Each is one field equation costing `log2 q` bits against `n` bits of block space, so the window is empty iff `t·L >= n`. This agrees with the exact FM+gate formula (T*) of `xr_radius_arithmetic/proof.md:41-43` to **0.0044%**, giving **`t = n/L`**. With (R1) `L > 41` and (R2) `L < 256`: **`t ∈ (2^33, 5.364e10]`** at `n = 2^41`. I reproduced the banked four-rate corridor table to the last digit as a control. Two independent lanes corroborate the `2^33` endpoint (`official_scale.json` n/t = 2^41/2^33, and `TARGET_3C_EXTRACTION.md:42-43`'s "(2^33, 256) is correct at rate 1/2").

**(P3) Adjudication — `t*` WINS; `7e10` is excluded by the rules.** Both literals descend from the *same* banked product (`f2_sl1_powersums/PROOFS.md:372-377`), differing only in the divisor — which makes this adjudicable. `7e10` back-implies `log2 q = 31.415`, but a field of that size cannot contain a subgroup of order `2^41`. Excluded under **both** field readings (extension cap `n/41 = 5.36e10`; base-field cap `n/39 = 5.64e10`) and at **both** `n = 2^40` and `n = 2^41`. `t* = 8,592,912,739` lies inside the interval. Honest scope: the derived quantity is an *interval*, so `t*` is right to three significant figures and right in kind; `7e10` is wrong in kind.

**(P4) m_16 — RESOLVED as a reading conflict, not an error.** `2^38` = new-part (elements of order *exactly* `n_j`, `φ(2^{24+j})/2 = 2^{22+j}`); `2^39` = nested (`n_16/2`). `PREREG.json:57`'s own formula `n/(2 log2 p)` sets `m = n/2`, which is exactly the nested count — so the two documents were counting different windows. **`m_16 = 2^38` is correct for the deployed window as `tower.py:17` defines it**; `PREREG.json:58` is a stale estimate never reconciled. But `2^38` is the *looser* reading, and `rules_freeze:9` mandates planning against the stricter one — see CATCH-3.

**(P5) LEMMA 3 recomputed at all 16 rungs — band stated plainly.** Controls first: the banked 7.89x reproduces as 7.8915x, the 0.9687x sign flip reproduces exactly, and the banked 1-13 / 1-10 bands reproduce. Worst case over the rules-forced t-interval:

| window | LEMMA 3 holds | THEOREM A/B band |
|---|---|---|
| new-part (`m_16=2^38`) | rungs 1-15 | **rungs 1-10** |
| nested (`m_16=2^39`, stricter) | rungs 1-14 | **rungs 1-9** |

Under **every** admissible `t`, LEMMA 3 — a *proved necessary condition for (O1)* — is **VIOLATED at rung 16**, and at rung 15 too under the stricter reading. The "rungs 1-13" headline is reachable only at `t = 7e10`, which no admissible field realises. Per my pre-registered falsifier: **the band is shorter than rungs 1-10 under the stricter reading — it is 1-9.** SL-1 is unaffected (`0.01563` at rung 16 reproduces; `f2_sl1_powersums`'s immunity survives).

**(P6) |K1|/PP5.0 — CANNOT be frozen from rules-level sources; instead PRICED.** PP5.0 is explicitly unfrozen (`f2_fixed_sector/REPORT.md:31`) and its only "freeze" is an internal working budget of 1/43 (`00-overview-and-gate-addendum.md:58`) — the rules say nothing about composition laws. So I priced the seam instead. With `dim K1 = ceil(t/2)`, the extension reading gives `log2|K1| = (t*/2)·L = (t*·L)/2 = n/2` — a **structural identity**, not a coincidence. **Average-vs-sum is therefore exactly a factor `2^{n/2}`**: (O1)'s target `2^{n/2+o(n)}` becomes `2^{n+o(n)}` under the sum reading. In the base reading it costs `n/(2e)` bits. **Under both readings the seam is Θ(n), never o(n)** — it cannot be absorbed into (O1)'s slack. The open choice, stated exactly: does PP5.0 consume K1 as an average over `K1` or as a sum over it? Nothing at rules level decides it.

## VERDICTS — my own registrations

**Q1 CONFIRMED** (tower breaks the field cap from rung 4). **Q2 CONFIRMED** (divisor must be `L`; `n | q-1` forces the interval). **Q3 CONFIRMED** exactly (`v_2(e)<=2`, `e<=6`, `log2 p>=39`, depth <=2). **Q4 CONFIRMED** (nested vs new-part, as predicted). **Q5 FALSIFIED** — see below. **Q6/Q7 honoured** (worst-case protocol; interval not collapsed; shorter band reported unsoftened).

**Q5 FALSIFIED, reported as a normal outcome.** I predicted the `[255.9113, 256)` sliver was `{L : t*(L) <= 2^33}` under (T*). That set's left endpoint is **255.988729**, not 255.9113 — off by 0.077 bits. The true generator, found afterwards and verified to 1e-4, is the **pure counting balance** `L >= n/t* = 255.911275`. My registration was wrong about the mechanism; the corrected formula is CATCH-5.

## CATCHES

1. **CATCH-1 (maintainer-level).** The 16-rung KoalaBear tower is not prize-admissible: `log2 q_16 = 2,030,874` vs a 256-bit cap. This answers the standing question at `field_cap_check/statement.md:9` verbatim — *"whether non-generating rows (hence the tower case) are admissible"* — **they are not, at rungs >= 4.**
2. **CATCH-2.** The `L = 255.9` convention lies **below** the sliver's own left endpoint `n/t* = 255.911275`: at `L = 255.9`, `t*·L = 2.198926e12 < n = 2.199023e12`. The corridor edge and the sliver are mutually inconsistent by 0.011 bits — `t*` is computed at a point that fails the emptiness balance the sliver encodes.
3. **CATCH-3.** `m_16 = 2^38` is the looser of two correct readings; `rules_freeze:9`'s "plan against the stricter reading" clause mandates `2^39`, halving every published margin. The clause was never invoked.
4. **CATCH-4.** `b2_modp_giant_extras/statement.md:9`'s *"within ~2% of the counting threshold"* is wrong by ~500x — the true gap is **0.0044%**, and the `2.15e12` literal understates the true product `2.198926e12` by 2.23%. This *strengthens* its own conclusion that "pure counting can NEVER close it".
5. **CATCH-5.** The sliver is generated by `t*·L >= n`, not by (T*) — the two endpoints differ by 0.077 bits.

## HONEST RESIDUALS

1. **The `t`-naming collision is real and unresolved.** LEMMA 3's `t` is `|Lambda|`; `xr_radius_arithmetic`'s `t` is `A - k`, an agreement excess. The repo *adjudicates* them as one quantity and three lanes agree on `2^33`, but **no proof identifies them.** If they are distinct, the exclusion of `7e10` survives (it rests only on `n | q-1` plus the product relation), but the positive identification of `t` with `t*` does not.
2. `t = n/L` is a leading-order balance (exact to 0.0044% at prize-max), not a theorem; `t` is pinned to an interval, not a point.
3. `t*` is conditional on the open slot `xr_ledger_qpower` (`proof.md:31-32`).
4. `rate_half_cyclic_simple_pole_mca_floor/node.json:9` already refutes `8,592,912,739` as a *fixed safe point* (at excess `8,594,128,895`) — different object, but a maintainer should reconcile them.
5. **I did not re-derive the F2 tower on an admissible row.** What mystery 2's obligations become on a 2-rung tower is open and not attempted — this is the natural successor task.
6. **Process defect, self-reported.** I ran one bare `python3` (COMPUTE LAW violation) while extracting a JSON field; read-only, no result used anywhere, immediately re-run under `ramguard tiny`. Disclosed rather than suppressed.

**Recommendation for the discharge caveat:** it should not merely stay open — the "rungs 1-13" headline should be **withdrawn** and replaced by "rungs 1-10 (1-9 under the stricter window reading), at a row whose field is admissible", with CATCH-1 raised to maintainer level as a scope defect affecting every F2 statement at rungs >= 4.
