# Rate-half FPC5 `M=4,t=3` low-multiplier prefix ladder

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **upstream interface:** quotient/prefix flatness `(Q)`

Fix one LS6 atom and write

```text
E=Etilde,       e=deg E,       c=lc(E),
M=L_2L_3,       j=2ell-a,       s=ell-a.
```

Assume the low-multiplier range

```text
a<=e<=s.                                               (PL1)
```

Then the complete monic unguarded LS6 flat has an exact disjoint
parametrization

```text
Q in K[X], deg Q=e-a, lc(Q)=c,
R in K[X], deg R<=s-e,                                (PL2)

M Q=E T_Q+R_Q,       deg R_Q<e,
D=T_Q+R,             V=-R_Q+E R.                     (PL3)
```

For each fixed `Q`, the locators `D` form one ordinary monic locator-prefix
cell: all coefficients in degrees above `s-e` are fixed. Its nonleading
prefix depth is

```text
h_e=j-(s-e)-1=ell+e-1.                               (PL4)
```

If `K` has order `Q_0`, there are exactly `Q_0^(e-a)` fixed-`Q` cells. Their
coarse ambient-normalized split mass obeys the exact ladder cancellation

```text
Q_0^(e-a) * binom(n,j)/Q_0^(ell+e-1)
 =binom(n,j)/Q_0^(ell+a-1).                          (PL5)
```

At the bottom `e=a`, there is one prefix cell of depth `ell+a-1`.

The conditions `D|L_C` and `gcd(D,V)=1` only delete members from these cells.

## Scope

This is a coordinate and average-scale theorem. It does not bound the
maximum prefix fiber, justify summing maximum bounds with a field-sized loss,
or treat the high-multiplier range `e>s`. Closure requires a prefix-flatness
theorem whose gain per extra depth survives the `Q_0^(e-a)` ladder.
