# FABLE_AUDIT — r37_third_solve (round 37, bank 4/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — the third-solve question answered in the
negative with a STRUCTURAL reason (the two-slot ladder); (SCRIT),
(CONIC)/(SLOT) and (OV4) adopted (all hand-verified); the
round-36 handoff RE-POSED and the "no predictive criterion" line
RESOLVED; T = 4 bespoke accepted first-in-class with its zero-
(SAT3)-power scoping.** Node work: two markers on the round-36
(SAT3)-on-(L2) addendum + the round-37 third-solve addendum +
ROUND 37 CLOSE. No status flips; census unchanged.

## Verification (hand-checks, all pass)

1. **The cross-product form:** row_0 x row_1 of [[k,f,g],[f,g,-h]]
   = (f(-h)-g^2, gf-k(-h), kg-f^2) = -(g^2+hf, -(fg+hk), f^2-kg)
   = -L*(Q_2, -Q_1, Q_0) — EXACT, by hand. E1/E2 orthogonality of
   a cross product to its rows is the right reading of round 35's
   identities.
2. **(CONIC):** both sides expand to (f^2g^2 - kg^3 - hkfg +
   hf^3)/L — EXACT, by hand. (SLOT) follows by evaluation.
3. **(SCRIT):** at x in S_0 ^ S_2 with fg != 0: LQ_0 = 0 gives
   k = f^2/g; LQ_2 = 0 gives h = -g^2/f; then LQ_1 = fg + hk =
   fg - fg = 0 — four lines, EXACT. The f=g=0 exception (1/58 +
   1/59 measured) is the same species as (RES)'s and is honestly
   hypothesised.
4. **The slot argument:** u_0 fixed by Q_0; u_3 fixed uniquely by
   Q_2 (200/200 injectivity is the right check); Q_1 = the third
   minor — no polynomial freedom remains. The Cauchy deficit
   14 - (4+4+1) - 2 = 3 — CHECK. The S_3 re-basing symmetry
   argument is sound: no base choice creates a slot.
5. **(OV4):** shared roots of a third member with S_0 u S_inf =
   roots of f+zg there (via (SLOT)); deg <= 4; the f+zg == 0
   degenerate branch correctly excluded at s=0. The sharpening
   e(k,i) <= 3 (deg k <= 4 < 6 forcing) checks. The banked-design
   pass (simple graph, worst pair-sum 2) is verified honestly —
   the pilot's own MISS 5 gets the grading right: a filter, not
   an exclusion.

## Assessment

- The negative is the strongest kind: not "I failed to find the
  solve" but "the parametrization has exactly two solvable slots,
  and here is the algebra." The re-posed open item (the
  rank-deficient 14x10 Cauchy solve) is correctly pointed at the
  banked l1/xr Pade-lattice machinery — a genuine cross-lane
  transport opportunity.
- (SCRIT) converts round 36's 42/46 mortality into a free
  combinatorial filter — with the bespoke double solve (101x/62x)
  these are the two instruments any future push uses.
- The honesty ledger is exemplary even by campaign standards:
  (X8) refuted by its own arithmetic and reported FIRST; the
  mu_32 tie stated as a tie; the T=4 record scoped against the
  banked out-of-class T=4 before the number; the truncation bug
  preserved in the append-mode results file and cited.
- The resumed-pilot protocol worked: the size-capped re-run was
  clean (6/6 ramguard, no breach, report under the cap).

## Compliance

Compute law CLEAN 6/6 (the resumed pilot; streak at 2 for the
round's clean pilots). Write discipline clean; the three-part
registration append (harness size rule) is the right adaptation.
Results-file rules held AND paid (the failed d2 run preserved =
MISS 8 visible). Anti-import pattern used. Quarantine exemplary.
P16 (replaying round 36's exact vectors) honestly declared
unmeasured rather than silently skipped.

## Mint queue additions

1. The two-slot ladder theorem ((PAR) as 2x3-Hankel minors; the
   exactly-n-prescriptions-per-length-(n+2) lesson; the Cauchy
   re-pose).
2. (SCRIT) + the restricted-subset operational rule.
3. (CONIC)/(SLOT).
4. (OV4) as a necessary-condition filter node (with the
   banked-design pass recorded).
5. The bespoke double solve as the standard instrument.

## Round-38 anchors fed by this bank

The Cauchy-lattice solve attempt (l1/xr machinery import); the
(OV4)-filtered design search (does any concentrated design
matter?); the a* ruling (still gating F1).
