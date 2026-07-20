# DSP8 unit-product trace normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependency:** `f3_h3_dsp8_primitive_shift_pair_adapter`

Take one decorated primitive cubic shift-pair record from the adapter. Write
its ordered cubic root sets as

```text
Z(A)={R,U,V},       Z(B)={S,X,Y},                  (UTN1)
```

where `R,S` are the distinguished roots. Thus

```text
RUV=SXY=RS,       R+U+V=S+X+Y.                    (UTN2)
```

Because `H` has dyadic order, cubing is a bijection on `H`. Let `q` be the
unique element with `q^3=RS`, and normalize

```text
(r,u,v,s,x,y)=q^(-1)(R,U,V,S,X,Y).                 (UTN3)
```

Then the decoration fixes the scale exactly:

```text
q=rs,       ruv=sxy=1,
sigma:=r+u+v=s+x+y.                                (UTN4)
```

Conversely, any two reduced, disjoint, product-one triples
`{r,u,v},{s,x,y}` in `H` with common trace `sigma`, decorated by `r,s`,
recover one decorated primitive shift pair after scaling all six roots by
the forced value `q=rs`. There is no additional `H`-scale choice.

The original DSP8 target is determined by the three coefficient parameters:

```text
t=(1-rs*u)(1-s/u)
 =(1-rs*x)(1-r/x)
 =1+rs(r+s-sigma).                                  (UTN5)
```

Equivalently, the two residual root pairs are the split quadratics

```text
F_(r,sigma)(T)=T^2-(sigma-r)T+r^(-1),
F_(s,sigma)(T)=T^2-(sigma-s)T+s^(-1).               (UTN6)
```

Thus `K_25^c` exactly counts the admissible reduced records

```text
(r,s,sigma,z,w),                                    (UTN7)
```

where the two quadratics in `(UTN6)` split over `H`, their roots and
decorations have six distinct signed coordinates after the forced scaling,
the original retained-target and class predicates hold, and

```text
1-w=[1+rs(r+s-sigma)](1-z).                         (UTN8)
```

This removes the ambient scale from the primitive-SP object. It supplies no
bound for `(UTN7)--(UTN8)`. In particular, the generic degree-three SP
all-pairs ceiling, which first chooses two disjoint triples and is of order
`n^6`, does not imply the required `O(n^2)` weighted correlation.
