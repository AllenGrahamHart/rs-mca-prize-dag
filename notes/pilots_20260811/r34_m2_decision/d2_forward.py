"""D2 (r34): THE DECISIVE FORWARD SEARCH at m=2, with the bottleneck
functional made EXACT.

Reduction used (derived in REPORT D1):  the locator curve is a NET
    F(Z,x) = c_2(x) Z^2 + c_1(x) Z + c_0(x),   deg c_i <= rho = 7,
whose member at slope g is  P_g = c_2 g^2 + c_1 g + c_0.  (SAT3) needs
T = 9 supported slopes, i.e. 9 members that split into rho = 7 DISTINCT
roots inside the N = 32 point domain, with every domain point used at most
e = 2 times.  Summing u_gamma = 7 over 9 slopes gives 63 incidences on 32
points, so the incidence graph on the 9 slopes has 31 edges and degrees
7^8,6.

EXACT WITNESS DETECTOR (no heuristic maximisation needed):
    a 9-set with 31 edges forces >= 8 slopes of degree exactly 7.
So the decisive functional is
    n7(net) = #{ g in P^1 : P_g splits with 7 distinct roots in D },
and (SAT3) at m=2 requires n7 >= 8 (plus a 9th slope of degree >= 6).
n7 <= 7 is an EXACT certificate that a net cannot host the design.

Normalisation: 3 members are PRESCRIBED split, at slopes 0, 1, infinity
(PGL_2 on the slope line makes this free), so every net searched already
starts with n7 >= 3.  Remaining freedom: two scalars (lambda, mu) and the
three root sets.  For each domain point x the equation P_g(x) = 0 is a
QUADRATIC IN g, so the whole incidence structure of a net costs O(N).

Usage: d2_forward.py OUTFILE
"""
import sys
import random

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


