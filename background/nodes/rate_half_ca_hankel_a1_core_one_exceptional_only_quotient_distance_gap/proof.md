# Proof

The `r-1` columns at the roots of `A` are independent. The full moment space
has dimension `2r+1`, so adjoining any `r+2` residual-domain columns outside
`R_A` gives a Vandermonde basis. Consequently

```text
3<=h<=r+2.                                             (1)
```

Choose a minimal quotient support `T` of size `h`. There is a source
representation

```text
h_1=sum_(a in R_A)alpha_a c(a)+sum_(t in T)omega_t c(t), (2)
```

and every `omega_t` is nonzero by minimality. The exceptional source has the
unique representation

```text
h_0=sum_(a in R_A)beta_a c(a),       beta_a!=0.       (3)
```

Uniqueness in `(2)--(3)` follows because their supports have at most
`(r-1)+(r+2)=2r+1` points.

At an ordinary supported slope `z`, let

```text
j_z=#{a in R_A:beta_a+z alpha_a=0}.                   (4)
```

The source representation of `h_0+zh_1` then has support

```text
F_z subset S,       |F_z|=r+h-1-j_z.                 (5)
```

Every point of `T` remains in `F_z`, since ordinary `z` is nonzero. The
ordinary Hankel rank is `r`, so the same moment vector has a unique clean
`r`-point representation on its locator `G_z`, with every coefficient
nonzero.

If the two representations coincide, their support sizes in `(5)` give

```text
j_z=h-1,       G_z=F_z subset S.                     (6)
```

Each affine coefficient in `(4)` can vanish at at most one slope because
`beta_a!=0`. Hence cancellation sets for fibers satisfying `(6)` are
disjoint, proving `(QDG4)`.

Otherwise subtraction gives a nonzero relation on `F_z union G_z`. Any at
most `2r+1` moment columns are Vandermonde-independent, so

```text
|F_z union G_z|>=2r+2.                               (7)
```

Equations `(5)--(7)` imply

```text
|F_z intersect G_z|<=h-3-j_z.                       (8)
```

The points of `S` omitted from `F_z` are exactly the `j_z` cancelled roots
of `A`. Therefore

```text
|G_z intersect S|<=|G_z intersect F_z|+j_z<=h-3.    (9)
```

This proves the asserted intersection cap for every noninternal fiber.

It remains to compare incidences. On the exceptional-only face the unique
root omission gives the exact total row deficit

```text
sum_(x in D_res)(e-d_x)=e,                            (10)
```

where `d_x` is the number of supported parameter roots of `Q(z;x)`. Since

```text
|S|=(r-1)+h=2e+h,
```

the supported incidences on `S` are at least `e(2e+h)-e`. The exceptional
fiber contributes its `2e` roots `R_A`, so the `4e` ordinary locators
contribute at least

```text
I_S>=2e^2+eh-3e.                                     (11)
```

Put `J=floor(2e/(h-1))`. By `(QDG4)`, at most `J` ordinary fibers are
internal. Equations `(6)` and `(9)` give the opposing upper bound

```text
I_S<=Jr+(4e-J)(h-3)
   =4e(h-3)+J(2e+4-h).                               (12)
```

This proves the necessary inequality `(QDG5)`.

Finally write `e=3m`, which is valid because
`2^38-1=3*174763*524287`. For `4<=h<=2e/3+1`, replace `J` in `(12)` by the
larger real value `2e/(h-1)`. After subtracting `(12)` from `(11)` and
multiplying by `(h-1)/e`, it is enough to prove

```text
f(h)=-3h^2+(2e+14)h-6e-17>0.                         (13)
```

This quadratic is concave. At the two endpoints,

```text
f(4)=2e-9>0,
f(2e/3+1)=4e/3-6>0.                                  (14)
```

Thus `(13)` holds throughout that interval. At the sole remaining value
`h=2e/3+2`, one has `J=2`, and direct subtraction in `(11)--(12)` gives

```text
I_S^(lower)-I_S^(upper)=e/3-4>0.                     (15)
```

Hence `(QDG5)` fails for every value in `(QDG3)`. Together with the original
distance-three alternative, this proves `(QDG2)`. QED.
