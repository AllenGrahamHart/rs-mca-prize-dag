# PREREG — r36_m4_nonsplit (round 36)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r35_bivcurve_m4/REPORT.md` (round 35)
2. `notes/pilots_20260811/r34_bivcurve_m34/REPORT.md` (round 34)

## Mandate

THE LAST m=4 CLASS + THE FLAT-SUPPLY LAW AS A THEOREM TARGET.
Round 35 relocated the (BIV-CURVE) m=4 obstruction to arithmetic
value-confinement (demand D(m) = 3m^2-7m+2 vs supply FLAT in m;
the (OV)/linearity layer is inert; the ceiling is 9 of 12 and
soft), refuted the parity prediction at m=5, and left exactly ONE
class untouched: **general non-split G with no sigma-symmetry and
no Q*L factorisation**. Two structural facts frame it: (i) the
general class has the FULL 3m-3 = 9 x-degree budget (every
sigma-symmetric ansatz provably wastes one unit — anchor 1's
even-degree lemma) and the full orbit pool; (ii) it loses tuple
sharing entirely UNLESS a non-involutive sharing pattern exists —
and the (OV) cap admits tuple multiplicity up to m-1 = 3 at m=4,
so ORDER-3 sharing (three points carrying one triple) is legal
where involutions only ever bought 2. mu_64 has no order-3
multiplicative action — the question is whether an order-3
sharing pattern exists WITHOUT a group action (the selection
layer is free; the cost is value-coincidences, and a 3-sharing
pattern cuts demand from 22 toward ~8, the m=3 crossing level —
derive the exact number BEFORE searching). Also mandatory: the
(DEG-m)-tightened search (rounds 34-35 ceilings were measured on
a RELAXATION — degree-1 slopes need middle support at m >= 4) and
the flat-supply law as a THEOREM attempt.

## Deliverables

**D1 — THE SHARING-PATTERN ARITHMETIC, DERIVED FIRST.** For a
k-sharing pattern (k points of S_g D S_h carrying one common
tuple, k <= m-1): the exact coincidence demand D_k(m), the
per-side and (OV) compliance conditions, and the constraint that
k=3 sharing imposes on G's structure (three points with the same
slope triple = a common cubic factor condition? a rational map
with 3-point fibres = degree-3 pencils reappear — but WITHOUT the
involution pairing, so which x-degree budget does it cost?).
Then: is there a G-ansatz realizing 3-sharing inside deg_x <= 9,
deg_Z = 3? Parameterize it exactly as anchor 2's (SPLIT-m) was.

**D2 — THE (DEG-m)-TIGHTENED m=4 SEARCH.** The TRUE selection
problem (degree-1 slopes require X'' >= 1 middle support; the
exact budget sum X'' = (m-1)(m-2) = 6). Run the general-nonsplit
and 3-sharing searches under the tightening, budgets and draw
counts matched to anchor 1's cells so ceilings are comparable.
Two fields. Report ceilings as ceilings (named class, named
budget).

**D3 — THE FLAT-SUPPLY LAW AS A THEOREM.** Anchor 1 measured
supply flat (8, 12, 9 achieved vs 8, 22, 42 demanded). Attempt:
for the PENCIL-IMAGE ansatz classes (values of <= c rational maps
of bounded degree on a fixed domain), PROVE a supply upper bound
o(m^2) — even a bound C*m log m would close (BIV-CURVE) for all
pencil classes at large m and re-derive the m=3 crossing. The
value-coincidence supply is a sum-of-fibre-collisions count over
bounded-degree maps on mu_N: this is Cauchy-Schwarz territory.
Grade honestly (a theorem for named classes, not "all G").

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record; whether
m=4 is now closed-for-all-named-classes or a witness landed;
misses first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(m=4 witness via general non-split), P(a legal 3-sharing
G-ansatz exists), P(the 3-sharing demand lands at or below the
m=3 crossing level), P(the flat-supply law provable for pencil
classes this round), P(the (DEG-m) tightening moves any ceiling).

## Pilot registrations

