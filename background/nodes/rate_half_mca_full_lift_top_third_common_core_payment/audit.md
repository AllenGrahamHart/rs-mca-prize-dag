# Audit

- Layers with `h>m` are empty and are omitted through `r_0=max(0,e-m)`.
- The affine-line synchronization remains layer-local.
- The total common core is a simultaneous base/direction pair support;
  pair noncontainment, not a polynomial root bound, limits it to `m-1`.
- The outside common core separately has size at most `K-1`.
- Layers with at most `K-1` outside agreements use the total-core cap
  `N-m+1`; no division by a nonpositive outside slack occurs.
- KoalaBear stops on a negative Johnson denominator.  Mersenne stops on a
  valid over-budget profile.  Neither is an unsafe certificate.
- The full scan uses exact integers and constant memory under RAMguard.
