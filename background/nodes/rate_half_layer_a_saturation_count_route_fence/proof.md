# Proof

For `x in W subset U`, one has `x^16=1`, hence `x^2 in H`. Since
`-1 in H`, both roots

```text
gamma=+x^2, -x^2
```

of `Q(Z,x)=Z^2-x^4` lie in `H`. They are distinct because the
characteristic is odd. No other element of `H` is a root, and the ninth
slope `eta` is not a root because `eta notin H`. Thus every `x` has exactly
two incident slopes and `(LAW2)` follows.

It remains to determine the kernel. Write an arbitrary biform of the allowed
bidegree as

```text
F(Z,X)=a_2(X)Z^2+a_1(X)Z+a_0(X),       deg a_i<=7.
```

If `F` vanishes on `I`, then for every `x in W`,

```text
F(x^2,x)=a_2(x)x^4+a_1(x)x^2+a_0(x)=0,
F(-x^2,x)=a_2(x)x^4-a_1(x)x^2+a_0(x)=0.
```

Subtracting and using `2x^2!=0` gives `a_1(x)=0` at thirteen distinct
points. Since `deg a_1<=7`, this forces `a_1=0`. Adding shows that

```text
b(X)=a_0(X)+X^4a_2(X)
```

vanishes at the same thirteen points. Its degree is at most eleven, so
`b=0`. Therefore `a_0=-X^4a_2`; the bound `deg a_0<=7` forces
`deg a_2<=3`. Conversely every `A(X)(Z^2-X^4)` with `deg A<=3` has the
allowed bidegree and vanishes on `I`.

The kernel is consequently four-dimensional. The matrix has 24 columns, so
its rank is `24-4=20`, proving `(LAW3)`. QED.
