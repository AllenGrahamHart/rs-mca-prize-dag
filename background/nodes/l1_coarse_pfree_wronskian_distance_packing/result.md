# Result

Every arbitrary-target coarse p-free locator fiber is a constant-weight code:
two distinct members must replace at least `ceil((d+2)/2)` roots on each
side. This yields the exact packing cap `(PWD4)` and, for scalar L1 prefixes,
the closed form `(PWD5)` with subset size `floor((a+k)/2)`. The theorem is
target-uniform and characteristic-safe. It removes close-pair concentration,
but the remaining linear-band packing cap can still be exponential. In fact,
when `a+k>=n` it is at least `2^(n-a)`, so under the official field cap it
cannot certify any cell with `n-a>=128`. Exact mixed/Pade fibers retain their
separate, stronger `d+1` codeword-distance bound.
