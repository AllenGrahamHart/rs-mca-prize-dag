# Claim contract

## Consumed content

- The split-prime router supplies profile `(2,10,S=18)`, cofactor `1028`,
  and the prize field floor.
- The conductor-256 autocorrelation dictionary supplies the 64 positive
  conjugate squares, their mean, and their second moment.
- The square-mass-18 global energy window leaves only energies `E=2,...,6` after its
  elementary zero- and one-energy exclusions.

## New proved content

1. Every energy-five or energy-six conjugate deviation lies in `(-18,12]`.
2. A rationally certified quadratic logarithm majorant holds on that whole
   interval.
3. Energies five and six force `Norm(F(zeta_256))<1028*p_min`.
4. The live cofactor-`1028` energy set contracts to `{2,3,4}`.

## Guards

- The argument uses no support census, finite-field heuristic, or numerical
  logarithm.
- It bounds the norm itself, not a sampled or approximate norm.
- It neither excludes energies two through four nor reduces the 128 prime
  ideals above `257`.
- The parent E1 target remains open.
