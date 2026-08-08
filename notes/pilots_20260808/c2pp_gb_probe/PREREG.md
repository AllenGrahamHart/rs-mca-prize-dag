# PRE-REGISTRATION — C2''-r3'S G-b FALSIFIER, EXECUTED (round 24)

Round 24, 2026-08-08. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 3's pose of
record (C2''-r3, the junction-sum form) is UNMEASURED at its own
quantifier depth — every prior number was single-junction stacking,
which the binding symmetric not-evidence clause retires in BOTH
directions. But its registered falsifier G-b is measurable NOW:
"sum_j log2(omega_j) growing without bound in q over >= 8
CONSECUTIVE junctions at >= 3 q-scales." Execute the FIRST
evidence-bearing C2'' measurement. If G-b fires, C2''-r3 is
falsified — a board-level event. If it does not, mystery 3 has its
first genuine data point and the growth shape of the junction sum.

## 0. Sources (quote verbatim first)
- critical/nodes/dli_c2pp_joint_reserve/statement.md — the
  round-23 adjudication addendum (C2''-r3's exact form; falsifiers
  G-a/G-b; the not-evidence clause; theta lessons) and
  notes/pilots_20260807/c2pp_diag/{REPORT.md, REPOSE_C2PP_R3_
  DRAFT.md} (the functional definitions: omega_j = the
  conditional-to-unconditional per-junction ratio at junction j of
  a SINGLE tower — quote the draft's exact definition and use it,
  not a reconstruction).
- The M1 census kernel (the banked exact machinery):
  critical/nodes/dli_prime_weighted_large_block_support/notes/
  m1_dli_m1_tower_census_modal.py::decompose_row — REUSE
  (read-only) as the single-junction primitive; your job is to
  CHAIN it into a genuine multi-junction tower measurement.
- The 34-level schedule definition (the official junction
  structure) — quote where the tower/junction ladder is defined
  and construct the toy analogue faithfully (state every place
  the toy differs from the official schedule).

## 1. Deliverables
- (D1) THE INSTRUMENT: a single-tower, >= 8-CONSECUTIVE-junction
  measurement of omega_j at toy scale — genuine sequential
  conditioning (state_{<j} null), NOT per-junction stacking.
  Design for the compute walls: exact integer censuses per
  junction with checkpointing; register in advance the largest
  (n, t-depth, q) cells you project reachable and the fallback
  ladder if the 8-junction depth is not reachable at the first
  cell size (report the deepest achieved honestly — a 6-junction
  measurement is reported as 6, not extrapolated to 8).
- (D2) THE G-b TEST: the junction-sum sum_j log2(omega_j) over
  the consecutive window at >= 3 q-scales (register the q ladder
  in advance). G-b FIRES iff the sum grows without bound in q
  (register the concrete firing criterion — e.g. monotone growth
  across all three scales with no saturation — BEFORE measuring).
  Also report the sum against the 21-bit reserve scaled to the
  toy window (with the honest statement that the 33-junction
  transport is NOT licensed — the toy sum is evidence about
  GROWTH SHAPE, not about the official reserve).
- (D3) THE SHAPE: is the junction sum dominated by early
  junctions, flat, or growing with depth? Does the per-junction
  omega_j decay, stabilize, or grow as the tower deepens? This
  shape is the first real input to whether the official 33-sum
  can plausibly exceed 21 bits.
- (D4) THE VERDICT: G-b FIRES (C2''-r3 falsified at toy scale
  under its own registered criterion — headline; reproduction
  script; the coordinator re-poses) / SILENT (the measured shape
  + what window/depth it covers + the registered next escalation)
  / UNREACHABLE (the exact wall and the honest Modal spec for
  the instrument at the needed depth).

## 2. Falsifiers / honesty
- The not-evidence clause binds YOU too: no uniform stacking, no
  single-junction proxy multiplied by anything. Sequential
  conditioning only.
- Toy-to-official transport is NOT licensed; label every number's
  scope. Census evidence is evidence, never proof.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260808/c2pp_gb_probe/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking; checkpoint deep censuses to YOUR OWN dir. 2-power
  grids (CATCH-Z6); no shift-0 cells (CATCH-19B); name every
  measured functional (CATCH-19C). Verbatim quotes with
  file:line. No REPORT.md — your final message IS the report.
  QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or past line 3173 (the "ROUND 24 LAUNCHED" marker); do not
  read the other round-24 pilot dirs (z_ceiling_assault,
  kernel_window_hunt, t_petal_lemma); PASS THIS QUARANTINE CLAUSE
  VERBATIM to any subagent you dispatch.

