# Proof

The preserving source lift gives

```text
star(bx)=tau(star(x)).                              (1)
```

The coordinate source-facet theorem proves `tau(I)=I` and `tau(J)=J`.
Hence `(1)` carries an `I-J` star to another `I-J` star. The colored
divisor consists exactly of the four points carrying those stars, so it is
`b`-invariant. All four points lie in free `L^c` fibers. Their quotient is
therefore a reduced degree-two divisor, proving `(KBCQ-1)` and the two
complete right-vertex edge pairs.

The fixed-point-free action of `tau(T)=-T` on each six-set pairs its labels
as `+/-t`. Thus its sextic is even and has the form `P_S(T)=p_S(T^2)` with
`deg p_S=3`.

For the positive source form,

```text
H(T,X)=A_2(W)T^2+A_0(W)+XT B_1(W).
```

At a paired source root `+/-t`, direct multiplication gives

```text
H(t,X)H(-t,X)
=(A_2(W)t^2+A_0(W))^2-Wt^2B_1(W)^2
=Phi_+(t^2,W).                                     (2)
```

For the negative form,

```text
H(T,X)=T A_1(W)+X(B_2(W)T^2+B_0(W)),
```

and similarly

```text
H(t,X)H(-t,X)
=W(B_2(W)t^2+B_0(W))^2-t^2A_1(W)^2
=Phi_-(t^2,W).                                     (3)
```

Multiplying `(2)` or `(3)` over the three `tau`-pairs in `S` is both the
product formula for `Res_T(P_S,H)` and the product formula for
`Res_Y(p_S,Phi_epsilon)`. This proves `(KBCQ-2)--(KBCQ-3)`.

In the quotient coordinate, the pullback forms in the universal compiler
are `D_K(X)=K_5(W)`, `D_R(X)=R_7(W)`, and `C_H(X)=c(W)`. Substitution in
the two universal partial-resultant identities proves `(KBCQ-4)`. Finally
`K` is a five-subset of the six-set `I`, so deleting its unique complement
`xi` gives the two printed factorizations of `K_5,R_7`. QED.
