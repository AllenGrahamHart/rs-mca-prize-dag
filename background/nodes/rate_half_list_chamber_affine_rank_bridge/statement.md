# rate_half_list_chamber_affine_rank_bridge

- **status:** TARGET
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing` (ev)
- **object:** the missing translation between the chamber atlas and the GF list compilers

## Statement

Let `C = RS[F,D,K]` be an official rate-1/2 row, `n = 2^41`, `K = 2^40`, and let
`c_0,...,c_3` be four codewords with `agr(c_i,u) >= a = 3n/4 - 1` for one received
word `u` — i.e. an instance of the `B* = 3` obstruction of
`rate_half_list_adjacent_crossing`. Such a quadruple realizes exactly one of the
**thirteen edge-degree chambers** of that node's atlas (the four cycle chambers,
linear and quadratic `K_4-e`, `K_4`, both path chambers, triangle-plus-singleton,
and the three pendant chambers), determined by the degrees of the edge factors
`b_ij` of its locator pencil under the Plücker gate

```text
b_01 b_23 - b_02 b_13 + b_03 b_12 = 0.
```

Produce the **bridge**: a map from a chamber's edge-degree data to the affine
invariants of the quadruple,

```text
chamber  |-->  (s, d_1, ..., d_s, b),
```

where `s = dim_F span{c_1-c_0, c_2-c_0, c_3-c_0}` is the affine rank, `d_j` are
the generalized Hamming weights of that direction code `C'`, `G` is its
common-zero set, `z = |G| = n - d_s`, `g` is the number of points of `G` at which
the common value agrees with `u`, and `b = z - g`. A **lower** bound on `s` and on
each `d_j`, plus an upper bound on `b`, suffices — those are the only inputs the
compilers consume.

## Why this is owed

Przemek's `thm:affine-span-list` (`experimental/grande_finale.tex:498`) and
`thm:rank-flat-list` (`:583`) bound the list inside an affine span by

```text
|L_A(u,m)| <= floor( C(n-K+s, s) / C(w+s, s) ),        w = m-K,
|L_A(u,m)| <= floor( d_s^{under s} / prod_j (d_j - t + b) ),   t = n-m.
```

Both are stated in `(s, d_j, b)`; the chamber atlas is stated in **locator**-pencil
edge degrees. These are different objects and this repo contains no map between
them, so the compilers cannot be evaluated per chamber. That is exactly why the
Convergence Ledger r1 S3 promotion test — *"ev→req when chamber coordinates are
bound to affine spans"* — cannot fire, and why H1 is ev-wired rather than a
requirement edge. See
`critical/nodes/rate_half_list_adjacent_crossing/notes/affine_span_chamber_replay_20260726.md`.

## What is already pinned (2026-07-26)

Proved, and independent of the compilers
(`critical/nodes/rate_half_list_adjacent_crossing/verify_affine_span_chamber_replay.py`):

```text
s >= 2    whenever   n-K+1 > floor(3(n-a)/2),
```

which at the official row holds for every `a >= 1,466,015,503,701 = 3n/4 -
183,251,937,963`, hence at `a = 3n/4 - 1`. So **`s in {2,3}`** and no three list
members are collinear. Consequently the bridge only has to separate `s = 2` from
`s = 3`, and:

```text
s = 2  ->  affine-span cap = 4  (EXACTLY the quadruple size: zero slack)
s = 3  ->  affine-span cap = 8  (slack 4)
```

so a chamber forced to `s = 2` is on a knife edge and any further constraint
(`b >= 1` at minimum support `d_2 = R+2`) would kill it, while a chamber forced to
`s = 3` cannot be killed by these compilers at all.

## Expected sign of the answer (stated up front, so a negative still counts)

Measured over **all twelve** four-codeword witnesses in the normalized branch of
the banked `RS[F_17,F_17^*,8]` row at `a = 3n/4 - 1` (`f_0 = 0`, `|Z| = 11`,
`|R_i| = 7`):

```text
s = 3          in 12 / 12 witnesses
b = 0          in 12 / 12 witnesses
d_1 = 9 = R+1  in 12 / 12 witnesses   (always at the MDS floor)
d_s = 14 (z=2) in 9;   d_s = 15 (z=1) in 3
pairwise agreements: 71 pairs at exactly K-1 = 7, one pair at 6
```

So the honest expectation is that the bridge returns **`s = 3, b = 0` always**, in
which case both compilers give cap `8` against list size `4` and **kill no
chamber**. Establishing that is a real result: it retires the H1 promotion hope
instead of leaving it indefinitely "promising", and forces the ledger's burn-down
to be re-priced. A negative here is the deliverable, not a failure.

## Attack surface

1. Compute `(s, d_j, b)` directly from the locator data of one chamber — the four
   block locators `A_i` and their edge factors `b_ij` — using the triangle
   identities `A_k b_ij + A_i b_jk = A_j b_ik` and the Plücker relation. The `A_i`
   partition the multiplicative-coset vanishing polynomial, so `d_s` should be
   readable off the exceptional degree (recorded in `{3,4,5,6,8}` for the nine
   Grassmann-line chambers).