# PILOT REGISTRATIONS

Appended 2026-08-08 BEFORE any computation (no script had been written
or run at the time of this append). Opus pilot, round 24.

## P0. The definitions I will use, quoted, not reconstructed

**(P0-a) The functional G-b names.** Verbatim, the pose's own text:

> - **(G-b) SELECTION GROWTH**: a demonstration that the coset selection
>   factor `omega_j := P[state_j in the coset column | null] /
>   P[state_j in the coset column]` has an aggregate `sum_j log2(omega_j)`
>   growing without bound in `q` along admissible rows, measured on
>   `>= 8` consecutive junctions at `>= 3` increasing q-scales.
> — `notes/pilots_20260807/c2pp_diag/REPOSE_C2PP_R3_DRAFT.md:133-137`

**(P0-b) The claim the falsifier attacks.** Verbatim:

> ```text
>     sum_{j=1}^{33}  log2 ( E_U[ rho_j | state_{<j} null ] / E_U[ rho_j ] )   <=   21.
>                                                                    (C2''-r3)
> ```
> — `REPOSE_C2PP_R3_DRAFT.md:49-52` (= `critical/nodes/dli_c2pp_joint_reserve/statement.md:94`)

**(P0-c) The binding symmetric clause, which binds me.** Verbatim:

> A single-junction measurement multiplied by 33 ("uniform stacking",
> `x**33` vs `2**21`, `m4_assembly_verifier.py::gate_calibration`,
> lines 402-417) is NOT evidence FOR C2''-r3 and NOT evidence AGAINST it.
> — `REPOSE_C2PP_R3_DRAFT.md:65-69`

**(P0-d) The tower.** Verbatim:

> The b2b nested tower at an admissible row (q prime, q ≡ 1 mod n, n = 2^s;
> official schedule 34 levels, Σ_j L_j = t, 33 junctions); junction j
> conditions level-(j+1) skew variables on the state-dependent domain
> G(state_{<j}); tower total = Σ_states skewcount(G(state)) (TEST-1 exact, 8
> rows).
> — `critical/nodes/dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md:12-16`

