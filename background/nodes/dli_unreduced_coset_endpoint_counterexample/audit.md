# Audit

- Primality is certified by Proth's theorem using one modular exponentiation.
- The root-of-unity geometric sum proves all `t` power sums vanish at once;
  no subset enumeration is used.
- The half-band count uses exact binomial integers on 128 fibers.
- The near-cap normalization uses Bernoulli's inequality and the exact check
  `t(2^256-q)<2^255`; no floating-point logarithm is used.
- The witnesses are explicitly periodic, so the result cannot be widened to
  the primitive residue.
