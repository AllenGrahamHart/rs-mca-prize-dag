# `A=1` shape-A static-source arbitrary-drop fence

- **status:** PROVED
- **closure:** every omitted-recurrence run length is compatible with one
  exact-corank-one all-nonzero static source
- **consumer:** `rate_half_band_crossing_location`

Let `d,n>=0`, put `R=d+n+2`, and let `U subset F` have `R`
distinct points. Assume that `F` contains at least `R+d+1` elements.
For every integer

```text
0<=q<=n,                                             (SDF1)
```

there are:

- a squarefree polynomial `Q` of degree `d), with all roots outside
  `U`;
- a polynomial `G` of degree `n-q), nonzero on both `U` and the
  roots of `Q`; and
- weights `omega_x in F^x` for every `x in U`

such that, for

```text
L(X)=product_(x in U)(X-x),
omega_x=G(x)/(Q(x)L'(x)),
h_j=sum_(x in U)omega_x x^j,                        (SDF2)
M=(h_(i+j))_(0<=i,j<=d),
R_j=sum_(i=0)^d q_i h_(i+j),
Q(X)=sum_(i=0)^d q_iX^i,
```

one has

```text
rank M=d,       ker M=span{(q_0,...,q_d)^T},        (SDF3)
```

and the omitted defects have exact initial zero-run length `q`:

```text
R_(d+1)=...=R_(d+q)=0,
R_(d+1+q)=lc(G)!=0.                                (SDF4)
```

For `q=0`, the empty string of equalities in `(SDF4)` means simply
`R_(d+1)=lc(G)!=0`.

Consequently, all-nonzero static source weights, exact middle-Hankel
corank one, the replacement-minor identities, and the bordered-source
determinant identities do not imply any nontrivial upper bound on the
degree-drop run. Such a bound must use structure coupling different
parameter values.

## Scope

The construction is one static moment functional. It does not realize the
global parameter-linear source pencil, the three-class source partition,
the split-fiber incidence grid, the scalar weld, the collision jets, or
Shape A itself. It fences only a source-pointwise non-stagnation argument.
