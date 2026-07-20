# Proof

For a proposed pair `(a,b)`, the matching-free boundary theorem says that
its boundary gate holds exactly when

```text
Y_b=-Y_a.                                             (1)
```

The dual row-product theorem gives

```text
R_(a,b)=-M/(C(a)C(b)).                                (2)
```

This is an `r`-th power exactly when its class in `G_r` is one. With
`mu=[-M]_r`, equation `(2)` is therefore equivalent to

```text
[C(b)]_r=mu [C(a)]_r^(-1).                           (3)
```

Equations `(1),(3)` say precisely

```text
Lambda(b)=tau(Lambda(a)).                             (4)
```

The map `tau` is an involution because

```text
tau^2(y,g)=(y,mu(mu g^(-1))^(-1))=(y,g).
```

It has no fixed points: a fixed point would require `y=-y`, impossible for
nonzero `y` in the official odd-characteristic field. Hence a perfect
matching satisfying both gates exists if and only if every label and its
`tau` image occur with equal multiplicity. This is exactly multiset
invariance under `tau`, and pairing corresponding occurrences gives the
reconstruction.

Finally multiply `(3)` over one endpoint `a` from each of the `e` pairs and
then multiply by the classes of their partners. Each pair contributes `mu`,
so

```text
[product_(a in R_A)C(a)]_r=mu^e=[(-M)^e]_r.
```

This proves `(JRM6)` and its equivalent power-membership test `(JRM7)`.
The monic resultant identities

```text
Res(A,C)=product_(a in R_A)C(a),
Res(B,C)=product_(t in T)C(t)=M
```

give `(JRM8)`. QED.
