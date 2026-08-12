# PREREG — r37_third_solve (round 37)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r36_sat3_on_l2/REPORT.md` (round 36)
2. `notes/pilots_20260811/r35_l2_gate/REPORT.md` (round 35)

## Mandate

THE THIRD EXACT SOLVE — the single named instrument of the
converged question. Round 36 rationally parametrized the whole
e=m=2 (L2) stratum ((PAR): L*Q_0 = f^2-kg, L*Q_1 = fg+hk,
L*Q_2 = g^2+hf, two conditions at ell) and achieved T = 2 over
mu_32 by exact algebra: prescribing Q_0 split = a square root mod
g; prescribing Q_2 too = one proportionality in F_q[x]/(f). The
T = 3 cell sits at +62.5 bits AT EVERY FIELD (the 18-6T exponent
vanishes at T = 3) and no exact solve reaches it — the failure is
algorithmic, not arithmetic. YOUR JOB: find the third exact solve
— or prove the third prescription is structurally different and
name what replaces it. Every T >= 3 object over mu_32 is the
first of its kind; if T climbs past 3, the ledger exponent goes
negative and you are probing the first genuine
emptiness-mechanism territory in the lane ((SAT3) itself sits at
T = 9 = the packing ceiling).

## Deliverables

**D1 — THE THREE-MEMBER SYSTEM, STRUCTURED.** With Q_0 and Q_2
prescribed split (the (PAR) coordinates fix f, g, k up to the
solved conditions), a third member at slope z_3 is
Q_{z_3} = Q_0 + z_3 Q_1 + z_3^2 Q_2 with Q_1 = (fg+hk)/L — and h
still carries free coefficients. Derive exactly: what does
"Q_{z_3} splits over mu_32 (or a designed 32-set)" cost in the
remaining freedom (h's free coefficients + the choice of z_3 +
any residual scaling)? Is it another ring-proportionality (an
exact solve exists), a norm-type condition (partially exact), or
generic (search only)? The answer, either way, is the
deliverable. Consider ALSO re-basing: (PAR) is symmetric under
Möbius in z — prescribing members at z = 0, 1, infinity may make
the third condition cleaner than 0, infinity, z_3.

**D2 — THE PUSH.** Execute the best instrument from D1 at two
fields: exact solve if it exists, else the sharpest structured
search seeded by the T = 2 exact objects (their h-fibres are the
natural search space). Track T over mu_32 as the objective;
full certification table (e = m = 2, s = 0, generic rank 7,
nullity, entrywise M(Z)Q_Z = 0) for every T >= 3 object; push to
T = 4 if T = 3 lands (the first negative-exponent cell). Also:
the s != 0 degeneracy criterion (42/46 of round 36's exact
solutions died there — find the predictive test; round 36's
rigid pattern s=k => nullity 2k is the lead).

**D3 — THE MECHANISM QUESTION.** If a wall appears: is it
eigenvalue-confinement (the 2x2 pencil P(x)+zR(x) reading — the
occupancy/concentration functionals round 36 defined), and can
it be stated as an exact constraint (the lane's first genuine
mechanism)? If NO wall appears through T = 4: state honestly
that the counting instruments are failing in the direction of
EXISTENCE and what that means for the (SAT3) class question.

**D4 — VERDICT.** The T-record with provenance; the
solve-vs-search status of the third prescription; misses first;
cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(a third exact solve exists), P(T >= 3 over mu_32 this round),
P(T >= 4), P(a genuine mechanism/wall is named), expected max T
(a number), P(the s != 0 criterion found).

## Pilot registrations

Registered after reading EXACTLY the two named anchors
(`r36_sat3_on_l2/REPORT.md`, `r35_l2_gate/REPORT.md`) and BEFORE
any other read, any grep, any `ls`, and any interpreter
invocation. Appended with the Edit tool in three parts (harness
size rule); no post-registration addenda.

### R0 — notation taken from the anchors alone