> DYADIC DESCENT.  h_j = n/2^j.  m_0 = x, and for j >= 0
>       m_{j+1}(i) = m_j(i) + m_j(i + h_{j+1}),      i in Z/h_{j+1}
>       d_j(i)     = m_j(i) - m_j(i + h_{j+1}).
> Because zeta_{h_j}^{r(i+h_{j+1})} = (-1)^r zeta_{h_j}^{r i}:
>   * r EVEN  ->  the constraint descends verbatim to level j+1;
>   * r ODD   ->  the constraint becomes  sum_i d_j(i) zeta_{h_j}^{r i} = 0.
> Iterating, constraint r is consumed at level j = v_2(r).  Hence
>   BLOCK j (the pose's "level j") owns  U_j = {odd u : u*2^j <= t},
>   L_j = |U_j| = ceil(floor(t/2^j)/2) = the pose's ell_j,  sum_j L_j = t,
> — `notes/pilots_20260802/c2pp_nullity_structure/dli_model.py:14-25`

> STATE-DEPENDENT DOMAIN. ... the EFFECTIVE SUPPORT is
>     S_j = { i : 0 < m_{j+1}(i) < 2^{j+1} }        (the unsaturated cells).
> At j = 0 this is exactly the archived "singleton set G" and the domain is
> {+-1}^G, i.e. skewcount(G).
> — `dli_model.py:27-33`

**(P0-e) The coset column.** Verbatim:

> COSET column = k = 0 (routed, clause i); ACCIDENT classes = k >= 1 with
> class-conditional mean > theta = 2 x unconditional class mean
> — `critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_tower_census_modal.py:25-27`

with `k = #singletons` at junction 0, i.e. `k = |S_0|`
(`m1_dli_m1_tower_census_modal.py:15-16`). I therefore fix, for every
junction j, **coset column := {S_j = empty}** (= every level-(j+1) cell
saturated). This is the unique reading that reduces to the banked
`k = 0` column at j = 0.

**(P0-f) The official ladder, for the divergence list.** Verbatim:

> Blocks `B_j = {r <= t : v_2(r) = j}` for `j = 0..33`, so `L_j = |B_j| = 2^{32-j}`
> for `j <= 32` and `L_33 = 1`, `sum_j L_j = t`. Junction `j` (`j = 0..32`,
> 33 junctions) works in `Z[zeta_{h_j}]` with `h_j = n/2^j`, degree
> `N_j = phi(h_j) = h_{j+1} = 2^{40-j}` ... Uniformly
> ```text
> N_j = 256 L_j        for every j = 0, ..., 32.                       (OS-1)
> ```
> — `background/nodes/dli_official_support_forcing/statement.md:21-30`
> (`n = 2^41`, `t = 2^33`, admissible `q` odd prime, `v_2(q-1) >= 41`,
> `q < 2^256` — same node, `:5-10`)

## P1. THE CONDITIONING LEMMA (registered before computing; asserted in code)

The whole instrument rests on one identity, which I state now so it can
be falsified independently of my numbers.

> **LEMMA (accumulated conditioning = coarse nullity).** Under the dyadic
> descent of P0-d, for every junction `j`,
> ```
> N_{>j} := AND_{j' > j} { block j' constraint holds }
>         = { m_{j+1} is T_{j+1}-null on Z/h_{j+1} },
>   T_{j+1} := floor( t / 2^{j+1} ),
> ```
> i.e. `sum_i m_{j+1}(i) zeta_{h_{j+1}}^{r i} = 0` for `r = 1..T_{j+1}`.
> *Reason:* constraint `r` is consumed at block `v_2(r)`, so the blocks
> strictly coarser than `j` are exactly `{r <= t : v_2(r) > j}`
> `= {2^{j+1} r' : 1 <= r' <= floor(t/2^{j+1})}`, and each such constraint
> descends verbatim to level `j+1` as the `r'`-th moment of `m_{j+1}`.

CONSISTENCY CHECK, registered as a pass/fail gate: at `j = 0` this gives
`T_1 = floor(t/2)`, which is exactly the banked kernel's even-moment
conditioning — "`e = floor(t/2)` even moments `p_{2s}(m_1) = sum_i m_1(i)
zeta^{2si}`" (`m1_dli_m1_tower_census_modal.py:17-18`). If my machinery
does not reproduce the banked `n_null` values from `BANKED_F2B` at
`n = 32`, the lemma or my code is wrong and NOTHING is read (see PR6).

This is what makes the measurement SEQUENTIAL rather than stacked: at
junction `j` the conditioning event is the accumulated nullity of every
coarser junction already traversed in the SAME tower, and the events are
genuinely nested, `N_{>0} subset N_{>1} subset ... subset N_{>J-1}`.
No junction is measured in isolation and no number is raised to a power.

## P2. Named functionals (CATCH-19C) — all fixed before any run

Base measure `U` := `x` uniform on `{0,1}^n` (the tower's own
unconditional measure; it induces `m_j(i) ~ iid Binom(2^j, 1/2)` across
the `h_j` cells, and at `j = 1` it reproduces the banked
`an[k] = C(h,k) 2^{h-k}`, `n_all = 3^h` weights of
`m1_dli_m1_tower_census_modal.py:554-556` exactly).

For junction `j`, with `h := h_{j+1} = n/2^{j+1}`, `u := 2^{j+1}`,
`T := T_{j+1} = floor(t/2^{j+1})`, `zeta_h` the deterministic primitive
`h`-th root (`get_zeta` convention, least primitive root `^((q-1)/n)`,
`m1_dli_m1_tower_census_modal.py:255-261`):

| name | definition |
|---|---|
| `S_j` | `{ i in Z/h : 0 < m_{j+1}(i) < u }` (unsaturated cells) |
| `COSET_j` | the event `S_j = empty` (every cell saturated) |
| `C_j` | `#{ A subset Z/h : sum_{i in A} zeta_h^{r i} = 0 in F_q, r = 1..T }` |
| `Z_j` | `#{ x in {0,1}^n : m_{j+1}(x) is T-null }` (weighted state count) |
| `Zstate_j` | `#{ M in {0..u}^h : M is T-null }` — UNWEIGHTED, the banked `n_null` object, used only for the positive control |
| `P_cos(j)` | `P_U[COSET_j] = 2^{h-n}` (closed form; asserted in code) |
| `P_nul(j)` | `P_U[N_{>j}] = Z_j / 2^n` |
| `omega_j(q)` | `P[COSET_j | N_{>j}] / P[COSET_j]` |
| `Sigma_W(q)` | `sum_{j in W} log2 omega_j(q)` — THE G-b JUNCTION SUM |
| `Pblk_j` | `P_U[ block j constraint holds ]` (unconditional junction marginal) |
| `R3_W(q)` | `sum_{j in W} log2( E_U[rho_j | N_{>j}] / E_U[rho_j] )` (secondary) |
| `ceil_j` | `n - h_{j+1}` bits — the registered saturation ceiling of `log2 omega_j` |

**Bayes identity (registered, asserted in code as an exactness guard):**
`omega_j = P[N_{>j} | COSET_j] / P[N_{>j}] = (C_j / 2^h) / (Z_j / 2^n)`.
Conditioned on `COSET_j` the state is `m_{j+1} = u * 1_A` with `A`
uniform on subsets of `Z/h` (each saturated cell is `0` or `u` with equal
weight, `C(u,0) = C(u,u) = 1`), and `u*1_A` is `T`-null iff `A` is
`T`-null — hence the numerator is a pure SUBSET census.

**`rho_j` convention (declared divergence, D-10 below):** I take
`rho_j(M) := q^{L_j} P_U[ block j holds | m_{j+1} = M ]` with the
`U`-induced (binomial) skew law, not the uniform-on-domain law of
`dli_model.py:155-178`. Then `E_U[rho_j] = q^{L_j} Pblk_j` and
`E_U[rho_j | N_{>j}] = q^{L_j} P_nul(j-1)/P_nul(j)`, so
`R3_W(q) = sum_{j in W} log2( P_nul(j-1) / (P_nul(j) * Pblk_j) )`.
`R3_W` is G-a's object, NOT G-b's; it is reported as shape data only and
CANNOT fire G-a at `J < 8` (and I register no transport `J -> 33`).

## P3. THE TOY TOWER, and EVERY divergence from the official schedule

Construction: the dyadic descent of P0-d verbatim — same `h_j = n/2^j`,
same `m_{j+1}/d_j` recursion, same `U_j = {odd u : u 2^j <= t}`, same
`L_j = ceil(floor(t/2^j)/2)`, same `sum_j L_j = t`, same blocks
`j = 0..D-1` with `D = floor(log2 t) + 1`, same junctions `j = 0..D-2`,
same `get_zeta` convention, same admissibility form `q` prime `= 1 mod n`.

PRIMARY CELL (L0): `n = 32`, `t = 16` -> `D = 5` blocks, junctions
`W = {0,1,2,3}`, `J = 4`;
`(h_1,h_2,h_3,h_4) = (16,8,4,2)`, `(T_1,T_2,T_3,T_4) = (8,4,2,1)`,
`(L_0,L_1,L_2,L_3) = (8,4,2,1)`.

**Divergences from the official schedule — every one named:**

- **D-1 SCALE.** `n = 32` vs official `n = 2^41`; `t = 16` vs `t = 2^33`.
- **D-2 DEPTH.** 4 junctions vs 33. The registered G-b depth is `>= 8`;
  see P5 for why 8 is unreachable and what I will report instead.
- **D-3 SUPPORT/CONSTRAINT RATIO.** Official `N_j = 256 L_j` (OS-1), i.e.
  `h_{j+1}/L_j = 256` at every junction. Toy: `h_{j+1}/L_j = 2` at every
  junction. **Divergence factor 128.** This is forced: `h_{j+1}/L_j ~ n/t`
  and `n/t = 256` at official scale needs `t <= n/256`, which at any
  computable `n` leaves fewer than 2 junctions.
- **D-4 DENSITY / BALANCE POINT.** Official has `log2 q <= 256 = n/t`, so
  `2^{h_{j+1}} ~ q^{L_j}` — the official row sits AT or BELOW the
  knife-edge where the number of level-`(j+1)` states equals the number of
  constraint values (`official_scale.json`: `"exceeds_2^21_iff":
  "256 - log2 q < 107/2^33"`). The toy CANNOT sit there: admissibility
  forces `q > n = 2^5` while `n/t = 2`, so every toy row has
  `q^{T} >> 2^{h}` — the toy is ABOVE the balance point by at least
  `(log2 q - n/t) * T` bits at junction j. **This is the single most
  important divergence and I register it as such**: it means the toy's
  null sets are structure-dominated where the official row's are not.
  The q ladder is chosen to sweep this axis, and PR4 predicts what it does.
- **D-5 CEIL ARTEFACT.** Official `L_33 = 1` is a `ceil` artefact and gets
  no junction. Toy uses the identical `ceil` rule and identically gives the
  terminal block no junction.
- **D-6 ADMISSIBILITY.** Official: `q` odd prime, `v_2(q-1) >= 41`,
  `q < 2^256`. Toy: `q` prime, `v_2(q-1) >= 5` (`= 1 mod 32`), no upper
  bound imposed. SAME FORM, different modulus; no upper cap (deliberate —
  G-b asks about growth in `q`).
- **D-7 FIELD/ROOT CONVENTION.** Identical (`get_zeta`, least primitive
  root `^((q-1)/n)`); no divergence.
- **D-8 BASE MEASURE.** Identical to the banked kernel's "all states"
  measure at level 1 (`an[k]`, `n_all = 3^h`); no divergence.
- **D-9 NO DECOMPOSITION.** I take no coset/accident/bulk split, no
  `theta`, and strip no column. Matches C2''-r3 (`REPOSE...DRAFT.md:59-62`)
  and dodges the round-23 theta kill entirely.
- **D-10 `rho_j` WEIGHTING.** `U`-induced binomial skew law vs
  `dli_model.py`'s uniform-on-domain. Affects only the SECONDARY `R3_W`,
  never `omega_j` / `Sigma_W`.
- **D-11 SINGLE ROW.** Each measurement is one `(n,t,q)` row = one tower;
  the q ladder is a family of towers, not a stack of junctions.

CROSS-WINDOW CELL (L2): `n = 64`, `t = 32`, `W = {1,2,3,4}`, `J = 4` —
same depth, window placed away from `j = 0`, to test whether the shape
is an artefact of the shallowest junction. Same divergence list with
`h_{j+1}/L_j = 2` again.

## P4. THE q LADDER (registered before measuring; CATCH-Z6, CATCH-19B)

2-power grid: for each `n`, `q_k :=` the least prime `q = 1 (mod n)` with
`q >= 2^k`, over
```
K = { 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32 }      (n = 32)
K = { 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32 }      (n = 64)
```
14 q-scales, spanning 25 octaves — far more than G-b's `>= 3`. The cost
of my census is q-INDEPENDENT (meet-in-the-middle over states with
dictionary keys in `F_q^T`, never a `q^T` grid), which is exactly why a
25-octave ladder is affordable and a deep window is not.

- **CATCH-Z6**: every `n` is a 2-power and every `q` is prime; no
  composite modulus and no composite `2N` toy is used anywhere.
- **CATCH-19B**: every junction in every measured window has `T_{j+1} >= 1`
  and `L_j >= 1` and `h_{j+1} >= 2`. Cells with `T = 0` (no constraint —
  `omega_j = 1` by construction) and the terminal `h_{j+1} = 1` cell (the
  trivial character) are excluded BY DESIGN, in the window definition,
  not by post-hoc filtering of results.

## P5. DEPTH: the registered wall, and the fallback ladder

**REGISTERED WALL (stated before measuring, so it cannot be a
post-hoc excuse).** The exact census cost at junction `j` is
```
   min(  (2^{j+1} + 1)^(h_{j+1}/2)  ,  q^(T_{j+1}) * h_{j+1} * 2^{j+1}  )
```
(meet-in-the-middle over cells; or a key grid in `F_q^{T}`). Any window
of `J` CONSECUTIVE junctions contains a junction with
`T_{j+1} >= 2^{J-1}`, and non-degeneracy needs `h_{j+1} > T_{j+1}`.
For `J = 8`: `T >= 128`, so the grid route costs `>= q^128 >= 2^700` and
the MITM route costs `>= 3^64 = 2^101`. **Both are dead by dozens of
orders of magnitude at ANY budget — this is a property of exact nullity
counting, not of the 1 GB / 5 min law, and no Modal spec repairs it.**
I therefore register NOW that G-b's mandated depth 8 is UNREACHABLE by
exact census, that I will report the deepest depth actually achieved,
and that I will NEVER extrapolate a 4-junction reading to 8 or to 33.

**FALLBACK LADDER (execute in order; report deepest achieved):**
- **L0** `n=32, t=16, W={0,1,2,3}` — `J = 4`. PRIMARY.
- **L1** `n=32, t=8,  W={0,1,2}`   — `J = 3`. Only if L0 hits a wall.
- **L2** `n=64, t=32, W={1,2,3,4}` — `J = 4`, independent window placement.
- **L3** `n=64, t=32, W={0,1,2,3,4}` — `J = 5`, STRETCH: needs junction 0
  at `n=64` = a `3^16 = 43,046,721`-state MITM half, checkpointed across
  the 5-minute walls to my own directory. Attempted only after L0 and L2
  are banked.
- **L4** `n=128, t=64, W={3,4,5}` — `J = 3`, third window placement.

## P6. Concrete G-b firing criterion (registered BEFORE measuring)

Let `W` be the measured consecutive window, `J = |W|`, and
`Sigma_W(q_k)` the junction sum over the registered q ladder.

**G-b FIRES iff ALL FOUR hold:**
- **(F1) DEPTH** `J >= 8` (the pose's own quantifier).
- **(F2) MONOTONE** `Sigma_W(q_k)` strictly increasing across the whole
  registered ladder (all 14 scales; `>= 3` is the pose's minimum).
- **(F3) NO SATURATION** the least-squares slope of `Sigma_W` against
  `log2 q` over the TOP HALF of the ladder is `>= 0.25` bits/octave, AND
  the top-octave increment is `>= 0.5 x` the median increment (no
  geometric decay to a ceiling).
- **(F4) NOT ONE JUNCTION** at least `ceil(J/2)` individual junctions have
  `log2 omega_j` strictly increasing over the top 3 scales.

**G-b is SILENT** iff (F2) or (F3) fails at the achieved depth.
**If (F2)-(F4) hold but (F1) fails**, the verdict is
`SUB-DEPTH GROWTH SIGNAL at depth J` — explicitly NOT a falsification of
C2''-r3, recorded as an escalation trigger for the coordinator.

**Registered saturation read (the strongest non-firing).** As `q -> inf`
at fixed `(n,t)`, every `T`-null level-`(j+1)` state should become
saturated, giving the q-independent ceiling
`log2 omega_j -> ceil_j = n - h_{j+1}`. If the measured `omega_j` reach
that ceiling and stop, G-b is SILENT WITH AN EXPLICIT BOUND.

**Reserve comparison, with its scope stated in advance.** I will report
`Sigma_W(q)` against 21 bits and against the window-scaled reserve
`21 * J / 33`. **The `J -> 33` transport is NOT licensed** (it is exactly
the uniform stacking the binding clause retires, in both directions);
the comparison is printed as a SHAPE descriptor and is not evidence about
the official reserve. No number in my report carries an official-row
scope.

## P7. Predictions (registered before computing; scored either way)

- **PR1** `omega_j > 1` at every junction and every `q` (conditioning
  selects INTO the coset column, never out of it).
- **PR2** `log2 omega_j` INCREASES with `j` across the window (deeper
  junctions select harder, because `h_{j+1}` shrinks).
- **PR3** `Sigma_W(q)` SATURATES; G-b does not fire; the ceiling at
  `n=32, W={0,1,2,3}` is `(32-16)+(32-8)+(32-4)+(32-2) = 98` bits.
- **PR4** Saturation onset at `log2 q ~ h_{j+1}/T_{j+1} = n/t = 2`, which
  is BELOW the smallest admissible `q = 97`; so PR4 predicts the toy is
  ALREADY saturated at the bottom of the ladder and `Sigma_W` is nearly
  q-FLAT across all 25 octaves.
- **PR5** The junction sum is dominated by the DEEPEST junctions in the
  window, not the early ones.
- **PR6** POSITIVE CONTROL, gating: at `n = 32`, junction 0, my machinery
  reproduces the banked `BANKED_F2B` null-state counts EXACTLY —
  `443841` at `(t=2,q=97)`, `223041` at `(t=2,q=193)`, `10881` at
  `(t=2,q=8353)`, `7713` at `(t=2,q=32801)`, `443841` at `(t=3,q=97)`,
  `223041` at `(t=3,q=193)`, `4369` at `(t=4,q=97)`, `1137` at
  `(t=4,q=193)` (`m1_dli_m1_tower_census_modal.py:192-201`). **If any of
  the 8 fails, no G-b read is taken.**

## P8. What this pilot cannot reach (registered in advance)

- No official-row inference of any kind. Toy-to-official transport is not
  licensed and is not attempted.
- Depth 8 is unreachable by exact census (P5); therefore G-b cannot FIRE
  under its own (F1) no matter what the numbers say. The honest maximum
  outcome of this pilot is a SUB-DEPTH signal or a SILENT-with-bound read.
- `R3_W` is not a G-a firing and no `J -> 33` transport is registered.
- Census evidence is evidence, never proof. No status flip, no closure
  claim, nothing outside this directory is written.
