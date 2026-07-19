# Rich-fiber route-selection result

Modal run `ap-ttBP0c2JCopfqrGmGtvnI2` exactly inspected the row

```text
n=8192, p=67657729.
```

The largest product fiber on nonidentity quotient support has

```text
P(t)=20, R(t)=1, t=40697698.
```

Its ten unordered exponent pairs are emitted by `rich_fiber_modal.py`. The
unique quotient witness has root exponents `(4914,2457)`; notably
`4914=2*2457`, so this parameter is the telescoping value
`t=(1-q^2)/(1-q)=1+q` for `q` of order `8192`.

The result does not prove a uniform inverse relation between `P` and `R`, but
it shows that the largest observed pointwise fiber carries minimal quotient
weight. This motivated replacing M35 on the critical path by the truncated
weighted excess `f3_h3_mobius_excess_half`.

A second replay, `ap-sTFOJvu8xxKqcxPrUt9l7r`, measured the exact factorial
collision moment

```text
sum_(t!=1)P(t)(P(t)-1)R(t)=132310328=1.971577525*n^2,
```

and `X_35=0`. This calibrates the background `FM69` route; it remains evidence.

A third replay, `ap-mQIrCagX2naqUwhjODqvHz`, split that moment into the
universal swapped-representation family and its complement:

```text
swap moment     = 66499900 = 0.990925729*n^2,
non-swap moment = 65810428 = 0.980651796*n^2.
```

Thus deleting swaps removes almost exactly half of the observed factorial
moment, but the non-swap part is still macroscopic.  This selects the proved
`f3_h3_nonswap_moment_68` reduction as a cleaner analytic route; the replay is
calibration, not proof of its required uniform `68n^2` estimate.

A cutoff-aware replay, Modal run `ap-yTeGirrfOykwHEmzAcuamR`, measured the
strictly weaker moment that the current critical compiler actually consumes:

```text
full non-swap moment                 = 65810428
single finite-characteristic term   = 41778976
joint quotient-excess term          = 24031452
targets with P(t) >= 19              = 2
S_ns^rich                           = 720
X_18                                = 4
```

Thus `68X_18=272<=720`, as required by the exact compiler, while deleting the
irrelevant `P(t)<=18` fibers reduces the observed sufficient moment by more
than 90,000-fold. Both rich targets have `P(t)=20` and `R(t)=1`. This is strong
route-selection evidence for attacking the simultaneous rich locus directly;
it is not a uniform proof over the official corridor.

Modal run `ap-qQ3yscqJjP1LR8yH9nqI5y` additionally replayed the proved
fifth-orbit compiler. The untruncated fifth orbit moment is `17914`, while
the consumer-aware restriction is

```text
M_5^rich=2*binom(10,5)=504.
```

This is `504/8192^2<0.00000752`, against the sufficient uniform allowance
`(34650/17)n^2`. The separation is evidence for a distinct-configuration
Stepanov route; no extrapolation to untested rows is consumed.

Paired-intersection route selection used Modal apps
`ap-Iw8T7ThqAqRZBGkXdzZWFc` and `ap-JD3AwzFHGglY5LEXLqtx4M`. All first twelve
boundary primes at `n=8192` and first four at `n=16384` completed exhaustively.
Their maxima were

```text
max(P+2R) in {24,26,28},
max(P+R)  <= 22,
max(P R)  <= 98.
```

Since `P+2R=I_inv+2I_aff-2`, the observed paired-PGL2 maximum is at most 30,
against the sufficient target 39. This is evidence only; it motivates the
exact reduction `f3_h3_pgl2_pair_identity` rather than a status change.
