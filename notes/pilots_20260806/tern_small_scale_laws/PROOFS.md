# TERNARY SMALL-SCALE LAWS — the proofs

Round 19, 2026-08-06, pilot `notes/pilots_20260806/tern_small_scale_laws/`.
Verifier `verify_ssl.py`, stages `ctrl l1 l2 l3 l4 ctl`,
**412 checks, 0 FAIL**, exit 0. Log: `VERIFY_LOG.txt`.
Registrations A–E appended to `PREREG.md` **before any computation**.

All arithmetic is exact integer / `F_p` arithmetic. Floats appear only in
printed diagnostics, never in a decision path. Every census below is
EXHAUSTIVE (meet-in-the-middle over the full `3^N` ternary cube); nothing
is sampled.

---

## §0. SUBTRACTION LEDGER (hard law 5) — declared before any claim

Five surfaces swept (`critical/`, `background/`, `notes/`, `archive/`,
`experiments/`+`formal/`), excluding the sibling `tern_route_b/`, which
was not read.

- **BANKED — the object, three times over.** `efloor_sparsity/PROOFS.md:88-96`
  (LEMMA AB), `crossing_low_w/PROOFS.md:330-332` (LEMMA ROT),
  `es_coprimality/PROOFS.md:143-151` (LEMMA STRAT),
  `f2_adm/PROOFS.md:232-235` (the GRS half-system). This pilot **measures**
  these objects; it does not re-derive them.
- **BANKED — the anomaly itself.** `efloor_sparsity/PROOFS.md:339-344`,
  verbatim:

  > **An anomaly worth recording (lead).** At `n = 32`, `p = 5`, `w = 2` the
  > code `C_odd` has `3^{16} = 4.3e7` ternary candidates mapping into
  > `5^8 = 3.9e5` syndromes, so a flat model predicts about **110** nonzero
  > ternary codewords. The exact count is **0**.

  §4 explains it. The anomaly is the efloor pilot's; the explanation is new.
- **BANKED — the first moment.** `z1_ternary_mass/PROOFS.md:53-54` quoting
  `f2_sl1_powersums/PROOFS.md:291`, verbatim:
  `E[ Z(L) ]  =  1 + (2^m - 1)(p^{m-d} - 1)/(p^m - 1)   ~   1 + 2^m / p^d .`
  §2.3 shows this is the *weighted* flat model and that the efloor pilot's
  `3^N/p^{rk}` is the *unweighted* one; the two differ by `(3/2)^N`.
- **BANKED — the composite-length contamination.** `z1_ternary_mass/REPORT.md:35`,
  verbatim: *"`2N=12` → 8 common vectors of min weight 3, `2N=20` → 8,
  `2N=24` → 80"*. §6 reproduces all three numbers by an independent route
  and then shows the disease has a second door (CATCH-19C).
- **NOT BANKED — self-orthogonality of the census code.** The five-surface
  sweep for `self-orthogonal|self-dual|weight divisib|divisible code`
  returns only the `rate_half_ca_hankel_a1_*` / `rate_half_band_closure`
  Hankel–Forney lane (a self-dual *frame* for the `A=1` exceptional
  algebra) — a different object in a different lane. No in-repo statement
  connects self-orthogonality to the ternary census.
- **STANDARD, NOT CLAIMED — the one-line mechanism.** "A self-orthogonal
  code over `F_p` has all `{0,±1}`-codeword weights divisible by `p`" is
  textbook coding theory (it is the standard proof that self-dual ternary
  codes have weights `= 0 mod 3`). **What is new here is not the
  mechanism** but (i) the identification that the round-18 anomaly cell
  *is* self-orthogonal, (ii) the exact combinatorial predicate on the
  defining set that decides which census cells are, and (iii) the
  quantitative ledger that closes the anomaly.

---

## §1. ONE framework, and the controls that license it

### 1.1 The framework

All three miniatures are censused by one routine (`ssl_lib.py`):

```text
CT(N, p, T) = { v in {0,+-1}^N : sum_{i<N} v_i omega^{s i} = 0, for all s in T }
```

`M = 2N`, `omega` a primitive `M`-th root of unity in characteristic `p`,
`T <= Z/M` closed under multiplication by `p`. The instance dictionary:

