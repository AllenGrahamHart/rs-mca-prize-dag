# Proof - L1 intrinsic quotient source-chart census

Fix a complete-fiber core `C` of size `k-1` and a disjoint complete petal
`T` of size `ell`. If two degree-below-`k` polynomials satisfy `(IC2)`, their
difference has at least

```text
|C union T|=k-1+ell>=k
```

distinct roots. Its degree is at most `k-1`, so the difference is zero. This
proves source-member uniqueness for every fixed `(C,T)`.

Now assign each of the `L` fibers a role from `(IC3)`. The core and petal
sets are determined. For every petal, its source member is either the unique
polynomial from `(IC2)` or does not exist. Conditions that source members have
the required common core, distinct labels, exact petals, and maximality only
remove assignments. Hence there are at most `3^L` canonical source charts,
proving `(IC4)`.

At the cutoff,

```text
L=n/ell<=log_2 n/c_0,
```

so

```text
3^L=2^(L log_2 3)<=2^(log_2(n) log_2(3)/c_0)
    =n^(log_2(3)/c_0),
```

which is `(IC5)`.

Order the at most `log_2 n+1` intrinsic dyadic scales, then the finite role
assignments at each scale. Assign every contributor to its first carrying
chart. First-match classes are disjoint and each is a subset of its chart's
complete contribution, so a uniform `n^B` per-chart bound sums to `(IC6)`.
Applying the explicit per-chart bipolar bound gives the stated fixed-box
corollary.

