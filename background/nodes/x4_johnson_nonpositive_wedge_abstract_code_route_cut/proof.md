# Proof

The exact-slice corridor theorem gives

```text
128t_XR<=t_XR log2(q)<=N-129,
```

so `t_XR<=N/128-2`.  In particular `d=e-t_XR-1>0`.  At rate one half,
both `S0` and its complement contain at least `N/4=2e` points.

Choose `e` disjoint pairs inside `S0` and another `e` disjoint pairs inside
`D\S0`.  A binary word of length

```text
L=2e=N/4
```

chooses one point from each pair.  Its first `e` choices form `Q`, and its
last `e` choices form `P`.  Every changed set has size `L=2e`.  For two words
`u,v`,

```text
|W_u intersect W_v|=L-dist(u,v).                       (1)
```

Use the greedy binary-code construction with minimum distance `t_XR+1`.
Each chosen word deletes at most the radius-`t_XR` Hamming-ball volume

```text
V(L,t_XR)=sum_(i=0)^t_XR binom(L,i),
```

so the resulting code has size at least `2^L/V(L,t_XR)`.

Because `t_XR<=L/32`, binomial monotonicity and
`binom(L,t)<=(3L/t)^t` apply.  The function
`t log(3L/t)` is increasing for `0<t<=L/32`, so

```text
V(L,t_XR)<=(t_XR+1)96^(L/32)<2^(7L/32+35).             (2)
```

Here `log2(96)<7` and `t_XR+1<2^35`.  Therefore the code has more than

```text
2^(25L/32-35)>2^127=16N^3                              (3)
```

words.  Equations `(1)` and the minimum distance give

```text
|W_u intersect W_v|<=L-t_XR-1=2e-t_XR-1=e+d,
```

which proves `(AC-1)`.

By definition, `e=t_XR+d+1`.  Also

```text
4e^2=N^2/16,
N(e+d)=N(N/4-t_XR-1)>=N^2/16,
```

because `t_XR+1<=3N/16`.  Hence the parameters lie in the residual wedge.
No step imposes locator equations, so the conclusion is exactly a route cut
for intersection-only arguments. QED.
