# Audit - pma saturated mixed-support kernel

## Checked axes

1. `X` is the exact noncore agreement support. Extra agreements are separate
   guards in the converse direction; the linear kernel alone does not forbid
   them.
2. Label classes aggregate equal labels. Distinct source labels are
   load-bearing in the cofactor injection; treating two equal labels as two
   classes makes the rank statement false.
3. The PMA inequalities `a_j<=d`, `a_j<=ell`, and background size `<ell` are
   used. The theorem is not an ambient statement for arbitrary class sizes.
4. The exceptional rank loss is exactly one dimension and can occur only at
   zero slack with a full petal. The verifier contains a sharp rank-one toy.
5. Exactness of `D`, not merely splitness of `F`, proves `gcd(F,W)=1`.
6. Common-factor multiplication produces duplicate lower-defect codewords,
   not a new large family. It must not be counted as kernel growth.
7. The dual moment matrix uses the exact `L_X'(x)` weights. Dropping them or
   replacing realized labels by an ambient codomain changes the kernel.
8. Maximal rank uses both `deg F=d` and `gcd(F,W)=1`. A common-factor
   representation can have rank strictly below `min(d,w)`.
9. The root-pinning map is per exact labelled support `X` and source core. Its
   binomial bound can be exponential when `d-w` grows and cannot be summed
   naively over support patterns.

## Adversarial controls

The verifier checks:

- a strict mixed pattern where `rank=a_*`;
- the zero-slack full-petal exception where `rank=a_*-1` is sharp;
- collapse of distinct labels, which destroys the claimed rank;
- a multiplied common-factor representation, which gives the same codeword
  contribution but fails the exact-defect and gcd guards;
- exact interpolation, fiber divisibility, and pairwise coprimality on a
  reduced rational-map toy;
- equality of the top-coefficient and weighted-Hankel kernels;
- maximal rank in the regimes `d<w`, `d=w`, and `d>w`;
- exhaustive fixed-core split-locator counts against the root-pinning bound;
- an unsaturated common-factor rational map where maximal rank fails.

## Remaining attack

Aggregate the root-pinned fixed-pattern charges over exact supports, defects,
and first-match layouts. Large `binom(k-1,max(0,d-w))` regimes must be sharpened
or assigned once to a legitimate natural-scale profile; multiplying this
bound by a raw support census is not a polynomial theorem.
