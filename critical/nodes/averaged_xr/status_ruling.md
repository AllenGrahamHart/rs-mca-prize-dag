# Status ruling

The 2026-07-27 demotion was correct for the former auto-proof: it cited a
nonexistent conditional packet and used an exponent dictionary as though it
proved de-correlation.

The repaired closure is independent of that argument. Przemek's repository
already contained a later exact theorem in
`experimental/notes/m1/m1_average_support_collinearity.md` and the occupancy
consumer in `experimental/notes/m1/m1_averaged_slope_conversion.md`, both
introduced at commit `674503f72134eaed4a20f1944f1423b23744ce2c`. The proof
has been rederived locally and replayed with an independent interpolation-
matrix verifier.

The status is therefore `PROVED` only for the exact fixed-slope pair moment
stated here. The wider worst-case XR claims remain outside this closure.
