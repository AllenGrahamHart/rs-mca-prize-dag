# R-L2: the e = m stratum is NONEMPTY at m = 2 (witness theorem)

- **status:** PROVED (witness-checkable existence). The counting statements
  attached below are separated by status.
- **closure:** explicit certified witnesses
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/l2_nonempty_theorem/`, coordinator
  line-audited; the a* convention flag below is RESOLVED (round-38 ruling).

## The theorem

> There exist `(4m+1) x 4m` syndrome Hankel pencils with minimal index
> **exactly** `m = 2`, generic rank `4m-1 = 7`, `s = 0`, `delta = m-1 = 1`,
> and independent `Q_0, Q_1, Q_2`.

Twelve such objects are certified over five fields
`q in {97, 193, 257, 641, 769}`. Existence is witness-checkable, so **this
part is a THEOREM**: the emptiness route to the strict endpoint is dead at
`m = 2` constructively.

## The certificate (the published q = 97 object; replayed from scratch)

```text
Q_0 = [7,10,78,31,43,62,29,22]
Q_1 = [80,88,69,63,34,94,70,62]
Q_2 = [80,4,73,12,82,59,47,1]
y_0 = [77,90,33,0,95,81,25,10,92,6,84,21,86,26,40,74]
y_1 = [1,20,62,91,3,28,56,71,93,78,43,53,86,96,93,1]
```

with `M(Z) = M_r(y_0) + Z M_r(y_1)`, `M_r(y)[a][b] = y[a+b]`, `9 x 8`, and
`Q_Z = Q_0 + Z Q_1 + Z^2 Q_2`. Verified: degrees `(7,7,7)`; separation rank
`3` (`m+1`, as (RNC2) requires); `s = 0`; `M(Z)Q_Z = 0` entrywise;
`nullity(36x32) = 1` with `(y_0,y_1)` spanning that kernel; generic rank `7`;
a single finite rank drop at `z = 10` to rank `6` and **no** drop at
infinity; **no** kernel vector of parameter degree `<= 1`, so the minimal
index is exactly `e = m = 2`.

## (D-B) — the congruence criterion

```text
nullity(36x32) = 10 - rank(Phi),
Phi : (f,g) |-> (Q_2 f - Q_1 g mod Q_0,  Q_1 f - Q_0 g mod Q_2),   14 x 10,
```

for `(f,g)` of degree `<= 4`. Verified on the witness and on `60/60` fresh
pairwise-coprime squarefree random curves over `q = 97, 193`.

## (D-F) — the inversion

For fixed `B = (f,g,h,k)` the cleared system is a **square** `24 x 24` in the
curve, so existence is the ONE condition `det M(B) = 0` — hit rate `~1/q`
against `q^-5` blind. **`m = 2` accident:** at `m = 3` the same clearing gives
`80` equations on `48` for fixed `B`; a new inversion is needed. [Since round
36, the rate-1 (PAR) parametrization — sibling node
`rate_half_l2_stratum_rational_parametrization` — supersedes (D-F) as the
construction instrument; the witness theorem is unaffected.]

## The counting corrections (the round's forced re-pricing)

- **The `+4` was NEVER the existence count.** The equation-count excess
  `4m^2-7m+2 = -1, +4, +17, +38` at `m = 1,2,3,4` is not an existence
  codimension.
- **The honest count.** Determinantal codimension `(36-31)(32-31) = 5` in the
  `23`-dimensional projective curve space, so the expected dimension is
  `11m-4`, **positive at EVERY `m >= 1`**; at `m = 2` it is `18 = 23-5`,
  matching the independent measurement.
- **The excess component.** Curves with a planted common root have
  `nullity = 2` (verified `24/24` here, `40/40` per field in the source) and
  form a family of dimension `3*7-1+1 = 21` — the round-34 incidence count
  `19` is contaminated by it. The good component has dimension exactly `18`.
- Consequence: **the emptiness route is dead at `m = 2` constructively and
  expected-dead at every `m` by the `11m-4` count.**

## The stake, as re-priced by the coordinator

The PROVED background node
`rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion` already
excludes every strict `A=3`, `e=m` ENDPOINT PROFILE on even rows `m >= 6`,
including the official `m = 2^37` row. R-L2's emptiness branch was therefore
never the decisive route to the official endpoint; its value is the
structural small-`m` content, which the witnesses deliver. The witness
(`m = 2`, `T = 0`) is outside that node's hypotheses on both counts — **no
contradiction**.

## Where the difficulty went (undiminished)

All witnesses have `T = 0`; not one locator splits completely over `F_q`; the
root-count histogram matches the Poisson(1) law of random degree-7
polynomials to within noise. **Having a syndrome pencil buys NOTHING at the
splitting layer.** The gate of record moved to (SAT3)-on-(L2).

## CONVENTION FLAG — RESOLVED (round-38 coordinator ruling: PROJECTIVE)

The banked witness line records `a* = w* = min_{g != g'} |S_g u S_g'| = 13`.
That value is reproduced **only under the projective reading**, in which each
pencil member is read as a form of degree exactly `rho = 7` on `P^1`, so a
member of affine degree `7-t` carries `t` roots at infinity and
`|S_g u S_g'| = 14 - (deg gcd of finite parts) - min(7-deg_g, 7-deg_g')`.
Under the affine reading (`|S_g| = deg_g`) the same witness gives
`a* = 12`. This verifier computes BOTH and asserts the projective value.
[RESOLVED at wiring, 2026-08-11: the drafting pilot's D1 flag was accepted
as a genuine ambiguity in round 37, and round 38's Cauchy-lattice bank
issued the ruling — the convention of record is PROJECTIVE (roots at
infinity counted), which reproduces the banked 13; the ruling was
additionally proved OPERATIONALLY INERT on supported pairs (a* = 2rho on
every s = 0 two-slope object, either convention's difference vanishing
there). The round-35 F1 sentence is convention-sensitive and is to be read
projectively.]

## Scope

- Five prime fields is **not** a lift to `Z` and **not** a `q ~ 2^128`
  statement.
- The witnesses satisfy the pencil-intrinsic half of (SAT1) and **NONE** of
  (SAT2)-(SAT5) (vacuous at `T = 0`, not verified).
- The `m >= 3` branch of R-L2 is untouched.
- Blind (L2) search is banned at every `m` (`q^-5`); use the inversion — or,
  after round 36, the rate-1 parametrization (sibling node
  `rate_half_l2_stratum_rational_parametrization`).
- F1 was exercised only weakly; **(NEWCAP) remains at ZERO POWER.**

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:3526-3604`
  (Round-35 R-L2 addendum, 2026-08-11, coordinator-audited; round 35 bank 1,
  pilot `r35_l2_gate`). Coordinator-independent verification recorded at
  ibid. :3528-3534.
- Witness bank: `notes/pilots_20260811/r35_l2_gate/d2_results.txt:9-31`.
- Model: `notes/pilots_20260811/r35_l2_gate/d1_structure.py:6-9`;
  (D-B) shape: ibid. :160-172.
- Deficit row and codimension:
  `notes/pilots_20260811/r35_l2_gate/d1_results.txt:34-44`.
- Re-priced stake: statement.md:3560-3572.
- The a* ruling: A1's round-38 Cauchy-lattice addendum.

## Replay

```text
tools/ramguard local -- python3 \
  background/nodes/rate_half_l2_stratum_nonempty_at_m_two/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_l2_stratum_nonempty_at_m_two/verify_audit.py
```
