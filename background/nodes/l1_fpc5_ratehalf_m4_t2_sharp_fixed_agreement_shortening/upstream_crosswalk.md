# Upstream crosswalk

- **upstream packet:** `przchojecki/rs-mca` PR #1125, `LIST: add
  balanced-pencil anchor determinant atlas`;
- **pinned head:** `f1503e54024f4949cf6542683712729e730eb6ca`;
- **upstream status at pin:** open, ready for review;
- **local supplier:** `l1_balanced_pencil_anchor_determinant_atlas`;
- **relation:** exact theorem specialization after the proved shortening,
  now exported upstream in the companion FPC5 note at this pin.

The parameter dictionary is

```text
upstream/local atlas n  = 5ell-5,
upstream/local atlas k  = 2ell-1,
exact shell m           = 3ell-2,
error-locator degree    = 2ell-3,
balance s               = ell-2.
```

Under this substitution the upstream coefficient determinant is a
degree-at-most-`ell-3` coordinate, its gcd with the anchor defect locator is
the FPC5 common-error owner, and the two fixed-owner bounds become `(SH8)`.
No field, object, quantifier, or unit changes: both sides count exact LIST
codewords in one received-word shell. The FPC5 contributors form a filtered
subset of that shell.

The exported theorem does not aggregate the possible gcd owners, preserve a
first-match owner for the FPC5 source chart, or prove a finite row numerator.
Those are the remaining shared obligations.
