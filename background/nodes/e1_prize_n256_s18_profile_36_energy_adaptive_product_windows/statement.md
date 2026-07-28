# E1 prize N=256 profile-(3,6) energy-adaptive product windows

- **status:** PROVED
- **closure:** analytic cap plus 6273 exact rational comparisons
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependencies:** bounded product windows and the multiplicity-one
  low-energy exclusion

For every profile vector, integer autocorrelation sharpens the conjugate-square
cap from `144` to

```text
y_u <= min(144,18+V).
```

The resulting exact product envelope gives

```text
m=256: V<=46,          m=514: V<=22.
```

For `m=514`, multiplicity one and the proved empty energies `E=2,...,6`
leave `E=7,...,11`. If `q` is the odd-autocorrelation weight, parity-adaptive
caps remove four more subchambers. The complete live interface is

```text
(E,q) in {(7,3),(7,7),(8,4),(8,8),(9,5),(9,9),
          (10,6),(10,10),(11,11)}.
```

This is a strict route contraction, not a cofactor exclusion.
