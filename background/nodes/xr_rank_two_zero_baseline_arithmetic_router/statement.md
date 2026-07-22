# XR rank-two zero-baseline arithmetic router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_maxwell_collision_defect_identity`,
  `xr_higher_rank_rank_two_shell_maxwell_router`, `xr_target_budget_audit`

Use a rank-two relation whose `t>=4` active rows are all blocks of one
minimal Maxwell core. Put

```text
D=d+1,       Z=sum_i z_i,
D_0=t h+(t-2)((t-1)D-2Z),                           (ZB1)
```

in the notation of the shell router and collision-defect identity. Suppose
the exact shell baseline is zero: `D_0=0`.

At every clean XR row the reserve `h=A-k` is odd. There is therefore a
divisor `s|h` such that

```text
t=2s+2,       D is even.                             (ZB2)
```

In particular every zero-baseline full-core relation has even active-row
arity and odd shell depth `d`; a five-row relation is impossible.

All defect charges vanish:

```text
I=sigma=H=0.                                        (ZB3)
```

Thus no extension reuses an active zero, every pair budget is saturated,
and every outside extension point belongs to one or two rows. If `P` and `Q`
are respectively the numbers of outside points of multiplicity one and two,
then

```text
Z = t h/(2(t-2))+(t-1)D/2,
Q = (t-1)(t h/(t-2)-D)/2,
P = ((t-3)D-t h/(t-2))/2,
P+Q=t h/2-D.                                        (ZB4)
```

Consequently

```text
L=t h/(t-2)=h+h/s,
r=((h-h/s)/2) mod (t-3),

D >= even_ceil max{
       t h/((t-3)(t-2)),
       t(h+2(t-2))/((t-2)(t+1)),
       (L+2tr)/(t-3)
     },
D <= L,
a >= Z-D = (h+h/s+(2s-1)D)/2.                      (ZB5)
```

Here `even_ceil` means the least positive even integer satisfying every
displayed lower bound. The second lower bound is the row-degree capacity
`Z<=t(D-1)`. The third is the exact private-point congruence: every row's
private count is congruent to `r` modulo `t-3`. The inherited flat-nullity
scope also has `a<=k`, so arities whose rank floor exceeds the row dimension
are empty.

The exact official arithmetic gives:

| rows | `h` | arities not arithmetically excluded | necessary lower bound on `a` |
|---|---:|---|---:|
| RowC `1/4,1/8` | `5` | `4,12` | `10` |
| RowC `1/16` | `3` | `4,8` | `6` |
| prize `1/4,1/8` | `2^33+1` | `15` divisor arities | `8,601,474,050` |
| prize `1/16` | `2^32+1` | `2` divisor arities | `4,302,648,690` |

For the two large reserve classes the tuples minimizing this necessary rank
bound are

```text
(2049,4100,2101250),       (641,1284,3359586).       (ZB6)
```

The four-row case collapses completely:

```text
t=4  =>  D=2h, a>=2h, z_i=h for all i, T_i=empty.   (ZB7)
```

Hence its four selected blocks are exactly the complements in `X` of four
disjoint `h`-point zero fibers, and every pair intersection is exactly `a`.

This theorem does not count the surviving even-arity records, treat a
strictly negative baseline, promote a proper local circuit to a full core,
classify trade rank at least three or nonuniform cells, or prove P-A.
