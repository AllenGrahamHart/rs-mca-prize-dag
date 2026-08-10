# Rate-half FPC5 `M=4,t=2` payment

- **status:** TARGET
- **consumer:** `l1_fpc5_m4_t2_payment`

Fix one admissible maximal rate-half source with `M=4`. Count all non-planted
FPC5 contributors touching exactly two full petals. For a cell

```text
d=ell+s,       0<=s<ell,
```

the proved petal-equation envelope has dimension `2s+2`; the exact cell also
imposes its background roots and exact nonagreements. The formal locator
codimension is at least two. At equality, official arithmetic forces

```text
5ell=k+4,       b=r=s=ell-3,       d=2ell-3,
```

and the full-background guard cuts the pair and locator dimensions to
`ell-1`.

The uniform guarded-codimension theorem now covers every fixed exact
background set `R`, not only that endpoint. If `r=|R|`, the threshold gives
`r>=s`, and the guarded locator codimension is at least `ell-1`; it is exactly
`ell-1` when `r=s` and at least `ell` when `r>=s+1`. Aggregated without
choosing `R`, the remaining locus is one joint split-pair problem:

```text
F split on C,       W_F has at least s roots on B.      (RH0)
```

The exact set `R=Z_B(W_F)` is unique, but an independent sum over all
`binom(b,r)` possible sets is not a polynomial payment.

Primitive cofactor determinants give the first direct aggregate bound. For
two distinct contributors at fixed `s` and touched pair,

```text
|D intersect D'|+|R intersect R'|<=2s,               (RH0a)
```

and hence

```text
L_(s,pair)
 <= binom(k-1+b,2s+1)/binom(ell+2s,2s+1).            (RH0b)
```

This avoids background-set enumeration, but its exponent grows with `s` and
is not the required uniform polynomial payment.

The sharp distance-only no-go fence proves this limitation is structural:
even with the exact fixed background block and overlap cap, abstract defect
families of size

```text
2^((0.099865...+o(1))(ell-2))
```

exist. They are not asserted to lie in the guarded flat. Any closure must use
the algebraic cofactor equations, smooth-domain incidence, or received-word
ownership beyond support weights and pairwise distance.

The proved sharp projective-flat descriptor now identifies this endpoint
exactly. For each fixed touched pair, contributors inject into

```text
P(V_F) intersect D_(2ell-3)(C),
|C|=5ell-5,       dim P(V_F)=ell-2,
affine codimension=ell-1.                              (RH1)
```

The numerator is reconstructed uniquely, and primitive, untouched-petal,
and first-owner conditions remain explicit filters. A companion theorem
proves the entire locator flat has maximal common gcd `1`, so no flat-wide
common-divisor branch remains. This is distinct from the candidate-wise
primitive filter `gcd(F,W_F)=1`. Since `n=2^41` and `2ell-3` is odd, the
proper pure multiplicative quotient-pullback stratum is also empty. Partial
quotient tails and reciprocal/dihedral classes remain. Because the projective
dimension grows with `ell`, the upstream fixed-dimensional split-flat bound
does not close (RH1).

Two further exact descriptors expose structure hidden by (RH1). First, each
sharp contributor gives a degree-`2ell-3` rational map with a complete
core `1`-fiber, the touched petals in its zero and pole fibers, the full
background in a fourth marked fiber, and two distinct forbidden fibers on
the untouched petals. These blocks partition the whole official domain.
Second, shortening the fixed background and touched pair injects the same
contributors into

```text
RS[C,2ell-1],       |C|=5ell-5,
agreement=3ell-2,   radius=2ell-3.                    (RH2)
```

The latter is outside the ordinary Johnson range and is not itself a
payment. Together the descriptors offer two non-equivalent attack routes:
marked rational-map incidence and a structured shortened-list theorem.

Prove one disjoint aggregate payment of the remaining root-rich split-pair
locus over the six touched pairs and all defect/background cells in this
fixed source. Internal tangent, quotient, background-root, and
contributor-dependent recharts must have explicit first owners. No sum over
maximal source layouts is needed:
`l1_general_first_layout_domination` makes the fixed-layout payment global
after adding at most four anchors.

## Round-23 diagnosis addendum (2026-08-07, coordinator-applied on replay: fpc5_diag)

