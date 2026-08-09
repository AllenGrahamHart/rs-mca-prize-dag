# L1 root-free rational-Q projective packing

- **status:** PROVED
- **role:** identify the residual boundary cell with Conjecture-F and pay its
  bounded residual-dimension range
- **consumer:** `l1_mixed_petal_amplification`

## Projective cell

Use the planted-root descent with `r<k`, and put

```text
n'=n-r,       j=m-r,       d=k-r,       j-d=w,
G=Wbar_1 P_S-Nbar_1,
V=span(G, W_1 F[X]_<d) <= F[X]_<=j.                 (PC1)
```

If the exact boundary cell is nonempty, then:

1. `dim V=d+1` and `V` has no common root on `H'=H\roots(D)`;
2. the exact cell is in bijection with the full projective split-locator
   intersection

   ```text
   P(V) intersect Dloc_j(H');                         (PC2)
   ```

3. the hyperplane at infinity `P(W_1 F[X]_<d)` contains no point of
   `Dloc_j(H')`.

Thus the residual is exactly a gcd-trivial codimension-`w` Conjecture-F cell,
not merely an injection into one.

## Packing payment

Distinct locators in `(PC2)` have root-set intersection at most `d-1`.
Consequently

```text
|P(V) intersect Dloc_j(H')|
    <= floor( binom(n',d) / binom(j,d) ).             (PC3)
```

For `d=1` this is `floor((n-r)/(m-r))`; for every fixed `d` it is polynomial
in `n`.  More generally, if `j>=alpha n'` and `d<=alpha n'/2`, then

```text
binom(n',d)/binom(j,d) <= (2/alpha)^d.                (PC4)
```

Thus `d=o(n')` costs `exp(o(n'))`, and under an agreement reserve `R` it is
absorbable whenever `d=o(R log |B|)`.  Together with the rigid `r>=k`
branch, this pays the fixed-dimensional range and the sublinear-dimensional
range at the corresponding asymptotic scale.

## Scope

`(PC3)` is an anticode/packing ceiling, not row-sharp Q flatness.  It can be
exponential when `d=Theta(n)`, and it is not normalized by the
base-field average.  No quotient coalescing, smooth-puncture inheritance, or
finite adjacent reserve fit is proved.

## Round-25a instrument calibration (2026-08-09, coordinator-applied: the mystery-7 mechanism sharpened)

Measured at BOTH exhibited M31 flats (upstream #1148's 16-branch
fixture, parsed from its own shipped data; and our PROVED
l1_m31_fixed_support_divisor_direction_cap_route_cut fixture): the
flats of interest sit at this instrument's OWN known-counterexample
end r -> j (pairwise root overlaps 444-446 of degree 479, r/j =
0.931; and 4979/4980, r/j = 0.9998). The anticode ceiling at the
upstream flat is 2^840.2 against a truth of 16 — vacuous by 2^836.
**Mystery 7's wall is therefore NOT "the exponent grows with the
flat dimension" — it is that the live flats consist of locators
sharing almost all their roots.**

**THE LEAD (CANDIDATE, a coordinate-change proposal, not a bound):**
in SYMMETRIC-DIFFERENCE coordinates the same instrument becomes
sharp — at the upstream flat the 16 branches are 35-subsets
pairwise meeting in <= 2, giving C(514,3)/C(35,3) = 3437 vs truth
16 (2^7.75 loose instead of 2^836 vacuous); at our fixture the
complement count m - (t-1) = 67449 is the node's own count EXACTLY
(2^0). Caveats: the upstream "exactly the sixteen" truth rests on
their UNREPLAYED 10.69e9-normal C++ sieves (their synthesis +
Schur Python verifiers replayed PASS by us); the complement
structure is a property of the exhibited VERTICES — an arbitrary
hull member need not have its roots inside U. Own-repo
subtraction: complement coordinates appear once (a lineage note)
and never against the packing instrument. **[THE SUBTRACTION LINE
IS FALSE — corrected by the round-25 addendum below.]** Source:
notes/pilots_20260809/pr_harvest/ (fixture1148 measured;
mystery7_calibration SUPERSEDED banner on the invalid first
pricing).

