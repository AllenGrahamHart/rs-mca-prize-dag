#!/usr/bin/env python3
"""PROBE 2 verifier: unsafe_crossing_family_instantiation vs THEOREM BB.

Round 21, notes/pilots_20260807/red_closability_probes/.
Stdlib only.  Run under:  tools/ramguard local -- python3 <this>  [stage]

Stages (registered in PREREG.md P5-P7 as C1-C4):
  region      C2: the admissible e-range of the crossing lane, and what BB covers
  functional  C1: L_1 and B_C are DIFFERENT functionals -- exact finite countermodel
              to  "L_1(a) > B*  =>  B_C(a) > B*"
  endpoint    C4: BB's agreement vs this node's deployed endpoints
  failclosed  a control that MUST exit 1
  all         everything except failclosed
"""
import itertools
import sys

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append("%s  %s" % (name, detail))
        print("  FAIL  %s  %s" % (name, detail))
    return cond


# --------------------------------------------------------------- C2: region

def stage_region():
    print("== region (C2): the admissible e-range, and what THEOREM BB reaches ==")
    # Constants, all quoted:
    #   log2 q >= 245.1491  -- the lane must WANT w = 2^34
    #       (notes/pilots_20260806/gamma_shell/PROOFS.md:348;
    #        es_g_lanes/full_run.txt:126-127)
    #   log2 q <  256       -- the field cap (field_cap_check, PROVED)
    #   p >= 2^39 + 1       -- gamma_shell/PROOFS.md:382 row check
    #   Cauchy-Schwarz non-vacuous  <=>  Q = p^{delta_a} < 2^126
    #       (gamma_shell/PROOFS.md:350)
    LO, HI, PMIN, CS = 245.1491, 256.0, 39.0, 126.0
    admissible = []
    for e in range(1, 12):
        lo, hi = LO / e, HI / e
        if hi <= PMIN:
            continue                       # window entirely below the prime floor
        lo = max(lo, PMIN)
        if lo >= hi:
            continue
        admissible.append((e, lo, hi))
    print("   admissible extension degrees for the rate-1/2 crossing lane:")
    for (e, lo, hi) in admissible:
        rows = []
        for da in (1, 2, 4):
            nonvac = da * lo < CS
            sub_hi = min(hi, CS / da)
            rows.append("delta_a=%d: %s" % (da, ("reaches up to log2 p < %.4f" % sub_hi)
                                            if nonvac else "VACUOUS"))
        print("     e=%-2d live log2 p in [%.4f, %.4f)   %s" % (e, lo, hi, "; ".join(rows)))
    es = [e for (e, lo, hi) in admissible]
    check("region.admissible-e-range-is-1-to-6", es == [1, 2, 3, 4, 5, 6],
          "got %s" % es)
    # e = 1 (prime rows) -- Cauchy-Schwarz vacuous at every delta_a
    e1 = [x for x in admissible if x[0] == 1][0]
    check("region.e1-cauchy-schwarz-vacuous", 1 * e1[1] >= CS,
          "log2 p >= %.4f but CS needs < %.1f" % (e1[1], CS))
    print("   => e = 1 (PRIME rows) admissible and NON-EMPTY, and BB's method is")
    print("      provably vacuous there (log2 p >= %.4f > %.1f)." % (e1[1], CS))
    covered = [3, 4, 5, 6]                 # full at delta_a = 1 (gamma_shell REPORT:51)
    partial = [2]                          # sub-window only
    uncovered = [e for e in es if e not in covered and e not in partial]
    check("region.uncovered-is-exactly-e1", uncovered == [1], "got %s" % uncovered)
    print("   BB coverage of the admissible e-range %s:" % es)
    print("     FULL (delta_a=1): %s      PARTIAL: %s      NONE: %s" % (covered, partial, uncovered))
    print("     => 4 of 6 degrees full, 1 partial, 1 (the prime rows) unreachable in principle.")


# ----------------------------------------------------- C1: the two functionals

def build_rs(q, n, k):
    """RS[F_q, D, k] with D the first n elements of F_q. Returns (codewords, D)."""
    D = list(range(n))
    words = []
    for coeffs in itertools.product(range(q), repeat=k):
        c = []
        for x in D:
            v = 0
            for a in reversed(coeffs):
                v = (v * x + a) % q
            c.append(v)
        words.append(tuple(c))
    return sorted(set(words)), D


