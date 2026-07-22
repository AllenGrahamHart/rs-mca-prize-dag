# Proof

Assume that `K` has a nonzero member `(R,y)`. The classification dependency
shows that `R` is nonzero and that the roots of each `D_i` lie in one fiber
of `B/R`, including the fiber at infinity when `y_i=0`.

First, `B` and `R` are coprime. Otherwise cancellation gives a rational map
of degree at most two. Degree one cannot have a two-point fiber. A separable
degree-two rational map has one common nonidentity deck involution, which
would exchange the roots of every `D_i`. The pair-locator Mobius dichotomy
inside the classification dependency would then put all `D_i` in a
two-dimensional span, contrary to the generic hypothesis. Separability is
automatic because `p>2^167`. Hence

```text
f=B/R:P^1 -> P^1
```

has degree three and is separable.

Form the symmetric off-diagonal coincidence polynomial

```text
C(x,y)=[B(x)R(y)-B(y)R(x)]/(x-y).                  (1)
```

Each exceptional pair `{a_i,b_i}` contributes the two distinct ordered
points `(a_i,b_i)` and `(b_i,a_i)` to `C=0` in `H^2`. Therefore

```text
#C(H x H)>=2e=2^39-2.                              (2)
```

We first suppose that `C` is absolutely irreducible. Write

```text
B=x^3+b_2x^2+b_1x+b_0,       R=r_2x^2+r_1x+r_0.
```

Here `b_0!=0` because every root of `B` belongs to `H`. Direct division in
`(1)` gives the symmetric coefficient array

```text
       y^0                    y^1                       y^2
x^0   b_1r_0-b_0r_1          b_2r_0-b_0r_2            r_0
x^1   b_2r_0-b_0r_2          r_0+b_2r_1-b_1r_2        r_1
x^2   r_0                    r_1                       r_2.       (3)
```

If one boundary row `y^j`, `j in {0,2}`, has a nonzero endpoint and one
other nonzero coefficient, independently invert `x` and `y` as needed to
move that endpoint to `(0,0)`, then clear the coordinate monomial. Inversion
preserves `H`. The resulting absolutely irreducible polynomial has bidegree
at most `(2,2)`, nonzero constant term, and nonconstant restriction at
`y=0`, exactly the coordinate hypotheses of the bound in `source.md`.

There are only three ways for this corner choice to fail. If `r_0!=0`, both
boundary rows in `(3)` already have a nonzero endpoint. Failure then forces

```text
b_1r_0-b_0r_1=b_2r_0-b_0r_2=r_1=r_2=0,
```

and `(3)` becomes `C=r_0(x^2+xy+y^2)`, contrary to absolute
irreducibility. If `r_0=0`, failure forces either `R=r_1x` or `R=r_2x^2`.
After removing the nonzero scalar, these two curves and torus
automorphisms are

```text
R=x:   C=xy(x+y+b_2)-b_0,
       (U,V)=(x^2y,x^(-1)),
       C=U^2V^3+b_2UV+U-b_0;

R=x^2: C=x^2y^2-b_1xy-b_0(x+y),
       (U,V)=(y/x,x),
       C=V[U^2V^3-b_1UV-b_0(1+U)].                 (4)
```

Both exponent maps have determinant `+/-1`, so they biject `H^2`. The
bracketed equations in `(4)` are absolutely irreducible whenever `C` is,
have bidegree `(2,3)`, nonzero constant term, and nonconstant restriction at
`V=0`. The published estimate therefore gives in every irreducible case

```text
#C(H x H)<=1440 N^(2/3),                            (5)
```

where `1440=16*2*3^2*(2+3)` is the worst transformed constant. Its size
hypotheses hold since

```text
100*6^(3/2)<N<p^(3/4)/3.
```

Exact cubing of the positive quantities gives

```text
1440 N^(2/3)<2e,                                    (6)
```

contradicting `(2)`.

It remains to treat geometric reducibility. Coprimality of `B,R` makes `C`
primitive in each variable. Over the rational function field in `x`,
equation `(1)` is the degree-two polynomial for the other two conjugates of
`x` over `Fbar(f)`. If it factors, one conjugate is rational in `x`, so
`Fbar(x)/Fbar(f)` has a nontrivial automorphism. Its degree is three; hence
the extension is cyclic and `C` is the union of the two bidegree-`(1,1)`
graphs of an order-three Mobius map `tau` and `tau^2`.

The two components cannot be exchanged by Frobenius: an `F_p`-point on an
exchanged component would lie on both components, while their two graph
components meet only at fixed points and no selected pair is diagonal.
Thus `tau` is defined over `F_p`. Each exceptional unordered pair contributes
one orientation to each graph, so each graph contains at least `e` points of
`H^2`.

For a general Mobius graph

```text
tau(x)=(ax+b)/(cx+d),       cxy+dy-ax-b=0,          (7)
```

the same published bidegree-`(1,1)` estimate applies after at most swapping
the coordinates or inverting `y`, except in exactly two cases:

```text
y=kx       or       xy=k.                           (8)
```

Indeed, if `ab!=0`, `(7)` is already admissible. If `b!=0,a=0`, swapping
works when `d!=0`, and `d=0` is the second form in `(8)`. If `b=0`,
nonsingularity gives `ad!=0`; inversion of `y` works when `c!=0`, while
`c=0` is the first form in `(8)`. Every nonspecial graph consequently has
at most

```text
32N^(2/3)<e                                            (9)
```

subgroup points, a contradiction. The map `x |-> k/x` has order two. For
`x |-> kx`, one graph point in `H^2` gives `k in H`, while order three gives
`k^3=1`; since `|H|=2^41`, this forces `k=1` and the identity map. Neither
special form can be the nonidentity order-three deck map.

Both irreducibility cases contradict the assumed nonzero member of `K`.
Thus `K=0`, and the exact defect identity in the classification dependency
gives `dim(VV)=3e+1`. QED.
