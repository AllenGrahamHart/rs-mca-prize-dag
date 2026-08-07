# REPORT — l1_pma_diag (persisted verbatim by the coordinator from the session transcript, task a14bb594eddaf7f36, 2026-08-07)

Sanity check done: all six artifacts confined to the draft directory, no node/dag/tool touched, registrations timestamped before the first compute run, and the replication gate (43/33/2879/2857) passed by three independent code paths.

---

# MYSTERY 6 — `l1_mixed_petal_amplification`: first full diagnosis

**Headline: the N10 census cannot fire its own falsifier, and never could.** Its enumeration domain is an exactly-degree-6 polynomial in n, and its retained counts are the plain random-word law `BOX/q` to within 0.4%. The growth parameter of this object is **petal size `ell`, not n** — and the census only ever ran `ell = 2`. The mandatory adversarial construction **failed**, and I found the mechanism that kills it.

## D1 — The consumer contract, quoted and weakened

`critical/nodes/imgfib/statement.md:9`: *"For ALL received words U: #ImgFib_U(k+sigma) &lt;= n^B once sigma log2(q_D) &gt;= (1+eps) log2 C(n, k+sigma) and the quotient profile is budgeted."*

Quantified against the banked budget (`critical/nodes/petal_growth/conditional.md:16`, `node.json`): the allowance is `floor(n^6/C(n+6,6)) = 720` columns, the full-petal side saturates **one** at exponent ≤ 5.785 with 9.49 bits of slack that the node explicitly forbids spending. `B &gt; 6` is a *named open cell* (codegree conversion imgfib → list_safe). So the mixed bucket's real contract is: **fit inside 719 columns of `C(n+6,6)` at exponent 6.**

Weakenings actually available: `B` need not be uniform — *"B explicit per row"* (`imgfib/notes/l1_upstream_crosswalk_20260713.md:14`); and `sigma` may be taken at the reserve, not at 1.

**Finding D1-1 (P5, registered): the entire banked census mass sits below the corrected reserve at its own rows.** σ_min = 2/5/8 at (16,8,97)/(32,16,97)/(64,32,193) (ε=0; 3/5/8 at ε=0.05), while every retained contributor has σ ∈ {1,2}. At σ=1 the entropy condition fails by 6.9 / 22.5 / 53.0 bits. *Honest note: I registered "σ_min ≥ 3 at (16,8,97) even at ε=0" and it is 2 — P5 is falsified as written at that one cell. The conclusion it was testing survives at all three rows for both ε.*

## D2 — The obstruction made exact

Retraction semantics recovered: `c = d − ell`, `K_{I,d} = ker(pi_{&gt;d} R_{I,d})`, Lemma 13 `dim K &lt;= c+1`, Lemma 8 `#extras &lt;= q^{dim K}` — so growing `c` makes the banked bound `q^{c+1}`, super-polynomial. The census runs at `c ≈ k−4`, where that bound is `q^{k−3}` and the truth is `n^6/q`. The kernel route is exponentially loose exactly where the census lives.

**The exact closed form (P1, registered before computing, MATCHES all three banked candidate counts 5,096 / 386,640 / 27,152,032):** the band `d &gt;= 2(t−2)` forces ≤3 core points kept and ≤3 petal points omitted, giving a degree-6 polynomial with leading term `C(k,3)C(k−1,3) → n^6/2304`.

Generalized to any maximal-source chart (`|C| = k−1`, `t` petals of size `ell`, `b &lt; ell`), verified at 45 cells:

```
a &lt;= A_max = 2·ell + b − 2 =: Λ        om &lt;= om_max = 2·ell + b − 1 − σ
BOX = Θ(n^{2Λ}) = Θ(n^{4·ell + 2b − 4}),  and EMPTY once σ &gt; Λ
```

At `ell=2, b=1`: Λ=3, BOX = Θ(n⁶). **The registered super-polynomial falsifier is unfireable there for every received word — a counting fact, not an observation.**

