(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

Clean re-run: 54 checks PASS, 0 FAIL, exit 0. Nothing outside my dir touched, no REPORT.md, no commits.

---

# REPORT — the ternary unification, attacked (round 19, ADVERSARIAL)

**Verdict in one line: this is NOT a pun — but the strongest form of the claim is dead, and it dies for a reason the (ES) post-mortem never registered.**

Artifacts: `PREREG.md` (coordinator brief + my registrations P1–P13, §4 discloses the one utility that ran before them), `PROOFS.md`, `verify.py` / `verify.log` (54 checks, 0 failures, exit 0, fail-closed, under `tools/ramguard local`).

## The master object (needed for every verdict below)

All three instances are **exactly** the ternary part of a **negacyclic** `F_p`-code with an **all-odd, shift-0** window:

```
M(N,c,p) = { eps in {0,±1}^N : sum_j eps_j·theta^{(2i-1)j} = 0, i = 1..c },  ord(theta) = 2N
```

| inst | N | c | root order |
|---|---|---|---|
| I1 | `S = 2^40/e` | `R ≈ 2^32` | `2^{e_p}` |
| I2 | `L = 2^{41−v}` (=128 at v=34) | `delta_a` (=1 at prime rows) | `2L` |
| I3 | `h = 2^40` | `ceil((w−1)/2) = 2^33` | `n = 2h` |

In each case the root has order exactly **twice** the length, so `theta^N = −1` and the ambient algebra is `F_p[X]/(X^N+1)`.

## A1 — SHAPE-PUN TEST: the test is PASSED, and the test is too weak

A single parametrized statement does exist. **PROPOSITION FIB**: every obligation is `Phi(C;mu) = (the eps=0 term)·(1+delta)`, where `mu(eps)` counts the **binary preimages** of `eps`. I1 and I3 share the *same* `mu = 2^{N−wt}`; I2's is a binomial because the crossing lane fixes the weight. So the brief's registered A1 criterion is met — which is why I report it as **passed but insufficient**: a schema that classifies without implying is a taxonomy.

Two of the brief's four registered disanalogies are **refuted**:

- **(iii) is FALSE.** I1's ternary vectors are *not* native. `z1_ternary_mass/PROOFS.md:141` defines `F_s = {b in {0,1}^m : Ab = s}` and `:144-155` shows `eps = b − b'` with `2^{m−wt(eps)}` preimages. **I1's `2^{-wt}` weight IS the fibre size** — LEMMA AB clause 3's `2^{z(v)} = 2^{h−wt(v)}` is the same formula. Disanalogies (i) and (iii) are one phenomenon seen twice, and they cancel: I1's "mass" *is* a count, of binary pairs. The real split is **constant-weight (I2) vs full-cube (I1, I3)**.
- **(iv) is FALSE.** "Half-system vs theta-powers vs cyclic" is one structure in three notations.
- **(ii) absorbs** into the parameter `c` — but generates the phase transition below.

## A2 — REGIME AUDIT: the regimes ARE satisfiable (the anti-(ES) result)

**THEOREM SR.** Any prime with `v_2(p−1) = 41` and `log2 p in [255.9113, 256)` is admissible for **all three at once** — I1's `e=1` generating class, I2's recorded `e=1` prime row (`B* &gt;= 3`, provably outside DSA so the question is open), I3's official row. Existence is unconditional (Dirichlet); explicit exhibit, inside the prize-max sliver:

```
p = 108887375294690666722882806605166818982732176609682603652941949788724960165889
```

This is the **exact opposite** of (ES), whose four lanes were mutually unsatisfiable. **But there is no shared discharge** — see A4.

**CATCH-19-ADV-1 (against the brief):** the brief's `p ~ 2^39–2^64` for I1 is **unsourced**. The banked pins (`p &gt;= 2^39`; `e·log2 p &lt; 256`) admit `p` to `2^256` at `e = 1`; `2^64` is the *witness row's* prime at `e = 4`. The brief's premise for disjointness is wrong — in the direction favourable to the unification.

## A4 — STRUCTURAL DISANALOGY: found, proved, load-bearing

**THEOREM PT.** With `tau := c·log2 p / N`, Z-FLOOR is informative iff `tau &lt; 1`, and ternary vectors are expected present iff `tau &lt; log2 3 = 1.585`.

| inst | tau | Z-FLOOR (bits) | first moment (bits) | |
|---|---|---|---|---|
| I1 | **1** (forced by saturation) | −46.02 | **+0.585·2^38** | SUPERcritical |
| I2 | 2 | −128 | −53.125 | subcritical |
| I3 | 2 | −2^40 | −0.415·2^40 | subcritical |

I1's `tau = 1` is **forced**: the saturation pin `R/S = 1/log2 p` (THEOREM Z-NOGO) says exactly `c·log2 p = N`.

The coordinate is not numerology — it **reproduces four banked constants it was not fitted to**: the knife edge `−46.0249` / `+17.9751` with a step of `63.999999 = log2 p`; CATCH-Z1's `(3/2)^S = 2^{0.584963·2^38}`; LEMMA TC's `3^128 = 2^202.8752`; and DSA's `−53.1248` / orbit-corrected `−61.1248`.

**This is the pun's exact location.** I1 and {I2,I3} are on **opposite sides of the ternary counting threshold**, so no single monotone target specializes to both: at I1 the solution set is astronomically populated, so only a MASS bound can be true; at I2/I3 it is expected empty, so EMPTINESS is the target. **CATCH-Z1's re-pin of the F2 terminal to the mass form was forced by `sign(Tcrit)`, not by taste.**

On the length axis A4 finds **no** disanalogy: **LEMMA ZB** (proved, and CATCH-Z6's counts reproduced exactly: 0/0/0 at `2N=8,16,32`; 8, 8, 80 at `12, 20, 24`) — at 2-power `2N`, `deg Phi_{2N} = N` exactly, so parasitic relations cannot exist. All three live at 2-power `N`. Shared positive.

**COROLLARY PT-2 (new, campaign-relevant).** The crossing bracket's lower endpoint `w = 2^34` clears the ternary threshold `log2(3)·2^33` by only **0.336 bits**. One step below the bracket (`v = 33`, `L = 256`) gives `tau = 1` and `+149.75` bits — the deep stratum would be supercritical at the **recorded PRIME rows**, not just tower rows.

## A3 — TRANSFER MATRIX: dense in exact matches, empty in content

| instrument | I1 | I2 | I3 |
|---|---|---|---|
| Z-FLOOR | · | APPLIES, **vacuous** | APPLIES, **vacuous** |
| Z-1 / D1 | · | APPLIES, yield 3 | APPLIES, yield `w+1` |
| Z-NOGO | · | APPLIES (no-go) | APPLIES (no-go) |
| LEMMA ROT | APPLIES (`2N`) | · | APPLIES (`2h`) |
| DSA | FAILS by **2 bits** | · | FAILS by `2^40` bits |
| CS | FAILS (hyp) **+ provably vacuous** | binary parent | · |
| SP-COVER | FAILS by 9 bits | by 41 bits | by 3 bits |

- **DSA = Z-FLOOR's existence corollary + support control** (proved, verified on toys). Both are the same binary-difference collision; DSA's `p^{delta_a} &lt; 2^{L−2}` is `tau &lt; 1 − 2/N`. **Applied to I1, DSA fails by exactly 2 bits** — I1's 46-bit knife edge and I2's DSA boundary are the *same boundary*.
- **Z-FLOOR is hypothesis-free**, so it transfers verbatim and says **nothing** — its vacuity is precisely `tau &gt; 1`.
- **Z-1's yield is `2c+1`** — proportional to the parameter that differs by `2^32` across instances. On I3 it gives min ternary weight `&gt;= w+1`, a real factor-2 gain (and **absent from the repo**), but seven orders short of CC-sparsity.
- **CS fails on I1 twice**: banked hypotheses need a 0/1 indicator set and a char-0 ideal norm; and its ternary extension collapses at saturation to "excludes `U &lt; 4`" — verified `U &lt; 4.000000`, against Z-1's `2R+1 = 8,589,934,681`.
- **SP-COVER fails on all three for one shared reason** → **CATCH-19-ADV-2**: CATCH E-3 is banked as an (ES)-lane defect; it is not — the official gate `v_2(q−1) &gt;= 41` blind-spots SP-COVER in **all three** simultaneously.

## THE GRADED VERDICT

| grade | verdict |
|---|---|
| **OBJECT** | **SURVIVES (proved)** — negacyclic code, all-odd shift-0 window; sharper than round 18's phrasing |
| **REGIME** | **SURVIVES as satisfiability (proved)** — explicit shared row; **no shared discharge** |
| **METHOD** | **SURVIVES (proved) but INERT** — 4 verbatim transfers + 1 proved identification + 1 shared obstruction; every one provably vacuous or insufficient at its target's `tau` |
| **STATEMENT** | **KILLED as a theorem-unification**; survives only as a schema. `delta` is pinned by `sign(Tcrit)`, and CATCH-Z1 proves the two settings have opposite truth values at one object |

**Methodological finding.** A1 as registered is passable by a taxonomy, and A2 (regime disjointness) is not the only regime failure mode. I registered and applied a third gate — **CRITICALITY-COMPATIBILITY**: *do the instances lie in a common `tau`-interval where the instruments are non-vacuous?* Here they do not. I recommend adopting it alongside the (ES) regime test.

**Registered prediction P13 held** on all four grades (recorded before computing).

## Catches

1. **CATCH-19-ADV-1** — brief's I1 range `2^39–2^64` unsourced (§4).
2. **CATCH-19-ADV-2** — CATCH E-3 is a shared-row property, not an (ES)-lane defect.
3. **CATCH-19-ADV-3** — brief's disanalogy (iii) is false; the real split is constant-weight vs full-cube.
4. **CATCH-19-ADV-4** — **I4 is not an independent instance**: LEMMA TC's `3^L` is the *cardinality* of I2's ambient cube, and TC is a **crossing** lemma, not a band one (the brief labels it "band pricing"). Counting it inflates 3 instances to 4 — the same inflation that made "(ES) discharges all four consumers" attractive.
5. **CATCH-19-ADV-5 (process)** — **the round-19 quarantine is porous.** My subtraction sweep, searching only *outside* the quarantined dirs, recovered the sibling's headline results from `notes/pilots_20260802/CAMPAIGN_LEDGER.md:1815-1875`. Timeline, stated plainly: **all A1–A4 work and every verify.py number predate the sweep**, and I adjusted no conclusion to match. One upside — the ledger records the sibling reproducing `−46.0249 / +17.9751` to four decimals, which my run produced independently: a genuine blind convergence.

**Subtraction (no novelty claimed):** the `(3/2)^S` count and the `0.6309` saturation ratio are already banked (`z1_ternary_mass/PROOFS.md:487-489`, `f2_adm/PROOFS.md:518-521`, `f2_sl1_powersums/PROOFS.md:296-298`). Z-FLOOR≡DSA, the shared negacyclic frame, and the `2^{z(v)}`≡`2^{-wt}` identification are absent from the open surface but already banked by the quarantined sibling. **Genuinely absent from the whole repo:** the Z-1 transport to `C_odd`; COROLLARY PT-2; CATCH E-3 as a shared-row property.

**Self-corrections during the run (both caught by my own gates):** a `ceil` implemented with Decimal `//` (which truncates) gave a wrong `R` — caught by the fail-closed check against the banked `4,294,967,340`; and my first mixed-parity test **passed vacuously** (empty windows), a fail-open, fixed with an explicit non-vacuity guard at `N = 16`.

## Honest residuals

1. `Tcrit` is a **first moment** — heuristic for presence/absence, exactly as the banked `2^{-53.1}` re-pricing is labelled. Only the `tau &lt; 1` side is proved (pigeonhole).
2. Toys calibrate only; per `f2_z1_mass_knife_edge/statement.md:68-69` no toy is evidence about an official row. The structural results are algebraic identities, not extrapolations.
3. Z-1 → I3 gives `w+1` against length `2^40`: an improvement, not a route.
4. The shared-row exhibit is a Miller-Rabin probable prime; existence rests on Dirichlet.
5. The ternary extension of CS is unproved — used only to show CS is vacuous at I1, which holds either way.
6. **Untested cell:** I2's constant-weight fibration against a constant-weight Z-FLOOR. That is the one place a genuinely new instrument might live.
7. **Open conflict for adjudication:** ledger CATCH-19A says the ROT orbit constant "collapses to 2 for I1's mixed-parity windows at R &gt;= 2 — negacyclic iff all-odd". I verified the *mechanism* is right (mixed-parity windows are not negacyclic-closed; populated toys, 4796 and 52 codewords). But **I1's banked window is all-odd** (`z1_ternary_mass/PROOFS.md:87-94`), so on the banked reading the `2N` constant stands for I1. Coordinator should adjudicate which reading of I1's window is of record.

result: Ternary unification attacked and GRADED — object/regime/method unifications SURVIVE with proofs (incl. an explicit shared admissible 256-bit prime row, the anti-(ES) result), statement unification KILLED as a theorem-unification by a proved phase transition (I1 at tau=1 supercritical vs I2/I3 at tau=2 subcritical, reproducing four banked constants unfitted); 5 catches incl. a porous quarantine and three brief defects; 54/54 checks pass.
