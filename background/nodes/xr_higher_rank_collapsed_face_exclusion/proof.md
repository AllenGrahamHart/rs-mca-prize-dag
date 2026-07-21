# Proof

The dependency gives the normalized split-pencil family after puncturing
the common affine zero set `P_0`. Its kernel code is a fixed-coordinate
scaling of `GRS_a`; remove that common scaling from all functions. For an
active selected slope `gamma_i`, there is therefore a polynomial

```text
w_i in F[T]_<a
```

such that the normalized selected error vanishes wherever
`U-gamma_i q=w_i`.

Assume for contradiction that the collapsed branch occurs. By `(MF6)` in
the dependency, the restrictions of `U` and `q` to the active union `X`
have unique interpolants

```text
p_U,p_q in F[T]_<a.                                  (1)
```

The active row of the dual trade at slope `gamma_i` is supported on the
facet `S_i=X\{x_i}`. A dual row is assembled from parity checks of the
selected agreement block, so

```text
S_i subset A_i.                                      (2)
```

On `(2)`, both descriptions of the selected agreement give

```text
w_i(y)=U(y)-gamma_i q(y)
      =p_U(y)-gamma_i p_q(y),       y in S_i.        (3)
```

The difference

```text
w_i-(p_U-gamma_i p_q)
```

has degree less than `a`. Equation `(3)` gives it the `a+1` distinct roots
of `S_i`, so it is zero. Hence

```text
w_i=p_U-gamma_i p_q                                  (4)
```

as polynomials. Evaluating `(4)` on every point of `X` shows that the
selected error at slope `gamma_i` vanishes throughout `X`.

Before puncturing, every member of the selected affine family also vanishes
on `P_0`, and `P_0` is disjoint from `X`. Therefore every active selected
error vanishes on

```text
P_0 union X,
```

whose size is

```text
(k-a)+(a+2)=k+2.                                    (5)
```

There are at least four active rows with distinct slopes. Choose any two.
Equation `(5)` says their common zero set has size at least `k+2`, while the
post-strip high-core theorem built into the uniform split-pencil dependency
gives the cap `k` for every distinct-slope pair. This contradiction excludes
the collapsed branch.

The preceding dichotomy has no mixed branch. Its only remaining
minimum-union branch is therefore the regular face-syzygy space, and that
space is exactly the known Plucker kernel already quotiented there. The
general rank-two lower bound is `|X|>=a+2`; deleting the equality case leaves
`|X|>=a+3`, which is `(CFE4)`. QED.
