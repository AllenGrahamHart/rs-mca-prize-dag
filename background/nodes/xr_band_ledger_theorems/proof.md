# Proof

Notation and hypotheses as in `statement.md`. (H1) is the banked
k-packing; the fibre identity (core = support intersection, exactly)
is `xr_two_slope_cost_theorem` Lemma 0 (= this pilot's THEOREM 2, not
re-stated).

## Claim 1 (THEOREM 3: line cap under `J >= k`)

Let `P = (f, g)` have `|Z_P| = J >= k` and let `z` be a slope whose
forced ray `c_z = f + zg` has agreement set `S_z` of size `>= A`
against `w_z = u + zv`. `S_z` contains `Z_P` (on `Z_P`, `u = f` and
`v = g` pointwise, so `w_z = c_z` there), hence `S_z \ Z_P` has size
`>= A - J`. For two such slopes `z != z'`, a point
`i in (S_z \ Z_P) ^ (S_{z'} \ Z_P)` would satisfy
`e_i + z e'_i = 0 = e_i + z' e'_i` (`e = u - f`, `e' = v - g`),
forcing `e_i = e'_i = 0`, i.e. `i in Z_P` — contradiction. So the
sets `S_z \ Z_P` are pairwise disjoint inside the `n - J` points off
`Z_P`:

```text
L_P (A - J) <= n - J,   i.e.   L_P <= floor((n - J)/(A - J)).
```

