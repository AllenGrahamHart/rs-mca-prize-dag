# Cycle 175: rate-half `A=1` nonreduced normalization collision (2026-08-12)

Normalization arithmetic removes every noncollision nonzero-jet profile
from the unshared nonreduced packet. If

```text
B=sum_b m_b b,       e_b=ord_b(t-tau),
s=ord_tau F_0,
```

then the exact contact divisors force

```text
e_b s=2m_b.
```

Because `deg B=2` and the two-jet gate gives `s>=2`, only three
normalization patterns survive. The smooth doubled-point pattern has
`s=4`, both jets zero, and Smith type `[4]`. The other two patterns have
`s=2`, a nonzero second jet, and total parameter ramification two above
`(tau,x_*)`; equivalently, `x_*` is an exact double root of
`Q(tau,X)`. A first-nonzero third jet is impossible.

```text
result:                  PROVED normalization/collision dichotomy
DAG delta after repair:  +1 PROVED leaf, 2 req edges, 1 evidence edge
critical status delta:   none
compute:                 three integer valuation patterns; no Modal spend
new assumptions:         unshared nonreduced minimum-gap packet
```

The remaining nonreduced obstruction is therefore the exact locator-root
collision. It has either one ramified normalization branch or two
unramified branches and still requires a source/Hankel exclusion or an
exact Smith classification.
