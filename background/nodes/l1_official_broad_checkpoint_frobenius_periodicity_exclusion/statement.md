# L1 official broad-checkpoint Frobenius periodicity exclusion

- **status:** PROVED
- **role:** remove every broad-remainder higher-multiplicity minimum-width row
- **consumer:** `l1_mixed_petal_amplification`

Let `H=gamma<zeta>` be an official multiplicative coset of order `n` in
characteristic `p`. Suppose two disjoint `p`-point subsets `X,Y subset H`
have equal power sums through degree `p-1`. Write their exponent sets as
`I,J subset Z/nZ` and define

```text
A(T)=sum_(i in I) T^i-sum_(j in J) T^j in F_p[T]/(T^n-1).  (BFP1)
```

Then `A(zeta^a)=0` for `0<=a<p`. Since the coefficients lie in the prime
field, the zero set is closed under multiplication by `p` modulo `n`. Put

```text
S_(n,p)=union_(r>=0) p^r {0,...,p-1} mod n,
M_(n,p)=(Z/nZ) minus S_(n,p).                            (BFP2)
```

The exact official checkpoint atlas has seven `m=floor(n/p)>=3` rows with
`s=n-mp>16`. Their exhaustive orbit closures are:

| `n` | `p` | `ord_n(p)` | `m` | `s` | `|S|` | `|M|` | `gcd(M)` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 16384 | 5119 | 16 | 3 | 1027 | 14975 | 1409 | 4 |
| 32768 | 6143 | 16 | 5 | 2053 | 28159 | 4609 | 4 |
| 65536 | 12289 | 16 | 5 | 4091 | 57601 | 7935 | 4 |
| 65536 | 20479 | 16 | 3 | 4099 | 59903 | 5633 | 4 |
| 131072 | 40961 | 16 | 3 | 8189 | 122369 | 8703 | 8 |
| 262144 | 65537 | 4 | 3 | 65533 | 180225 | 81919 | 2 |
| 524288 | 65537 | 8 | 7 | 65529 | 352257 | 172031 | 2 |

Thus the Fourier transform of `A` is supported only on multiples of the
printed even integer `g=gcd(M)`. Fourier inversion makes the coefficient
word periodic with period `n/g`. Every coefficient orbit has size `g`, so
both its `+1` support and its `-1` support have size divisible by `g`. Their
sizes are both the odd prime `p`, a contradiction. Therefore

```text
no two complete p-point fibers exist on any of the seven rows.             (BFP3)
```

Consequently all seven broad-remainder `m>=3` rows have empty minimum-width
`t=p` first-checkpoint strata at every depth. Only the nine rows with

```text
s=m in {4,8,16},       n=m(p+1),                                  (BFP4)
```

retain a higher-multiplicity minimum-width endpoint. This theorem does not
bound those nine rows, widths above `p`, or the complete L1 fiber.
