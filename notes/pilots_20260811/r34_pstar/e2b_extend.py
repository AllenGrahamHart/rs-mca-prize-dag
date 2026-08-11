"""r34_pstar E2b:
 (a) how FIXED is the low generator?  modal-generator multiplicity per slope
     on FG constructions and on the intermediate stratum;
 (b) does the scaled-Vandermonde descent extend OFF FG?  For uniform random
     column-far pencils: is p* <= r, is dim Ann(V)_{p*} = 1, is P* squarefree?
     (If yes, EVERY such pencil descends to Lambda = F[x]/(P*), dim p*,
      not just the FG ones -- an extension of round 33's FG3.)
 (c) bad-slope sweep on constructed FG pencils vs the candidate bounds
     rho, p, r+1, q.
Stdlib only.  Run under tools/ramguard.
"""
import sys, random
from e1_census import (rank_mod, nullspace, stack, pstar, poly_mul,
                       poly_from_roots, poly_gcd, build_Dr, column_far,
                       bad_slopes)
from e2_construct import (find_irreducible, impulse, extend, low_generator,
                          poly_divides)


def deriv(P, q):
    return [(i * P[i]) % q for i in range(1, len(P))]


def is_squarefree(P, q):
    d = deriv(P, q)
    while d and d[-1] == 0:
        d.pop()
    if not d:
        return False
    g = poly_gcd(P[:], d, q)
    return len(g) - 1 == 0


CELLS = [
    ("W1_round33", 13, 11, 3, 6),
    ("S1_sep", 11, 11, 1, 8),
    ("S2_sep", 13, 13, 1, 10),
    ("S3_sep", 17, 17, 1, 13),
]


def gen_profile(y0, y1, R, q, r):
    gens = {}
    for gm in range(q):
        yg = [(y0[m] + gm * y1[m]) % q for m in range(R)]
        pg, g = low_generator(yg, R, q, r)
        key = (pg, tuple(g) if g else None)
        gens[key] = gens.get(key, 0) + 1
    top = max(gens.values())
    return top, len(gens), gens


