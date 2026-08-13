# Dependency sub-DAG

```text
gauge equivalence                    [PROVED]
sparse-direction punctured payment   [PROVED]
direction recursive shortening       [PROVED]
affine-span incidence counterexample [PROVED]
proper-subspace occupancy compiler   [PROVED]
full-rank lifted/gauge dichotomy      [PROVED]
full-lift near-MDS extension reduction [PROVED]
  -> rank/support replacement target [TARGET]
       -evidence-> rate_half_band_crossing_location
```

The refuted incidence nodes are not requirements.  The corrected compiler
pays low affine ranks and high-support prefixes.  The lifted-rank dichotomy
splits the top cell into an exact rank-drop branch and a full-lift branch,
and the near-MDS reduction computes the full-lift weight hierarchy exactly,
but leaves the printed middle intervals.
