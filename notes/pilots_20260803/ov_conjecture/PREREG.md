# PRE-REGISTRATION — CONJECTURE OV (2026-08-03, Opus 5)

Written BEFORE any computation in this pilot dir.

TARGET.  Every gate-clean ((T): triples <= k-1; pairwise >= k+1)
ZERO-ESCAPE ray system with OVERLAPPING complements (some
`A_a ^ A_b != empty`) has `Ann = 0` (rank = 2m), hence is band-
INADMISSIBLE by LEMMA R; so admissible zero-escape systems have
DISJOINT complements.

## 0. Notation (matches the three sibling pilots)

`U` = union of supports, `n_U = |U| = k + h + t`, `|S_a| = k + h`,
`A_a = U \ S_a`, `|A_a| = t`, `m = n_U - k = h + t`,
`w_ab = |A_a ^ A_b|`, `lam` = the common value under uniform depth,
`d = |S_a^S_b| - k` = band depth, `e = 2t - h`, `t0 = |A_0|`.
`W = F^U / RS_k|_U` (dim `m`), `e_x` = class of `delta_x`,
`W_a` = span of `{e_x : x in A_a}` (dim `t`).
`Ann = {(lam,mu) in W x W : lam + z_a mu in W_a for all a}` (THM 1').

## 1. The dictionary I will use (stated before testing)

MDS fact: `{e_x : x in B}` independent iff `|B| <= m`.

- (D1) pairwise gate `|S_a^S_b| >= k+1`  <=>  `|A_a u A_b| = m - d <= m-1`.
- (D2) gate (T) `|S_a^S_b^S_c| <= k-1`   <=>  `|A_a u A_b u A_c| >= m+1`.
- (D3) zero escape `m_x <= V-3`          =>   `^_{a<b} (A_a u A_b) = empty`.
- (D4) `W_a ^ W_b = span(A_a ^ A_b)` (dim `lam`), by (D1)+MDS.
- (D5) `W_a + W_b = span(A_a u A_b)`, dim `m - d`;
       `(W_a + W_b)^perp = L_ab * F[X]_{<d}`, `L_ab = prod_{x in A_a u A_b}(X-x)`.

Define the PARAMETER-FREE OBSTRUCTION SPACE
`Jperp := ^_{a<b} (W_a + W_b) <= W`,  `J := sum_{a<b} L_ab F[X]_{<d}`,
`dim Jperp = m - dim J`.

Containment I claim and will machine-check: if `(lam,mu) in Ann` with
`lam, mu` linearly independent then `P = span(lam,mu) <= Jperp`, so
`dim Ann >= 1` (non-degenerate branch) implies `dim Jperp >= 2`.

## 2. Pre-registered falsifiers

**OV1 (the conjecture itself).**  An OVERLAPPING (`lam >= 1`)
gate-clean zero-escape ray system, with an explicit point set
`U <= F_q` and slope tuple `(z_a)`, having `dim Ann >= 1`.
Machine-audited through the sibling `zec.ann_dim` / `zec.rank_row`.
FIRES => **CONJECTURE OV REFUTED**; report the fixture.

**OV2 (route 2a — the parameter-free route).**  An overlapping
gate-clean zero-escape system with `dim Jperp >= 2`.
FIRES => the parameter-free obstruction is NOT enough; OV (if true)
needs the slope/cross-ratio data, and I must go to route 2b.

**OV3 (dictionary sanity — kills everything downstream if it fires).**
A gate-clean system violating any of (D1)-(D5) as literally stated:
`|A_a u A_b| != m-d`, or a triple with `|A_a u A_b u A_c| <= m`, or
`dim(W_a+W_b) != m-d`, or `dim(W_a^W_b) != w_ab`, or
`^_{a<b}(A_a u A_b) != empty` under zero escape.

**OV4 (containment sanity).**  A system with `dim Ann >= 1` in the
non-degenerate branch but `dim Jperp <= 1`.  FIRES => my derivation of
`P <= Jperp` is WRONG and section 1 is void.  In particular the banked
DISJOINT counterexamples X1/X2/X3 (`zero_escape_collapse` 5.1) MUST
have `dim Jperp >= 2`; if any of them has `dim Jperp <= 1` this fires.

**OV5 (the extremal case).**  `PG(2,3)` read as a block system
(`V = 13`, `t = 4`, `n_U = 13`, `k = 5`, `h = 4`, `d = 1`, `lam = 1`)
with `dim Jperp >= 2`, over any point set `U <= F_q` I test.
FIRES => route 2a is dead at exactly the case the sliver says is sharp.

**OV6 (the lam boundary).**  An overlapping gate-clean zero-escape
system with `lam >= 2` and `dim Jperp >= 2` while every `lam = 1`
system tested has `dim Jperp <= 1`.
FIRES => verdict is PARTIAL with the exact boundary at `lam = 1`.

**OV7 (degenerate branch).**  A gate-clean zero-escape system with
`^_{a in A} W_a != 0` for some `|A| >= V-1`.  Predicted impossible:
it needs a point in `>= V-1` blocks, i.e. `m_x >= V-1 > V-3`.
FIRES => the `dim P = 1` branch of the argument is not closed by zero
escape alone.

**OV8 (compute-law / replay).**  Any claimed theorem in this pilot
that does not replay PG(2,3) AND the sliver's frozen minimal witness
`MINWIT` (`V=6, n_U=11, t=4, h=4, k=3`) as mandatory checks.

## 3. Pre-registered predictions (dated before the run)

- **P1.** OV1 does NOT fire (OV is true).
- **P2.** OV2 does NOT fire: `dim Jperp <= 1` for every overlapping
  gate-clean zero-escape system, over every point set.  I predict
  `dim Jperp = 0` in the large majority and `= 1` only sporadically.
- **P3.** OV4 does NOT fire; X1/X2/X3 all have `dim Jperp >= 2`
  (X1 predicted exactly 2: its `L_ab = (X^2-c_a)(X^2-c_b)` all lie in
  `span{1, X^2, X^4}`, so `dim J <= 3 = m-2`).
- **P4.** OV5 does NOT fire; `PG(2,3)` has `dim Jperp = 0`.
- **P5 (structure).**  The mechanism that makes `dim Jperp >= 2`
  possible is the blocks being FIBRES of a pencil, and fibres are
  pairwise DISJOINT — so overlap kills the only known mechanism.  I
  predict the proof of P2 runs through: `nu in Jperp` has a UNIQUE
  representative `v^{ab}` supported on `A_a u A_b` (uniqueness because
  `|A_a u A_b| = m-d < m+1 = ` the MDS minimum distance), and zero
  escape forces `^_{a<b}(A_a u A_b) = empty`, so the reps cannot all
  agree; overlap obstructs the disagreement.
- **P6.** OV3, OV7, OV8 do NOT fire.

## 4. What counts as which verdict

- OV1 audited  => **OV REFUTED**, with the fixture and its mechanism.
- OV1 not found, OV2 not found, and a PROOF of `dim Jperp <= 1` from
  the gates + overlap + zero escape  => **OV PROVED** (parameter-free,
  strictly stronger than OV).
- OV1 not found, OV2 not found, no proof  => **PARTIAL**: state the
  exact proved sub-class (e.g. `lam = 1`, or `d = 1`) and the exact
  residual, with the evidence.
- OV2 fires  => route 2a dead; verdict PARTIAL or REFUTED per OV1.
- OV6 fires  => **PARTIAL with the exact lam-boundary.**

## 5. Compute law

`tools/ramguard tiny -- python3 ...` (or `local` if needed) from the
repo root, literal `--`.  No Modal, no network.  All ray algebra is
reused read-only via `importlib` from
`notes/pilots_20260803/zero_escape_collapse/verify.py` (`zec`) and
`notes/pilots_20260803/overlap_sliver/verify.py` (`osl`).
