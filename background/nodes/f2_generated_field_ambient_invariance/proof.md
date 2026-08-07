# Proof

Write every element of `S` uniquely as `gy` with `y in T`. Then

```text
sum_(x in S) x^j = sum_(y in T) (gy)^j
                  = g^j sum_(y in T) y^j.
```

The same homogeneity argument gives `e_j(gT)=g^j e_j(T)`. Since `g` is
nonzero, multiplication by `g^j` preserves zero and equality. Scaling is a
bijection on the domain, commutes with complements, and sends each coset of
a subgroup `H<=mu_n` to the corresponding coset in `g mu_n`. This proves
the block assertions. If a block is a fiber of `P(X)`, substitution
`X=gY` gives the corresponding fiber of `P(gY)`; a zero top coefficient
remains zero after the resulting nonzero homogeneous scaling. Applying the
same substitution to every member gives the mixed-family assertion.

For `(AI-2)`, the `ell`th coordinate after scaling is

```text
sum_(x in W_0) a_x (gx)^ell
  = g^ell sum_(x in W_0) a_x x^ell.
```

Every `g^ell` is nonzero, so the diagonal map is invertible on its image.
The two syndrome maps therefore have the same kernel over `F_p`, and their
fibers correspond by the same diagonal map on syndromes. Rank, maximum fiber
size, collision sums, and every sum depending only on kernel words and their
coordinate weights are identical.

Finally, apply the proved 12-type classification. If `k<e`, replacing the
ambient field by `B=F_(p^k)` sends exactly the five plus order-one extension
types to `e=1`, and the plus/minus order-two degree-four types to `e=2`.
Together with the two order-four and the other generating types, only the
five signed generating types remain. QED.
