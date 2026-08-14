# Proof

Let `D` be the official evaluation domain and choose `J subset D` with
`|J|=K-1`. Put

```text
u(X)=product_(x in J)(X-x).
```

Then `deg u=K-1`, `u` vanishes exactly on `J`, and `u` is a nonzero RS
codeword. Fix `B subset J`, `|B|=9`. Nine degree-at-most-eight interpolation
polynomials together with `u` span a ten-space `V` whose evaluation on `B`
has rank nine and kernel `F u`.

Outside `J` there are

```text
N=n-(K-1)=1048577
```

coordinates, while a rich support needs outside weight

```text
L=m-(K-1)=67473.
```

Assign eight owner points `P_i=(a_i,0)` weight `L-1=67472` each. Assign the
remaining

```text
M=N-8(L-1)=508801
```

coordinates weight one at points `Q_j=(j,1)`, `0<=j<M`. Choose
`a_i=c+iM`. The `8M=4070408` values

```text
gamma_(i,j)=a_i-j
```

are distinct: before the common translate `c`, the eight difference
intervals are consecutive and disjoint. Since the KoalaBear base prime is
`2130706433>18*4070408`, `c` can also be chosen so that these slopes avoid
any prescribed eighteen forbidden values.

At a coordinate labelled `(alpha_x,beta_x)`, define

```text
r_0(x)=alpha_x u(x),       r_1(x)=beta_x u(x),
```

and set both received columns to zero on `J`. For `(i,j)`, use the codeword

```text
h_(i,j)=a_i u.
```

The equation `alpha+gamma_(i,j) beta=a_i` contains exactly `P_i` and
`Q_j` among the assigned owner points. Hence the agreement support is

```text
J disjoint_union fibre(P_i) disjoint_union fibre(Q_j)
```

and has size `(K-1)+(L-1)+1=m`. All slopes are distinct. No polynomial pair
contains this support. Indeed, its second component would agree with `r_1=0`
on `J union fibre(P_i)`, a set of size `m-1>K-1`, and hence would be zero by
the RS root bound. At the remaining point `Q_j`, however, `r_1=u!=0`. This
is a contradiction. In particular the visible owner `P_i` itself has core
only `J union fibre(P_i)`, of size `m-1`.

Choose two coordinates in `fibre(P_i)` and adjoin them to `B`. The resulting
eleven-subset has evaluation rank ten, and the fixed owner `P_i` makes its
parameter line a positive-dimensional affine-owner component. Finally,

```text
e_(i,j)=r_0+gamma_(i,j)r_1-a_i u,
```

so all error differences lie in `span(r_1,u)`. The error affine rank is at
most two. Every owner in the plane agrees with the received pair on exactly
the common set `J`, which has size `K-1`. This proves every asserted local
property and the strict numerical fence.
