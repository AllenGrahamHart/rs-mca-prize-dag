# Linear-difference projection codegree bound

- **status:** PROVED
- **closure:** proof

Let `D` be a finite set of size `N` in a field, fix an `A`-subset `S0`,
and let `e>=2`.  Consider the fixed-base linear-difference incidences

```text
Q subset S0,              P subset D\S0,
|P|=|Q|=e,                L_P-L_Q=aX+b,    a!=0.       (PC-1)
```

For a fixed added set `P`, the number of possible removed sets `Q` is at
most

```text
floor(A(e-1)/(e^2-A))                                      (PC-2)
```

whenever `e^2>A`.  Dually, for a fixed `Q`, the number of possible `P` is
at most

```text
floor((N-A)(e-1)/(e^2-(N-A))).                            (PC-3)
```

whenever `e^2>N-A`.

At every official X4 base row,

```text
N=2^41,  128<=log2(q)<256,
t=t_XR=min{j>=0:j log2(q)>=log2 binom(N,N-K-j)+128},
K/N in {1/2,1/4,1/8,1/16},
```

one has `t>=2^31`.  Every `d=1` record has `e>=t+2`, so both denominators
above are positive and both projection codegrees are at most `1024`.

Consequently, at a fixed residual base support the `d=1` population is at
most `1024` times either its distinct-`P` projection or its distinct-`Q`
projection.  This is a bounded-multiplicity reduction, not a bound on either
projection and not a payment of the `16N^3-1` primitive allowance.

## Falsifier

Two distinct fixed-`P` incidences whose removed sets meet in at least two
points, the dual fixed-`Q` event, an official corridor with `t<2^31`, or an
official `d=1` projection fiber containing at least `1025` records.
