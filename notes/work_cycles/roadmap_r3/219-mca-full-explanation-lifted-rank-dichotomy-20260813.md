# Cycle 219: MCA full-explanation lifted-rank dichotomy (2026-08-13)

Cycle 218 left the widest cells at explanation affine rank equal to the
shortened code dimension `K`.  The new theorem separates them using the
affine rank `h` of the lifted pairs `(gamma,c_gamma)`.

After anchoring one slope, explanation differences span all of `C`, while
lifted differences lie in `F direct_sum C`.  Hence

```text
h in {K,K+1}.
```

If `h=K`, the lifted space is the graph of a nonzero functional
`ell:C->F`.  Every gauge `b` on the affine hyperplane `ell(b)=1` drops the
transformed explanation rank exactly to `K-1`.  If `h=K+1`, the lifted space
is all of `F direct_sum C` and no codeword gauge drops rank.

Pair noncontainment forces `r_1` outside the code, so the map

```text
(a,u) -> a r_1-u
```

is injective on the lifted space.  Thus the selected error-vector affine
rank is exactly `h`.  This identifies the split simultaneously in the
fixed-core and all-LineRay languages.

The gauge-drop branch inherits the penultimate-rank occupancy wall because
direction coset support is gauge invariant:

```text
KoalaBear q=14, h=14:   e<=5 or e>=992852;
KoalaBear q=14, h=15:   e<=5 or e>=1044239;
Mersenne  q=6,  h=6:    e<=1 or e>=1037876;
Mersenne  q=6,  h=7:    e<=1 or e>=1044242.
```

The primary `GF(7),K=3` control exhausts 686 gauges: the drop branch has
49 rank-dropping and 294 other gauges, while all 343 gauges in the full-lift
branch retain full rank.  An independent `GF(5),K=2` implementation checks
50 gauges and a hostile rank-raising perturbation.

```text
start:                   d9b81e631
canonical prize:         c8d48cd4b
upstream main:           93fba1be
relevant upstream PRs:   #1163, #1164, #1165
upstream export head:    #1165 @ 0a4960f6
result:                  NARROWED + EXPORTED; one PROVED structural dichotomy
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
upstream terminal delta: proved fixed-core/all-LineRay correspondence,
                         exact top-rank split, and fourth verifier added to
                         PR #1165; dependency comments added to #1163/#1164
delta-star movement:     none
compute:                 exact bounded local arithmetic under RAMguard
next route action:       attack the full-lift top-rank middle-support
                         interval without assuming a gauge rank drop
```
