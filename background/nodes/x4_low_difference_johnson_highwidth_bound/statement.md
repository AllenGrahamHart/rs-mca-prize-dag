# Low-difference Johnson high-width bound

- **status:** PROVED
- **closure:** proof

Let `D` have size `N`, fix an `A`-subset `S0`, and fix integers `e>d>=0`.
Let `R_(e,<=d)(S0)` be any family of distinct `A`-subsets `S!=S0` such
that, writing

```text
C=S intersect S0,   P=S\S0,   Q=S0\S,
|P|=|Q|=e,          H=L_P-L_Q,
```

one has `deg H<=d`.  Then the changed sets `W_S=P union Q`, each of size
`2e`, satisfy

```text
|W_S intersect W_T|<=e+d       for distinct S,T.       (HJ-1)
```

Consequently, whenever `4e^2>N(e+d)`,

```text
|R_(e,<=d)(S0)|
 <=floor(N(e-d)/(4e^2-N(e+d))).                        (HJ-2)
```

For `N=2^41` and `d=1`, every width `N/4+1<=e<=N/2` has at most `N^2/16`
records.  There are at most `N/4` such widths, so for every base support and
every support-wise residual subfamily,

```text
sum_(e=N/4+1)^(N/2) D_(e,1)(S0) <= N^3/64.             (HJ-3)
```

Here `D_(e,1)` counts exact linear-difference records.  Thus the official
X4 `d=1` problem is reduced to the low-width interval

```text
t_XR+2<=e<=N/4.
```

This theorem does not bound that interval, any `d>=2` aggregate, or a
transported quotient tuple.

## Falsifier

Two records in the stated family with changed-set intersection above `e+d`,
a family exceeding `(HJ-2)` when its denominator is positive, or an official
high-width `d=1` aggregate above `N^3/64`.
