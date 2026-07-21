# Proof

The uniform split-pencil dependency gives `t>=4`, pairwise nonproportional
active rows, row weight at least `a+1`, selected-block intersection at most
`a`, and a polynomial-pencil model of degree at most `d` on `X`.

At every active coordinate, evaluation on the two-dimensional row space is a
nonzero functional. Its kernel contains at most one projective row class.
Thus the `Z_i` are pairwise disjoint. The row-weight floor gives

```text
z_i<=rho-(a+1)=d.                                    (1)
```

For two rows, disjointness of their zero sets and containment of their
supports in the selected blocks give

```text
rho-z_i-z_j
 =|supp(lambda_i) intersect supp(lambda_j)|<=a.
```

Therefore `z_i+z_j>=d+1`. In particular no `z_i` is zero, proving `(SR2)`.

Order the sizes so that `z_1<=...<=z_t`. Then

```text
z_j>=max(z_1,d+1-z_1)       for j>=2.
```

For fixed `z_1`, the smallest possible total is

```text
z_1+(t-1)max(z_1,d+1-z_1).
```

Below the midpoint this decreases as `z_1` increases; above the midpoint it
equals `t z_1` and increases. Thus its minimum is attained at
`z_1=floor((d+1)/2)`, giving `(SR3)` and its equality profiles. Disjointness
gives `sum_i z_i<=rho`; solving `M_d(t)<=a+d+1` gives `(SR4)`.

After dividing the two pencil polynomials by their gcd, a row with `z_i`
distinct zeros forces the rational-map degree to be at least `z_i`. The
dependency gives the upper bound `d`, proving the degree claim.

It remains to prove the Maxwell router. Put

```text
S_i=supp(lambda_i),
I_0=sum_i |S_i|,
P_0=sum_(i<j)|S_i intersect S_j|,
Z=sum_i z_i.
```

The disjoint-zero description gives

```text
I_0=t rho-Z,
P_0=C(t,2)rho-(t-1)Z.                               (2)
```

There are

```text
E=t(a+h)-I_0=t(h-d-1)+Z                             (3)
```

additional block incidences beyond the active supports. Let `q` be the
number of coordinates outside `X` carrying at least one additional
incidence, so `v_J=rho+q`.

An added incidence on a coordinate already in `X` creates at least one new
block-pair incidence. If an outside coordinate carries `r` added incidences,
it saves `r-1` coordinates relative to private placement and creates
`C(r,2)>=r-1` block pairs. Hence the new block-pair incidence is at least
`E-q`. The pair cap supplies only

```text
a C(t,2)-P_0
```

unused pair incidence. Therefore

```text
q>=E-(a C(t,2)-P_0).
```

Substitute `(2)--(3)` and `rho=a+d+1`:

```text
v_J>=rho+t(h-d-1)+(d+1)C(t,2)-(t-2)Z.               (4)
```

Twice `(4)`, minus `2a+ht`, is the first inequality in `(SR5)`. The second
uses both `Z<=td` and `Z<=rho`.

For all blocks of a minimal Maxwell core, the defining identity is

```text
h|G|=2|union G|-2a+e,       e>=0.
```

Thus a full active set has `Delta_J=-e<=0`; positivity of `D_min` excludes
it.

For `d=2`, use `Z<=2t` in `(SR5)` to get

```text
Delta_J>=6+t(h-t-1).                                 (5)
```

The `d=2` arity bound is `t<=floor((a+4)/2)`. Equation `(5)` proves the two
`h=5,a<=7` cases. At `h=3,a=4`, one has `t=4` and the sharper `Z<=rho=7`;
`(SR5)` gives `Delta_J>=2`. At a prize row, `a<=2h-5` implies `t<=h-1`, so
`(5)` is at least six. Substitution of the three printed `h` values gives
the first consequence.

For `d=3`, use `Z<=3t` to obtain

```text
Delta_J>=8+t(h-2t).                                  (6)
```

Here `t<=floor((a+4)/2)`. At the odd prize values of `h`, the printed bounds
on `a` imply `t<=floor(h/2)`, so `(6)` is positive.

Finally take `d=a-1`. If `a` is odd, `(SR4)` gives `t<=3`, contradicting
`t>=4`. If `a` is even, `(SR4)` gives `t<=4`; hence `t=4`, and equality in
the odd-`d` zero-mass bound forces four fibers of size `a/2` whose union is
all `2a` coordinates. QED.
