# Proof

The rational-pair-pencil branch says that all

```text
T_p=(1,a_p,b_p)
```

have rank at most two over `F(X)`. Choose distinct types `p_0,p_1` and put

```text
A=a_1-a_0,       B=b_1-b_0.
```

They are not both zero. Write

```text
C=gcd(A,B),       A=CU,       B=CV,
```

with `C` monic and `gcd(U,V)=1`. This convention also covers a zero
component: the other primitive component is then a nonzero constant.

For any type `p`, put `A_p=a_p-a_0` and `B_p=b_p-b_0`. The determinant of
`T_(p_0),T_(p_1),T_p` vanishes, so

```text
A B_p-B A_p=0,
U B_p-V A_p=0.                                      (1)
```

Since `F[X]` is a PID and `U,V` are coprime, `(1)` gives a polynomial
`R_p` with

```text
A_p=U R_p,       B_p=V R_p.                         (2)
```

For example, if both primitive components are nonzero, `U|A_p` and
`V|B_p`; the one-zero case follows because the other component is a unit.
This proves `(NF1)`, with `R_(p_0)=0` and `R_(p_1)=C`. Since `(U,V)` is not
the zero pair, `(2)` is injective in `R_p`; distinct pair types therefore
give distinct scalar polynomials.

All pair-component differences lie in the four-dimensional correction
space supplied by the heavy-ruling reduction. Multiplication by the fixed
pair `(U,V)` is an injective `F`-linear map. Hence

```text
dim_F span{R_p}<=4.                                  (3)
```

Every `a_p,b_p` has degree below `K`. If
`d=max(deg U,deg V)`, ignoring a zero component, `(2)` gives

```text
deg R_p+d<=K-1                                      (4)
```

for every nonzero `R_p`.

It remains to translate the pair cores. Bezout gives polynomials `S,T` with
`SU+TV=1`, so `U,V` have no common root. At a domain point `x`, equations
`(2)` imply

```text
(a_p-a_q,b_p-b_q)(x)
  =(R_p-R_q)(x)(U,V)(x).
```

Therefore the two pair codewords agree at `x` exactly when
`(R_p-R_q)(x)=0`. A point of both complete pair cores is a point where the
received pair agrees with both codeword pairs, and hence

```text
H_p intersection H_q subset Z_D(R_p-R_q).          (5)
```

Every quotient core has size `s=m-2=1116046`. Inclusion--exclusion inside
the `n=2097152` coordinate domain gives

```text
|H_p intersection H_q|>=2s-n=134940.                (6)
```

By `(5)`, every listed nonzero scalar difference therefore has at least
134940 distinct domain roots. Combining this with `(4)` yields

```text
134940<=deg(R_p-R_q)<=K-1-d,
d<=1048575-134940=913635.
```

All conclusions follow. QED.
