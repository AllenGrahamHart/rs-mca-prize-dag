# Proof

Put

```text
f(x)=log(18+x),               -18<x<=M,
a=-v/M.
```

Let `q` be the quadratic Hermite interpolant satisfying

```text
q(a)=f(a),       q'(a)=f'(a),       q(M)=f(M).       (1)
```

The Hermite remainder at every `x<M` is

```text
f(x)-q(x)=f'''(xi)(x-a)^2(x-M)/3!                  (2)
```

for a `xi` between `x,a,M`. Since

```text
f'''(xi)=2/(18+xi)^3>0,
```

equation `(2)` is nonpositive; equality also holds at `M`. Thus

```text
f(x)<=q(x)                  for every -18<x<=M.      (3)
```

Now let `x_1,...,x_64` have

```text
sum x_u=0,                  sum x_u^2=64v.           (4)
```

The average of any quadratic is determined by `(4)`. The two-point
distribution on `{a,M}` with weights

```text
w_a=M^2/(M^2+v),            w_M=v/(M^2+v)            (5)
```

has the same first two moments. Summing `(3)` and using `(1),(4),(5)` gives

```text
sum_u log(18+x_u)
 <=64[w_a log(18-v/M)+w_M log(18+M)].               (6)
```

For an autocorrelation profile `(n_1,n_2,n_3)`, put

```text
E=n_1+4n_2+9n_3,          L=n_1+2n_2+3n_3.
```

The conductor-256 moment dictionary gives `(4)` with `v=2E`, while the
triangle inequality gives `x_u<=2L`; hence take `M=2L` in `(6)`.

For `(E;n_1,n_2,n_3)=(9;1,2,0)`, this gives

```text
v=18, M=10, a=-9/5, w_a=50/59, w_M=9/59,

Norm(F)^59
 <=(81/5)^3200 28^576
 <(514 p_min)^59.                                      (7)
```

For `(E;n_1,n_2,n_3)=(11;7,1,0)`, it gives

```text
v=22, M=18, a=-11/9, w_a=162/173, w_M=11/173,

Norm(F)^173
 <=(151/9)^10368 36^704
 <(514 p_min)^173.                                     (8)
```

Both strict inequalities are exact integer cross-multiplications with

```text
p_min=317494674775468773183020924238786383963*2^128.
```

Their positive cross-multiplied margins have bit lengths `23060` and
`78695`, respectively. Equations `(7)--(8)` force
`Norm(F)<514*p_min`, contradicting an official-row cofactor-`514`
collision. Deleting the two rows from the proved 15-profile ledger leaves
13 profiles. QED.
