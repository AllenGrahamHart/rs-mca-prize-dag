# Proof

Write `q(x)=C(x,2)`.  For one line abbreviate `x_p=x_(L,p)` and put

```text
Q_L=sum_p q(x_p),       X_L=sum_(p<a) x_p x_a.
```

Since `sum_p x_p=P`,

```text
Q_L+X_L=C(P,2).                                      (1)
```

Call an owner globally heavy when `s_p>P/2`.  There are at most

```text
h=floor(S/(floor(P/2)+1))                            (2)
```

such owners.

## Balanced lines

If `max_p x_p<=P/2`, the argument from the zero-offset selected-support
theorem gives `Q_L<=X_L`.  Moreover a balanced integral partition of `P`
has

```text
X_L>=M=floor(P^2/4).                                 (3)
```

Indeed `X_L` is minimized by concentrating the partition as much as the
half-mass ceiling permits; `M` is a valid lower bound for both parities.
Cross-owner coordinate pairs inject globally because their two owner points
determine a unique affine line.  Hence

```text
sum_(L balanced) X_L<=sum_(p<a) s_p s_a<=C(S,2).
```

Equation (3) also bounds the number of balanced lines by
`sum X_L/M`.  Therefore

```text
sum_(L balanced) R_L
 <=(1+rP/M) C(S,2).
```

The left side is integral, so the floor in `(SPO)` is valid.

## Heavy-owner collision lines

Every nonbalanced line has a unique selected dominant owner.  Set aside
lines containing at least two globally heavy owners.  A pair of heavy points
determines at most one line, so there are at most `C(h,2)` such lines.
Convexity under `sum x_p=P` and `x_p<=P-1` gives

```text
Q_L<=C(P-1,2).
```

Their total offset charge is therefore at most

```text
C(h,2)(C(P-1,2)+rP).                                (4)
```

## Clean dominant lines

For a remaining line let its dominant owner have global weight `s`, and put
`d=P-s`.  Then `P/2<s<=P-1` and `1<=d<P/2`.  If its selected dominant mass
is `x`, superadditivity of `q` on the complementary masses and monotonicity
away from `P/2` give

```text
Q_L<=q(x)+q(P-x)<=q(s)+q(d).                        (5)
```

Distinct lines through this owner use disjoint sets of globally light owner
points.  Each uses at least `P-x>=d` selected light mass.  If `H` and `ell`
are the total heavy and light masses, respectively, at most `ell/d` clean
lines pass through this owner.

The zero-offset slack identity is

```text
d*s*(P-2)-[s(s-1)+d(d-1)]
 =(d-1)(d+s)(s-1)>=0.
```

Consequently

```text
[q(s)+q(d)+rP]/d <=s(P-2)/2+rP.                    (6)
```

There are at most `h` heavy owners.  Summing (5)--(6), and using
`H+ell<=S`, bounds all clean lines by

```text
ell*((P-2)(S-ell)/2+h*r*P).
```

Maximizing over the integral light mass `0<=ell<=S` gives `C_clean`.
Adding the balanced, collision, and clean bounds proves `(SPO)`.
