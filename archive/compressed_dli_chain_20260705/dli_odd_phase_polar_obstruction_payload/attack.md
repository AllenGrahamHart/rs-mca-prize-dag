# ATTACK - dli_odd_phase_polar_obstruction_payload

This is now an assembly node. The live DLI leaf is
`dli_reduced_phase_manifest_payload`.

Needed output at the reduced-phase manifest:

- choose the local point(s) on each relevant square-root component where the
  odd-evaluation phase can have a pole;
- write `P_lambda(sigma(y))` in a local parameter after all forced central
  profile relations are imposed;
- perform the Artin-Schreier reduction of the local expansion, removing
  `p`-divisible leading polar terms;
- exhibit a remaining pole whose order is positive and not divisible by `p`;
  and
- verify uniform coverage over every central profile, nonzero frequency,
  DLI harmonic, and square-root component in the DLI ranges, including the
  reduced-pole majorant row for the same tuple.

The soundness of this certificate format is proved in
`dli_odd_phase_polar_obstruction_soundness`. The missing content is the actual
DLI reduced-phase manifest.
