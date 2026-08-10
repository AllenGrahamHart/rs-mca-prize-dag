#!/usr/bin/env python3
"""T2 test: the DISTANCE-1 received word Y = f + c(X^n-1)/(X-u).

Its normalized word class at maximal slack delta = m-1 is
W(z) = sum_{j=0}^{m} u^j z^j.  Predicted F_SUBSET = C(n-1, a), F_LIST = 1.
Measured with the BANKED round-27 instrument (nf_probe_copy.probe),
unmodified, imported from the scratch copy.
"""
import json, sys
from math import comb
import nf_probe_copy as NP

out = sys.argv[1] if len(sys.argv) > 1 else None
res = []
for n, qs in ((8, (73, 97, 113)), (16, (10177, 12289))):
    k = n // 2
    a = k + 1
    m = n - a
    delta = m - 1
    for q in qs:
        g = NP.find_gen(q, n)
        D = [pow(g, i, q) for i in range(n)]
        for ui in (0, 1, 3):
            u = D[ui]
            W = [pow(u, j, q) for j in range(m + 1)]
            r = NP.probe(n, q, 1, delta, W, D, g)
            r.update(n=n, q=q, delta=delta, u_index=ui,
                     pred_F_SUBSET=comb(n - 1, a), PLATEAU=comb(n // 2 - 1, n // 4))
            r["T2_hit"] = (r["F_SUBSET"] == comb(n - 1, a) and r["F_LIST"] == 1)
            res.append(r)
            print(json.dumps(r), flush=True)
if out:
    with open(out, "w") as f:
        json.dump(res, f, indent=1)