**CLASSIFICATION: MYSTERY-HARD** — the master split-locator flatness
wall (statement (MF): count monic degree-d locators split on C
inside a linear flat of projective dimension e = 2d+1-t*ell, codim
exactly sigma), shared with the m4_t3 and large-source reds and
with upstream prob:capfr1-master-flatness. The shape-pun test
PASSES: one statement, three specializations. NOT a first-moment
problem: the CODIMENSION-RESERVE IDENTITY codim(F-flat) = sigma
holds identically (verified exactly, ell = 4..39, both printed
families, reproducing this node's (RH1)); at the official cell the
first moment is <= 2^{-7.948e12}. Everything open is max-to-mean.

**THE FIRST POSITIVE LEAD (the round-23 adversarial cap).** The
guarded flat V_F does not depend on C — so the strongest adversary
fixes (background, petals, labels), enumerates the whole monic
chart, and CHOOSES the core to pack split members (a strictly
stronger attack than anything in attack.md, executed with
exhaustive sound branch-and-bound): max packed = **4**, INVARIANT
under q (97 -> 193 with 8x more split members) and flat in ell
(4 at ell = 4 and ell = 5-free-domain; 0 on the official mu_n
domain at ell = 5). Adversarial core placement buys ~1200x over
the mean and stops dead at 4. Registered escapes did not fire
(4 < 4(ell-2)).

**SCOPE PIN vs the banked nonemptiness census:** the
sharp_cell_nonemptiness figures (71 contributors / 41 of 50
layouts) are LABEL-FREE (lambda solved per cell, worth one q
dimension); the fixed-source object this payment must bound is a
factor ~q smaller (measured 85x at q = 97, predicted q). The
census is correct for its stated nonemptiness job; do not read it
as contributor density.

**Derived sharpening (checked on all witnesses):** at the sharp
cell r = b is forced, so joint_support_distance's
|D cap D'| + |R cap R'| <= 2s tightens to |D cap D'| <= 2s - b =
ell - 3; feeding it into the packing improves (RH0b) from
2^{2.755 ell} to 2^{1.61 ell} — still fenced off as a closure by
the distance-only no-go, recorded as an instrument sharpening.

**Cheapest decisive probe:** at ell = 4 the chart is a
2-dimensional affine plane — "can 5 split members share a 15-point
core?" is finite and decidable per q up to affine equivalence:
exhibit a 5-packing or prove <= 4 at ell = 4. Hours, not Modal.
Source: notes/pilots_20260807/fpc5_diag/ (A1 gate PASS replayed;
cap-4 replayed 5/5 trials; official constants cross-checked
against the sharp_dyadic verifier's pinned values).

## Round-23b adjudication note (2026-08-07, coordinator-applied on replay: mf_wall_adversary)

The round-23 one-wall evidence is REPRICED under adversarial attack:
the statement-level (MF) shape-pun test FAILED its power control
(the PROVED rate-quarter sibling satisfies every (MF) clause with
better margins; the separating clause — over-determination
t*ell > N — is not part of (MF)), and the two quantitative handles
are WITHDRAWN as classification evidence (the cap-4 is
structure-specific — a random flat with identical parameters
reaches 5; the trivial-owner concentration is 92x its parametric
reference). Both remain valid node-level findings, and the cap-4
data is STRENGTHENED (exact, not sampled, at ell = 4, 5, 6 over
329 configs and three primes; the sharpened overlap cap ell-3
achieved tightly at every ell; the cap is soft — budget elasticity
+1..+4 core points — and stiffens with ell; the mechanism at
ell >= 5 is UNIDENTIFIED). The REPAIRED test (round-19 three
gates, METHOD = the-missing-theorem-is-the-same; passed all three
power controls incl. the PROVED-sibling hard control): the m4_t2
and m4_t3 reds SHARE ONE WALL at METHOD level — a
dimension-uniform max-to-mean bound for split locators in a
growing-dimensional flat (the anticode bound's exponent grows with
flat dimension). The same METHOD wall matches the PROVED
l1_rootfree_rational_q_projective_packing at its own open
d = Theta(n) regime and f_global_packing_step (identical formula,
identically named failure). The large-source red is UNDECIDED:
only 142/408 residual rows are even posable as flats; the other
266 await the t-petal overlap-cap lemma. Upstream
prob:capfr1-master-flatness has ZERO discriminating power as a
wall test (PROVED nodes are instances of it; (MF) is an instance,
not the same statement; a |B|^{-s} vs q^{-sigma} normalization
mismatch is unresolved). Source:
notes/pilots_20260807/mf_wall_adversary/ (coordinator-replayed).

**MYSTERY 7 MEMBERSHIP RATIFIED (2026-08-07, user):** this node is a
member of mystery 7, "the dimension-uniform split-locator
max-to-mean wall" (board of record: roadmap section 12, r5 update).