| instance | `CT` parameters | conditions |
|---|---|---|
| **I3**`(n,p,w)` (efloor / LEMMA AB) | `N = n/2`, `T = <p>`-closure of `{odd s in [1,w-1]}` | all-ODD `T` |
| **I2**`(L,p)` (crossing toy) | `N = L`, `T = <p>`-closure of `{1}` | all-ODD `T` |
| **I1**`(2N,p,R,a)` (z1 GRS-dual) | `N`, `T = {a,...,a+R-1}` | consecutive window, MIXED parity for `R>=2` |

`I1` forces `p = 1 mod 2N` structurally (`f2_adm/PROOFS.md:232-235`,
verbatim: *"an explicit `[2^{e_p-1}, 2^{e_p-1} - R, R+1]_p` GRS code whose
evaluation points are the half-system of `mu_{2^{e_p}} <= F_p^*`"*), so
`<p> = {1}` and `T` is the window itself.

### 1.2 The controls (registered E; a failure voids the pilot)

- **(C1) Replication.** The framework reproduces
  `efloor_sparsity/PROOFS.md:320-326` **exactly in all 16 cells**
  (`n=32`; `p in {3,5,7,17}`; `w in {2,4,6,8}`), including the four
  headline numbers `6560 / 0 / 16640 / 148224` at `w=2`.
- **(C2) Factor independence.** The ternary count is independent of which
  irreducible factor of `X^N+1` (which prime `P | p`) is chosen — verified
  over all factors in 16 cells. *Reason:* `sigma_u : v(X) -> v(X^u)` is a
  signed coordinate permutation of `F_p^N` preserving `{0,±1}` and carrying
  `C_{uT}` onto `C_T`.
- **(C3) Two disjoint code paths.** Brute-force enumeration over `3^N`
  agrees with the meet-in-the-middle census, weight by weight, in every
  `n=16` cell over `p in {3,5,7,11,13,17}`.
- **(C4)** Unreached cells are reported as unreached (§7).

---

## §2. (L1) THE MATCHED CENSUS

### 2.1 The count law in `p` at fixed shape

`I3` at `n=32` (`N=16`), `w=2`, every odd `p <= 61` (`VERIFY_LOG.txt`, L1.1).
Writing `rk` for the exact `F_p`-rank of the condition system and
`flat = (3^N-1)/p^{rk}`:

| `p` | 3 | 5 | 7 | 11 | 17 | 23 | 31 | 41 | 47 |
|---|---|---|---|---|---|---|---|---|---|
| `rk` | 8 | 8 | 4 | 8 | 2 | 4 | 2 | 4 | 2 |
| count | 6560 | **0** | 16640 | 0 | 148224 | 288 | 44544 | **0** | 17152 |
| count/flat | 1.000 | 0.000 | 0.928 | 0.00 | 0.995 | 1.872 | 0.994 | 0.000 | 0.880 |

The flat model is accurate to a few percent **exactly at the primes where
`rk` is small**, and fails completely at `p in {5,41}`. §4 shows the failure
is not noise: it is decided by a predicate on `T`.

### 2.2 Orbit structure at matched lengths

`VERIFY_LOG.txt`, L1.2. At every nonempty `I2`/`I3` cell over
`2N in {8,16,32}` the ternary kernel decomposes into orbits of size
**exactly `2N`** — never a proper divisor:

| `2N` | 8 | 16 | 16 | 16 | 32 | 32 | 32 |
|---|---|---|---|---|---|---|---|
| `p` | 3 | 3 | 7 | 17 | 3 | 7 | 17 |
| count | 8 | 80 | 128 | 384 | 6560 | 16640 | 148224 |
| orbits | 1 | 5 | 8 | 24 | 205 | 520 | 4632 |
| orbit sizes | 8 | 16 | 16 | 16 | 32 | 32 | 32 |

So LEMMA ROT's orbits (`crossing_low_w/PROOFS.md:330-332`) are **free** on
this object, and the over-dispersion factor is exactly `2N`, uniformly in
`p` and `N`. This is measured, not assumed.

### 2.3 Weighted mass vs unweighted count — the convention gap

With `Z = sum_v 2^{-wt(v)}` over the whole kernel (the z1 mass) and
`count` the unweighted number of nonzero ternary kernel vectors
(`VERIFY_LOG.txt`, L1.3):

| `N` | `p` | count | `Z-1` | `count/(Z-1)` | `(3/2)^N` |
|---|---|---|---|---|---|
| 8 | 7 | 128 | 4.50000 | 28.44 | 25.63 |
| 8 | 17 | 384 | 14.06250 | 27.31 | 25.63 |
| 16 | 7 | 16640 | 29.25000 | 568.89 | 656.84 |
| 16 | 17 | 148224 | 225.87891 | 656.21 | 656.84 |

**The ratio converges to `(3/2)^N`.** The two instances' own first-moment
conventions therefore differ by `(3/2)^N` — a factor of **657 at `N=16`**:

```text
E[count] = 3^N / p^{rk}      (efloor's flat model, unweighted)
E[Z] - 1 = 2^N / p^{rk}      (z1's first moment, f2_sl1_powersums:291, weighted)
```

Both are correct expectations of their own functionals; but a "flat model"
claim is meaningless until the convention is named. This is the L1
deliverable the mandate asked for, and it is directly relevant to §4:
at the anomaly cell `E[count] = 110.20` while `E[Z]-1 = 0.168`.

---

## §3. (L2) THE TRACKING TEST — the adversarial core

### 3.1 The dictionaries verify EXACTLY (D1, D2, D3)

- **D1 (the LEMMA STRAT dictionary).** For every `L in {4,8,16}` and
  `p in {3,5,7,11,17,97}`: the defining sets agree, the weight spectra
  agree, and — the strong form — the **sets of vectors are identical**.
  The coordinator's expectation is confirmed exactly: *I3's binding
  stratum IS an I2 instance*, coordinate for coordinate, with the identity
  dictionary `eps_j = v_j`, `theta = xi`, `L = n/2`.
- **D2.** Building `I1` from its OWN description (GRS parity check on the
  half-system evaluation points `x_e = omega^e`, never from the shared
  framework), `I1(2N,p,R=1,a=1)` has the same weight spectrum as `I2(N,p)`
  at every `N in {4,8,16}` and every `p = 1 mod 2N` tested.
- **D3 (the multiplicity dictionary).** Registered identity
  `Sct = 2^N (Z - 1)` **confirmed in every cell**, with the two sides
  computed by *disjoint code paths*: the left by the banked 0/1 subset
  census over `2^n` subsets of `Z/n` (`sp_lib.census_by_weight` minus
  `periodic_census_by_weight`), the right from my ternary weight
  distribution over `3^{n/2}` vectors. E.g. `n=32, p=17, w=2`:
  `14803200 = 14803200`.

  **So the efloor S-count and the z1 weighted mass are ONE functional.**
  This is the single most load-bearing positive result for the
  unification's *quantitative* content, and it is exact, not statistical.

### 3.2 CATCH-19A — the orbit constant is instance-dependent (P2 fires)

Registered P2 predicted the break; it happens. Measured closure of the
kernel under the negacyclic twisted rotation `R_neg`
(`crossing_low_w/PROOFS.md:330-332`) and the plain cyclic rotation
(`VERIFY_LOG.txt`, L2/P2, `N=8`):

| instance | `T` parity | count | closed `-v` | closed `R_neg` | closed `R_cyc` | orbit sizes |
|---|---|---|---|---|---|---|
| I2 | odd | 384 | yes | **yes** | no | **16** |
| I1 `R=1,a=1` | odd | 384 | yes | **yes** | no | **16** |
| I1 `R=1,a=0` | even | 1106 | yes | no | **yes** | 2,4,8,16 |
| I1 `R=2,a=1` | MIXED | 20 | yes | no | no | **2** |
| I1 `R=2,a=0` | MIXED | 64 | yes | no | no | **2** |
| I1 `R=3,a=0` | MIXED | 2 | yes | no | no | **2** |

Proved-and-measured rule (`ssl_lib.rot_neg`, `rot_cyc`): the kernel is
closed under `R_neg` **iff** every `s in T` is odd, and under `R_cyc`
**iff** every `s in T` is even. `I1`'s window `{a,...,a+R-1}` has mixed
parity for every `R >= 2`, so **neither survives**.

> **CATCH-19A.** LEMMA ROT's `2L`-orbit over-dispersion — the correction
> that `crossing_low_w/REPORT.md:104` uses to turn a naive prediction of
> 44.1 into 2.76 — **does not transport to I1 at `R >= 2`**. There the
> orbits have size 2, not `2N`. Any accident estimate that imports the
> `2L` factor across the dictionary over-corrects by a factor `N`.

This is not cosmetic. Using the I2/I3 constant `2N` in the onset
functional mislocates the I1 threshold: registered P6 found **2 cells with
`F < 0` but nonempty** and 0 with `F > 0` but empty; recomputing with the
instance-correct orbit constant gives **0 mispredictions of either kind**
(`VERIFY_LOG.txt`, L4.3).

### 3.3 CATCH-19B — the shift-0 layer is not an `F_p` layer at all

Registered P1's null was `count ~ (3^N-1)/p^{rk}` ("R independent
I2-layers"). Aggregated measured/predicted ratios by shift
(`VERIFY_LOG.txt`, L2/P1, 6 cells each):

| `R` | `a=0` | `a=1` | `a=2` |
|---|---|---|---|
| 1 | **17.384** | 1.004 | 1.126 |
| 2 | **15.246** | 0.648 | 0.790 |
| 3 | **10.767** | 0.703 | 1.063 |
| 4 | **34.466** | 0.000 | 0.686 |

At `a >= 1` the heuristic holds (in the large-count cells it is tight:
`N=16, p=97, R=1`: `443776` vs `443780.6`, ratio `1.000`; `R=2`: `4526`
vs `4575.1`, ratio `0.989`). At `a = 0` it fails by **one full factor of
`p`**, and the ratio grows *linearly in `p`* (11.71, 23.30, 31.03 at
`p = 97, 193, 257`) — the signature of a missing `1/p`.

The mechanism is exact. `omega^0 = 1`, so the `t = 0` condition is
`sum_e v_e = 0` in `F_p`; but `|sum_e v_e| <= N < p` at every `I1`
miniature (`p = 1 mod 2N` forces `p > 2N`), so it is the **integer**
condition `sum_e v_e = 0` — completely `p`-independent. Hence

```text
count(I1; N, p, R, a=0)  =  T(N) - 1          for R = 1, exactly,
count(I1; N, p, R, a=0)  ~  T(N) / p^{R-1}    for R >= 2,
```

where `T(N)` is the central trinomial coefficient. **Verified exactly**,
for every `p` tested, at `N = 4, 8, 16` (`VERIFY_LOG.txt`, L4.1):
`T(8)-1 = 1106` measured `1106`; `T(16)-1 = 5196626` measured `5196626`,
identically for `p = 97, 193, 257`. The corrected `R >= 2` law tracks to a
few percent (ratios `1.000, 0.999, 0.952, 1.002, 0.982, 1.093`).

> **CATCH-19B.** CATCH-Z6 (`z1_ternary_mass/REPORT.md:35`) banned composite
> `2N` because it carries `p`-independent parasitic relations. The
> 2-power rule does **not** close that door: at **2-power** length, shift
> `a = 0` reintroduces a `p`-independent *integer* relation, and the z1
> calibration grid explicitly ranges over `shifts a in {0,1,2,3}`
> (`z1_ternary_mass/PROOFS.md:407-408`). One quarter of that grid carries a
> structural layer that no `p`-accident model prices.

### 3.4 Verdict on the tracking test

**The unification is NOT refuted, and its exact content is confirmed;
its heuristic content is refuted in two identified places.**

- Confirmed exactly (D1, D2, D3): same object, same vectors, same
  functional up to the stated `2^N` and `(3/2)^N` conversions.
- Refuted as stated, with the exact deviation law in each case:
  the LEMMA ROT orbit constant (CATCH-19A, deviation factor `N`) and the
  independent-layers heuristic at shift 0 (CATCH-19B, deviation factor
  `p * T(N)/3^N`).

Neither deviation is absorbed by a free parameter: both were predicted
before measurement (P2 as registered; P1's `a=0` failure was *not*
predicted and is reported as a miss of my own null, with its mechanism).

---

## §4. (L3) THE ANOMALY — explained, and its transport measured

### 4.1 LEMMA TWT

> **LEMMA TWT (ternary weight theorem).** Let `C <= F_p^N` be
> self-orthogonal (`C <= C^perp`), `p` odd. Then every `v in C` with all
> coordinates in `{0,±1}` satisfies `p | wt(v)`.

**Proof.** `v in C <= C^perp` gives `<v,v> = 0` in `F_p`. With
`v_i in {0,±1}` we have `v_i^2 in {0,1}` with `v_i^2 = 1` exactly on the
support, so `<v,v> = sum_i v_i^2 = wt(v)` in `F_p`. Hence `p | wt(v)`. ∎

(The mechanism is standard coding theory — see §0. Its *relevance here* is
the new part.)

### 4.2 Which census cells are self-orthogonal — the exact predicate

> **SELF-ORTH`(N,p,T)`:** `T u (-T)` contains every odd residue mod `2N`.

For all-odd `T` the code is negacyclic and its dual has defining set
`(Z/2N)^* \ (-T)`, so SELF-ORTH is exactly `C <= C^perp`. **Verified
directly, without using that theory**, by computing a basis of the null
space and testing every pairwise inner product: the registered predicate
and the direct test **agree in every cell** over
`n in {8,16,32}`, `p in {3,5,7,11,13,17,19,23}`, `w in {2,4,6,8}`
(`VERIFY_LOG.txt`, L3/P3a).

### 4.3 LEMMA TWT holds, and the predicate is sharp

`VERIFY_LOG.txt`, L3/P3b–P3c:

- **83 SELF-ORTH cells tested, 0 violations.** Every nonzero ternary
  codeword has `p | wt`.
- **13 non-SELF-ORTH cells; in none of them are the weights
  `p`-restricted** (P3c). The predicate is sharp, not a coincidence.

Measured weight spectra at `n=32` make the mechanism visible:

| `p` | `w` | SELF-ORTH | count | weights present |
|---|---|---|---|---|
| 3 | 2 | yes | 6560 | 3, 6, 9, 12 |
| 7 | 4 | yes | 288 | **7, 14** |
| 7 | 2 | no | 16640 | 3,4,5,6,... |
| 17 | 4 | no | 288 | 6, 12 |
| 23 | 2 | no | 288 | 5, 10 |

### 4.4 The anomaly ledger

At `n = 32`, `p = 5`, `w = 2`: `T = <5> = {s = 1 mod 4}`, `-T = {s = 3 mod 4}`,
so SELF-ORTH holds and `5 | wt` forces `wt in {5,10,15}`.

```text
ternary population                     3^16                 = 43 046 721
syndrome space                         5^8                  =    390 625
FLAT model (the banked "~110")                              =     110.20
admissible after LEMMA TWT             C(16,5)2^5+C(16,10)2^10+C(16,15)2^15
                                                            =  8 864 256
corrected expected codewords           8864256 / 5^8        =      22.69
per LEMMA ROT orbit of size 2N = 32                         =  0.709 orbits
Poisson P(0 orbits) = exp(-0.709)                           =       0.49
MEASURED                                                    =          0
```

**The anomaly is fully accounted for.** The `155x` suppression factors as
`4.9x` (LEMMA TWT, an exact arithmetic obstruction) `x 32` (LEMMA ROT
orbit quantization, measured free in §2.2). What remains is an expected
**0.709 orbits**, for which **0 is the modal outcome**. There is no
residual anomaly to explain.

Two corollaries worth recording:

- The mandate's candidate list (SP-TERNARY / Gauss-sum exactness / orbit
  over-dispersion) was **incomplete**: orbit over-dispersion alone leaves
  a `3.4`-orbit expectation (`P(0) = 3%`); the missing `4.9x` is LEMMA TWT,
  a mechanism not on the list.
