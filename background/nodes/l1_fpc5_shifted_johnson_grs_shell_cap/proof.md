# Proof: FPC5 shifted-Johnson GRS shell cap

First suppose `u<0`. The owner-free FPC5 Hankel chart has `h-d-1` recurrence
rows, so its total syndrome-check count is

```text
D=d+(h-d-1)=h-1=H-1.
```

The GRS syndrome-shell theorem identifies its primitive locators with an
exact radius-`d` shell of

```text
C+=RS[F,Core,N-D]=RS[F,Core,K+1].                    (1)
```

There is one such chart, giving `W=1`.

Now suppose `0<=u<=b`. For each required `u`-set `R` of background points,
the fixed-background chart has `ell-1` recurrence rows. Hence

```text
D=d+ell-1=H-1,
```

and its exact shell is again the code in `(1)`. The fixed-background
incidence theorem covers the full cell by summing these chart bounds over the
`W=binom(b,u)` possible sets `R`. It is a union bound with the correct
incidence multiplicity; no chart is silently discarded.

Let `C=RS[F,Core,K]`, the adjacent subcode of `(1)`. In the degree-at-most
convention used by Haboeck, `C` has reduced rate

```text
rho=(K-1)/N.
```

At Haboeck parameter `m`, the agreement threshold is

```text
(1+1/(2m))sqrt(N(K-1)).                              (2)
```

Condition `(SJ3)` says exactly that the shell agreement `a=N-d` is at least
`(2)`. Therefore the shell radius `d/N` is no larger than Haboeck's radius.
Support-wise MCA monotonicity and the imported theorem give an MCA bad-slope
numerator at most `Q_m` at radius `d/N`. The real bound can be floored because
the numerator is an integer. Every CA-bad slope is MCA-bad: CA-farness rules
out any common explaining support, which is precisely enough for the
support-wise MCA event. Thus the CA numerator of `C` is also at most `Q_m`.

The deep-point integer-radius gate is automatic. In either chart,

```text
N-K-1=H-1>=d,                                        (3)
```

where the owner-free inequality is the nonnegative Hankel-row condition
`d<=h-1`, and the fixed-background inequality follows from `H=d+ell`.
Condition `(SJ4)` is the strict denominator gate in the self-contained
deep-point conversion. Applying its integer-numerator corollary to `C` and
`C+` proves that each chart contains at most `L_m(q)` shell points.

There is one chart in the first branch and `binom(b,u)` charts in the second.
Summing their bounds proves `(SJ5)`. Equation `(SJ6)` is then immediate.
QED.
