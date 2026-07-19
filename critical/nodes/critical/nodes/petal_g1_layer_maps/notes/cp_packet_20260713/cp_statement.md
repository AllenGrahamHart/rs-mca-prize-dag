# cp_statement — CLAUSE (P) closed at the floor band: the aperiodic top-band
# atlas supply is a support-rigidity counting theorem (word-free, q-free)
# 2026-07-13, fresh-context proof worker. Catch ledger continues from #167.

- **target:** `petal_g1_layer_maps` = CLAUSE (P) after the 2026-07-13 surgery
  (dag.json statement, final block): at every official row and every received
  word `U`, the APERIODIC (`c(S)=1`) top-band full-petal contributors are
  covered by an explicitly defined finite first-match atlas `A_U^prim` of
  fixed `(D0,R0)` sunflower auxiliary layers (printed dictionary, coset
  petals, `|R0| < ell`, retained-zero), with paid weighted census
  `sum_chi (m_chi + 1) <= (121/128) n^6`, quantified at the FLOOR BAND
  `d >= ell(t_ch - 2)` (pin P1's deep reading; `t_ch` = chart petal count),
  official rows only, with the #153 both-subfamilies cap and the #145
  odd-lift hazard noted (poly at the floor band, EMPTY at rate <= 1/4).
- **verdict:** PROVED as posed (see cp_proof.md), by a support-rigidity
  counting theorem that needs NO open input: the floor band forces
  `|S n Z| <= 3` and touched petals `m in {t_ch - 1, t_ch}` at rate 1/2, and
  is EMPTY (for ALL contributors, any scale) at official rates <= 1/4.
  The atlas is WORD-INDEPENDENT — received-word uniformity holds trivially,
  dissolving the frontier.md extraction obstruction at this band.
- **verifier:** cp_verify.py (ramguard tiny, staged P1..P7; ALL PASS —
  record in cp_findings.md): complete-census cross-validation at (16,8,97)
  and (16,4,97), banked-pin reproduction 53/48/8/0, two fresh cells,
  non-coset layouts, 4 mutation controls incl. the required-to-trip ones,
  exact bigint official-grid arithmetic s = 3..44.
- **provenance:** notes/g1a_findings.md (#138-#144), notes/
  bsr_repose_20260713/ (#145-#149), bsra_findings.md (#150-#155);
  this packet mints catches #168-#171 (cp_findings.md).

## 0. Setting and pinned conventions (inherited verbatim)

Row: `n = 2^s`, `sigma = 1`, `ell = sigma + 1 = 2`, `2 <= k <= n-2`;
official rows have `k = rho n`, `rho in {1/2, 1/4, 1/8, 1/16}` (the four
official maximal rows are `n = 2^41..2^44`, `k = 2^40`; official `k` is
always even). `q` a prime power with `n | q-1`, `H <= F_q^*` the order-`n`
subgroup, `dom[j] = g0^j`.

**Layout** (the house sunflower chart layout, cg_petal_census /
bsr_check conventions): `L = (Z, {T_1..T_{t_ch}}, B)` with

```text
core       Z,  |Z| = k-1,
petals     T_i, pairwise disjoint 2-point sets disjoint from Z
           (fiber-aligned house instance: K_2-cosets {x, -x}; printed
            quotient scale M = 2),
background B = the rest, b0 := |B| <= 1
           (b0 = 1 exactly when k is even; B = {-x_nf} in the
            fiber-aligned even-k layout — the chart residual home,
            |R0| <= b0 < ell).
```

`t_ch := t_ch(L)` = the layout/chart petal count. For the even-`k`
fiber-aligned layout `t_ch = (n-k)/2` (bsr_check: `t_ch = len(petals)`;
catch #58's chart-local pin, operationalized as in every banked
measurement). Lemmas B/C/D below are PURE COMBINATORICS: they hold for ANY
disjoint 2-set petal system (coset structure not consumed) and any word.

**Contributor / class / chart data.** A contributor to a received word `U`
(any function `H -> F_q`) is a codeword `f` (deg `f < k`) with EXACT
agreement set `S = agr(f, U)`, `|S| >= k + sigma = k+1`. A class is the
support `S` (distinct classes = distinct supports; `|S| >= k+1 > deg f`
pins the codeword — `petal_g3_full_support_codeword_injectivity`, PROVED,
one line). Scale `c(S)` = the dyadic translation-stabilizer order;
aperiodic means `c(S) = 1`. Chart data of `S` w.r.t. `L`:

```text
d   = |Z \ S|      (missed core),      j = |S n Z| = k-1-d,
m   = #{ i : T_i <= S }                (touched petals),
s_r = |S n B|      (<= b0 <= 1).
```

Full-petal: `S n T_i in {empty, T_i}` for every `i`.

**FLOOR BAND (pin P1 deep reading, AS POSED in clause (P)):**

```text
d >= ell (t_ch - 2) = 2 (t_ch - 2).
```

**LAYOUT ANCHORING PIN (catch #168, minted here — load-bearing).** The
floor band is read against ONE fixed layout per (row, word) — the layout
the atlas/compiler carries, as in every banked measurement (the word's own
layout at chart words). The layout-EXISTENTIAL reading ("`S` is floor-band
w.r.t. SOME layout") is PRE-FALSIFIED by core re-basing: every wide-band
odd-lift class (the #145 family) becomes floor-band in a tailored layout
(constructive: cp_proof.md section 5; verified in vivo, cp_verify P6), so
that reading inherits the #145 kill `C(63,32) = 2^59.67 > (121/128)128^6 =
2^41.92` verbatim. All results below are per fixed layout, UNIFORMLY in
the layout.

---

## THEOREM P (clause (P), proved form)

Fix any row `(n, k)`, any layout `L` as above, and ANY received word `U`.
Write `thr = 2(t_ch - 2)` and `J := (k-1) - thr = k + 3 - 2 t_ch`.

**(P-i) EMPTINESS LAW (all scales, not only the hazard family).** If
`J < 0` — equivalently `2k < n - 3` at the even-`k` fiber-aligned layout —
then NO contributor of ANY scale is floor-band (`d <= |Z| = k-1 < thr`).
On even-`k` 2-power rows: floor band nonempty `<=>` `2k >= n`, i.e. rate
`>= 1/2` (no even-`k` 2-power row has `2k = n-2`; parity). In particular
at official rates `1/4, 1/8, 1/16` clause (P) holds with the EMPTY atlas
and weighted census 0.

**(P-ii) RIGIDITY.** Every floor-band full-petal class satisfies

```text
j = |S n Z| <= J        and        m in { t_ch - 1, t_ch }.
```

At rate 1/2 (`n = 2k`): `J = 3` exactly, for every row size.

**(P-iii) CENSUS (word-free, q-free, scale-free).** The number of
floor-band full-petal classes of `U` (aperiodic AND periodic together) is
at most

```text
N_max = 2^{b0} * (t_ch + 1) * S_J(k-1),     S_J(k-1) = sum_{i=0}^{J} C(k-1, i).
```

At rate 1/2: `N_max = 2 (t_ch + 1)(1 + (k-1) + C(k-1,2) + C(k-1,3))`.

**(P-iv) ATLAS.** The WORD-INDEPENDENT atlas

```text
A^prim(L) := { chart(D0, R) :  D0 <= Z, |D0| >= thr,  R <= B }
```

— each chart the fixed `(D0, R0=R)` sunflower auxiliary layer over the
FULL petal set (`m_chi = t_ch` coset petals at printed scale 2, `|R0| <=
b0 < ell`, retained-zero flavor per `R`, dictionary `a = sigma + d + 1 -
|R0|`) — covers every floor-band full-petal contributor: the first (and
only) covering chart of class `S` is `(Z \ S, S n B)`. Every chart
satisfies K4's chart hypotheses (`|R0| < ell`, band `d >= ell(m_chi - 2) =
thr`). The paid weighted census is EXACTLY

```text
sum_chi (m_chi + 1) = 2^{b0} * (t_ch + 1) * S_J(k-1) = N_max,
```

and at every rate-1/2 row `n = 2k >= 8`:

```text
N_max <= (121/128) n^6,
```

with margin ~ `90.75 n^2` (exact at the binding official row `n = 2^41`:
`N_max = 2^157.42`, budget `2^245.92`, margin `2^88.50`; cp_verify P7,
exact bigint, verified for all `s = 3..44` and the four official maximal
rows).

**(P-v) PER-CHART K4 LINE, RE-PROVED WORD-FREE.** Within one chart
`(D0, R)`, a covered class is DETERMINED by its touched petal set (its
support is `(Z \ D0) u petals(M) u R`), and admissible touched sets have
size in `{t_ch - 1, t_ch}`: at most `t_ch + 1` classes per chart — K4's
`m_chi + 1` bound holds for these charts by support counting alone (no
layer map, no auxiliary word, no dictionary transport consumed). The
aggregate primitive payment is therefore `<= N_max` unconditionally.

**(P-vi) APERIODIC CLAUSE / HAZARD CALIBRATION.** The aperiodic
sub-family is covered a fortiori. The #145/#153 two-family lift caps embed:
at `(128, 64)`, `993 + 31 = 1024 <= N_max = 2,754,048`; measured floor
censuses (53 at `(32,16,97)`, 48 at `(32,16,193)`, 8 at `(16,8,97)`, 0 at
`(32,12,97)`) all reproduce and sit under the per-cell caps (cp_verify
P1-P3).

## Consumed hypotheses (complete list)

1. `petal_g3_full_support_codeword_injectivity` (PROVED; classes =
   supports). Nothing else mathematical: (P-i)-(P-v) are self-contained
   combinatorics (proofs in cp_proof.md, machine-verified).
2. Pin P1 = FLOOR reading, AS POSED (decision-gate; the pre-registered
   tripwire (P)-3 stands: if P1 resolves wide, #145 falsifies (P) and the
   odd-lift carve-out is owed — quantified in cp_findings #171).
3. Layout anchoring (catch #168, this packet): one fixed layout per
   (row, word) — the banked operational semantics. The layout-existential
   reading is refuted constructively (not assumed away).
4. NOT consumed: G4 dictionary transport, prop:capf-pma, K4-as-a-node, any
   q condition, any label/torus structure, chart-word form of `U`. The
   packet's bounds are word-free; K4's per-chart line is re-derived
   independently at these charts (P-v), so no new seam is created.

## Falsifiers (pre-registered, executable)

- **F1:** a realized floor-band full-petal class with `j > J` or
  `m < t_ch - 1` at any cell (complete enumeration executable at n <= 16;
  candidate-complete at n = 32 via brute cross-validation at n = 16).
- **F2:** any floor-band full-petal contributor at an official-rate-<=-1/4
  shaped row (complete enumeration executable at (16,4)).
- **F3:** a cell where `N_max > (121/128) n^6` at rate 1/2 (pure bigint).
- **F4:** a floor-band full-petal contributor not covered by
  `A^prim(L)`, or a chart of `A^prim(L)` violating a K4 hypothesis.
- **F5 (inherited (P)-3):** pin P1 resolved wide without the odd-lift
  carve-out — clause (P) then falls by #145's arithmetic, not this packet.
