# PRE-REGISTRATION — L-B: ESCAPE-1 OVER-AGREEMENT

Pilot: Opus 5, 2026-08-03, dir
`notes/pilots_20260803/lb_escape1_overagreement/`.
**Written and saved BEFORE any computation in this pilot** (no `verify.py`
existed at save time; the first run is timestamped after this file).

Anchor: `notes/band_heart_consolidation_20260803/CONSOLIDATION.md` item
L-B (section 5.3), fallback #2 of the ratified consolidation; sibling
inputs `notes/pilots_20260803/escape1_realizability/{REPORT.md,
FABLE_AUDIT.md,verify.py}` (LEMMA R, the E1P phenomenon, flags 4/6/8).

## 0. The claim under test

**L-B.** In a full-gate admissible live-slope system realised by a
received pair `(u,v)`, a core ray `a` of escape exactly 1 is never the
SELECTED exact-A ray of its slope: `agr(z_a) > A`, hence `V_1 = 0`.

Notation of record: `A = k+h`; `agr(z) = max_{deg P < k} #{i : u_i + z
v_i = P(x_i)}`; live slope = `agr(z) = A` exactly (definitions item 7);
`(3,k+1)`-core operator `PHI` and `T^inf_a` from the unification pilot;
escape `esc_a = |S_a \ T^inf_a|`; realiser space `Ann` (collapse pilot
THEOREM 1) with `dim Ann = 2m - rank` (LEMMA R), `m = |U| - k`.

## 1. Route to be tested (fixed here, before measurement)

R1. **Reduction.** For a ray `a` with escape 1 and escaped point `x_0`,
write `Sigma~` for the system with ray `a`'s realiser condition imposed
only on `T^inf_a = S_a \ {x_0}`, and `R = Ann(Sigma~)`. For `y` outside
`S_a` let `Psi_y : R -> F_q` be the linear functional `(lambda,mu) ->
(lambda + z_a mu)(y) - p_a(y)` (`p_a` = the deg<k interpolant of
`(lambda + z_a mu)|_{T_a}`, well defined as `|T_a| = A-1 >= k`).

R2. **Dichotomy to be proved.** either some `Psi_y = 0` identically
(over-agreement FORCED at a fixed point y, for every realiser: L-B holds
at `a`), or all `Psi_y != 0` and a counting argument produces a realiser
with `agr(z_a) = A` exactly (L-B fails at `a`, modulo the other gates).

R3. **Mechanism to be identified.** WHY the E1P measurement (520/520
gave `A+1`) holds: candidate = rigidity, i.e. the condition of ray `a`
at the perturbed point is REDUNDANT given the other rays, so `p_a`
retains its unperturbed agreement set.

## 2. Predictions (P1-P6, fixed before running)

