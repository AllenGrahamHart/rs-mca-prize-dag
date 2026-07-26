# rate_half_list_chamber_affine_rank_bridge

- **status:** PROVED
- **closure:** proof
- **dependencies:** `upstream_gfv4_affine_span_list_compiler`,
  `rate_half_list_budget_three_intersection_reduction`,
  `rate_half_list_budget_three_affine_rank_rigidity`,
  `rate_half_list_budget_three_common_mismatch_zero`
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

### Scope reconciliation after the affine-rank theorem

The preceding `s in {2,3}` paragraph is superseded in this worktree by the
proved theorem `rate_half_list_budget_three_affine_rank_rigidity`. At the
printed scope it gives, without using chamber geometry,

```text
s=3
```

for every four-codeword witness. Its proof excludes rank two by analyzing the
equality case of the affine-line compiler: rank two would force `2d+2`
active coordinates to inject into the six roots of pairwise affine-linear
quotient differences. Thus every later `s=2` calculation in this file is a
valid counterfactual consequence but is not a live branch and must not guide
further work.

The proved `rate_half_list_budget_three_common_mismatch_zero` theorem also
gives `b=0` in every chamber: the selected agreement sets cover `D`, so one
selected agreement at a common direction zero forces the common value to
equal `u`. The live bridge residue is therefore only the chamber-to-
`(d_1,d_2,d_3)` transport.
The affine-span compiler is already fixed at cap eight and kills no chamber.
Here `b=0` minimizes every denominator factor `d_j-t+b`, so the mismatch
theorem narrows the route but gives the rank-flat compiler no extra bite.
Lower generalized-weight bounds must be coupled to enough control of `d_3`,
which occurs in both the falling-factorial numerator and the denominator. The
original sentence that lower `d_j` bounds plus an upper `b` bound suffice was
therefore incorrectly oriented.

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

## PROGRESS 2: the split-pencil direction pin (2026-07-26)

CZB combines with a fiber count to nearly pin the `s=2` case. Verified in
`verify_common_zero_budget.py`.

Assume `s = 2`, so `C' = span{f,g}` is a pencil. Put `h = gcd(f,g)`, `deg h = z`,
`f = h f'`, `g = h g'` with `gcd(f',g') = 1`. Each of the six pairwise differences
`c_i - c_j` is a nonzero element of `C'`, hence `h` times a pencil member, and by
the razor bracket every pair agrees in `K-2` or `K-1` places — so **every one of
the six differences is a minimum- or near-minimum-weight codeword**, and its pencil
member has at least `K-2-z` roots in `D`.

Distinct projective members of a base-point-free pencil are coprime, so **their
root sets in `D` are disjoint**. Letting `Ddir` be the number of distinct
directions among the six differences,

```text
Ddir * (K - 2 - z) <= |D| = n,      i.e.   z >= K - 2 - n/Ddir.       (DIR)
```

Against `CZB`'s `z <= (n-2)/3`, at `n = 2^41`, `K = 2^40`:

| `Ddir` | `(DIR)` floor on `z` | window with CZB |
|---:|---:|---:|
| **6** | 733,007,751,849 | **2 values** |
| 5 | 659,706,976,664 | 7.3e10 |
| 4 | 549,755,813,886 | 1.8e11 |
| 3 | 366,503,875,924 | 3.7e11 |

**Corollary (`Ddir = 6`).** `z in {733,007,751,849, 733,007,751,850}`, and in both
cases `CZB` gives `4b <= 3`, hence **`b = 0`** — route 3's conclusion, proved
outright in the generic `s=2` case. Correspondingly `d_s in {1,466,015,503,702,
1,466,015,503,703}`, exactly at the `(2n+2)/3` floor.

**Residual.** `Ddir >= 3` always (no three of the four are collinear), but `Ddir`
can drop below 6 in special position — a complete quadrangle whose opposite sides
are parallel. The remaining work for this route is the case analysis
`Ddir in {3,4,5}`, where the window is wide and no pin follows. Note this is now a
*finite configuration question in the affine plane*, not a coding question.

