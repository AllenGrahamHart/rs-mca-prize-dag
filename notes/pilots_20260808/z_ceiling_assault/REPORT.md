# REPORT — z_ceiling_assault (persisted verbatim by the coordinator from the session transcript, task a0bc32d723fc69262, 2026-08-08)

All work is confined to my pilot directory. Writing the report.

**ROUND-24 PILOT REPORT — CONJECTURE Z-CEILING: THE ASSAULT**

Registrations were appended to `notes/pilots_20260808/z_ceiling_assault/PREREG.md` (sections R0–R7, lines 87–297) **before any computation**. Every claim below is from `zcore.py` / `escape.py` / `sweep.py` / `deep.py` / `rc.py` / `probe.py` / `addendum.py` / `law.py` / `sharpen.py` in that directory, outputs saved as `*.txt`, `SWEEP.tsv`, `DEEP16.tsv`. All runs via `tools/ramguard local -- python3`, stdlib only. No writes outside the pilot dir; no status flip; no closure claim.

## 1. VERDICT

**Z-CEILING SURVIVES the assault — but its constant of record is wrong and must be raised from 1.2610 to ≥ 1.7681.** No admissible 2-power cell exceeded 2 in **59,203 exact-rational cell evaluations**. The registered falsifier was not tripped.

## 2. THE RE-AIMING (a forced correction of the brief's direction D1(a))

The brief's D1(a) asked me to follow the σ→−∞ family lines. Registered in R1 *before computing*: with `H = (2^N−1)/p^κ`,

    CRATIO = (1 + EXCESS·H)/(1+H)   ⟹   CRATIO &gt; 2 ⟺ EXCESS &gt; 2 AND H &gt; 1/(EXCESS−2)

So σ→−∞ is **provably the safe direction** for the ratio form. Registered prediction P1a: `CRATIO(16,2,3137) = 1.0089 ± 0.0010`; measured **1.008906**. The known EXCESS counterexample (EXCESS 2.3463) sits at σ = −7.23 and is no threat at all. The danger is σ ≈ 0. That re-aiming is what produced the new record.

## 3. HEADLINE: A NEW RECORD ON THE ADMISSIBLE 2-POWER GRID

`background/nodes/f2_z1_mass_knife_edge/statement.md:190` — "the ratio form survives 7,000+ cells at C &lt;= 1.2610".

**That constant is superseded.** Record cell: family I2/M4 (RSET, Λ={1}), **N = 16, κ = 1, p = 161761**:

- `TMASS = 159/64` **exactly**, `HEUR = 227296/161761`, **CRATIO = 1.7680688810**
- `SIGMA = −1.3035`, `EXCESS = 3.6639` (a *second* EXCESS&gt;2 cell, and unlike the banked one this one bites the ratio form), `ZFRATIO = 6.132`
- weight enumerator `0:1, 5:32, 8:96, 10:64, 11:96`, `UMIN = 5`, `|ker∩T| = 289`

Verified by **three independent algorithms** (my exact MITM DP; the round-23 `weight_enum_kernel` executed verbatim out of `cw.py`; a floating character sum) — agreement to 6.5e-14 (`sharpen.txt`, E7 block, 21/0).

**Consequence for the node's own arithmetic** (`statement.md:190-193`): I reproduce its chain exactly (17.98 + log2 1.2610 = 18.31; 22.75 − 18.31 = 4.44). With C = 1.7681, log2 C = 0.8222, so `Z_1 ≤ 2^18.80` and **the headroom drops from 4.44 bits to 3.95 bits**. Still comfortable, but 0.49 bits were spent.

Cell counts: `sweep.py` 36,351 cells (M4 N∈{4,8,16,32,64,128}; M2 S∈{8,16,32}, R∈{1..4}); `deep.py` 18,452 cells exhausting **all** p ≡ 1 mod 32 below 2^22 at N=16; 4,400 sampled cells for σ ∈ [−16.5, −6.5].

## 4. THEOREM RC — the main new mathematics (PROVED, 20/0)

Stated and proved in the header of `rc.py`. Let n = 2N be a power of two, p ≡ 1 mod n, eps ternary of weight U, f(x) = Σ eps_j x^j (deg &lt; N = deg Φ_n):

    eps ∈ ker  ⟹  p | Res(Φ_n, f)  and  1 ≤ |Res(Φ_n, f)| ≤ U^{N/2},  hence p ≤ U^{N/2} ≤ N^{N/2}

Proof: Parseval over all 2N roots gives Σ|f(z)|² = 2NU; over the N-th roots (= the non-primitive ones, no folding since deg f &lt; N) it gives NU; subtracting, the N primitive roots carry NU; AM-GM gives |Res|² ≤ U^N. Consequences, all verified:

