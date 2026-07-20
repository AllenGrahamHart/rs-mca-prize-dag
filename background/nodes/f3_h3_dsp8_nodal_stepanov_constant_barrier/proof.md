# Proof

Normalize the positive parameters by

```text
a=A/m^(2/3),       b=B/m^(1/3),
d=D/m^(2/3),       y=d/b=D/(B m^(1/3)).              (1)
```

The second inequality in `(NSB1)` gives `ab<=1`. The first becomes

```text
d(a+d)<ab^2.
```

Substituting `d=by` and dividing by `b` gives

```text
y(a+by)<ab,
by^2<a(b-y).                                         (2)
```

The left side is positive, so `b-y>0`. Since `a<=1/b`, equation `(2)`
implies

```text
b^2y^2-b+y<0.                                       (3)
```

For the quadratic in `b` in `(3)` to take a negative value, its discriminant
must be positive. Therefore

```text
1-4y^3>0,       y<2^(-2/3).                         (4)
```

It follows that

```text
(A+2mB)/D
 >2mB/D
 =2m^(2/3)/y
 >2^(5/3)m^(2/3),
```

which proves `(NSB2)`. Cubing `51/16` gives `(NSB3)` because
`51^3=132651>131072=32*16^3`.

For the nodal application, let `C_1` and `C_3` be constants certified by this
ansatz for subgroup orders `n` and `3n`. Equation `(NSB2)` gives

```text
C_1>2^(5/3),       C_3>2^(5/3).
```

The class-blind leading coefficient in the existing nodal product envelope is

```text
17 C_1 C_3^2 3^(4/3)
 >17*32*3^(4/3).
```

Since `3^(1/3)>4/3`, one has `3^(4/3)>4`, and hence this coefficient is
strictly greater than `17*32*4=2176`. Finally

```text
2176=87040/40>76599/40.
```

This proves `(NSB4)`. The argument concerns only the certificate furnished by
the displayed Stepanov ansatz; it makes no claim about the true correlation.
QED.