def main():
    random.seed(2718281828)
    out = open(sys.argv[1], "w")

    def emit(s):
        out.write(s + "\n")
        out.flush()
        print(s)

    emit("# r34_pstar E2b")
    for (name, q, n, k, r) in CELLS:
        R = n - k
        rho = R - r
        D = list(range(n))
        Dr = build_Dr(D, r, q)
        emit("")
        emit("== %s  q=%d R=%d r=%d rho=%d 2rho=%d floor(R/2)=%d" %
             (name, q, R, r, rho, 2 * rho, R // 2))

        # (a) generator fixity, FG (p=2rho) vs intermediate (p in (2rho,R/2])
        P1 = find_irreducible(rho, q)
        P2 = poly_from_roots(list(range(rho)), q)
        Pfg = poly_mul(P1, P2, q)
        stats = []
        for _ in range(40):
            s0 = [random.randrange(q) for _ in range(2 * rho)]
            s1 = [random.randrange(q) for _ in range(2 * rho)]
            y0 = extend(s0, Pfg, R, q)
            y1 = extend(s1, Pfg, R, q)
            if rank_mod(stack(y0, y1, r, R, q), r + 1, q) != 2 * rho:
                continue
            if not column_far(y0, y1, Dr, R, r, q):
                continue
            top, nd, _ = gen_profile(y0, y1, R, q, r)
            stats.append((top, nd))
        if stats:
            emit("  (a) FG p=2rho=%d : over %d column-far draws, modal low "
                 "generator covers min %d / max %d of q=%d slopes ; "
                 "#distinct generators min %d max %d"
                 % (2 * rho, len(stats), min(s[0] for s in stats),
                    max(s[0] for s in stats), q,
                    min(s[1] for s in stats), max(s[1] for s in stats)))
        for p in range(2 * rho + 1, R // 2 + 1):
            if p > r or p - 2 > n:
                continue
            base = find_irreducible(2, q)
            Pst = poly_mul(base, poly_from_roots(list(range(p - 2)), q), q)
            st2 = []
            for _ in range(40):
                s0 = [random.randrange(q) for _ in range(p)]
                s1 = [random.randrange(q) for _ in range(p)]
                y0 = extend(s0, Pst, R, q)
                y1 = extend(s1, Pst, R, q)
                if pstar(y0, y1, R, q, r) != p:
                    continue
                if not column_far(y0, y1, Dr, R, r, q):
                    continue
                top, nd, _ = gen_profile(y0, y1, R, q, r)
                st2.append((top, nd))
            if st2:
                emit("  (a) intermediate p=%d (2rho<p<=R/2) : over %d "
                     "column-far draws, modal generator covers min %d / max %d "
                     "of q=%d ; #distinct min %d max %d"
                     % (p, len(st2), min(s[0] for s in st2),
                        max(s[0] for s in st2), q,
                        min(s[1] for s in st2), max(s[1] for s in st2)))

        # (b) descent off FG: random column-far pencils
        N = 400
        ok_le_r = 0
        dim1 = 0
        sqf = 0
        tot = 0
        dimquot = {}
        for _ in range(N):
            y0 = [random.randrange(q) for _ in range(R)]
            y1 = [random.randrange(q) for _ in range(R)]
            if not column_far(y0, y1, Dr, R, r, q):
                continue
            tot += 1
            ps = pstar(y0, y1, R, q, r)
            if ps <= r:
                ok_le_r += 1
                ns = nullspace(stack(y0, y1, ps, R, q), ps + 1, q)
                if len(ns) == 1:
                    dim1 += 1
                P = ns[0][:]
                while P and P[-1] == 0:
                    P.pop()
                if is_squarefree(P, q):
                    sqf += 1
                hr = rank_mod(stack(y0, y1, r, R, q), r + 1, q)
                dk = r + 1 - hr
                dq = dk - (r + 1 - ps)   # dim K_0 / P* F[x]
                dimquot[dq] = dimquot.get(dq, 0) + 1
        emit("  (b) %d column-far random pencils : p* <= r in %d ; "
             "dim Ann(V)_{p*} = 1 in %d ; P* squarefree in %d"
             % (tot, ok_le_r, dim1, sqf))
        emit("      dim (K_0 / P*F[x]) spectrum : %s   (0 == principal == FG ; "
             "predicted p*-2rho = %d for p*=%d)"
             % (" ".join("%d:%d" % (a, dimquot[a]) for a in sorted(dimquot)),
                -(-2 * R // 3) - 2 * rho, -(-2 * R // 3)))

        # (c) bad-slope sweep on FG constructions
        Ts = []
        for _ in range(120):
            s0 = [random.randrange(q) for _ in range(2 * rho)]
            s1 = [random.randrange(q) for _ in range(2 * rho)]
            y0 = extend(s0, Pfg, R, q)
            y1 = extend(s1, Pfg, R, q)
            if rank_mod(stack(y0, y1, r, R, q), r + 1, q) != 2 * rho:
                continue
            if not column_far(y0, y1, Dr, R, r, q):
                continue
            Ts.append(bad_slopes(y0, y1, Dr, R, r, q))
        if Ts:
            hist = {}
            for t in Ts:
                hist[t] = hist.get(t, 0) + 1
            emit("  (c) FG bad-slope T over %d column-far FG pencils: %s"
                 % (len(Ts), " ".join("%d:%d" % (a, hist[a])
                                      for a in sorted(hist))))
            emit("      MAX T=%d  vs rho=%d p=%d r+1=%d q=%d  -> "
                 "T<=rho:%s  T<=p:%s  T<=r+1:%s"
                 % (max(Ts), rho, 2 * rho, r + 1, q,
                    max(Ts) <= rho, max(Ts) <= 2 * rho, max(Ts) <= r + 1))
    out.close()


if __name__ == "__main__":
    main()
