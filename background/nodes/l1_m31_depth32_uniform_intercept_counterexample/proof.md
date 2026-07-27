# Proof

Write the `1024` quotient labels as

```text
q_r=2^(-2047) Re(g^(r 2^19)) mod p,
g=(1717986917,1288490189),
r odd, 1<=r<=2047,
```

in `F_p[i]`, `i^2=-1`. Delete the labels represented by `r=1,3`.
The exact finite-field reconstruction verifies that the remaining labels are
distinct.

A `T_16` class named by odd `a in [1,127]` consists of the sixteen odd
representatives congruent to `a` or `256-a` modulo `256`. A `T_64` class
named by odd `b in [1,31]` consists of the sixty-four odd representatives
congruent to `b` or `64-b` modulo `64`. Thus each intact `T_64` class is the
disjoint union of four `T_16` classes.

The anchor is the union of the twenty-nine complete `T_16` classes

```text
5,7,9,11,13,17,19,45,47,51,53,55,57,59,69,71,73,75,
77,81,83,109,111,115,117,119,121,123,125
```

and the fifteen surviving members of class `3`. The first twenty-eight
complete classes are exactly the seven intact `T_64` classes

```text
5,7,9,11,13,17,19;
```

class `125` and the punctured class `3` form the fixed degree-`31` residual.

The other seven intact `T_64` classes are

```text
15,21,23,25,27,29,31.
```

Exchange any three selected classes for any three complementary classes.
There are `C(7,3)^2=1225` distinct results, each at deficiency `3*64=192`.
The locator polynomials of the fourteen intact `T_64` classes have identical
nonconstant coefficients: they are constant translates of the same monic
degree-`64` Chebyshev polynomial. Therefore varying three class constants in
a product of seven such factors can first affect degree `384`; multiplying
by the fixed degree-`31` residual can first affect degree `415`. The first
`32` nonleading coefficients of the degree-`479` locator, at degrees
`478,...,447`, are unchanged.

For the twelve mixed supports, remove and add the twelve class sets printed
in upstream PR #1102. Direct multiplication of their degree-`479` locators
over `F_p` gives the anchor's same first `32` coefficients. Each exchange is
disjoint and has size twelve on each side, so its deficiency is `12*16=192`.
Their `T_16` class sets are pairwise distinct. Each has a partially occupied
intact `T_64` class, whereas every whole-class exchange has occupancy zero or
four in every intact `T_64` class, so the two families are disjoint.

Hence

```text
d_192(A)>=1225+12=1237>1233,
```

and `192` lies in the claimed band. This proves the route refutation.