2. Prove `s = 3` outright: show a coplanar (`s = 2`) quadruple at `a = 3n/4 - 1`
   forces a locator degeneration incompatible with every chamber. Since `s = 2`
   sits exactly at the affine-span cap, this is an equality-case rigidity problem.
3. Prove `b = 0` outright from the common-zero structure: on `G` all four members
   share one value, so `b >= 1` costs each member an agreement, and the budget at
   `a = 3n/4 - 1` is tight.

## Falsifier

Two four-codeword configurations realizing the **same** chamber with **different**
affine rank `s` (or different `b`). That refutes the bridge as posed — the chamber
would not determine the affine invariants — and forces a refinement of the atlas
before any compiler can be applied per chamber.

A cheap wired instance of this test is `verify.py` in this folder: it re-derives
every witness of the banked F_17 branch and pins the `(s, d_1, d_s, z, g, b)`
census above. Any future witness in that branch with `s != 3` or `b != 0` breaks
it and is exactly the falsifier.

## Non-claims

- Proves nothing about `L_1(3n/4 - 1)` at the official row and constructs no
  official counterexample.
- The F_17 evidence is a **power-of-two multiplicative-domain route fence**, in the
  sense already recorded in `rate_half_list_adjacent_crossing/statement.md`: a
  small analogue is falsification and route-selection evidence only, never a proof
  of the official uniform statement, and there is no transport to `d = 2^39`.
- `thm:affine-span-list` and `thm:rank-flat-list` are Przemek's theorems; this node
  consumes them and proves neither.
- Wired `ev`, not `req`: `rate_half_list_adjacent_crossing` does not depend on this
  bridge for its truth. The bridge only decides whether the H1 harvest can ever be
  promoted to a requirement edge.

## PROGRESS: the common-zero budget bound (CZB) — 2026-07-26

Route 3 of the attack surface ("prove `b=0` outright from the common-zero
structure") is now partly paid, and it kills the case that made `s=2` look
killable. Artifact: `verify_common_zero_budget.py`.

**Theorem.** For four distinct codewords at agreement `>= m` with a common `u`,
with `z = |G|` and `b` as above,

```text
4(m - g) <= (n - z) + 6(K - 1 - z),        g = z - b,
```

and at the razor `m = 3n/4 - 1`, with `K = n/2`, this collapses to

```text
3z + 4b <= n - 2.                                            (CZB)
```

*Proof.* Each `c_i - c_j` is a nonzero codeword, so `agr(c_i,c_j) <= K-1`. Summing
pairwise agreements by position, `G` contributes `C(4,2)=6` per point while off `G`
the four values are not all equal, so `P(x) = sum_k C(n_k(x),2) in {0,1,2,3}` and
`6z + sum_{off G} P(x) <= 6(K-1)`. Off `G`, `a_x = #{i : c_i(x)=u(x)}` satisfies
`a_x <= 1 + P(x)` (`a_x=2` forces an agreeing pair, `a_x=3` forces three, `a_x=4`
is impossible). On `G`, `a_x = 4` at the `g` agreeing points and `0` at the other
`b`. Combining with `sum_i agr(c_i,u) >= 4m` gives the display. ∎

**Consequences at the official row** (`n=2^41`, `K=2^40`):

```text
z   <= 733,007,751,850   = (n-2)/3     (vs the trivial pairwise z <= K-1 = n/2 - 1)
d_s >= 1,466,015,503,702 = (2n+2)/3
b = 0 forced once z >= 733,007,751,849
```

1. **The minimum-support case `d_s = R+2` is IMPOSSIBLE** (`4b <= -1.09e12 < 0`).
   That is precisely the case in which `thm:rank-flat-list` appeared to force
   `b = 0` — see §3 of the H1/S3 replay note, where that apparent rigidity was
   flagged as an artifact of pinning `d_j` at the MDS floor. (CZB) now shows the
   MDS floor is *unreachable* here, so the artifact could never have been
   instantiated: the two findings agree.
2. The admissible band for `d_s` shrinks from `[n/2, n]` to `[2n/3, n]`, i.e. by a
   third, and `(CZB)` and the rank-flat `b`-budget are active in different parts of
   what remains.
3. Sharpness: the step-2 pairwise bound is **tight on 11 of the 12** banked F_17
   witnesses, so (CZB) is essentially optimal for this argument rather than lossy.
4. Note `(2n+2)/3 = 1,466,015,503,702` sits one above the collinearity floor
   `1,466,015,503,701` of the `s>=2` exclusion — both are `~2n/3` phenomena, and
   the coincidence is arithmetic, not a shared mechanism.

**Not a closure.** (CZB) does not by itself decide `s=2` vs `s=3`, and `b=0` is
forced only in the high-`z` regime. The node stays TARGET.
