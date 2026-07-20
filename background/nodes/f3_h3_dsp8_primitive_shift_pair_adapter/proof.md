# Proof

The split-pencil router gives `r=xy`, `s=uv`, and says that distinct generic
representations in one target fiber have `r!=s`: equality of `r,s` would make
their root sums equal as well, hence make the two monic quadratics and the two
unordered representations equal.

Expand `(SPA1)`. In descending coefficient order,

```text
A=[1, -(1+r+s-t), s+r(1+s-t), -rs],
B=[1, -(1+r+s-t), r+s(1+r-t), -rs].                (1)
```

Their difference is

```text
[0,0,t(s-r),0],                                     (2)
```

which proves `(SPA2)`. The signed support of `E` is `+r-x-y`, and that of
`F` is `+s-u-v`. Genericity and disjointness say that the six corresponding
half-basis coordinates are distinct. Rearranging their equality gives

```text
r+u+v=s+x+y,                                        (3)
```

which is the equal-sum reading of the cubic shift pair. Since the difference
in `(2)` is nonzero and linear, its degree is exactly

```text
3-1-1=1;
```

the pair has depth one.

For a split locator of degree `e`, every coefficient quotient scale divides
both the ambient cyclic order and `e`. Here `e=3` and the official order is a
power of two. Hence every common scale divides `gcd(n,3)=1`, proving
coefficient primitivity. Notice that this is stronger than merely failing to
recognize a quotient pattern: no nontrivial coefficient-scale quotient exists.

For the converse, let `alpha` be the common coefficient of `X^2` in `A,B`.
The constant condition in `(SPA4)` and the distinguished roots give the monic
divisions

```text
A/(X-r)=X^2+(alpha+r)X+s,
B/(X-s)=X^2+(alpha+s)X+r.                            (4)
```

Subtracting the two products in `(4)` shows

```text
lambda=(s-r)(1+alpha+r+s).                          (5)
```

Thus `(SPA5)` gives `t=1+alpha+r+s`, and `(4)` becomes

```text
A/(X-r)=X^2-(1+s-t)X+s=Q_(t,s),
B/(X-s)=X^2-(1+r-t)X+r=Q_(t,r).                     (6)
```

The residual roots therefore give two representations of the same shifted
product target. Distinct signed coordinates make both representations generic
and their supports disjoint. The retained-target and quotient-line predicates
then recover exactly one ordered DSP8 edge/quotient record. Equations
`(SPA1)` and `(6)` are inverse constructions.

One unordered disjoint edge has two endpoint orders. For each endpoint order,
the decorated cubics forget only the two root orders inside each residual
quadratic, giving four raw presentations. The quotient representation is
already ordered. Consequently

```text
K_25^c=2D_6,25^c,
J_25^c=4K_25^c=8D_6,25^c,
```

which proves `(SPA6)`. Substitute `J=4K` into DSP8 and divide by four to get
`(SPA7)`. QED.
