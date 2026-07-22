# WCL extended six-slot sparse divisor endpoints

- **status:** PROVED
- **closure:** proof
- **consumers:** the six extended WCL slot targets and
  `dli_wcl_zone_coverage`
- **dependency:** `dli_wcl_newton_short_window_exclusion`

Let `K` be a field of characteristic zero or characteristic greater than
`w`, containing `mu_M`. Let `M=2N` be the signed-root order at one of the six
extended-window slots, and let `w` distinct, antipodal-free roots
`rho_i in mu_M` satisfy

```text
p_1=p_3=...=p_(2ell-1)=0,       p_j=sum_i rho_i^j.       (XW1)
```

If `w=2r+1` is odd, common dilation uniquely normalizes
`product_i rho_i=1`. There are unique polynomials

```text
A(Y) monic of degree r,
B(Y) of degree at most r-ell,       B(0)=1,              (XW2)
```

such that the root locator and squared-root locator are

```text
F(X)=X A(X^2)-B(X^2),
G(Y)=Y A(Y)^2-B(Y)^2=product_i(Y-rho_i^2).               (XW3)
```

If `w=2r` is even, there are unique polynomials

```text
E(Y) monic of degree r,
B(Y) of degree at most r-ell-1,                          (XW4)
```

with

```text
F(X)=E(X^2)-X B(X^2),
G(Y)=E(Y)^2-YB(Y)^2=product_i(Y-rho_i^2).                (XW5)
```

In both cases

```text
G divides Y^N-1.                                        (XW6)
```

Conversely, every coefficient tuple in `(XW2)` or `(XW4)` satisfying
`(XW6)` reconstructs one antipodal-free relation in `mu_M`: at a root `y`
of `G`, use `rho=B(y)/A(y)` in the odd case and `rho=E(y)/B(y)` in the even
case. The denominators cannot vanish because `Y^N-1` is squarefree. Thus the
six relation problems are exactly the following fixed divisor problems,
modulo the unique common dilation in odd weight.

| slot | `M` | `N=2^m` | `w` | base variables `b` | divisor form |
|---|---:|---:|---:|---:|---|
| `(1,7)` | 512 | 256 | 7 | 5 | `YA^2-B^2`, `deg A=3`, `deg B<=2`, `B(0)=1` |
| `(1,8)` | 512 | 256 | 8 | 7 | `E^2-YB^2`, `deg E=4`, `deg B<=2` |
| `(2,8)` | 1024 | 512 | 8 | 6 | `E^2-YB^2`, `deg E=4`, `deg B<=1` |
| `(2,9)` | 1024 | 512 | 9 | 6 | `YA^2-B^2`, `deg A=4`, `deg B<=2`, `B(0)=1` |
| `(4,10)` | 2048 | 1024 | 10 | 6 | `E^2-YB^2`, `deg E=5`, `deg B=0` |
| `(4,11)` | 2048 | 1024 | 11 | 6 | `YA^2-B^2`, `deg A=5`, `deg B<=1`, `B(0)=1` |

Apply the monic repeated-squaring lift directly to each `G`. Put

```text
s=floor(log_2(w-1)),       k=m-s,
V_s=Y^(2^s),
V_t^2=V_(t+1)+GQ_t,        s<=t<m,
V_m=1.                                                    (XW7)
```

The pruned systems have `b+k(2w-1)-w` variables, `k(2w-1)` equations, and
maximum total degree three:

| slot | `s` | `k` | variables | equations |
|---|---:|---:|---:|---:|
| `(1,7)` | 2 | 6 | 76 | 78 |
| `(1,8)` | 2 | 6 | 89 | 90 |
| `(2,8)` | 2 | 7 | 103 | 105 |
| `(2,9)` | 3 | 6 | 99 | 102 |
| `(4,10)` | 3 | 7 | 129 | 133 |
| `(4,11)` | 3 | 7 | 142 | 147 |

Every one of these six ideals is the unit ideal over `Q`. Consequently each
slot has a nonzero integer straight-line certificate

```text
Delta=sum_a H_a E_a,                                    (XW8)
```

and every supporting finite characteristic divides any checked `Delta` for
that slot. Computing and factoring the six integers remains open; no slot is
promoted here.

For route sizing, a blind affine-Galois support census has at least the class
count in the final column below. It is the raw signed-support count divided
by the maximum affine-orbit size `M phi(M)=M^2/2`.

| slot | raw reduced signed supports | affine-class lower bound |
|---|---:|---:|
| `(1,7)` | 842,360,690,688,000 | 6,426,702,047 |
| `(1,8)` | 52,436,952,995,328,000 | 400,062,202,418 |
| `(2,8)` | 14,189,981,600,607,887,360 | 27,065,242,005,554 |
| `(2,9)` | 1,589,277,939,268,083,384,320 | 3,031,307,104,622,047 |
| `(4,10)` | 171,144,124,159,294,538,557,161,472 | 81,607,877,807,280,797,271 |
| `(4,11)` | 31,552,753,072,277,211,290,356,678,656 | 15,045,525,108,469,586,987,666 |

These are route fences, not lower bounds on actual moment-vanishing
relations. They rule out a blind support-orbit continuation as the intended
proof implementation and select the six fixed sparse certificates instead.
