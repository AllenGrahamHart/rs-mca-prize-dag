# Proof

Choose a minimal rank-three presentation

```text
G(t,X)=A_0(t)B_0(X)+A_1(t)B_1(X)+A_2(t)B_2(X).    (1)
```

The all-excess birationality theorems show that

```text
a(t)=[A_0(t):A_1(t):A_2(t)],
b(X)=[B_0(X):B_1(X):B_2(X)]                       (2)
```

are basepoint-free and birational onto their images. Minimality makes each
image nondegenerate in `P^2`. Since the pullbacks of a line have degrees
`m` and `n`, respectively, the images `C_t,C_X` are irreducible rational
plane curves of degrees `m,n`.

Group the marked normalization points as in `(WIG2)--(WIG3)`. In the dual
coefficient planes, equation `(1)` says

```text
G(delta,x)=0 iff a(delta) dot b(x)=0.              (3)
```

Thus equality of either coefficient image makes the corresponding marked
root set identical, and the incidence relation descends to a simple
bipartite graph on the image groups. Two distinct parameter image points
have polar lines meeting in only one domain image point. Hence two
parameter vertices have at most one common domain neighbour. This is
exactly the `C_4`-free property.

Every classified domain row has `m` distinct roots in `Gamma`. For a
domain image vertex `Q`, all of its `l_Q` normalization branches have the
same root set, so counting those roots by parameter image group gives

```text
sum_(P~Q)s_P=m.                                    (4)
```

For an off-line slope `delta`, the all-excess factorization gives

```text
|I_delta|=n-a_delta-r_delta.                       (5)
```

The residual factor has no root on `U_0\I_delta`, while the padded factor
is supported at `x_*`, which lies outside `U_0`. Therefore `(5)` is exactly
the number of marked domain roots of `G(delta,-)`. Slopes with the same
parameter image have proportional nonzero fibers, hence the same marked
root set. The integer

```text
w_P=n-sum_(Q~P)l_Q                                 (6)
```

is consequently common to their group and equals `a_delta+r_delta`.
Shape A has

```text
sum_delta a_delta=e,
sum_delta r_delta=e-7,                             (7)
```

so summing `(6)` with parameter weights proves `(WIG5)`. The remaining
weight sums in `(WIG4)` are definitions.

It remains to charge image collisions. If `s_P` marked normalization
points map to one point of the reduced plane curve `C_t`, they determine
`s_P` distinct local branches there. The local delta invariant is at least
one for every pair of branches, hence at least `binom(s_P,2)`. Since the
normalization is `P^1`, the total delta invariant of `C_t` is its arithmetic
genus `binom(m-1,2)`. Summing over the marked image points proves the first
inequality in `(WIG6)`. The same argument on `C_X` proves the second.

The individual bounds `(WIG7)` follow immediately because
`binom(m,2)>binom(m-1,2)` and similarly for `n`. For the number `N_t` of
parameter image vertices,

```text
sum_P s_P^2
 =T+2 sum_P binom(s_P,2)
 <=3e+(m-1)(m-2)
 =e^2-4e+12.                                      (8)
```

Cauchy--Schwarz gives

```text
9e^2=T^2<=N_t(e^2-4e+12).                         (9)
```

For `e>3`, `(9)` excludes `N_t<=9`, so `N_t>=10`. Similarly, if `N_X`
is the number of domain image vertices, then

```text
sum_Q l_Q^2
 <=R+(n-1)(n-2)=n^2+9,                            (10)
R^2=(3n+7)^2<=N_X(n^2+9).                         (11)
```

Since `(3n+7)^2>9(n^2+9)` for `n>=1`, one has `N_X>=10`.

Finally, `(4)` and `s_P<=m-1` force every domain vertex to have at least
two neighbours. Parameter branches with positive integer deficit have
total weight at most `2e-7`; therefore the zero-deficit branch weight is at
least

```text
T-(2e-7)=e+7.                                     (12)
```

One parameter vertex has weight at most `m-1=e-3`, so `(12)` occupies at
least two vertices. At each such vertex `(WIG5)` gives weighted domain
degree `n`; because `l_Q<=n-1`, it too has at least two neighbours. QED.
