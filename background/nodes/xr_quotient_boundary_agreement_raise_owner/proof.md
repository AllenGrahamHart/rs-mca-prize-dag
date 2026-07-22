# Proof

Fix a declared fiber size `c`. The remainder-one boundary descent gives

```text
Q_c(>=A)=Q_c(A) union T_c(A).                           (1)
```

Take `z in T_c(A)`. By definition there are `B>A`, a support

```text
S=S_0 union {x},       |S|=B,
```

and a codeword pair `(c_0,c_1)` that explains `(u,v)` on the pure-fiber core
`S_0`. The boundary theorem also gives a witness codeword

```text
p_z=c_0+z c_1                                           (2)
```

and says that `x` is a genuine discrepancy coordinate at which the affine
error cancels.

The codeword `p_z` agrees with `u+zv` on every point of `S_0` by the common
pair explanation, and it agrees at `x` by the boundary witness. Thus it
agrees on all `B` points of `S`. Since `B>A`,

```text
agr(u+zv,p_z)>=B>=A+1,
```

so `z in B_(A+1)(u,v)`. This is the agreement-raise owner applied to the
boundary tangent. It does not depend on which pure-fiber core or quotient
scale produced `z`. Therefore

```text
T_c(A) subseteq B_(A+1)(u,v)                            (3)
```

for every `c`. Substitute `(3)` into `(1)` and take the union over the finite
declared scale family to obtain `(QAO1)`. QED.
