# Proof

## Classification of the zero locus

Suppose `(1-x)(1-y)(1-z)=1-w` for nonidentity `n`th roots. If
`x=zeta_n^a`, then the valuation at the unique prime above two is

```text
v_pi(1-zeta_n^a)=2^v_2(a).                         (1)
```

This follows down the dyadic cyclotomic tower, and odd dilation is Galois.
The equality of valuations says that a sum of three powers of two is one
power of two. After permuting the inputs, its only solution is

```text
v_2(a)=v_2(b)=r,       v_2(c)=r+1,
v_2(d)=r+2.                                      (2)
```

Put `eta=zeta_n^(2^r)`. Then `eta` has order at least eight and, for odd
integers `A,B,C,D`, write

```text
x=eta^A,       y=eta^B,       z=eta^(2C),
w=eta^(4D).                                         (3)
```

The quotient `(1-w)/(1-z)` lies in `Q(eta^2)`, so `(1-x)(1-y)` is fixed by
the involution `eta -> -eta` of `Q(eta)/Q(eta^2)`. Therefore

```text
(1+x)(1+y)=(1-x)(1-y),
```

which gives `y=-x`. The original equality becomes

```text
(1-x^2)(1-z)=1-w.                                  (4)
```

Now apply the involution `eta^2 -> -eta^2` over `Q(eta^4)`. The right side
of `(4)` is fixed, so

```text
(1+x^2)(1+z)=(1-x^2)(1-z),
```

and hence `z=-x^2`. Equation `(4)` then gives `w=x^4`. Conversely,

```text
(1-q)(1+q)(1+q^2)=1-q^4,                           (5)
```

so these are all the solutions. The restrictions that all shifted factors
are nonzero say exactly that `q` has order at least eight.

There are `n-4` such parameters. The parameters `q` and `-q` give the same
unordered input triple, and no other pair does; the two lowest-valuation
roots recover `{q,-q}`. At order at least eight, `q^4` differs from each of
the three input roots, so every distinguished quotient is nonidentity. Each
unordered triple has three choices for that denominator, proving `(NZC4)`.

## Selecting a nonzero quotient anchor

Fix a finite target `t!=1` and a product lift `E` reducing to it. Suppose two
distinct quotient lifts `Q_0,Q_1` both had zero coupling. In characteristic
zero this would give

```text
D_(Q_0)/C_(Q_0)=beta_E=D_(Q_1)/C_(Q_1).            (6)
```

The middle value is not one: otherwise its reduction would be `t=1`. The
proved quotient consequence of shifted-product Sidonicity says that a
nonidentity quotient has at most one ordered representation. Equation `(6)`
would force `Q_0=Q_1`, a contradiction. Thus at most one coupling vanishes,
which proves `(NZC5)`.

If `P(t)>=19`, the proved joint-ideal router supplies a rooted star
`(E;F,G)` satisfying `(ISR2)`. Every normalized product difference in
`(NZC1)` lies in the degree-one row-prime ideal

```text
mathfrak p=(p,zeta_n-g).
```

For every finite quotient representation of the same target,
`beta_E C_Q-D_Q` also vanishes modulo `mathfrak p`. Since `pi` is a unit
modulo this odd prime ideal, every integral `lambda_(E,Q)` lies in
`mathfrak p`. Therefore `K_t^NZ subset mathfrak p`, and when `R(t)>=2` the
batch has at least one nonzero coupling generator. Norm reverses ideal
inclusion, giving `p | N(K_t^NZ)`.

Each principal generator ideal is contained in `K_t^NZ`, so its absolute
norm is divisible by `N(K_t^NZ)`. The two product generators retain the
proved bound `6^(n/4)/4`; this proves `(NZC7)`.

Finally, if `Y_18>0`, some `t!=1` has `P(t)>=19` and `R(t)>=2`. Select one of
the at least `R(t)-1` nonzero quotient anchors. Its three-generator ideal in
`(NZC8)` is contained in `mathfrak p`, so its norm is divisible by `p`. This
proves `(NZC9)`. A prime outside `D_n^NZ` therefore has `Y_18=0`, and the
cutoff-18 double-accident reduction proves C36'. QED.
