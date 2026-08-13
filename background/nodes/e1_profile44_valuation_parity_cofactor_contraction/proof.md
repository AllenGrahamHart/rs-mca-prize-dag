# Proof

Reduce the four odd profile coefficients modulo two. Their support polynomial

```text
P(X)=sum_(e in T) X^e in F_2[X]
```

has `(X+1)`-multiplicity `mu`. Modulo `X^128-1=(X+1)^128`, the parity of the
negacyclic autocorrelation is `P(X)P(X^-1)`. Hence its positive-half weight
is exactly `q`.

Both quantities are invariant under translating `T`. Fixing one support
point at zero, the pinned census exhausts all

```text
C(127,3)=333375
```

normalized supports. It computes `mu` by the Hasse-derivative criterion and
`q` by a separate folded-lag mask. The exact joint table in
`certificate.json` gives `(P44-P1)`.

Since every `A_d` is an integer,

```text
E=sum_d A_d^2=q mod 4.                                 (1)
```

The parent excludes `E<=4`. For `q=2,4,6`, the least integer at least five
satisfying (1) and `E>=q` is respectively `6,8,6`. In every case `E>=6`,
proving `(P44-P2)`.

The parent's energy-adaptive majorant at variance `V=12` is

```text
U_12=20^64 exp(-16/5)(8/5)^(16/3).                    (2)
```

The same monotonicity proof makes (2) valid for every `V>=12`. Cubing and
using exact degree-`27` Taylor bounds for `e^(48/5)` proves

```text
853574 P < U_12 < 853575 P,
P=B_P 2^128.                                          (3)
```

Thus an official collision in a branch from `(P44-P1)` cannot have
`m>=853575`. Reconstructing the exact parent list and applying this
branchwise ceiling removes precisely the twelve values in the statement and
leaves `645`. QED.
