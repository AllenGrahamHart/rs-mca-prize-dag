# Proof

Work over the algebraic closure of `K`. Write `D_act` and `D_src` for the
reduced zero divisors of `V_act` and `A`. The endpoint divisor is

```text
div(f)=D_act-5 D_src.                                (KBD-1)
```

Suppose `f=F composed h`, with `deg(h)=m` and `deg(F)=n`. If an outer zero
`z` has order `c` and `x` lies above it with ramification index `e_h(x)`,
then its order in `F(h)` is `c e_h(x)`. Every zero in `(KBD-1)` has order
one. Hence

```text
c=1,       e_h(x)=1                                 (KBD-2)
```

at every point over every outer zero. The zero divisor of `F` therefore has
`n` distinct points. Each has `m` distinct unramified preimages, and
`(KBD-1)` says all of them are roots of `V_act`. Their total number is
`mn=60`, so they partition the complete active divisor into `n` fibers of
size `m`. Since the active roots lie in `K`, every point in every printed
fiber lies in `K`.

Now let an outer pole have order `r`. Every point above it is a source root
and satisfies

```text
r e_h(x)=5.                                         (KBD-3)
```

Thus `r` is one or five. An order-five outer pole has one complete
unramified fiber of `m` source points. An order-one outer pole has `m/5`
source points, each of ramification index five. If `a,b` count the two pole
types, respectively, then

```text
5a+b=n,       a m+b m/5=12.                         (KBD-4)
```

Substituting the eight profiles from the proved pole and Riemann-Hurwitz
ladder gives:

```text
(m,n,a,b)=(2,30,6,0), (3,20,4,0), (4,15,3,0),
            (5,12,2,2), (6,10,2,0), (10,6,1,1),
            (12,5,1,0), (30,2,0,2).
```

Applying the two fiber rules to these rows is exactly the table in the
statement. No coefficient-field descent is used. QED.