- In the *weighted* convention the cell was never anomalous at all:
  `E[Z]-1 = 2^16/5^8 = 0.168` (§2.3). The "1–2 orders of magnitude" felt
  by the round-18 pilot is partly the `(3/2)^N` convention gap.

### 4.5 P4 — transport: the mechanism is INSTANCE-LOCAL

SELF-ORTH is a property of `(2N, p, T)` alone, hence in principle shared.
But it needs `|T| >= N/2`, and `I1` structurally forces `p = 1 mod 2N`,
so `<p> = {1}` and `|T| = R`. **Measured: SELF-ORTH is false at every `I1`
miniature with `R <= 4`, `N >= 8`** (`VERIFY_LOG.txt`, L3/P4).

> **CATCH-19D (the disanalogy datum).** The anomaly's mechanism lives on
> cells where `<p>` has large index — i.e. **non-split** primes. `I3`'s
> census scans all `p`; `I1` and `I2` sample only `p = 1 mod 2N`
> (structurally for `I1`; by grid choice for `I2` —
> `crossing_low_w/PROOFS.md:339-345` uses `p in {193,257,449,577,641}` at
> `2L=16`, all `= 1 mod 2L`). **The three instances share the object but
> sample disjoint strata of its parameter space.** A law measured on an
> `I1`/`I2` grid does not transfer to an `I3` grid without controlling for
> `ord_{2N}(p)`. This is the honest answer to L3's transport question:
> **instance-local, not shared** — the weaker of the two outcomes the
> mandate anticipated.

