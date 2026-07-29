# Proof - L1 Mersenne HNF order-one color-degree barrier

Write

```text
E(W)=sum_(j=0)^d a_j W^j,       a_d!=0.              (1)
```

For one reduced root `x`, put `epsilon=E(x)=x^(p+1)`. On every official row
`epsilon in mu_m` and `p=-1 mod m`, so

```text
epsilon^p=epsilon^(-1),       x^p=epsilon/x.         (2)
```

In the affine `(W,X)` plane define

```text
f(W,X)=E(W)-X,
g(W,X)=sum_(j=0)^d a_j^p X^(j+1) W^(d-j)-W^d.       (3)
```

Taking the `p`th power of `E(x)=epsilon`, substituting (2), and multiplying
by `epsilon*x^d` gives

```text
f(x,epsilon)=g(x,epsilon)=0.                         (4)
```

The total degrees of `f` and `g` are `d` and `d+1`. They have no common
component. Indeed, `f` is irreducible because it is linear in `X`; if it
divided `g`, then `g(W,E(W))` would vanish identically. For `d>=2`, the
unique top-degree term of this substitution comes from `j=d` and has

```text
degree d(d+1),       coefficient a_d^p a_d^(d+1)!=0.
```

For `d=1`, an identity first evaluated at `W=0` would force `a_0=0`, after
which `g(W,E(W))=-W+a_1^p a_1^2 W^2` is still nonzero.

Bézout therefore bounds the number of projective intersections of `f=0`
and `g=0`, counted with multiplicity, by `d(d+1)`. The `H` reduced roots are
distinct, and (4) gives `H` distinct affine intersection points even when
some colors repeat. This proves (CDB1).

At `h=7`, `H=6`; degree one is impossible because `2<6`. At `h=15`,
`H=14`; degrees one, two, and three are impossible because
`2,6,12<14`. This is (CDB2). QED.