This also welds the bridge to the M-1 lane: `(DIR)` is a split-pencil fiber count,
the same mechanism as the minimal-index budget `(MI2)` in
`rate_half_ca_hankel_minimal_index_budget`.

## PROGRESS 3: the direction count is classified — `Ddir in {4,5,6}` (2026-07-26)

The residual of PROGRESS 2 is now settled as a finite affine-plane fact.

Normalize `P_0 = 0`; no-three-collinear makes `A = P_1`, `B = P_2` a basis, and
`P_3 = C = alpha A + beta B` with `alpha != 0`, `beta != 0`, `alpha + beta != 1`.
The six difference directions are

```text
d1=[1:0]  d2=[0:1]  d3=[alpha:beta]
d4=[-1:1] d5=[alpha-1:beta]  d6=[alpha:beta-1].
```

Checking all fifteen pairs, the **only** possible coincidences are

```text
beta = 1        <=>  d1 = d6
alpha = 1       <=>  d2 = d5
alpha + beta = 0 <=> d3 = d4
```

(every other pair differs by a nonzero constant, or would force `alpha = 0`,
`beta = 0`, or `alpha + beta = 1`, all excluded). All three simultaneously would
give `2 = 0`, so **in odd characteristic at most two hold**, and

```text
Ddir = 6 - #(coincidences)  in  {4, 5, 6},   and Ddir = 3 is IMPOSSIBLE.
```

`Ddir = 4` occurs for **exactly three** configurations, independent of the field:

```text
(alpha,beta) in { (1,1), (1,-1), (-1,1) },
```

i.e. `C = A+B` (the parallelogram `c_3 = c_1 + c_2 - c_0`), `C = A-B`, `C = -A+B`.

Verified by brute force over `F_p`, `p in {5,7,11,13,17,19,23}`: the distribution
is `Ddir = 4` in exactly 3 configurations at every `p`, the rest split between 5
and 6, and `Ddir < 4` never occurs.

**Status of the `s=2` route.** `Ddir = 6` is closed (PROGRESS 2: `z` pinned to two
values, `b = 0`). The residual is `Ddir in {4,5}` — one or two of the three
coincidence relations holding — with `Ddir = 4` reduced to three explicit
configurations. The fiber bound `(DIR)` weakens there
(`Ddir=5` gives a `7.3e10` window, `Ddir=4` a `1.8e11` one), so these need a
different argument, not a sharper constant.

*Recorded correction:* the tempting strengthening `Ddir*(K-2-z) <= n - z`, using
`R_dir subset D \ G`, is **false** — a root of a pencil member may lie in the base
locus `G`. The correct statement is that each point of `G` belongs to exactly one
direction (since `gcd(f',g') = 1`), giving `sum_dir |R_dir| <= n` and no
improvement. With the false version `Ddir = 6` would have been excluded outright;
it is not.

## PROGRESS 4: `s = 2` is fully determined — `Ddir = 6`, `b = 0`, `z` pinned (2026-07-26)

`Ddir in {4,5}` is now excluded, closing the residual of PROGRESS 3.

Every coincidence found in PROGRESS 3 is a **disjoint-pair** proportionality:
`d1=d6` pairs `{0,1},{2,3}`; `d2=d5` pairs `{0,2},{1,3}`; `d3=d4` pairs
`{0,3},{1,2}`. (A coincidence between pairs sharing an index would put three of
the four points on a line, which is excluded.) So a coincidence reads

```text
c_b - c_a = lambda (c_d - c_c),    lambda != 0,   {a,b} disjoint from {c,d}.
```

**Lemma.** Under such a relation, `a_x = 3` forces `a_x = 4`.
*Proof.* If the non-matching index lies in `{c,d}`, then `c_b - c_a = 0`, so
`lambda(c_d - c_c) = 0`, so `c_d = c_c = u(x)`. If it lies in `{a,b}`, then
`c_d - c_c = 0`, so `c_b = c_a = u(x)`. ∎

