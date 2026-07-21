# Proof

The uniform Maxwell compiler gives

```text
|G|<=floor((2N+h-(2a+1))/h).
```

Since `N=R+a`, cancellation of `2a` gives `(PB1)`. Substitution of the three
prize values of `R` and `h` gives `(PB2)`.

Let `t=|G|`. The shell/Maxwell dependency gives

```text
Delta_G
 >=2(d+1)+t(h-2d-2)+(d+1)t(t-1)-2(t-2)Z.           (1)
```

Every row-zero fiber has size at most `d`, so `Z<=td`. Substitution in `(1)`
and collection of powers of `t` gives

```text
Delta_G>=th+(1-d)t^2+(d-3)t+2(d+1)=B_(h,d)(t).      (2)
```

Rank two gives `t>=4`. For `d>=2`, the coefficient of `t^2` in `(2)` is
negative, so `B_(h,d)` is concave. Its minimum on the integer interval
`4<=t<=L_max` is therefore attained at one of the two endpoints.

For a fixed row and `t>=4`, `(2)` decreases with `d`, because

```text
B_(h,d+1)(t)-B_(h,d)(t)=-(t-2)(t+1)<0.             (3)
```

It is consequently enough to check both endpoints at the largest claimed
`D_row`. Direct integer substitution gives every positive value in `(PB4)`.
Thus `(2)` is positive for every `2<=d<=D_row` and every permitted `t`.

If the active rows were all blocks of `G`, the Maxwell identity would instead
give

```text
Delta_G=2|union G|-2a-h|G|=-e<=0,
```

a contradiction. This proves `(PB5)`.

Finally, substituting `D_row+1` and `t=L_max` gives the three negative values
in the statement. This records the exact reach of the present uniform
deficit bound; it neither constructs a trade beyond the endpoint nor claims
the theorem itself is sharp. QED.
