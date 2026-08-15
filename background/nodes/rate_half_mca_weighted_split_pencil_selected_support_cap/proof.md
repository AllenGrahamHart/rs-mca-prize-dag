# Proof

Write `q(x)=C(x,2)`. For a line `L`, abbreviate `x_p=x_(L,p)` and put

```text
Q_L=sum_p q(x_p),       X_L=sum_(p<r) x_p x_r.
```

Since `sum_p x_p=A`,

```text
Q_L+X_L=C(A,2).                                      (1)
```

Call an owner point globally heavy when `s_p>A/2`. There are at most

```text
h=floor(S/(floor(A/2)+1))                            (2)
```

such points. Classify each line by its selected partition.

## Balanced selected partitions

Suppose `max_p x_p<=A/2`. Then

```text
sum_p x_p^2 <= (max_p x_p) sum_p x_p <= A^2/2.
```

Together with

```text
2Q_L=sum_p x_p^2-A,
2X_L=A^2-sum_p x_p^2,
```

this gives `Q_L<=X_L`.

Interpret `X_L` as the number of unordered coordinate pairs selected from
two different owner petals on `L`. A coordinate pair from two distinct
petals determines its two owner points, and those points determine a unique
affine line. Since the lines are distinct, no such coordinate pair is
counted by two lines. Therefore

```text
sum_(L balanced) Q_L
 <=sum_(L balanced) X_L
 <=sum_(p<r) s_p s_r
 <=C(S,2).                                           (3)
```

## Dominant lines with two heavy owners

Every remaining line has a unique selected dominant owner with `x_p>A/2`.
First set aside lines containing at least two globally heavy owner points.
Any pair of heavy points determines at most one line, so there are at most
`C(h,2)` such lines. Convexity under `sum x_p=A` and `x_p<=A-1` gives

```text
Q_L<=C(A-1,2).
```

Hence these collision lines contribute at most

```text
C(h,2)C(A-1,2).                                     (4)
```

## Clean dominant lines

It remains to consider a dominant line whose dominant owner `p` is the only
globally heavy point on the line. Put `s=s_p` and `d=A-s`; then

```text
A/2<s<=A-1,       1<=d<A/2.
```

If its selected dominant mass is `x`, the complementary selected masses sum
to `A-x`. Superadditivity of `q` and monotonicity away from `A/2` give

```text
Q_L <= q(x)+q(A-x) <= q(s)+q(d).                    (5)
```

Distinct lines through `p` have disjoint sets of other owner points. Every
clean line through `p` uses at least

```text
A-x>=A-s=d
```

selected mass from globally light petals. If `H` and `L` are the total
heavy and light petal masses, respectively, the number of clean lines
through `p` is at most `L/d`.

The needed one-variable inequality is exact. After multiplying by `2d`,
its slack factors as

```text
d*s*(A-2)-[s(s-1)+d(d-1)]
 =(d-1)(d+s)(s-1)>=0.
```

Thus

```text
[q(s)+q(d)]/d <= s(A-2)/2.                          (6)
```

Summing (5)--(6) first over clean lines through one heavy owner and then
over all heavy owners gives

```text
sum_(L clean dominant) Q_L
 <=(A-2)HL/2
 <=(A-2)S^2/8,                                     (7)
```

where the last step uses `H+L<=S` and `HL<=(H+L)^2/4`. The left side is an
integer, so the floor of the last expression is valid. Adding (3), (4),
and (7) proves `(SP1)`.
