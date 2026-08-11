# PREREG — r35_rout_layer_a (round 35)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r34_layer_a/REPORT.md` (round 34)
2. `notes/pilots_20260811/r34_bivcurve_m34/REPORT.md` (round 34)

## Mandate

THE LAYER-A LANE'S TWO NAMED RESIDUALS + THE GATE PUSH. Round 34
made layer A the sole exclusion instrument at m = 2, 3 (the
W-layer is fenced by witnesses at both m; layer A is orthogonal to
(BIV-CURVE) 80/80). Its standing now rides on three questions this
round must move: (1) **Rout** — round 34 restated the refuted
(NS-m) as (NS-W-m) (roots IN W; survives 5280/5280) and named Rout
(the count of type-2 h_gamma roots OUTSIDE W; measured <= 3 on
648/648) as THE deciding question: is Rout <= d - m (equivalently,
is (NS-W-m)'s hypothesis d >= m free where the ledger needs it) a
THEOREM or a sample artifact? (2) **layer A on the m = 3
(BIV-CURVE) witness** — anchor 2 built the witness but never ran
layer A on it (its declared MISS 7); the banked expectation is
that layer A kills it. MEASURE IT. (3) **the multiplicative-domain
gate** — the factor-degree dichotomy's surviving profiles are ONE
per m at m = 2, 3, 4, and the cardinality-only count never touched
the multiplicative structure of D = mu_N; one more constraint may
empty the survivors.

## Deliverables

**D1 — Rout DECIDED.** Theorem with proof (state hypotheses
exactly; the m=1 regression test applies — any theorem must
either hold on the realized m=1 witnesses or be honestly
m-dependent), or a counterexample, or a wall with the obstruction
named. The refutation/redirection status of the whole (NS-m) ->
(NS-W-m) move follows from this — say which it is.

**D2 — LAYER A ON THE m=3 WITNESS.** Anchor 2's witness is fully
specified (phi = A/B over F_97 and F_193; the A_x table; scripts
in its dir — copy before use). Run the layer-A rank system on it,
both fields. If it dies: extract WHICH equations bind (the
consistency relations = candidate exclusion mechanisms at m = 3 —
this is the instrument working; name the mechanism). If it
SURVIVES: that is a major event (the banked orthogonality
expectation falls and layer A's instrument status is in doubt) —
verify twice, state loudly.

**D3 — THE MULTIPLICATIVE-DOMAIN PUSH.** The dichotomy's
surviving profile at m = 2, 3, 4 carries an irreducible factor of
Z-degree exactly ceil((3m+1)/4). The domain is mu_N
(multiplicative!). Derive what the mu_N structure imposes on that
factor's fibres (norms/traces/subgroup orbits — the RNC node's
named gate) and test whether the surviving profile is consistent
with it at m = 2 (then 3, 4). Emptying the survivors would make
the dichotomy an unconditional exclusion instrument.

**D4 — VERDICT.** Misses first. (NS-W-m)'s standing after Rout;
layer A's instrument status after D2; the dichotomy's reach after
D3. Cross-pilot flag (do NOT read siblings): anything you find
that bears on the realizability layer is a candidate mechanism for
the sibling lane — write it self-contained.

## Blind priors to register

P(Rout <= d - m is a theorem), P(layer A kills the m=3 witness),
P(the multiplicative push empties the m=2 survivor), P((NS-W-m)
survives the round as the target of record).

---

## Pilot registrations

Appended with the Edit tool after reading EXACTLY the two named anchors
(`r34_layer_a/REPORT.md`, `r34_bivcurve_m34/REPORT.md`) and BEFORE any
other read, any grep, any `ls`, and any interpreter invocation.

### R0 — notation and arithmetic, derived from the two anchors alone

`m`; `N = 16m`; `rho = 4m-1`; `R = 8m`; `e = m`; `delta = m-1`;
`T = rho+2 = 4m+1` (SAT3); `D = mu_N`. `W = S_g u S_h`, `a = |W|`,
`d = a-(4m+2)`, `need_X = d-m`. Argmax `a = (20m-2)/3`, there
`d = (8m-8)/3` and `d-m = (5m-8)/3`.

Root bookkeeping for a type-2 `h_gamma`:
`Rin` = roots in `W` (with multiplicity), `Rout` = `F_q`-roots outside
`W`, and `Rin + Rout <= deg h_gamma <= d`. So

```
(NS-m)    <=>  Rin + Rout <= d-m
(NS-W-m)  <=>  Rin        <= d-m      (hypothesis d >= m)
```

Hence **`(NS-m)` = `(NS-W-m)` + `Rout <= (d-m) - Rin`**, and the brief's
`Rout <= d-m` is the slack-free version of that. I record now that the
brief's parenthetical ("equivalently, is `d >= m` free where the ledger
needs it") is **not** an equivalence: anchor 1 already settles the
hypothesis (`d = (8m-8)/3 >= m` for all `m >= 2`,
`r34_layer_a/REPORT.md:255`). I answer the `Rout` question as primary
and say so.

Layer A at level `m`: `(rho+1)(T-m-1)` conditions on `T` unknowns
`c_gamma`. At `m = 3`: `12 * 9 = 108` conditions on `13` unknowns.
Banked RNC span bound: `m+1 = 4`; full rank is `min(T, rho+1) = 12`.
`m=3` witness constants (anchor 2, line 17): `N=48, rho=11, T=13,
a = w* = a* = 20, R = 24, e = 3`, `|S_g ^ S_h| = 2`, type-2 slopes 11.

### R1 — blind priors (the four the brief demands, plus auxiliaries)

1. `P(Rout <= d-m is a theorem, in a form that holds where the ledger
   needs it) = 0.06`
2. `P(layer A kills the m=3 (BIV-CURVE) witness) = 0.92`
3. `P(the multiplicative-domain push empties the m=2 survivor) = 0.12`
4. `P((NS-W-m) survives this round as the target of record) = 0.80`

Auxiliary: `P(D1 decided by an explicit counterexample at m >= 2) =
0.55`; `P(D1 ends in a named wall instead) = 0.30`;
`P(Rout <= C for an m-independent constant C is a theorem) = 0.15`;
`P(bank 1's "Rout <= 3 on 648/648" is a DEGREE artifact) = 0.50`;
`P(a new-in-lane multiplicative identity lands even if it empties
nothing) = 0.55`; `P(the m=3 witness's layer-A kill is independent of
the randomized outside completion) = 0.85`.

### R2 — falsifiable derivations, committed before measurement

**R2.1 (m=1 regression, from anchor 1's table lines 215-218 alone).**
At the realized `a* = 6`: `deg h = 0` in `480/480`, so `Rin = Rout = 0`
while `d-m = -1`; **`Rout <= d-m` fails `480/480`**. At the planted
`a = 7`: `deg h in {0,1}`, so `Rout = 1` in exactly the `4800` `NS-A`
failures and `0` in the other `480`; **`Rout <= d-m = 0` fails
`4800/5280`, and `max Rout = 1`**. Prediction: my own rerun reproduces
the histogram `{0:480, 1:4800}` at `a=7` and `{0:480}` at `a=6`.
`P = 0.88`.

**R2.2 (degree ceiling — the artifact hypothesis).** `Rout <= deg
h_gamma <= d` always. Therefore **any census whose `max d <= 3` cannot
distinguish "`Rout <= 3`" from the trivial degree bound.** Prediction:
bank 1's 648-measurement census has `max d <= 3` or
`max deg h_gamma <= 3`. `P = 0.50`. Fallback if false:
`P(sample correlation — few distinct H per configuration — explains it)
= 0.30`.

**R2.3 (null model, pre-registered so the comparison is a test).** Off
`W`, `h_gamma` is unconstrained by the `W`-layer data, so its
`F_q`-roots outside `W` should behave like those of a uniformly random
polynomial: `#F_q-roots ~ Poisson(1)` in the large-`q`, large-degree
limit, `P(>= 4) ~ 0.019`, `E[max over n draws] ~ log n / log log n`.
Consequence registered in advance: `648` INDEPENDENT draws with
`max Rout = 3` would be mildly surprising under the null (`~12` draws
with `Rout >= 4` expected), so the observation demands either small `d`
(R2.2) or correlation. Prediction: at `m >= 3` with a planted `a`
giving `d >= m+2`, a sweep over admissible kernel elements exhibits
`Rout > d-m` within `10^4` draws. `P = 0.60`.

**R2.4 (layer A on the m=3 witness).** Predicted: locator span rank
`= 12 = rho+1` (full) and layer-A nullity `0`, on both `F_97` and
`F_193`. `P = 0.90`. Secondary: the kill is already forced by the first
`m+2 = 5` locators in slope order (rank `> m+1 = 4` among them).
`P = 0.75`. Tertiary: if it SURVIVES, I verify on both fields, with two
independent builders, before writing a single sentence of consequence.

**R2.5 (a derivation I commit to now, to be checked, not fitted).**
With `Q(gamma,.)` vanishing on `S_gamma`, `deg_x Q = rho`, and
`sum_gamma |S_gamma| = T*rho - O` (anchor 1's step (4)):

```
(total deg_x drops of Q(gamma,.)) + (total roots of Q(gamma,.) off S_gamma) = O <= m-1
```

Predicted consequences: (i) if `O = 0` then `c(x)` is a nonzero
CONSTANT (not merely zero-free on `D`) and every `Q(gamma,.)` is a
scalar multiple of the locator `L_gamma`; (ii) the resultant identity
`Res_Z(C(Z), Q(Z,x)) * E(x) = Lambda * (x^N-1)^m` with `C` the
degree-`T` slope locator and `deg E = 1+O`; (iii) the per-factor
sharpening `T*d_j - N*m_j <= Drop_j` with `sum_j Drop_j <= O`, i.e.
**every irreducible factor is "small" up to `O`**, strictly stronger
than the `min(T d_j, N m_j)` bookkeeping. `P(the identity survives my
own check) = 0.70`. `P(it empties the m=2,3,4 survivor) = 0.12` — I
predict it does NOT, because for `Q` irreducible
`T*rho - N*m = -1 <= O` for every `m`.

**R2.6 (the expected wall, named in advance).** Every value-level
`mu_N` condition ("these `N = 16m` values are squares", "this
degree-`m` rational function maps `Gamma` into `mu_N`") costs a factor
`~2^{-N}` or `~q^{-c}` against a parameter space of dimension
`Theta(m^2)` over `F_q`; at official scale `q ~ 2^167` the surviving
count is still `q^{Theta(m^2)}`. Prediction: the multiplicative push
yields exact identities and per-factor pinning but **no emptying at
`m=2` by any counting argument**. `P = 0.75`. Corollary registered:
any construction that "uses the whole domain" multiplies `Z`-degrees by
`N = 16m`, giving `~16m^2` against only `T = 4m+1` slopes — a factor
`~4m` gap. I predict this gap is the obstruction I end up naming.
`P = 0.60`.

**R2.7 (declared vacuous before trying, and not tried).** Weil /
character-sum bounds over `mu_N` (`|sum_{x in mu_N} chi(f(x))| <<
deg(f) sqrt(q)`) and Chebotarev densities for the branch covering are
vacuous whenever `N = 16m << sqrt(q)`. Inherited from anchor 1's
zero-power 9. I will not manufacture a result from them.

### R3 — MISS-2 guard (mean-vs-max), three clauses

(a) **`Rout`.** A sample mean or a sample max NEVER bounds the true
max. I will not claim "`Rout <= C`" from any census, however large; a
census can only refute (by exhibiting a large `Rout`) or leave the
question open. Symmetrically I will not claim `Rout` is unbounded from
the Poisson heuristic — R2.3 is a null model, not a theorem.

(b) **Aggregate counting (inherited, anchor 1 R3).** The dichotomy's
inequality bounds a SUM: it refutes factorisation profiles, it never
certifies one. Positive slack is not existence — anchor 2's MISS 4 is
the canonical failure (the aggregate pair-slot count was satisfied
while the configuration was infeasible), and I expect the same trap in
D3's "the survivors are few, so one more constraint may empty them".

(c) **Layer A on one witness.** A kill on one sampled outside
completion is not a kill of the witness class, and a full span rank is
a max-type statement about a sample. I will resample completions and
report the DISTRIBUTION of the span rank / nullity, not its best case,
and I will grade any survival as a single-witness event.

### R4 — zero-power pre-declarations

1. `m=1` has `max Rout <= d <= 1` in every reachable stratum
   (`a in {6,7}`; `a = 8` unreachable, anchor 1 line 205), so **`m=1`
   has ZERO power to separate "`Rout <= 3`" from the degree bound.**
2. Bank 1's `Rout` census is at a PLANTED `W` (anchor 1 MISS 7);
   nothing there bears on realizability.
3. A layer-A kill of the `m=3` witness has power over that witness and
   its sampled completions only. It cannot show that layer A excludes
   `(BIV-CURVE)` at `m=3` in general.
4. Nullity `0` on a structured object is evidence about that object,
   never evidence of non-existence (anchor 1 R4.1; bank 2's
   `q^{-Theta(m^2)}`).
5. Profile scans are combinatorial; surviving profiles are NOT claimed
   realizable (anchor 1 MISS 9).
6. Two fields is not `q`-uniformity; nothing here is at official scale.
7. Everything remains `(SAT3)`-conditional; I build no realizable
   pencil.
8. Any `m >= 2` `Rout` measurement I make is at a planted `W` too, so a
   counterexample there refutes the literal quantifier and does not by
   itself decide the realized case — I will say which stratum every
   number lives in.

### R5 — subtraction plan (CATCH-24A), before any novelty claim

Own-repo greps for, at minimum: `Rout`, `R_out`, `R-out`, "outside W",
"roots outside", "off W"; `resultant`, `Res_Z`, `norm`, `Bezout`,
`x^N-1`, "divides x^N", `locator`, "extra root", "degree drop";
"multiplicative domain" AND the hyphenated/infixed variants
("multiplicative-domain", "mu_N structure", "subgroup orbit",
"evaluation hyperplane"). Every recursive grep rooted at `critical/`,
`background/`, or a specific named pilot directory, with
`--exclude-dir` applied at the SEARCH level, never by filtering output.

### R6 — expected misses

(i) At least one script or ramguard failure. (ii) My reconstruction of
`h_gamma` may differ from bank 1's definition; I will correct my object
rather than bend theirs. (iii) The `m=3` outside completion is
randomised, so I may fail to reproduce anchor 2's exact witness; the
fallback is the recorded `A`, `B` coefficient vectors. (iv) I expect to
over-claim novelty on the resultant identity and be subtracted by the
RNC node's own "norm/Bezout factorization" gate line.

### R7 — execution order

D1 (bank 1's definitions, `m=1` rerun, `m >= 2` counterexample search)
-> D2 (layer A on the `m=3` witness, both fields, resampled
completions) -> D3 (multiplicative push) -> D4. Report MISSES FIRST.
