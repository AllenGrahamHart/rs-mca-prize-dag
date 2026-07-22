# Upstream crosswalk - first-checkpoint split-pencil reduction

This is a direct bridge from coarse `(Q)` collisions to upstream's
split-pencil census. The minimum width `t=p` across
`p<=d<=2p-2` is not a generic shift pair: it is exactly two split fibers of
`Z^p+Q`, with perturbation degree descending from `p-1` to one as depth
increases.

The terminal linear perturbation is closed by an official-domain argument:
an affine `F_p`-line has ratio set `p^2-p+1`, too large for the smooth
multiplicative coset under `11n<=256p`. The remaining lower-depth fibers are
a typed split-pencil census suitable for the upstream `(A)` lane; no bound
for that census is claimed here.

The same ratio method closes more than the terminal line. On the nonzero
fiber, every nonidentity multiplicative ratio has at most `deg Q` witnesses.
Hence all perturbation degrees at most
`floor((p(p-1)-1)/(n-1))` are impossible on each official row. The uniform
family floor is `floor(11(p-1)/256)`, but upstream row packets should consume
the stronger exact value. The residual begins strictly above that degree.

The proved successor `l1_official_split_pencil_value_capacity` specializes
upstream's one-parameter moving-root theorem to the surviving affine pencil.
It caps a fixed normalized `Q` at 23 split values and 253 unordered fiber
pairs. Therefore an upstream packet or compute request should present the
remaining object as a `Q` census with a bounded value payload, not as an
independent `(Q,b,c)` search.