**What a proof must control that the retracted induction did not:** not `c`, but `ell`. By the listing inequality `|C| + ell = k−1+ell &gt;= k+σ`, a contributor at threshold `k+σ` needs `ell &gt;= σ+1`. At the official rows σ_min = Θ(n/log n), so `ell = Ω(n/log n)`, `Λ &gt;= 2σ`, and BOX = `n^{Θ(n/log n)}`. The census's regime (`ell=2 ⟺ σ=1`) and the consumer's regime are separated by Θ(n/log n) in the one parameter that controls the object.

## D3 — Mechanism hunt and the mandatory adversarial attempt

**The census growth law is the random-word law.** `retained ≈ Σ_m N_{k+m}·q^{−m}(1−1/q)^{n−k−m}` predicts: 34.0 vs banked 43/33; 2,824.6 vs 2,879/2,857; **108,960.8 vs 109,391/108,600** — errors 26.6%, −2.8%, +1.9%, +1.1%, **+0.4%, −0.3%**. Sub-counts at agreement k+2 predicted 5.5/53.2 vs banked 8,7/62,53. The "doubling factor about 38" is predicted at **38.58** (banked 38.00/38.01) and is q-driven: box ratio 77.30 × (97/193). *P3 registered a 10% threshold: met at 5 of 6 cells; the (16,8,97) consec cell misses at 26.6%, a +1.55σ Poisson fluctuation on mean 34.*

**Reconciliation with today's concurrent audit** (annotated at `l1_mixed_petal_amplification/attack.md:23-26`, catch C-V4-1): the field correction is right and I derive it independently. But **"ABOVE the separately-disproved n^6 line" is a finite-size artifact.** The exact box polynomial's local doubling slope runs 6.50 → 6.27 → **6.14** → 6.07 → … → 6.0000, while `N/(n⁶/2304)` climbs 0.48 → 0.69 → 0.83 → … → 1.0000 **from below**. The quoted 6.14–6.21 is precisely this pre-asymptotic slope; the count never exceeds n⁶/2304 at any n.

**Adversarial construction — MANDATORY, attempted, FAILED.** The census fixes one word per cell; the legal family compatible with the layout is `c ∈ F_q^t`. I linearized retention (the (k+1)-point dual condition on μ_n reduces to `Σ_i c_i γ_i = 0`, machine-checked against the census) and searched:

- **n=16, EXHAUSTIVE over all 830,490 legal words:** mean 32.15, max **66** (2.05x). The banked consec word (43) sits at ~95th percentile; geom5 (33) is at the median.
- **n=32:** 12 random words → 2805 ± 46; best found = **3,273**, the minimal-degree word `deg U = k+1` (a consistent ≈16% structural excess at both scales, +11σ).
- Both pre-registered escape tests **do not fire**: MAX32/MAX16 = 49.6 vs threshold 261.8; MAX16 = 66 vs threshold 321.5.

**The mechanism that stops it, quantified.** Degenerate words *do* spike the linear-algebra filter enormously — at n=32 RANSAC found filter count **268,026** (69x the mean 3,885) — but exactness collapses it to **122**, a 22x *suppression* below the mean. Adversarial degeneracy makes codewords agree on **larger** sets, which promotes them out of the mixed floor-band class into a higher-agreement stratum. The bucket is self-limiting under exact-agreement semantics. This is the answer to "what bounds mixed-petal mass?" at fixed `ell`.

**The danger, measured.** At **fixed** n=24, sweeping only `ell`: 475 → **8,135** (17.1x) → **20,942** (44.1x) for ell = 2,3,4 — against 2,544x for *three doublings of n* at ell=2. One increment of `ell` buys more than a doubling of n.

## D4 — Cross-lane instrument matrix (applies / fails-because)

