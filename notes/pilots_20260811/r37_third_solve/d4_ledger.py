"""D4 - ledger reconciliation, the distance to T=3 over mu_32, and the (OV4)
consequence for the (SAT3) design. r37_third_solve. Appends to d4_results.txt.
"""
import math, time
from math import comb, log2

def main():
    out=["","=== RUN d4_ledger %s ==="%time.strftime("%Y-%m-%dT%H:%M:%S")]
    C=comb(32,7)
    out.append("C(32,7) = %d = 2^%.2f"%(C,log2(C)))
    out.append("")
    out.append("A. LEDGER (round-36 form) log2 E(T) = 18 log2 q + log2 C(q+1,T) + T[log2 C(32,7) - 7 log2 q]")
    for q in (97,193,257,641,769):
        row=[]
        for T in (1,2,3,4,5):
            v=18*log2(q)+log2(comb(q+1,T))+T*(log2(C)-7*log2(q))
            row.append("%+.1f"%v)
        out.append("  q=%-4d T=1..5: %s"%(q," ".join(row)))
    out.append("")
    out.append("B. MY SUB-LOCUS COUNT vs THE LEDGER (refutes my registered (X8))")
    out.append("  fix the supported pair at (0,inf): objects with Q_0,Q_2 both split over mu_32")
    out.append("  = q^18 * [C(32,7)/q^7]^2 = q^4 * C(32,7)^2  (a 4-DIMENSIONAL family per (S_0,S_inf))")
    out.append("  M := #{(object, z_3) : 0,inf,z_3 all supported} = C(32,7)^3 (q-1)/q^3")
    out.append("  ledger E(3) must equal M*(q+1)*q/6   [6 = orderings of an unordered triple]")
    for q in (97,193,257,641,769):
        M=C**3*(q-1)/q**3
        mine=M*(q+1)*q/6
        led=q**18*comb(q+1,3)*(C/q**7)**3
        out.append("  q=%-4d  log2(mine)=%+.4f  log2(ledger)=%+.4f  ratio=%.12f"
                   %(q,log2(mine),log2(led),mine/led))
    out.append("  => EXACT agreement at every field: the doubly-prescribed sub-locus is NOT thinner")
    out.append("     than the stratum average. (X8) IS REFUTED BY MY OWN ARITHMETIC.")
    out.append("")
    out.append("C. THE DISTANCE TO T=3 OVER mu_32 (the honest cost of the missing solve)")
    for q in (97,193):
        fam=q**4
        hits=C*(q-1)/q**3
        out.append("  q=%-4d 4-dim family per (S_0,S_inf) = q^4 = %d points; expected T>=3 in it = %.1f"
                   %(q,fam,hits))
        out.append("        => P(T>=3 | one exact T=2 object) = %.3e ; exact T=2 objects needed per T=3 = %.3g"
                   %(hits/fam,fam/hits))
    out.append("  measured this round: 28 certified s=0 T=2 objects at q=97, 4 at q=193")
    out.append("  => shortfall factor %.3g (q=97) and %.3g (q=193)"
               %(97**4/(C*96/97**3)/28, 193**4/(C*192/193**3)/4))
    out.append("")
    out.append("D. THE (SCRIT) GAIN: restricting S_2 to mu_32 \\ S_0")
    out.append("  C(25,7)/C(32,7) = %d/%d = %.4f ; s=0 yield goes 0.1428 -> 1.0000, search space /%.2f"
               %(comb(25,7),C,comb(25,7)/C,C/comb(25,7)))
    out.append("")
    out.append("E. (OV4) AGAINST THE BANKED (SAT3) m=2 DESIGN")
    out.append("  (OV4): for distinct supported slopes i,j,k :  e(k,i)+e(k,j) <= 4")
    out.append("  (SAT3) at m=2: 9 slopes, 63 slots on 32 points, d_x<=2 => 31 doubled points,")
    out.append("  i.e. a 9-vertex multigraph with 31 edges and degree sum 62 (degrees 7^8,6).")
    out.append("  Consequences of (OV4) on that multigraph:")
    out.append("   - e(k,i) <= 4 for all pairs; e(k,i)=4 forces deg k = 4 < 6 => e(k,i) <= 3.")
    out.append("   - e(k,i)=3 forces e(k,j) <= 1 for every other j.")
    out.append("   - two multiplicity-2 edges at a vertex are allowed (2+2=4), three are too.")
    # banked design: K_9 minus a 2-path and 3 disjoint edges -> simple graph
    n=9
    E=set()
    for a in range(n):
        for b in range(a+1,n): E.add((a,b))
    for e in [(0,1),(1,2)]: E.discard(e)            # a 2-path
    for e in [(3,4),(5,6),(7,8)]: E.discard(e)      # 3 disjoint edges
    deg=[0]*n
    for a,b in E: deg[a]+=1; deg[b]+=1
    mult={}
    for a,b in E: mult[(a,b)]=1
    def ee(a,b):
        if a==b: return 0
        return mult.get((min(a,b),max(a,b)),0)
    worst=0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if len({i,j,k})==3: worst=max(worst,ee(k,i)+ee(k,j))
    out.append("  banked design (K_9 minus a 2-path and 3 disjoint edges): |E|=%d, degrees=%s"
               %(len(E),sorted(deg,reverse=True)))
    out.append("  worst e(k,i)+e(k,j) = %d  =>  (OV4) %s (slack %d)"
               %(worst,"PASSES" if worst<=4 else "FAILS",4-worst))
    out.append("  HONEST: (OV4) is a NECESSARY condition that the banked design SATISFIES.")
    out.append("  It excludes only concentrated designs; it does not close (SAT3) at m=2.")
    out.append("")
    out.append("F. THE THIRD PRESCRIPTION AS RATIONAL INTERPOLATION (dof bookkeeping)")
    out.append("  type-(4,4) rational function f/g : 4+4+1 = 9 degrees of freedom")
    out.append("  prescribed values at |S_0|+|S_inf| = 14 points  =>  overdetermined by 14-9 = 5")
    out.append("  free scale ratios (alpha:beta:gamma) in P^2 : 2  =>  net deficit 5-2 = 3")
    out.append("  expected solutions per subset-triple = q^2 * q^-5 = q^-3 :")
    for q in (97,193):
        out.append("     q=%-4d  q^-3 = %.3e   triples needed ~ %d   (C(32,7)^3 = 2^%.1f available)"
                   %(q,q**-3.0,q**3,3*log2(C)))
    with open("notes/pilots_20260811/r37_third_solve/d4_results.txt","a") as fh:
        fh.write("\n".join(out)+"\n")
    print("\n".join(out))

main()
