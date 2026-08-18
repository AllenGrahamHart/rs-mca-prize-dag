# Proof

Let `P` be the 520 selected points in the two-dimensional scalar polynomial
space, and let `L` range over affine `F`-lines containing at least two points
of `P`. Put `r_L=|L intersection P|`. The affine-line cap gives

```text
2<=r_L<=15.                                           (1)
```

Every unordered pair of selected points determines a unique affine line, so

```text
sum_L binom(r_L,2)=binom(520,2),
sum_L r_L(r_L-1)=520*519=269880.                      (2)
```

Fix a selected point. The other 519 points are partitioned among the secant
lines through it, with at most 14 other points on each line. Thus every point
is incident to at least

```text
ceil(519/14)=38                                      (3)
```

secant lines. If `b` is the number of lines and `I=sum_L r_L` is their point-
line incidence count, `(3)` gives `I>=520*38=19760`. Also, by `(2)`,

```text
sum_L r_L^2=269880+I.
```

Cauchy--Schwarz gives

```text
I^2<=b(269880+I).
```

The function `I^2/(269880+I)` is increasing for positive `I`, hence

```text
b>=ceil(19760^2/(269880+19760))=1349.                (4)
```

## Common-core packing

Factor the scalar-space gcd as in the dimension-two common-core theorem.
For an affine secant line `L=S+FT`, every pair of selected types on `L` has
the same complete pair-core intersection `I_L`: on a root of `T` all their
pair codewords have the common line value, and off those roots distinct line
parameters give distinct pair codewords.

Take two distinct affine secant lines. If their directions are distinct, a
point of both intersections is a common root of two independent primitive
pencil members. If they are parallel, it is a common root of the direction
and the nonparallel offset difference. Either way the coordinate lies in the
scalar-space gcd root set. Since it also lies in one actual pair-core
intersection, the received pair equals the common codeword-pair value there.
Thus it lies in `J`. Conversely `J` lies in every complete pair core, proving

```text
I_L intersection I_M=J                              (5)
```

for distinct secant lines.

Every `I_L` has size at least `134940`. Select 1349 lines from `(4)`. Their
petals outside `J` are disjoint, so with `j=|J|`,

```text
2097152>=1349*134940-1348j.
```

Ceiling division gives `j>=133485`. At this floor the shortened domain has
size `2097152-133485=1963667`, each residual petal has size at least
`134940-133485=1455`, and

```text
1963667-1349*1455=872.
```

The reversible shortening itself is the preceding proved node. QED.