QED (1). *(Four lines, hypothesis `J >= k` only — used exactly where
`common_code_line_budget`'s hypothesis `a + b - n >= k` fails.)*

## Claim 2 (THEOREM 4: ray rigidity)

Suppose distinct pairs `P_1 = (f_1, g_1)`, `P_2 = (f_2, g_2)` with
`|Z_i| >= k` are both subordinate to the ray `(z, c)` (their cores lie
in its agreement set). Interpolation on `Z_i` (size `>= k`) forces
`c = f_i + z g_i` for both `i` (on `Z_i`: `c = w_z = f_i + z g_i`
pointwise, both sides degree `< k`... `c` has degree `< k` and agrees
with the degree-`< k` polynomial `f_i + z g_i` on `>= k` points, so
they are equal). Equating: `f_1 - f_2 = -z (g_1 - g_2)`. If
`g_1 = g_2` then `f_1 = f_2`, contradicting distinctness; otherwise
`z` is the unique scalar of proportionality — so a SECOND common ray
`(z', c')` with `z' != z` is impossible, and a second common ray with
the same slope `z` would have `c' = f_1 + z g_1 = c`. At most one
common ray, keyed on the ray, with the proportionality identity. QED
(2)

## Claim 3 (THEOREM 5 + corollary)

**Union identity.** If `f_1 - f_2 = -z^* (g_1 - g_2)`, put
`c := f_1 + z^* g_1 = f_2 + z^* g_2`. On `Z_1`:
`u + z^* v = f_1 + z^* g_1 = c` pointwise; on `Z_2` likewise. So `c`
agrees with `w_{z^*}` on ALL of `Z_1 u Z_2`.

**Corollary.** By (H1), `|Z_1 ^ Z_2| <= k - 1`, so
`|Z_1 u Z_2| >= (k+d_1) + (k+d_2) - (k-1) = k + d_1 + d_2 + 1`. If
`d_1 + d_2 >= h` this exceeds `A = k + h`: an agreement `> A` at
direction `z^*` — a T2/P2 tangent event; the received pair leaves the
generic branch. (For `z^*` at `0` or `(0:1)` — `f_1 = f_2` or
`g_1 = g_2` — the same identity holds against `w_0 = u` or
`w_{(0:1)} = v`; this is where the pencil-wide gate is used.)

**Automatic proportionality at overlap `k - 1`.** If
`|Z_1 ^ Z_2| = k - 1` exactly, both `f_1 - f_2` and `g_1 - g_2` are
degree-`< k` polynomials vanishing on the `k - 1` overlap points,
hence constant multiples of its vanishing polynomial, hence
proportional — the shared-block class strips itself. QED (3)

## Claim 4 (THEOREM 7: two-column determinacy)

Fix a coordinate `i` and pairs `P_1, P_2` with directions
`z_s = zeta_{P_s}(i)` (defined whenever
`(u_i, v_i) != (f_s(x_i), g_s(x_i))`; the direction is the slope of
the line joining the received point `(u_i, v_i)` to the pair's centre
`(f_s(x_i), g_s(x_i))` in `A^2`, in the pencil parametrization
`e + z e' = 0`). If `z_1 != z_2`, the linear system

```text
u_i + z_s v_i = f_s(x_i) + z_s g_s(x_i)     (s = 1, 2)
```

has determinant `z_2 - z_1 != 0` and so determines `(u_i, v_i)` —
and with it `zeta_P(i)` for every other pair `P`. This is why
steering attacks control exactly TWO pairs per coordinate (the
battery's shared-block finding), and why band occupancy is a
point-line incidence question in `A^2`. QED (4)

## Claim 5 (master ledger + pricing)

Every slope in `Gamma_band` is, by definition, live for some band
pair `P` with `L_P >= 2`, so
`|Gamma_band| <= SUM_P L_P <= SUM_d N_d max_{|Z|=k+d} L_P
<= SUM_d N_d L(d)` with `L(d) = floor((R - d)/(h - d))` by Claim 1 at
`J = k + d` (note `n - J = R - d`, `A - J = h - d`).

**Pricing (exact integers, recomputed by the verifier).**
Band-proper sum `SUM_{d=1}^{h-2} L(d)`: substituting `g = h - d`,
`SUM_{g=2}^{h-1} floor((R - h + g)/g) = (h - 2) + SUM_{g=2}^{h-1}
floor((R-h)/g)`, evaluated by divisor blocks at the prize rows.
Pins: 828 / 967 / 479 (RowC), 36,839,268,578,566 /
43,010,571,891,409 / 44,764,496,190,275 (prize) — matching the
pilot's persisted `band_arith.json` (and the occupancy-v2
`arith.json` independently). `L(h-1) = floor((R-h+1)/1) = R - h + 1
= n - A + 1` exactly. The printed-column comparison (`SUM_d L(d)` vs
`n - A + 1`): 828 > 764, 967 > 892, 479 <= 958, and the prize rows
exceed by ~22x — dead on 5 of 6 rows even at `N_d = 1`, hence the
third-generic-column design of record. QED (5)

## Warning W (Theorem 6 — bijection, recorded against misuse)

Fix a ray `(z, c)`, `z != 0`, with agreement set `S`, `|S| = A`. If
`P = (f, g)` is subordinate with `|Z_P| >= k`, then `c = f + zg`
(Claim 2's interpolation step), so `f = c - zg` and, for `i in S`,
`u_i + z v_i = c(x_i)` gives `u_i - f(x_i) = z(g(x_i) - v_i)`: hence
`i in Z_P iff g(x_i) = v_i`. The map `g -> (c - zg, g)` is thus a
bijection between codewords of the punctured code `C|_S` (an
`[A, k, h+1]` MDS code) with `#{i in S : g(x_i) = v_i} >= k` and
pairs subordinate to the ray with `|Z_P| >= k`. Per-ray multiplicity
is an MDS list size at agreement `k+1` out of `A` — below Johnson,
unbounded by anything banked. The master inequality is therefore
lossy in general; the amendment of record adds: it is WORST-CASE
TIGHT (slack `1.000` attained; the max-`N_d` sunflower family sits at
exactly `2.000`), so slope-counting reformulations buy at most a
factor 2. This W is context for consumers; it asserts no bound.

## Honest scope

Claims 1-4 are complete proofs from (H1) + (H3) + interpolation.
Claim 5's inequality is proved; its pricing is exact arithmetic at
the pinned rows. Toy-verified: tightness of the cap, the fixture
battery (0 violations across > 4e7 pair comparisons in the pilot
record; fresh fixtures here), the slack-2.000 sunflower point.
Nothing here bounds `N_d`.
