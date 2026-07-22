# Proof

The flat-nullity basis charge gives, before the outer integer floor,

```text
E(u,v)=
 [a L C(R+a+u,a)+v(W_u(a+h+u+v)-W_u(a+h+u))]
 /W_u(a+h+u+v),                                    (1)
```

and `|P|<=max(v,floor(E(u,v)))`. Write

```text
C_v=C(a+h+v-1,a-1),       C_0=C(a+h-1,a-1),
c=a+h.
```

Since

```text
W_u(c+u+v)=(c+u+v)C_v,
W_u(c+u)=(c+u)C_0,
```

equation `(1)` becomes

```text
E(u,v)=v(1-C_0/C_v)
 +[a L C(R+a+u,a)+v^2 C_0]/[(c+u+v)C_v].           (2)
```

We prove the endpoint reduction. Set `y=c+u+v` and `D=R-h-v`. Then

```text
C(R+a+u,a)/(c+u+v)
 =C(y+D,a)/y
 =(1/a!) product_(j=0)^(a-1)(y+D-j)/y.             (3)
```

On every prize row, `v<=k-a` and

```text
D-(a-1)>=R-h-k+1>0.                                 (4)
```

Expanding `(3)` in powers of `y` therefore gives a positive linear
combination of

```text
y^(a-1), y^(a-2), ..., y, 1, 1/y.
```

Each term is convex on `y>0`. The other nonconstant term in `(2)` is a
positive multiple of `1/y`. Hence `E(u,v)` is convex in `u`, and its maximum
on the allowed interval is attained at one of the endpoints in `(NC1)`.

For a uniform bound at those endpoints, discard the negative correction in
the first term of `(2)` and use `v<=k<B`. At `u=0`,

```text
E(0,v)<=k+
 a L C(R+a,a)/[(c+v)C(c+v-1,a-1)].                  (5)
```

At `u=k-a-v`,

```text
E(k-a-v,v)<=k+
 a L C(n-v,a)/[(k+h)C(c+v-1,a-1)].                 (6)
```

Both displayed correction terms decrease with `v`: their denominators
increase, and the numerator in `(6)` also decreases. Let `V` be the least
integer for which both right sides are at most `B`. Exact cross-multiplication
at the three first-open prize cells gives

```text
V=1,526,176,111;       2,902,067,940;       1,962,285,107.  (7)
```

For `v>=V`, convexity plus `(5)--(6)` gives `E(u,v)<=B` for every allowed
`u`; also `v<B`. Thus `(FN3)` pays the cell. Any over-budget cell has
`v<=V-1`, giving the final column of the table. The effective-core column is
`xr_prize_flat_nullity_effective_core_floor`. QED.