P1. E1P's extra agreement point is exactly the point deleted by the
    perturbation (`blocks[1][0]` in the sibling's `fibre_system`), not
    the escaped private point.
P2. For a COMPLETE fibre system (`U` = a multiplicative group of order
    `N`, blocks = all fibres of `x -> x^d`, `d | N`, `V = N/d >= 3`),
    `Ann` is pinned by ANY THREE rays and has the closed-form dimension
    given by the coefficient recursion `w_{d+j} = c^{-1} w_j`; hence
    `Psi_{x_0} = 0` and E1P over-agreement is a THEOREM, not a sample.
P3. For that family the pinning survives deleting one point from one
    ray, i.e. `dim Ann(Sigma~) = dim Ann(Sigma)` (redundancy).
P4. A gate-clean escape-1 system with `dim Ann(Sigma~) > dim Ann(Sigma)`
    (independent escaped-point condition) exists; on it some realiser
    gives `agr(z_a) = A` exactly.
P5. Honest prior on the verdict: **L-B is PARTIAL** — provable exactly
    on the rigid (pencil/fibre) class, with the boundary "the escaped
    point's condition is redundant"; unconditional L-B is expected to
    need L-A (pencil rigidity) as an input.
P6. Sibling sharp question (escape-1 flag 6): an all-escape-1 gate-clean
    system with `dim Ann = 1` — prior: NOT found (matching the sibling's
    820-tuple null), but the search here is over SHAPES, not slopes.

## 3. Falsifiers (LB-F1 .. LB-F10)

Each is evaluated and reported as HIT or MISS in `verify.py`; a hit is
an honest outcome, never a crash.

- **LB-F1 (headline / claim falsifier).** A fixture passing the occlib
  FULL BAND GATE (`s4lib.gate_report: FULL_GATE = True`) whose live
  system contains a `(3,k+1)`-core ray of escape exactly 1 that is
  exact-A selected (verified max agreement = A by an exact oracle).
  => **L-B REFUTED**; fixture is the deliverable.
- **LB-F2 (weak claim falsifier).** Same but only gate-clean ((T)+(P),
  band-proper depths) without the full occlib gate => L-B survives only
  as a full-gate statement; PARTIAL with that boundary.
- **LB-F3 (E1P falsifier).** A nondegenerate realiser of the sibling's
  E1P with the escape-1 ray's max agreement exactly `A`. => the 520
  samples were unrepresentative; L-B refuted at its own witness.
- **LB-F4 (THEOREM F falsifier).** In a complete fibre system with
  `V >= 3`, `dim Ann` differs from the coefficient-recursion prediction,
  or three rays fail to pin it. => P2 false, mechanism unexplained.
- **LB-F5 (dichotomy falsifier).** A fixture with `dim R >= 1`, every
  `Psi_y != 0`, and yet NO realiser attaining `agr(z_a) = A` (after the
  degeneracy exclusions counted in the proof). => R2 false.
- **LB-F6 (redundancy-vs-agreement falsifier).** A fixture with
  `dim Ann(Sigma~) = dim Ann(Sigma) + 1` (escaped-point condition
  independent) in which nonetheless every sampled realiser over-agrees.
  => a mechanism beyond the dichotomy exists; report it.
- **LB-F7 (sibling question).** An all-escape-1 gate-clean system with
  `dim Ann = 1` (`rank = 2m-1`). => flag 6 answered YES; if a realiser
  makes an escape-1 ray exact-A it also fires LB-F1/LB-F2.
- **LB-F8 (LEMMA R replay).** `dim{realisers} - 2k != 2m - rank` on any
  fixture built here => imported machinery broken, all numbers void.
- **LB-F9 (oracle soundness).** The exact agreement oracle used here
  (complement enumeration for `n-A-1` deletions, cross-checked against
  Berlekamp-Welch/brute force on small cases) disagrees with brute force
  => every agreement measurement in this pilot is void.
- **LB-F10 (fixture honesty).** The live-slope system recomputed from
  the received pair (all `z` in `P^1` with `agr(z) = A`, plus the
  selected supports) differs from the designed ray list in a way that
  changes the escape vector => the fixture does not exhibit what it
  claims.

## 4. Compute plan (law-abiding)

`tools/ramguard tiny -- python3 .../verify.py` (256M/60s); if the search
parts exceed that, `tools/ramguard local -- python3 ...` (1G/5min).
Toy scale only: `q <= 61`, `n <= 34`, exact oracles chosen so that the
agreement measurement is provably exact (complement enumeration of size
`n-A-1`, or unique decoding when `2h > m`, whichever is valid; the
validity side condition is machine-checked per fixture). No Modal, no
network. Sibling machinery (`s4lib`, `tslib`, the escape-1 and
unification `verify.py`) imported READ-ONLY via `sys.path`; nothing
outside this directory is written.

## 5. Honesty rules

- A falsifier that fires is reported in the final message, in the
  verdict line, and is not re-parameterised away.
- Any fixture claimed as a refutation must pass, in one run: gates,
  `PHI`-core with `esc_a = 1`, exact-A liveness of ray `a` by the exact
  oracle, LEMMA R identity, and the recomputed live-slope system check
  (LB-F10).
- Sampling counts and field sizes are reported; "no counterexample
  found" is never upgraded to "none exists".
