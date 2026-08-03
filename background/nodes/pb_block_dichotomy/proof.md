# Proof

Notation as in `statement.md`. **Provenance of the argument.** The
record asserts the dichotomy as "proved + verified"
(`pb_h4_hunt/REPORT.md:15`) and states it in code (`expE.py:4-14`) with
the proof deferred "to the report", where no derivation appears. Claims
1-3 below are therefore written out from scratch; the coset power-sum
vanishing behind Claim 3 is the part the coordinator independently
hand-verified (`pb_h4_hunt/FABLE_AUDIT.md:19-23`). Claim 4 is
reconstructed in corrected coordinates. Nothing is transplanted
verbatim, because there was nothing to transplant.

## Claim 1 (spread threshold)

The blocks are pairwise disjoint and disjoint from `G`, so for
`a`-subsets `J, J'` of the pool

```text
S_J ^ S_{J'} = G u (union_{j in J ^ J'} B_j),
|S_J ^ S_{J'}| = |G| + m |J ^ J'|.
```

For `J != J'` we have `|J ^ J'| <= a-1`, with equality attained whenever
two `a`-subsets share `a-1` blocks — possible exactly when
`b >= a+1`. So the maximum pairwise core is

```text
max_{J != J'} |S_J ^ S_{J'}| = |G| + (a-1) m = (|G| + a m) - m = A - m.
```

Spreadness is `A - m <= K - 1`; with `A = K + h` this reads
`K + h - m <= K - 1`, i.e. `m >= h + 1`. Conversely if `m >= h+1` then
every pairwise core is `<= A - m <= K - 1`. QED (1)

## Claim 2 (SF-SELFCOLLISION, derived)

Immediately from Claim 1: if `m <= h` then the maximum pairwise core is
`A - m = K + h - m >= K`. Moreover EVERY member is involved: given `J`,
pick `J'` sharing `a-1` blocks with it (possible since `b >= a+1`), and
the pair `(S_J, S_{J'})` has core `A - m >= K`. So every planted member
has a core-`>= K` partner and lies in `Gamma_hi`, never in `Gamma_lo`.
QED (2)

This is exactly the identity quoted in the P-B TARGET's addendum,
`|S_J ^ S_{J'}| = g + m|J ^ J'|` with `g = |G|`, and its consequence
"`m <= h` forces adjacent cores `A - m >= K`"
(`critical/nodes/xr_lowcore_spread_heart/notes/OFFICIAL_SCALE_REFRAME_20260802.md:47-50`).
Note the derivation needs **no** hypothesis on the slope structure — it
is pure counting.

## Claim 3 (coset blocks; the dichotomy)

**The coset polynomial.** Let `B = g mu_m` with `mu_m <= mu_n <= F_q^*`,
`m | n`. Then `prod_{x in B}(X - x) = prod_{i=0}^{m-1}(X - g zeta^i)`
where `zeta` generates `mu_m`. Substituting `X = gT`, this is
`g^m prod_i (T - zeta^i) = g^m (T^m - 1) = X^m - g^m`. Hence

```text
R_B(Y) = Y^{|B|} * (that, evaluated at 1/Y)  =  1 - g^m Y^m ,
```

exactly (no truncation needed yet); equivalently `e_j(B) = 0` for
`1 <= j <= m-1` and `e_m(B) = (-1)^{m+1} g^m`.

*(Power-sum form, for comparison with the source's phrasing:
`p_t(B) = sum_i (g zeta^i)^t = g^t sum_i zeta^{it} = m g^t` if `m | t`
and `0` otherwise. So for `1 <= t <= h < 2m` the only non-zero entry is
`t = m`, with value `m g^m` — the source's `beta_j = m lam_j e_m`,
`lam_j = g_j^m`. Both coordinate systems give the same direction `e_m`
for cosets.)*

**Branch `m > h`.** Then `Y^m = 0` in `R = F_q[Y]/(Y^{h+1})`, so
`R_{B_j} = 1` for every block and

```text
R_{S_J} = R_G * prod_{j in J} R_{B_j} = R_G     in R,
```

independently of `J`. So `E(S_J)` is the same point `P` for every `J`:
the whole family sits at ONE point of `AG(h,q)`.

Now read `(STAR)` at that point. If `beta != 0` then `z -> alpha + z beta`
is injective, so `P` lies on `L` for **exactly one** `z`, and every
member of the family is a witness at that ONE slope. If `beta = 0` the
pencil carries no slope parameter at all. In both cases the family
exhibits a single slope: **no live slope direction** — a strip, not a
multi-slope spread family. (Claim 1 does say the family is spread here,
`m >= h+1`; it is spread and slope-dead.) QED (branch 1)

**Branch `m <= h < 2m`.** Then `Y^{2m} = 0` in `R` but `Y^m != 0`, so
all products of two or more block factors vanish:

```text
R_{S_J} = R_G * prod_{j in J} (1 - g_j^m Y^m)
        = R_G * (1 - (sum_{j in J} g_j^m) Y^m)
        = R_G - (sum_{j in J} g_j^m) Y^m       in R,
```