`m=2`, `rho=4m-1=7`, `N=16m=32`, `R=16`, `A=R+1-2rho=3`,
`D=mu_32`, `e` = minimal index, `s = deg gcd(Q_0,Q_1,Q_2)`,
`delta = rho-3e`, `T` = number of slopes `z in P^1` whose locator
`Q_z` splits into 7 distinct roots in the domain, `T_target =
rho+2 = 9`. (PAR): `L Q_0 = f^2-kg`, `L Q_1 = fg+hk`,
`L Q_2 = g^2+hf`, `deg f,g,h,k <= 4`, `L` linear with root `ell`,
two conditions at `ell`. Ledger: `log2 E(T) = 18 log2 q +
log2 C(q+1,T) + T[log2 C(32,7) - 7 log2 q]`, exponent `18-6T`.

### R1 — execution order (committed in advance)

D1 (structure of the third condition, incl. the Möbius re-basing
at `z in {0,1,infinity}`) -> D2 (push at two fields, `q=97,193`;
`s != 0` criterion) -> D3 (mechanism/wall or honest existence
statement) -> D4 (verdict). Reported in that order regardless of
which deliverable kills which.

### X — falsifiable derivations, each with its falsifier

- **(X1) THE THIRD-MEMBER SHAPE.** With `Q_0` and `Q_2`
  prescribed, `Q_1 = (fg+hk)/L` is ALREADY DETERMINED by
  `(f,g,k,h,L)`, and `h` is the only remaining freedom (`k` is
  forced by `k = (f^2-LQ_0)/g`). Therefore
  `L Q_{z} = (f+zg)^2 - (k-z^2 h)(g - z f)`... — I register the
  weaker committed form: `L Q_z = det(P+zR)` with
  `P=[[f,k],[g,f]]`, `R=[[g,f],[-h,g]]`, so
  `L Q_z = (f+zg)^2 - (k+zf)(g-zh)`. **Falsifier:** expanding
  this in `z` fails to reproduce `f^2-kg`, `fg+hk`, `g^2+hf` as
  the `z^0,z^1,z^2` coefficients on at least one random draw.
- **(X2) DEGREES OF FREEDOM IN `h`.** After prescribing `Q_0`
  (fixes `f,g,k` up to the square-root/`c g` choices) the residual
  freedom is: `h` has 5 coefficients minus 1 used by the `ell`
  condition `g(ell)^2 = -h(ell) f(ell)` = **4 free**, plus the
  choice of `z_3` (1 parameter, but discrete over `F_q`), plus
  scaling. Prescribing `Q_2` split consumes 3 of those 4 (the
  proportionality in `F_q[x]/(f)`, a 4-dim ring, mod scale).
  **Registered count: after two prescriptions the residual `h`
  freedom is 4-3 = 1 dimension (plus scale).** A third
  prescription needs 3 more conditions against 1 remaining
  dimension => **deficit 2**. **Falsifier:** the measured
  dimension of the `h`-fibre of a fixed `(S_0,S_2)` exact
  solution is not 1 (projectively 0-dimensional after scale) at
  either field.
- **(X3) THE THIRD CONDITION IS NOT A RING PROPORTIONALITY.**
  Because `Q_1` is determined and `Q_{z_3} = Q_0 + z_3 Q_1 +
  z_3^2 Q_2` with `Q_0,Q_2` already fixed as products over
  `mu_32`, the third member is an AFFINE-in-`z_3` pencil through
  two FIXED polynomials, so "splits over `mu_32`" is a condition
  on the single scalar `z_3` (plus the 1-dim `h` residue), not on
  a free degree-7 form. **Registered verdict: the third
  prescription is NOT another exact solve of the same species; it
  is a norm/root-counting condition, i.e. partially exact at
  best.** **Falsifier:** I exhibit an exact solve (a closed-form
  construction with hit rate bounded below independent of search)
  for a third split member.
