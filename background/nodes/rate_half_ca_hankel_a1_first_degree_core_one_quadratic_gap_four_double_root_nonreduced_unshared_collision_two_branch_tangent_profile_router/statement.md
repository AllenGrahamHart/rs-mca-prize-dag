# `A=1` nonreduced collision two-branch tangent-profile router

- **status:** PROVED
- **closure:** companion shapes B and D cannot have collision profile `[4]`
- **consumer:** `rate_half_band_crossing_location`

Retain shape B or D from the factorwise Bezout classification. Exactly two
factors vanish at the collision with heavy-fiber order one. Over a common
splitting field, let their local germs be `f_1,f_2`, put `z=t-tau` and
`y=X-x_*`, and write

```text
f_i(z,y)=a_i z+v_i y+terms of total order at least two,
a_i!=0.                                             (TBP1)
```

The product of the remaining factor germs and the global scalar is a unit
`u(z,y)`, so

```text
G(tau+z,x_*+y)=u(z,y)f_1(z,y)f_2(z,y),
u_0:=u(0,0)!=0.                                    (TBP2)
```

Then

```text
G_X(tau,x_*)=0,
[z]G_X(t,x_*)=u_0(a_1v_2+a_2v_1).                 (TBP3)
```

In particular, define the factor-scaling-invariant tangent sum

```text
Theta=v_1/a_1+v_2/a_2.                            (TBP4)
```

The Pade/split-jet dictionary routes the two companion shapes exactly as

```text
Theta!=0:       collision profile [1,3];
Theta=0:        collision profile [2,2].           (TBP5)
```

Thus shapes B and D exclude profile `[4]`. Shape B is the large factor plus
one `(2,3)` companion; shape D is the large factor plus two `(2,3)`
companions. The formula applies to the two factors with correction order one
in either case.

## Scope

The theorem does not exclude shapes B or D and does not prove that `Theta`
is nonzero. Shapes A and C have only one collision factor, of correction
order two, so the product-rule vanishing in `(TBP3)` does not apply to them.
No profile is removed from A or C here.
