# Proof

Assume for contradiction that the dominant component is `(SPX3)`.  For each
`y in P^1(Fbar)`, put

```text
a_y=|Z intersect g^(-1)(y)|,
b_y=|D intersect f^(-1)(y)|.                          (1)
```

The degrees of the two rational maps give

```text
0<=a_y<=e,       sum_y a_y=T,
0<=b_y<=r,       sum_y b_y=N.                         (2)
```

Every grid zero is one pair with a common image `y`, and conversely, so

```text
I_*=sum_y a_y b_y.                                    (3)
```

## 1. A sharp capacity bound

Write

```text
T=q e+s,       q=floor(T/e),       0<=s<e,
L=N-q r.                                                   (4)
```

Suppose `0<L<=r`.  Among all sequences satisfying `(2)`, the dot product in
`(3)` is maximized by concentrating the `a`-mass into `q` entries equal to
`e` and one entry equal to `s`, then placing `r` units of `b` on each full
entry and the remaining `L` units on the partial entry.  This is the usual
exchange proof of rearrangement: moving `a`-mass from a smaller-`b` entry to
a larger-`b` entry cannot decrease the dot product, and the same argument
then concentrates `b` under the largest `a` entries.  Therefore

```text
I_*<=q e r+sL,
C_*=N e-I_*>=L(e-s).                                  (5)
```

It remains to check the official integer ranges.

## 2. The `q=4` range

Put `b=m-e`.  From `(SPX1)`,

```text
4<T/e<6,
```

so `q` is either four or five.  If `q=4`, then

```text
s=4b+1,
L=16b+4,
e-s=m-5b-1.                                          (6)
```

The condition `q=4` gives `m-5b-1>=1`, and

```text
r-L=4m-20b-5>=3,
```

so `(5)` applies.  As a function of real `b` on the permitted interval,

```text
(16b+4)(m-5b-1)
```

is concave.  Its endpoint values are at least

```text
4(m-1),       (16m-12)/5,
```

both strictly greater than `m` for `m>1`.  Hence `C_*>m` in this range.

## 3. The `q=5` range

Now suppose `q=5`.  Since `m=2^37` is congruent to `2 modulo 5`, the integer
condition `e<=T/5` gives

```text
b>=ceil((m-1)/5)=(m+3)/5.                            (7)
```

The lower bound in `(SPX1)` and divisibility of `m` by four give

```text
b<=m/4-1.                                             (8)
```

Here

```text
s=5b-m+1,
L=20b-4m+5>=17,
e-s=2m-6b-1>=m/2+5.                                  (9)
```

Also `L<=m-15<r`, so `(5)` again applies.  Equations `(9)` yield

```text
C_*>=17(m/2+5)>m.                                    (10)
```

Thus `(SPX4)` holds in both possible ranges.  It contradicts the exact total
column-defect budget `(SPX5)`, proving that the dominant component is not a
separated rational pullback.

## 4. Separation-rank corollary

The dominant component has positive degree in both variables and is
irreducible, so it cannot have separation rank one.  Suppose it had rank two:

```text
Q_*=A_0(X)B_0(U,V)+A_1(X)B_1(U,V).                   (11)
```

After homogenizing the `A_i` to binary forms of degree `r`, irreducibility
forces `gcd(A_0,A_1)=1` and `gcd(B_0,B_1)=1`; a nonconstant common factor on
either side would divide `Q_*`.  The two coprime pairs therefore define
rational maps of degrees exactly `r` and `e`, and `(11)` is their
cross-multiplied equality.  This is the separated pullback already excluded.
Thus the separation rank is at least three, proving `(SPX6)`.

The same reasoning applies directly to the full generic generator.  It has
no parameter-only or parameter-independent factor and has bidegree
`(4m-1,m)`.  Rank one is therefore impossible.  Rank two would give a
base-point-free separated equality with map degrees `4m-1` and `m`.  In the
capacity notation,

```text
q=4,       s=1,       L=N-4(4m-1)=4,
```

so `(5)` gives

```text
N*m-I>=4(m-1)>m.
```

But endpoint saturation gives the exact left side `1+O<=m`.  Hence the full
generator also has separation rank at least three.  QED.
