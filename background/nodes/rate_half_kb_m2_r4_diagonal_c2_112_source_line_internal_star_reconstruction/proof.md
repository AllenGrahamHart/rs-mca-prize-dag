# Proof

The reciprocal `U` spaces have dimensions five and four. Evaluation at the
forced label `w` is surjective in both signs, including the repaired
ramified case `w=0`. Membership in the nonzero line `<q>` has codimension
two, so `S_+(w,q)` and `S_-(w,q)` have dimensions three and two.

Suppose `U in S_epsilon(w,q)` and `U(T,z)=0`. Reciprocal symmetry also gives
`U(T,z^(-1))=0`. The internal orbit is unramified and fixed-point-free, so
`z!=z^(-1)`. Hence

```text
U(T,W)=chi_z(W) R(T),
chi_z(W)=(W-z)(W-z^(-1)).                           (1)
```

The positive reciprocal quadratic `chi_z` and the source reciprocity of
`U` imply

```text
T^2 R(1/T)=epsilon R(T).                           (2)
```

The forced orbit differs from the internal orbit, so `chi_z(w)!=0`.
Because `U(T,w) in <q>`, equations `(1)--(2)` would make `q` an endpoint
reciprocal eigenform of sign `epsilon`. That is impossible: the roots of
`q` are `J_1`, while `tau(J_1)` lies in the disjoint crossing subset of
`I`, so the root set of `q` is not `tau`-invariant. Thus `R=0`, proving
injectivity in `(KBSR-1)`. The source and target dimensions make the
positive map an isomorphism and the negative image a two-plane.

At the two source points `x,-x` over `z`, write

```text
H(T,x)=lambda e(T),       H(T,-x)=mu f(T).          (3)
```

Both scalars are nonzero because the stars are nonzero. Subtracting and
adding `(3)` gives `(KBSR-2)--(KBSR-4)`. The preceding odd-part incidence
gate proves that `e,f` share exactly one root, so their span is the full
two-dimensional space of quadratics divisible by that common linear form.
The equation `V(a,z)=0` puts `V(T,z)` in this span. Since `V(T,z)` cannot be
zero when `e,f` are distinct and both scalars in `(3)` are nonzero,
`(KBSR-2)` determines `lambda,mu` up to their common normalization.
Consequently `(KBSR-3)` is fixed in the same normalization as `V`.

Injectivity of `ev_z` now proves uniqueness of `U` whenever `(KBSR-4)` is
solvable. Positive surjectivity gives existence for every target quadratic;
the negative image has codimension one and gives the printed linear test.

Finally enumerate the six edges on `J_0` with its two-pair involution. The
one-unit pure defect condition leaves five four-edge multisets. Their
numbers of unordered pairs `(e,f)` satisfying

```text
{e,f,tau(e),tau(f)} = the printed multiset
```

are `2,2,4,2,2`. Thus there are at most four edge assignments and two signs,
or eight reconstructed forms, per packet. QED.
