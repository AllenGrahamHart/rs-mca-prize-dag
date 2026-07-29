# Audit

## Independent reconstruction

1. Fixed `P_r` makes all occupied `Q_s` equal in `Cl(L)`.
2. Relative ideal norm preserves equality of ideal classes.
3. Complete splitting of 257 makes `N_(L/K)(Q_s)` a degree-one prime, not a
   nontrivial power.
4. Squaring primitive 256-th roots modulo 257 maps 128 roots onto the 64
   primitive 128-th roots with fibers `{s,-s}`.
5. Pairwise separation of the 64 classes in `K` therefore permits at most one
   lower prime and two upper primes.

## Boundary checks

- `257=1 mod 256`, so no residue-degree factor was omitted.
- The ramified prime `(1-zeta_256)` is principal and disappears in the class
  equation.
- Equality of classes, rather than equality of ideals, is exactly what ideal
  norm transports.
- The proof gives two, stronger than the required five.

## Open dependency

The n=64 prime-class orbit has not been independently reconstructed. This
node remains `CONDITIONAL` even though the published coordinates pass the
tiny orbit arithmetic.
