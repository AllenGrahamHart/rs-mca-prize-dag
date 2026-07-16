# DLI ell-two weight-five pair-quadratic router

- **status:** PROVED
- **closure:** proof

Let `F` have characteristic different from `2,3`, let `H<=F*` be cyclic of
order `M`, with `M` even, and let `R` be an antipodal-free five-subset of `H`.
Then

```text
sum_(r in R) r = sum_(r in R) r^3 = 0
```

if and only if the following router succeeds.

Choose `e in R`, choose an unordered pair `{a,b}` from `R\{e}`, scale by
`e^-1`, and put

```text
x=a/e, y=b/e, u=x+y, A=xy,
v=-1-u, B=u(v-A)/v.
```

The antipodal-free hypothesis gives `u,v!=0`. The other two scaled roots are
exactly the distinct roots in `H` of

```text
T^2-vT+B.
```

Conversely, any guarded choice `x,y in H` for which this quadratic has two
distinct roots in `H`, disjoint and antipodal-free with `{1,x,y}`, reconstructs
an ell-two weight-five relation.

Writing `D_0=2`, `D_1=v`, and

```text
D_m=vD_(m-1)-B D_(m-2),
```

the quadratic membership test is equivalently

```text
B^M=1, D_M(v,B)=2,
```

subject to nonzero discriminant. For the open WCL slot, `M=1024`. This is an
exact reduction to two shape variables and two recurrence equations; it does
not prove that the slot is empty.
