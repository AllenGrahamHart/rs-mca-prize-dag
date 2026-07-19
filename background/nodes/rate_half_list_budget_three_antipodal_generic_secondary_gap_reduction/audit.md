# Audit

The theorem is scoped to the maximal official generic floor. The identity
`v=h-3`, which creates exactly two terminal zero coefficients, is not the
degree arithmetic of the intermediate or above-floor strata.

The square root is normalized by constant term one. The unnormalized `C` is
determined only up to `C(0)`, matching the allowed rescaling of the pencil's
degree-drop direction.

The series `J` is not an independent input: it is computed from `E`, the
canonical `B`, and `1-z^d`. Formula `(2)` proves that its apparent division by
`z^(2h)` is exact for valid generic boundary data.

A tiny exploratory scan at subgroup orders `8,16,32` found non-coset
single-primary-gap examples at order `32`, so no intermediate rigidity is
inferred from one fourth-root coefficient. The scan is heuristic and is not
used in the proof.

The complete scan counts are `(single,double,coset-double)=(2,2,2)` at order
eight, `(0,0,0)` at order sixteen, and `(192,0,0)` at order thirty-two. It is
replayed by `verify_audit.py` under `ramguard tiny`.

The primary-only route also fails in the first larger divisibility analogue.
Over `F_193` at order `64`, the noncoset deleted-root exponents

```text
{0,1,3,62}={0,1,3,-2}
```

give exact fourth-root coefficients `(a_16,a_17,a_18)=(0,0,94)`. Common
subgroup scaling produces `64` distinct primary-gap quadruples. The secondary
series rejects the entire orbit: its two forbidden coefficients are
`102,24`, both nonzero. Since `193>d=64`, this already refutes primary
nonvanishing under the theorem chain's generic characteristic hypothesis.
At the first order-64 prime above the deliberately stronger threshold
`p>=d^2`, namely `p=4289`, the same exponent pattern instead has primary
triple `(2769,3151,2930)` and does not pass.

The strong threshold is not a uniform official premise. On the maximal
`B*=3` row, the field collapse gives either `q=p` with `p>=3*2^128`, or
`q=p^2` with only `p>2^64`, while `d=2^39`. A primary-only official attack
would therefore have to use these two arithmetic branches separately. This
is a route fence, not an official-row construction.

A complete bounded Modal scan of all `C(64,4)=635376` quadruples over each of
the first eight order-64 primes above `p>=d^2` found primary single-gap
counts `64,64,128,64,192,0,0,128` and no primary double gap. The exact output,
launcher, and hash-pinned checker are in
`experiments/prize_resolution/rate_half_list_order64_primary_gap_{modal,result,check}.*`.
This is high-characteristic route evidence, but absence of a hit at fixed
order is not theorem evidence for either growing official field branch.