But `a_x = 4` means all four codewords agree at `x`, i.e. `x in G`. Hence **off `G`,
`a_x <= 2`** (not merely `<= 3`). Re-running the budget count of `(CZB)` with this
sharper pointwise bound:

```text
4(m - g) <= sum_{off G} a_x <= 2(n - z),     g = z - b
  =>  4b <= 2z - n + 4,   so  b >= 0  forces  z >= (n-4)/2.
```

Against `CZB`'s `z <= (n-2)/3` this is a contradiction whenever
`3n - 12 > 2n - 4`, i.e. **for every `n > 8`**. At the official row the two bounds
miss by `366,503,875,924`. Therefore no coincidence can occur and `Ddir = 6`.

**Consequently the `s = 2` case is completely determined:**

```text
Ddir = 6,     b = 0,
z    in {733,007,751,849, 733,007,751,850},
d_s  in {1,466,015,503,703, 1,466,015,503,702}   (exactly the (2n+2)/3 floor).
```

So route 3 of the attack surface is **fully paid**: `b = 0` holds in the `s = 2`
case unconditionally, not just generically. What remains for the bridge is `s = 3`
(where the compilers give cap 8 and cannot bite) and the chamber-to-`s` map itself.

### Lead for the `s=2` exclusion (2026-07-26)

With `s=2` pinned (PROGRESS 4), the pencil is **almost exhausting the domain**.
Each of the six directions has `|R_dir| in [K-2-z, K-1-z]` and the `R_dir` are
pairwise disjoint in `D`, so at `z = 733,007,751,850`:

```text
6*(K-2-z) = 2,199,023,255,544      6*(K-1-z) = 2,199,023,255,550
n         = 2,199,023,255,552      slack: 8 (at min), 2 (at max)
```

So the six fibers of the degree-`(K-1-z)` pencil map cover all but at most **8**
points of `D`. That is an extreme rigidity — a covering-type statement on a
multiplicative coset of order `2^41` by six fibers of one rational map — and it is
the natural place to look for the contradiction that would exclude `s=2` entirely
and force `s=3`. Note `d_1 = K+1` exactly (the MDS floor), since the six
differences have weight `K+1` or `K+2`.

### `s=2` reduced to a six-fiber covering of the coset (2026-07-26)

The near-exhaustion above has an exact reformulation. Let `S = union of R_dir`
(disjoint, `|S| >= 6(d-1)` with `d = K-1-z`), and `E = prod_{x in D \ S}(X-x)`,
`deg E = n - |S| <= 8`. Since `prod_i Q_i` vanishes on `S` and has degree `<= 6d`,

```text
E * prod_{i=1}^{6} Q_i = c' * W * (X^n - c),        deg E <= 8,  deg W <= 6,
```

where the `Q_i` are six members of the **two-dimensional** pencil. Equivalently:

> a degree-`d` rational map `psi = A/B` sends the order-`2^41` multiplicative coset
> `D` into a set of just **six** points, with at most 8 exceptions — i.e.
> `D = psi^{-1}(Lambda)` up to 8 points, `|Lambda| = 6`.

This is the balanced case `n = 6d` (indeed `6d` and `n` agree to within 6, which is
exactly what pinned `z`).

**Where to attack.** The most symmetric realization would take the six `lambda_i`
in geometric progression, giving `prod_i (A - lambda_i B) = A^6 - mu B^6` and
requiring the coset to be a `6`-th power fibration — but `n = 2^41` has **no factor
of 3**, so `6 | n` fails and that realization is unavailable. The open question is
whether an asymmetric `Lambda` can do it: does a degree-`d` map exist carrying a
multiplicative coset of 2-power order onto six points? A negative answer excludes
`s = 2` outright and forces `s = 3`, completing half the bridge.

### The composition obstruction (2026-07-26) — where the `s=2` exclusion should come from

