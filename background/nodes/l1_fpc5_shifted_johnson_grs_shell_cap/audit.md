# Audit

The main scope risks were checked explicitly:

1. The target shell is dimension `K+1`; Haboeck is applied to the adjacent
   dimension-`K` code, with reduced rate `(K-1)/N`.
2. The deep-point integer-radius gate is `d<=H-1`, not a real-radius
   approximation.
3. MCA supplies CA only in the direction `CA<=MCA`.
4. Fixed-background charts cost `binom(b,u)`; that factor is retained in both
   the theorem and every official threshold.
5. The strict field denominator `q-N-KQ_m` is tested before any ceiling.
6. The official replay separates the new `J_fix<=0` cells from cells already
   paid by the ordinary fixed-background Johnson theorem.

The primary verifier uses exact interval enumeration and binary threshold
search. The independent audit scans every candidate defect degree directly
from the printed `(PF6)` inequalities and checks adjacent `m` failures and the
rounded power-of-two field thresholds.