Appended with the Edit tool after reading EXACTLY the two named
anchors (`r35_bivcurve_m4/REPORT.md`, `r34_bivcurve_m34/REPORT.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation. Everything below is derived by hand, on paper, from the
two anchors only. No post-registration addenda will be made;
registration errors will be reported as outcomes.

### R0 — notation carried forward (from the anchors, not re-derived)

`m`, `N = 16m`, `rho = 4m-1`, `R = 8m`, `e = m`, `T = rho+2`,
`T_1 = 2`, `T_2 = rho`, `a = 7m-1`, `delta = m-1`;
`|S_g ^ S_h| = m-1`, `|S_g D S_h| = 6m`, `|W| = a`.
At `m=4`: `N=64, rho=15, T=17, a=27, |S_g^S_h|=3, |S_g D S_h|=24,
T_2=15, deg_x G <= 3m-3 = 9, deg_Z G = m-1 = 3`.
`X'_gamma = |S_gamma ^ (S_g D S_h)|`, `X''_gamma = |S_gamma ^ (S_g ^ S_h)|`.

### R1 — D1 THE SHARING ARITHMETIC, DERIVED BEFORE ANY SEARCH

**R1.1 (the exact demand, k-sharing).** Let the `6m` points of
`S_g D S_h` be partitioned into tuple-classes of size `k` (each class
carrying ONE common `(m-1)`-tuple of type-2 slopes) and the `m-1`
middles into classes of size `k'` (each carrying one `(m-2)`-tuple).
Distinct-tuple slope-SLOTS are then

```
slots(k,k') = 6m(m-1)/k  +  (m-1)(m-2)/k' ,
```

and since `T_2 = rho` exactly (forced by `T = rho+2`, `T_1 = 2`) and
`(OUT-m)` forbids `X_gamma = 0`, ALL `rho` type-2 slopes must be used.
Hence the **coincidence demand**

```
D(k,k') = 6m(m-1)/k + (m-1)(m-2)/k' - (4m-1).
```

CALIBRATION (registered as a check on the formula, not as a result):
`m=3, k=k'=2` gives `18 + 1 - 11 = 8`, which **reproduces anchor 1's
`m=3` demand 8 exactly** (`r35 REPORT.md:220-222`).

REGISTERED VALUES AT `m=4` (`k <= m-1 = 3` by the `(OV)` cap):

```
k=1 (no sharing)      : 72 + 6 - 15 = 63     (anchor-convention 58)
k=2 (involution)      : 36 + 4 - 15 = 25     (anchor-convention 22)
k=3 (this round)      : 24 + 2 - 15 = 11     (anchor-convention 10)
m=3 crossing level    :                  8
measured supply, m=4  :                 12   (r35 REPORT.md:221)
```

**R1.2 (I register a correction to anchor 1's demand row).** Anchor 1's
`D(m) = 3m(m-1) - (rho-1)` (`r35 REPORT.md:220`) charges the middle
tuples NO slope-slots and reserves them ONE slope. That is exact at
`m=3` (1 middle slot, 1 reserved slope — they cancel) and **undercounts
by 3 at `m=4`** (4 middle slots, 1 reserved slope). Registered
prediction: the true `m=4` 2-sharing demand is **25, not 22**, and the
true `m=5` 2-sharing demand is `60 + 6 - 19 = 47, not 42`. I report
both conventions throughout. `P(this correction is right) = 0.80`.

**R1.3 (the answer to the brief's question, registered as a NO).** The
brief conjectures 3-sharing "cuts demand from 22 toward ~8, the m=3
crossing level". **Derived: it cuts it to 11 (anchor-convention 10),
which is ABOVE the m=3 crossing level 8 and BELOW the measured m=4
supply 12.** So `P(3-sharing demand <= 8) = 0.03` (I have derived it;
this is registered as a pre-search derivation, not a prior), and
`P(3-sharing demand <= measured supply 12) = 0.92`.

**R1.4 (the ledger flips sign — the round's central registered claim).**
The `(SUPPLY-CODIM)` excess `E = supply - demand` at `m=4`:

```
(SPLIT-4)   supply 10  demand 25  E = -15   (anchor-convention -12)
(QUAD-4)    supply 14  demand 25  E = -11   (anchor-convention  -8)
(SHARE3-4)  supply 15  demand 11  E =  +4   <-- FIRST POSITIVE E AT m=4
```

`P(E > 0 for (SHARE3-4) under my parameter count) = 0.85`. R6 binds:
**a positive excess is NOT existence** (anchor 2's MISS 4, anchor 1's
MISS 3 — the supply proxy is measurably loose in BOTH directions).

**R1.5 (STRUCTURE THEOREM for k-sharing — derived, with a falsifier).**
Write `G(Z,x) = U(x)Z^3 - E_1(x)Z^2 + E_2(x)Z - E_3(x)` (`m=4`), and let
`Psi : P^1 -> P^3`, `x |-> [U:E_1:E_2:E_3](x)`, be the **tuple map**
(after removing common factors). Two points carry the same unordered
slope tuple iff they lie in the same fibre of `Psi`. Therefore:

> **UNIFORM `k`-sharing forces `Psi = Psi~ o w` with `deg w = k`.**
> Proof: the subfield of `F_q(x)` generated by the coordinate ratios of
> `Psi` has index `k`; by **Lüroth** it is `F_q(w)` for a single `w` of
> degree `k`. QED.

CONSEQUENCE (the `x`-degree cost the brief asks for): every coefficient
of `G` is a pullback, so `deg_x = k * deg_w <= 3m-3`, i.e.
`deg_w <= 3(m-1)/k`. **The budget is met with EQUALITY iff `k | 3(m-1)`,
and MAXIMAL sharing `k = m-1` always meets it exactly with `deg_w = 3`.**
At `m=4`, `k=3`: `deg_w = 3` and `deg_x = 9 = 3m-3` **with no waste** —
in explicit contrast to anchor 1's even-degree lemma (`r35
REPORT.md:161`), where every `sigma`-symmetric ansatz wastes one unit
(`k=2`, `deg_x = 2*deg_u <= 8 < 9`). Registered: `P(R1.5 as stated,
including the no-waste claim at k=3) = 0.85`.

**R1.6 (the pencil-of-cubics reformulation — the search instrument).**
`w = P/Q` with `deg P, Q <= 3`. A fibre `{x_1,x_2,x_3}` of `w` over `t`
satisfies `P - tQ = lambda (X-x_1)(X-x_2)(X-x_3)`. Hence:

> **A 3-sharing pattern with `t` complete triples in `mu_64` EXISTS iff
> there is a LINE in `P^3 = P(binary cubics)` containing `t` of the
> `C(64,3) = 41664` points `{prod_{x in T}(X - x) : T subset mu_64,
> |T| = 3}`.** Equivalently: `t` values of multiplicity exactly 3 in the
> 64-element multiset `{w(x) : x in mu_64}`.

This is the brief's "degree-3 pencils reappear", made exact and WITHOUT
any group action. Registered `P(R1.6 correct) = 0.90`.

**R1.7 (no group action is available — derived, not assumed).**
`mu_64` has no element of order 3 (`gcd(3,64)=1`), and `x -> x^3` is a
BIJECTION of `mu_64` (3 invertible mod 64), so the Galois route to
3-sharing is empty and `w` must be a **non-Galois** degree-3 map.
`P = 0.97`.

**R1.8 (mixed sharing is impossible — a sharp derived exclusion).** With
`n_j` classes of size `j` (`j=1,2,3`), `3n_3+2n_2+n_1 = 24` and
`t = n_1+n_2+n_3`; demand `3t + 2 - 15 <= supply 12` forces `t <= 8`,
and `2n_3 + n_2 = 24 - t >= 16` with `n_3 <= t <= 8` forces
**`n_3 = 8, n_2 = n_1 = 0`**. So the ONLY viable pattern is PURE uniform
3-sharing of all 24 points into 8 triples. `P(R1.8) = 0.90`.

**R1.9 (SPORADIC 3-sharing is dead; only uniform survives).** A `Psi`
that does not factor has `deg Psi <= 9` and its size-3 fibres inside
`mu_64` are chance collisions, expected `~C(64,3)/q^2 ~ 1.1` at
`q=193`. R1.8 requires **eight** of them. `P(a non-factoring Psi gives 8
size-3 fibres in mu_64) < 10^-4`. Registered so that a null result in
the general non-split search is NOT read as evidence against R1.5.

**R1.10 (the per-side cap forces hypergraph degree <= 2 at k=3).**
`X'_gamma = 3 d_gamma`; the per-side caps are
`|S_gamma ^ S_g| <= m-1 = 3` and `|S_gamma ^ S_h| <= 3`, and
`X'_gamma = (g-side) + (h-side)`, so `3 d_gamma <= 6 - 2X''_gamma`, i.e.
**`d_gamma <= 2`** (versus `d_gamma <= 3` at `k=2`). With
`sum_gamma d_gamma = 24`, this forces **`s >= 12` slopes on the
Delta-part**, and with 2 slopes for the middles and `T_2 = 15` exactly,
**`s = 13`: eleven degree-2 slopes and two degree-1 slopes**.
`P(R1.10) = 0.85`.

**R1.11 (the k=3 selection layer, decided POSITIVE by construction).**
Each triple splits `(a_T, 3-a_T)` across `S_g\S_h` / `S_h\S_g` with
`sum_T a_T = 12` over 8 triples, so exactly **four `(2,1)` triples and
four `(1,2)` triples** (or `(3,0)`/`(0,3)` variants). A degree-2 slope
`gamma` in triples `T,T'` has `a_T + a_{T'} <= 3` **and**
`(3-a_T)+(3-a_{T'}) <= 3`, forcing `a_T + a_{T'} = 3`: **every degree-2
slope joins a `(2,1)` triple to a `(1,2)` triple.** Hence the slope
graph on the 8 triples is **simple** (the `(OV)` cap at `k=3` is met with
EQUALITY — `|S_al ^ S_be| = 3 = m-1` — so no two triples may share even
one pair, i.e. no multi-edges) and **bipartite 4+4**. Certificate,
hand-checkable: `K_{4,4}` minus a perfect matching (3-regular, simple,
bipartite, 12 edges, 8 vertices) for `s=12`; delete one edge and attach
two pendant slopes for the forced `s=13`. **Registered prediction: the
3-sharing selection layer is FREE, exactly as anchor 1 found the
2-sharing selection layer free** (`r35 REPORT.md:130`). `P = 0.90`.
Zero-power: R4 below — this decides nothing about realizability.

**R1.12 ((OUT-m)/(DEG-m) is FREE at k=3 — derived).** `(DEG-m)` reads
`X'_gamma + 2X''_gamma >= m-1-eps~`. With `X' = k d`: at `k=2` this is
`d + X'' >= 2` (anchor 1's middle-support tightening); at `k=3` it is
`3d >= 3`, satisfied by **every** slope of degree `>= 1` with **no
middle support at all**. Registered: **the (DEG-m) tightening has ZERO
power over the 3-sharing class** and full power over the 2-sharing
class. `P = 0.90`.

**R1.13 (SPLIT 3-sharing is deficient — predict searched-negative).**
If `G` also splits, `phi_j = phi~_j o w` with
`sum_j deg_x phi_j = 3 sum_j deg_w phi~_j <= 9`, so each `phi~_j` is
**Möbius in `w`**; then `|A_j| = |w(S)| = 8` for every `j` and, fixing
`phi~_1 = id` to absorb `PGL_2` on the `w`-line, the continuous supply is
`3+3 = 6` against demand 11: **deficit 5**. Registered prediction: the
split 3-sharing ansatz is searched-negative, and **only the NON-SPLIT
`Psi~` (15 parameters) can carry a witness**. `P(split 3-sharing
witness) = 0.05`.

**R1.14 (the parameter count of the new ansatz `(SHARE3-4)`).**
`w`: 7 projective; `Psi~ = [U~:E~_1:E~_2:E~_3]`, `deg_w <= 3`:
`16 - 1 = 15` projective; minus `PGL_2` on the `w`-line: 3.
**Total 19**, versus `(SPLIT-4)`'s 10 and `(QUAD-4)`'s 14 (`r35
REPORT.md:155-157`). Continuous supply usable against coincidences =
**15** (`w` is 0-dimensional once its 8 fibres are pinned; see R2.1).
Prescribing "slope `gamma` occurs at fibre `t`" is exactly **one
homogeneous linear condition** on the 16 coefficients
(`U~(t)gamma^3 - E~_1(t)gamma^2 + E~_2(t)gamma - E~_3(t) = 0`), so at
most 15 of the 26 incidences can be prescribed by linear algebra and
`8` third-roots come out free. `P(R1.14) = 0.80`.

### R2 — THE ARITHMETIC EXISTENCE OF `w`, AND A SHARP q-THRESHOLD

**R2.1 (first moment for the pencil).** The number of 8-families of
pairwise disjoint triples in a 64-set is
`C(64,3)C(61,3)...C(43,3)/8! = 2.30 x 10^30` (registered as an exact
arithmetic claim, to be recomputed under ramguard). A fixed line of
`P^3` contains a fixed such point with probability `~q^-2`, and there are
`~q^4` lines, so

```
E[# degree-3 pencils on mu_64 with 8 disjoint complete fibres]
        ~  2.30e30 * q^-12
   q=193 : 855      q=257 : 27.7     q=449 : 0.034    q=577 : 0.0017
```

**REGISTERED FALSIFIABLE PREDICTION (the round's sharpest):** such
pencils EXIST at `q=193` and `q=257` and are ABSENT at `q=449` and
`q=577`; the threshold is `q ~ 340`. `P(exists at 193) = 0.80`,
`P(exists at 257) = 0.55`, `P(exists at 449) = 0.05`,
`P(exists at 577) = 0.02`. **FALSIFIER F-R2:** finding one at `q=449`
or `q=577` kills the first-moment model and I will report it as a MISS.

**R2.2 (the small-q verdict, registered in advance).** Because
`2.30e30` is `q`-independent, the supply of 3-sharing pencils decays as
`q^-12`. **Therefore, even a successful `m=4` witness via 3-sharing is a
SMALL-`q` ACCIDENT and does NOT extend to official scale
`q ~ 2^167`.** Registered now so that a positive result cannot be
over-claimed later. `P(this reading survives the round) = 0.90`.

**R2.3 (the search instrument is cheap — registered so a null result is
interpretable).** For a pencil spanned by cubics `C_1, C_2`, compute
`w(x) = C_1(x)/C_2(x)` for the 64 points of `mu_64` and histogram; a
value of multiplicity exactly 3 is a complete fibre. Enumerating a fixed
triple `T_1` against all `~35000` disjoint `T_2` costs `~10^7`
operations and covers every line through `T_1`. **Predicted: this is
exhaustive-per-`T_1`, so a null result over many `T_1` is a genuine
non-existence statement over the sampled lines, NOT a DFS ceiling** —
the first non-ceiling negative available in this lane. `P = 0.80`.

### R3 — D2 THE (DEG-m)-TIGHTENED SEARCH

**R3.1.** Budgets and draw counts will be matched to anchor 1's `m4_struct`
cell (`r35 REPORT.md:170-176`: DFS budget 12000, ~215 draws, same run,
same field) so the ceilings are comparable, and reported as
CEILINGS with class and budget named.

**R3.2 (registered prediction).** The `(DEG-m)` tightening (degree-1
slopes need `X'' >= 1`, `sum_gamma X''_gamma = (m-1)(m-2) = 6` exactly)
**lowers the 2-sharing `m=4` ceiling by at least 1** (anchor 1's `k=9`
candidates already carry six degree-1 slopes against a completeness
bound of four, `r35 REPORT.md:268-277`). `P(ceiling moves down) = 0.35`;
`P(ceiling moves at all) = 0.40`. By R1.12 it moves the 3-sharing
ceiling by **0** — registered as a zero-power pre-declaration, not as a
finding.

**R3.3 (registered prediction).** The 3-sharing search reaches its full
target `8 of 8` triples at `q=193` if and only if R2.1's pencil exists;
conditional on the pencil, `P(the 26 slots pack into 15 slopes) = 0.30`
(15 continuous parameters against 11 coincidences, discounted by anchor
1's MISS 3 that the parameter proxy overstates).

### R4 — MISS-2 GUARD (mean-vs-max), BOTH DIRECTIONS

Registered explicitly, per CONSTRAINTS.md and anchor 2's MISS 4
(a satisfied aggregate over an infeasible configuration) and anchor 1's
MISS 2 (a registered quantity that was not the quantity computed):

1. **Aggregate-to-existence.** A positive `(SUPPLY-CODIM)` excess
   (`E = +4`, R1.4), a positive first moment (`855`, R2.1), a satisfied
   slot/capacity count, or a free selection layer (R1.11) is a
   **mean** statement. None of them is existence. I will not write
   "feasible", "realizable" or "witness" on the strength of any of them.
2. **Max-to-bound.** A DFS/enumeration ceiling is a **max under a named
   budget over a named class**, never an upper bound; every such number
   will carry its class, its budget and its draw count.
3. **Computed-vs-registered.** For every registered quantity I will
   print the quantity actually computed next to it, and any silently
   ignored parameter (anchor 1's dead `mindeg`) is a MISS to be
   reported, not fixed quietly.
4. **Per-slope vs aggregate.** `(OUT-m)` binds PER BLOCK; aggregate
   pair-slot slack has no power (anchor 2 MISS 4). Every `(OUT-m)`
   check will be per-slope with the minimum reported, not the mean.

### R5 — D3 THE FLAT-SUPPLY LAW: WHAT I COMMIT TO ATTEMPTING

**R5.1 (the Cauchy-Schwarz demand-side inequality — registered as a
derivation I commit to BEFORE running anything).** For pencil-image
classes `phi_1..phi_{m-1}` with `sum_j deg phi_j <= 3(m-1)` and a
selection `S` of `|S| = 6m` points, put `A_j = phi_j(S)`. Then
`|A_j| >= |S|/d_j`, so by AM-HM
`sum_j |A_j| >= |S|(m-1)^2 / sum_j d_j >= 2m(m-1)`, and by
Cauchy-Schwarz on the multiplicity function
`|U A_j| >= (sum_j |A_j|)^2 / sum_{j,j'} |A_j ^ A_{j'}|`. Feasibility
needs `|U A_j| <= rho = 4m-1`, whence

```
sum_{j != j'} |A_j ^ A_{j'}|  >=  m(m-1)(m-7),
average pairwise cross-coincidence  >=  m(m-7)/(m-2)  ~  m-5.
```

**Registered predictions:** (i) the inequality is VACUOUS for `m <= 7`
(so it cannot decide `m=4` — declared in advance, R7.3); (ii) it is a
genuine `Omega(m)` LOWER bound on required cross-coincidence for every
`m >= 8`; (iii) combined with the heuristic Weil-type supply
`|A_j ^ A_{j'}| ~ N^2/q = 256m^2/q`, it gives a **q-threshold
`q <~ 256 m (m-2)/(m-7)`, i.e. `q = O(m)` — a CONSTANT-order threshold
of about `10^4` across `8 <= m <= 32`**, and hence infeasibility for all
pencil classes at official scale. `P(R5.1 (i)+(ii) correct) = 0.70`.

**R5.2 (the honest grade I commit to in advance).** The `o(m^2)` SUPPLY
upper bound the brief asks for requires an unconditional bound on
`|A_j ^ A_{j'}|`, which is a Weil/character-sum statement with a
`O(d^2 sqrt q)` error term that is LARGER than the `m` we need whenever
`q >> m^2`. **I therefore pre-declare that I expect to deliver an
UNCONDITIONAL demand-side theorem plus a CONDITIONAL supply bound, and
to grade the flat-supply law as PROVED-FOR-NAMED-CLASSES-CONDITIONALLY,
not as a theorem for all `G`.** `P(a fully unconditional o(m^2) supply
theorem this round) = 0.10`; `P(the conditional form lands) = 0.70`.

**R5.3 (a clean unconditional by-product I predict).** `deg phi_j = 1`
is impossible: a Möbius `phi_j` is injective on `S`, giving `6m > 4m-1`
distinct slopes. Hence **every factor has degree `>= 2`**, and with the
budget `sum d_j <= 3(m-1)` at most `m-1` factors can reach degree 3.
`P = 0.90`.

### R6 — BLIND PRIORS THE BRIEF DEMANDS

```
P(m=4 witness via general non-split G)                      = 0.22
P(a legal 3-sharing G-ansatz exists, q=193)                 = 0.55
   ... conditional on R2.1's pencil existing                = 0.30
P(3-sharing demand <= the m=3 crossing level 8)             = 0.03  [DERIVED NO: 11]
P(3-sharing demand <= the measured m=4 supply 12)           = 0.92  [DERIVED YES: 11]
P(flat-supply law provable for pencil classes this round)   = 0.10 unconditional
                                                            = 0.70 conditional
P((DEG-m) tightening moves any ceiling)                     = 0.40
P(m=4 closed for all named classes at end of round)         = 0.15
P(a witness lands this round)                               = 0.12
P(the m=4 obstruction is again purely arithmetic)           = 0.85
```

### R7 — ZERO-POWER PRE-DECLARATIONS (made BEFORE any computation)

1. **Every negative I produce is a ceiling under a named budget over a
   named class**, except the R2.3 pencil enumeration, which is
   exhaustive per starting triple and will be reported as such.
2. **`(SUPPLY-CODIM)` is a heuristic** with a supply proxy measured
   loose in both directions (anchor 1 MISS 3). No non-existence will be
   inferred from `E < 0` and no existence from `E > 0`.
3. **R5.1 is VACUOUS at `m <= 7`** and therefore has **zero power over
   `m=4`**. Declared now so it cannot be presented later as bearing on
   the round's mandate.
4. **R1.11's selection-layer certificate has zero power over
   realizability** — it relocates, exactly as anchor 1's did.
5. **Two fields is not `q`-uniformity**; and by R2.2 a positive result
   at small `q` is explicitly NOT a statement at official scale.
6. **No configuration will be completed** unless I say so explicitly:
   outside completion, the bivariate system, the full `W`, and the
   per-side split are all separate layers (anchor 1 MISS 7, MISS 8).
   In particular I pre-declare that I expect NOT to verify the per-side
   split, and that R1.11's `(2,1)/(1,2)` balance is a derived
   requirement I may only check combinatorially.
7. **Layer A will not be run.** `(SAT3)`-conditionality (`T = rho+2`)
   carries forward untouched. `m=1` will not be exercised.
8. **`(OUT-m)` is POSED, not proved** (anchor 1's zero-power 10);
   `(DEG-m)`, R1.10, R1.11 and R1.12 all inherit that status.
9. **The first moment R2.1 treats the 41664 split-cubics as random
   points of `P^3`. They are not** — they are a structured set. R2.1 is
   HEURISTIC and its falsifier F-R2 is the honest test.

### R8 — EXPECTED MISSES (registered in advance)

1. I expect an off-by-one or off-by-three in the middle-tuple slot
   bookkeeping (R1.2 is exactly such a correction to the anchor; mine
   may be wrong in the same way). Both conventions will be printed.
2. I expect at least one registered count (2.30e30, 855, 27.7) to be
   wrong on recomputation; recomputation is registered as mandatory.
3. I expect the `(2,1)/(1,2)` per-side balance (R1.11) to be the
   constraint that kills a candidate I have not anticipated — it is the
   `m=4` analogue of the per-side cap that killed anchor 2's second
   design.
4. I expect the non-split `Psi~` search to be limited by the
   split-over-`F_q` requirement at the 8 fibres (each cubic must have 3
   distinct roots in `F_q`, `~1/6` per fibre unprescribed), which no
   parameter count above accounts for.

### R9 — CATCH-24A COMMITMENT

Own-repo greps precede every novelty claim, including hyphenated and
infixed variants, at the SEARCH level with the full `--exclude-dir` set
and `--exclude=dag.json`. Objects to subtract before claiming:
`Lüroth`, `tuple map`, `pencil of cubics`, `3-sharing` / `three-sharing`
/ `k-sharing`, `(SHARE3-m)`, `non-Galois degree-3`, `first moment` on
lines in `P^3`, `Cauchy-Schwarz` supply bounds, `bipartite 3-regular` /
`K_{4,4} minus a perfect matching`, and `deg_H` (anchor 1's MISS 10
notation collision with
`rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction`).