---

## §5. (L4) THE SCALING VERDICT

No prize-row claims are made. What follows is the small-scale consistency
verdict with the correction terms priced in bits.

Main term (all instances): `N log2 3`. The three measured corrections:

| correction | size (bits) | at `N=16` | at `N=2^38` | survives to scale? |
|---|---|---|---|---|
| ORBIT (LEMMA ROT) | `log2(2N)` | 5.00 | 39.00 | yes, but the **I1-vs-I2/I3 GAP** is `log2 N` |
| LEMMA TWT | `~log2 p`, **only if** `|T| >= N/2` | 2.3 | — | **no** (hypothesis dies) |
| SHIFT-0 integer layer | `0.5 log2 N + 1.20` instead of `log2 p` | 3.03 | 20.03 | **yes** |

- **ORBIT.** The gap between the instances is `log2(N)`: 4 bits at `N=16`,
  **38 bits** at the official `I1` row `N = 2^38`. It is an *absolute*
  offset against a main term of `4.36e11` bits, so it matters only when a
  balance is struck within `log2 N` bits of zero — which is precisely the
  regime the accident-zone functionals of
  `crossing_low_w/PROOFS.md:193-196` operate in.
- **LEMMA TWT.** At the official `I1` row `R ~ S/log2 p ~ 2^38/64 = 2^32`
  while `N/2 = 2^37`: SELF-ORTH fails by five orders of magnitude. The
  suppression that closes the round-18 anomaly is a **small-scale-only**
  effect for `I1`. Small-scale ternary-suppression evidence therefore does
  **not** transport to the prize rows, and must not be cited as if it did.
