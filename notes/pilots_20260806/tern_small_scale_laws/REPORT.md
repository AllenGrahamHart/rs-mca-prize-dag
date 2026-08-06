(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

Sanity check complete: verifier exits 0 with 412 checks from a clean re-run; every file I wrote is inside my pilot directory (the `dag.json`/`orbit/` files predate my session at 20:03–20:04); no `__pycache__` leaked into the banked dirs; PREREG registrations were appended before any computation; no REPORT.md written.

# TERNARY SMALL-SCALE LAWS — round 19, ADVERSARIAL-EMPIRICAL

**Verifier:** `notes/pilots_20260806/tern_small_scale_laws/verify_ssl.py`, stages `ctrl l1 l2 l3 l4 ctl` — **412 checks, 0 FAIL, exit 0**. Log: `.../VERIFY_LOG.txt`. Proofs: `.../PROOFS.md`. Framework: `.../ssl_lib.py`. Registrations A–E appended to `.../PREREG.md` **before any computation**. Every census is exhaustive (meet-in-the-middle over the full `3^N` ternary cube); nothing is sampled; all arithmetic exact.

## Headline

**The unification's exact content is confirmed; its heuristic content is refuted in two identified places, with the deviation law given in each case. The round-18 anomaly is fully explained — and the explanation shows the mechanism is instance-local, not shared.**

## Licensing controls (a failure would have voided the pilot)

- **C1 replication:** my framework reproduces `efloor_sparsity/PROOFS.md:320-326` **exactly in all 16 cells**, including `6560 / 0 / 16640 / 148224`.
- **C2 factor independence:** count independent of which prime `P | p` is chosen, all factors, 16 cells.
- **C3 disjoint code paths:** brute force over `3^N` agrees with MITM weight-by-weight in every `n=16` cell.
- **Independent second replication:** the composite control reproduces CATCH-Z6's three banked numbers verbatim (`2N=12` → 8 vectors of min weight 3; `2N=20` → 8; `2N=24` → 80; 2-power rows clean) by a different route than z1's.

## L1 — THE MATCHED CENSUS: verdict DELIVERED

One framework `CT(N,p,T) = {v ∈ {0,±1}^N : Σ v_i ω^{si} = 0 ∀s∈T}` covers all three shapes (I3: `T` = ⟨p⟩-closure of odd window; I2: closure of {1}; I1: the window `{a..a+R-1}`).

- **Count law:** flat model accurate to a few percent exactly where the rank is small; total failure at `p ∈ {5,41}` (n=32,w=2). Not noise — decided by a predicate (L3).
- **Orbit structure:** at every nonempty I2/I3 cell over `2N ∈ {8,16,32}`, orbits have size **exactly `2N`**, never a proper divisor. LEMMA ROT's orbits are **free**; over-dispersion is exactly `2N`, uniformly in `p` and `N`.
- **Weighted-vs-unweighted ratio (CATCH-19C):** `count/(Z−1) → (3/2)^N` — **657 at N=16**. The efloor flat model (`3^N/p^rk`, unweighted) and the z1 first moment (`2^N/p^rk`, weighted, `f2_sl1_powersums/PROOFS.md:291`) are both correct for their own functional but differ by `(3/2)^N`. "Flat model" claims are not comparable across the two pilots until the convention is named.

## L2 — THE TRACKING TEST: unification NOT refuted; two heuristics refuted

**Dictionaries verify exactly.**
- **D1 (the LEMMA STRAT dictionary):** confirmed in its strongest form — I2's relation set and I3's binding stratum are **the same set of vectors**, coordinate for coordinate, at every matched cell. The coordinator's expectation is exactly right.
- **D2:** I1 built from its *own* description (GRS half-system parity check on `x_e = ω^e`) has the same spectrum as I2 at `R=1, a=1`.
- **D3 (new, load-bearing):** registered identity `Sct = 2^N(Z−1)` confirmed in every cell, sides computed by **disjoint code paths** (banked 0/1 subset census over `2^n` subsets vs my ternary census over `3^{n/2}` vectors). **The efloor S-count and the z1 weighted mass are one functional** — exact, not statistical.

**CATCH-19A (registered prediction P2 fires) — the orbit constant is instance-dependent.** The kernel is closed under the negacyclic rotation **iff** `T` is all-odd, under the cyclic rotation **iff** `T` is all-even. I1's window has mixed parity for every `R ≥ 2`, so **neither survives**: measured orbit sizes are **2, not `2N`**. LEMMA ROT's `2L` over-dispersion factor — the one that turns 44.1 into 2.76 at `crossing_low_w/REPORT.md:104` — **does not transport to I1 at `R ≥ 2`**. Consequence measured: the onset functional using the I2/I3 constant `2N` gives 2 threshold mispredictions; with the instance-correct constant, **0**.

**CATCH-19B (my own registered null P1 MISSED) — shift 0 is not an `F_p` layer.** At `a=0`, `ω^0 = 1`, so the `t=0` condition is `Σv_e = 0` in `F_p`; but `|Σv_e| ≤ N &lt; p` at every I1 miniature, so it is the **integer** condition — `p`-independent. Measured ratios to the independent-layers null: **17.4, 15.2, 10.8, 34.5** at `a=0` versus **≈1** at `a≥1`, with the excess growing *linearly in p* (11.71, 23.30, 31.03 at p=97,193,257) — the signature of a missing `1/p`. Exact corrected law, verified identically for every `p` at `N=4,8,16`:

```
count(a=0, R=1) = T(N) − 1   exactly   (T = central trinomial; T(16)−1 = 5196626 measured 5196626)
count(a=0, R)  ≈ T(N)/p^{R−1}          (ratios 1.000, 0.999, 0.952, 1.002, 0.982, 1.093)
```

CATCH-Z6 banned composite `2N` for carrying `p`-independent relations; **the 2-power rule does not close that door** — shift 0 reintroduces one at 2-power length, and z1's calibration grid ranges over `a ∈ {0,1,2,3}` (`z1_ternary_mass/PROOFS.md:407-408`).

Neither deviation is absorbed post hoc: P2 was registered before measuring; P1's failure is reported as a miss of my own null with its exact mechanism.

## L3 — THE ANOMALY: explained, mechanism new, transport INSTANCE-LOCAL

**LEMMA TWT.** *If `C ≤ F_p^N` is self-orthogonal and `v ∈ C` has coordinates in `{0,±1}`, then `p | wt(v)`.* Proof, one line: `0 = ⟨v,v⟩ = Σv_i² = wt(v)` in `F_p`.

**The exact predicate for which cells qualify:** `SELF-ORTH(N,p,T)` ⟺ `T ∪ (−T)` contains every odd residue mod `2N`. Verified **directly** (null-space basis, all pairwise inner products) against the registered combinatorial predicate — **agreement in every cell** over `n∈{8,16,32}`, `p∈{3,5,7,11,13,17,19,23}`, `w∈{2,4,6,8}`.

**LEMMA TWT holds and the predicate is sharp:** 83 SELF-ORTH cells, **0 violations**; 13 non-SELF-ORTH cells, **none** `p`-weight-restricted. (Visible in the spectra: `p=7,w=4` → weights exactly {7,14}; `p=3` → {3,6,9,12}.)

**The anomaly ledger at n=32, p=5, w=2** (SELF-ORTH holds; `5|wt` forces `wt ∈ {5,10,15}`):

```
flat model (the banked "~110")                        110.20
after LEMMA TWT      8 864 256 / 5^8            =      22.69
per LEMMA ROT orbit of size 32                  =  0.709 orbits
Poisson P(0 orbits) = exp(−0.709)               =       0.49
MEASURED                                        =          0
```

**Fully accounted for.** The 155× suppression = **4.9× (LEMMA TWT, exact arithmetic obstruction) × 32 (orbit quantization)**. No residual anomaly. Note the mandate's candidate list was incomplete: orbit over-dispersion alone leaves 3.4 orbits expected (`P(0)=3%`); the missing 4.9× is LEMMA TWT, which was not on the list. Also, in the *weighted* convention the cell was never anomalous: `E[Z]−1 = 2^16/5^8 = 0.168`.

**CATCH-19D — transport is INSTANCE-LOCAL (the weaker outcome).** SELF-ORTH needs `|T| ≥ N/2`; I1 structurally forces `p ≡ 1 mod 2N` (`f2_adm/PROOFS.md:232-235`), so `⟨p⟩={1}`, `|T|=R`. Measured: **SELF-ORTH false at every I1 miniature with `R ≤ 4`, `N ≥ 8`**. The mechanism lives on **non-split** primes; I3's census scans all `p`, while I1 (structurally) and I2 (by grid choice — all its primes are `≡1 mod 2L`) sample only split primes. **The three instances share the object but sample disjoint strata of its parameter space.** A law measured on an I1/I2 grid does not transfer to an I3 grid without controlling for `ord_{2N}(p)`.

## L4 — THE SCALING VERDICT (no prize-row claims)

| correction | size (bits) | N=16 | N=2^38 | survives? |
|---|---|---|---|---|
| ORBIT (LEMMA ROT) | `log2(2N)`; **I1-vs-I2/I3 gap = `log2 N`** | 5.00 | 39.00 | yes (gap grows) |
| LEMMA TWT | `~log2 p`, only if `|T| ≥ N/2` | 2.3 | — | **no** |
| SHIFT-0 integer layer | `0.5·log2 N + 1.20` instead of `log2 p` | 3.03 | 20.03 | **yes** |

- **TWT dies at scale for I1:** at the official row `R ~ 2^32` vs `N/2 = 2^37` — fails by five orders of magnitude. **Small-scale ternary-suppression evidence must not be cited as if it transported to the prize rows.**
- **The orbit gap grows as `log2 N`:** 4 bits at N=16, **38 bits** at `N=2^38`. Absolute, not relative — it bites precisely in the near-balance regime the accident-zone functionals of `crossing_low_w/PROOFS.md:193-196` operate in.
- **Shift-0 persists and points the dangerous way:** worth 20.0 bits where the heuristic charges 64 — a **2^44 excess** of accidents over the independent-layers heuristic at the official I1 row, not decaying with `N`.

**Verdict: the instances do NOT leave the shared regime at the same rate.** The exact structure (D1/D2/D3) is scale-free and holds identically everywhere; the heuristic corrections are instance-dependent and diverge. Small-scale agreement of the *counts* is weak evidence about the prize rows; small-scale agreement of the *dictionaries* is strong and scale-free.

## Honest residuals

1. **My registered null P1 missed at `a=0`**, 5 of 5 shift-0 rows — reported as CATCH-19B, not buried.
2. **UNREACHED: `2N=64` (N=32)** — the full `3^32` census exceeds the compute law in the pure-Python path. Reported unreached, never estimated; the ladder rests on N=4,8,16 plus exact identities.
3. **Unexplained over-representation at `p=7, w=4`:** 288 codewords vs a TWT-corrected prediction of 0.595 — a **484× excess** (9 orbits where 0.019 expected). TWT explains the weights {7,14} but not the multiplicity. A second, opposite-signed mechanism exists that I have not identified. Open lead.
4. **`a ≥ 1` ratios are noisy in small-count cells** (0.648–1.126); tight where measurable (0.989–1.000). I claim only "consistent with 1 at the available precision".
5. **`p=3` is degenerate** for any flat model (`F_3 = {0,±1}`); excluded from ratio laws.
6. **LEMMA TWT's hypothesis is certified per cell, not `n`-uniform** — same honest scope as SP-TERNARY (`efloor_sparsity/PROOFS.md:335-337`).
7. The one-line TWT mechanism is **standard coding theory**; new here are its identification at the anomaly cell, the exact predicate, and the ledger. Five-surface subtraction sweep found no in-repo prior (only the unrelated `rate_half` Hankel–Forney self-dual *frame*).

**Catches minted:** CATCH-19A (orbit constant does not transport), CATCH-19B (shift-0 integer layer; CATCH-Z6's second door), CATCH-19C (the `(3/2)^N` convention gap), CATCH-19D (disjoint prime strata), plus LEMMA TWT + the SELF-ORTH predicate.

result: Ternary unification survives the empirical stress test — dictionaries D1/D2/D3 verify exactly (I3's binding stratum IS an I2 instance, vector for vector; efloor's S-count and z1's mass are one functional, `Sct = 2^N(Z−1)`, via disjoint code paths) — but two heuristics are quantitatively refuted with exact deviation laws (CATCH-19A: LEMMA ROT's `2L` orbit constant collapses from `2N` to 2 for I1 at R≥2; CATCH-19B: shift a=0 is a p-independent INTEGER layer, count `= T(N)−1` exactly, not `3^N/p`), and the round-18 n=32,p=5,w=2 anomaly is fully closed by new LEMMA TWT (self-orthogonality + ternary alphabet ⟹ p | weight; 83 cells, 0 violations, predicate sharp) × orbit quantization = 155×, leaving 0.709 expected orbits where 0 is modal — with the mechanism proved INSTANCE-LOCAL to non-split primes, so the three instances share the object but sample disjoint strata; 412 checks, 0 fail.
