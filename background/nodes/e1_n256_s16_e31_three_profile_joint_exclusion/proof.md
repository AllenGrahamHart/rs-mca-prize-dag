# Proof

The proved E31 profile/parity/light reduction leaves exactly three magnitude
profiles and classifies every possible four-point light support into the eight
affine odd-unit orbits

```text
{0,t,2t,64}, {0,t,32,64},       t in {1,2,4,8}.
```

Translation and multiplication by an odd unit preserve the magnitude profile,
the cyclotomic norm, `M_3`, and full-versus-proper conductor. It is therefore
enough to inspect one representative of each orbit.

For each representative, both engines choose the three heavy positions from
the remaining 124 positions and inspect all 64 relative sign choices after
fixing the first heavy coefficient to `+2`. Global sign does not affect any
tested invariant. Hence each engine covers exactly

```text
8*binom(124,3)*64 = 158,783,488
```

representative vectors.

The production engine folds the 21 support chords directly into positive-half
autocorrelation classes. The audit engine independently multiplies the full
coefficient vector by its negacyclic reverse in `Z[x]/(x^128+1)` and verifies
the expected anti-palindromic identities before extracting the positive half.
Both classify profiles and compute `M_3` from the resulting exact integer
autocorrelation. They agree on every aggregate in the statement.

The E31 reduction proves that `M_3<=1302` puts the cyclotomic norm strictly
below `2^250`. The unrestricted maxima for `(2,5,1)` and `(1,3,2)` are 1068
and 1122, so those profiles are impossible. The full-conductor maximum for
`(3,7)` is 1206, so every full-conductor vector in that profile is impossible.
The remaining 3348 representative `(3,7)` vectors have proper conductor and
are excluded by `e1_n256_proper_conductor_collision_exclusion`. The three
profiles exhaust the E31 reduction. QED.
