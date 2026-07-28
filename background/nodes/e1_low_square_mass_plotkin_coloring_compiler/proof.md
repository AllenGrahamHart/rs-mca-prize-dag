# Proof

Let `x_1,...,x_M` be distinct signed singleton vectors in one E1 fiber and in
one color class of `G_p(ell)`. Because the coloring is proper, no pair is a
low-square-mass collision. Every pair is already in the same fiber, so

```text
S(x_i,x_j)>2ell.
```

Square mass is even, hence `S(x_i,x_j)>=2ell+2`. The Euclidean variance
identity gives

```text
sum_{i<j} ||x_i-x_j||^2
  = M sum_i ||x_i||^2 - ||sum_i x_i||^2
  <= M sum_i ||x_i||^2
  <= M^2 ell,
```

because each class vector has at most `ell` singleton coordinates. The lower
bound from the pairwise separation is

```text
sum_{i<j} ||x_i-x_j||^2
  >= binom(M,2)(2ell+2)
  = M(M-1)(ell+1).
```

Combining and cancelling `M>0` gives

```text
(M-1)(ell+1)<=M ell,      hence M<=ell+1.
```

Each fiber meets each of the `c` color classes in at most `ell+1` vertices,
so its size is at most `c(ell+1)`. Partitioning all `K` classes into fibers
then gives `L>=ceil(K/(c(ell+1)))`.

For one row, this image floor exceeds `B*` whenever

```text
c(ell+1)B* < K.
```

The largest admissible integer is therefore
`c_max=floor((K-1)/(B*(ell+1)))`. Substitution of the six exact `K,B*` pairs
from `e1_clean_anchor_exact_collision_allowance` gives the table in
`statement.md`. The verifier recomputes every quotient, fiber cap, image
floor, strict inequality, and one-color-too-many boundary. QED.