| Instrument | Status | Verdict vs this chart |
|---|---|---|
| `xr_pencil_forcing_t0` (T0-NR, P-SHARE) | PROVED (T0 open on `t&lt;=2e−3`, incl. prize shapes; T1/T2 REFUTED) | **FAILS** — gate H4 needs `pair &gt;= k+1`; petal agreement sets meet in `|C| = k−1`. Fails at the first hypothesis, every n |
| `xr_pencil_cascade` | PROVED | **FAILS** — needs a received *pair* (u,v) |
| **L-A** (pencil rigidity, e&gt;=2) | **REFUTED as stated**; L-A′ partial; V&gt;=5 evidence VOID | **FAILS** — same gate, and nothing unrepaired to transfer |
| **L-B** (escape-1 over-agreement) | PARTIAL; mechanism REFUTED; dropped, now ⇐ L-A | **FAILS** — no slope/pair; `esc_a` undefined here |
| **LEMMA R** (band form, `rank &lt;= 2m−1`) | PROVED/banked | **FAILS, near-vacuous** — bite needs every point multiplicity &gt;=2; petal points are private (multiplicity 1) |
| LEMMA R (L-A reduction form) | PROVED | **FAILS** — block-system-internal |
| **ternary object** `tern_master_threshold` | PROVED; single-theorem form KILLED by THEOREM PT | **PARTIAL ambient, WRONG word class** — half-system of μ_n and odd p match; but no `Λ`, so `g` and `τ` cannot be formed. Node's own vacuity column says every transfer is vacuous at its target's τ |
| `pma_arbitrary_petal_source_realizability` | PROVED | **EXACT MATCH** — its hypotheses are the census word *verbatim* (`U=0` on C∪B, `U=c_i L_C` on `T_i`). But it is a **route cut**: maximality does not force a common pencil |
| `l1_mixed_residual_intersection_pin` + 8 `l1_marked_common_pencil_*` | PROVED | **APPLY only inside a common-pencil chart** — which the line above proves is not free |

Net: **zero band-lane instruments transfer.** The vocabularies are disjoint (39 petal-bearing node ids, none `xr_*`), and the one exact-ambient hit is a no-go theorem.

## D5 — Re-pose draft

Full text at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/l1_pma_diag/REPOSE_DRAFT.md`. Clause (a) is **discharged by counting, unconditionally, for every received word** (empty when `σ &gt; 2ell+b−2`; else `&lt;= BOX`, which at ell=2 is 0.31 columns against a 720-column allowance). Clause (b) — `ell` growing — carries the entire content. Two falsifiers: (F-w1) a word exceeding `10·BOX(ell)/q`; (F-w2) any contributor at `σ &gt; 2ell+b−2`.

**Compute recommendation: drop `L1-N10-128`.** It costs ~74 CPU-hours / $4.1 to buy a fourth point on a curve whose closed form I now have exactly and which is provably capped at n⁶. Replace with `L1-N10-ELL`: fix n, sweep `ell = 2..6`. The ell=2,3,4 row at n=24 is already done locally at zero Modal cost.

## Honesty ledger

- Replication gate passed **before** anything downstream was reported; 43/33/2879/2857 reproduced by three independent code paths.
- Registered P5 **falsified as written** at one cell (σ_min = 2, not ≥3, at ε=0); P3 misses its 10% threshold at 1 of 6 cells (+1.55σ).
- MAX16 = 66 is **exhaustive**; MAX32 = 3,273 is a **search** — a lower bound on the true max, labelled as such.
- All census results are evidence, never proof. The BOX identities and the closed form are derivations, machine-checked.
- Blind to `notes/wave24_integration_20260727/PMA_*` throughout; quarantine clause passed to both subagents (one read `CAMPAIGN_LEDGER.md` only through line 2303; the marker is at 2304).

result: Mystery 6 diagnosed — the N10 census is structurally incapable of firing its falsifier (its domain is an exactly-degree-6 polynomial, closed form matching 5,096/386,640/27,152,032 exactly) and its counts are the random-word law BOX/q to 0.4%; the real growth parameter is petal size ell, not n (44x from ell=2→4 at fixed n=24, vs 2,544x for three doublings of n), the bucket is provably empty once σ &gt; 2·ell+b−2 so the official rows need ell = Ω(n/log n) where the box is n^{Θ(n/log n)}; the mandatory adversarial construction failed at reachable scale (exhaustive worst word over all 830,490 legal words at n=16 = 66 vs mean 32.1, both escape tests silent) with the blocking mechanism identified and quantified (exactness collapses a 268,026 filter spike to 122); zero band-lane instruments transfer; re-pose draft + falsifiers written and `L1-N10-128` recommended for replacement by an ell-sweep.
