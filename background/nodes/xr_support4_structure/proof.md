# Proof

Notation as in `statement.md`. Inputs consumed: L1 / dual bases
(`xr_two_slope_cost_theorem`), the banked pair-core k-packing
(`background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`)
through hypothesis (T), and the adv_sublinear_rank support-`<= 3`
transversality record.

## Claim 1 (S4-1: triple-locus localisation)

Let `(c_a)` satisfy `sum_a e(z_a) (x) c_a = 0`, `e(z) = (1, z)` (for
`z = (0:1)` read `e = (0, 1)`). Evaluate at a point `x`: in `F_q^2`,

```text
sum_a c_a(x) e(z_a) = 0.
```

The `e(z_a)` are PAIRWISE linearly independent (distinct points of
`P^1`). If exactly one `c_a(x) != 0`, then `c_a(x) e(z_a) = 0` —
impossible. If exactly two, `c_a(x) e(z_a) = -c_b(x) e(z_b)` with
independent directions — impossible. So at every `x` the number of
nonzero components is `0` or `>= 3`; a point of `supp(c_a)` lies in
`S_a` and in the supports of at least two other rays of the relation
(as `supp(c_b) <= S_b`), hence in the triple locus. QED (1)

## Claim 2 (S4-2': general-position kill; K_V no-relation)

If `|S_a ^ (triple locus)| <= k` for every `a`, then by Claim 1 each
`c_a` is supported on `<= k` points; a nonzero element of `C_{S_a}`
has weight `>= k + 1` (its support carries a word orthogonal to the
MDS code `RS_k`, and any `k` columns of the dual are independent), so
`c_a = 0` for all `a`: `Rel = 0` and `rank = V h` exactly.

K_V instance: supports `S_a = Y u (union of pair blocks B_ab) u
(top-up_a)` with `Y` common of size `k - 1`, the `B_ab` in exactly
the two supports `a, b`, top-ups private. The triple locus is exactly
`Y`, of size `k - 1 <= k`, so K_V carries NO relation: the banked
rank measurement (`rank = V h` in all 13 fixtures, 104/104) is now a
THEOREM. QED (2)

## Claim 3 (S4-3: rank-2 rigidity)

Let the relation have support exactly `{1, 2, 3, 4}`. The two
component equations read `c_3 + c_4 = -(c_1 + c_2)` and
`z_3 c_3 + z_4 c_4 = -(z_1 c_1 + z_2 c_2)`; the matrix
`[[1, 1], [z_3, z_4]]` is invertible (`z_3 != z_4`), so `c_3, c_4`
are linear combinations of `c_1, c_2`: all four lie in
`L := span(c_1, c_2)`, of dimension `<= 2`; dimension exactly 2
because `c_2 = t c_1` would, by the same inversion applied to the
pairs `{1,3}, {1,4}`, make every `c_a` a multiple of `c_1` — then
supp`(c_1) <= S_a` for all four (each `c_a != 0` on the support-4
relation), so `S_1 ^ S_2 ^ S_3 ^ S_4` contains the `>= k + 1` points
of `supp(c_1)`, and the triple intersections exceed `k - 1`,
violating (T). QED (3)

## Claim 4 (S4-4: Mobius / cross-ratio criterion)

By Claim 3 any support-4 relation lives in a fixed 2-dimensional
`L`, with the direction of ray `a`'s component pinned to a point
`zeta_a in P(L)` (in the U-mechanism, `c_a` must be a multiple of
the unique minimum-weight word `e_{y_a}` compatible with
`supp(c_a) <= S_a ^ U = U \ {y_a}`; in general `zeta_a` is the
forced direction the localisation admits). Writing `c_a = t_a w_a`
with `w_a` a fixed representative of `zeta_a` and coordinates
`w_a in F_q^2` for `L`, the relation `sum_a t_a e(z_a) (x) w_a = 0`
is a nonzero kernel vector of the `4 x 4` Segre matrix with columns
`e(z_a) (x) w_a in F_q^2 (x) F_q^2`. Its determinant vanishes iff
the four points `([1:z_a], zeta_a)` of `P^1 x P^1` lie on a
`(1,1)`-divisor (`alpha + beta z + gamma w + delta z w = 0`, a
4-dimensional coefficient space — the classical Segre condition),
which for four points in general position is equivalent to the
cross-ratio equality `CR(z_1..z_4) = CR(zeta_1..zeta_4)` (a
`(1,1)`-divisor is the graph of a Mobius transformation carrying
`z_a -> zeta_a`; Mobius maps preserve cross-ratio, and conversely a
cross-ratio match defines the interpolating Mobius map). When it
vanishes, the kernel is 1-dimensional for distinct `z_a` and
distinct `zeta_a` (any two columns are independent), so the relation
is unique up to scalar. At fixed supports the equality is one
equation in the slopes: codimension 1. Minimal case: `|U| = k + 2`
gives `L = C_U`; the weight-`(k+1)` words of `C_U` are exactly
`e_y = lam^U (x - x_y)|_U`, and identifying `P(L)` by the pencil
parameter gives `zeta_y = x_y`. QED (4)

## Claim 5 (S4-14: connectivity floor)

**MDS sum lemma.** If `|X ^ S| >= k` then
`dim(C_X + C_S) = (|X| - k) + (|S| - k) - (|X ^ S| - k)
= |X u S| - k = dim C_{X u S}` (L1 for the intersection), and
`C_X + C_S <= C_{X u S}` is clear; equality follows.

