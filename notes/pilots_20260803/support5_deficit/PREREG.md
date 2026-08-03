# PRE-REGISTRATION — support-5 / E1-family deficit pilot

**Pilot:** Opus 5 proof pilot, rs-mca Proximity Prize campaign.
**Written:** 2026-08-03T13:34:44Z (UTC, `date -u`), BEFORE any computation
in this pilot directory. No `verify.py` existed at write time.

## The commissioned question

> Does a gate-clean ALL-ESCAPE-1 ray system with `dim Ann >= 1` exist?

Setting and notation are the banked ones (`background/nodes/
xr_support4_structure/statement.md`, `notes/pilots_20260803/
zero_escape_collapse/REPORT.md` THEOREM 1):
`Row = sum_a G_{z_a}(C_{S_a})`, `U = union S_a`, `m = |U| - k`,
`rank(Row) = 2m - dim Ann`, `rank = Vh - dim Rel`.
`Ann = {(lambda,mu) : (lambda + z_a mu)|_{S_a} in RS_k|_{S_a} for all a}
/ (RS_k|_U)^2`.

Gate-clean = the campaign's `s4lib.combinatorial_gates`:
`|S_a| = k+h` (size_ok), `|S_a ^ S_b| >= k+1` (pairwise_intersecting),
`|S_a ^ S_b ^ S_c| <= k-1` (kpacking_ok); band-proper depth
`|S_a ^ S_b| <= k+h-2` (depth_ok) tracked separately, as in the
escape-1 pilot's `measure`.
All-escape-1 = every ray's `(3,k+1)`-core escape is exactly 1
(`UNI.phi_kernel`, the unification pilot's operator), core = all rays.

Prior record: 820 + 434-tuple slope sweeps over 4 + 31 E1-family shapes
found **no** deficit (`escape1_realizability/REPORT.md`,
`lb_escape1_overagreement/REPORT.md` flag 6).

## HYPOTHESIS H (stated before computing)

The prior sweeps varied **slopes at fixed supports**, and the supports
were consecutive-integer blocks. The collapse pilot's own lesson
(section 5.2) is that a deficit can be a **support** property invisible
to slope sweeps. I therefore predict:

**H1 (construction).** Take the E1 shape
`U = A_0 u B_1 u ... u B_V u Y`, `S_a = A_0 u (u_{b != a} B_b) u
{y_{i(a)}}`, `|B_b| = s`, `|Y| = p = V/2` with a perfect matching, and
choose the blocks `B_a` to be **V distinct full fibres of a degree-`s`
pencil** (concretely `x |-> x^s`, `s | q-1`, `B_a = {x : x^s = c_a}` for
distinct nonzero `s`-th powers `c_a`), and the slopes to be a **Mobius
image of the pencil parameters**, `z_a = M(c_a)` (concretely the
identity, `z_a = c_a`). Then

```text
dim Ann  =  2s - h + 1      (exactly),  hence  rank = 2m - (2s-h+1).
```

**H2 (gates).** Such a system is gate-clean, band-proper, all-escape-1,
core = all `V` rays — the gate window is `ceil(h/2) <= s <= h-2`
(so `h >= 4`), identical to the recorded E1 window.

**H3 (THEOREM D is tight).** The 3-drop floor of
`escape1_realizability/REPORT.md` gives `dim Ann <= 2s - h + 1` on this
shape; H1 saturates it, so the construction is EXTREMAL for THEOREM D.

**H4 (necessity / classification).** At the tight gate `2s = h`, for the
E1 shape, `dim Ann >= 1` holds **iff** the `V` monic degree-`s` block
polynomials `beta_a = prod_{x in B_a}(X-x)` span a **2-dimensional**
space of polynomials (blocks = fibres of one pencil) **and** the slope
tuple is a Mobius image of the pencil-parameter tuple. (Degenerate
sub-cases with vanishing coordinates are allowed to be exceptions; if
any exception appears it is reported, not hidden.)

**H5 (charge).** With `s = h/2` the construction gives
`rank = 2m - 1 = 2s + V + 2h - 3`, so `rank < 2V` iff `V > 2s + 2h - 3`;
at `s = 2, h = 4` that is `V >= 10`. Such a fixture is simultaneously
charge-defeating (`rank < 2V`) **and** deficient (`dim Ann >= 1`, so by
LEMMA R nontrivial realisers exist) — which the escape-1 pilot's
implication 4 ("every pure escape-1 counterexample has `rank = 2m`,
non-realisable") says should not exist.

## Numeric predictions (pinned BEFORE running)

All `t_0 = |A_0|`, `p = V/2`, `n = |U| = t_0 + Vs + p`,
`k = t_0 + (V-1)s + 1 - h`, `m = s + V/2 - 1 + h`.

| id | q | s | h | V | t_0 | k | n | m | pred dim Ann | pred rank | 2m | 2V | Vh | pred dim Rel |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PF1 | 11 | 2 | 4 | 4 | 0 | 3 | 10 | 7 | 1 | 13 | 14 | 8 | 16 | 3 |
| PF2 | 29 | 2 | 4 | 10 | 0 | 15 | 25 | 10 | 1 | 19 | 20 | 20 | 40 | 21 |
| PF3 | 31 | 2 | 4 | 12 | 0 | 19 | 30 | 11 | 1 | 21 | 22 | 24 | 48 | 27 |
| PF4 | 29 | 4 | 6 | 4 | 0 | 7 | 18 | 11 | 3 | 19 | 22 | 8 | 24 | 5 |
| PF5 | 17 | 2 | 4 | 4 | 2 | 5 | 12 | 7 | 1 | 13 | 14 | 8 | 16 | 3 |
| PF6 | 29 | 2 | 4 | 4 | 0 | 3 | 12 | 9 | 1 | 17 | 18 | 8 | 16 | -1 |

PF3 is the recorded **E1 pin** `(h,s,p,k) = (4,2,6,19)` with the blocks
moved onto pencil fibres and the slopes Mobius-matched; the record's
value there is `rank = 22 = 2m`, `dim Ann = 0`.
PF6 is the **private-point** variant (`|Y| = V`, every escaped point of
multiplicity 1 instead of matched pairs).

### AMENDMENT A1 — 2026-08-03T13:39:26Z, still BEFORE any computation

The PF6 row above is **self-inconsistent and I am correcting it now, on
paper, before running anything** (`ls` of this directory at the
timestamp shows only `PREREG.md`; no `verify.py` exists yet). PF6 as
pinned predicts `rank = 2m - dim Ann = 18 - 1 = 17`, but
`rank <= Vh = 16` always. The error was mine: I counted the constraints
at the escaped points and forgot that the escaped points also carry
**freedom**.

**PROP 0 (new, pre-registered as a prediction).** Every point of `U` of
multiplicity 1 contributes an independent element of `Ann`: for `y`
private to ray `a`, the pair `(lambda, mu) = (-z_a, 1)` supported at `y`
alone annihilates `Row` (ray `a` sees `lambda + z_a mu = 0` at `y`;
every other ray has `y` outside its support), and a weight-1 vector is
never in the MDS code `RS_k|_U` when `m >= 1`. Hence

```text
dim Ann  >=  #{points of U of multiplicity 1}.
```

Matched (multiplicity-2) escaped points contribute **nothing** — two
rays give two equations in the two unknowns `lambda(y), mu(y)`.

Corrected / added predictions:

| id | q | s | h | V | t_0 | escape pts | k | n | m | pred dim Ann | pred rank | 2m | 2V | Vh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PF6 | 29 | 2 | 4 | 4 | 0 | private, pencil | 3 | 12 | 9 | 5 = V + 1 | 13 | 18 | 8 | 16 |
| PF7 | 29 | 2 | 4 | 4 | 0 | private, NON-pencil | 3 | 12 | 9 | 4 = V | 14 | 18 | 8 | 16 |
| PF8 | 37 | 2 | 4 | 12 | 0 | private, NON-pencil | 19 | 36 | 17 | 12 = V | 22 | 34 | 24 | 48 |

So PF7/PF8 predict that the **private-escape variant answers the
commissioned question affirmatively for free**, with no pencil and no
Mobius condition, and that PF8 is *also* charge-defeating
(`rank = 22 < 24 = 2V`, charge `1.833`). If PROP 0 holds, the sharp and
non-trivial version of the question is the **matched (multiplicity-2)**
one — that is where H1/H4 live, and that is the headline.

Corresponding extra falsifiers:

- **SD-F14** PROP 0 fails: some PF6/PF7/PF8 fixture has
  `dim Ann < #(multiplicity-1 points)`.
- **SD-F15** PF7/PF8 (private, non-pencil) has `dim Ann > V`, i.e. the
  private freedom is not the whole story at non-pencil supports.
- **SD-F16** PF6 (private + pencil) has `dim Ann != V + (2s-h+1)`.

Cross-check adopted into the predictions (from the coordinator-audited
L-B pilot, read read-only): THEOREM F says the **complete block**
fibre system `S_a = U \ A_a`, `A_a` a full fibre of `x -> x^d`, slopes
`z_a = c_a`, has `dim Ann = max(0, d - max(0, h-d)) = max(0, 2d - h)`.
My derivation reproduces exactly that for the complete-block shape, and
gives `2s - h + 1` for the E1 shape — **one more**, the single equation
freed by the escaped point. I pre-register this as

- **SD-F17** A complete-block fibre fixture (same `q, s, h, V`, no `Y`)
  fails to reproduce THEOREM F's `max(0, 2s-h)`, or the E1 fixture on
  the same blocks fails to sit exactly one above it.

Predicted charge: PF2 `1.9 < 2`, PF3 `1.75 < 2` — both charge-defeating
with a genuine deficit.

## Controls (predicted NEGATIVE)

- **CTRL-A**: the recorded E1 build (consecutive-integer blocks) at the
  PF3 parameters, any slopes: `dim Ann = 0`, `rank = 22` (banked value
  reproduced).
- **CTRL-B**: PF1/PF3 supports (pencil fibres) with slopes NOT a Mobius
  image of `(c_a)`: `dim Ann = 0` for every such tuple swept.
- **CTRL-C**: non-pencil blocks (block polynomials spanning `> 2`
  dimensions) with every slope tuple: `dim Ann = 0`.

## Falsifiers (fire = recorded, not hidden)

- **SD-F1** PF1/PF2/PF3 is not gate-clean, or not all-escape-1, or its
  core is not all `V` rays.
- **SD-F2** PF1 (or PF3) has `dim Ann = 0` — the construction fails and
  H1 is dead.
- **SD-F3** `dim Ann != 2s - h + 1` on any PF fixture (either direction).
- **SD-F4** THEOREM D violated: `dim Rel > sum_K (h - esc) - G3`, or
  `rank <` the 3-drop floor.
- **SD-F5** `rank != 2m - dim Ann` or `rank != Vh - dim Rel` anywhere
  (would indicate a coding error, invalidating the run).
- **SD-F6** CTRL-B fires: some non-Mobius slope tuple on pencil supports
  gives `dim Ann >= 1` (H4's Mobius half is wrong).
- **SD-F7** CTRL-C fires: a non-pencil block configuration gives
  `dim Ann >= 1` (H4's pencil half is wrong).
- **SD-F8** PF2 has `rank >= 2V` (no charge defeat) — H5 dead.
- **SD-F9** LEMMA R mismatch: `dim{nontrivial realisers} != 2m - rank`.
- **SD-F10** The exhaustive smallest-shape sweep finds a `dim Ann >= 1`
  configuration that is NOT (pencil + Mobius) — H4 refuted, H1 survives.
- **SD-F11** On a nondegenerate realiser of a PF fixture, every
  escape-1 ray's maximum agreement is `A+1`, never exactly `A`
  (the E1P over-agreement phenomenon, `escape1_realizability` FLAG 4 /
  `lb_escape1_overagreement` COROLLARY F1). If this fires the fixture is
  deficient but still not band-admissible, and the verdict is PARTIAL,
  not EXISTS-for-the-band.
- **SD-F12** A banked replay disagrees: E1 (consecutive) `rank = 22`,
  U-mechanism `(3,5,1,4)` `rank = 19`, `K_V (3,7,1,5)` `rank = 35`.
- **SD-F13** (cross-check, not a hypothesis test) PF1 has `V = 4`, so
  every relation has ray-support `<= 4`. If PF1 shows `dim Ann >= 1`
  then the flag-6 statement "a deficit needs a relation of ray-support
  `>= 5`" is REFUTED at `V = 4`; if instead PF1 shows `dim Ann = 0` while
  PF3 shows `dim Ann = 1`, flag-6 survives and the deficit is genuinely
  a support-`>= 5` phenomenon. Both outcomes are reported.

## Decisive design for the smallest shape (route 3)

Smallest admissible all-escape-1 E1 shape: `s = 2, h = 4, V = 4,
t_0 = 0, k = 3, n = 10`, minimal field `q = 11`.
`dim Ann` is invariant under affine reparametrisation of the evaluation
points (`RS_k` is affine-invariant), so every configuration is
equivalent to one with `B_1 = {0,1}`. That leaves
`C(9,2) C(7,2) C(5,2) * 3 * 2 = 45,360` configurations; the conditions
depend on the slopes only through two ratios, giving `9 * 8 = 72`
admissible slope classes. `45,360 * 72 = 3,265,920` cases — **exhaustive,
not sampled**. A NO on the complement of (pencil + Mobius) is therefore a
theorem for this shape over `F_11`.
The fast per-case test (a `(V-2)(h-1) x 2s` matrix nullity) will be
validated against the full `2m - rank(Row)` computation on random
samples before it is trusted; a mismatch fires SD-F5.

## Compute law

Every run under `tools/ramguard tiny|local -- python3 ...` from the repo
root, literal `--`. No Modal, no network. Sibling libraries
(`tslib`, `occlib`, `s4lib`, the escape-1 and unification verifiers)
are imported READ-ONLY; no node, `dag.json`, `critical/`, `background/`
or `tools/` file is edited by this pilot.
