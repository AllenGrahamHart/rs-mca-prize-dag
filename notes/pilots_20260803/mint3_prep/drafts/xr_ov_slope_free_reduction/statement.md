# xr_ov_slope_free_reduction

- **status:** PROVED
- **closure:** proof
- **scope:** **THIS NODE IS EVIDENCE AND STRUCTURE, NOT A CLOSE.**
  **CONJECTURE OV REMAINS OPEN** — not proved and not refuted. What is
  proved is (i) a dictionary explaining why a whole family of attacks
  cannot work, (ii) a **slope-free reduction** of OV to a
  parameter-free support statement, and (iii) that statement's
  **minimal-degree branch**. The complementary branch `r > d` is OPEN.
- **provenance (IN-REPO ONLY — see FLAG 1):**
  `notes/pilots_20260803/ov_conjecture/`: `PREREG.md:5-9` (the TARGET),
  `:13-19` (notation), `:30-34` (`J`/`Jperp` and the perp identity),
  `:42-83` (falsifiers OV1-OV8), `:87-103` (predictions P1-P6),
  `:107-113` (the logical grading); `FABLE_AUDIT.md:1-31` (coordinator
  verdict + the hand-checks, which are the fullest in-repo statement of
  THEOREMS 1/2/5); `verify.py` (section headers and check labels);
  `verify.json` (22 checks, 0 failures). Ledger
  `notes/pilots_20260802/CAMPAIGN_LEDGER.md:934-941`.
- **HONESTY FLAG 1 — THE PROOF TEXT IS NOT IN THE REPOSITORY.** The OV
  pilot's `REPORT.md` **write was harness-blocked and no `REPORT.md`
  exists** in `notes/pilots_20260803/ov_conjecture/`. The full statements
  and proofs of THEOREMS 1-5 survive only in the pilot's **subagent
  transcript**, which is outside the repository tree and is **not a
  citable source for a permanent node**. Everything below is therefore
  reconstructed from the in-repo sources listed above — principally the
  coordinator's own hand-check descriptions at `FABLE_AUDIT.md:7-15`,
  which are precise enough to state the theorems but are **not proofs**.
  **RECOMMENDED ACTION BEFORE WIRING: the coordinator should persist
  `ov_conjecture/REPORT.md` verbatim from the pilot's final message,
  exactly as was done for the sibling pilot** — whose file records
  "Persisted verbatim by the coordinator from the pilot's final message;
  the pilot's own REPORT.md write was harness-blocked"
  (`notes/pilots_20260803/zero_escape_collapse/REPORT.md:3-4`). Until
  that exists, this node's proofs are RECONSTRUCTIONS and are labelled so
  throughout.
- **HONESTY FLAG 2 — THEOREMS 3 and 4 were NOT hand-verified.**
  `FABLE_AUDIT.md:7-15` hand-checks exactly **THEOREM 1**, **THEOREM 2**
  (both branches) and **THEOREM 5**. THEOREMS 3/4 are never named in the
  audit; and in the source they carry **no separate proof paragraph** —
  their derivations are inline in their statements, with only machine
  check A7 as independent support. They are stated here as
  **derivation-in-statement, machine-corroborated**, never as "proved".

## SUBTRACTION (hard law 5)

- **`collapse <=> Ann = 0` IS ALREADY BANKED IN A NODE** —
  `background/nodes/xr_support4_structure/statement.md:233` (Addendum 2,
  round-7 collapse pilot): "New proved tools: **the duality criterion
  (collapse `<=>` Ann = 0)**...". THEOREM 2's contribution is the
  `Jperp = 0 => Ann = 0` implication, **not** the duality criterion,
  which is cited.