- **SHIFT-0.** `T(N)/3^N ~ sqrt(3/(4 pi N))`, so the shift-0 layer is worth
  `0.5 log2 N + 1.20` bits where the heuristic charges `log2 p`. At
  `N = 2^38, p ~ 2^64` that is **20.0 vs 64 bits**: a `2^44` EXCESS of
  accidents over the independent-layers heuristic, and it does **not**
  decay with `N`. Of the three, this is the only correction that both
  survives to the prize scale and moves in the *dangerous* direction
  (more accidents than predicted).

**Verdict.** The instances do not leave the shared regime at the same
rate. The exact structure (D1/D2/D3) is scale-free and holds identically
everywhere. The heuristic corrections are not: TWT dies for `I1`, the
orbit constant splits into two instance-dependent values whose gap grows
as `log2 N`, and the shift-0 layer persists. Small-scale agreement of the
*counts* is therefore weak evidence about the prize rows; small-scale
agreement of the *dictionaries* is strong and scale-free.

---

## §6. The labelled composite negative control (P5)

One deliberately composite cell block, as registered (`VERIFY_LOG.txt`,
CTL). Common ternary relations across all admissible `p = 1 mod 2N`:

| `2N` | type | primes | `p`-independent relations | min weight |
|---|---|---|---|---|
| 12 | COMPOSITE | 13,37,61,73,97 | **8** | 3 |
| 20 | COMPOSITE | 41,61,101,181,241 | **8** | 5 |
| 24 | COMPOSITE | 73,97,193,241,313 | **80** | 3 |
| 16 | 2-power | 17,97,113,193,241 | **0** | — |
| 32 | 2-power | 97,193,257,353,449 | **0** | — |

