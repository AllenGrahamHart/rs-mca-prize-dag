"""D3b -- the WIDER-RADIUS full LP at G1 (k = 3 and, budget permitting, k = 4).
Round-22 f2_rlocality pilot, DRAFT ONLY.

The k = 4 (= 2R) system is 496 rows x 12870 columns and does not finish
inside the ramguard `local` wall limit with my from-scratch simplex; k = 3
(165 rows) does, and already shows the monotone effect of the radius.
"""
import math, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_lib as R
import lp_lib as LP

PASS, FAIL = [], []
def chk(tag, cond, msg):
    (PASS if cond else FAIL).append(tag)
    print(("PASS " if cond else "FAIL ") + tag + " :: " + msg)

cs = R.CSTAR
p1, S1, R1 = 17, 8, 2
out = {}
for k in (2, 3, 4):
    t0 = time.time()
    A, b, cost, ns = LP.build_full(p1, S1, k)
    print("k = %d : %d states, %d rows (build %.1fs)"
          % (k, ns, A.shape[0], time.time() - t0), flush=True)
    for c in (cs, 1.00):
        t1 = time.time()
        o = LP.full_lp_at(A, b, cost, S1, c)
        f = c / (-math.log2(o) / S1) if o > 0 else float("inf")
        out[(k, round(c, 6))] = (o, f)
        print("   c = %.4f : OPT_k = %.6e   FLOOR_k = %.4f   [%.1fs]"
              % (c, o, f, time.time() - t1), flush=True)

for k in (2, 3, 4):
    key = (k, round(1.0, 6))
    if key in out:
        chk("D3b.end%d" % k,
            abs(out[key][0] - float(p1) ** (-k * R1 / 2.0)) < 1e-9,
            "OPT_{k=%d}(1) = %.4e = p^{-k/2 * R} exactly -- the c = 1 layer "
            "costs NOTHING to any locality radius" % (k, out[key][0]))
ks = [k for k in (2, 3, 4) if (k, round(cs, 6)) in out]
fl = [out[(k, round(cs, 6))][1] for k in ks]
print("FLOOR_k(c*) at G1 by radius:",
      ", ".join("k=%d -> %.4f" % (k, f) for k, f in zip(ks, fl)))
chk("D3b.mono", all(fl[i] >= fl[i + 1] - 1e-9 for i in range(len(fl) - 1)),
    "FLOOR_k(c*) is non-increasing in the locality radius k: %s"
    % ", ".join("%.4f" % f for f in fl))
print("D3b SUMMARY: %d PASS, %d FAIL" % (len(PASS), len(FAIL)))
sys.exit(1 if FAIL else 0)
