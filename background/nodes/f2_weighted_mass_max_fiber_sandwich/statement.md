# F2 weighted mass and heaviest-fiber sandwich

- **status:** PROVED
- **closure:** proof

Let `A:F_p^m -> V` be linear, let

```text
N(v)=#{S subset {1,...,m}: A 1_S=v},
M=max_v N(v),
Z(A)=sum_(eps in ker(A) intersect {-1,0,1}^m) 2^-wt(eps).
```

Then

```text
M^2/2^m <= Z(A) <= M.                               (MF-1)
```

If `A` has rank `d` and a row-sharp quotient/prefix estimate has the
normalized form

```text
M <= Lambda_Q * (2^m/p^d) + E_Q,                    (MF-2)
```

then, with no further loss,

```text
Z(A) <= Lambda_Q * (2^m/p^d) + E_Q.                 (MF-3)
```

Each `N(v)` is the output size of binary full-agreement list recovery in
one affine coset of `ker(A)`. Consequently, any uniform subexponential
max-fiber bound pays the weighted-mass terminal for both the plus-branch
GRS maps and the coupled minus-branch root-code maps.

This theorem is an exact interface. It does not prove `(MF-2)`, quotient
flatness, a weighted-mass upper bound, or an F2/Prize close.
