# Proof

An affine change of variable and independent nonzero rescaling of the two
forms reduce the membership conditions to

```text
x^m=alpha,       (x-1)^m=beta                       (1)
```

for fixed nonzero `alpha,beta`. The in-house Stepanov construction uses

```text
Psi(X)=Phi(X,X^m,(X-1)^m),
Phi=sum lambda_(a,b,c)X^aY^bZ^c,
0<=a<A,       0<=b,c<B.                            (2)
```

It gives a nonzero `Psi` vanishing to order at least `D` at every solution
of `(1)` whenever

```text
D(A+D)<AB^2,       AB<=m,       A+mB<p.             (3)
```

Since `deg Psi<A+2mB`, the number of solutions is then below

```text
(A+2mB)/D.                                          (4)
```

Choose `B,A,D` deterministically by

```text
B=ceil((2m)^(1/3)),
A=floor(m/B),
D=max{d>=1:d(A+d)<AB^2}.                            (5)
```

These integers are positive in the stated range. The first inequality in
`(3)` is strict by the definition of `D`, and

```text
A B<=m.                                              (6)
```

The remaining field-degree condition and the sharpened degree comparison are
finite exact arithmetic at the 58 pairs `(s,m/n)` in the statement. Integer
cubing gives, with positive slack in every case,

```text
A+mB<n^2+1<=p,
4096(A+2mB)^3<132651D^3m^2.                        (7)
```

The last inequality is exactly

```text
(A+2mB)/D <(51/16)m^(2/3).
```

Combining `(3)--(7)` proves `(CPS1)`. The verifier recomputes every integer
from the displayed integer rule; no floating-point approximation is consumed.
QED.
