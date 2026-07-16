# XR rank-five collision directions form a star configuration

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_rank_five_divided_difference_clique_bridge`

Let `A` be a retained agreement set in the P-A `u=v=0` rank-five `r=2`
core, and put `m=|A|=4+h`. In the affine four-space of cubic polynomials,
define

```text
H_x={p:p(x)=q(x)}              for x in A.
```

The hyperplanes `H_x` are in simple position: every four have the unique
intersection `I_Tq`, and no five have a common point. Thus the collision-line
directions

```text
r_T=q-I_Tq,       T subset A, |T|=4,
```

form the projective image of the `C(m,4)` vertices of a four-dimensional
star configuration.

More precisely, if `F` is a nonzero polynomial of degree `d<=h` on the
cubic-coefficient space, then

```text
#{T: F(I_Tq)!=0} >= C(m-d,4).                         (SC)
```

The bound is sharp. At `d=h`, evaluation on the vertices is an isomorphism
from polynomials of degree at most `h` to all functions on the vertices.

For the reused direction sets in the official `r=2` cores, (SC) implies that
no nonzero direction polynomial of degree at most

```text
4,4,2
```

can vanish on every reused direction at rates `1/4,1/8,1/16` respectively.
This is a local direction-rigidity theorem. It does not count the selected
points and does not promote P-A.