- **(i)** `UMIN ≥ p^{2/N}` — 0 violations over 233 nonempty-kernel cells; tightest slack ×1.096 at (N=8, p=433).
- **(ii)** `TMASS = 1 exactly for every admissible p &gt; N^{N/2}` — 0 violations; at N=4 (bound 16) **no admissible cell has a nonzero ternary kernel at all**; at N=8 (bound 4096) the largest p with TMASS&gt;1 is **881**.
- **(iii)** Σ over all admissible p of (TMASS−1) ≤ (N/2)log₂N·(2^N−1): each N-line carries finite total excess, so `sup_p CRATIO` is a **maximum over finitely many primes**, proved.

RC is exactly why my census found max CRATIO **&lt; 1** at N=4 and N=8 while N=16 reaches 1.768: the fluctuation is not statistical there, it is arithmetically extinguished. The bound |Res| ≤ U^{N/2} is tight (worst ratio exactly 1.000000, exhaustive over all 6,560 ternary f at N=8).

## 5. THE EXACT GATE (D1(c)) — subtracted against upstream first

The gate is **already banked** as CZ-M, `background/nodes/tern_master_threshold/statement.md:37-38`: "CZ-M: char-0 emptiness iff n is a 2-power (CATCH-Z6 upgraded to a rank statement, count 3^{N-phi(n)} - 1)." I claim only the quantification:

- **PFMASS(2^a·3) = (5/4)^{L/3} exactly** (Φ_n = x^{n/3} − x^{n/6} + 1 is ternary and its n/6 shifts have pairwise disjoint supports). Verified exactly at n = 12, 24, 48: 25/16, 625/256, 390625/65536.
- `lim_{p→∞} EXCESS = (PFMASS−1)p/(2^L−1)`. At L=6: slope 0.5625/63, predicting **EXCESS(6, 19993) = 178.51** — registered in advance, measured **178.5089**. That is the banked number at `statement.md:197` reproduced from a closed form.
- `lim_{p→∞} CRATIO = PFMASS`, so **sup CRATIO over composite grids is unbounded**, growing like (5/4)^{L/3}. The gate is not a technicality.
- **Registered exhibit P3c hit:** least prime p ≡ 1 mod 24 above 10^6 is p = 1000033, giving `TMASS = 625/256` **exactly** and **CRATIO = 2.4314 &gt; 2** (registered 2.4355 ± 0.03). RC's mechanism is precisely what fails here: Res(Φ_24, f) = 0 for the p-free f.
- Sharpest form of the gate: *a nonzero ternary f of degree &lt; n/2 with Res(Φ_n, f) = 0 exists iff n is not a 2-power* — one statement covering both the gate and RC's ceiling.

## 6. TWO CATCHES

**CATCH-Z24-A (forced-correction candidate on a background node).** CZ-M's parenthetical count formula `3^{n/2−phi(n)} − 1` is **false**. Exhaustive MITM over all 3^{n/2} ternary vectors: **n = 30 gives 447 (446 nonzero), formula says 2187**; **n = 42 gives 2967, formula says 19683**. It is correct at every n I tested with at most one distinct odd prime factor (8, 16, 32, 12, 18, 20, 24, 28, 36). The qualitative spine — emptiness iff 2-power — is **untouched and confirmed at every n tested**. Only the count is wrong. I did not edit the node.

**CATCH-Z24-B (my own error, self-corrected).** My first `pfree_mass` enumerated only {0,±1}-combinations of the shift basis and reported 217 at n=30 — a **lower bound**, not the count. It is exact only where the shifts have disjoint supports (the 2^a·3 family). All n = 18, 20, 28, 30, 36, 40, 44 rows in `escape.txt` are lower bounds; `addendum.py` recomputes them exhaustively.

## 7. D2 — THE CONSTANT'S LAW: one pass, two registered misses

Registered model (R4): `SD(CRATIO) = √2·2^{−0.20752N}·g(σ)`, `g(σ) = 2^{σ/2}/(1+2^σ)`.

- **P4a PASSES.** Regression of log₂(sd/g) on N over 26 live bins: slope **−0.22532**, inside the registered window [−0.30, −0.12], model −0.20752. **The DEATH condition is not met**: the fluctuation scale decays exponentially in N.
- **P4b FAILS as registered.** RSD ∈ [0.5,2] for only **11/107 bins (10.3%)**; even restricted to live bins, **11/26 (42.3%)** vs the registered ≥80%. Diagnosis: the random-code null is refuted in the σ≪0 half — **conservatively**. THEOREM RC empties the kernel there, so TMASS ≡ 1 and the only residual spread is H itself; reality fluctuates *less* than the model by up to three orders of magnitude. The model is an upper bound, not a description.
- **P4c FAILS.** The two-point fit on N∈{8,16} is unstable (only 2 live bins at N=8) and returns a positive slope; the N=32 prediction misses by a factor 2.3 (tolerance was 2). The N=4 prediction is meaningless for a reason I only learned this round: RC makes MAXCR−1 &lt; 0 identically at N=4.
- Deep-σ tail at N=16 (sampled, 400/octave): max CRATIO falls 1.0562 (σ=−6.5) → 0.999992 (σ=−16.5), and RC(ii) proves the line is dead beyond p = 2^32.

