# PREREG — rh_fr_algebraic (round 32)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `background/nodes/rate_half_type2_fr_incidence_only_route_fence/statement.md`
2. `notes/pilots_20260810/rh_type2_stratum/REPORT.md` (round 31)

## Mandate

Residual (ii) of the RH-AC budgets stands at a factor 9/4 with ONE
missing inequality, (FR): every non-minimum-weight type-2 slope of a
strict-A=3 pencil at T = rho+2 has |S_gamma ^ W| <= ~2m (the
max-vs-mean upgrade). The wave-57 fence PROVED the incidence route
dead: an explicit m = 64 quartic cyclotomic set system satisfies
EVERY banked incidence constraint (saturation, (OV), (C2) spend,
min pair union = a) yet has max |S_gamma ^ W| = 3m-3 = 189 > 2m.
The fence's own scope line: it is NOT a realizable Hankel-pencil
counterexample. YOUR JOB: the algebraic attack — use the objects
the fence cannot see: the generalized reciprocal-locator polynomials
f_gamma ((GNF): kappa_x = f(x)/sigma'_Z(x), deg f <= j), the common
syndrome pencil, and the apolar Hankel equations.

## Deliverables

**D1 — EXCLUDE THE FENCE SYSTEM.** Is the m = 64 fence system
REALIZABLE as an actual pencil configuration (actual locator sets of
actual type-2 slopes over an admissible field)? Attempt the
realization; if it fails, identify WHICH algebraic constraint kills
it — that constraint is (FR)'s candidate mechanism. If it succeeds,
(FR) as stated is FALSE and the 9/4 is real — that is a
route-deciding result of the first order; verify to the fence's own
standard (two implementations) before claiming.

**D2 — THE ALGEBRAIC (FR).** Derive the max-bound on
|S_gamma ^ W| for REALIZABLE configurations from (GNF) + the
divisibility structure (sigma_{S_gamma} relations through the
common pencil) + the apolar equations. Target: <= 2m + O(1), which
closes residual (ii) to a factor ~1. POSE with falsifiers what you
cannot prove; partial subclass theorems welcome (each with exact
scope).

**D3 — THE SMALL-SCALE REALIZABILITY CENSUS.** At the round-31
census scales (m = 2,3,4, two fields each): measure the TRUE max
|S_gamma ^ W| over realizable configurations vs the incidence bound
3m-3 vs the target 2m. Pre-register the expected separation BEFORE
running. Use the round-31 pilot's decoder machinery (copy scripts
into your dir; its d3_census.py is banked in rh_type2_stratum/).

**D4 — VERDICT.** Either the algebraic (FR) proved/posed with named
gaps, or the honest wall with the exact missing algebra named.
Misses first; zero-power declarations; the (SAT3)-conditionality
and (EQ)-converse caveats from round 31 carry forward — quote them.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  runs, repo root, literal `--`. RAMGUARD_TIMEOUT documented per
  use. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; checkpointed
  batches with results files.
- WRITE SCOPE: ONLY notes/pilots_20260810/rh_fr_algebraic/. No
  dag/, nodes/, tools/ edits. No git. Never touch prize-codex-*.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-32 dirs (rh_farca_upper,
  rh_haboeck_seam, rh_residuals_close). Round-31 and earlier pilot
  dirs are readable.
- BLIND PRIORS: after the two anchors only, append "## Pilot
  registrations" (P(fence system realizable), P(algebraic FR
  provable this round), expected killing constraint) BEFORE any
  further read.
- REPORT: REPORT.md in your dir (if the harness refuses the write,
  return the full text as your final message — and in all cases
  ALSO return it verbatim as your final message); MISSES-FIRST;
  file:line quotes (CATCH-24C); own-repo greps before novelty
  (CATCH-24A); zero-power declarations; banked scripts from scratch
  copies only.

## Pilot registrations

Appended after reading EXACTLY the two named anchors
(`background/nodes/rate_half_type2_fr_incidence_only_route_fence/statement.md`
and `notes/pilots_20260810/rh_type2_stratum/REPORT.md`) and BEFORE any
other read, any grep, and any interpreter invocation.

### R0 — notation I will use (inherited from round 31)

`N=16m`, `rho=4m-1`, `R=8m`, `R+1=8m+1`, `e=m`, `A=3`, `T=rho+2=4m+1`;
`W` = the minimum joint support, `a=w*=|W|`; `S_gamma=supp(v_gamma)`;
`z_gamma` = the `W`-supported representative of slope `gamma`;
`kappa_gamma=z_gamma-v_gamma in K`; `p_gamma=|S_gamma\W|`;
`n_gamma`, `n_0`, `j_gamma=wt(kappa_gamma)-(R+1)`; `d_x`; `O=sum o_gamma`.
NEW objects I intend to introduce: the **fibre map** `mu: W -> P^1`,
`mu(x)=` the unique slope `g` with `z_{g,x}=0` (well defined because
`x in W` means the representation pair is not jointly zero at `x`), its
fibres `F_g=mu^{-1}(g)` with `|F_g|=n_g` and `sum_{g in P^1} n_g = a`;
`G={g : n_g>0}`; `z_g`-supports `supp(z_g)=W\F_g`.

