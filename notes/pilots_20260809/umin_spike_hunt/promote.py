#!/usr/bin/env python3
"""Triage (PREREG section U2): group RESSIEVE hits by prime, compute the
EXACT low-weight profile AU[U], and rank by

    PREDCR(p) = 1 + BONUS(p)/(1+H(p)),  BONUS = sum_U AU[U] 2^-U,
    H = (2^N-1)/p^kappa

(E[mass from weights > Umax] = H exactly, so PREDCR is the conditional mean
of CRATIO given the low-weight profile).  Promote iff PREDCR >= 1.30 or
UMIN <= 6.  Exact AU is computed by twisting every hit to a genuine kernel
vector at p (rs.verify_hit) and taking the union of its mu_64 orbit --
so the Galois multiplicity of the f-enumeration is divided out exactly,
not assumed.

  N=32 KAPPA=1 EXACT=200 tools/ramguard local -- python3 promote.py
"""
import glob
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rs                                                      # noqa: E402

N = int(os.environ.get("N", "32"))
KAPPA = int(os.environ.get("KAPPA", "1"))
EXACT = int(os.environ.get("EXACT", "200"))     # how many top cells get exact AU
PAT = os.environ.get("PAT", "HITS.N%d.U*.s*.tsv" % N)
OUT = os.environ.get("OUT", "CANDS.N%d.k%d.tsv" % (N, KAPPA))

by_p = {}
nline = 0
for fn in sorted(glob.glob(os.path.join(HERE, PAT))):
    for ln in open(fn):
        f = ln.split("\t")
        p = int(f[0])
        U = int(f[1])
        S = tuple(int(x) for x in f[2].split(","))
        t = int(f[3])
        nline += 1
        d = by_p.setdefault(p, {})
        d.setdefault(U, []).append((S, t))
print("read %d hits over %d distinct primes" % (nline, len(by_p)), flush=True)

HNUM = (1 << N) - 1


def predcr_est(p, d):
    """cheap ranking pass: Galois multiplicity of the f-enumeration is 2N/2 =
    N generically (Res is Galois-invariant), and each orbit has 2N vectors."""
    bonus = 0.0
    for U, lst in d.items():
        bonus += (2 * N) * (len(lst) / float(N)) * 2.0 ** (-U)
    H = HNUM / float(p ** KAPPA)
    return 1.0 + bonus / (1.0 + H), H


rank = sorted(by_p.items(), key=lambda kv: -predcr_est(kv[0], kv[1])[0])
print("ranked; computing EXACT AU for the top %d" % EXACT, flush=True)

rows = []
t0 = time.time()
for i, (p, d) in enumerate(rank):
    umin = min(d)
    est, H = predcr_est(p, d)
    exact = None
    if i < EXACT:
        reps = []
        for U, lst in d.items():
            for (S, t) in lst:
                v = rs.verify_hit(N, p, S, t, kappa=KAPPA)
                assert v is not None, "hit %d U=%d failed re-verification" % (p, U)
                reps.append((U, v[1]))
        AU = rs.au_from_reps(N, reps)
        bonus = sum(a * 2.0 ** (-U) for U, a in AU.items())
        exact = (AU, bonus, 1.0 + bonus / (1.0 + H))
    sig = N - KAPPA * math.log2(p)
    rows.append((p, sig, umin, est, H, exact))

with open(os.path.join(HERE, OUT), "w") as fh:
    fh.write("p\tSIGMA\tUMIN\tH\tPREDCR_est\tPREDCR_exact\tBONUS\tAU\n")
    for (p, sig, umin, est, H, ex) in rows:
        if ex is None:
            fh.write("%d\t%.6f\t%d\t%.6f\t%.6f\t\t\t\n" % (p, sig, umin, H, est))
        else:
            AU, bonus, pc = ex
            fh.write("%d\t%.6f\t%d\t%.6f\t%.6f\t%.6f\t%.6f\t%s\n"
                     % (p, sig, umin, H, est, pc, bonus,
                        ";".join("%d:%d" % (u, AU[u]) for u in sorted(AU))))
print("wrote %s  (%.1fs)" % (OUT, time.time() - t0), flush=True)
for (p, sig, umin, est, H, ex) in rows[:25]:
    print("  p=%-13d sigma=%+.4f UMIN=%d  PREDCR=%.4f %s"
          % (p, sig, umin, ex[2] if ex else est,
             ("AU=" + ";".join("%d:%d" % (u, ex[0][u]) for u in sorted(ex[0])))
             if ex else "(est)"), flush=True)
