# SL-1b — the base-3 first-moment dimension threshold: the proofs

Round 16, 2026-08-06. Pilot `notes/pilots_20260806/f2_sl1b/`.
Verifier `verify.py`, stages S0-S9, **37/37 PASS**, digest
`F2_SL1B_ALL_PASS`. Log: `results/VERIFY_LOG.txt`.
Run: `tools/ramguard local -- python3 notes/pilots_20260806/f2_sl1b/verify.py`.

Notation is `f2_opening/PROOFS.md`'s. `F_q = F_{p^k}` is the ambient
field, `k = [F_q : F_p]`; `R` = the number of exponents in a run of
**consecutive odd** exponents contained in `Lambda`; under the
`"odd l <= t"` reading `R = |Lambda| = ceil(t/2)`
(`f2_sl1_powersums/PROOFS.md:8-10`).

---

## 0. The target, quoted verbatim

`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:316-319`:

> **SL-1b (the named residual, replacing SL-1 on the obligation list):** prove
> a **lower** bound `dim_{F_p} L >= m · log_p 3` (or a second-moment /
> anti-concentration step for `Z(L)`). This is a counting statement about the
> deployed `L`; SL-1 (distance) is now discharged and is not the obstruction.

and the two thresholds it is calibrated between,
`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:296-299`:

> ```text
>    E[Z] = O(1)          iff  p^d >~ 2^m   iff  d >= m / log2 p     <-- LEMMA 3
>    L^perp ∩ T = {0}     iff  p^d >~ 3^m   iff  d >= m · log_p 3    <-- existence
> ```