- **(X4) THE `z_3` COUNT.** With `Q_0,Q_2` fixed and `h` on a
  1-parameter residue, the number of `(z_3, h)` making `Q_{z_3}`
  split over `mu_32` has expectation `~ (q+1) * q * C(32,7)/q^7 =
  (q+1) q * 5.19e-8` at `q=97` = **4.9e-4**, i.e. **essentially
  zero per exact `(S_0,S_2)` solution**. Summed over the 46 (resp.
  13) exact solutions of round 36: `~0.02` at `q=97`. **Registered
  prediction: the T=3 push from the round-36 T=2 objects' own
  h-fibres has expected yield << 1 and will FAIL.** **Falsifier:**
  a `T=3` object over `mu_32` emerges from that fibre.
- **(X5) THE RE-BASING IS THE RIGHT MOVE.** Prescribing at
  `z in {0,1,infinity}` means prescribing `Q_0`, `Q_2` and
  `Q_0+Q_1+Q_2` split. Under (PAR) with `Q_1=(fg+hk)/L`, the
  member at `z=1` is `L Q_1' = (f+g)^2 - (k+f)(g-h)`, i.e. the
  SAME determinantal shape with `(f,g,h,k) -> (f+g, ?, ?, ?)`.
  **Registered claim: the three-member problem at `{0,1,infinity}`
  is a system of THREE simultaneous "square root mod g"-type
  conditions on ONE parameter set, and its symmetry group is the
  `S_3` of Möbius maps permuting `{0,1,infinity}`.** **Falsifier:**
  the `z=1` member does not admit the same `f^2-kg` shape in
  re-based coordinates.
- **(X6) THE `s != 0` CRITERION.** Round 36 measured `s=k =>
  nullity 2k`, generic rank `k`, `deg<=1` kernel `16-2k`
  (`r36_sat3_on_l2/REPORT.md:38`). **Registered criterion:
  `s = deg gcd(Q_0,Q_1,Q_2) = deg gcd(f^2-kg, fg+hk, g^2+hf) -
  deg L`, i.e. `s != 0` exactly when the three (PAR) numerators
  share a root BEYOND `ell`** — the (RES) resultant criterion of
  round 36 with `L` divided out. It is therefore PREDICTABLE
  BEFORE building `Q`: compute `gcd` of the three numerators;
  `s = deg gcd - 1`. **Falsifier:** on the exact `mu_32`
  solutions, `deg gcd(numerators) - 1` disagrees with the measured
  `s` on any instance.
- **(X7) THE `s != 0` SOURCE IN THE MEET-IN-THE-MIDDLE.** The 42/46
  degenerate solutions arise because the proportionality
  `L Q_2 == g^2 (mod f)` is solved in `F_q[x]/(f)` WITHOUT
  requiring `gcd(Q_2, f) = 1`; a common root of `Q_2` and `f`
  forces a common root of `f^2-kg` and `g^2+hf` off `ell`.
  **Registered predictive test: `s != 0` iff `gcd(Q_2, f) != 1`
  (equivalently some `b in S_2` is a root of `f`), and then
  `s = deg gcd(Q_2,f)`.** **Falsifier:** any instance where
  `deg gcd(Q_2,f) != s`.
- **(X8) THE COUNT AT `T=3` IS NOT ACHIEVABLE BY MY BUDGET.**
  `T=3` over `mu_32` is `+62.5` bits `q`-independently
  (`r36_sat3_on_l2/REPORT.md:88-92`), but the abundance is over the
  FULL 18-dimensional stratum; my instruments reach only the
  codim-14 sub-locus where `Q_0,Q_2` are prescribed. On that
  sub-locus the expected `T=3` count is `18-7-7 = 4` dims of
  freedom against 7 more conditions => `4-7 = -3` dims, i.e.
  `q^{-3} C(32,7) ~ 2^{21.68-19.8} = 3.7` at `q=97` PER
  `(S_0,S_2,S_3)` TRIPLE but only `~q^{-3}·C(32,7)` summed
  differently... **Committed number: expected number of `T>=3`
  objects reachable from a FIXED `(S_0,S_2)` exact solution over
  all `S_3` and all `z_3` and the 1-dim `h` residue is
  `C(32,7)·(q+1)·q/q^7 = 2^{21.68}·98·97/97^7 = 1.6e-6` at
  `q=97`.** **Falsifier:** yield exceeds 1 in the fibres I scan.
