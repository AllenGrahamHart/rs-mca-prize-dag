# HGE4 non-full near-square straight-line lift

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_primitive_shift_pair_near_square_union_router`,
  `x24_char0_dyadic_descent`

Fix an official row `n=2^s` and a width `4<=h<=n/2`. Write

```text
S(X)=X^h+s_(h-1)X^(h-1)+...+s_1X+s_0,
D(X)=S(X)^2-a^2.                                    (NFS1)
```

The near-square union condition is exactly

```text
D(X) divides X^n-1.                                 (NFS2)
```

Among such divisors, the characteristic-zero full-fiber class is exactly

```text
s_1=...=s_(h-1)=0.                                  (NFS3)
```

Introduce selector variables `z_1,...,z_(h-1)` and impose

```text
sum_(j=1)^(h-1) z_j s_j=1.                          (NFS4)
```

Over every field, the projection of `(NFS4)` is precisely the non-full-fiber
locus. Therefore every primitive free or swap near-square union surviving
the full-fiber deletion lifts to this selector scheme.

Put `V_0=X`. As in the swap lift, impose

```text
V_t^2=V_(t+1)+DQ_t,       0<=t<s,
deg V_t<2h,               deg Q_t<=2h-2,
V_s=1.                                                (NFS5)
```

This repeated-squaring scheme is isomorphic over `Z` to `(NFS2)` before the
selector is added. Set

```text
r_0=floor(log_2(2h-1)),       k=s-r_0.               (NFS6)
```

After removing deterministic initial squarings and substituting `V_s=1`, the
single selector presentation has

```text
variables = k(4h-1),
equations = k(4h-1)+1,
maximum total degree = 3.                             (NFS7)
```

Equivalently, cover the locus by `h-1` charts. Chart `j` adds one inverse
`u_j s_j=1` and has

```text
variables = k(4h-1)-h+2,
equations = k(4h-1)+1.                               (NFS8)
```

At the smallest official order `n=8192`, the first widths have

```text
h     one-chart variables/equations     number of charts
4                 163/166                       3
5                 187/191                       4
6                 226/231                       5
8                 304/311                       7.    (NFS9)
```

The selector scheme and every chart have no characteristic-zero point.
Consequently each fixed `(n,h)` admits nonzero integer Nullstellensatz
certificates whose prime divisors contain every characteristic supporting a
non-full-fiber near-square divisor at that cell.

No certificate is computed. No uniform prime-factor bound, survivor count,
or HGE4 aggregate is proved. The selector variables are a coverage device,
not a one-to-one counting parameterization.
