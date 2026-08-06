(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Sanity check passed: `PREREG.md` was written before any compute, all three verifiers are on disk, and round 3 reproduces 19/19. Totals across the pilot: **152 checks, 3 failures, all three in round 1 and all resolved openly in round 2** (two were a choice-of-`c` artefact; one is a genuine refutation of my own pre-registered `iff`).

Files (absolute):
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/crossing_w2_opening/PREREG.md`
- `.../verify_crossing_w2.py` (74 checks, 3 fail)
- `.../verify2_floor.py` (59 checks, 0 fail)
- `.../verify3_prizerow.py` (19 checks, 0 fail)

REPORT.md writes are harness-blocked, so the report is below.

---

# CROSSING at w ≥ 2 — the lane's first dedicated opening

## 1. The exact statement the crossing heart needs

**Consumer chain.** `rate_half_list_adjacent_crossing` (TARGET, `requires: []`, a true leaf) → `list_adjacency_closing` → `list_large_m_scope_closure` → `list_grand` → `prize`.

**Obligation, verbatim:**
```
q=|F|,  B*=floor(q/2^128),  L_1(a)=max_u #{c in C: agr(c,u)&gt;=a}.
There is an agreement index a_L(C) such that
   L_1(a_L(C)) &lt;= B* &lt; L_1(a_L(C)-1).                 (RHL-ADJ)
```
**Open part, verbatim** (`frontier.md`): *"For every remaining branch `B*&gt;=3`, locate the first safe agreement inside the now-proved bracket. In the razor case, `k+2^34 &lt;= a_L(C) &lt;= a_IJ(C)`. … A closure still needs a stronger upper profile theorem and a matching predecessor witness at the same candidate."*

In `w`-coordinates (`a = k+w`), the open bracket at `n=2^41, k=2^40, q&lt;2^256` is `2^34 ≤ w ≤ n/4 = 2^39`, and the heart needs both **(UP)** `L_1(k+w) ≤ B*` and **(LO)** `L_1(k+w-1) &gt; B*`.

**The q-dependence structure, explicit.** The only exact general-`w` handle is MC-1: for `u = X^{n-1}+cX^{k+w-1}` on `H=x_0μ_n`, `r'=n-k-w`, the codewords at agreement `≥ k+w` are exactly `{T : |T|=r', e_1(T)=…=e_{w-1}(T)=0, prod T = γ}`. Indexing by `S ⊆ Z/n` and writing `W_w := {S : |S|=r', e_s(T(S))=0, s&lt;w}`, `sig(S) := ΣS mod n`, the shell is `X_w(γ) = #{S ∈ W_w : sig(S)=t(γ)}`. **All q-dependence of the (LO) side lives in the pair (|W_w|, its sig-profile).**

## 2. The obstruction map

At `w=1` the index `s` runs over the **empty** range `1..0` — `W_1` is *all* `r'`-subsets, cut out by **no field equation**. The only condition left is `prod T = γ`, a condition on `sig(S)` in `Z/n`: pure combinatorics, blind to the field. That is PK1's q-freeness.

At `w ≥ 2` the `e_s(T)=0` are genuine field equations. `e_s(T)` is a fixed `E_s(S) ∈ Z[ζ_n]`, and the condition is `P | E_s(S)` for the prime `P` over `p`. Hence `W_w = W_w^struct` (vanishes already in char 0 — Lam-Leung) `∪ W_w^acc` (nonzero in char 0, killed mod `P`).

**Where MC-3's argument breaks.** MC-3 has two steps: (i) coset unions kill `e_1..e_{M-1}` *for free* via the banked `e22` factorization; (ii) the shift `S→S+1` moves the product by the unit `m`, so `gcd(m,N)=1` equidistributes. **Step (ii) is *not* the obstruction** — §3.1 generalizes it to all `T` and all `w`. **Step (i) is the whole obstruction:** for non-coset `T` there is no identity forcing `e_s(T)=0`.

**Symmetry form.** `W_w^struct` is invariant under the full affine group `{S→aS+b : a ∈ (Z/n)*}`. In char `p` only the Frobenius subgroup `{S→p^iS+b}` survives. **The break from w=1 to w≥2 is exactly the break of `(Z/n)*` down to `⟨p⟩`.**

**Measured accidental mass** — it is the bulk, not a correction:

| (n,r') | char-0 structural | measured \|W_2\| by p |
|---|---|---|
| (15,5) | **3** | 2⁴:168, 31:93, 61:48, 11²:33, 151:33, 181:18, 19²:3, 211:3, 241:3, 271:3, 331:3 |
| (15,6) | **10** | 2⁴:280, 31:160, 61:85, 181:40, 241:40, 11²:40, 19²:25, 151:25, 211:10, 271:10 |
| (16,6) | **56** | 17:472, 7²:168, 97:136, 3⁴:120, 5⁴:56, 23²:56, 241:56 |

Accidental excess up to **56×**. PK2's calibration (`C(n,r)/q ~ 2^(2^41−256)`) puts official rows far deeper in this regime.

## 3. Proved partials

### 3.1 LEMMA X — product equidistribution for GENERAL T, all w (PROVED, 20 fixtures)

&gt; `W_w` is `ρ:S→S+1`-invariant (since `e_s(ζT)=ζ^s e_s(T)`), and `sig(ρS)=sig(S)+r'`. With `d := gcd(r',n)`, fibres of `sig` over any two residues **equal mod d** have equal size. Hence `X_w(γ) = (d/n)·#{S ∈ W_w : sig(S) ≡ t mod d}`, and `0` unless `γ/x_0^{r'} ∈ μ_n`.

*Proof.* `sig(ρ^aS)=sig(S)+ar'`; as `a` ranges over `Z/n`, `ar'` ranges over `⟨r'⟩ = dZ/n`. For `t ≡ t' (mod d)` pick `a` with `ar' ≡ t'−t`; `ρ^a` bijects the fibres. ∎

MC-3's Lemma 5 is the coset-restricted instance. Lemma X removes **both** the coset hypothesis and the `gcd=1` hypothesis — the gcd reappears exactly and only as the factor `n/d`.

**It confirms PK2 against independent data.** Round 1 fixed `c=1` and got 29/7 vs PK2's 30/8 — flagged as failures. Lemma X says the shell takes exactly `d = gcd(6,16) = 2` values. Measured fibres: `q=17 {29,30}`, `q=81 {7,8}`, `q=97 {8,9}`, `q=241 {0,7}`, `q=257 {0,7}` — **every PK2 number is one of the two Lemma-X fibres**; the gap was PK2 pinning `c ∈ F_q`, whose log class moves with the field (cf. their own row M2, "q=17, c=3"). It adds what PK2 did not record: that shell can take **only two values**, and the structural value 7 is exactly `56·d/n`.

**Prize-row bite (exact).** At `n=2^41`: `d = 2^{v_2(w)}`, so Lemma X divides by `n/d = 2^{41−v_2(w)}`. MC-3 at a 2-power `n` forces `M = 2^{v_2(w)}` and `w ≤ 2^{v_2(w)}` — i.e. **MC-3 applies only when `w` is an exact power of two: 6 values out of the 532,575,944,705 integers in the open bracket. Lemma X applies to all of them.**

### 3.2 THEOREM Q — the w≥2 dependence is on the CHARACTERISTIC only (PROVED, 7 tower pairs)

&gt; Fix `n,r',w`. For every `q` with `n | q−1`, `W_w` and its entire sig-profile depend on `q` only through `p = char F_q` — never through `e` in `q=p^e`. Changing `ζ` only permutes the profile by `S→aS`.

*Proof.* Normalize `x_0=1`. Then `T(S) ⊆ μ_n ⊆ F_p(μ_n) = F_{p^δ}`, `δ = ord_n(p)`, and every `e_s(T(S))` lies there. `F_{p^δ}` is a subfield of every admissible `F_q` (as `δ|e`), and a subfield element is zero iff it is zero in the extension. ∎

PK2's operational conclusion was *"any w≥2 claim must … be certified per-field."* **Theorem Q replaces "per-field" by "per-characteristic"** and turns PK2's parenthetical "characteristic-dependent" into a theorem with a proof. Corollary: the MC shell is invariant along the whole tower `F_p ⊂ F_{p²} ⊂ …` while `B* = ⌊q/2^128⌋` grows like `p^e`.

### 3.3 LEMMA Y — Newton linearization (one way PROVED; my `iff` REFUTED)

&gt; (a) `W_w ⊆ BCH_w := {S : p_s(T(S))=0, s&lt;w}` in **every** characteristic (that Newton direction needs no division). (b) If `w ≤ p`, equality. (c) `p_s(T(S)) = x_0^s·χ_S(ζ^s)`, so `BCH_w` = **0/1 vectors of weight r' in the cyclic code of length n over F_p with zeros ζ,…,ζ^{w−1}** — a constant-weight count in a BCH code of designed distance w.

The pre-registered `p=2, w=3` falsifier **fired hard, as predicted**: `n=15,r'=5,w=3,p=2` gives `|W_3|=3` vs `|BCH_3|=168`; `n=21,r'=7` gives 24 vs 1956. And my `iff` was **refuted**: `n=16,r'=6,w=4,p=3` has `w&gt;p` yet both sides `=8`.

**Prize-row corollary (exact).** At the razor row every admissible characteristic has `p ≥ 2^39+1 &gt; 2^39 ≥ w`: `2^41 | p^e−1` with `ord_{2^41}(p)=2^j` gives by LTE `v_2(p²−1) ≥ 42−j`, so `p ≥ 2^{41−j}−1`; `p^{2^j} ≤ q &lt; 2^256` forces `2^j(41−j) &lt; 256`, i.e. `j ≤ 2`, so `p ≥ 2^39−1`; and `2^39−1` is composite (7 | it, 8191 | it), so `p ≥ 2^39+1`. **Hence at every official rate-half razor row the window conditions are equivalent to a LINEAR system, and the crossing heart at w≥2 is literally: how many weight-r' 0/1 vectors lie in a prescribed cyclic code of length 2^41 over F_p?**

### 3.4 A q-free structural floor at w=2 that beats MC-3

Disjoint unions of `μ_p`-cosets for primes `p|n` (**mixed moduli allowed**) have `e_1(T)=0` in every characteristic. Counting them and applying Lemma X gives a q-free lower bound valid for every admissible `q`:

| (n,r') | coset-unions | char-0 struct | equal? | best MC-3 | q-free floor |
|---|---|---|---|---|---|
| (12,4) | 15 | 15 | yes | 1 | **3** |
| (12,5) | 12 | 12 | yes | **0 (vacuous)** | **1** |
| (12,6) | 24 | 24 | yes | 1 | **4** |
| (16,8) | 70 | 70 | yes | 1 | **10** |
| (18,6) | 96 | 96 | yes | 1 | **12** |
| (20,8) | 210 | 210 | yes | 2 | **22** |

Strict improvement in 7/10 rows, up to **12×**; MC-3 is outright vacuous at (12,5). Independently, the char-0 structural window is **exactly** the disjoint prime-coset unions in all ten rows (a Lam-Leung generation check). **Honest limitation, flagged: at `n=2^41` the only prime is 2, so this collapses back to MC-3 — it buys nothing at the binding razor row.**

## 4. MERGE CHECK (3b) — **VERDICT: YES at the counting-problem level, NO as a drop-in dependency reduction**

**It merges — and part of it was already machine-checked upstream.** Round-13 `sl2_unstructured` pre-registered and verified `"P2 (MC-1 is the sparse-syndrome specialization)"`, with check `"M: LEMMA W solution set == MC-1 solution set"` at `algebra.py:262-274`. **I do not claim the identification.** What is new here is the *shape*:

&gt; **LEMMA MW (new, proved + 6/6 verified).** For the MC word, LEMMA W's `w×(r'+1)` Toeplitz system has rank exactly `w` and its solution set is a **codimension-w COORDINATE affine subspace**: the rows are literally `E_{r'−s}=0` for `s=1..w−1` together with `E_0 = −c`.

*Proof.* `u` has two nonzero coefficients. Row `j=n−1−s` needs `i=−s mod n` for the `X^{n−1}` term (impossible for `1≤s≤w−1`) and `i=r'−s` for the `cX^{k+w−1}` term — a single coordinate. Row `s=0` picks up both, at `i=0` and `i=r'`. ∎

So both hearts are the same problem: *how many monic split degree-r' divisors of `X^n−1` lie on a prescribed affine subspace of locator-coefficient space?* Crossing = the **single-word (d=w)** instance at the **sparsest** syndrome on a **coordinate** subspace; SL-2-RES = the **joint (2d)** instance at a generic gated syndrome plus three filters.

**Four blockers to a real dependency reduction, all load-bearing:** (1) **quantifier** — crossing needs `max_u`, the band leaf one gated generic pair; (2) **arity** — `w` equations vs a stacked `2d` system whose rank is even hypothesized; (3) **filters** — the band leaf carries maximality, `L_P≥2`, strip survival, and the lane has already certified raw ≠ selected (`ld_core_count`: `RAW_1=334&gt;272`, selected `N_1=0`); (4) **direction** — band needs an upper bound only, crossing needs upper *and* a matching lower witness.

**What the merge does buy:** shared machinery immediately (Lemma X was derived for the crossing and is a statement about divisor windows); a **proved, exactly-counted, arbitrarily-large-excess witness for the band lane's ROUTE CUT** on a window that is not merely full rank but *coordinate* (upgrading that route cut from measurement to theorem); and a **shared terminal question** — §5's A6 residual is verbatim the band lane's own recorded terminal ("arithmetic anti-concentration / sub-Johnson RS list size on μ_n — all four lenses provably equivalent"). **The two deepest mysteries have the same terminal obstruction.** That is the honest form of the fifth reduction: not an edge deletion, but a confirmed single terminal.

## 5. Ranked anchors — the crossing lane's first anchor list

| # | anchor | status | owner |
|---|---|---|---|
| **A1** | **LEMMA X** — general-T equidistribution, shell `=(d/n)|W_w^{(j)}|` | **PROVED + 20 fixtures** | done |
| **A2** | **THEOREM Q** — certify per-CHARACTERISTIC, not per-field | **PROVED + 7 tower pairs** | done |
| **A3** | **LEMMA Y/MW** — `W_w ⊆ BCH_w` always, `=` when `w≤p`; `w&lt;p` at every official row ⇒ linear system; MC window is a codim-w coordinate subspace | **PROVED (one-way; `iff` refuted) + 16 fixtures** | done |
| **A4** | q-free mixed-modulus floor beating MC-3 up to 12× | **PROVED + 10 rows** | done; **no bite at n=2^41** |
| **A5** | **the accidental count law** — `#{S : |S|=r', χ_S(ζ^s)=0, s&lt;w}` as a function of `(n,r',w,p)`. **THE HEART** | **OPEN — the real target** | **external** |
| **A6** | analytic route: `|W_w| = p^{−δ(w−1)} Σ_a e_{r'}({ψ(Tr Σ a_s x^s)})`; residual = incomplete character sums over `μ_n` | **route, not verified here** | **external** (Bourgain–Konyagin/Katz) |
| **A7** | sig-class splitting at 2-power n (Lemma X only buys `2^{41−v_2(w)}`) | **OPEN, mechanical** | Codex |
| **A8** | Lam-Leung generation beyond two primes | **OPEN** | Codex |

**Falsifier outcomes:** (X) did not fire 0/20; (Q) did not fire 0/7; (Y) `p=2,w=3` **fired as predicted**; the `iff` **refuted my own claim**; (S) did not fire; (P) confirmed; (V) MC-1 census matched 4/4 with ceiling 4/4; (CAL) resolved as choice-of-`c`.

**New pre-registrations:** F-A8 — at `n=30` or `105` the char-0 structural window ≠ disjoint prime-coset unions, **PREDICT: FIRES**. F-A7 — sig-classes not equinumerous *across* classes at 2-power n, **PREDICT: FIRES**. F-Q2 — Theorem Q extends to the joint pair system, **PREDICT: HOLDS**.

## 6. Honest assessment

**Internal, done:** A1, A2, A3, A4, MW — complete elementary proofs, machine-checked, nothing external needed. **Internal, next:** A7 census, F-Q2, three-prime floors, Lemma X for the joint system (the band lane consumes that directly). **Codex lane:** A7, A8 — high-volume, mechanical, sharp pre-registered predictions. **External — the headline:** A5/A6 is the heart and is not an internal problem; it is *count the r'-subsets of μ_n ⊆ F_p\* whose first w−1 power sums vanish*, equivalently a constant-weight count in a length-2^41 cyclic code, equivalently anti-concentration for incomplete character sums over a large multiplicative subgroup. The "one factor of `q^{w−1}` short" gap named in `band_adjudication` and `ej_coset_spread` is the same gap.

**What did NOT move:** no bound on `L_1` for a general word. The **(UP) safe side of (RHL-ADJ) is untouched** — all of this is exact counting for one structured word family and serves the (LO) side only. The w≥2 crossing remains open.

## 7. Subtraction ledger (hard law 5)

MC-1/2/3/5, `e22`, PK1 Lemma 5, THEOREM I/I', KEY LEMMA: **banked**, cited. PK2's structural/accidental split, its naming of Lam-Leung and of "characteristic-dependent": **banked** — Theorem Q is the proof and sharpening, not the observation. LEMMA W, THEOREM D, the Toeplitz form, and the machine-checked `LEMMA W == MC-1`: **banked** (`sl2_unstructured`); Lemma MW is new. Newton-identity linearization with the `d&lt;p` caveat and Frobenius-checkpoint repair: **banked in the L1 lane** (`l1_mixed_petal_amplification/statement.md:376-404`) — not claimed. "BCH-type low-weight window" / "Mersenne cyclic code": **banked** for a different object (same file, 968-995) — not claimed; the *transfer* to the crossing window and the prize-row `w&lt;p` proof are what this pilot claims. No string `weight enumerator` / `weight distribution` exists anywhere in the repo (checked before computing).

result: Crossing w≥2 opened — 3 new proved partials (LEMMA X general-T equidistribution, THEOREM Q collapsing q-dependence to characteristic-only, LEMMA Y/MW making the window a linear BCH constant-weight count with `w&lt;p` proved at every official razor row) plus a mixed-modulus q-free floor beating MC-3 up to 12×; 152 checks/3 honest failures; MERGE VERDICT: crossing and the band divisor-count ARE the same counting problem (upstream-verified) with four blockers to a drop-in reduction, but a confirmed shared terminal obstruction (anti-concentration over μ_n).