- **(X9) WHAT REPLACES THE THIRD PRESCRIPTION.** If (X3) holds,
  the structurally different object is: **do not prescribe a third
  SET; prescribe a third ROOT PATTERN.** Concretely, use the
  packing/(SAT4) direction — demand that the third member share
  roots with `S_0 u S_2` (round 36 measured `|union| < 3·7`
  spontaneously, `REPORT.md:146-149`), which converts a
  codimension-7 set condition into a smaller one. **Registered
  claim: the third prescription's natural replacement is a
  SHARED-ROOT (deficit) condition, not a split condition, and this
  is exactly the `(SAT4)` deficit identity turning on for the
  first time.** **Falsifier:** shared-root prescription is no
  cheaper than the free one in the measured yield.

### P — numeric priors (blind; the brief's six are P1-P6)

- **P1** a third EXACT solve exists (closed form, rate bounded
  below independent of search) = **0.15**
- **P2** `T >= 3` over `mu_32` achieved this round = **0.22**
- **P3** `T >= 4` over `mu_32` achieved this round = **0.03**
- **P4** a genuine mechanism/wall is NAMED (an exact constraint,
  not a measured functional) = **0.25**
- **P5** **expected max `T` over `mu_32` this round = 2**
  (i.e. I expect to TIE round 36, not beat it). **P5a** expected
  max `T` over a bespoke 32-set = **3** (tie). **P5b** expected
  max `T` over `mu_32` under the `{0,1,infinity}` re-basing = **2**.
- **P6** the `s != 0` predictive criterion is FOUND and verified
  = **0.70** (it is (X6)/(X7), and both are one gcd)
- **P7** (X1)'s determinantal expansion verifies with no
  correction = **0.80**
- **P8** (X6) is the right criterion (gcd of numerators) = **0.60**
- **P9** (X7) is the right criterion (`gcd(Q_2,f)`) = **0.55**
- **P10** the re-basing at `{0,1,infinity}` makes the third
  condition strictly cleaner than at `{0,infinity,z_3}` = **0.35**
- **P11** at least one of my headline structural claims is
  already banked in-repo (CATCH-24A subtraction fires
  load-bearing) = **0.75**
- **P12** the `18-6T` exponent / `+62.5` bits at `T=3` reproduces
  exactly from my own arithmetic = **0.90**
- **P13** I find a `T=3` object over a BESPOKE 32-set (tying
  round 36) = **0.60**
- **P14** the third-member condition turns out to be a NORM
  condition in a quadratic/quartic extension (partially exact)
  = **0.30**
- **P15** at least one ramguard run fails (timeout or memory)
  = **0.35**
- **P16** I reproduce round 36's exact `T=2` `mu_32` witness
  (the published `q=97` coefficient vectors certify) = **0.85**
- **P17** the count `+62.5` at `T=3` is misleading because the
  prescribed sub-locus is codim 14 (my (X8)) = **0.65**

### R4 — MISS-2 GUARD (mean-vs-max), four clauses, binding

(i) **A sample maximum is never a bound.** Every `max T` I report
is the maximum over the constructions I actually ran; I will
never write "T cannot exceed" from a measured max, and every
`max`-quantified sentence carries its denominator.
(ii) **Every `T` is reported with its FULL DISTRIBUTION**, not
only its max — histogram over the population scanned.
(iii) **Asymmetric power:** a witness has full power (existence is
witness-checkable); a null has power only against the rate
actually sampled, and I will state that rate.
(iv) **Mean-vs-max on the ledger:** `log2 E(T)` is a FIRST MOMENT
(a mean). A positive first moment does not imply a witness
exists, and a negative one does not imply emptiness — the
`pb_design_ceiling/proof.md:125` blind spot. I will not convert
`+62.5` bits into "T=3 exists" nor a negative cell into
"T is impossible" anywhere in the report. Specifically: round 36
read `+62.5` as "abundant"; my (X8) registers in advance that the
mean over the FULL stratum says nothing about the reachable
sub-locus, and I will report the sub-locus count separately.

