# KoalaBear m2 r4 coordinate coefficient normal form

- **status:** PROVED
- **scope:** actual `(m,r,delta)=(2,4,2)` component with stabilizer
  `S=<tau x 1>`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` and
  `rate_half_kb_m2_r4_source_row_interpolation_compiler`
- **consumer:** `rate_half_band_closure`

Over the geometric closure, choose coordinates

```text
tau(T)=-T,       b(X)=-X,       W=psi(X)=X^2.
```

The preserving source lift makes the irreducible bidegree-`(2,4)` source
equation an eigenform

```text
H(-T,-X)=epsilon H(T,X),       epsilon in {+1,-1}. (KBCO-1)
```

Writing `H=U(T,W)+XV(T,W)`, the two exact normal forms are:

```text
epsilon=+1:
H=A_2(W)T^2+A_0(W)+XT B_1(W),
deg A_2,deg A_0<=2,       deg B_1<=1;               (KBCO-2)

epsilon=-1:
H=T A_1(W)+X(B_2(W)T^2+B_0(W)),
deg A_1<=2,       deg B_2,deg B_0<=1.               (KBCO-3)
```

The coefficient dimensions are eight and seven. The deck conjugate is
distinct exactly only if the odd-`X` part is nonzero: `B_1!=0` in
`(KBCO-2)`, or `(B_2,B_0)!=(0,0)` in `(KBCO-3)`.

After projective rescaling, the endpoint equation is

```text
G(T,W)=U(T,W)^2-WV(T,W)^2,       G(-T,W)=G(T,W).    (KBCO-4)
```

Thus a coordinate source-row packet which passes the `45 x 12` source
interpolation gate is deleted if its unique interpolant lies in neither
normal form, has zero odd part, or produces an endpoint biform which is not
even in `T`.

This theorem does not prove universal failure of either normal form. It
does not apply to the transposed or diagonal orientation and proves no
order-two type, trivial type, owner, payment, row, or Prize result.

## Falsifier

An actual coordinate component violating `(KBCO-1)--(KBCO-4)`, a third
eigenspace dimension, or an actual deck-distinct source equation with zero
odd-`X` part.
