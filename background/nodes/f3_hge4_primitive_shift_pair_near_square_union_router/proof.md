# Proof

Let `(P,Q)` be an ordered primitive top shift pair and write its monic
locators as `A=L_P` and `B=L_Q`. Equality of the first `h-1` elementary
symmetric functions says that the two monic polynomials differ only in their
constant terms. Thus `A-B=2d` for some `d!=0`. Since the official
characteristic is odd, put

```text
S=(A+B)/2.
```

The supports are disjoint, so their union locator is

```text
D_U=AB=(S+d)(S-d)=S^2-d^2.                         (1)
```

This proves that every pair gives a valid near-square union.

Conversely, suppose `(NSU1)` holds. Then

```text
D_U=(S_U-d_U)(S_U+d_U).
```

The two factors are monic of degree `h` and coprime because `2d_U!=0`.
As their product is the squarefree locator of `U`, their root sets are
disjoint `h`-subsets partitioning `U`, and every root lies in `H`. The two
locators differ by a nonzero constant, hence give a top shift pair. The
primitive clause on `U` is exactly the primitive clause on this unordered
pair.

The centered polynomial is unique. If monic degree-`h` polynomials `S,T`
both satisfy that `S^2-D_U` and `T^2-D_U` are constant, then

```text
(S-T)(S+T)=constant.
```

Since `S+T` has positive degree, this forces `S=T`. The two square roots of
the nonzero constant exchange the factors. This proves the claimed
bijection.

Scaling preserves the construction: for `gamma in H`,

```text
D_(gamma U)(X)=gamma^(2h)D_U(X/gamma),
S_(gamma U)(X)=gamma^h S_U(X/gamma),
d_(gamma U)=gamma^h d_U.                            (2)
```

Now let `G_U` be the stabilizer of a valid primitive union. Uniqueness of the
unordered factorization means that every element of `G_U` either preserves
both reconstructed supports or exchanges them. The kernel of this action on
two supports is trivial by the proved free ordered-pair action. Hence
`G_U` injects into the two-element permutation group.

If `G_U` is nontrivial, its nonidentity element squares into the trivial
kernel, so it has order two. The dyadic cyclic group `H` has the unique
order-two element `-1`, and that element exchanges the two supports. Thus
every valid primitive union orbit is of exactly one of the two stated types.

Above a free union orbit, the two orientations lie in two distinct ordered
pair orbits. Above a swap union orbit, multiplication by `-1` connects the
two orientations, so they form one ordered pair orbit. This proves `(NSU2)`.

If the union stabilizer has size `s in {1,2}`, its scaling orbit contains
exactly `2h/s` distinct members containing `1`: the `2h` scales indexed by
elements of `U` are identified precisely in stabilizer cosets. Therefore a
free union orbit contributes `2h` anchored unions and a swap orbit contributes
`h`. Summing gives `(NSU3)`. Substitution into `(OAR2)` proves `(NSU4)`, and
`O_h^prim<=2(V_h^free+V_h^swap)` proves `(NSU5)`.

Substituting `A_h^union=hO_h^prim` into `(OAR3)` proves `(NSU6)`.

Finally,

```text
[binom(n-1,h-1)binom(n-h,h)]/binom(n-1,2h-1)
 =(2h-1)!/((h-1)!h!)
 =binom(2h-1,h-1),
```

which proves `(NSU7)`. QED.
