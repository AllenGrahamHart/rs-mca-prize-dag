# Proof - exceptional-E J-zero structural-consistency compiler

The coefficient router reconstructs

```text
D=D_*/(3600b).
```

On `E_G=X_*=0`, (FCR7) gives `Q_0=q^2/3=Q_j`. The original `Q_0`
definition is

```text
Q_0=6G_2+x(ell-2G_2)-20-8q/3-D.
```

Since `6-2x=A`, this is

```text
Q_0=A G_2+x ell-20-8q/3-D.                        (1)
```

The inherited `A!=0` saturation makes (1) equivalent to `G_2=G_j` in
(FJS1). Then `H_j+G_j=ell` and
`H_j=G_j+A(x+Y_j)` recover the original definitions of `H,Y`; defining
`V_j=G_j+xY_j+Y_j^2` recovers `V`. The original equation `D=YV` is now
exactly `Z_D^j=0`.

On `Z_D^j=0`, the original definition of `W_0` becomes

```text
W_0=(A+x)D_j+15+23q/4+q^2/8.                     (2)
```

Substitute (2), `Q_0=Q_j`, and `H_j=ell-G_j` into
`R_0=G_2H-xQ_0-W_0`. The result is precisely `Z_R^j=0`. Before imposing
`Z_D^j=0`, the original `R_0` residual minus the simplified residual in
(FJS2) is

```text
(A+x)(Y_jV_j-D_j).
```

Thus the joint use of `Z_D^j,Z_R^j` is reversible, proving (FJS3).

For the degree ledger, ignore fixed numerical units and use the explicit
uncancelled denominators. The tuples `(D_j,G_j,Y_j,V_j)` have
numerator/denominator total-degree bounds

```text
(3/1), (4/2), (4/3), (8/6),                      (3)
```

with numerator `q`-degrees at most `1,2,2,4`. Indeed a denominator for
`G_j` is `bA`, one for `Y_j` is `bA^2`, and one for `V_j` is
`b^2A^4`. Hence the denominator of `Y_jV_j` divides `b^3A^6`; clearing
`D_j-Y_jV_j` gives total degree at most 12 and `q`-degree at most 6.

A denominator `(bA)^2` clears the second line of (FJS2). The product
`G_jH_j` gives total degree at most 8 and `q`-degree at most 4; every other
term is smaller. This proves (FJS4). Cancellation can only lower the bounds.

Finally, let `Z(b,q)` have total degree at most `d` and `q`-degree at most
`m`. In the term `c_i(b)q^i`, one has `deg c_i<=d-i`. Since
`deg(5bM)=3` and `deg T=2`, every term of

```text
T^m Z(b,5bM/T)
```

has degree at most

```text
(d-i)+3i+2(m-i)=d+2m.                             (4)
```

Applying (4) to `(d,m)=(12,6)` and `(8,4)` gives (FJS6). The substitution
is reversible because (FJ04)--(FJ05) prove `T!=0` on the chart. Combining
(FJ08) with (FJS3)--(FJS6) proves (FJS7). All equations not used in this
structural reconstruction remain retained. QED.