### R5 — zero-power pre-declarations

1. **Bespoke-domain results have ZERO POWER for `(SAT3)`, the
   strict endpoint, or the official row.** The endpoint's domain
   is `mu_N`; a designed non-multiplicative 32-set is a
   relaxation. I will never merge the two columns.
2. **A failure to reach `T=3` over `mu_32` has ZERO POWER against
   the existence of `T=3` objects** — it is absence at the rate I
   sampled, on a codim-14 sub-locus, not absence in the stratum.
3. **Two fields (`q=97,193`) is not a theorem over `Z` and not a
   statement at `q ~ 2^128`.** No Lang–Weil, no lift.
4. **Nothing this round bears on `m >= 3`** — (PAR) is
   `m=2`-specific (`r36_sat3_on_l2/REPORT.md:210`) — nor on
   `Rout`, the `9/4` or `7/4` ledgers, FR-canonical, or layer A.
5. **Any counting excess refutes nothing** (R4(iv)).
6. **F1/(NEWCAP) is at zero power below `T=3`**: with `T=2` there
   is one supported pair and `a*` is a single number
   (`r36_sat3_on_l2/REPORT.md:42`). I will declare it zero-power
   unless `T >= 3` lands with `>= 3` supported pairs.
7. **`s != 0` criterion power:** if (X6)/(X7) verify, they verify
   on the exact solutions I can regenerate, a specific and
   reported denominator — not on the stratum.
8. **If NO wall appears, that is not evidence of existence
   either.** Per the brief's D3 second horn I will state the
   direction honestly and declare its power explicitly.
9. **Möbius re-basing is a change of coordinates, not a
   discovery**; any `T` gained by it must be re-certified from
   scratch against the ORIGINAL `36x32` system.

### R6 — CATCH-24A subtraction plan (before ANY novelty claim)

Recursive greps over `background/`, `critical/`, `notes/`, each
carrying at the SEARCH level `--exclude-dir=r37_urand
--exclude-dir=r37_share3_gap --exclude-dir=r37_mint_drafts
--exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*'
--exclude-dir=.git --exclude-dir=__pycache__
--exclude=dag.json`. Hyphenated and infixed variants committed in
advance: `third prescription`/`third-prescription`;
`third member`/`third-member`; `shared root`/`shared-root`/
`root sharing`/`root-sharing`; `norm condition`/`norm-condition`/
`norm form`; `Mobius`/`Möbius`/`mobius`/`re-basing`/`rebasing`;
`gcd(Q_2,f)`/`gcd(Q_2, f)`; `eigenvalue confinement`/
`eigenvalue-confinement`; `deficit identity`/`deficit-identity`;
`0,1,infinity`/`{0,1,infty}`/`three-point normalisation`.

### R7 — expected misses (registered in advance)

(a) My `T`-record will most likely TIE, not beat, round 36's, and
I must headline that (P5 = 2).
(b) (X8) may itself be the round's real content — a NEGATIVE
structural finding (the prescribed sub-locus is too thin) — and I
must not dress a negative up as a wall (R5.8).
(c) I may find that the "third exact solve" question is
ill-posed as stated because `Q_1` is already determined by
`(f,g,h,k)`; if so, the mandate's premise needs re-posing and I
must say so plainly rather than manufacture a solve.
(d) The `s != 0` criterion is the most likely deliverable to
land, and it is the LEAST exciting one; I must not let it
displace the misses.
(e) Round 36's `+62.5` reading may be quoted by me
uncritically — R4(iv) exists to stop that.

