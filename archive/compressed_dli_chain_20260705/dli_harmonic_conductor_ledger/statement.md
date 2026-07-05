# dli_harmonic_conductor_ledger

- **status:** TARGET
- **closure:** proof

## Statement
The REAL terminal DLI gap (Pro): the DLI harmonic expansion has LOW TOTAL
NORMALIZED CONDUCTOR MASS. The peak-mass/log-transfer machinery rewrites the
level-j discrepancy as Delta_j(M,lambda) <= sum_{omega in Omega_j(M)} |c_omega|
|S_omega(P_lambda)| with each S_omega a complete low-conductor Artin-Schreier/
Kummer sum; the required ledger bound is
    sum_j (1/L_j) sup_{M,lambda != 0} sum_{omega} |c_omega| cond(omega) sqrt(q) = o(t).
Then Deligne gives Delta_j = o(L_j), the truncated-log transfer gives DLI_j with
sum eps_j = o(t), closing dli -> ejm -> primitive core.

CRITICAL (why the poles alone don't suffice): ordinary Deligne is NON-SAVING at
the section scale — sqrt(q) = 2^128 dwarfs the section N = 2^41 by sqrt(q)/N =
2^87 (verified). A single complete Weil sum gives nothing; the estimate MUST come
from many small-conductor sums whose weighted total is o(t). The signed-midpoint
stress (eta*/L = 0.019 at mu_32, decreasing in N) is a LEDGER mass term, not a
pole singularity.

## Falsifier
A DLI harmonic expansion whose weighted normalized conductor total is NOT o(t)
(e.g. a low harmonic carrying Omega(t) conductor mass) — the geometric-mean DLI
route fails and the primitive core needs a different equidistribution mechanism.
