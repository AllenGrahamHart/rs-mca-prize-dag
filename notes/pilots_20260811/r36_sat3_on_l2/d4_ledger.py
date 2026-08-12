"""r36_sat3_on_l2 D4: the corrected B-side first-moment ledger and the
corrected (SAT3) realizability excess once e=m is priced at its true
dimension.  Stdlib only; writes only d4_results.txt in this directory."""
from math import log2, comb

OUT = "notes/pilots_20260811/r36_sat3_on_l2/d4_results.txt"
L = []


def say(s=""):
    L.append(str(s))


say("# d4_results — corrected ledgers")
say("")
say("## A. B-side first moment for (SAT3)-on-(L2) at m=2, domain mu_32")
say("   log2 E(T) = 18*log2 q + log2 C(q+1,T) + T*[log2 C(32,7) - 7*log2 q]")
say("   18 = the (L2) good component dimension (anchor 1, re-derived here);")
say("   anchor 2 used (m+1)(rho+1)-4 = 20, so the gap is exactly 2*log2 q.")
say("   log2 C(32,7) = log2 %d = %.4f" % (comb(32, 7), log2(comb(32, 7))))
for q in (97, 193, 257, 641, 769):
    lq = log2(q)
    per = log2(comb(32, 7)) - 7 * lq
    row = []
    for T in range(1, 10):
        row.append((T, 18 * lq + log2(comb(q + 1, T)) + T * per))
    say("q=%-4d log2 q=%.4f  per-member term=%.3f" % (q, lq, per))
    say("      " + "  ".join("T=%d:%+.1f" % r for r in row))
    cross = [T for T, v in row if v < 0]
    say("      first T with log2 E < 0: %s ; log2 E(T=9) = %+.2f ; anchor-2 value = %+.2f"
        % (cross[0] if cross else "none", row[8][1], row[8][1] + 2 * lq))
say("")
say("## B. (SAT3) realizability excess, corrected for the mandatory e=m")
say("   banked (rh_sat3_realizability/REPORT.md:193-198):")
say("     params(m) = [4m(m+1)-1] + (4m+1) + 16m = 4m^2+24m")
say("     conds(m)  = T*rho - O = 16m^2-1-O ;  excess = conds-params = 12m^2-24m-1-O")
say("   (ERC2) (PROVED, exceptional_root_charge/statement.md:73) closes 1<=e<=m-1,")
say("   so (SAT3) forces e=m, i.e. the curve must lie on the (L2) good component,")
say("   whose dimension is 18 at m=2 (NOT the ambient 4m(m+1)-1 = 23).")
for m in (1, 2, 3, 4):
    T = 4 * m + 1
    rho = 4 * m - 1
    amb = 4 * m * (m + 1) - 1
    params = amb + T + 16 * m
    conds = T * rho
    say("  m=%d: ambient curve dim=%d  params=%d  conds(O=0)=%d  banked excess=%+d"
        % (m, amb, params, conds, conds - params))
say("  m=2 CORRECTED: ambient 23 -> (L2) good component 18 (codim 5, anchor 1 +")
say("     this round, two fields), so params 64 -> 59 and")
say("     excess = 63 - O - 59 = +4 - O, i.e. +4 at O=0 and +3 at O=1 (SAT2: O<=m-1=1).")
say("     The banked ledger's ONLY negative cell at m>=2 flips sign.")
say("")
say("## C. the packing ceiling arithmetic (banked (SAT4); re-derived)")
for m in (1, 2, 3):
    say("  m=%d: T*rho = %d ; m*N = %d ; slack = %d  (SAT4: sum_x(m-d_x)=1+O)"
        % (m, (4 * m + 1) * (4 * m - 1), m * 16 * m, m * 16 * m - (4 * m + 1) * (4 * m - 1)))
say("  so at every m the packing is tight to exactly ONE free slot: 16m^2-(16m^2-1)=1.")
say("")
with open(OUT, "w") as fh:
    fh.write("\n".join(L) + "\n")
print("\n".join(L))
