# Proof

Notation and (H1)/(H3) as in `statement.md`. Inputs consumed: the
banked k-packing
(`background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`),
L1 and the fibre identity (Lemma 0) from `xr_two_slope_cost_theorem`,
and the union-agreement identity (`xr_band_ledger_theorems` Claim 3 =
graded-band-ledger THEOREM 5), recapped where used.

## Claim 1 (THEOREM 2, low/high dichotomy)

Let `P_1 = (f_1, g_1) != P_2 = (f_2, g_2)` be codeword pairs of joint
agreement `k + d` each, `2d >= h`.

**The shared integer.** By (H1), `|Z_1 ^ Z_2| <= k - 1`, so

```text
|Z_1 u Z_2| >= 2(k + d) - (k - 1) = k + 2d + 1 >= k + h + 1 = A + 1.  (*)
```

**(a) No proportional differences.** "Proportional differences" means:
the nonzero difference pair `(f_1 - f_2, g_1 - g_2)` lies on a single
pencil direction `z^* in P^1(F_q)`, with the conventions
`z^* in F_q  <=>  f_1 - f_2 = -z^* (g_1 - g_2)` (so `z^* = 0` is
`f_1 = f_2`), and `z^* = (0:1)  <=>  g_1 = g_2`. In every case a
single codeword agrees with the pencil word `w_{z^*}` on all of
`Z_1 u Z_2`:

- `z^* in F_q`: `c := f_1 + z^* g_1 = f_2 + z^* g_2`; on `Z_i`,
  `w_{z^*} = u + z^* v = f_i + z^* g_i = c` pointwise.
- `z^* = (0:1)`: `c := g_1 = g_2`; on `Z_i`, `w_{(0:1)} = v = g_i = c`
  pointwise.

By `(*)` this agreement is `>= A + 1`, contradicting (H3). The
`(0:1)` case is exactly why (H3) must be stated pencil-wide over
`P^1` including `(0:1)` (the banked scan omitted that direction — the
occupancy pilot's gate-completeness correction). QED (a)

**(b) No live ray carries two.** Suppose a codeword `c` has agreement
set `S` against some `w_z`, `|S| <= A` by (H3), with
`Z_1 u Z_2 <= S`. Then `A >= |Z_1 u Z_2| >= A + 1` by `(*)` —
impossible. So at `2d >= h` every ray of agreement `<= A` contains at
most one depth-`d` core. QED (b)

**Consequence.** The sunflower mechanism produces, from two same-depth
data whose cores meet in `k - 1` points, a shared slope (their
differences are constant multiples of the overlap's vanishing
polynomial, hence proportional) and a live ray on the union. By (a)
this configuration is barred for `2d >= h`; it requires
`k + 2d + 1 <= A`, i.e. `2d <= h - 1`, i.e. `d <= (h-1)/2`. QED (1)

## Claim 2 (THEOREM G)

**(i)** is L1 applied to the two agreement sets:
`C_{S_1} ^ C_{S_2} = C_{S_1 ^ S_2}`, of dimension
`max(0, |S_1 ^ S_2| - k)`; nonzero iff `|S_1 ^ S_2| >= k + 1`.

**(ii)** Let `z_1 != z_2` in `P^1(F_q)`, `|S_1 ^ S_2| >= k + 1`. On
the overlap both `u + z_1 v = c_1` and `u + z_2 v = c_2` hold, and the
`2 x 2` slope system inverts (determinant `z_2 - z_1 != 0`; if one
slope is `(0:1)` the system reads `u + z_1 v = c_1`, `v = c_2` and
still inverts), giving degree-`< k` polynomials `f, g` with `u = f`,
`v = g` on `S_1 ^ S_2`. The fibre identity
(`xr_two_slope_cost_theorem` Lemma 0) upgrades containment to
equality: `Z_P = S_1 ^ S_2` EXACTLY. Both rays contain `Z_P` inside
their agreement sets by construction, so both slopes are live for `P`:
`L_P >= 2` and `P` is a two-slope band pair at depth
`e = |S_1 ^ S_2| - k >= 1`. QED (ii)

**(iii)** Two distinct cores `Z` (depth `d`) and `W` (depth `e`) inside
one agreement set `S`, `|S| <= A = k + h`: by (H1)
`|Z ^ W| <= k - 1`, so
`k + h >= |Z u W| >= (k+d) + (k+e) - (k-1) = k + d + e + 1`, i.e.
`d + e <= h - 1`. QED (iii)

## Claim 3 (core transversality)

For distinct pair cores `Z != Z'`: `(H1)` gives `|Z ^ Z'| <= k - 1`,
and `C_Z ^ C_{Z'} = C_{Z ^ Z'}` (L1) is supported on `< k` points
inside the dual of an MDS code, hence `0`. So core condition spaces
are pairwise transverse and the only pairwise sharing channel between
two-slope data is the ray-support overlap of (ii). QED (3)

## Honest scope

- Claim 2 prices the PAIRWISE channel. Family-level deficits beyond
  it exist: ray-support-4 relations (`xr_support4_structure`), which
  need four rays and a Mobius match; supports `<= 3` are zero (the
  adv_sublinear_rank induction, k-packing killing the triple step).
- The self-referential grading (every sharing event is another band
  pair, at complementary depth) is what blocked the pilot's attempts
  to close the occupancy lemma by induction on sharing; recorded as
  structure, not as a bound.
- Machine record at draft time: 371 cumulative witnessed sharing
  events across five shapes, 0 violations
  (`notes/pilots_20260802/xr_occupancy_v2/hunt_e0.json`; the
  REPORT's "371" is the cumulative total of that file's running
  counter — per-shape increments 61/129/57/113/11). The verifier
  reproduces the phenomenon on fresh fixtures with a fresh engine.
