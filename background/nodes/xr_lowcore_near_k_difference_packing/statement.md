# XR low-core near-K oriented-difference packing

- **status:** PROVED
- **consumer:** `xr_lowcore_spread_heart`

Let `mathcal F` be a family of distinct `a`-subsets of an `N`-set with

```text
a=K+h,       H=h+1,
|S intersect T|<=K-1=a-H       for distinct S,T in mathcal F.    (NK1)
```

For one nonzero oriented indicator difference `(X,Y)` of width `t`, use the
residual fiber from `xr_lowcore_shift_pair_terminal_fiber_bound`:

```text
R_(X,Y)={I: X union I,Y union I in mathcal F},
|X|=|Y|=t,       |I|=a-t.                              (NK2)
```

Put

```text
c=K-t,       v=N-2t=N-2K+2c,       w=a-t=H+c-1.       (NK3)
```

For every repeated width `t<=K-1`, so `c>=1`,

```text
|R_(X,Y)|
 <=R_c:=floor(binom(N-2K+2c,c)/binom(H+c-1,c)).        (NK4)
```

Indeed, two distinct residuals intersect in at most `c-1`, so no `c`-subset
can occur in two residuals.

If `M=|mathcal F|` and `C` is any set of positive codimensions, let `E_C` be
the oriented-difference energy from widths `t=K-c`, `c in C`. Then

```text
E_C<=max_(c in C) R_c M(M-1).                         (NK5)
```

Consequently, if `N,H<=n`, `M>8n^3`, and `max R_c<=8n`, then

```text
E_C<M^3/n^2.                                          (NK6)
```

Thus these widths are below the registered P-B high-energy threshold in one
aggregate charge; the theorem does not merely give a per-difference bound.

## Official prefixes

For the six clean-rate rows, `(NK6)` pays the following maximal consecutive
prefixes `1<=c<=C_0` by this exact bound:

| row | `H` | `C_0` | `R_(C_0)` | `R_(C_0+1)` |
|---|---:|---:|---:|---:|
| RowC `1/4` | `6` | `2` | `6,327` | `411,273` |
| RowC `1/8` | `6` | `1` | `128` | `14,171` |
| RowC `1/16` | `4` | `1` | `224` | `40,455` |
| prize `1/4` | `8,589,934,594` | `6` | `4,398,046,497,508` | `562,949,951,166,976` |
| prize `1/8` | `8,589,934,594` | `5` | `260,919,262,630` | `50,096,498,384,811` |
| prize `1/16` | `4,294,967,298` | `4` | `40,282,095,485` | `18,046,378,752,308` |

Here `n=2^10` on RowC, `n=2^41` on the prize rows, and the threshold is
`8n`. The unfloored ratios in `(NK4)` are increasing in `c` on these rows,
so the displayed next failure makes each prefix maximal for this payment.
The paid codimension sequence is exactly `2,1,1,6,5,4` in table order.

The unresolved repeated-difference ranges are narrowed from
`H<=t<=K-1` to `H<=t<=K-C_0-1`. No bound on the number of difference types,
no lower bound on total energy, no CAP25 locator-SPI estimate, and no P-B
slope-count conclusion is claimed.
