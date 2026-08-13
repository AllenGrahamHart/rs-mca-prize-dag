# Proof

The pure-split theorem supplies at least `e+7` parameter values `delta`
for which `G(delta,X)` has `n` distinct roots in the classified row set,
hence in `H`. The cover `C -> P^1_t` is etale above each such value.

Fix a geometric off-diagonal component `W`. Since both maps in the fiber
product are finite, `W` dominates the parameter line. If its degree over
the first copy of `C` is `h`, its degree over the parameter line is `nh`.
Above every pure value it therefore has exactly `nh` reduced points. Each
is an ordered pair of distinct base-field roots and is base-field rational.
At an etale fiber-product point there is only one geometric component.
Frobenius fixes the point and must therefore fix `W`. Thus `W`, and hence
its image `Z`, is defined over the base field.

The degrees over the two copies of `C` are equal: composing either
projection with the common degree-`n` parameter map computes the same
degree of `W -> P^1_t`. Call the common degree `h`. The row coordinate on
`C` has degree `m`, so both coordinate functions on `W` have degree `mh`.
If `q` is the generic degree of `W -> Z`, the two coordinate functions on
the normalization of `Z` both have degree

```text
D=mh/q.                                               (1)
```

This proves `(CDF2)` and the bidegree assertion.

Across the pure fibers, `W` has `(e+7)nh` distinct rational points. A
point of `Z` has at most `q` geometric preimages under the finite map from
`W`. All image coordinates lie in `H`, so

```text
#Z(H^2)>=ceil((e+7)nh/q)=ceil((e+7)nD/m).            (2)
```

We next remove the toral alternative. Suppose

```text
Z: X^aY^b=c,       gcd(a,b)=1.                      (3)
```

An actual point of `Z(H^2)` gives `c in H`. Coordinate-degree comparison
in `(1)` gives

```text
q|a|=q|b|=mh.
```

Hence `|a|=|b|`, and primitivity forces both absolute values to be one.
Thus `Z` is the graph of `Y=cX` or `Y=c/X`. The first projection
`W -> C` then has degree one, so this graph induces a nonidentity deck
automorphism of the degree-`n` cover. In the scaling case its order is a
power of two because `c in H`; in the reciprocal case its order is two.
But the deck-group order divides the odd cover degree
`n=2^38-3`. A nontrivial scaling or reciprocal automorphism is impossible,
while `c=1` in the scaling case is the deleted diagonal. Therefore `Z` is
not toral.

It remains to apply the audited Corvaja--Zannier bound. Suppose `D<D_0`.
Then `D<P_char`, the two coordinate differentials are nonzero, and the
normalization of a non-toral bidegree-`(D,D)` curve has

```text
chi<=2D^2.
```

The subgroup-point theorem gives

```text
#Z(H^2)<=max{
  3(4N^2D^4)^(1/3),
  12N^2D^2/P_char
}.                                                   (4)
```

Put `alpha=(e+7)n/m`. By the definition of `D_0`, every positive integer
`D<D_0` satisfies

```text
108N^2D^4<(alpha D)^3.                              (5)
```

The second term of `(4)` is also smaller than `alpha D`, since the exact
prime-field comparison is

```text
D_0 < 2^167 alpha/(12N^2).                          (6)
```

Equations `(2)`, `(4)--(6)` contradict each other. Hence `D>=D_0`.
Direct official substitution gives `D_0=39768216` and `(CDF5)`. Finally,
`D=mh/q>=D_0` gives

```text
q<=mh/D_0<4608h,
```

because `m<4608D_0`. This proves `(CDF4)--(CDF6)`. QED.
