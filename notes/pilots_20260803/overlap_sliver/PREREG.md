# PRE-REGISTRATION — the OVERLAP SLIVER (2026-08-03, Opus 5)

Written BEFORE any computation in this pilot dir.  Target: item (2) of
the final open surface of `notes/band_heart_consolidation_20260803/
CONSOLIDATION.md` (UPDATE 3) — prove or refute `V <= |U|/2` (or any
bound `<= 1.16 n`) for gate-clean zero-escape ray systems with
OVERLAPPING complements at `e >= 3`, `V >= 5`.

## 0. Notation fixed here (matches the two sibling pilots)

`U` = union of the supports, `n_U = |U|`, `|S_a| = A = k+h` for all
rays, `A_a := U \ S_a` with `|A_a| = t`, `A_0` = points in every
support (`t0 = |A_0|`), `w_ab := |A_a ^ A_b|`, `m_x` = number of BLOCKS
containing `x`, `W := union of the A_a`, `n_U = |W| + t0 = k + h + t`,
`e := 2t - h`, band depth `d` = `|S_a ^ S_b| - k`.

GATE-CLEAN = (i) zero escape: every point of `U` in `>= 3` supports,
i.e. `m_x <= V-3`; (ii) pairwise `|S_a ^ S_b| >= k+1`; (iii) (T)
`|S_a ^ S_b ^ S_c| <= k-1`; (iv) depth `1 <= d <= h-2`.
NON-COLLAPSING = `Ann != 0`, i.e. `rank(Row) < 2m` (admissible /
"live" in the L-A sense).

## 1. Pre-registered falsifiers

**OS1 (the falsifier named in the task).** An OVERLAPPING gate-clean
zero-escape NON-COLLAPSING system with `V > n_U/2`.  If exhibited and
machine-audited, `V <= n/2` is REFUTED for the sliver.

**OS2 (combinatorial form of OS1).** A gate-clean zero-escape system
(overlaps present, `e >= 3`, `V >= 5`) with `V > n_U/2`, admissibility
NOT required.  Fires => the `n/2` target cannot be proved from the
combinatorial gates alone; the sliver then needs the algebra.

**OS3 (the Fisher line).** A gate-clean zero-escape system with
`V > |W|` (equivalently `V > n_U` at `t0 = 0`).  Fires => even the
`c = 1` bound `V <= n` fails combinatorially and the sliver is not
closable at any `c <= 1.16` from the gates.

**OS4 (route 1).** An overlapping gate-clean zero-escape system at
`e >= 3, V >= 5` that IS non-collapsing.  Fires => "overlap forces
collapse" (the route the task asks to try first) is REFUTED.

**OS5 (derivation sanity).** A gate-clean system violating either of
the two inequalities this pilot derives from the gates:
  (a) `w_ab + w_ac <= e - 1` for every triple of distinct blocks;
  (b) under uniform depth, `w_ab = t - h + d` for EVERY pair, and
      `t - w_ab = h - d >= 2`.
Fires => my translation of the gates is wrong; everything downstream
is void.

**OS6 (sunflower branch).** A gate-clean system whose complements form
a sunflower (common core `C`, `|A_a ^ A_b| = |C|` for all pairs) with
`V > n_U/2`.  Predicted impossible because `t - |C| = h - d >= 2`.

**OS7 (Deza branch).** A gate-clean uniform-depth system that is NOT a
sunflower and has `V > t^2 - t + 1`.  Fires => Deza's theorem is being
misapplied here.

**OS8 (multiplicity).** A gate-clean system with `max_x m_x > t`.
(Not load-bearing; recorded because `m_x <= t` would give `V <= |W|`
by double counting alone.)

## 2. Pre-registered predictions (dated before the run)

**P1.** OS2 FIRES: the projective plane `PG(2,3)` read as the block
system (`V = 13` lines of size `t = 4` on `n_U = 13` points, `k = 5`,
`h = 4`, `d = 1`, `e = 4`, `t0 = 0`) is gate-clean, overlapping, zero
escape, and has `V = n_U > n_U/2`.  `PG(2,2)` (Fano) is predicted NOT
gate-clean — (T) fails there — so `PG(2,3)` is the minimal witness.

**P2.** OS3 does NOT fire: `V <= |W| <= n_U <= n` for every gate-clean
zero-escape system, tight exactly at projective planes.  Under uniform
depth this is Fisher/Majumdar applied to `G = MM^T = (t-λ)I + λJ`.

**P3.** OS4 does NOT fire: no overlapping gate-clean non-collapsing
system exists at `V >= 5` (extends the sibling's F1/F2 measurements to
`e >= 3` and to the plane shapes).  If P3 survives, the sliver closes
at `V <= n_U/2` for ADMISSIBLE systems and at `V <= n_U` for
combinatorial ones.

**P4.** OS6 and OS7 do NOT fire.

**P5 (structure prediction).** Under uniform depth the complete
dichotomy is: sunflower (incl. disjoint) => `V <= (n_U - λ)/(t - λ)
<= n_U/2`; non-sunflower => `V <= min(n_U, t^2 - t + 1)` with equality
only for a projective plane of order `t-1`.

## 3. What counts as which verdict

- OS1 audited => REFUTED for `n/2`; report the exact surviving bound.
- OS1 not found, OS2 found, OS3 not found => the honest verdict is
  PARTIAL with the EXACT boundary: `n/2` false combinatorially,
  `V <= n_U <= n` true (hence within the `<= 1.16 n` budget), and the
  `n/2` form true exactly on the sunflower branch (and on every
  admissible system if P3 holds).
- OS3 found => the sliver is not closable from the gates; say so.

## 4. Compute law

`tools/ramguard tiny -- python3 ...` from the repo root, literal `--`.
No Modal, no network.  All algebra reuses
`notes/pilots_20260803/zero_escape_collapse/verify.py` and
`notes/pilots_20260803/la_pencil_rigidity/verify.py` read-only via
`importlib`.
