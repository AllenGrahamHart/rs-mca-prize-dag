# Proof

Put `a=3d` and `a_0=3d-1`.

## Safe side

Apply the exact-integer Johnson theorem. For `B=1`, `ell=B+1=2` and

```text
ell*a=6d=(4d)*1+2d.
```

The balanced pair-intersection lower bound is `2d`, while two distinct
degree-`<2d` polynomials can agree in at most `2d-1` points. The Johnson
inequality is strict, so `L_1(3d)<=1`.

For `B=2`, `ell=3` and

```text
ell*a=9d=(4d)*2+d.
```

The balanced lower bound is

```text
4d binom(2,2)+d*2=6d,
```

whereas the three pairwise intersections total at most
`binom(3,2)(2d-1)=6d-3`. Hence `L_1(3d)<=2`.

## Unsafe side for budget one

Choose subsets `S_0,S_1` of `D` such that

```text
|S_0|=|S_1|=3d-1,       S_0 union S_1=D,
|I|=|S_0 intersect S_1|=2d-2.
```

Choose a set `Z subset D` of size `2d-1` containing `I`, and let

```text
c_0(X)=0,       c_1(X)=product_(z in Z)(X-z).
```

These are distinct code polynomials of degree less than `k=2d`. Define a
received word `u` to equal `c_0` on `S_0` and `c_1` on `S_1`. This is
well-defined on the overlap because `I subset Z`. Both codewords agree with
`u` on at least `3d-1` coordinates, proving `L_1(a_0)>=2`.

## Unsafe side for budget two

Write `D=gamma H`, choose a generator `zeta` of `H`, and put

```text
i=zeta^d,       y=(X/gamma)^d.
```

Then `i^2=-1`, and the four fibers

```text
D_s={x in D:y(x)=s},       s in {1,-1,i,-i},
```

all have size `d`. Fix `x_0 in D_(-i)` and define

```text
G(X)=product_(x in D_(-i)\{x_0})(X-x),
c_0=0,
c_1=G(y-1),
c_2=i G(y+1).
```

Each polynomial has degree at most `(d-1)+d=2d-1<k`. They are distinct.
Moreover

```text
c_1-c_2
 =G((1-i)y-(1+i))
 =(1-i)G(y-i),                                      (1)
```

because `(1+i)/(1-i)=i`.

Define `u` fiberwise:

```text
u=0          on D_1 union D_(-1) union D_(-i),
u=c_1=c_2   on D_i.
```

The equalities used here are exact: `c_0=c_1` on `D_1`, `c_0=c_2` on
`D_(-1)`, `c_1=c_2` on `D_i` by `(1)`, and all three vanish at the `d-1`
roots of `G`. Therefore

```text
agr(c_0,u)>=3d,
agr(c_1,u)>=d+d+(d-1)=3d-1,
agr(c_2,u)>=d+d+(d-1)=3d-1.
```

Thus `L_1(a_0)>=3`. Combining both unsafe constructions with the safe side
proves `(LB12)`. Substituting the official integer budget proves `(LB13)`.
QED.
