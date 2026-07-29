# L1 Mersenne HNF payoff-scope router

- **status:** PROVED
- **consumer:** `l1_mixed_petal_amplification`
- **role:** quantify exactly what a closure of the colored-Frobenius HNF
  endpoint buys, before further chamber expansion

After the official checkpoint atlas, maximal-value exclusion, broad-row
periodicity exclusion, and the complete `m=4,h=3` exclusion, the unresolved
minimum-width `t=p` split-pencil obligations on the nine Mersenne rows are:

| `m` | rows | remaining `h` | row/degree cells |
|---:|---:|---:|---:|
| 4 | 4 | 2 | 4 |
| 8 | 4 | 2,...,7 | 24 |
| 16 | 1 | 2,...,15 | 14 |

Thus there are exactly

```text
4+24+14=42                                             (HPR1)
```

row/degree cells which must be either excluded or assigned to an already
paid owner. The embedded antipodal family is compatible only with even `h`.
It can occur in 23 of these cells; the other 19 cells have odd `h`.

A complete `h=7` close on all four `m=8` rows removes four cells. A complete
`h=15` close on the `m=16` row removes one more. Hence closing both
next-to-maximal degrees changes the obligation count only as

```text
42 -> 37,             odd cells 19 -> 14.              (HPR2)
```

The exceptional `J_*=0`, cubic `3+2+1` role chart is a proper subchart of
the `m=8,h=7` order-one cell. Closing it alone closes no row/degree cell;
the other order-one multiplicity and color-degree charts must also be paid
or excluded. The already proved order-zero exclusions do not change this
fact.                                                        (HPR3)

For one Mersenne row `n=m(p+1)`, one degree `2<=h<m`, and one checkpoint
depth `p<=d<=2p-2`, put

```text
u_(m,h)=(m-h)p+m,
ell_(m,h,d)=(m-h+1)p+m-d.
```

The complement census supplies the explicit term

```text
B_(m,h,d)=binom(h,2)
  floor(binom(m(p+1),ell_(m,h,d))
        /binom(u_(m,h),ell_(m,h,d))).                 (HPR4)
```

A full cell exclusion replaces this term by zero. In particular, the
potential terms removed by complete next-to-maximal closures are

```text
B_(8,7,d)=21 floor(binom(8(p+1),2p+8-d)
                         /binom(p+8,2p+8-d)),
B_(16,15,d)=105 floor(binom(16(p+1),2p+16-d)
                           /binom(p+16,2p+16-d)).      (HPR5)
```

These are census caps, not proved attained masses.

Even if every one of the 42 residual cells is excluded or paid and the
explicit embedded family is removed by its owner, the immediate generic
packing consequence is only deletion of the width `t=p` stratum. For an
`a`-set fiber this changes the packing subset size from `a-p+1` to `a-p`:

```text
C_p     =floor(binom(n,a-p+1)/binom(a,a-p+1)),
C_(p+1) =floor(binom(n,a-p)  /binom(a,a-p)).           (HPR6)
```

Before floors, the exact improvement factor is

```text
[binom(n,a-p+1)/binom(a,a-p+1)]
 /[binom(n,a-p)/binom(a,a-p)]
 =(n-a+p)/p < m+2 <=18.                               (HPR7)
```

Therefore the HNF lane is a finite, valid pruning lane, but not a standalone
closure route for L1. Widths above `p` and the global Toeplitz/Pade or
aggregate first-owner payment remain necessary. No HNF subchart should be
reported as a critical payoff unless it closes a complete `(m,h)` cell or
supplies an independently budgeted owner payment.