**Floor.** For finite slopes, `pi_1(G_{z_a}(C_{S_a})) = C_{S_a}`, so
`pi_1(Row) = sum_a C_{S_a}`. Pairwise intersecting (`>= k`) makes
the union connected in the lemma's sense: adding supports one at a
time, each new `S_a` meets the accumulated union in `>= k` points
(it meets ONE existing support in `>= k` points), so by induction
`sum_a C_{S_a} = C_{union}`, of dimension `m`. Hence
`rank >= dim pi_1(Row) = m`. Also every row lies in
`C_union x C_union` (each `c in C_{S_a} <= C_union`), so
`rank <= 2m`. Charge per ray `rank/V in [m/V, 2m/V]`; if
`V <= m/2` then `rank/V >= m/V >= 2` — the occupancy per-ray floor
holds automatically (definitions item 12). QED (5)

## Claim 6 (escape floor / peeling)

By Claim 1, every relation of the system is supported inside the
triple locus, so it is also a relation of the peeled system
`(z_a, S_a ^ W)`, `W` = triple locus (the component `c_a` lies in
`C_{S_a ^ W}`); iterating to the stable limit `S_a^inf`:
`Rel <= (+)_a C_{S_a^inf}`, so
`dim Rel <= sum_a max(0, |S_a^inf| - k)`. Then

```text
rank = V h - dim Rel >= sum_a ( h - (|S_a^inf| - k)^+ )
     = sum_a min( h, |S_a \ S_a^inf| )           (the ESCAPE floor)
```

— the per-ray term is `|S_a| - |S_a^inf| = |S_a \ S_a^inf|` when
`|S_a^inf| >= k`, and caps at `h` when `|S_a^inf| < k` (a ray never
contributes more than `h`). This is the pilot's S4-15 form
`rank >= sum_a min(h, |S_a \ S_a^inf|)`, reproduced exactly on the
fixtures (U-mechanism: floor 16, rank 19; K_V: floor 35 = rank,
where the naive uncapped sum 40 would be FALSE — the cap is
load-bearing). If every ray escapes `>= 2` points
(`|S_a \ S_a^inf| >= 2`, which holds whenever every ray support has
`>= 2` points lying in at most two supports) and `h >= 2`, then
`rank >= 2V`: per-ray charge `>= 2` — the escape form of the
occupancy heart. QED (6)

## Claim 7 (zero-escape collapse — MEASURED, not proved)

For zero-escape cliques the floor above degenerates
(`S_a^inf = S_a`) and the measured value across exhaustive slope
sweeps is `rank = 2m` EXACTLY (3,876 + 8,855 tuples at two
fixtures, never `2m - 1`; reproduced on 60 deterministic tuples by
the verifier). At `rank = 2m`, `Row = C_union x C_union` and any
realising `(u, v)` is annihilated by `C_union x C_union`, i.e.
`(u, v)` is jointly explained on `union S_a` — a single deep pair,
not a family (the T3-type collapse). **Status: measurement.** The
named open sub-items of record: prove the collapse; prove
`V <= m/2` for non-collapsing systems. Secondary exact criterion
from the pilot: the zero-escape channel can reach per-ray charge
`< 2` only when `k > 2h^2` — margins `2.7e8`-`5.4e8` at the prize
rows; at the RowC toy rows `k > 2h^2` HOLDS and the collapse
measurement is the load-bearing kill there (honest limitation of
the arithmetic route, kept from the record).

## Claim 8 (U-mechanism, calibration)

Construction as in `statement.md`; the combinatorial identities
(`|S_a| = A`, pairwise `k + d`, triples exactly `k - 1`) are direct
counting from the builder's blocks. `S_a ^ U = U \ {y_a}` forces
(Claim 1 localisation + the minimal-case pencil picture) each
component to be a multiple of `e_{y_a}`, weight exactly `k + 1`;
Claim 4 then gives: a relation exists iff
`CR(z_1..z_4) = CR(x_{y_1}..x_{y_4})`, and the Mobius-matched
builder (`z_a = nu(x_{y_a})`, `nu in PGL_2`) satisfies it for EVERY
4-subset of rays; `dim Rel = 1` at `V = 4` (uniqueness up to
scalar) and deficit `<= 1` per ray in clusters (S4-10 no stacking:
cluster deficit `= V - 3` exactly, rank `= V(h-1) + 3`). Full-gate
admissibility is the pilot's 6/6 fixture record (toy). Re-pricing:
the deficit is 1 against a per-ray charge of order `h`, so the
banked prize-row numbers are UNCHANGED (relative `1e-10`); at RowC
1/4, `d = 1`, the builder packs 51 clusters of `V = 5` rays on 10
points each: `U_N = 51 x C(5,2) = 510` data vs K_V's 384
(`x 1.328125`), two below `n/2 = 512` — the sharpest surviving
margin of SHARP-OCC's weak form. (The 51-cluster budget formula is
the pilot's; the verifier checks its arithmetic consistency, not
its derivation — flagged.) QED (8, with the stated scope)

## Honest scope

Claims 1-6 and the structure half of 8 are complete proofs. Claim 7
is a measurement and says so. Toy-verified: full-gate admissibility,
the exhaustive slope sweeps, the stage JSON pins (`dim_rel = 1`,
`rank = 19` at the `(3,5,1,4)` fixture; escape floor `16`, cap `4`;
KV `rank = Vh`, `S^inf` sizes `2`). Not re-derived: the
official-scale cluster packing; the double-hole family; support-3
transversality (consumed).
