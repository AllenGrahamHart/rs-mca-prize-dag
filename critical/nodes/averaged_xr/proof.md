# Proof: exact slope-resolved support-pair moment

Put `s=k+t`, and fix supports `S,T` of size `s`. Write
`c=|S cap T|` and `d=s-c`.

## Joint rank

Restrict the combined map `(Pi_S,Pi_T)` to words on `S union T`. Its kernel
consists of functions whose restrictions to `S` and `T` are evaluations of
degree-`<k` polynomials `P` and `Q` that agree on `S cap T`.

If `c<k`, the `c` agreement equations on `(P,Q)` are independent by the
Vandermonde rank theorem. The kernel therefore has dimension `2k-c`. Since
`|S union T|=2(k+t)-c`, the combined rank is `2t`.

If `c>=k`, the polynomial `P-Q` has at least `k` distinct roots and degree
less than `k`, so `P=Q`. The kernel has dimension `k`, and the combined rank
is

```text
2(k+t)-c-k = t+d.
```

Now `c<k` is equivalent to `d>t`, while `c>=k` is equivalent to `d<=t`.
Both cases are exactly

```text
rank(Pi_S,Pi_T)=t+min(d,t).                         (1)
```

Coordinates outside `S union T` are free and do not change the codimension,
so (1) holds for the maps on all of `F^D`.

## Fixed-slope pair probability

For fixed `z`, make the invertible linear change

```text
U=f+zg,  V=g.
```

Then `U,V` are independent uniform words. A support `S` contributes slope
`z` precisely when `U in K_S` and `V notin K_S`: under `U in K_S`, the
excluded event `V in K_S` is exactly the event that both original syndrome
vectors vanish.

Each `K_S` has codimension `t`. By (1), for a pair at distance `d`,

```text
Pr[U in K_S cap K_T] = alpha_d = q^(-t-min(d,t)).
```

Inclusion-exclusion gives

```text
Pr[V notin K_S and V notin K_T]
  = 1-2q^(-t)+alpha_d.
```

Independence of `U,V` proves the claimed product formula. When `d>=t`,
`alpha_d=q^(-2t)`, so the product is
`q^(-2t)(1-q^(-t))^2=p_z^2`.

## Restricted-family factorial moment

Let `A` be a deterministic family of `M` supports, let `X_z(A)` count its
supports contributing `z`, and let

```text
Delta_d(A)=#{(S,T) in A^2:S!=T, |S\T|=d},  1<=d<t.
```

Summing the exact ordered-pair probabilities gives

```text
E[X_z(A)(X_z(A)-1)]
 = (M(M-1)-sum_(d=1)^(t-1) Delta_d(A)) p_z^2
   + sum_(d=1)^(t-1) Delta_d(A)
       q^(-t-d)(1-2q^(-t)+q^(-t-d)).
```

The expression is independent of `z`. This is `C_t(A)` in
`averaged_slope_conversion` and completes the proof.

## Verification

`verify.py` independently constructs the interpolation matrices over several
prime fields, checks (1) for every support pair in each toy row, exhaustively
counts the two fixed-slope pair events on a small row, and checks the
pointwise occupancy inequality used by the consumer.
