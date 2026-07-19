# Proof

Fix a target of excess `e=P(t)-18>=15`, and let `m` be its number of small
representations. The degree ladder gives

```text
m>=7+ceil(e/2),
W(t)=2N_4(t)+N_6(t)>=ceil(m(m-4)/2).                (1)
```

If the fiber is antipodal-free, the distance-four fiber-degree cap gives

```text
N_4(t)<=m,
```

and hence

```text
N_6(t)>=F_0(m):=ceil(m(m-4)/2)-2m.                 (2)
```

If the fiber contains its unique antipodal representation, the norm profile
from the same theorem improves the centroid input from `3m` to `3m-2`:

```text
m sum_E ||v_E||^2 <=m(3m-2).
```

Repeating the centroid rearrangement gives

```text
W(t)>=ceil(m(m-2)/2).
```

Together with `N_4(t)<=2(m-1)`, this gives

```text
N_6(t)>=F_A(m):=ceil(m(m-2)/2)-4(m-1).             (3)
```

The two ceiling terms differ by exactly `m`, so
`F_0(m)-F_A(m)=m-4>=0` on the selected tail. Thus `(3)` is a uniform lower
bound. At `m=15`, it gives

```text
F_A(15)=98-4*14=42.
```

Here `e<=16`, so `21e<=8F_A(m)`, with equality possible at `e=16`.

Now take `m>=16`. Discarding favorable rounding in `(3)` gives

```text
F_A(m)>=m(m-2)/2-4(m-1)=(m^2-10m+8)/2.            (4)
```

Also `e<=2(m-7)`. The inequality

```text
(m^2-10m+8)/2 >=21(m-7)/4                         (5)
```

is equivalent to

```text
2m^2-41m+163>=0.
```

The quadratic has value `19` at `m=16` and is increasing thereafter. Equations
`(4),(5)` therefore give

```text
N_6(t)>=21e/8,
```

which is `(H6M2)`.

Multiply `(H6M2)` by `R(t)` and sum over the high tail:

```text
X_18^>14 <=(8/21)M_6,33.                           (6)
```

Under `(H6M3)`, equation `(6)` gives exactly the `E=14` residual budget, so
the proved excess-budget tradeoff closes C36'. Replacing that exact budget by
`62n^2` yields

```text
M_6,33<=(21*62/136)n^2=(651/68)n^2,
```

proving `(H6M4)`. QED.
