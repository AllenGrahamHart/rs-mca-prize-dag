# `A=1` core-one active-core two-sided partition

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_trace_nonvanishing`

Retain either of the two active systems `(ETN6)`. Put

```text
z=deg X_0 in {0,1},       R_X=P_XX_1=G_X/X_0,
deg R_X=D_0-z.                                         (ATP1)
```

Every clean supported slope `gamma` gives an exact squarefree partition

```text
Q(gamma;X) A_a(gamma;X)=R_X,                          (ATP2)
deg_X Q(gamma;X)=r,
deg_X A_a(gamma;X)=D_0-z-r.                           (ATP3)
```

The two factors in `(ATP2)` are squarefree, split over `D\S`, and have
disjoint root sets. In particular, every clean specialization of `A_a`
attains the global degree

```text
deg_X A_a=D_0-r-z.                                    (ATP4)
```

Every saturated residual domain row `x`, meaning `P_X(x)=0`, gives the dual
exact squarefree partition

```text
Q(U,V;x) V_a(U,V;x)=P,                                (ATP5)
deg_(U,V)Q(U,V;x)=e_*,
deg_(U,V)V_a(U,V;x)=T-e_*.                            (ATP6)
```

The two factors in `(ATP5)` are squarefree, split over the full supported set,
and have disjoint roots. Thus every saturated specialization of `V_a`
attains its global parameter degree.

There are exactly `T-D_*` partitions of type `(ATP2)` and `D_0-c` partitions
of type `(ATP5)`. The active bad-row clean-incidence count is exact. If
`E_bad` is the number of bad rows at which the exceptional supported slope is
a root (zero when `D_*=0`), then

```text
sum_(x:X_1(x)=0) a_x=c e_*-C_*-E_bad,                 (ATP7)
```

because a zero-trace row, when present, has no clean root. Explicitly,

```text
D_*=0: sum a_x=(c-1)e+(5-c)b+1;
D_*=1: sum a_x=(c-1)e+(5-c)b-E_bad.                   (ATP8)
```

Every summand in `(ATP7)` is positive because every `X_1` trace is active.
This theorem supplies a degree-tight two-sided divisor-partition interface;
it does not exclude either active system.
