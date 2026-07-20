# Proof

For either budget in `(RPFC1)`, the field order is odd and satisfies

```text
2^167<q<2^168.                                           (1)
```

The lower inequality is immediate for `B=2^39+1`; for `B=2^39`, equality
would make `q` a power of two, contrary to `2^41|q-1`.

Write `q=p^f`. Since `p>=3` and `3^106>2^168`, one has `f<=105`. If `f` is
odd, odd-exponent LTE gives

```text
v_2(p^f-1)=v_2(p-1)>=41.
```

Hence `p>=2^41+1`. If odd `f>=5`, then `p^f>2^205`, contradicting `(1)`.
Thus odd `f` is `1` or `3`.

Suppose `f` is even and put `t=v_2(f)`. The even-exponent LTE formula gives

```text
v_2(p^f-1)=v_2(p-1)+v_2(p+1)+t-1>=41.                (2)
```

Exactly one of `p-1,p+1` has 2-adic valuation one, so `(2)` implies

```text
p>=2^(41-t)-1.                                         (3)
```

The bound `f<=105` gives `t<=6`. If `3<=t<=6`, then `f>=2^t` and already

```text
(2^(41-t)-1)^(2^t)>2^168,
```

as follows for example from `2^(41-t)-1>2^(40-t)`; the smallest resulting
exponent is `(40-3)2^3=296`. Hence `t` is one or two. If `t=1` and `f!=2`,
then `f>=6`; `(3)` gives `p>2^39`, so `q>2^234`. If `t=2` and `f!=4`, then
`f>=12`; `(3)` gives `p>2^38`, so `q>2^456`. Both contradict `(1)`. This
proves `(RPFC4)`.

It remains to exclude `f=2,3,4`. For a budget `B`, define

```text
L_B=B*2^128,       U_B=(B+1)*2^128,
I_(B,f)={p in Z:ceil(L_B^(1/f))<=p<ceil(U_B^(1/f))}.  (4)
```

The unit group modulo `2^41` is `C_2 x C_(2^39)`. Therefore the complete
root sets of `x^f=1 mod 2^41` have sizes four, one, and eight for
`f=2,3,4`, respectively. Explicitly they are

```text
f=2: {1,-1,1+2^40,-1+2^40},
f=3: {1},
f=4: {+/-1+j*2^39:0<=j<4},                            (5)
```

with residues taken modulo `2^41`.

The verifier computes both endpoints in `(4)` by exact integer binary
search, intersects each interval with every residue class in `(5)`, and
checks the defining power and interval inequalities for every result. The
`f=3,4` intersections are empty. The `f=2` intersections contain exactly
the `46` integers in `quadratic_candidate_factors.tsv`; for every row the
printed integer is strictly between one and the candidate and divides it
exactly. Hence none is prime. This excludes all `f>1` in `(RPFC4)` and proves
`(RPFC2)`.

Finally `(1)` and `f=1` give `(RPFC3)`. QED.
