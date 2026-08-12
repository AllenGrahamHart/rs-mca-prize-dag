"""r35_l2_gate D4 -- the first T / a* measurement on a REAL m = 2 object.

Round 34 could measure n7 only on nets that carry NO syndrome pencil.
These witnesses carry one.  Measured here, per witness:
  * the full split-profile of the pencil: for every parameter z, the
    number of roots of the locator Q_z inside F_q;
  * T over the multiplicative domain mu_32 (the endpoint's domain);
  * T over a DESIGNED 32-subset domain (greedy set-cover: a LOWER bound
    on the best designable T, never an upper bound -- MISS-2 guard (i));
  * a* = min |S_g u S_g'| over all slope pairs and over split pairs,
    against F1's 7m-1 = 13;
  * the incidence functionals d_x, O, and the (SAT4) deficit on the
    designed domain.
"""
LINES = []


def P(s=""):
    LINES.append(str(s))


exec(open("notes/pilots_20260811/r35_l2_gate/_shared.py").read())

WITS = [
    dict(p=97, tag="q=97 #1",
         Q0=[7, 10, 78, 31, 43, 62, 29, 22],
         Q1=[80, 88, 69, 63, 34, 94, 70, 62],
         Q2=[80, 4, 73, 12, 82, 59, 47, 1]),
    dict(p=193, tag="q=193 #1",
         Q0=[100, 171, 13, 99, 32, 133, 85, 141],
         Q1=[68, 181, 102, 84, 155, 1, 89, 104],
         Q2=[98, 184, 87, 75, 41, 63, 38, 1]),
]


def peval(a, x, p):
    v = 0
    for c in reversed(a):
        v = (v * x + c) % p
    return v


def main():
    for W in WITS:
        p = W["p"]
        Q = [W["Q0"], W["Q1"], W["Q2"]]
        gg = 2
        while pow(gg, (p - 1) // 2, p) == 1:
            gg += 1
        w = pow(gg, (p - 1) // 32, p)
        mu32 = sorted({pow(w, i, p) for i in range(32)})
        P("=" * 70)
        P("WITNESS %s   (e = m = 2, generic rank 7, s = 0, certified)"
          % W["tag"])
        P("=" * 70)
        locs = {}
        hist = {}
        splitz = {}
        nonsf = 0
        for z in range(p):
            Qz = ptrim([(Q[0][i] + z * Q[1][i] + z * z * Q[2][i]) % p
                        for i in range(8)], p)
            locs[z] = Qz
            if len(Qz) != 8:
                continue
            if len(pgcd(Qz, pderiv(Qz, p), p)) > 1:
                nonsf += 1
                continue
            rts = [x for x in range(p) if peval(Qz, x, p) == 0]
            hist[len(rts)] = hist.get(len(rts), 0) + 1
            if len(rts) == 7:
                splitz[z] = set(rts)
        P("  locator root-count histogram over all %d finite parameters,"
          " roots in F_q: %s" % (p, dict(sorted(hist.items()))))
        P("  non-squarefree / degree-deficient parameters: %d" % nonsf)
        P("  parameters whose locator splits COMPLETELY over F_q: %d"
          % len(splitz))
        # T over the endpoint's multiplicative domain
        mus = set(mu32)
        tmu = sum(1 for z in splitz if splitz[z] <= mus)
        best_in_mu = max([len(splitz[z] & mus) for z in splitz] or [0])
        allmu = max([len([x for x in mu32 if peval(locs[z], x, p) == 0])
                     for z in range(p)] or [0])
        P("  T over D = mu_32 (endpoint domain)                : %d" % tmu)
        P("  max roots of any locator inside mu_32             : %d" % allmu)
        # designed domain: greedy set cover with |D| = 32
        chosen = []
        cur = set()
        order = sorted(splitz, key=lambda z: len(splitz[z] - cur))
        improved = True
        while improved:
            improved = False
            bestz, bestcost = None, None
            for z in splitz:
                if z in chosen:
                    continue
                cost = len(splitz[z] - cur)
                if len(cur | splitz[z]) <= 32:
                    if bestcost is None or cost < bestcost:
                        bestz, bestcost = z, cost
            if bestz is not None:
                chosen.append(bestz)
                cur |= splitz[bestz]
                improved = True
        P("  DESIGNED domain (greedy, |D| <= 32): T = %d supported"
          " parameters, |D| = %d" % (len(chosen), len(cur)))
        P("  (a greedy value is a LOWER bound on the best designable T,"
          " never an upper bound -- MISS-2 guard (i))")
        P("  the endpoint needs T = rho+2 = 9.")
        if chosen:
            D = sorted(cur)
            dx = {}
            for z in chosen:
                for x in splitz[z]:
                    dx[x] = dx.get(x, 0) + 1
            P("  d_x histogram on the designed domain (e = m = 2 caps d_x"
              " at 2): %s"
              % dict(sorted({v: list(dx.values()).count(v)
                             for v in set(dx.values())}.items())))
            P("  saturated points (d_x = 2): %d ; |D| = %d ; deficit"
              " sum_x (m - d_x) = %d"
              % (sum(1 for v in dx.values() if v == 2), len(D),
                 sum(2 - dx.get(x, 0) for x in D)))
            O = sum(7 - len(splitz[z] & set(D)) for z in chosen)
            P("  O = sum_gamma (rho - u_gamma) on the designed domain: %d" % O)
        # a*
        mx_all, arg = 0, None
        for z in range(p):
            for zz in range(z + 1, p):
                d = len(pgcd(locs[z], locs[zz], p)) - 1
                if d > mx_all:
                    mx_all, arg = d, (z, zz)
        P("  max shared roots over ALL slope pairs: %d  (at %s)"
          % (mx_all, arg))
        P("  a* over ALL slope pairs = 14 - %d = %d   vs F1's 7m-1 = 13"
          % (mx_all, 14 - mx_all))
        if len(splitz) >= 2:
            sl = sorted(splitz)
            mx_s = 0
            for i in range(len(sl)):
                for j in range(i + 1, len(sl)):
                    d = len(splitz[sl[i]] & splitz[sl[j]])
                    mx_s = max(mx_s, d)
            P("  a* over SPLIT (candidate-supported) pairs = %d" % (14 - mx_s))
    with open("notes/pilots_20260811/r35_l2_gate/d4_results.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\n".join(LINES))


main()