the last step because `R_G` has constant term `1` and `R_G Y^m == Y^m`
modulo `Y^{h+1}` (any higher term of `R_G` multiplied by `Y^m` has degree
`> h`... precisely: `R_G Y^m = (1 + c_1 Y + ...) Y^m`, and terms
`c_i Y^{m+i}` with `m+i <= h` survive — so the correct statement is
`R_{S_J} = R_G - sigma_J * (R_G Y^m mod Y^{h+1})` with
`sigma_J := sum_{j in J} g_j^m`). Either way the dependence on `J` is
**affine in the single scalar `sigma_J`**: the moment vectors
`E(S_J)` lie on the line through `E(G u ...)` with the fixed direction
vector `R_G Y^m mod Y^{h+1}`. Distinct `sigma_J` give distinct points, so
as soon as two `a`-subsets have different `sigma_J` the family carries at
least two slopes: a live direction exists. But `m <= h` means
`m < h+1`, so by Claim 1 the family is **NOT spread** (max core
`A - m >= K`). QED (branch 2)

**The dichotomy.** The two branches exhaust the coset geometries
(`m <= h` or `m > h`), and in each exactly one of {spread, live slope
direction} holds. Hence for every coset-block geometry **spreadness and
a live slope direction are incompatible**. QED (3)

## Claim 4 (collinearity is necessary — reconstructed)

Work in `R = F_q[Y]/(Y^{h+1})`. Two facts:

- **(M)** for disjoint `S, T`, `R_{S u T} = R_S R_T` in `R` (the defining
  product over points splits);
- **(U)** every `R_S` has constant term `1`, so it is a UNIT of `R`, and
  multiplication by a fixed unit `C` is an `F_q`-LINEAR bijection
  `R -> R`. It therefore maps affine lines to affine lines, in both
  directions.

The witness condition `(STAR)` says `E(S) in L` for an affine line
`L <= AG(h,q)`; in the `R`-picture this is `R_S in L'` for the
corresponding affine line `L'` of the hyperplane `{constant term = 1}`
(the coordinate change `E <-> R` is the fixed sign flip
`(-1)^j` per coordinate, itself linear).

**Case `a = 1`.** `S_j = G u B_j`, so `R_{S_j} = R_G R_{B_j}` by (M).
All `R_{S_j}` lie on `L'`, so all `R_{B_j}` lie on `R_G^{-1} L'`, which
by (U) is an affine line. Done, for all `b` at once.

**Case `a >= 2`, `b >= a+2`.** Fix an `(a-1)`-subset `J_0` of the pool and
let the last block vary over `P_0 := pool \ J_0`, of size
`b - a + 1 >= 3`. With `C_{J_0} := R_G prod_{i in J_0} R_{B_i}` (a unit
by (U)),

```text
R_{S_{J_0 u {j}}} = C_{J_0} R_{B_j}        for every j in P_0.
```

All the left sides lie on `L'`, so `{R_{B_j} : j in P_0}` lies on the
affine line `Lam_{J_0} := C_{J_0}^{-1} L'`.

Now let `J_0'` be another `(a-1)`-subset differing from `J_0` in exactly
one element. Then `P_0 ^ P_0' = pool \ (J_0 u J_0')` has size
`b - a >= 2`, so `Lam_{J_0}` and `Lam_{J_0'}` share at least two distinct
points — two distinct points determine a unique affine line, so
`Lam_{J_0} = Lam_{J_0'}`. Any two `(a-1)`-subsets are joined by a chain
of single-element swaps, so ALL the lines `Lam_{J_0}` coincide, in one
line `Lam`; and every block `B_j` lies in `P_0` for some `J_0` (choose
`J_0` avoiding `j`, possible since `b >= a+1`). Hence
`{R_{B_1}, ..., R_{B_b}} <= Lam`, i.e. the block moment vectors are
collinear. QED (4)

*(Two distinct points share at most one line only if they are distinct —
`b - a >= 2` gives two DISTINCT indices, and their `R_{B_j}` are distinct
whenever the blocks are distinct sets with distinct moment data; if two
blocks have equal moment vectors the conclusion is weaker but still
true, since a repeated point never obstructs collinearity. The verifier
checks the conclusion directly, not this side remark.)*

## Honest scope

- **Claim 4 is a NECESSARY condition, not a characterisation.** The
  dichotomy (Claim 3) does not use it: Claim 3 computes `E(B_j)` for
  cosets outright. Claim 4's role is to say what the residual geometry
  must look like — "non-coset blocks of size `m >= h+1` with collinear
  moment vectors" — and that residue is OPEN (see `statement.md`).
- **The coordinate flag is real.** Newton's identities
  `e_j = (1/j) sum_{i=1..j} (-1)^{i-1} e_{j-i} p_i` are polynomial, not
  affine, in `p`; the verifier exhibits `p`-collinear triples whose
  Newton images are not `e`-collinear. The source's `p`-phrasing of
  Claim 4 is therefore not equivalent to what its code computes. For
  COSET blocks both readings give direction `e_m`, so Claims 2 and 3 —
  and hence (SF-SELFCOLLISION) and the dichotomy — are unaffected. This
  is flagged, not repaired silently.
- **Nothing here bounds `Gamma_lo`.** In particular the identity half
  proved here does NOT give `Gamma_lo = 0` for split-fibre: that needs
  the support-keyed selector (the SELECTOR CATCH), which is a separate,
  PP4.0-coupled hypothesis.
- The first-moment infeasibility of non-coset spread blocks
  (`OFFICIAL.json`) is not a theorem and is not used.