Write `F(u,v) = prod_i (u - lambda_i v)` (a binary sextic with distinct roots) and
`rho(t) = F(t,1)`, a degree-6 polynomial map. Then

```text
F(A(X),B(X)) = B(X)^6 * rho(psi(X)),        psi = A/B,
```

so the six-fiber identity says the composite `theta = rho o psi`, of degree `~6d`,
has `theta^{-1}(0) = D` up to at most 8 points, every point simple. **`theta`
factors through a degree-6 map.**

The natural map with that fiber is `theta_0(X) = X^n - c`, whose fiber over `0` is
exactly `D`, all simple. If `theta` were literally `theta_0`, the obstruction is
immediate: `rho` is totally ramified over `infinity` with index 6, so every
multiplicity in `theta^{-1}(infinity)` is divisible by 6, while
`theta_0^{-1}(infinity) = {infinity}` with multiplicity `n = 2^41` — and
**`6 does not divide 2^41`**, since `3 ∤ 2^41`. Contradiction.

**The gap.** `theta` is not literally `theta_0`: the identity only gives
`theta = c' W (X^n - c) / E` with `deg W <= 6`, `deg E <= 8`. Degrees are
consistent (`6d = n-2` at `z = 733,007,751,850`, `6d = n+4` at
`z = 733,007,751,849`, both reachable with the allowed `W`, `E`), so the
divisibility contradiction does not apply verbatim. Closing `s=2` reduces to:

> show that no degree-`<=8` / degree-`<=6` correction can repair the
> `6 ∤ 2^41` mismatch — i.e. that `theta`'s fibre multiplicities over the
> `rho`-critical values remain incompatible with those of `W (X^n-c) / E`.

That is a bounded, purely local question at finitely many points, and it is the
recommended next step for this node.

#### Caveat for the composition attack (recorded 2026-07-26 — do not skip this)

The tempting execution is: `rho` is totally ramified of index 6 over `infinity`, so
every multiplicity in `theta^{-1}(infinity)` is divisible by 6; read the pole order
at `infinity` off `theta = c' W (X^n - c)/E` and conclude `6 | (n + deg W - deg E)`,
which `6 ∤ 2^41` then obstructs.

**That is wrong as stated.** `theta` is not `c' W (X^n-c)/E`. Since
`F(u,v) = prod(u - lambda_i v)` is homogeneous of degree 6,

```text
theta = rho(A/B) = F(A,B)/B^6 = c' W (X^n - c) / (E * B^6),
```

so the pole divisor carries an extra `B^6`, and `deg theta = 6d` forces a relation
between `deg A`, `deg B`, `deg W` and `deg E` rather than the naive one. The
divisibility bookkeeping must be redone with the `B^6` present and split by whether
`deg A > deg B`, `deg A = deg B`, or `deg A < deg B` (equivalently, whether
`infinity` is a pole of `psi`, a `lambda_i`-point, or neither).

The obstruction may well survive — `6 ∤ 2^41` is robust and `deg W <= 6`,
`deg E <= 8` are tight — but it must be derived, not asserted. Anyone continuing
should start from `theta = prod_i Q_i / B^6` and track the fibre over `infinity`
honestly.

#### RESOLVED 2026-07-26: the composition/divisibility route is DEAD

The caveat above is fatal, not repairable. Carrying the `B^6` through:
`theta = prod_i Q_i / B^6` with `gcd(Q_i, B) = 1` (a common root of `Q_i` and `B`
would be a common root of `A` and `B`). So every **finite** pole of `theta` is a
zero of `B` with multiplicity `6 * mult_B(x)` — divisible by 6 automatically. And
at infinity, with `k = 6d - deg(prod Q_i) >= 0`:

```text
deg A > deg B :  all deg Q_i = d, k = 0, pole order 6(d - deg B)   -- 6 | it, free
deg A < deg B :  all deg Q_i = deg B, pole order 0, infinity regular -- free
deg A = deg B :  at most ONE i cancels (the lambda_i are distinct), so
                 deg prod = 6d - k and infinity is a ZERO of order k, not a pole
```

