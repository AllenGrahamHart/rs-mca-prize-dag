# cp_proof — CLAUSE (P) at the floor band: proofs
# Companion to cp_statement.md. All notation from there.

## 1. Lemma A (emptiness law) — (P-i)

A floor-band class needs `thr = 2(t_ch - 2) <= d <= |Z| = k-1`, i.e.
`J = (k-1) - thr >= 0`. For the even-`k` fiber-aligned layout
`t_ch = (n-k)/2`, so `J = k+3-2t_ch = 2k - n + 3`, and `J >= 0 <=>
2k >= n-3 <=> 2k >= n-2` (integers, both sides even). On a 2-power row
with `k` even, `2k = n-2` would force `k = n/2 - 1`, which is odd for
`n >= 8` — impossible; hence nonempty `<=> 2k >= n <=> rho >= 1/2`.
At official rates `1/4, 1/8, 1/16`: `2k in {n/2, n/4, n/8} < n-3` for
`n >= 8`, so NO contributor of any scale lies in the floor band; the
empty atlas discharges clause (P) with weighted census 0. QED.

*Remark (boundary bookkeeping, part of catch #169).* bsra_findings' law
is printed as `z0 >= 0 <=> 2k >= n-1` using the half-integer formalization
`t_ch = (n-k+1)/2`; the operational `t_ch = len(petals) = (n-k)/2` (even
`k`) gives `2k >= n-2`. The two disagree only at `2k = n-2`, which no
even-`k` 2-power row attains — immaterial in scope, recorded for honesty.
Lemma A also STRENGTHENS the banked law from the odd-lift hazard family
(#145/#153: `z0 >= 0 <=> ...`) to ALL contributors of every scale: the
same threshold empties the entire band, not just the hazard.

## 2. Lemma B (rigidity) — (P-ii)

Let `S` be floor-band full-petal, `|S| >= k+1`. The layout partitions the
row, so

```text
|S| = j + 2m + s_r,          j = k-1-d,   s_r <= b0 <= 1.
```

From `|S| >= k+1`: `2m >= (k+1) - j - s_r = d + 2 - s_r >= d + 1`, so
`m >= ceil((d+1)/2)`. Floor band `d >= 2 t_ch - 4` gives
`m >= ceil((2 t_ch - 3)/2) = t_ch - 1`; trivially `m <= t_ch`. And
`j = k-1-d <= (k-1) - (2 t_ch - 4) = J`. QED.

At rate 1/2 (even-`k` fiber-aligned, `t_ch = k/2`): `J = 2k - n + 3 = 3` —
floor-band full-petal contributors agree on AT MOST THREE core points,
for every row size, every word, every field. This single inequality is
what kills both banked hazards at once: the #145 odd-lift mass lives at
`j = 2z+1`, so `j <= 3 <=> z <= 1 = z0` (the banked floor cap), and the
#138 exponential periodic mass lives at `j ~ 2z` with `z` hypergeometric-
large (`~ k'/2`), far above 3 — the g1a falsification never enters the
floor band (consistency check in cp_findings, item C3).

## 3. Lemma C (census) + Theorem (atlas) — (P-iii), (P-iv), (P-v)

**Census.** A floor-band full-petal class is DETERMINED by the triple
`(S n Z, touched petal set, S n B)`, since
`S = (S n Z) u (union of touched petals) u (S n B)`. By Lemma B the
admissible triples number at most

```text
S_J(k-1)  *  [ C(t_ch, t_ch - 1) + C(t_ch, t_ch) ]  *  2^{b0}
   =  S_J(k-1) * (t_ch + 1) * 2^{b0}  =  N_max .
```

Classes inject into supports (`petal_g3_full_support_codeword_injectivity`
/ one line: two deg `< k` polynomials agreeing on `|S| >= k+1 > k-1`
points coincide, and a class IS its support). Hence #classes `<= N_max`,
uniformly in `U`, `q`, and the scale distribution. QED.

**Atlas.** `A^prim(L) = {(D0, R) : D0 <= Z, |D0| >= thr, R <= B}`:

1. *Legality.* Each chart is a fixed `(D0, R0 = R)` sunflower layer over
   the full petal set: `m_chi = t_ch` coset petals (printed scale `M = 2`
   in the fiber-aligned instance), `|R0| <= b0 <= 1 < ell = 2`, retained-
   zero flavor per `R`, agreement dictionary `a = sigma + d + 1 - |R0|`
   with `d = |D0|`. The chart band `d >= thr = ell(m_chi - 2)` holds by
   the index constraint — every chart satisfies K4's chart hypotheses
   (`petal_top_band_tail_collapse` applies verbatim: `ell = 2 > r >= 0`,
   `m_chi >= 2`, `d >= ell(m_chi - 2)`).
2. *Coverage + first-match.* A floor-band full-petal class `S` is covered
   by `(Z \ S, S n B)`: `|Z \ S| = d >= thr` puts it in the index, the
   chart's petal set contains all of `S`'s petals (it contains ALL
   petals), the missed core is exactly `D0`, the residual flavor matches.
   No other chart covers `S` under exact-missed-core matching, so ANY
   fixed total order gives first-match assignment with zero overlap.
3. *Weighted census.* `#A^prim = S_J(k-1) * 2^{b0}` charts (choose the
   AGREED core `Z \ D0`, size `<= J`; choose `R`), each of weight
   `m_chi + 1 = t_ch + 1`:

   ```text
   sum_chi (m_chi + 1) = 2^{b0} (t_ch + 1) S_J(k-1) = N_max.
   ```

4. *Budget.* At rate 1/2 (`t_ch = n/4`, `b0 = 1`, `J = 3`):
   `N_max = 2(n/4 + 1)(1 + (k-1) + C(k-1,2) + C(k-1,3)) <= n^4` for all
   `n >= 8` (crudely `S_3(k-1) <= k^3 = n^3/8` for `k >= 8`, and small
   rows check directly), while `(121/128) n^6 >= 0.945 n^6`. Exact bigint
   verification over `s = 3..44` and at the four official maximal rows in
   cp_verify P7; binding official row `n = 2^41`: `N_max ~ 2^157.42` vs
   budget `~ 2^245.92`, margin `2^88.50`. At official rates `<= 1/4`,
   Lemma A: census 0.

5. *(P-v), per-chart K4 line word-free.* Two classes covered by the SAME
   chart `(D0, R)` have the same `S n Z = Z \ D0` and same `S n B = R`;
   they can differ only in the touched petal set, which by Lemma B has
   size `t_ch - 1` or `t_ch`: at most `t_ch + 1` admissible sets, so at
   most `m_chi + 1` classes per chart. This re-proves, for these charts,
   exactly the bound K4 supplies — with no layer map, auxiliary word, or
   dictionary transport consumed. The aggregate (aperiodic) primitive
   payment is `<= sum_chi (m_chi + 1) = N_max` unconditionally. QED.

*Why this does not contradict the P3-curse (#139).* The curse ("`<= 1`
class per chart makes coverage expensive") binds when the demanded class
family is exponential (the periodic band census at chart words). Here the
demanded family is itself `<= N_max = poly` BY RIGIDITY, and moreover the
floor-band charts hold up to `t_ch + 1` classes each (uniqueness at
`ell' = 1` descended band charts does not apply to these official-row
`ell = 2` full-petal charts). The mission brief's reading is exact: at the
floor band the aperiodic/primitive family is the SMALL family, and
counting closes it.

## 4. Complement / aperiodic-locus analysis (mission item 4 — reusable)

Setting: even-`k` fiber-aligned CHART word `U = (X - x_nf) u1(X^2)` (csp
S2), `n' = n/2`, `k' = k/2`. For any codeword `f`, write the parity
decomposition `f = f0(X^2) + X f1(X^2)` (`deg f0, f1 <= k'-1`) and define

```text
h := f0 + x_nf * f1     in F_q[Y],   deg h <= k'-1.
```

**(A) Fiber-agreement dichotomy.** For a fiber `{x, -x}` over `y = x^2`:
- petal fiber (`U = c_i L_Z` there): both points agree `<=> h(y) = 0 AND
  f1(y) = u1(y)`;
- core fiber (`U = 0`): both agree `<=> f0(y) = f1(y) = 0 => h(y) = 0`
  (and `f1(y) = 0 = u1(y)`);
- split fiber `{x_nf, -x_nf}` (`U = 0`): `x_nf` agrees `<=> h(y_nf) = 0`;
  `-x_nf` agrees `<=> (f0 - x_nf f1)(y_nf) = 0`.

So with `Y_full := {y : pi^{-1}(y) <= S}` and the split half-agreement,
`Z(h) >= Y_full u {y_nf if x_nf in S}`. Since `deg h <= k'-1`:

**(B) Lift dichotomy (exact).** `|Y_full| + [x_nf in S] >= k'  =>  h = 0
<=> f = (X - x_nf) f1(X^2)` — the S3/S4 lift form; aperiodic iff
`f1(y_nf) != 0` (#145's family). Conversely every non-lift contributor
has `|Y_full| + [x_nf in S] <= k'-1`. This is the exact complement of the
diamond-cofactor locus: the g1a torus analysis lives on the lift branch
with `g(y_nf) = 0` (periodic; one DIAMOND equation per class, mass
`~ C/q`); the branch `g(y_nf) != 0` carries NO consistency equation at
`|agr| = k'` (interpolation always solves) — this is exactly why the
aperiodic wide-band mass is q-FREE and supply-complete (#145, measured
93-92 percent of `C(n'-1,k')` at two primes). ANSWER to the mission's
item-4 question: the torus/rank analysis gives NO suppression on the
aperiodic lift locus (rank 0 — no equations), and rank `>= 1` only on the
non-lift aperiodic locus, as follows.

**(C) Floor-band structure at rate 1/2 (exact).** Let `S` be floor-band
full-petal, non-lift. By Lemma B, `m >= t_ch - 1 = k'-1` full petal
fibers, so `|Y_full| >= k'-1`; non-lift forces `|Y_full| + [x_nf in S] =
k'-1` exactly: `m = k'-1`, no full core fiber, `x_nf notin S`, and

```text
h = c * L_{Y_full},   c != 0   (deg h <= k'-1 with k'-1 known roots),
f1 = interp(u1 | Y_full) + lambda * L_{Y_full}
```

— a TWO-parameter family `(c, lambda)` per touched-petal choice, which
must still produce `>= 3` half-agreements (`|S| = j + 2(k'-1) + s_r >=
2k'+1 => j + s_r >= 3`) at prescribed core/residual points, each one an
affine condition in `(c, lambda)` with label-dependent coefficients: on
the label torus this is a rank-`>= 1` system after eliminating `(c,
lambda)`, giving first-moment `E[#non-lift floor classes] = O(poly(n)/q)`
— the "aperiodic accidents decay ~ 1/p" law of the 372-cell tables, now
with a mechanism. (First-moment grade; NOT consumed by Theorem P — the
counting bound holds for every word regardless.)

**(D) Wide-band complement (what survives outside the floor).** Non-lift
full-petal contributors in the wide band have `|Y_full| <= k'-1` but no
`m`-rigidity; their supports satisfy `|S| <= 2(k'-1) + (half-agreed
points)`, with every half-agreement carrying one affine condition — the
same torus scaffold, rank `>= (|S| - 2|Y_full|) - 2` heuristically. The
aperiodic wide-band TRUTH remains the lift supply `~ C(n'-1, k') +
C(n'-1, k'+1)` (q-free, #145): upper and lower bounds now match at
binomial scale, so NO wide-band budget rescue exists at any field size —
the floor band is the unique poly window. This quantifies the P1
decision-gate stakes (cp_findings #171).

## 5. Catch #168 construction (layout re-basing; kills the
## layout-existential reading)

Let `f = (X - x_nf) g(X^2)` be any wide-band odd lift at rate 1/2 with
`|agr(g, u1)| = k'` and `z = |agr n Z'| >= 2` (floor-EXCLUDED in the
word's own layout: `d = 2(k'-1-z) < 2(t_ch - 2)`). Its support is
`S = {x_nf} u pi^{-1}(A)`, `|A| = k'`. The row has `n' = 2k'` fibers;
outside `A` and the split fiber there are `n' - k' - 1 = k'-1` fibers.
TAILORED LAYOUT `L*`: core `Z* =` those `k'-1` full fibers `u {x_nf}`
(size `2(k'-1)+1 = k-1` — legal), petals = the `k'` fibers of `A`
(`t* = k'`), background `{-x_nf}`. Then w.r.t. `L*`: `S` is full-petal
(`m* = t* = k'`), `j* = |S n Z*| = 1`, `d* = k-2 >= 2(t* - 2)` — FLOOR
BAND. Every `|S| = k+1` lift is re-basable this way (the count of spare
fibers fits exactly), so the layout-existential floor census at `(128,64)`
is `>= 6012/6435`-fraction of `C(63,32) = 2^59.67 > 2^41.92` — the #145
kill transports verbatim. Hence the floor band protects ONLY as a
per-layout notion; clause (P) must be (and in this packet is) read
layout-anchored. Verified in vivo at `(32,16,97)` (cp_verify P6/M4).

## 6. What is NOT claimed

- Nothing about the wide band's aperiodic mass beyond section 4-D (it is
  outside clause (P) as posed; its fate under the floor posing is the
  below-top obligation — flagged, with numbers, in cp_findings #171).
- No dictionary/layer-map transport for arbitrary words is claimed or
  needed here (P-v re-derives the per-chart bound by counting); consumers
  that want the auxiliary-image reading at chart words keep prop:capf-pma
  and pin G4 exactly as banked.
- No claim at odd `k` on official rows (official `k` is even); the
  combinatorial lemmas hold for any layout meeting Section 0's shape,
  including odd-`k` (`b0 = 0`) instances, and are machine-checked on
  non-coset layouts too.
- Mixed-petal contributors: outside the packet (petal_growth scope,
  unchanged).