All ten cited lines are machine-checked verbatim at their cited
`file:line` by **S0** — including the two above, `f2_opening/PROOFS.md:42`
(the definition of `L`), `:81` (the dual description), `:225` (LEMMA 3),
`:15` (`m_j = 2^{22+j}`), `:330` (`dim L <= t < m`), and
`f2_sl1_powersums/PROOFS.md:99` (SL-1's `wt(eps) >= R + 1`).

### 0.1 DEFECT-1 — the statement is ambiguous, and the two readings differ

PROOFS.md:316-319 asks for one inequality; PROOFS.md:298 attaches a
*conclusion* to that inequality. They are not the same obligation:

- **(R-A) LITERAL** — `dim_{F_p} L >= m · log_p 3`, a statement about one
  integer attached to the deployed `L`.
- **(R-B) INTENDED** — the conclusion `L^perp ∩ T = {0}` that PROOFS.md:298
  ties to it, which is what (O1) at rungs 14-16 actually needs.

Per the pilot's honesty clause (`PREREG.md:60-63`) this ambiguity is
reported as a defect, both readings are addressed, and neither is
silently swapped for the other. **(R-A) is PROVED (conditionally on `t`);
(R-B) does not follow from it, and the implication is REFUTED.**

### 0.2 DEFECT-2 — the audit gloss mis-describes the constant

`FABLE_AUDIT.md:19-22` glosses SL-1b as *"the base-3 first-moment
threshold, exactly log2 3 from LEMMA 3's"*. The ratio `log2 3` is right,
but the two lines of PROOFS.md:296-299 carry **different conclusions**
(`E[Z] = O(1)` vs `L^perp ∩ T = {0}`), not one conclusion at two
constants. PROOFS.md governs. Consequence recorded in §5.

---

## 1. SUBTRACTION LEDGER (hard law 5) — declared before any claim

Five surfaces swept (`critical/`, `background/`, `notes/`, `archive/`,
`dag.json`/`experiments/`), plus this lane's own files per the
fifth-surface rule.

- **BANKED — the mechanism, in full.** The `diag × Vandermonde`
  factorisation is *not* mine. At the full `m × m` matrix:
  `f2_opening/PROOFS.md:111-123` (LEMMA 2). Applied locally to `w × w`
  minors: `f2_sl1_powersums/PROOFS.md:104-115` (THEOREM SL-1). The
  skew-tower precedent: `archive/compressed_dli_lane_20260705/
  b2b_primitive_core/notes/pro_skew_tower_packet.md:10-15`. **§2 below
  runs exactly this banked mechanism, one square further, on the
  *rank* rather than on the *distance*.** That step, and only that step,
  is claimed as new.
- **BANKED — the dual description.** `f2_opening/PROOFS.md:81`,
  verbatim: *"    sum_{i=1}^{m} eps_i y_i^{l} = 0  in F_{p^2},  for every l in Lambda."*
  Cited, not re-derived.
- **BANKED — the distance law.** `f2_sl1_powersums/PROOFS.md:99`,
  verbatim: *"> and `eps != 0` satisfies **`wt(eps) >= R + 1`**."* Used
  once, in §2 Step 5, for the `R > m` branch.
- **BANKED — LEMMA 3.** `f2_opening/PROOFS.md:225`, verbatim:
  *"    dim_{F_p} L  >=  m / log2 p  -  o(n)/log2 p."* This is a
  **necessary** condition for (O1). §5 uses it, does not reprove it.
- **BANKED — the upper bound on `dim L`.** `f2_opening/PROOFS.md:330`,
  verbatim: *"  is forced, since `dim L <= t < m`) and (O1) reduces to bounding"*,
  and the same bound in code at `f2_sl1_powersums/verify.py:1044`,
  verbatim: *"        cond_max = min(m_j, t) * log2p       # dim L <= min(m, 2R) ~ min(m,t)"*.
  **The round-15 pilot had the UPPER bound and used it; it did not have
  the LOWER bound.** That asymmetry is the whole gap this pilot closes.
- **BANKED — the first-moment identity** `E[Z(L)] = 1 + (2^m-1)(p^{m-d}-1)/(p^m-1)`
  for a **uniformly random** subspace: `f2_sl1_powersums/PROOFS.md:288-292`,
  verified there by full enumeration. §4 uses it only to state what it
  does *not* say; it is not re-derived and not disputed.
- **BANKED — the counterexample shapes.** The five rows of
  `f2_sl1_powersums/PROOFS.md:194-199` are theirs. §4 *re-uses* them,
  re-measuring each one's `dim L`, which that pilot never computed.
  **S5 reproduces all five banked minimum weights exactly (3, 5, 5, 5, 7).**
- **BANKED, AND IT ALREADY REFUTES §4's IMPLICATION IN ANOTHER LANE.**
  `critical/nodes/dli_prime_weighted_large_block_support/proof.md:18-21`,
  verbatim:

  > The earlier pointwise/sup flatness premise is false.  A low-mass full-rank
  > ternary profile can have only the zero skew in `Z_j`, giving
  > `rho_j = q^{L_j}/3^m`; when `m` is too small relative to `L_j log_3(q)`, this is
  > `q^{Omega(L_j)}` even though there is no rank defect.

  This is the **same phenomenon** as §4: a rank/dimension condition being
  satisfied does not deliver the ternary-count conclusion. The DLI lane
  refuted it for its own object in July 2026. **No F2 file cites it.**
  §4 is therefore *not* a new phenomenon — it is the F2-lane instance of a
  banked refutation, and what this pilot adds is (a) the identification,
  (b) explicit witnesses inside the *deployed* F2 family, and (c) the
  observation that it kills the named SL-1b. This runs in the direction
  DLI -> F2, the **same direction** as round-15's uncited-reduction find
  (`f2_sl1_powersums/PROOFS.md:333-340`).
- **BANKED — the tower, which pins `k`.**
  `notes/pilots_20260802/f2_deployed_windows/tower.py:15-18`, verbatim:

  > `    RUNG j (j = 1..16):  n_j = 2^{24+j},  q_j = p^{2^j},  k_j = 2^j,`
  > `    the descent step is the quadratic extension F_{q_j} / F_{q_{j-1}},`
  > `    the moving coordinates are the elements of order EXACTLY 2^{24+j},`
  > `    m_j = (n_j - n_{j-1}) / 2 = 2^{22+j} conjugate pairs.`

  and `:26`, verbatim:
  *"  (i)   v_2(q_j - 1) = e + j            for every j >= 0   [LTE],"*.
  §5.2 cites this; S8 re-verifies the LTE independently for `j = 0..8`.
- **The BCH/alternant/GRS machinery**: classical, not claimed.

**CLAIMED AS NEW BY THIS PILOT, and nothing else:**
1. §2 LEMMA SL-1b-DIM: the two-sided rank law
   `min(m, R) <= dim_{F_p} L <= min(m, k|Lambda|)`, with both bounds
   sharp (§3).
2. §3 the sharpness family (`k = 1` forces equality on the left).
3. §4 the **refutation** of `(R-A) => (R-B)`, with 61 witnesses inside
   the deployed family and an unconditional abstract argument.
4. §5 the rung-by-rung verdict table and the two named interactions
   (CATCH-4's `k`-dependence; DEFECT-3, the `F_{p^2}` feasibility
   obstruction).
5. §6 the renamed residual SL-1b'.

---

## 2. LEMMA SL-1b-DIM — the rank law

*Verified: S1 (1060 configurations, 0 violations), S2 (1060, 0
violations).*

> Let `F_q = F_{p^k}`, `n` even, `mu_n <= F_q^*`, and let `W <= mu_n` be
> closed under `x -> -x`, with `m = |W|/2` and `y_1,...,y_m` one
> representative per antipodal pair. Let `Lambda` be a set of odd
> exponents containing `R` consecutive odd exponents
> `2a+1, 2a+3, ..., 2a+2R-1` that are distinct residues mod `n`. Let `L`
> be the image of the `F_p`-linear evaluation map of
> `f2_opening/PROOFS.md:42-43`. Then
>
> ```text
>       min(m, R)   <=   dim_{F_p} L   <=   min(m, k·|Lambda|).
> ```

*Proof of the lower bound.*

**Step 1 (dual description — BANKED).** By `f2_opening/PROOFS.md:76-82`,
`eps in L^perp` iff `sum_{i} eps_i y_i^l = 0` in `F_q` for every
`l in Lambda`. (The argument there is: `<eps, s(c)> = Tr(sum_l C_l u_l)`
with `u_l = sum_i eps_i y_i^l`, and this vanishes for all
`(C_l) in F_q^{|Lambda|}` iff every `u_l = 0`, the trace form being
non-degenerate. It is stated for `k = 2`; nothing in it uses `k = 2`.)
Hence, writing `A = (y_i^l)_{l in Lambda, i=1..m} in F_q^{|Lambda| × m}`,

```text
      L^perp  =  ker(A) ∩ F_p^m   =:  ker_{F_p}(A).
```

**Step 2 (restrict to the run).** Let `A'` be the `R × m` submatrix of
`A` whose rows are the consecutive run `2a+1, ..., 2a+2R-1`. Then
`ker_{F_p}(A) ⊆ ker_{F_p}(A') ⊆ ker_{F_q}(A') ∩ F_p^m`.

**Step 3 (the banked minor is invertible).** Assume `R <= m`. Take the
first `R` columns of `A'`:

```text
      M  =  (y_{i}^{2a+2r+1})_{r=0..R-1,\ i=1..R}
         =  diag(y_1^{2a+1}, ..., y_R^{2a+1}) · ( (y_i^2)^r )_{r,i}.
```

The diagonal factor is invertible (`y_i != 0`). The second factor is a
Vandermonde in the squares `y_i^2`; since `n` is even, `-1 in mu_n` and
`-1 != 1`, so `y -> y^2` is exactly 2-to-1 on `mu_n` with fibres the
antipodal pairs, and the `y_i` are one per pair, so the `y_i^2` are
pairwise distinct. Hence `M` is invertible and
`rank_{F_q}(A') = R`, i.e. `dim_{F_q} ker_{F_q}(A') = m - R`. *This is
verbatim the mechanism of `f2_sl1_powersums/PROOFS.md:104-115`; the only
change is that it is read as a statement about the rank of `A'` instead
of about a hypothetical low-weight support.*

**Step 4 (base change).** Let `U := ker_{F_p}(A') ⊆ F_p^m`, an
`F_p`-subspace, `u := dim_{F_p} U`. An `F_p`-basis of `U` consists of
`u` vectors of `F_p^m` that are `F_p`-linearly independent; under
`F_p^m ⊗_{F_p} F_q ≅ F_q^m` they remain `F_q`-linearly independent
(a linear dependence over `F_q`, expanded in an `F_p`-basis of `F_q`,
yields one over `F_p`). They lie in `ker_{F_q}(A')`, so
`u <= dim_{F_q} ker_{F_q}(A') = m - R`.

**Step 5 (conclude).** `dim_{F_p} L = m - dim_{F_p} L^perp >= m - u >= R`.
If instead `R > m`, then by the banked distance law
(`f2_sl1_powersums/PROOFS.md:99`) any nonzero `eps in L^perp` would have
`wt(eps) >= R + 1 > m + 1`, impossible; so `L^perp = 0` and
`dim L = m`. In both branches `dim_{F_p} L >= min(m, R)`. **QED**

*Proof of the upper bound.* `L` is the image of `K1(Lambda)`, whose
`F_p`-dimension is `k·|Lambda|` (the coefficients `C_l` range over
`F_q`), and `L <= F_p^m`. **QED**

**REMARK (the distinctness hypothesis is free at the official row).**
`W ⊆ mu_n` forces `n >= |W| = 2m`, so `R <= m` gives `2a+2R-1 <= 2R-1 < 2m <= n`
for `a = 0`: the run consists of distinct residues automatically. Rungs
14-16 are exactly the regime `R < m` (`f2_opening/PROOFS.md:330`).

**COROLLARY 2.1 (the official-row form).** With `Lambda = {odd l <= t}`,
`R = |Lambda| = ceil(t/2)`, so at rungs 14-16 (`R < m`)

```text
       ceil(t/2)   <=   dim_{F_p} L   <=   min(m, k·ceil(t/2)).
```

**COROLLARY 2.2 ((R-A), the literal SL-1b).** `dim_{F_p} L >= m·log_p 3`
holds as soon as

```text
       ceil(t/2)  >=  m · log_p 3,     i.e.    t  >=  2m·log_p 3  =  2·log2(3)·m / log2 p.
```

Since `log_p 3 = 0.051146492` at `p = 2^31-2^24+1`, this reads
`t >= 0.102292984 · m`.

**COROLLARY 2.3 (LEMMA 3 is now checkable from below).** Likewise
`dim L >= m/log2 p` — the *necessary* condition
`f2_opening/PROOFS.md:225` — holds as soon as `t >= 2m/log2 p`. Before
this lemma the repo could only observe that its **upper** bound on
`dim L` was not yet below the requirement (`f2_sl1_powersums/verify.py:1044`),
which fails to refute LEMMA 3 but does not verify it. §5 verifies it.

---

## 3. Sharpness of both bounds

*Verified: S3.*

**(a) The lower bound is attained, inside the setting's own hypotheses.**
If `k = 1` (i.e. `n | p - 1`, so `mu_n <= F_p^*`), then `A` has entries in
`F_p` and only `|Lambda|` rows, so `rank_{F_p}(A) <= |Lambda|`; with
`Lambda` a consecutive odd run of length `R <= m` Step 3 gives equality:

```text
        k = 1   =>   dim_{F_p} L  =  min(m, R)   EXACTLY.
```

S3 confirms this on **all 131** `k = 1` configurations of the grid, with
no exception.

**Consequence (a no-go for improving the constant).** Any proof of
SL-1b that uses only the hypotheses of `f2_opening`'s setting — `n` even,
`W` antipodally closed, `Lambda` a consecutive odd run — cannot conclude
more than `dim L >= ceil(t/2)`. In particular the requirement
`t >= 2m·log_p 3` of Corollary 2.2 **cannot be relaxed to
`t >= m·log_p 3`** without importing information about `k` (equivalently,
about how far the window fails to lie in the prime field). The factor 2
is not slack in my argument; it is the truth on a nonempty family.

**(b) The upper bound is attained too.** 557 of the 855 configurations
with `k >= 2` have `dim L = min(m, k|Lambda|)` exactly, and 181 sit
strictly inside the interval. So `dim L` genuinely ranges over
`[min(m,R), min(m,kR)]` and neither bound can be dropped.

---

## 4. (R-B) — the intended reading — is REFUTED

*Verified: S4 (61 witnesses), S5 (banked shapes replayed), S6.*

### 4.1 The implication fails abstractly

PROOFS.md:296-299 derives its two thresholds **for a uniformly random
subspace** ("*For `L^perp` a uniformly random subspace of `F_p^m` of
codimension `d = dim L`*", `PROOFS.md:287-288`). A first-moment
threshold is a statement about an *average over subspaces*; it is not a
property of any particular one. Concretely, for any `p > 3` and any
`m >= 1/(1 - log_p 3)`, put

```text
        L^perp  =  span_{F_p} { (1, 1, 0, ..., 0) },   dim L = m - 1.
```

Then `p^{m-1} >= 3^m`, so (R-A) holds with room to spare, while
`(1,1,0,...,0) in L^perp ∩ T` is a nonzero ternary vector, so (R-B)
fails. S6 checks this at `(p,m) = (5,4), (7,4), (11,3)` and at the
**official prime** `p = 2^31-2^24+1, m = 4` — by exact integer
comparison `p^{m-1} >= 3^m`, no floating point.

This alone shows (R-A) cannot be *sufficient*. One might still hope the
deployed family is special. It is not.

### 4.2 The implication fails on the deployed family

S4 sweeps the pre-registered grid (`PREREG.md` §D) and asks: how many
configurations satisfy (R-A) — tested **exactly**, as the integer
comparison `p^{dim L} >= 3^m` — and *still* carry a nonzero ternary dual
vector? Rows with `p = 3` are excluded as declared-degenerate
(`log_3 3 = 1` makes (R-A) read `L^perp = 0`, so the implication is
vacuous there).

**714 configurations satisfy (R-A); 61 of them carry a nonzero ternary
dual vector.** Falsifier **S-F2 FIRES**. The smallest witness:

```text
   p = 7,  k = 2,  n = 12,  W = mu_12,  m = 6,  Lambda = {5, 7}  (R = 2, a = 2)
   dim L = 4     p^{dim L} = 2401  >=  3^m = 729        (R-A) HOLDS
   min ternary dual weight = 3                          (R-B) FAILS
```

and a larger one, `p = 7, k = 3, n = 18, W = mu_18, m = 9, R = 3, a = 0`,
with `dim L = 7`, `7^7 = 823543 >= 3^9 = 19683`, and a ternary dual
vector of weight 9. Every one of the 61 witnesses has minimum ternary
dual weight `>= R + 1`, so **none of them contradicts THEOREM SL-1** —
the distance law is respected exactly, and the count still refuses to
vanish. That is precisely §6's own point (`PROOFS.md:282-284`: *"These
are strictly different"*), now turned against the residual that was
named to close it.

### 4.2b CATCH — the measurement that supported the implication is a floored logarithm

*Verified: S4b.*

The implication I refute has exactly one piece of empirical support in the
repo, `f2_sl1_powersums/PROOFS.md:320-322`, verbatim:

> *Supporting measurement (S4):* over 74 configurations the count threshold
> `m·log2 3 > dim L · log2 p` **never under-predicts** — every configuration
> admitting a nonzero ternary dual vector satisfies it

That predicate is the contrapositive of (R-A) => (R-B). But the code that
checks it, `f2_sl1_powersums/verify.py:454`, is verbatim:

```text
            cond = dL * (p.bit_length() - 1)          # dim L * log2 p (approx)
```

`p.bit_length() - 1` is `floor(log2 p)`, not `log2 p`
(`log2 7 = 2.807` vs `2`; `log2 5 = 2.322` vs `2`; `log2 3 = 1.585` vs `1`).
It **understates the condition budget** by up to 40% on the very primes the
grid uses, which biases the test towards over-prediction — precisely the
"safe direction" the claim celebrates.

Re-evaluated on my 61 witnesses:

| predicate | false negatives |
|---|---|
| as **written** in PROOFS.md:321 (true `log2 p`) | **61 of 61** |
| as **coded** in verify.py:454 (`floor(log2 p)`) | 48 of 61 |

So the claim "never under-predicts" fails on every one of my witnesses
under its own stated predicate, and the floored logarithm is what masks
13 of them. Example, with an unshifted `Lambda = {1,3,5}`:

```text
   p = 7, k = 3, n = 18, W = mu_18, m = 9, R = 3, a = 0:   dim L = 7
   m log2 3      = 14.265
   dim L log2 p  = 19.651   (as coded: 7 x 2 = 14.000)
   -> stated predicate says "no ternary dual"; a ternary dual of weight 9 EXISTS.
```

The 74-row measurement is not wrong *on its own rows*; the defect is that
`verify.py:454` does not implement the predicate `PROOFS.md:321` states,
and the conclusion drawn from it does not survive either the correction or
the wider grid. **This is a code-level catch against a banked verifier and
should go back to the round-15 pilot.**

### 4.3 The banked shapes, re-measured

S5 replays the five shapes of `f2_sl1_powersums/PROOFS.md:194-199` and
reproduces all five banked minimum ternary weights exactly (3, 5, 5, 5,
7), adding the `dim L` that pilot never computed:

| shape (`p`, `k`, `n`, `m`, `R`) | banked min wt | reproduced | `dim L` | `p^{dim L} >= 3^m`? |
|---|---|---|---|---|
| 3, 2, 8, 4, 2 | 3 | **3** | 2 | no |
| 5, 2, 12, 6, 3 | 5 | **5** | 3 | no |
| 5, 2, 24, 12, 3 | 5 | **5** | 4 | no |
| 5, 2, 24, 12, 4 | 5 | **5** | 6 | no |
| 7, 2, 16, 8, 4 | 7 | **7** | 4 | no |

Honest reading: these five shapes are *not* themselves counterexamples
to the implication — each fails (R-A) — so the round-15 pilot's own
table does not by itself refute (R-B). The 61 witnesses of §4.2 do.
Recorded because the opposite (and wrong) inference is easy to draw from
the table alone.

### 4.3b Independent cross-check of every load-bearing number

*Verified: S9.*

Because §4.2b overturns a banked measurement, every witness is recomputed
by a **second, disjoint code path**: instead of constructing `F_{p^k}` as
tuples modulo an irreducible polynomial and hunting a generator, S9 builds
the cyclotomic polynomial `Phi_n(X)` over `Z`, reduces mod `p`, takes an
irreducible degree-`k` factor `g`, and uses

```text
     eps in L^perp   <=>   g(X)  |  sum_i eps_i X^{(a_i l) mod n}   in F_p[X],
```

deciding everything by polynomial remainder. Both `dim L` and the minimum
ternary weight are invariant under the relabelling `zeta -> zeta^u`, so the
two routes must agree exactly. **They agree on all 9 checked
configurations**, including all six witness shapes and the three banked
shapes of §4.3.

### 4.4 What survives

The correct residue of §6 is a **consistency check, not a discharge
route**: Corollary 2.1 shows the deployed `L` clears the base-3
first-moment threshold with a factor `2.49` in the exponent at rung 16
(§5), i.e. the deployed subspace is *no worse than a random one* at this
statistic. That is worth knowing and it is now proved rather than
assumed. It is not a proof that `L^perp ∩ T = {0}`, and no amount of
sharpening the dimension bound will make it one.

---

## 5. The official row, rung by rung

*Verified: S7 (Decimal, 60 digits, every margin reported), S8.*

Constants: `p = 2^31-2^24+1`, `log2 p = 30.988685`,
`log_p 3 = 0.051146492`, `m_j = 2^{22+j}` (`f2_opening/PROOFS.md:15`),
the four live `t` of `f2_sl1_powersums/PROOFS.md:386-391`, and the
`m_16 = 2^38` vs `2^39` ambiguity carried in both branches.

Verdicts for **(R-A)**: `PROVED` when `ceil(t/2) >= m log_p 3`;
`REFUTED` when `min(m, k·ceil(t/2)) < m log_p 3`; `OPEN` when the
interval of Corollary 2.1 straddles the threshold. Shown for `k = 2`.

**Branch `m_16 = 2^38`:**

| `t` | rung 14 | rung 15 | rung 16 |
|---|---|---|---|
| `7e10` (`f2_opening/verify.py:958,1038`) | PROVED 9.958x | PROVED 4.979x | **PROVED 2.490x** |
| `2^36` (`F2_CAMPAIGN_LOG.md:213,376,717,734`) | PROVED 9.776x | PROVED 4.888x | PROVED 2.444x |
| `2^41/log2 p` (base-field reading) | PROVED 10.095x | PROVED 5.047x | PROVED 2.524x |
| `t* = 8,592,912,739` (`xr_radius_arithmetic/proof.md:41-58`) | PROVED 1.222x | **OPEN 0.611x** | **REFUTED 0.306x** |

**Branch `m_16 = 2^39`:**

| `t` | rung 14 | rung 15 | rung 16 |
|---|---|---|---|
| `7e10` | PROVED 4.979x | PROVED 2.490x | **PROVED 1.245x** |
| `2^36` | PROVED 4.888x | PROVED 2.444x | PROVED 1.222x |
| `2^41/log2 p` | PROVED 5.047x | PROVED 2.524x | PROVED 1.262x |
| `t*` | **OPEN 0.611x** | **REFUTED 0.306x** | **REFUTED 0.153x** |

**Under the tower `k_j = 2^j` (§5.1), `m_16 = 2^38`:** the upper bound is
vacuous, so no cell can be `REFUTED` and only the `k`-free lower bound
decides:

| `t` | rung 14 | rung 15 | rung 16 |
|---|---|---|---|
| `7e10` | PROVED 9.958x | PROVED 4.979x | **PROVED 2.490x** |
| `2^36` | PROVED 9.776x | PROVED 4.888x | PROVED 2.444x |
| `2^41/log2 p` | PROVED 10.095x | PROVED 5.047x | PROVED 2.524x |
| `t*` | PROVED 1.222x | **OPEN 0.611x** | **OPEN 0.306x** |

**COROLLARY 5.1 (LEMMA 3, verified from below).** Under the three
large-`t` readings, `dim L >= ceil(t/2) >= 3.44e10 > 8.87e9 = m_16/log2 p`:
LEMMA 3's proved *necessary* condition for (O1) is **satisfied**, not
merely un-refuted. Under `t*` it is `NOT ESTABLISHED` from below
(`4.30e9 < 8.87e9`).

### 5.1 DEFECT-3 — `f2_opening`'s ambient field is a rung-1-only reading

*Verified: S8, exact integer arithmetic.*

`f2_opening/PROOFS.md:10` fixes the setting as, verbatim,
*"`G = mu_{n}` with `n | p^2-1`, `n` even; `psi(s) = zeta_p^s`."*
But the deployed ladder is a **tower**, not a fixed quadratic extension.
`notes/pilots_20260802/f2_deployed_windows/tower.py:15` fixes, verbatim:

> `    RUNG j (j = 1..16):  n_j = 2^{24+j},  q_j = p^{2^j},  k_j = 2^j,`

These are inconsistent from rung 2 upward. With `e := v_2(p-1) = 24` and
`v_2(p^2-1) = 25` (S8, from `p-1 = 2^24·127`, `p+1 = 2·1065353217`):

```text
   n_j = 2^{24+j}  divides  p^2 - 1   <=>   24 + j <= 25   <=>   j = 1.
```

S8 confirms `n_j | p^2-1` **fails at every `j` in 2..16**, and re-verifies
the tower's LTE `v_2(p^{2^j}-1) = 24+j` directly for `j = 0..8`. So
`f2_opening`'s stated setting hosts **rung 1 only**; at rungs 14-16 the
ambient field is `F_{p^{2^j}}` with `k_14 = 16384`, `k_15 = 32768`,
`k_16 = 65536`. (The tower is internally consistent with `m_j = 2^{22+j}`:
`|W| = phi(2^{24+j}) = 2^{23+j} = 2 m_j`, and `n_j = 4 m_j`, which is what
makes the distinctness hypothesis of §2 free.)

This is not a defect in §2 — the lower bound `dim L >= min(m,R)` is
`k`-free and holds in every branch. It is a defect in every argument that
used an **upper** bound on `dim L`.

### 5.2 INTERACTION-1 — CATCH-4's sign flip does not survive the tower (FLAGGED)

`f2_sl1_powersums/PROOFS.md:391` records `t*` at rung 16 as
`**VIOLATED, 0.9687x**` — a *"sign flip"* of LEMMA 3, the round-15
pilot's maintainer-level catch. That 0.9687 is `t*/(m_16/log2 p)`: it
uses the upper bound `dim L <= 2·|Lambda| ~ t`, i.e. the `k = 2` case of
Corollary 2.1, exactly as `f2_opening/PROOFS.md:330` and
`f2_sl1_powersums/verify.py:1044` do. Under the tower value `k_16 = 2^16`:

```text
   k = 2      :  dim L <= 8.593e9   <  8.870e9  ->  LEMMA 3 VIOLATED  (banked)
   k = 3      :  dim L <= 1.289e10  >  8.870e9  ->  no violation
   k_16 = 2^16:  k|Lambda| = 2.816e14 >> m_16   ->  upper bound is VACUOUS,
                 dim L <= m_16 = 2.749e11       ->  no violation derivable
```

S8 confirms the upper bound `min(m, k|Lambda|)` collapses to `m` at rungs
14-16 under **every** live `t` once `k_j = 2^j`. Consequences:

- **CATCH-4's rung-16 LEMMA 3 violation is not derivable under the
  tower.** It is an artifact of the `k = 2` reading. LEMMA 3 is not
  thereby *satisfied* under `t*` either — §5's last block shows the lower
  bound only reaches `4.30e9 < 8.87e9` — it is simply **undetermined**.
- **My own rung-16 `REFUTED` verdict for (R-A) under `t*` likewise
  evaporates** (it needs `k < 3.2722`). Under the tower the `t*` column
  reads: rung 14 PROVED (1.222x), rungs 15 and 16 **OPEN**, none refuted.
- The same collapse retracts `f2_opening/PROOFS.md:330`'s parenthetical
  *"at rungs 15-16 it is forced, since `dim L <= t < m`"*: under the tower
  `L^perp != 0` is **not** forced at rungs 15-16, because no upper bound
  puts `dim L` below `m`.

**FLAGGED, NOT RESOLVED.** Which of `f2_opening/PROOFS.md:10` and
`tower.py:15` governs is the `q = p^k` half of the sibling pilot's `t/q`
pin. This pilot takes no position; it reports that **three banked
conclusions — CATCH-4's sign flip, `f2_opening:330`'s forcing, and my own
`t*` refutation — all rest on the same `k = 2` upper bound, and all three
fail together if the tower governs.** Every `PROVED` cell in §5's tables
is `k`-free and unaffected.

---

## 6. SL-1b' — the residual, renamed

SL-1b was named (`PROOFS.md:316-319`) as the object standing between
mystery 2 and (O1) at rungs 14-16. After this pilot:

- **(R-A) is PROVED** at rungs 14-16 under `t in {7e10, 2^36, 2^41/log2 p}`,
  by Corollary 2.2, `k`-free, non-asymptotically, with margin `>= 1.22x`
  in the worst (`m_16 = 2^39`) branch. Under `t*` it is REFUTED at rung
  16 (`k <= 3`) and OPEN at rung 15.
- **(R-A) does not imply (R-B)** (§4), so proving it does **not**
  discharge (O1). Mystery 2's obligation list shortens **in name only**.

The honest replacement, stated so it cannot be mistaken for a dimension
bound again:

> **SL-1b' (the corrected residual).** At rungs 14-16, bound the ternary
> mass of the *deployed* alternant code
> `L^perp = { eps in F_p^m : sum_i eps_i y_i^l = 0, l in Lambda }`:
> prove `Z(L) = sum_{eps in L^perp ∩ T} 2^{-wt(eps)} <= 2^{o(m)}`.
> Equivalently, prove `L^perp ∩ T = {0}` for this specific code. The
> dimension of `L` is now known exactly to within the interval
> `[ceil(t/2), min(m, k·ceil(t/2))]` (§2) and is **not** the obstruction.

**A lead, not a claim (recorded so it is not re-derived).** The lower
bound of §2 can be sharpened without new ideas: for `eps in F_p^m`,
`A_Lambda eps = 0` implies `A_{p·Lambda} eps = 0` by Frobenius, so with
`Lambda*` the closure of `Lambda` under `l -> pl mod n`,

```text
        L^perp = ker_{F_p}(A_{Lambda*}),   hence   dim L >= rank_{F_q}(A_{Lambda*}).
```

`Lambda*` consists of odd residues, and at rung `j` the Frobenius orbits
have size `ord_{n_j}(p) = 2^j` (`tower.py:15`), so `|Lambda*|` can exceed
`|Lambda|` by a large factor. Whether that buys a longer *consecutive*
odd run — the only thing §2 Step 3 can use — depends on the arithmetic of
`p` mod `2^{24+j}`, i.e. on the pinned `q`. **Not evaluated here; it is
downstream of the sibling's pin.** Note the standing warning at
`f2_sl1_powersums/PROOFS.md:158-162` that gapped (generalized-Vandermonde)
minors *do* vanish in characteristic `p`, so `rank(A_{Lambda*}) = |Lambda*|`
must not be assumed.

This is the same terminal `f2_sl1_powersums/PROOFS.md:359-364` already
identified — *"Mystery 2's remaining obligation ... and mystery 4's heart
(LEMMA Y's constant-weight count in a BCH code) are the **same species of
open problem**"* — and this pilot's contribution is to remove the one
obligation that looked like a way around it.

---

## 7. Scope — what is NOT claimed

- §2 is a statement about `dim L` only. It says nothing about `Z(L)`, and
  §4 shows it cannot be made to.
- The 61 witnesses of §4.2 live in the declared box
  (`p <= 19`, `n <= 48`, `k <= 3`, `m <= 10` for the ternary sweep,
  `R <= 8`). They refute the implication; they are not evidence about the
  official row's `Z(L)`, and no extrapolation to it is made.
- Falsifier **(S-F1)** (`dim L < min(m,R)`) and **(S-F3)**
  (`dim L > min(m,k|Lambda|)`) did **not** fire anywhere in the 1060-row
  grid. That is consistency, not proof; §2 is the proof.
- §5's tables are conditional on `t` and (for the `REFUTED`/`OPEN` cells)
  on `k`. Neither is pinned here. The `PROVED` cells are `k`-free.
- DEFECT-3 (§5.1) reports that `f2_opening/PROOFS.md:10` and
  `tower.py:15` are inconsistent from rung 2 up, and that three banked
  conclusions rest on the reading that fails. It is **not** a claim about
  which reading is correct; that is the `t/q` pin pilot's question.
- §4.2b is a defect report against `f2_sl1_powersums/verify.py:454` and
  the claim at `PROOFS.md:320-322`. It does not touch that pilot's
  THEOREM SL-1, its §3 measured weight law, or its (M1)/(M2)/(M3) mass
  bounds, none of which use that predicate.
- The `Lambda*` lead in §6 is stated as a lead. It is not proved, not
  evaluated at the official row, and nothing here depends on it.
- Nothing here touches SL-2 / CATCH-3 (the `|K1|` seam), SL-1c, or PP5.0.
- No status flip is proposed for any minted node. DRAFT ONLY; no file
  outside `notes/pilots_20260806/f2_sl1b/` was written.