## Round-25 correction + kill (2026-08-09, coordinator-applied on replay: m7_complement_repose)

**The CANDIDATE lead above is WITHDRAWN as a mystery-7 route — a
named kill with an exact threshold — and three lines of the
round-25a addendum are corrected.**

**(1) The subtraction line above is FALSE.** The instrument in
complement/difference coordinates is already PROVED in this repo
three times, all on the l1_mixed_petal_amplification consumer
chain: xr_lowcore_near_k_difference_packing (NK4) — the full
annulus form with an official prize-row payment table;
l1_band_complement_dimension_packing (CP2); and
l1_official_max_split_value_complement_census (MSC4). The
common-core orientation is moreover already deployed against the
m4_t3 red (its statement's fixed-owner bound after removing G).
The "coordinate-change proposal" was a re-derivation.

**(2) The 2^836 figure decomposes: 723 bits were a GROUND-SET
ERROR, not the root-sharing wall.** The fixture ambient (1023
points) is the evaluation domain; the root sets live in their
union U (514 points). Corrected ambient gives 2^117 (direct
orientation); the complement orientation gives 3437 = 2^11.75 vs
truth 16. Only ~105 bits are attributable to orientation/regime.

**(3) The mechanism sentence ("the live flats consist of locators
sharing almost all their roots") is TRUE at the two exhibited M31
flats and FALSE at our FPC5 cells.** Measured by FULL exact chart
enumeration (63/63 configs, ell=4 q in {97,193}, ell=5 q=127,
full contributor filters): pairwise-overlap mode 0 (60.5-86.5% of
mass), max = the sharpened cap ell-3, common core EMPTY (kappa=0)
and PENCIL_MAX=1 in every config. The root-sharing stratum DOES
appear in the ambient chart (one config produced a 75-member
sunflower P(X)(X-a), the M31 route-cut structure verbatim) and is
DELETED by our own guards (primitivity + untouched-petal
nonagreement: 94 -> 18 members). Mystery 7's wall is re-described,
not moved.

**The kill, stated exactly (PC3', proved base lemma):** with
kappa=|∩T_i|, sigma=|∪T_i|-kappa, a=j-kappa, delta=j-max|T_i∩T_j|,
the two orientations differ only through min(a, sigma-a), so the
complement orientation beats the direct one iff **sigma < 2a**.
Every rate-half FPC5 cell has |C|=5ell-5 against d=2ell-3 with
kappa=0 measured, so sigma/a -> 2.5 and the condition reads
"ell < -1" — never. The direct orientation is the m4_t2 node's
already-banked 2^(1.61 ell) sharpening (independently recomputed:
1.609). The complement orientation is strictly worse at every
cell, asymptotically 2^(2.097 ell), +0.49 bits/ell.

**REGISTERED FALSIFIER (reopens the route if exhibited):** one
FPC5 rate-half or large-source cell, satisfying its node's own
admissibility, whose GUARDED split members have ∩T_i ≠ ∅ or
|U| < 2d. Cheapest place to look: the M >= 5 large-source cells
legalized by the round-25 CJ transfer audit, where b can approach
ell — their overlap structure is UNTESTED. Vertex-vs-hull at the
M31 fixture: resolved by first-moment at scaled analogues (ratio
0.980 at t=6; pure sunflower, zero hull escape at t=9);
extrapolated E[extras] = 2^-128066 at the real parameters — the
"EXACT (2^0)" calibration survives with a first-moment
qualification, not proof. Source:
notes/pilots_20260809/m7_complement_repose/ (REPORT.md,
FABLE_AUDIT.md; D3 + D4 replayed byte-identical, Arm-A ell=4 q=97
and Arm-B t=9 replayed exact by the coordinator).
