# HGE4 primitive swap straight-line certificate lift

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_primitive_swap_half_order_square_descent`

Fix an official row and write

```text
N=n/2=2^m,       h=2d+1,       F(Y)=Y T(Y)^2-c,
```

where `T` is monic of degree `d`. The half-order square descent says that the
swap branch is exactly the divisibility condition

```text
F(Y) divides Y^N-1.                                  (SLC1)
```

Put `V_0(Y)=Y`. Introduce `deg V_t<h` and `deg Q_t<=h-2` and impose

```text
V_t(Y)^2=V_(t+1)(Y)+F(Y)Q_t(Y),       0<=t<m,
V_m(Y)=1.                                             (SLC2)
```

Over every commutative base ring, the recurrence variables before the
terminal condition are uniquely determined. The resulting scheme is
isomorphic over `Z` to `(SLC1)`; it introduces and discards no components.
Every equation in `(SLC2)` has total degree at most three.

There is an exact pruned presentation. Set

```text
s_0=floor(log_2(h-1)),       k=m-s_0,       b=d+1.     (SLC3)
```

The first `s_0` remainders are fixed as `V_t=Y^(2^t)`. Starting at `t=s_0`
and substituting `V_m=1` gives

```text
variables = b+k(2h-1)-h,
equations = k(2h-1),
maximum total degree = 3.                              (SLC4)
```

For the smallest official order `n=8192`, the first three odd widths have

```text
h      variables      equations
5          88             90
7         127            130
9         149            153.                         (SLC5)
```

The base divisor scheme, and hence the straight-line scheme, has no point in
characteristic zero. Therefore, for every fixed `(N,h)`, there are a nonzero
integer `Delta_(N,h)` and integer polynomials `H_a` such that

```text
Delta_(N,h)=sum_a H_a E_a,                            (SLC6)
```

where the `E_a` are the pruned cubic equations. Every finite characteristic
supporting a swap divisor at `(N,h)` divides any checked `Delta_(N,h)`.

This theorem computes no `Delta_(N,h)`, supplies no uniform bound on its prime
divisors, and does not bound the number of swap or free unions. A coefficient
expansion of `Y^N mod F` and a blind Groebner run are not implied to be cheap.
