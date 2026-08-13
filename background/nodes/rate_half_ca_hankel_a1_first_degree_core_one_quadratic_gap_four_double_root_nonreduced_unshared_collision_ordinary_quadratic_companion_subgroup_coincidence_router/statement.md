# `A=1` collision ordinary-quadratic subgroup-coincidence router

- **status:** PROVED
- **closure:** every dense ordinary-quadratic coincidence component is
  coordinate-corner exceptional
- **consumer:** `rate_half_band_crossing_location`

Retain a bidegree-`(2,3)` ordinary companion from collision shape B or D.
To avoid the two uses of `p` in the surrounding literature, write `P` for
the characteristic of the official prime field. The exact row is

```text
N=2^41,                  H=mu_N subset F_P^*,
e=(2^39+1)/3,            |Gamma|=3e=2^39+1,
R=|U_0|=(9e-7)/2,        U_0,Gamma subset H,
P>2^167.                                             (QCR1)
```

Write the companion as

```text
Q(t,X)=a(X)t^2+b(X)t+c(X),       deg a,b,c<=3.      (QCR2)
```

It is absolutely irreducible. Define the divided coefficient minors

```text
A(X,Y)=[a(X)b(Y)-a(Y)b(X)]/(X-Y),
B(X,Y)=[a(X)c(Y)-a(Y)c(X)]/(X-Y),
C(X,Y)=[b(X)c(Y)-b(Y)c(X)]/(X-Y),
K_Q(X,Y)=B(X,Y)^2-A(X,Y)C(X,Y).                    (QCR3)
```

They satisfy

```text
bideg A,B,C<=(2,2),       bideg K_Q<=(4,4),
Res_t(Q(t,X),Q(t,Y))=(X-Y)^2 K_Q(X,Y),             (QCR4)
```

up to the harmless sign convention for the resultant, and `K_Q` is not
zero.

Call an absolutely irreducible component **VM-admissible** if, after
possibly swapping `X,Y` and independently replacing either coordinate by
its inverse and clearing a coordinate monomial, its defining polynomial
`P_0` has

```text
P_0(0,0)!=0,       deg P_0(X,0)>=1.                (QCR5)
```

Then every geometrically dense off-diagonal coincidence component of
`K_Q=0` is not VM-admissible. More precisely:

1. if the degree-three projection `Q=0 -> P^1_t` has geometric monodromy
   `S_3`, its unique reduced off-diagonal component has bidegree at most
   `(4,4)` and is coordinate-corner exceptional;
2. if its monodromy is `C_3`, each distinct orientation-image component
   has bidegree at most `(2,2)`, is defined over `F_P`, and is
   coordinate-corner exceptional.

## Scope

This router does not yet classify or exclude the coordinate-corner
exceptional components, so it does not exclude shapes B or D. It says
nothing about the bidegree-`(4,6)` companion in shape C. It uses the
prime-field collapse and makes no extension-field claim.
