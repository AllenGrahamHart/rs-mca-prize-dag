# Proof

Cycle 124 gives pair union at least `rho+4`. Suppose one pair has

```text
U=S_alpha union S_beta,       |U|=rho+j,
4<=j<=rho.                                             (1)
```

Remove the fixed core and put

```text
U_0=U\{s_0},       u=|U_0|=rho+j-1.                  (2)
```

Every point of `U_0` is light and therefore occurs in exactly `e` actual
supports globally. Hence the total incidence of all `T=3e+3` supported
slopes on `U_0` is

```text
e u.                                                  (3)
```

Let `A` be the complete set of supported slopes whose assigned centers lie
on the codeword line through the endpoint centers. Write

```text
h=|A|,       d_A=sum_(gamma in A)r_gamma.             (4)
```

The line's joint residual support is exactly `U`. A line slope `gamma`
therefore misses

```text
u-(rho-r_gamma-1)=j+r_gamma                          (5)
```

points of `U_0`. Each nonzero residual coordinate vanishes at at most one
line slope, so

```text
jh+d_A<=u.                                           (6)
```

The exact line incidence on `U_0` is `hu-jh-d_A`.

Now take a supported slope `delta` off the endpoint line. Minimum distance
forces

```text
|U union S_delta|>=2rho+1.
```

Since `|S_delta|=rho-r_delta`,

```text
|S_delta intersect U_0|<=j-r_delta-2.               (7)
```

The packet-wide deficit is `D=e-6`. Summing `(7)` over the `T-h` off-line
slopes, and adding the exact line incidence, gives

```text
e u
 <=h(u-j)-d_A+(j-2)(T-h)-(D-d_A)
 =h(rho-j+1)+(j-2)T-D.                              (8)
```

Equation `(6)` gives `h<=u/j`. Substitute this real upper bound into `(8)`
and multiply by `j`. A necessary condition is

```text
F_e(j)<=0,                                           (9)
```

where

```text
F_e(j)
 =3e^2j-9e^2-2ej^2+5ej+6e-2j^2-2j.                (10)
```

The quadratic `(10)` is concave in `j`. Since the official `e` is odd,
`rho/2=(3e-1)/2` is an integer. On the interval

```text
4<=j<=rho/2-2=(3e-5)/2,                             (11)
```

a concave function attains its minimum at an endpoint. Direct substitution
gives

```text
F_e(4)=3e^2-6e-40>0,
F_e((3e-5)/2)=(3e^2-14e-15)/2>0.                   (12)
```

Both inequalities hold for the official `e` (indeed for `e>=7`). Thus
`(9)` is impossible throughout `(11)`. Combining with the Cycle-124 floor
proves

```text
j>=rho/2-1,                                         (13)
```

which is `(MPF2)`.

For a codeword line with `h>=2` centers, its joint support contains a pair
union of at least `rho+j_0`. Repeating `(5)--(6)` with this lower bound gives
`(MPF4)`. Since

```text
4j_0=2rho-4>3rho/2-2,
```

one has `h<=3`; at `h=3`, `(MPF4)` gives `d_A<=1`. This proves `(MPF5)`.

Finally, any third slope whose full locator triple has union at most
`2rho` has its center on the endpoint line. That line contains at most three
supported centers, including the endpoints. Since `T=rho+4`, at least

```text
T-3=rho+1
```

other slopes are off the line and satisfy `(MPF6)`. QED.
