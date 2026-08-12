# FABLE_AUDIT — r35_bivcurve_m4 (round 35, bank 3/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — m = 4 stays OPEN, but the round-34 obstruction
attribution is CORRECTED (measured inert), the m=5 parity
falsifier FIRED, the ceiling is re-graded soft (7 -> 9), and
(OUT-m) is refined to an exact identity (adopted).** Node work:
CORRECTED marker on the round-34 m=4 bullet + the round-35
(BIV-CURVE) m=4 addendum. No status flips; census unchanged.

## Verification

- Results files consistent with every headline number: the
  ablation table (V1 = V2 = 7 at q=193 with interior-only
  histogram differences; m=5 FULL and NO-PAIRCAP histograms
  BIT-identical; V3/NO-SLOPES 12/12 and 15/15 in all draws), the
  m=3 positive control (9/9 both fields), the ALLOC-A 9-of-12
  ceiling, the disc-square rates.
- **Hand-checks:** (1) the Z_12 certificate — differences of
  {0,1,3} are +-1,+-2,+-3, all distinct mod 12, so translates
  meet in <= 1 residue (linear); each residue lies in translates
  i, i-1, i-3 (3-regular); i in T_i gives an SDR — VERIFIED.
  (2) Route (b) derivation — invariants of x -> c/x are F_q(w),
  w = x + c/x, [F_q(x):F_q(w)] = 2, so deg_x <= 3 invariant =>
  deg_w <= 1 => Möbius in w => injective on w-values = orbits —
  SOUND (and machine-confirmed 167/167, 177/177). (3) The
  (OUT-m) aggregate identity — sum_g eps~_g = sum_x def(x)*t_x is
  a double count; t_x = m-def / m-1-def / m-2-def by placement —
  VERIFIED (and the m=3 witness attains (m-1)(1+O) exactly,
  reproducing my round-34 catch as an equality). (4) (DEG-m)
  algebra and the middle budget sum X'' = (m-1)(m-2) — VERIFIED.
  (5) D(m) = 3m(m-1)-(rho-1) = 8, 22, 42 — CHECK (the rho-vs-rho-1
  off-by-one against round 34's 21 honestly reported as R10.1).

## Audit catch

**R2.3 is over-broad.** "A sigma-stable set of odd size needs an
odd number of fixed points [in the set]" is correct, but the
pilot's inference from "#Fix is even (0 or 2)" to "no involution
makes W sigma-stable at even m" fails on the c in mu_32 branch:
#Fix = 2 admits a stable odd set containing exactly ONE fixed
point. The inference is valid only when #Fix = 0 (sigma(x) = -x,
and c/x with c not in mu_32). Impact LOW: the route-(b) refutation
is carried by the injectivity derivation (sound), and the searched
ceiling (7) is independent. Qualifier applied in the addendum —
the FALSE-inference class, caught before banking.

## Assessment

- The ablation is the right instrument and its conclusion is
  clean: my round-34 addendum's obstruction attribution ((OV) ->
  linear hypergraph) was WRONG as a mechanism — real, proved, and
  inert. Corrected with a marker, not silently.
- My own round-35 brief's route-(b) hypothesis ("changes exactly
  that term — fixed points!") is refuted at derivation level.
  Coordinator brief error, recorded in the addendum. That is two
  coordinator texts corrected by this bank — the audit cadence
  running in both directions, as designed.
- The demand-vs-flat-supply law replacing parity is honest about
  its status (measured, not proved) and unifies the m=3 cost
  observations retroactively.
- MISS 2 (the dead mindeg parameter, self-caught and re-run) and
  MISS 6 (the starved cells re-run individually) are the pilot
  audit machinery working; MISS 12 (one dag.json grep traversal,
  filename only) is a light RAM-clause deviation — round-36
  CONSTRAINTS will add --exclude=dag.json to the standard flags.

## Compliance

Compute law CLEAN 9/9 (zero bare python3 — 7th consecutive clean
pilot). Write discipline CLEAN under the upgraded clause (banked
scripts copied by cp before use per the brief; none executed —
honestly declared, with the consequence that nothing this round is
gated by bank 2's verifier). Quarantine CLEAN (parent dir never
ls-ed — the exact fix the l2_gate bank asked for, adopted
independently). Registrations followed; the two registration
weaknesses reported as outcomes.

## Mint queue additions

1. The (OUT-m) node upgrade: the aggregate identity
   sum eps~ = sum def(x)*t_x + the three placement charges +
   (DEG-m) with its middle budget (all inheriting POSED status).
2. The m=4 scope table (five searched-negative classes with
   budgets) + the demand/supply law D(m) = 3m^2-7m+2 vs flat.
3. The (QUAD-4) line for the (SPLIT-m) template node (14-vs-10
   parameters, disc-square rate, half-orbit-pool cost).
4. The even-m budget-waste lemma (invariant factors have even
   x-degree => one unit of 3m-3 lost in every sigma-symmetric
   ansatz).

## Round-36 anchors fed by this bank

The general non-split m=4 probe (no sigma, no Q*L — the one
untouched class); the arithmetic value-confinement layer as its
own object (the flat-supply mechanism); (DEG-m)-tightened
searches (round 34's ceiling was on a relaxation).
