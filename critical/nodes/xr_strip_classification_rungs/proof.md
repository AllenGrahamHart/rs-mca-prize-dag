# Proof of the XR strip and classification rungs

The quotient and tangent strip bounds are the already-proved ledger inputs
consumed by this carrier. At every deciding row `j=n-A` is odd. A nontrivial
dyadic quotient cell requires its even fiber scale to divide `j`, so the
strict integral quotient census is zero; `B_quot_ub` is retained as the
conservative floor-rounded charge.

For the classification rung, let distinct slopes `z_1,z_2` carry codewords
`c_1,c_2`, and suppose both rays agree with `u+z_i v` on a common core `R`.
Since `z_1-z_2` is invertible, define

```text
g = (c_1-c_2)/(z_1-z_2),
f = c_1-z_1 g.
```

Both `f` and `g` have degree `<k`. On every point of `R`, subtraction gives
`g=v` and then `f=u`. Thus a distinct-slope pair with `|R|>=k+1` forces the
received pair to a codeword pair on more than `k` points. [ITEM-3
CORRECTION, ratified 2026-08-02 — see
`notes/BAND_OVERCLAIM_FLAG_20260802.md`.] The forcing is PROVED for all
cores `>=k+1`; no core-based CHARGE is proved at any threshold. The generic
core ceiling is `A-1`, sourced from genericity plus this forcing algebra
(core `=A` between exact-`A` selected supports coincides them, and the
forcing then yields a joint `A`-support explanation, i.e. the nongeneric
branch). The band `[k+1,A-1]` is CLASSIFIED, not removed: under the
ratified Route T partition it is carried by the third generic column
(`xr_graded_tangent_band_charge`, cascade tier `d=h-1` included), and the
post-band-column remainder has pairwise cores at most `k` by construction
of the partition, not by this rung.

The six-row integer calculation then subtracts `B_quot_ub(A)` and `n-A+1`
from `B*`. Direct evaluation gives at least `29 n^3` residual allowance on
every row; on each prize row it gives less than `30 n^3`. Therefore the
generic allocation `8 n^3+8 n^3` and the combined nongeneric allocation
`16 n^3` both fit.

The registered verifier runs two independent banked implementations. The
first rederives all six candidate values, quotient charges, tangent charges,
residual integers, and the `16/29/30` comparisons (69 checks). The second
replays the line/ray identities and the forcing algebra over deterministic
toy rows, including 4,662 nonvacuous forced pairs and a separate `t=3`
control (88 checks). The toy replay confirms the implementation and object
orientation; the displayed algebra is the field-generic proof.