So the divisibility condition is satisfied **automatically in every case** and
imposes nothing. All that survives is the degree identity `6d = n + deg W - deg E + k`,
which needs `deg W - deg E + k = 4 (mod 6)` since `n = 2 (mod 6)` — and there are
**74** admissible triples with `deg W <= 6`, `deg E <= 8`, `k >= 0`.

**Fence: do not attack `s=2` via `rho`'s total ramification over infinity, or via
any `6 ∤ 2^41` divisibility read off the pole divisor.** The `6`-divisibility is
structural (it comes from `B^6`) and carries no arithmetic information about `n`.

The six-fiber covering reduction (PROGRESS 4 + the reduction above) still stands
and is still the right frame; what is dead is this particular way of exploiting it.
A live attack must use the *multiplicative* structure of the coset `D` — that
`psi^{-1}(Lambda)` is a coset of `mu_{2^41}` — not the ramification bookkeeping.

#### The symmetric six-fiber realization is IMPOSSIBLE (2026-07-26)

The natural construction for the six-fiber covering is the symmetric one: take
`A = X^a`, `B = 1`, and the `lambda_i` the six 6th roots of some `mu`, so that

```text
prod_i (A - lambda_i B) = X^{6a} - mu.
```

Best fit is `a = 366,503,875,925`, giving `6a = n - 2`. The identity then demands
`E (X^{n-2} - mu) = c' W (X^n - c)` with `deg E <= 8`, `deg W <= 6`, hence
`X^{n-2} - mu` must divide `W (X^n - c)` up to `E`, i.e. the two must share at
least `(n-2) - 14 = 2,199,023,255,536` roots.

But the roots of `X^{n-2} = mu` form a coset of `mu_{n-2}` and the roots of
`X^n = c` a coset of `mu_n`, and

```text
gcd(n-2, n) = gcd(2^41 - 2, 2^41) = 2,
```

so **the two sets meet in at most 2 points**. Needing 2.2e12 shared roots and
having at most 2 is a contradiction by twelve orders of magnitude. The symmetric
realization is dead, and dead with enormous margin — no adjustment of `mu`, `a`,
`E` or `W` can rescue it.

**Scope (important).** This kills the symmetric *ansatz*, not the configuration.
The obstruction is that there `prod Q_i` has its roots on a `mu_{6a}`-coset, a
*different* coset from `D`; in the general problem `prod Q_i`'s roots lie in `D` by
construction, so no gcd obstruction arises. What this does establish is that any
realization must be genuinely asymmetric — the `lambda_i` cannot be in geometric
progression — which removes the only construction anyone would try first.

#### The equivariant reduction: `s=2` becomes a split-pencil problem (2026-07-26)

The coset structure does bite, and it collapses the six-fiber problem to a clean
statement. For `zeta in mu_n` put `psi_zeta(x) = psi(zeta x)`. Since
`psi^{-1}(Lambda) = D` up to `<=8` points and `zeta D = D`, also
`psi_zeta^{-1}(Lambda) = D` up to `<=16`. So `P = prod_i Q_i` and its twist
`P(zeta X)` have the same root set up to bounded error, hence are proportional up
to factors of degree `<=32`.

**In the exactly-equivariant case** `P(zeta X) = kappa_zeta P(X)` for all
`zeta in mu_n`. Writing `P = sum_j c_j X^j`, this forces `c_j(zeta^j - kappa_zeta) = 0`,
so any two exponents in the support are congruent mod `n`. With `deg P = 6d <= n+4`
the support lies in `{j_0, j_0+n}`, giving

```text
prod_{i=1}^{6} Q_i  =  beta * X^{j_0} * (X^n - c),        0 <= j_0 <= 4.
```

(`0 not in D`, so the `X^{j_0}` is absorbed by the allowed `deg W <= 6` factor.)

**Consequence.** Since `Q_i = A - lambda_i B`, fixing any two of them determines
`A` and `B`, and the remaining four are the prescribed combinations

