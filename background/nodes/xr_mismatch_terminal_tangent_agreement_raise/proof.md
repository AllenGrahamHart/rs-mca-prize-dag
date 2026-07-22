# Proof

Let

```text
Y={i:u_i=c_0(i) and v_i=c_1(i)}.
```

By hypothesis `|Y|>=A`. Put

```text
T=supp(u-c_0,v-c_1).
```

The true-tangent coordinate argument applies to the retained support-wise
bad witness. Its witness support must meet `T`; otherwise `(c_0,c_1)` would
jointly explain the received pair on that witness. Choose one coordinate
`i` in the intersection. The tangent identity `(TAR2)` and witness agreement
give

```text
u_i+zv_i=p_z(i)=c_0(i)+zc_1(i).                       (1)
```

Every coordinate of `Y` also satisfies `(1)`. Since `i in T`, it is not in
`Y`. Hence `p_z` agrees with `u+zv` on the disjoint set `Y union {i}`, of
size at least `A+1`. This proves `(TAR3)`.

The accumulated-locator theorem says that every pair reached by the
nongeneric descent is an original codeword pair and has an original common
agreement support of size at least `A`. At a terminal tangent its exact
global residual identity is `(TAR2)`. Applying the preceding argument to
each terminal pair puts every slope in the same original set
`B_(A+1)(u,v)`. Taking the union proves `(TAR4)` without summing over pairs,
paths, or locator flags.

Finally `B_(a+1)(u,v) subseteq B_a(u,v)` and `B_(n+1)(u,v)` is empty, so a
strict agreement raise can occur at most `n-A` times. QED.
