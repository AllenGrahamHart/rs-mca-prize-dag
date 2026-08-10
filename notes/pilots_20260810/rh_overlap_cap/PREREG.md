# PREREG — rh_overlap_cap (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/list_profile_bound/REPORT.md` (round 29)
2. `notes/pilots_20260810/collinearity_object/REPORT.md` (round 29)

## Mandate

THE SAFE HALF OF RH-AC IS ONE INEQUALITY (round-29 T5): if the
pairwise-overlap cap stays strictly below a^2/n = 2^39 + 2^34 + 2^27
at sigma = 2^34 (a = k + 2^34, n = 2^41, k = 2^40), then T3 closes
the safe half of the crossing with 89 bits of margin; the open
bracket is exactly the MDS-vs-Fisher overlap gap, ratio 0.999748.
Separately, round-29 T4 proved sporadic collinearities of the
locator set {P_S} DO NOT EXIST for RIG = a-1-2s >= 0 — all
collinearity families are pencils, M <= m+1, T <= rho+1 — and U1
proved the two round-28 point sets are one set up to a fixed
collineation. NOBODY has yet attacked the overlap-cap inequality
WITH the pencils-only structure in hand. YOUR JOB: that attack.

## Deliverables

**D1 — THE EXTREMAL STRUCTURE.** What does a pairwise-overlap
configuration at the cap look like? Use the T4 census (pencils only,
the d_x law, families capped at m+1) to characterize the maximal
overlap achievable by pencil families, exactly. If pencil structure
forces overlap <= a^2/n - delta for an explicit delta > 0, that is
the round: derive delta and check it against the 0.999748 ratio.

**D2 — SUBCLASS PROOFS.** Prove the inequality on the largest
structured subclasses you can reach (single-pencil, bounded-m,
minimum-weight strata), each stated with exact scope and a
falsifier. POSE what remains as named residuals.

**D3 — THE SCALED SEARCH.** At small admissible scales (the same
scale ladder the round-29 pilots used), measure the true max
pairwise overlap vs the a^2/n cap and vs the Fisher bound. Is the
0.999748 gap real headroom or an artifact of the bound pair? Exact
integers; scaling trend across >= 3 scales; pre-register the
extrapolation BEFORE running.

**D4 — CONSUMER CHECK (CATCH-24C).** Quote, file:line, exactly what
T3/T5 consume from the cap (which overlap notion, pairwise over
WHICH set, at which sigma) and confirm D1-D3 attack THAT object —
the round-28/29 corrections show near-miss objects are the campaign
hazard. Misses first.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (node.json
  shards + grep); stream-parse large files; checkpointed batches with
  results files for anything long.
- WRITE SCOPE: ONLY inside notes/pilots_20260810/rh_overlap_cap/.
  No dag/, nodes/, tools/ edits. No git. Never touch any path
  containing prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_type2_stratum,
  rh_transport_dictionary, rh_e_axis_audit). Round-30 and earlier
  pilot dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (P(inequality provable this round), expected
  extremal shape, expected scaled-gap trend) BEFORE any further read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims; banked scripts from scratch copies only.

## Pilot registrations

Appended after reading ONLY `list_profile_bound/REPORT.md` and
`collinearity_object/REPORT.md`, and BEFORE any other read, grep, ls,
or interpreter invocation. Everything below is derived from those two
anchors plus arithmetic done in-head; nothing here is measured.

### R0 — Functionals I will measure (CATCH-19C)