## 8. D3 — THE SHARPENING

- **S2 (the important one, PROVED and verified to 1e-14).** `TMASS = (2^N/p^κ)Σ_u Π_j cos²(π⟨u,c_j⟩/p)`, all terms non-negative. With `SMOOTH = Σ_{u≠0} G(u)`:

      Z-CEILING(C)  ⟺  SMOOTH ≤ (C−1) + C(p^κ−1)/2^N,     E[SMOOTH] = (p^κ−1)/2^N

  The u=0 term alone *is* THEOREM Z-FLOOR. **Registered disappointment, confirmed:** in the supercritical regime this says exactly "the non-trivial smoothness mass of the value code is bounded by an absolute constant" — i.e. Z-CEILING is a faithful restatement of the non-local input already named at `statement.md:157-165`, **not a weaker stepping stone**. SMOOTH at the record cell = 5.132126.
- **S1: PROVED and INERT**, as registered. E[TMASS] = HEUR exactly; Chebyshev bounds the *fraction* of bad subspaces, never the one structured subspace per cell.
- **S4: registered prediction half wrong.** USTAR/N → 1/2 confirmed in the supercritical rows; but W90/N sits at **0.688**, not the 0.5 I registered. Low-weight (Z-2) moment control reaches the mass only where the mass is already negligible — the same wall as CATCH-RL1.
- **P2a (rigidity) HIT**: TMASS is bit-identical across all φ(2S) primitive roots at 6 test cells. There is no design freedom inside the admissible family beyond (S,R,p,Λ).
- **P2b (Λ relaxation, declared boundary probe) HIT both parts**: non-consecutive all-odd Λ raises CRATIO (Λ={1,15} at (16,2,257) gives **1.5784** vs consecutive 0.8720) but stays &lt; 2 everywhere at S ≤ 16.

## 9. SCOPE PROBE — "admissible" is load-bearing and under-pinned

`statement.md:17` states Z-FLOOR for "EVERY F_p-subspace"; `statement.md:186-187` states Z-CEILING for "every **admissible** F_p-subspace L on the 2-POWER grid", with the pin only implicit at lines 13–15. For a general F_p-subspace the ratio form is false: L = span{(1,…,1)} gives the p-independent `TMASS = C(2N,N)/2^N` and, registered in advance, **CRATIO = 25.23** at N=8, p=257 (measured 25.2349). Recommend the statement pin "admissible" explicitly to the negacyclic-GRS parity row / I2 RSET row. *Self-correction:* I registered this as "unbounded in p" — wrong. It saturates at C(2N,N)/2^N ≈ 2^N/√(πN) as p→∞; it is unbounded in **N**, not p.

## 10. THE RE-POSED CONJECTURE OF RECORD (for the coordinator, not applied by me)

&gt; **CONJECTURE Z-CEILING (round-24 re-posing).** There is an absolute C such that for every admissible F_p-subspace L — *admissible pinned to the negacyclic-GRS parity row of `statement.md:13-15` and its I2 RSET specialization* — on the 2-power grid, Z(L) ≤ C(1 + 2^m/p^{dim L}). Measured floor **C ≥ 1.7681** (I2, N=16, p=161761, exact TMASS = 159/64). Registered falsifier unchanged: any admissible 2-power cell with CRATIO &gt; C. Companion **THEOREM RC** proves each N-line's sup is a finite maximum and that the ternary kernel is empty for p &gt; N^{N/2}. Load-bearing hypothesis restated sharply: Res(Φ_{2N}, f) ≠ 0 for every nonzero ternary f of degree &lt; N, which holds **iff 2N is a 2-power**; at composite 2^a·3 the p-free mass alone forces sup_p CRATIO = (5/4)^{L/3} → ∞.

## 11. THE GAP THAT MATTERS MOST

σ ≈ 0 is reachable only up to **N = 16**. The meet-in-the-middle state count is min(3^{N/2}, p^κ), and σ≈0 forces p^κ ≈ 2^N, so N=32 at σ≈0 needs 3^16 ≈ 43M states — out of reach at 1G by any κ. Since the record lives at σ≈0 and grows with the number of cells in that band (which scales like 2^N/N²), **N=32 at σ∈[−2,2] is the single highest-value next computation**, and it needs a different algorithm, not a bigger box. Until then the claim "C decays in N" rests on P4a's slope over N ∈ {8,16,32} plus RC, not on a σ-matched N-ladder.

**Honesty pins.** The calibration clause (`statement.md:96-98`, "No toy is evidence about Z_1 at the official row") binds everything above: every toy number is about the FORM. Census evidence is evidence, never proof. THEOREM RC and the PFMASS closed form are PROVED; the growth law is CONJECTURAL and two of its three registered tests failed; the record 1.7681 is exhaustive only for p &lt; 2^22 at N=16 (sampled above that, proved dead above 2^32).
