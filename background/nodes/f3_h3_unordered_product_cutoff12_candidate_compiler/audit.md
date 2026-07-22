# Audit

1. `Ucal_n` includes diagonal pairs once. Deleting them would make `(UPC4)`
   and the cutoff conversion false.
2. The derivative depth is 12: zeroth through twelfth Hasse derivatives
   detect multiplicity at least 13.
3. The scalar criterion `(UPC5)` is exact for unordered multiplicity, not for
   ordered multiplicity `P>=25`.
4. The boundary `U=13,D=2` has `P=24` and is a genuine false positive. A
   candidate-prime certificate must replay `D` as well as `U`.
5. DSP8 excludes `t=1`, but `P(1)` can be large. The inverse selector
   `(T-1)Y-1` is required; the unsaturated derivative scalar may be polluted
   by identity-only richness.
6. `p=1 mod n` guarantees simple split `n`th roots and excludes `p|n`.
7. The degree comparison is `n(n-1)/2` versus `(n-1)^2`; it does not imply a
   measured runtime or memory ratio.
8. The unique square root is a construction identity over `Z[T]`, not a
   recommendation to expand either official-scale dense polynomial locally.
