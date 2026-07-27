# E1 N=256 square-mass-16 high-variance exclusion

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let `zeta` be a primitive `256`-th root and let

```text
alpha=F(zeta)=sum_(i=0)^127 c_i zeta^i
```

have folded profile `(a,b,c)=(3,4,0)` in the first surviving `N=256,s=5`
band. Then

```text
sum_i c_i^2=16,       sum_i |c_i|=10.
```

For the 128 odd conjugates put `y_u=|F(zeta^u)|^2` and define the exact
negacyclic autocorrelation variance

```text
V=(1/128) sum_(u odd) (y_u-16)^2.
```

Then `V` is an even nonnegative integer. The following cases cannot collide
at a pair-feasible row prime:

```text
V=0,       or       V>=136.
```

Indeed, `V=0` gives `|Norm(alpha)|=16^64=2^256`, which has no odd prime
divisor. For `V>=136`, the exact pointwise logarithmic majorant

```text
log x <= log 16+(x-16)/16-(x-16)^2/2070
                    for 0<x<=100
```

gives `|Norm(alpha)|<2^250`. Thus an unresolved collision in profile
`(3,4,0)` must have

```text
0<V<=134,       V even.
```

This does not exclude that low-variance residual, profile `(4,2,0)`, or any
higher swap-distance band.