All three composite numbers reproduce `z1_ternary_mass/REPORT.md:35`
verbatim (*"`2N=12` → 8 common vectors of min weight 3, `2N=20` → 8,
`2N=24` → 80"*) **by an independent route**, and both 2-power rows are
clean. CATCH-Z6 is confirmed in both directions. These cells are excluded
from every law in §2–§5. Note CATCH-19B (§3.3): the 2-power rule is
necessary but **not sufficient** — shift 0 is the second door.

---

## §7. Honest residuals, misses and unreached cells

1. **My own registered null P1 MISSED at `a = 0`**, 5 of 5 shift-0 rows.
   I registered "R independent layers" without noticing that `omega^0 = 1`
   makes the first layer an integer condition. Reported as CATCH-19B with
   the exact corrected law, not buried; the null as registered stands
   refuted at `a=0` and confirmed at `a >= 1`.
2. **UNREACHED: `2N = 64` (`N = 32`).** Registered in grid G-A; the full
   `3^32` ternary census exceeds the COMPUTE LAW in the pure-Python code
   path. Reported as unreached, never estimated. The scaling ladder rests
   on `N = 4, 8, 16` (three points) plus exact combinatorial identities.
3. **The `a >= 1` ratios are noisy in the small-count cells** (means
   0.648–1.126 over 6 cells each). Where counts are large enough to
   measure they are tight (0.989–1.000). I do **not** claim a systematic
   deficit at `a >= 1`; the honest statement is "consistent with 1 at the
   available precision".
4. **Over-representation at `p=7, w=4` is unexplained.** 288 ternary
   codewords against a TWT-corrected flat prediction of 0.595 — a 484x
   *excess* (9 orbits where 0.019 are expected). LEMMA TWT explains the
   weights (`7, 14`) but not the multiplicity. There is a second,
   opposite-signed structural mechanism here that I have not identified.
   Recorded as an open lead, not explained away.
5. **`p = 3` is degenerate for every flat model.** `F_3 = {0,±1}`, so the
   ternary count is exactly `p^{N-rk} - 1` and no accident model applies.
   Excluded from the ratio laws (LEMMA TWT still holds there, and is then
   the classical divisibility theorem for self-orthogonal ternary codes).
6. **LEMMA TWT's hypothesis is verified per cell, not proved uniformly.**
   Like SP-TERNARY (`efloor_sparsity/PROOFS.md:335-337`: *"a certified
   criterion, verified instance by instance"*), SELF-ORTH is checked
   cell-by-cell; I make no `n`-uniform claim.
7. **No prize-row claim is made anywhere in this pilot**, per mandate.

---

## §8. Catches minted

- **CATCH-19A** — LEMMA ROT's `2L` orbit constant does not transport to
  I1 at `R >= 2` (orbits of size 2, not `2N`); the onset threshold is
  mislocated by `log2 N` bits if imported across the dictionary.
- **CATCH-19B** — shift `a = 0` reintroduces a `p`-independent INTEGER
  relation at 2-power length; `count = T(N) - 1` exactly at `R = 1`. The
  CATCH-Z6 2-power rule does not close this door, and the z1 calibration
  grid ranges over `a = 0`.
- **CATCH-19C** — (§2.3) the efloor and z1 flat models differ by
  `(3/2)^N` (657 at `N=16`); "flat model" claims are not comparable
  across the two pilots until the convention is named.
- **CATCH-19D** — the instances share the object but sample disjoint
  strata (`ord_{2N}(p)`): I1 is structurally confined to split primes, so
  the anomaly mechanism is instance-local.
- **LEMMA TWT** + the SELF-ORTH predicate — the round-18 anomaly's exact
  mechanism (mechanism standard, application new).