- `OVL(lam,mu) := |A_lam ∩ A_mu|` — the pairwise overlap. **Two rival
  readings, and separating them is R3 below**: (i) FAR-CA reading,
  `A_lam = Agr(y_1 - lam*y_2, c_lam)` (round-29 T1's sets); (ii)
  JOHNSON reading, `A_lam = Agr(z, c_lam)` for one fixed word `z` and
  distinct codewords `c_lam` (the classical MDS-Johnson setup).
- `e_P` — core size of a line/pencil `P` (T1(ii): all pairwise
  intersections on `P` coincide).
- `m_P` — number of slopes on line `P`; `t(lam_0)` — number of lines
  through a fixed slope (**LINE DEGREE**, my proposed new invariant).
- `GAP_FISHER(a) := (k-1) - a^2/n`; `BRACKET(a) := 3n/4 - a`.
- `RATIO_CAP := (k-1)/(a^2/n)` — the factor by which the cap must be
  beaten. `RATIO_FAR := (a-1)/(a^2/n)`.
- `MAXCONSTRUCT(cell)` — largest `OVL` I can *construct* in a cell
  subject to (>= 2 admissible slopes, each agreement >= a, far-ness).
  Explicitly a LOWER bound on the true max (see R7).

### R1 — Priors demanded by the brief

- **P(the inequality "max pairwise overlap < a^2/n at sigma=2^34" is
  PROVED this round) = 0.05.**
- **P(the route as posed is REFUTED this round — an explicit
  admissible configuration with `OVL >= a^2/n`) = 0.75.**
- **P(neither; ambiguous) = 0.20.**
- **P(T5 as written conflates two different overlap notions, i.e. the
  `k-1` cap and the far-CA sets do not belong to the same object)
  = 0.65.** This is the CATCH-24C hazard I expect to fire.

### R2 — Expected extremal shape (blind)

Two candidate extremal configurations, one per reading:

- **(E-JOH) the MDS-maximal pair.** Two codewords `c_1 != c_2` of the
  RS code agreeing on exactly `k-1 = 2^40-1` positions (attained,
  since MDS has weight-`(n-k+1)` codewords); let `z` equal them on all
  `k-1` of those, then equal `c_1` on `2^34+1` further positions and
  `c_2` on `2^34+1` further positions (disjoint; `n-(k-1) = 2^40+1`
  positions are free, so there is room). Then both agreements are
  `>= a` and `OVL = k-1 = 1,099,511,627,775 > a^2/n = 567,069,900,800`.
- **(E-PEN) the maximal-core pencil.** Core `E`, `|E| = e`; write
  `y_1 = u + d_1`, `y_2 = v + d_2` with `d_1,d_2` vanishing exactly on
  `E`; off `E` each coordinate `i` with `d_2(i) != 0` joins exactly one
  slope `lam_i = d_1(i)/d_2(i)`, so petals are automatically disjoint
  (this re-derives T1(iii)). Taking `e = a-1` and singleton petals
  gives `M = n-a+1` slopes with every pairwise overlap exactly
  `a-1 = 1,116,691,496,959`.

**Registered extremal prediction: the cap is not merely unproved, it
is FALSE at sigma = 2^34, and the witnesses are two-line objects.**

### R3 — The structural claims I expect to land (registered as targets)

- **(A) T5's "they end together" is FALSE.** Exactly
  `GAP_FISHER = BRACKET - 1 - s^2/(2k)` with `s = a-k`; at `s = 2^34`,
  `s^2/(2k) = 2^27`, hence `532,575,944,704 - 1 - 134,217,728 =
  532,441,726,975` and the ratio `0.999748` is a LOCAL coincidence at
  one `sigma`, not an identity. `GAP_FISHER` vanishes at
  `a = sqrt(n(k-1)) ~ 0.70711n`, `BRACKET` at `a = 0.75n`; they differ
  by **94,323,185,676** (predicted exactly; this is the same integer
  round-29's D2 attributes to the integer-Johnson anchor).
- **(B) The cap is a STRONGER statement than the theorem it serves.**
  By Corrádi/convexity the *average* pairwise overlap of `M` sets of
  size `a` in `[n]` is `a^2/n - a(n-a)/(n(M-1))`, i.e. it approaches
  `a^2/n` from below as `M` grows, and Fisher is exactly tight there.
  So "max overlap `<= a^2/n - 1`" implies `M <= a(n-a)/n + 1 =
  549,621,596,161` but is not implied by it: the route asks for
  something strictly stronger than the target list bound. Predicted
  reproduction of `549,621,596,161` from `a(n-a)/n + 1`.
- **(C) Big cores force SHORT lines.** T1(iv) at `e_P = a^2/n` gives
  `m_P <= 1 + n/a`; at razor `n/a = 1.96923`, so **`m_P <= 2`**. Lines
  whose core reaches the Fisher threshold carry exactly two slopes.
  This is the dichotomy engine and it survives the refutation of (A).
- **(D) The honest replacement target is the LINE DEGREE.**
  `B <= 1 + sum_{P through lam_0} (m_P - 1) <= 1 + t*(n-a)`, so
  `t <= 2^128/(n-a)` suffices. Predicted threshold
  `T_MAX = 2^128/1,082,331,758,592 = 2^88.02`. I register LINE-DEGREE
  as the named residual I expect to hand forward in place of the cap.
- **(E) Second-level Fisher is FARTHER away than the first.** Cores
  through a fixed slope live in `A_{lam_0}` (ground size `a`) with
  `|E_i| >= 2a-n = 2^35`; the second-level Fisher threshold is
  `(2a-n)^2/a = 2^36/65 = 1,057,222,656.98` (`~2^30`) against the same
  MDS cap `2^40-1` — a factor `~2^10`, versus the first level's factor
  `1.9389`. Predicted `a/(2a-n) = 65/2 = 32.5` exactly (so disjoint
  cores would give `t <= 32`).

### R4 — Route order

(a) D4 consumer check FIRST (which overlap notion, quoted file:line),
because R1 gives 0.65 to an object slip; (b) exact-integer replay of
the razor arithmetic; (c) explicit refutation constructions at razor
and at scaled cells; (d) the subclass proofs (single pencil, big-core,
bounded line degree); (e) the scaled ladder. Route (f), any character
sum or density heuristic, is NOT taken (R7).

### R5 — Cell grid, pre-registered BEFORE any run

The round-29 ladder is `(n_s,k_s) = (8,4)`, `a in {5,6,7}`, rate 1/2.
**Registered claim: that ladder has ZERO POWER for this round**,
because `GAP_FISHER = (k-1) - a^2/n = 3 - 25/8 = -0.125 < 0` at
`(8,4,5)` — the MDS cap already lies *below* the Fisher threshold
there, so T3's hypothesis is automatic and no counterexample can
exist. Round-29's "0 violations of T3" at that cell is therefore
predicted to be vacuous.

Positive-gap cells at rate 1/2 require `k^2 - 2k - 2ks - s^2 > 0`
(`s = a-k`). Registered ladder, with predicted `GAP_FISHER`:

| cell `(n_s,k_s,a)` | `k-1` | `a^2/n` | `GAP_FISHER` | `RATIO_CAP` | fields `q = 1 mod n` |
|---|---|---|---|---|---|
| (8,4,5)   | 3 | 3.125   | **-0.125** (zero power) | 0.960 | 17, 41, 97 |
| (10,5,6)  | 4 | 3.6     | +0.4     | 1.1111 | 11, 31, 41 |
| (12,6,7)  | 5 | 49/12   | +0.9167  | 1.2245 | 13, 37, 61 |
| (16,8,9)  | 7 | 81/16   | +1.9375  | 1.3827 | 17, 97, 113 |
| (16,8,10) | 7 | 6.25    | +0.75    | 1.12   | 17, 97 |

Smallest rate-1/2 dimension with a positive gap is predicted to be
`k = 5` (`k = 4` fails by `-1` in the integer test).

### R6 — Predictions with numeric windows

- **PR-1** `94,323,185,676` reproduced exactly (A).
- **PR-2** `RATIO_CAP` at razor in `[1.9389, 1.9390]` (point 1.938935),
  and `RATIO_CAP -> 2` as `k -> inf` with `s = o(k)`.
- **PR-3** `RATIO_FAR` at razor in `[1.9692, 1.9693]`.
- **PR-4** `m_P <= 2` exactly, for a line whose core is at `a^2/n`.
- **PR-5** single-pencil subclass margin `= 128 - log2(n-a+1)` in
  `[88.0, 88.1]` bits (point 88.02), with `n-a+1 = 1,082,331,758,593`.
- **PR-6** `T_MAX = 2^88.02` (line-degree residual threshold).
- **PR-7** the refutation construction succeeds at every registered
  positive-gap cell and FAILS at `(8,4,5)` — a two-sided prediction.
- **PR-8** `RATIO_CAP` monotone increasing along `s = 1`:
  `1.1111 (k=5) < 1.2245 (k=6) < 1.3827 (k=8)`, and the closed form
  `RATIO_CAP = 2k(k-1)/(k+s)^2` reproduces the razor value.
- **PR-9** `(2a-n)^2/a = 2^36/65` and `a/(2a-n) = 65/2` exactly.
- **PR-10** own-repo grep finds the MDS-Johnson threshold already
  banked (`rate_half_list_integer_johnson_safe_anchor`, per round-29
  D2); predicted **0** node files stating the `a^2/n` overlap cap as
  a target or hypothesis.
- **PR-11** predicted **0** `node.json` / `statement.md` files that
  consume T3/T5; the only consumer is a round-29 pilot REPORT. If so,
  "the safe half of RH-AC is one inequality" is a pilot-level claim
  with no node-level consumer, and I will say so.
- **PR-12** `549,621,596,161 = a(n-a)/n + 1` exactly (B).
- **PR-13 (miss-likely, registered)** I do NOT expect to close either
  half of RH-AC, and I do NOT expect to produce an unconditional
  `B_ca^far < 2^128`. I expect to hand forward LINE-DEGREE.

### R7 — Zero-power declarations, made in advance

- `MAXCONSTRUCT` is a **lower** bound on the true max overlap.
  Constructions can REFUTE a cap; they have **zero power** to
  establish one. I will not report any constructed maximum as an
  upper bound.
- **No exhaustive search over far pairs `(y_1,y_2)` is inside the
  compute law at any positive-gap cell**: the space is `q^(2 n_s)`,
  `>= 11^20 = 6.7e20` at the smallest such cell. Any "max over
  configurations" I report is over a *structured family I built*, and
  I declare that scope at the point of use.
- No mean/random-word/density quantity enters any verdict. Route (b)
  of round-29's collinearity pilot (character sums) is not taken.
- Any claim about `q`-dependence needs two fields; single-field
  numbers are controls only.
- If the far-CA definition in the repo turns out to bound the pair
  agreement at a threshold *other* than `a`, (E-PEN) may fail; I
  register that branch now rather than reinterpreting later.

### R8 — Compliance plan

Every interpreter invocation via `tools/ramguard tiny|local -- python3`
from the repo root with an explicit `RAMGUARD_TIMEOUT`; `dag.json`
never opened (node.json shards + grep only); writes confined to
`notes/pilots_20260810/rh_overlap_cap/`; `CAMPAIGN_LEDGER.md` never
opened; the three sibling round-31 directories never read or listed;
no path containing `prize-codex-` touched; no git, no network, no
subagents; banked scripts only from scratch copies. Misses first in
the report; every quantifier claim quoted `file:line`.
