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
and never against the packing instrument. Source:
notes/pilots_20260809/pr_harvest/ (fixture1148 measured;
mystery7_calibration SUPERSEDED banner on the invalid first
pricing).
