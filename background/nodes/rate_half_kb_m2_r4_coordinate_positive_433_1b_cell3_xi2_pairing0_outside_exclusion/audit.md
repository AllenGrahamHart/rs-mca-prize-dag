# Audit

- The source missing value is `m`, but the target `DE` product is `de=-m`.
  Losing this sign would test the already-paid positive copy instead.
- The negative `DE` squared-sum row is `(d-e)^2`, producing `(u-v)^2` after
  homogenization.  The positive-copy `(u+v)^2` equation is not reused.
- Norm zero is only necessary; every one of the eight roots is replayed in
  the original guarded equations.
- The target-free cut leaves two points per source sign, so the separate
  finite target solver is essential.
- The `32` point/lane fibers represent `16` raw atlas cases.
- No transport to `xi=3,...,6` or another matching is asserted.