```text
Q_i = [ (lambda_2 - lambda_i) Q_1 - (lambda_1 - lambda_i) Q_2 ] / (lambda_2 - lambda_1).
```

So `s = 2` requires **a two-dimensional pencil with six pairwise-coprime members,
each of degree about `d = n/6`, all splitting completely over `D`, whose root sets
partition `D`**. Equivalently: a degree-`d` map `P^1 -> P^1` with six totally
`D`-split fibres exhausting the order-`2^41` coset.

**This is the same object as the M-1 seam.** It is a split-pencil / moving-kernel
count of exactly the type bounded by `(MI2)` in
`rate_half_ca_hankel_minimal_index_budget`, and by the `T <= 4e+1` slope cap of the
strict `A=3` ledger. The bridge and the rate-half seam are therefore not two
problems but one mechanism seen from two sides, which is the first genuine weld
between the list lane and the MCA lane at this node.

**Next step (recommended):** import the minimal-index budget machinery and ask
whether it caps the number of totally-split members of a degree-`d` pencil below
six at `d ~ n/6`. If it does, `s = 2` dies and `s = 3` follows.

#### Reconciliation of the latest recommendation

That recommendation is retired for two independent reasons. First, `s=2` is
already impossible by `rate_half_list_budget_three_affine_rank_rigidity`.
Second, the Hankel minimal-index theorem does not automatically apply to the
residual polynomial pencil `A-lambda B`: its hypotheses require the pencil to
be the primitive apolar kernel of a syndrome Hankel pencil. The arbitrary-
pencil moving-root theorem gives only the sharp incidence bound six in this
near-partition regime, not a strict cap below six. Any reuse of `(MI2)` here
would need a new transport theorem and would still be unnecessary for the
affine-rank question.

The route-deciding question is now exact: for each of the nine split-unit and
four balanced-scroll chambers, express the supports of the one-, two-, and
three-dimensional subspaces of the codeword direction space in the chamber
incidence variables and substitute `b=0`. A chamber closes through the
harvested rank-flat compiler only if those exact bounds make its printed cap
at most three. Otherwise this bridge is a route fence and should be retired
as a closure mechanism.

## PROVED resolution: the rank-flat route is a fence

The latter alternative always occurs. Put `n=4d`, `K=2d`, `m=3d-1`, and
`t=d+1`, with `d>=3`.

Every one of the six incidence types has at least one pair with selected
intersection `2d-1`. That pair difference is a nonzero degree-`<2d`
polynomial, so it has exactly `2d-1` zeros and support `2d+1`. The MDS floor
gives the reverse inequality; hence

```text
d_1=2d+1.                                             (RF1)
```

Affine-rank rigidity makes every three of the four codewords an affine
basis of a two-dimensional direction subcode. In every incidence type, some
selected triple intersection has size at least `d-1`; it is a common-zero
set of that two-dimensional subcode. Therefore

```text
d_2<=4d-(d-1)=3d+1.                                  (RF2)
```

The generalized Singleton bound gives `x:=d_3>=2d+3`, while `x<=4d`, and
the common-mismatch theorem gives `b=0`. The unfloored rank-flat expression
is therefore bounded below by

```text
x(x-1)(x-2) / [d * 2d * (x-d-1)].                   (RF3)
```

For `x>=2d+3`,

```text
F_d(x)=x(x-1)(x-2)-8d^2(x-d-1)>0.                   (RF4)
```

Indeed `F_d(2d+3)=8d^2+22d+6>0`; its derivative there is
`4d^2+24d+11>0`, and its second derivative is `6x-6>0`. Thus `(RF3)` is
strictly greater than four, so its integer floor is at least four on every
chamber. The harvested rank-flat compiler can never prove the required cap
three on this atlas, even after an exact generalized-weight transport.

This closes the bridge as a proved negative result. It closes no locator
chamber and does not move the rate-half adjacent crossing. Further work must
attack the thirteen official-subgroup chambers directly or use a stronger
list theorem.
