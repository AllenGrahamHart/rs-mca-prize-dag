# Budget-three affine-rank rigidity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Let `d>=3`, let `C=RS[F,D,2d]` have length `n=4d`, and let `u in F^D`.
If four distinct codewords satisfy

```text
agr(c_i,u)>=3d-1,       i=0,1,2,3,                  (ARR1)
```

then the four codewords are affinely independent. Equivalently,

```text
dim span{c_1-c_0,c_2-c_0,c_3-c_0}=3.               (ARR2)
```

More precisely, a hypothetical affine-rank-two witness would be forced to
have a common direction-zero set `G` of size `2d-2`, common agreement on all
of `G`, exact agreement `3d-1` for every codeword, and exactly two agreeing
codewords at each of the remaining `2d+2` coordinates. After factoring the
locator of `G`, the four codewords differ by four distinct affine-linear
polynomials. Their six pairwise differences can vanish at only six distinct
coordinates, contradicting `2d+2>6`.

This is a codeword-affine-rank statement. It does not identify codeword rank
with the rank of the locator Plucker line or quadratic scroll in the
thirteen-chamber atlas, and it excludes no chamber without such a bridge.