def stage_functional():
    print("== functional (C1): L_1 and B_C are different counts ==")
    print("   L_1(a) = max_u #{c in C : agr(c,u) >= a}          (LIST side; BB bounds THIS)")
    print("   B_C(a) = max over lines #{finite slopes gamma bad at agreement >= a}  (MCA side;")
    print("            the node's falsifier is stated in B_C)")
    print("   Convention: I use the PLAIN MCA-bad predicate (a codeword at agreement >= a on")
    print("   the line point). The support-wise refinement of")
    print("   background/nodes/rate_half_arbitrary_line_syndrome_router/statement.md:8-16 only")
    print("   REMOVES slopes, so plain B_C >= support-wise B_C: every UPPER bound below is safe.")
    print("")
    # STRUCTURAL LEMMA: there are only q finite slopes, so B_C(a) <= q for every a,
    # whereas L_1(a) is bounded only by the codeword count and can exceed q.
    for (q, n, k) in ((5, 4, 2), (7, 6, 2)):
        code, D = build_rs(q, n, k)
        allwords = list(itertools.product(range(q), repeat=n))
        # exact L_1(a) for every a
        L1 = {}
        best_u = {}
        for u in allwords:
            cnt = {}
            for c in code:
                agr = sum(1 for i in range(n) if c[i] == u[i])
                for a in range(agr + 1):
                    cnt[a] = cnt.get(a, 0) + 1
            for a, v in cnt.items():
                if v > L1.get(a, -1):
                    L1[a] = v
                    best_u[a] = u
        # exact B_C(a) by enumerating all lines, for the small cell only
        BC = {}
        if q ** n <= 1000:
            close = {}
            for a in range(n + 1):
                close[a] = set()
            for u in allwords:
                m = 0
                for c in code:
                    agr = sum(1 for i in range(n) if c[i] == u[i])
                    if agr > m:
                        m = agr
                for a in range(m + 1):
                    close[a].add(u)
            for a in range(n + 1):
                best = 0
                ca = close[a]
                for u0 in allwords:
                    for u1 in allwords:
                        if not any(u1):
                            continue
                        cnt = 0
                        for g in range(q):
                            pt = tuple((u0[i] + g * u1[i]) % q for i in range(n))
                            if pt in ca:
                                cnt += 1
                        if cnt > best:
                            best = cnt
                            if best == q:
                                break
                    if best == q:
                        break
                BC[a] = best
        print("   RS[F_%d, |D|=%d, k=%d]:  q = %d finite slopes, |C| = %d codewords" % (q, n, k, q, len(code)))
        for a in range(1, n + 1):
            bc = BC.get(a)
            print("     a=%-2d  L_1(a) = %-6d   B_C(a) = %-6s   L_1 > q ? %s"
                  % (a, L1.get(a, 0), bc if bc is not None else "<= q (structural)", L1.get(a, 0) > q))
        check("functional.BC-bounded-by-q.q%d" % q,
              all(v <= q for v in BC.values()) if BC else True, str(BC))
        # THE COUNTERMODEL: an a with L_1(a) > q >= B_C(a).
        hits = [a for a in range(1, n + 1) if L1.get(a, 0) > q]
        check("functional.countermodel-exists.q%d" % q, len(hits) > 0,
              "no agreement with L_1(a) > q at this cell")
        if hits:
            a = hits[-1]
            Bstar = q
            print("     COUNTERMODEL at a = %d:  set B* = q = %d." % (a, Bstar))
            print("        L_1(%d) = %d > B* = %d,   yet   B_C(%d) <= q = %d = B*."
                  % (a, L1[a], Bstar, a, q))
            if BC:
                check("functional.countermodel-exact.q%d" % q, BC[a] <= Bstar < L1[a],
                      "B_C=%s B*=%s L_1=%s" % (BC[a], Bstar, L1[a]))
                print("        exact B_C(%d) = %d <= B* = %d < L_1(%d) = %d"
                      % (a, BC[a], Bstar, a, L1[a]))
            print("        => the implication  'L_1(a) > B*  =>  B_C(a) > B*'  is FALSE.")
        # neither dominates: find a with B_C(a) > L_1(a)
        if BC:
            rev = [a for a in range(1, n + 1) if BC[a] > L1.get(a, 0)]
            print("     agreements where B_C(a) > L_1(a): %s   (so neither count dominates)" % rev)
            check("functional.neither-dominates.q%d" % q, len(rev) > 0 and len(hits) > 0,
                  "rev=%s hits=%s" % (rev, hits))
        print("")


# ------------------------------------------------------------- C4: endpoint

def stage_endpoint():
    print("== endpoint (C4): BB's agreement vs this node's endpoints ==")
    k = 2 ** 40
    bb_a = k + 2 ** 34
    print("   THEOREM BB is stated at agreement k + 2^34 = %d  (n = 2^41, k = 2^40)" % bb_a)
    deployed = {"KoalaBear": 1116047, "Mersenne-31": 1116023}
    for nm, a in deployed.items():
        print("   node's deployed MCA row %-12s endpoint a_safe-1 = %d" % (nm, a))
        check("endpoint.mismatch.%s" % nm, a != bb_a,
              "%d vs %d" % (a, bb_a))
    print("   ratio BB endpoint / deployed endpoint = %.3e" % (bb_a / 1116047.0))
    print("   => BB's endpoint is not any endpoint this node currently carries; a BB-based")
    print("      payload would have to be re-derived at the node's own a_safe-1, on the MCA row.")


def stage_failclosed():
    print("== failclosed: this control MUST exit 1 ==")
    check("failclosed.deliberately-false", 1 * (245.1491) < 126.0,
          "asserts that e=1 rows are Cauchy-Schwarz-live, which they are not")


STAGES = {"region": stage_region, "functional": stage_functional,
          "endpoint": stage_endpoint, "failclosed": stage_failclosed}

if __name__ == "__main__":
    want = sys.argv[1] if len(sys.argv) > 1 else "all"
    if want == "all":
        for nm in ("region", "functional", "endpoint"):
            STAGES[nm]()
            print("")
    else:
        STAGES[want]()
    print("---- %d checks, %d failures ----" % (CHECKS[0], len(FAILURES)))
    for f in FAILURES:
        print("   " + f)
    sys.exit(1 if FAILURES else 0)
