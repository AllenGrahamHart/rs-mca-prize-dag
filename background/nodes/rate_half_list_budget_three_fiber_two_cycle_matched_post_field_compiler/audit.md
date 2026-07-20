# Audit

## Field-character audit

The surviving congruence is only `2N | p-1`. This makes `mu_N` square-valued
but does not make it fourth-power-valued. Every converse uses only that
`-1`, `q_out`, `-q_out`, `lambda`, and `mu` are squares. The final square
condition is therefore expressed as `T/q_out` fourth-power, which is valid in
both field shards.

## Harmonic audit

The old certificate covers trace levels `1,...,38` for every official
`p=1 mod 2^40`. Exact order `2^41` can occur only for even `k`, namely
`p=1 mod 2^41`. The new preregistered campaign covered all `2,247,720` such
classes at level `39` in 16 complete shards and found no hit. Its maximum
reported shard time was below 1.67 seconds, well inside the 60-second and
`$0.25` caps.

## Equivalence audit

From Euclidean uniqueness, `T/q_out=Z^2`. In `F_p[x]` with `-1` square,
`Z^2` is fourth-power exactly when `Z` is square. Reciprocal replacement
multiplies by `q_out^2`, itself fourth-power because `q_out` is square. The
independent verifier exhausts the analogous nonsplit field `F_17` and finds
examples where the old `T` test fails while the corrected test agrees with
the direct square condition.

## Scope audit

The theorem covers only the matched two-antipodal-denominator generic floor.
It does not cover other matched quartics, mismatch strata, intermediate or
pure boundaries, or above-floor solutions. The later trace-Jacobi/norm
interface remains theorem work, so no large CR-002-C run is authorized.
