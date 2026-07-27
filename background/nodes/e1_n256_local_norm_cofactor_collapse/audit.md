# Audit

Date: 2026-07-27.

## External theorem pin

The load-bearing external input is the local reciprocity law and its explicit
cyclotomic specialization:

- Kiran S. Kedlaya, *Notes on class field theory*, Theorem 4.1.2 and
  Example 4.1.4,
  https://kskedlaya.org/cft/sec_localrecip.html .

The theorem identifies the norm group with the reciprocity kernel; the
example states that on `Q_p` units the cyclotomic component is
`a -> a^-1`. At conductor 256 its kernel is exactly
`1+256 Z_2`.

## Falsification replay

Modal run `ap-1mAvRBXG3IhB77PeHwGRiO` computed 513 exact FLINT
resultants across both profiles, including the full-conductor variance-36
witness. Every odd norm part was one modulo 256; no counterexample was found.
The run completed in 0.177 seconds of container work. It is not load-bearing.

The local verifier checks all cofactor ranges and mutation-controls the
congruence filter. No broad support or norm census is claimed.
