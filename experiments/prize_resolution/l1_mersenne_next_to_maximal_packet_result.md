# Mersenne next-to-maximal packet result

The exact constant-memory check covers the five official rows with
`m in {8,16}` and `h=m-1`. For the forced outer binomial, there are
`m-2` distinct normalized nonzero split values `z`, and every
`w=1-z` must satisfy

```text
xi W^2+(1-xi)W-epsilon=0,
W^(p+1)=epsilon,       epsilon^m=1.
```

For every row, the only admissible norm packet is `epsilon=1`, and its gcd
has degree one. Thus at most one `w` exists, versus the required six or
fourteen distinct values.

```text
p=8191        m=8   xi=8100       required=6   available=1
p=131071      m=8   xi=109166     required=6   available=1
p=524287      m=8   xi=454794     required=6   available=1
p=2147483647  m=8   xi=634005911  required=6   available=1
p=8191        m=16  xi=6763       required=14  available=1
```

This is an exact finite packet certificate, not a search over coefficients,
supports, or field elements.