- **PG(2,3)'s extremality is ALREADY BANKED** —
  `notes/band_heart_consolidation_20260803/CONSOLIDATION.md:170-171`
  ("PG(2,3) sharp at `V = |U|`") and
  `notes/pilots_20260802/CAMPAIGN_LEDGER.md:768-769` ("`V <= |U| <= n`
  PROVED (Fisher, self-contained, **sharp at PG(2,3)**)"). "THEOREM 5
  covers PG(2,3)" is a **re-use of the banked extremal witness**, not a
  discovery of it.
- **CONJECTURE OV's statement of record** is
  `notes/pilots_20260803/overlap_sliver/REPORT.md:26-30`; its board-level
  entry is `notes/PRIZE_RESOLUTION_ROADMAP.md:17012-17013`; the
  coordinator-ratified **slope-free restatement** is the dated addendum
  at `notes/pilots_20260803/overlap_sliver/FABLE_AUDIT.md:33-40`.
- **LEMMA R** (why `Ann = 0` kills a system) is banked at
  `notes/BAND_LANE_DEFINITIONS.md:110-111`: "rank `<= 2m-1` is NECESSARY
  for band admissibility (rank `= 2m` kills exact-A liveness)".
- Consumed, not re-derived (`ov_conjecture` flag F7): the sibling
  THEOREM 1/1'/1'' duality, LEMMA O1/O2 (constant `lam`), THEOREM O4
  (Fisher), the X1/X2/X3 pencil family, and the `zec`/`osl` primitives.

## Setting

`U` = union of supports, `n_U = |U|`, `|S_a| = k+h`, `A_a = U \ S_a`
with `|A_a| = t`, `m = n_U - k`, `w_ab = |A_a ^ A_b|`,
`d = |S_a ^ S_b| - k` (band depth), `I_ab = S_a ^ S_b`.
`W = F^U / RS_k|_U` (dim `m`), `e_x` = class of `delta_x`,
`W_a = span{e_x : x in A_a}` (dim `t`).
`Ann = {(lam,mu) in W x W : lam + z_a mu in W_a for all a}`
(`PREREG.md:13-19`). **MDS fact used throughout:** `{e_x : x in B}` is
independent **iff** `|B| <= m`.

**GATE-CLEAN** is the executable predicate
(`overlap_sliver/verify.py:107-122`, called with `strict_depth=True`
throughout the OV pilot): **zero escape** (`m_x <= V-3`, i.e. every point
lies in at most `V-3` blocks) **and** pairwise `|S_a^S_b| >= k+1`
**and** (T) `|S_a^S_b^S_c| <= k-1` **and** strict depth
`1 <= d_ab <= h-2` for every pair.

**NOTATION COLLISIONS, fixed here (F4.b).** The source writes `W` both
for the quotient space `F^U/RS_k|_U` **and** for `union A_a` in THEOREM
5's hypothesis; and `lam` both for the overlap parameter (`lam = 1`) and
for the first component of an annihilator pair `(lam, mu)`. **This node
writes `W` only for the quotient, `Y := union_a A_a` for the block
union, and `L` for the overlap parameter.**

## Statement

### THEOREM 1 (the gate <-> MDS dictionary) — PROVED, hand-verified

For a gate-clean system:

| gate | equivalent MDS statement |
|---|---|
| pairwise `\|S_a^S_b\| >= k+1` | `\|A_a u A_b\| = m-d <= m-1` — pair unions **always INDEPENDENT** |
| (T) `\|S_a^S_b^S_c\| <= k-1` | `\|A_a u A_b u A_c\| >= m+1` — triple unions **always DEPENDENT** |
| zero escape `m_x <= V-3` | `^_{a<b} (A_a u A_b) = empty` |

**THE WALL EXPLANATION (the load-bearing consequence).** Every one-shot
argument in the sibling collapse pilot — its THEOREM 2's MDS chain and
THEOREM 3's triple cover — needs **one dependent pair-union** or **one
independent triple-union**. The gates say precisely that **neither ever
happens**. The gates are exactly calibrated to defeat every argument of
that shape, so **OV cannot be closed by "vanishing on `>= k` points",
and no sharpening of that shape will do it.**

### THEOREM 2 (the slope-free reduction) — PROVED, hand-verified. *This is the result.*

Define the **parameter-free obstruction space**

```text
Jperp := ^_{a<b} (W_a + W_b)  <=  W ,      dim Jperp = m - dim J,
J     := sum_{a<b} L_ab * F[X]_{<d_ab},    L_ab = prod_{x in A_a u A_b}(X-x).
```

`Jperp` depends **only on `U` and the blocks — the slopes `z_a` do not
occur.** Then

```text
(THM 2)   Jperp = 0   ==>   Ann = 0  for EVERY slope tuple.
Equivalently:  Ann != 0 for some tuple  ==>  dim Jperp >= 2.
```

**WHY THIS MATTERS (and it is a correction to the record).** The sibling
`overlap_sliver` gathered **3.3e12 slope tuples** of evidence for OV.
THEOREM 2 says the entire obstruction is **support-level**, so that
evidence — however large — **was gathered in the WRONG SEARCH SPACE**.
The right space is **point sets**; swept, it gives 8,400 configurations
with 0 hits. The coordinator applied this as a dated addendum to the
sliver's own audit (`overlap_sliver/FABLE_AUDIT.md:33-40`).

**Note the sufficient threshold is `dim Jperp <= 1`, not `= 0`**, since
`Ann != 0` forces `dim Jperp >= 2` (`PREREG.md:107-113`).

### THEOREMS 3 and 4 — derivation-in-statement, machine-corroborated (NOT hand-verified)

- **THEOREM 3 (flat-function form).**
  `Jperp ~ {v : U -> F | v|_{I_ab} in RS_k|_{I_ab} for every pair} / RS_k|_U`.
  Call such `v` *k-flat on `I_ab`*, with `f_ab` its unique `deg < k`
  interpolant there (unique since `|I_ab| = k+d >= k+1`). By THEOREM 1,
  zero escape gives `union_{a<b} I_ab = U`; hence **if all `f_ab`
  coincide, `Jperp = 0`.**
- **THEOREM 4 (degree filtration).** Identify `v` with its interpolant;
  `r := deg v - k` is an invariant of the class. `v` is k-flat on `I_ab`
  iff `M_ab := prod_{x in I_ab}(X-x)` (monic, degree `k+d`) divides
  `v - f_ab`. Hence **`r >= d`**, and

  ```text
  r = d  <=>  v = c*M_ab + f_ab for every pair
         <=>  e_1(I_ab), ..., e_d(I_ab) are CONSTANT across pairs;
  in particular e_1:   sigma_a + sigma_b - sigma_ab = C.
  ```

### THEOREM 5 (route 1 — shared-point forcing) — PROVED, hand-verified

```text
Let the system be gate-clean, zero-escape, with L = 1 (every two
complements meet in exactly one point) and UNIFORM multiplicity
m_x = mu on Y = union_a A_a, with char F not dividing V-1-mu.
Then the r = d branch of Jperp is EMPTY.
```

**This covers PG(2,3)** — `V=13, t=h=4, k=5, d=1, L=1`, every point on
exactly `mu=4` lines, `V-1-mu = 8`. It is exactly the "prove the
projective plane case first as a lemma" branch, and it is now a theorem.

**The disjoint/overlap separator (the `e_1` system solved for the POINT
SET, exact linear algebra):**

| system | solution space | forced coordinate collisions | usable point set? |
|---|---|---|---|
| PG(2,3) (overlapping) | dim 1 | all 78 | **no** — constants only |
| MINWIT `V=6` (overlapping) | dim 1 | all 55 | **no** — constants only |
| X1-shape (DISJOINT control) | dim 5 | 0 | **yes** |
| 24 grown overlapping systems | — | — | **0 / 24 alive** |

So the mechanism producing the known non-collapsing witnesses is **alive
on disjoint blocks and dead on overlapping ones** — precisely OV's
content, proved for this branch. **Structural reason:** the only known
non-collapsing mechanism is "the blocks are the fibres of a degree-`t`
pencil", and **fibres are pairwise disjoint**. Overlap kills the only
mechanism anyone has exhibited.

## Explicitly NOT claimed

- **CONJECTURE OV IS OPEN.** Statement of record
  (`overlap_sliver/REPORT.md:26-30`): "overlapping gate-clean
  zero-escape `=>` Ann = 0 (collapse)". **Not proved, not refuted.**
  This node does not close it and **must not be cited as a close.**
- **THE RESIDUAL: the `r > d` branch is OPEN.** For `d = 1`, writing
  `B_p = A_a u A_b` (size `m-1`), `dim Jperp >= 1` iff the `m` vectors
  `(e_j(B_p))_{p in pairs}`, `j = 0..m-1`, are linearly **dependent**.
  THEOREM 5 kills only the dependency `u_1 in <u_0>` — that is `r = d`.
  **Open: dependencies involving `e_2, ..., e_{m-1}`.** The pilot states
  plainly: *"I did **not** find a reduction of `r > d` to `r = d`, and I
  do not claim one."*
  - **Why the proof breaks there.** THEOREM 5 runs entirely on the
    single linear-in-the-points equation `e_1(I_ab) = const` supplied by
    THEOREM 4's `r = d` characterisation. When `r > d` there is no such
    equation to sum over `b != a`, so the `(V-1-mu)` counting trick has
    nothing to act on.
  - **The named next attack** (derived but not carried to a finish):
    the `s = 1` rigidity — if `|A_a u A_b u A_c| = m+1` then
    `f_ab - f_ac = alpha * Z_abc` with `Z_abc` monic of degree `k-1`, and
    the telescoping cocycle
    `alpha_bc Z_abc + alpha_ce Z_ace + alpha_eb Z_aeb = 0` with
    `alpha_bc + alpha_ce + alpha_eb = 0`. **Three-block relations alone
    do not force `alpha = 0`.**
- **THEOREM 5 IS NOT SHARP, and its scope hypotheses are NOT removed:**
  `L = 1`, uniform multiplicity, `char F` not dividing `V-1-mu`, and the
  `r = d` branch only. **MINWIT is outside those hypotheses** (its
  multiplicity vector is `[3,2,2,2,2,2,3,2,2,2,2]`, not uniform) **and is
  still dead** — so the theorem is not sharp, and the sharp form was not
  chased.
- **THEOREM 2 is a SUFFICIENT condition, not an equivalence.** The
  converse (`Ann = 0 => Jperp = 0`) is nowhere claimed.
- **CONSUMERS STAY BLOCKED — do not cash this.** The pilot's own flag:
  `overlap_sliver`'s `V <= |U|/2` upgrade and `crosslane_cashout`'s
  VERDICT A (the `|K|` close) **must NOT cite this as a close**; they may
  cite THEOREM 2 only to **re-scope** the obligation. The coordinator
  concurs: "CONSUMERS STAY BLOCKED ... correctly not cashed"
  (`FABLE_AUDIT.md:20-21`).
- **TOY FIELDS AND SMALL SHAPES ONLY.** `q <= 10007` for the exact `e_1`
  linear algebra, `q <= 41` for all `Jperp`/`Ann` work; `n_U <= 15`,
  `V <= 13`. **No prize-row-scale instance was tested.**
- **COMBINATORIAL GATES ONLY.** As in the sibling pilots, the
  combinatorial gates were verified; **no realising `(u,v)` band pair was
  exhibited**.
- **The `L >= 2` sample is THIN — 2 systems**, and the coordinator
  flagged it as the weakest cell.
- **OV is VACUOUS at `V = 4`**: zero escape at `V = 4` forces disjoint
  complements, so overlapping shapes first exist at `V >= 5`. The banked
  non-collapsing witnesses X1/X2/X3 are all `V = 4` and therefore do not
  touch OV.

## Falsifier

The pilot's pre-registered set OV1-OV8, **none of which fired**. The two
that would kill the node's own content: **OV2** — an overlapping
gate-clean zero-escape system with `dim Jperp >= 2` (would show the
parameter-free obstruction is not enough); and **OV4** — a system with
`dim Ann >= 1` in the non-degenerate branch but `dim Jperp <= 1` (would
make THEOREM 2's containment `P <= Jperp` **wrong**, voiding the
reduction). **OV1** — an overlapping system with `dim Ann >= 1` — would
refute CONJECTURE OV outright.

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, **no reads outside this
directory**; PG(2,3) and MINWIT are constructed from scratch rather than
imported from the sibling pilot). Checks: (A) the MDS fact and THEOREM
1's three dictionary rows; (B) zero escape `=>` the pair-union
intersection is empty; (C) `dim Jperp` computed **two independent ways**
(the `J`-construction and the dual-code/support route) and agreeing;
(D) THEOREM 2 on the banked disjoint witnesses — `dim Ann >= 1` together
with `dim Jperp >= 2`, the containment being real and tight; (E) PG(2,3)
built from `P^2(F_3)`, verified gate-clean/overlapping/zero-escape, with
`dim Jperp = 0` over several point sets; (F) THEOREM 5's hypotheses on
PG(2,3) (`mu = 4`, `V-1-mu = 8 != 0`) and the `e_1` separator — dim-1
constants-only for the overlapping systems, alive for the disjoint
control; (G) the `r > d` residual and OV's openness recorded as
NOT-claimed.
