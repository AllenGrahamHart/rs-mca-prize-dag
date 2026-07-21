# Proof

Because `T_i` is disjoint from `S_i=X\Z_i`, every extension point of `T_i`
that lies in `X` must lie in `Z_i`. This proves the disjoint split `(EC2)`.
For `i!=j`, disjointness of the zero fibers gives

```text
|S_i intersect S_j|=|X|-z_i-z_j=a+d+1-z_i-z_j.      (1)
```

It also gives

```text
T_i intersect S_j=I_i,
S_i intersect T_j=I_j,
T_i intersect T_j=O_i intersect O_j.                (2)
```

The four quadrants in `(1)--(2)` are disjoint and partition
`A_i intersect A_j`. Adding their sizes proves `(EC3)`. Subtracting the
support intersection from the cap `a` proves the equivalence `(EC4)`. The
nonnegativity of `ell_ij` is exactly the already proved shell inequality
`z_i+z_j>=d+1`. The zero-slack consequence is immediate because all three
terms on the left of `(EC4)` are nonnegative.

Sum `(EC4)` over unordered pairs. Each `|I_i|` occurs in exactly `t-1` pairs,
while

```text
sum_(i<j)|O_i intersect O_j|=sum_(x outside X)C(m_x,2). (3)
```

The right side sums to

```text
sum_(i<j)(z_i+z_j-d-1)
 =(t-1)Z-C(t,2)(d+1).                               (4)
```

Equations `(3)--(4)` prove `(EC5)`.

Finally, the actual-block router says independently that every `T_i` is a
`tau_i`-subset of `E_i`. The inside/outside split converts that condition
exactly into `(EC6)`, and `(EC4)` is equivalent to every pairwise block cap.
This proves the claimed finite compatibility characterization. QED.