### R1 — blind priors demanded by the brief

- **P(the `m=64` fence set system is realizable as an actual strict-`A=3`
  pencil configuration — actual locator sets of actual type-2 slopes over
  an admissible field) = 0.06.** (Low, because of R2; the residual 0.06
  is my probability that R2's mechanism is either not a theorem or does
  not bind the fence's particular numbers.)
- **P(the algebraic `(FR)` proved UNCONDITIONALLY this round) = 0.25.**
- **P(the algebraic `(FR)` proved for a NAMED subclass with exact scope,
  with the residual case posed with falsifiers) = 0.65.**
- **P(`(FR)` shown FALSE for realizable configurations this round) = 0.03.**
- **P(honest wall, no new theorem) = 0.10.** (These four are the D4 verdict
  partition and sum to `1.03` by construction — the subclass and
  unconditional branches overlap; the unconditional branch is a subset of
  "some theorem lands", which I put at `0.87`.)

### R2 — expected killing constraint, registered as a mechanism, not a slogan

I register the following as my predicted mechanism BEFORE testing it.
The fence's `W` is an unstructured `a`-set. In a realizable configuration
`W` is not free: it is the support of a **2-dimensional space** `V` of
vectors `z_g = c_0 + g c_1` (`g in P^1`), because `w*` is the minimum
joint support of a representation pair `(c_0,c_1)` of the syndrome pencil.
Two consequences the incidence axioms cannot see:

1. **(FIB)** `W` is partitioned by `mu` into fibres `F_g`, `sum n_g = a`,
   and `supp(z_g) = W \ F_g` for every `g in P^1`. In particular
   `W = supp(z_{g_1}) union supp(z_{g_2})` for ANY two distinct
   `g_1,g_2 in P^1` — `W` is always a union of **two** `V`-supports.
2. **(OV+)** round-31's `(OV)` needs only that a pair be a `D`-representation
   of the syndrome pair up to `GL_2`, not that both members be supported
   slopes. Hence for a supported slope `gamma` and ANY `g != gamma`,
   `(v_gamma, z_g)` is such a pair, so
   `w* <= |S_gamma union supp(z_g)|`, i.e.
   **`|S_gamma ^ supp(z_g)| <= |S_gamma| - n_g <= rho - n_g`.**

Combining, for any two `g_1 != g_2` both `!= gamma`:

> **(FR-2)** `|S_gamma ^ W| <= 2rho - n_{g_1} - n_{g_2}`.

**Registered corollary (the predicted proof of `(FR)`):** if the pencil has
`T_1 = 2` type-1 slopes `gamma_1,gamma_2` (`kappa=0`, so
`S_{gamma_i} = W \ F_{gamma_i}` and `n_{gamma_i} >= a-rho`), then at
`a = 7m-1` we get `n_{g_1}+n_{g_2} >= 2(a-rho) = 6m` and hence
**`|S_gamma ^ W| <= 2rho - 6m = 2m-2 <= 2m`, `(FR)` with `O(1) = -2`.**
Equivalently, via the pairwise form: `|S_gamma ^ S_{gamma_i}| <= 2rho-w* = m-1`
and `W = S_{gamma_1} union S_{gamma_2}`, so `|S_gamma ^ W| <= 2(m-1)`.

**Registered residual (what I expect to be left over):** the case
`T_1 <= 1`, i.e. the fibre mass `{n_g}` is NOT concentrated on two slopes.
I register in advance that this is where I expect the wall to be, and that
`(FR)`'s truth is equivalent (up to `O(1)`) to a **concentration statement
about the fibre partition of the minimum joint support**, i.e. to
`n_{(1)} + n_{(2)} >= 2rho - 2m = 6m-2` where `n_{(1)},n_{(2)}` are the two
largest fibres. `sum_g n_g = a = 7m-1` makes this a statement that the top
two fibres carry `(6m-2)/(7m-1) -> 6/7` of the mass.

**Registered equivalent reformulation (to be checked, not assumed):**
`|S_gamma ^ W| <= 2m` for a type-2 slope is equivalent to the spend floor
`p_gamma >= rho-2m = 2m-1`, i.e. (using round 31's
`wt(kappa)=a-n_0+p`) to a **weight-excess floor** `j_gamma >= m-2-n_0`.
So `(FR)` says: `K` carries no low-excess codeword with this support shape.
I register the prediction that the trivial bound `wt(kappa) >= R+1` gives
exactly `p >= m+2+n_0` — **the fence's own `|S\W| >= m+2`** — so the fence
is precisely the extremal configuration of the minimum-distance-only
argument, and the missing factor 2 must come from `(FIB)`/`(OV+)`, not from
weights.

### R3 — D1 registrations (excluding the fence system)

- The fence numbers force, by double counting, `sum_x C(d_x,2) = 1023*C(64,2)+C(63,2) = 2064321`
  against `C(257,2)=32896` pairs, i.e. **mean pairwise intersection
  `62.75`** with the `(OV)` ceiling `2rho-a = 63 = m-1`: the fence is a
  near-perfect quasi-design. I register that I will verify these three
  integers by interpreter before using them.
- **Registered D1 prediction:** the fence system satisfies the triple
  union constraint `|S_1 u S_2 u S_3| >= R+1 = 513` comfortably
  (`~576`), so round-31's `(TR1')` does **not** kill it; the kill, if any,
  comes from `(FIB)`: **`W` must be a union of two `V`-supports, and a
  block with `|S ^ W| = 3m-3 = 189` would need
  `|S ^ supp(z_{g_1})| + |S ^ supp(z_{g_2})| >= 189`, hence
  `n_{g_1}+n_{g_2} <= 2rho-189 = 321 = 5m+1 < 6m`,** which is compatible
  with `sum n_g = 447` only if the fibre mass is spread over `>= 3` slopes,
  which in turn forces `T_1 <= 1`. So my registered D1 answer is
  **"not realizable UNLESS `T_1 <= 1`"**, and D1 collapses onto the same
  residual as D2. `P(D1 resolves to a clean unconditional non-realizability) = 0.20`.
- I register that I will NOT claim non-realizability from a failed search;
  only from a named violated constraint with a proof.

### R4 — D3 census registrations (pre-registered separation)

Scales `m = 2,3,4`, two fields each (`16m | q-1`), round-31 decoder
machinery copied into my directory from scratch copies.

- **P4.1** In MODE-B-style configurations at `a = 2rho` (round 31's
  planted stratum) the measured `max |S_gamma ^ W|` will **EXCEED** `2m`
  and reach `rho - (R+1-a) = 4m-4` (`4, 8, 12` at `m=2,3,4`), i.e. even
  above the incidence bound `3m-3` (`3,6,9`). Registered probability
  `0.75`. **This is not a refutation of `(FR)`**: those configurations have
  `T=3 != rho+2` and their TRUE `w*` is below `2rho` (round-31 MISS/finding,
  `rh_type2_stratum/REPORT.md:156`). I register this in advance so the
  measurement cannot be spun as a falsification.
- **P4.2** After recomputing the TRUE `w*` and TRUE `W` of each realized
  configuration, **0 violations** of `(OV+)`: `|S_gamma ^ supp(z_g)| <= |S_gamma| - n_g`
  for every supported `gamma` and every `g != gamma` with `n_g > 0`.
  Registered probability `0.85`; a violation refutes R2 outright.
- **P4.3** After recomputing the TRUE `w*`, **0 violations** of (FR-2):
  `|S_gamma ^ W| <= 2rho - n_{(1)} - n_{(2)}` over the two largest fibres
  not equal to `gamma`. Registered probability `0.85`.
- **P4.4** Measured `max |S_gamma ^ W| / m` at TRUE `w*`, over realizable
  configurations, lands in `[1.5, 3.0]` at `m=2,3,4` — i.e. I expect the
  census to be **unable to separate `2m` from `3m-3`** at these scales
  (they are `4,6,8` vs `3,6,9` and coincide at `m=3`). Registered
  probability that the census cleanly separates them: `0.15`. **Zero-power
  declared in advance.**
- **P4.5** Measured `T_1` (type-1 count) will be `2` in `>= 90%` of
  realizable configurations that have a type-2 slope. Registered
  probability `0.5` — this is the single most informative number for R2's
  residual and I have no strong prior.
- **P4.6** The census will reach `T = 3` only, never `T = rho+2`, so
  `(SAT3)` is untestable and every `(SAT3)`-conditional claim carries
  round-31's zero-power declaration
  (`rh_type2_stratum/REPORT.md:219`). Registered probability `0.9`.

### R5 — carried-forward caveats (quoted at report time)

`(SAT3)`-conditionality (`rh_type2_stratum/REPORT.md:54`, `:219`) and the
`(EQ)` converse gap (`n_0 = n_gamma` sampled, not proved,
`rh_type2_stratum/REPORT.md:44`) carry forward and will be quoted with
file:line in the report. I register that any theorem I state inherits
`(SAT1)-(SAT4)` + `T = rho+2` unless I explicitly say otherwise.

### R6 — subtraction plan (CATCH-24A) and zero-power plan

Before claiming novelty for `(FIB)`, `(OV+)`, `(FR-2)`, or the fibre
concentration reformulation I will grep `critical/`, `background/`,
`notes/` for: the fibre/partition-of-`W` object, "minimum joint support"
as a 2-space, `supp(z_g)`, `n_gamma` partition identities, and any prior
statement of the form `|S ^ W| <= 2rho - n - n'`. I pre-commit to
reporting every hit as a PORT. I pre-declare zero power for: the census vs
`(SAT3)`; any max-over-sample quantity; any `q`-dependence.

### R7 — route order

D1 anatomy of the fence (integer verification + `(FIB)` test) -> D2
derivation -> D3 census -> D4. If D2's unconditional proof lands before
D3, the census becomes a falsifier run, not a discovery run, and I will
say so.
