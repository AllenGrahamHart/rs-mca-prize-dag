# xr_pencil_forcing_t0

- **status:** PROVED
- **closure:** proof
- **scope:** gate-clean zero-escape **block systems** `B(V,t,t_0,k)` with
  `V >= 5` and `dim Ann >= 1`. T0 and P-SHARE are proved; **T0 carries a
  NAMED RESIDUAL** (the `t <= 2e-3` band) which is recorded below as
  explicitly NOT claimed. **T1 and T2 — the stronger forcings — are
  FALSE**, refuted constructively on 18 fixtures, and are stated here
  only as refutations.
- **provenance:** F9 pencil-forcing pilot,
  `notes/pilots_20260803/f9_pencil_forcing/`: `PREREG.md:22-24` (T0),
  `:44-54` (P-SHARE), `:26-36` (T1/T2, refuted), `:85-101` (LEMMAS 2,3
  as Q1/Q2), `:132-141` (Q4), `:143-154` (T0's registered proof route),
  `:185-208` (IN-RUN AMENDMENT 1 + LEMMA 5 with its proof),
  `verify.py`/`verify.json` (39 checks), `FABLE_AUDIT.md:3-38`
  (coordinator verdict BANKED). Ledger `notes/pilots_20260802/CAMPAIGN_LEDGER.md:918-930`.
- **HONESTY FLAG 1 — there is NO `REPORT.md` for this pilot, and NO
  continuous prose proof of T0 anywhere on disk.** What exists is: the
  pre-registered proof route (`PREREG.md:143-154`), one full bracketed
  proof (LEMMA 5, `PREREG.md:196-201`), one-line sketches for LEMMAS 2
  and 3, **no written proof at all for LEMMA 4 or for case (b)**, and the
  coordinator's one-clause description of what she hand-verified. The
  lemma NUMBERING (LEMMA 2/3/4/5) exists **only as check-label strings
  inside `verify.py`**. `proof.md` reconstructs the connecting argument
  and marks every reconstructed joint.
- **HONESTY FLAG 2 — what was hand-verified is a strict subset.**
  `FABLE_AUDIT.md:15-20` hand-checks exactly three things: **LEMMA 5**
  (the unconditional case-(a) kill), **the case-(b) cross-multiplication**
  (`gcd(zeta_i, zeta_j) = 1` forcing `s_1 ~ zeta_i`), and **the
  `T0 => M <= 1 => C = 1/2` chain**. **LEMMAS 2, 3 and 4 were
  machine-replayed only (39/39), never hand-derived.**
- **HONESTY FLAG 3 — P-SHARE's slope form is ASSERTED, not computed.**
  `verify.py:574-577` records the slope form as a check whose value is
  **hard-coded `True`**, with the detail string "set-theoretic; blocks
  inside one family are disjoint". Only the **fibre** form is machine
  tested (5,302 distinct pencil pairs, 0 sharing `>= 2`). This node's
  `verify.py` **computes both**.

## Setting

**Block system** `B(V,t,t_0,k)` exactly as `v5_occupancy`
(`f9/PREREG.md:65-69`): `U = A_0 |_| A_1 |_| ... |_| A_V` with
`|A_0| = t_0`, `|A_a| = t`, supports `S_a = U \ A_a`, distinct slopes
`z_a`. Derived identities (`v5_occupancy/REPORT.md:34-45`):

```text
|U| = t_0 + V t,   A = t_0 + (V-1) t,   h = A - k,   m = |U| - k,
sigma = |S_a ^ S_b ^ S_c| = t_0 + (V-3) t,   e = k - sigma = 2t - h,
admissible:  t >= 2,   t+1 <= h <= 2t-1,   1 <= e <= t-1,
band-proper depth d = h - t in [1, h-2].
```

`B_a := prod_{x in A_a}(X - x)`. **PENCIL** = all `B_a` in one
**2-dimensional** subspace of `F_q[X]_{<=t}`; **fibre** of a pencil = the
root set of a member `w - c w'`. `Ann` is the annihilator
(`zero_escape_collapse/verify.py:236-242`); a system is
**NON-COLLAPSING** iff `dim Ann >= 1`. Gate-clean zero-escape is the
combinatorial predicate `min(mult) >= 3`, `pair >= k+1`, `trip <= k-1`,
`1 <= pair - k <= h-2` (`la_pencil_rigidity/verify.py:262-263`).

**Q0 (definitional, and load-bearing for T0's phrasing;
`unified_pencil_bound/PREREG.md:31-39`).** Any two disjoint equal-size
blocks are fibres of a common pencil. Hence "pencil-structured" is
**VACUOUS at family size 2**, which is exactly why T0 quantifies over
pencils carrying **`>= 3`** blocks.

## Statement

### T0 (the anchor-exact statement) — PROVED, with a named residual

```text
(T0)  For a gate-clean zero-escape system with V >= 5 blocks and
      dim Ann >= 1, the blocks CANNOT be covered by two DISTINCT
      pencils carrying >= 3 blocks each.          [T0 <=> M <= 1]
```

### P-SHARE — PROVED (fibre form machine-checked; slope form argued)

```text
(P-SHARE)  Two DISTINCT pencil-structured live families share at most
           ONE live slope (equivalently, at most one fibre).
```

**Why `<= 1` and not `<= 2` is load-bearing** (`f9/PREREG.md:44-48`):
`unified_pencil_bound` PREREG Q5 registered only "`<= 2` common fibres".
At 2 shared, the pinning subfamily could be `V = 4` — **exactly the
proved no-content regime** where the counterexamples W1/W2 live — and the
anchor's reduction would be **void**. P-SHARE keeps the pinning out of
`V = 4`.

### The supporting lemmas

- **LEMMA 2 (r-formula).** For blocks with distinct `lambda_a` and
  `g'_a != 0`: `dim span{B_a : a not in {i,j}} = 2 <=> d_{ij} = 1`,
  whenever there are `>= 3` such blocks (i.e. `V >= 5`).
- **LEMMA 3 (pencil normal form).** If `>= 2` blocks off the pair share
  a `g`-direction, every block with that direction is a fibre of the
  single pencil `<f_0, f_1>`, `f_0 = B_j^Z s_0`, `f_1 = B_i^Z s_1`.
- **LEMMA 4 (rogue criterion).** `B_j in <f_0,f_1>  <=>  s_0 ~ zeta_j`.
  *(This GENERALISES the pre-registered Q4 criterion "`Z_j = empty`";
  transplant LEMMA 4, not Q4.)*
- **LEMMA 5 (intersection lemma; the only lemma with a written proof).**
  `P' ^ <B_i,B_j>` is `0` unless `s_0 ~ zeta_j` (then `<B_j>`) or
  `s_1 ~ zeta_i` (then `<B_i>`); **in every case it contains NO third
  block.**

### T1 and T2 are FALSE — refuted, not open

- **T2** ("all `V` blocks are fibres of one pencil") and **T1**
  ("at least `V-1` are") are **FALSE**, constructively refuted on **18
  fixtures** (12 at `(t,e) = (3,2)` for T2; 6 at `(4,3)` and `(5,4)` for
  T1). T0 holds on all 18.
- Consequence adopted by the coordinator (`f9/FABLE_AUDIT.md:24-28`):
  `la_pencil_rigidity`'s `V >= 5` non-existence **evidence is VOID**
  (random partitions are structurally blind to a codimension-4
  condition); its falsifier FB fires at `Delta = 0` and its PREDICTION P
  is refuted — **but its proved theorems replay clean on all 18 new
  fixtures. The conjecture died; the theorems held.**

## Explicitly NOT claimed

- **THE NAMED RESIDUAL — the `t <= 2e-3` band.** T0's **case (b)** needs
  `t >= e + max|Z|`, which is unconditional for `e <= 3` and
  `t >= 2e-2`. **The band `t <= 2e-3` is NOT proved**, and it
  **includes the prize shapes**. Read `2e-3` as `2e MINUS 3` in the
  integer parameter `e` — **not** scientific notation (`f9/FABLE_AUDIT.md:28-33`).
  - **Equivalent forms (DERIVED here, checkable in two lines; F3.e).**
    From `e = 2t-h` and `d = h-t`: `t <= 2e-3  <=>  h >= 3d+3` (the
    audit's parenthesis). And the admissible window `1 <= e <= t-1`
    combined with `t <= 2e-3` forces `e >= (t+3)/2` and `e <= t-1`,
    hence **`t >= 5`: the residual band is EMPTY for `t <= 4`, and its
    smallest shape is exactly `(t,e) = (5,4)`.** This is *why* the audit
    can say "unconditional for `e <= 3`".
  - **What supports it is EMPIRICAL, and its coverage is better than
    "empirical zero" suggests**: `54 + 12` COMPLETE two-pencil sweeps
    (completeness machine-checked, not assumed — `verify.py:765-766`,
    `:943-944`, no budget truncation against a 400,000 cap) found zero
    there; `dim G = 1` in **all 134** non-collapsing systems observed;
    and the smallest band shape `(5,4)` was itself swept exhaustively
    (`q = 61, 71, t = 5`) and carries two live fixtures (`D_q101_t5`,
    `D_q151_t5`) on which T0 held.
  - **The residual attaches to case (b), NOT to LEMMA 5.** LEMMA 5's
    written proof needs only `|Z_i| + |Z_j| < t`, which is automatic
    (`|Z| <= e-1 <= t-2`). Do not present the residual as LEMMA 5's.
- **P-DISJ is NARROWED, NOT CLOSED** (`f9/FABLE_AUDIT.md:33`,
  `PREREG.md:56-61`). That the pinning subfamily's complements are
  pairwise disjoint outside a common core is **not automatic at
  `V >= 5`** — the gate only forces each point into `<= V-3` blocks. It
  is registered as an **inherited gap**; the pilot tested the
  anchor-relevant overlap shape and explicitly did **not** close it
  (12 overlapping configs, 0 non-collapsing, and the cross-check against
  banked duality **never executed** because no non-collapsing system was
  found to cross-check — `verify.json` `I.xcheck: [0,0]`).
- **`dim G >= 2` at `V >= 5` was never OBSERVED, which is not a
  theorem.** `verify.py:1015-1017` words its own check as "no ... **was
  observed** (the branch where T0's proof needs its degree hypothesis)".
  Observational.
- **THE C = 1/2 ANCHOR IS NOT PROVED BY THIS NODE.** The anchor stands on
  **three** inputs: `{UPB e=1 + T0 + P-SHARE}` (`f9/FABLE_AUDIT.md:37`).
  This node supplies **T0 and P-SHARE only**. `UPB e=1` — the
  unconditional `C = 1/2` for all live slopes at `e = 1` — is an
  **EXTERNAL BANKED INPUT** (`unified_pencil_bound/`, ledger
  `CAMPAIGN_LEDGER.md:838-849`, audit `FABLE_AUDIT.md:6-27`) and is
  **NOT restated as this node's content**. See the WIRING note: UPB is
  banked-but-unminted and is **missing from the round-12 mint queue**;
  a second node is owed.
- **`M <= 1` is established at `e = 1` only** without T0. The
  Ann-monotone `3+3` pinning consumes `v5_occupancy` THEOREM C′, which is
  PROVED at `e = 1` and **"at `e >= 2` MEASURED only"**
  (`v5_occupancy/REPORT.md:85-87`). Filling that hole at `e >= 2` is
  exactly what T0 does — subject to its residual.
- **Combinatorial `M <= 1` is FALSE.** 170 multi-pencil matchings exist
  combinatorially; what kills them is **realisability** (0/720 realised
  vs a positive control at 200/200) — and that PART E negative is
  reported by its own source "as a **NEGATIVE, not as support** for the
  anchor" (`unified_pencil_bound/verify.py:586-588`), because
  `realise_family` never returned a pair, so the gate was never evaluated
  on a multi-pencil config.
- **Nothing about the OTHER gate.** T0's gate is the **combinatorial**
  gate on supports; UPB's FULL GATE is a six-part **spectral** condition
  on an actual received pair `(u,v)`. They are different objects, and
  `t` means different things in the two pilots. This node speaks only of
  the combinatorial gate.
- No bound on `|Gamma|`; no occupancy claim; no discharge of heart 7.

## Falsifier

A gate-clean zero-escape `V >= 5` system with `dim Ann >= 1` whose blocks
are covered by two DISTINCT pencils with `>= 3` blocks each (this is the
pilot's registered F9-F5, which kills the anchor); or two distinct
pencil-structured families sharing 2 live slopes (F9-FS); or a
counterexample to LEMMA 5's "no third block"; or two disjoint equal-size
blocks NOT realisable as fibres of a common pencil (kills Q0, hence T0's
`>= 3` phrasing).

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, **no reads outside this
directory**). The source's `verify.py` imports two other pilot
directories by absolute path (`la_pencil_rigidity`,
`zero_escape_collapse`); everything needed is **re-implemented from
scratch here** so the node survives the move. Checks: (A) Q0 — disjoint
equal-size blocks always share a pencil, so `>= 3` is the right
threshold; (B) exhaustive pencil enumeration, and **P-SHARE's fibre
form** over every distinct pencil pair; (C) **P-SHARE's slope form,
COMPUTED** — the source hard-codes it `True`; (D) LEMMA 5's algebraic
core — the coprime-degree forcing; (E) T0 as a census over enumerated
pencil covers; (F) the residual-band arithmetic — `t <= 2e-3 <=> h >= 3d+3`,
the band is EMPTY for `t <= 4`, smallest shape `(5,4)`; (G) the 18-fixture
refutation shapes recorded as REFUTATIONS of T1/T2; (H) the
`Delta` bookkeeping catch at `V = 6`, recorded.
