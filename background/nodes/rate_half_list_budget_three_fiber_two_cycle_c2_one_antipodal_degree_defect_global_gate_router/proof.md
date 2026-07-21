# Proof

Put `r=2H-3`, let `m=H-3-e`, and retain

```text
Theta=HBC+z(BC'-B'C),
J=Q_-C^2Theta+Q_+C(-z)^2Theta(-z),
Q_+=Q_-(-z).                                          (1)
```

The polynomial `B` has exact degree `r`. If `e=0`, the leading term in
`Theta` cancels and the support compiler gives

```text
deg J<=5H-11=d_e.                                     (2)
```

Suppose `e>0`. If `b,c` are the leading coefficients of `B,C`, the leading
coefficient of `Theta` is

```text
(H+m-r)bc=-e bc.                                      (3)
```

Here `1<=e<=H-3<p`, so `(3)` is nonzero and

```text
deg Theta=r+m=3H-6-e.                                 (4)
```

Write `A=Q_-C^2Theta`. Its exact degree is

```text
delta=2+2m+(r+m)=5H-10-3e,                            (5)
```

and `J=A(z)+A(-z)`. Since `H` is odd, `delta` is even exactly when `e` is
odd. For odd `e`, the two leading terms add and `deg J=delta`; for even `e`
they cancel and `deg J<=delta-1`. This proves `deg J<=d_e`, including `(2)`.

The first nonzero barycentric syndrome makes `J` nonzero. Its subgroup-root
set away from `+/-1` is stable under negation and has no fixed point, so
`r_J` is even. The number `d_e` is also even, and the pointwise support
compiler gives

```text
|supp u|=N-2-r_J.
```

Writing `eta=d_e-r_J` and using `N=8H-8` proves `(DGR2)--(DGR4)`.

Now assume `e=0`, so `deg C=H-3`. The canonical identity is

```text
Q=B^4+V^2(alpha B^2+beta BV+gamma V^2),       V=z^HC.
```

Exactly as in the differential calculation, define

```text
T=NEB-z(E'B+4EB'),       P=TB^3-N.
```

Using `EQ=1-z^N` gives `P=zS'-NS` with
`S=EV^2(alpha B^2+beta BV+gamma V^2)`, hence `V|P` and
`gcd(V,TB)=1`. The primary double gap gives `z^(2H)|P`. Substitution of the
proved secondary differential identity turns `P/8` into
`T_0B^3-(H-1)`, so

```text
C|P_0,       gcd(C,T_0B)=1.                           (6)
```

Reducing `(6)` modulo `C` and applying resultant multiplicativity yields

```text
Res(C_sharp,T_0)Res(C_sharp,B)^3=(H-1)^(deg C).       (7)
```

Here `deg C=H-3=2^37-2` is divisible by three. Both resultants are nonzero,
so `(7)` proves the cube assertion in `(DGR6)`. No support-size hypothesis
has entered this calculation.

For the infinity gate, each canonical cell factor has degree
`r=2H-3` and

```text
G_i=B+w_i z^HC=product_(x in A_i)(1-xz).
```

Its leading coefficient is `ell_i=b+cw_i`. Since `r` is odd and every
`x` lies in `mu_N`, each `ell_i` lies in `mu_N`. They are distinct because
`c!=0` and the `w_i` are distinct. Expanding their polynomial gives
`O_inf`; multiplying them and comparing the leading coefficient of
`Q=(1-z^N)/E` gives `product_i ell_i=P_src^(-1)`. Thus `(DGR7)` holds.
Affine scaling of the four roots gives

```text
O_inf'(ell_i)=c^3Phi'(w_i).                            (8)
```

The global collision router therefore transfers its unique derivative
collision to the infinity quartet.

On the selected-antipodal collision shard, the router gives
`s^2=4alpha/3` and `q^2=-alpha/6`. Hence `a=s/(2q)` satisfies `a^2=-2`, and
the centered outer roots are

```text
q(a+3), q(a-3), q(-a+1), q(-a-1).
```

Applying `w -> b+cw`, dividing by `tau=ell_4`, and solving
`y=ell_3/ell_4` gives `(DGR8)--(DGR9)`. The fourth-power image of `mu_N` is
`mu_(N/4)`, which proves the last test in `(DGR9)`.

Finally the two affine forms have determinant three. The in-house Stepanov
construction with

```text
A_0=D_0=79896510,       B_0=12902
```

has sparse degree below the uniform official characteristic lower bound.
Its exact degree quotient is

```text
(A_0+2NB_0)/D_0
 =355106851+51038404/79896510.
```

The same nonvanishing proof works over prime and quadratic fields, proving
`(DGR10)`. QED.
