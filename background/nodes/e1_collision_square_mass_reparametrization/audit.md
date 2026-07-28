# Audit

- Canonical precursor `0acf7e8f` correctly identified `S=4a+b` and the three
  additional `S=16` splits.
- Canonical correction `c90a724b` correctly changed the `N=512` distance floor
  from `s>=3` to `s>=2`.
- The precursor's claim that `s` is unbounded at fixed quotient order is false:
  only `h` antipodal positions exist. This packet replaces it by the exact
  class-support bounds `H<=2T` and `S<=4T`.
- The formerly missing `ell` input is pinned by `acl_count` and the clean-anchor
  rows. It bounds the global range but does not eliminate any of the extra
  `S=16` splits.
- `verify.py` independently constructs valid class pairs for both official
  `N=256` subset sizes and checks every norm threshold using integer arithmetic.
- The theorem deliberately claims no modular collision and no collision-pair
  allowance.
