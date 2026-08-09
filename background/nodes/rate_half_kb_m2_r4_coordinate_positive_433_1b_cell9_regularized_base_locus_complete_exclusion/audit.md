# Audit

- The census uses the reconstructed nonzero pointwise kernel, never the zero
  global section.
- Missing product and squared-sum equations are imposed for every omitted
  role because reconstructed `A(-t^2)` is nonzero.
- All 105 role/matching labels are explicit in each lane.
- Intermediate Groebner bases are killed after each system to bound remote
  memory; this does not change exact arithmetic or the transcript.
