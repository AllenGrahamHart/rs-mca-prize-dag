# Proof

Suppose distinct supported slopes `alpha,beta` satisfy

```text
|S_alpha union S_beta|=rho+3.                       (1)
```

Use the bidirectional heavy-incidence localization. Put

```text
R=r_alpha+r_beta,
X=S_beta\S_alpha,       Y=S_alpha\S_beta,
n=|X|+|Y|=R+6.                                      (2)
```

The supported slopes are partitioned into the common center-line set `L`,
the `n` pairwise disjoint residual root sets, and the slack set `W`, with

```text
|L|=g+1,
|R_x|=e-g,
s=|W|=(R+5)g-(R+3)e+2.                             (3)
```

Every residual slope has deficit zero and belongs to the support of exactly
one point of `X union Y`.

Let

```text
J=(S_alpha intersect S_beta)\{s_0}.
```

Then

```text
|J|=rho-R-4=3e-R-5.                                (4)
```

No residual slope can support a point of `J`. Such a slope already supports
`s_0` and one point of `X union Y`; adding a point of `J` would give three
actual-support intersections with `S_alpha union S_beta`, so its triple
support union would have size at most `2rho`. Minimum distance would put its
center on the endpoint line, where it would be a common gcd root rather than
a residual root.

A slope in `W` supports no point of `X union Y`. If it has deficit zero, it
can support at most one point of `J`; two such points together with `s_0`
would again force the center onto the endpoint line. If it has deficit one,
even one point of `J` forces the line. A slope in `W` cannot have deficit at
least two, because the fixed core point alone then gives

```text
|S_alpha union S_beta union S_delta|
 <=rho+3+(rho-2)-1=2rho.                            (5)
```

In every case line ownership would make the third error support contain all
of `X union Y`, contrary to membership in `W`. Thus

```text
r_delta<=1       for delta in W,
|S_delta intersect J|<=1_(r_delta=0).               (6)
```

Every point of `J` is light and has global supported degree `e`. It has at
most `g+1` incidences on `L`, none on a residual slope, and therefore at
least `e-g-1` incidences in `W`. If `g<=e-2`, put `q=e-g>=2`. Equations
`(3),(4),(6)` would require

```text
(3e-R-5)(q-1)<=s=2e-(R+5)q+2.                      (7)
```

The left side minus the right side is

```text
e(3q-5)+R+3>0,                                     (8)
```

a contradiction. Since the two parameter forms defining either oriented
pencil are independent of degree at most `e`, their common gcd has degree
at most `e-1`. Hence

```text
g=e-1.                                              (9)
```

Now `|L|=e` and `s=2e-R-3`. Put

```text
d_L=sum_(delta in L)r_delta.
```

The line-deficit cap `(BHL7)` at `g=e-1` gives `d_L<=1`.

The exact line missing count is `3e+d_L`, while every point of
`X union Y` is missing at exactly its defining endpoint. Thus the number of
points of `J` missing at one slope of `L` is

```text
M_J=3e+d_L-(R+6)=3e-R-6+d_L.                       (10)
```

Each such point needs exactly one incidence outside `L` to reach its global
degree `e`. Residual slopes support no point of `J`. The packet deficit is
`e-6`, all residual deficits vanish, and `(6)` makes every positive deficit
in `W` equal one. Therefore the number of zero-deficit slack slopes is

```text
|W_0|=s-(e-6-d_L)=e-R+3+d_L.                       (11)
```

By `(6)`, each of them supplies at most one `J` incidence. Equations
`(10),(11)` force

```text
3e-R-6+d_L<=e-R+3+d_L,
2e<=9,                                               (12)
```

contrary to the official `e=183251937963`. This proves `(QME1)`.

If a codeword line contains `h>=2` assigned centers, its joint support
contains the union of any two endpoint supports and hence has size at least
`rho+4`. A nonzero projective linear coordinate is present at at least
`h-1` selected slopes, so

```text
(h-1)(rho+4)
 <=sum_(gamma in A)|S_gamma|
 =h rho-sum_(gamma in A)r_gamma.                    (13)
```

Rearranging gives `(QME2)`. Finally, every third slope whose full locator
triple has union at most `2rho` has its center on the endpoint line.
Equation `(QME2)` bounds the number of such line centers by

```text
floor((rho+4-r_alpha-r_beta)/4).                    (14)
```

Subtracting `(14)` from `T=rho+4` proves `(QME3)--(QME4)`. QED.
