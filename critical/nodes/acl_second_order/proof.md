# acl_second_order proof/evaluation

The task of this node is to turn the quotient-side antipodal class estimate
from an interval into a numeric per-rate input for the corridor ledger.

The evaluated input is:

```text
Acl_tot(N') = (3^(N'/2) + 1) / 2
```

at the rho = 1/2 reference, together with the size-restricted class count from
the certified `thm:exactcount` formula.

The resulting grid-step contributions are:

```text
rate 1/4:  X_acl = +0.0497
rate 1/8:  X_acl = +0.0164
rate 1/16: X_acl = -0.0056
```

These are the requested second-order numeric terms. They are also a negative
result for the original hope that the ACL term would close the clean corridors:
rate 1/8 remains short by `0.00707` grid steps, and the rate 1/16 finite-N'
term widens rather than narrows the corridor. Thus the node is proved as a
computation, with a negative corridor verdict.