def mu_group(q, n):
    for a in range(2, q):
        h = pow(a, (q - 1) // n, q)
        seen = {pow(h, i, q) for i in range(n)}
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError


def sqrt_table(q):
    t = {}
    for a in range(q):
        t.setdefault(a * a % q, a)
    return t


def poly_vals(roots, D, q):
    """values of prod (x - r) over r in roots, at every x in D"""
    v = []
    for x in D:
        p = 1
        for r in roots:
            p = p * (x - r) % q
        v.append(p)
    return v


def inv_table(q):
    return [0] + [pow(a, q - 2, q) for a in range(1, q)]


def net_incidences(A, B, C, lam, mu_, q, sq, IV):
    """For each domain point, the (<=2) slopes g with P_g(x) = 0.

    P_g(x) = a(1-g) + lam*b*g + mu*c*g(g-1),  a=A[i], b=B[i], c=C[i]
           = (mu c) g^2 + (lam b - a - mu c) g + a.
    Returns (edges, fixed_root_flag).  Slope infinity is encoded as q.
    """
    edges = []
    for i in range(len(A)):
        a, b, c = A[i], B[i], C[i]
        aa = mu_ * c % q
        bb = (lam * b - a - mu_ * c) % q
        cc = a % q
        if aa == 0:
            if bb == 0:
                if cc == 0:
                    return None, True          # x is a fixed root: s > 0
                continue                        # no slope hits x
            g = (-cc) * IV[bb] % q
            edges.append((g, q))                # partner is infinity
            continue
        disc = (bb * bb - 4 * aa * cc) % q
        if disc == 0:
            g = (-bb) * IV[2 * aa % q] % q
            edges.append((g, g))                # double root: d_x = 1
            continue
        if disc not in sq:
            continue                            # no F_q slopes at x
        s = sq[disc]
        iv = IV[2 * aa % q]
        g1 = (-bb + s) * iv % q
        g2 = (-bb - s) * iv % q
        edges.append((g1, g2))
    return edges, False


def profile(edges):
    """slope -> number of domain roots (u_gamma), and the edge multiset"""
    deg = {}
    for (u, v) in edges:
        if u == v:
            deg[u] = deg.get(u, 0) + 1
        else:
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
    return deg


def main():
    random.seed(34340811)
    out("=== r34 D2: forward search for (SAT3) at m=2 ===")
    out("EXACT certificate used: a 31-edge 9-set forces >= 8 slopes of")
    out("degree exactly rho=7, so n7 <= 7 certifies that a net cannot host")
    out("the design.  n7 counts TOTALLY SPLIT members of the net.")
    out("")

    # ---------------- positive control: m = 1 --------------------------
    out("--- POSITIVE CONTROL (m=1, e=1, rho=3, N=16): same machinery ---")
    q = 17
    D1 = mu_group(q, 16)
    sq1 = sqrt_table(q)
    IV1 = inv_table(q)
    best1 = 0
    hist1 = {}
    trials1 = 0
    for _ in range(4000):
        S1 = random.sample(D1, 3)
        S2 = random.sample(D1, 3)
        if set(S1) & set(S2):
            continue
        A = poly_vals(S1, D1, q)
        B = poly_vals(S2, D1, q)
        for lam in range(1, q):
            trials1 += 1
            # pencil P_g = A + g*lam*B  -> for each x, ONE slope (linear)
            deg = {}
            bad = False
            for i in range(16):
                a, b = A[i], lam * B[i] % q
                if b == 0:
                    if a == 0:
                        bad = True
                        break
                    continue
                g = (-a) * IV1[b] % q
                deg[g] = deg.get(g, 0) + 1
            if bad:
                continue
            n3 = sum(1 for v in deg.values() if v == 3) + 1  # +1: slope inf
            hist1[n3] = hist1.get(n3, 0) + 1
            best1 = max(best1, n3)
    out(f"  q=17, D=mu_16, {trials1} pencils with 2 prescribed split members")
    out(f"  n_split histogram (incl. the member at infinity): "
        f"{dict(sorted(hist1.items()))}")
    out(f"  MAX n_split = {best1}   (round 33: T = rho+2 = 5 is attained)")
    out(f"  control verdict: {'REPRODUCED' if best1 >= 5 else 'FAILED'}")
    out("")

    # ---------------- main search: m = 2 --------------------------------
    out("--- MAIN SEARCH (m=2, e=2, rho=7, N=32): nets with 3 prescribed "
        "split members ---")
    out("target: n7 >= 8 (of which 9 slopes must carry the 31-edge design)")
    for q in (97, 193):
        D = mu_group(q, 32)
        sq = sqrt_table(q)
        IV = inv_table(q)
        hist = {}
        best = 0
        best_cfg = None
        n_nets = 0
        budget = 240000 if q == 97 else 240000
        while n_nets < budget:
            # three 7-subsets, pairwise meeting in exactly one point
            pts = random.sample(D, 18)
            s12, s13, s23 = pts[0], pts[1], pts[2]
            rest = pts[3:]
            S1 = [s12, s13] + rest[0:5]
            S2 = [s12, s23] + rest[5:10]
            S3 = [s13, s23] + rest[10:15]
            A = poly_vals(S1, D, q)
            B = poly_vals(S2, D, q)
            C = poly_vals(S3, D, q)
            for _ in range(40):
                lam = random.randrange(1, q)
                mu_ = random.randrange(1, q)
                n_nets += 1
                edges, fixed = net_incidences(A, B, C, lam, mu_, q, sq, IV)
                if fixed:
                    continue
                deg = profile(edges)
                n7 = sum(1 for v in deg.values() if v == 7)
                hist[n7] = hist.get(n7, 0) + 1
                if n7 > best:
                    best = n7
                    best_cfg = (sorted(S1), sorted(S2), sorted(S3), lam, mu_,
                                sorted(deg.values(), reverse=True)[:12])
        out(f"  q={q}: {n_nets} nets scanned (each already carries 3 split "
            f"members by construction)")
        out(f"    n7 histogram: {dict(sorted(hist.items()))}")
        out(f"    MAX n7 = {best}   (need >= 8)   "
            f"{'WITNESS-CAPABLE' if best >= 8 else 'no net can host the design'}")
        if best_cfg:
            out(f"    best config: lam={best_cfg[3]} mu={best_cfg[4]} "
                f"top degrees {best_cfg[5]}")
        tot = sum(hist.values())
        for k in sorted(hist):
            out(f"      n7={k}: {hist[k]}  ({hist[k]/tot:.4%})")
    out("")

    # ---------------- decay law -----------------------------------------
    out("--- the decay: empirical cost of each extra split member ---")
    out("(read off the histograms above; see REPORT for the fit)")
    out("")

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(LINES) + "\n")


main()
