"""r34_pstar E2: EXPLICIT low-p* column-far pencils.

Four constructions, all scale-free (they use only p, rho, r, R and a choice
of P*), so whatever they verify at small cells is verified by the SAME
elementary argument at razor shape.

  A  (non-squarefree, closed form)  y0 = e_{2rho-1}, y1 = e_{rho-1}
       => K_0 = x^{2rho} F[x]_{<=r-2rho}, p* = 2rho, column-far for free
          (every element of K_0 has a repeated root).
  B  (squarefree, disjoint halves)  P1 irreducible of degree rho,
       P2 squarefree of degree rho coprime to P1; y0 = impulse(P1),
       y1 = impulse(P2)  => K_0 = P1P2 F[x]_{<=r-2rho}, p* = 2rho.
  B' (control) P1 chosen D-SPLIT squarefree => column-farness must FAIL
       (tests round 33's FG2 equivalence in the negative direction).
  C  (generic V inside IS(P*))  P* squarefree of degree p, V random 2-dim.
  E  (intermediate stratum) p with 2rho < p <= floor(R/2): fixed generator
       but NON-principal K_0  =>  p* <= R/2 does NOT imply FG.

Stdlib only.  Run under tools/ramguard.
"""
import sys, random
from itertools import combinations
from e1_census import (rank_mod, nullspace, stack, pstar, pgen, poly_mul,
                       poly_from_roots, poly_gcd, build_Dr, in_kernel,
                       column_far, bad_slopes)


def is_irreducible_small(P, q):
    """Degree 2 or 3 monic: irreducible iff no root in F_q."""
    d = len(P) - 1
    assert 2 <= d <= 3
    for x in range(q):
        v = 0
        for c in reversed(P):
            v = (v * x + c) % q
        if v == 0:
            return False
    return True


def find_irreducible(d, q):
    for tup in _monics(d, q):
        if is_irreducible_small(tup, q):
            return tup
    raise RuntimeError("none")


def _monics(d, q):
    if d == 2:
        for a in range(q):
            for b in range(q):
                yield [a, b, 1]
    else:
        for a in range(q):
            for b in range(q):
                for c in range(q):
                    yield [a, b, c, 1]


def impulse(P, R, q):
    """Sequence of length R with minimal polynomial exactly P (monic)."""
    d = len(P) - 1
    y = [0] * (d - 1) + [1]
    while len(y) < R:
        m = len(y) - d
        s = 0
        for j in range(d):
            s += P[j] * y[m + j]
        y.append((-s) % q)
    return y[:R]


def extend(seed, P, R, q):
    d = len(P) - 1
    y = list(seed)
    while len(y) < R:
        m = len(y) - d
        s = 0
        for j in range(d):
            s += P[j] * y[m + j]
        y.append((-s) % q)
    return y[:R]


def poly_divides(a, b, q):
    """does a | b ?"""
    b = b[:]
    while b and b[-1] == 0:
        b.pop()
    if not b:
        return True
    da = len(a) - 1
    inv = pow(a[-1], q - 2, q)
    while len(b) - 1 >= da:
        f = b[-1] * inv % q
        sh = len(b) - 1 - da
        for i in range(da + 1):
            b[sh + i] = (b[sh + i] - f * a[i]) % q
        while b and b[-1] == 0:
            b.pop()
        if not b:
            return True
    return False


def low_generator(y, R, q, cap):
    """(p_gen, monic minimal-degree annihilator) of one slope."""
    for i in range(0, cap + 1):
        rows = [[y[t + j] for j in range(i + 1)] for t in range(R - i)]
        ns = nullspace(rows, i + 1, q)
        if ns:
            v = ns[0][:]
            while v and v[-1] == 0:
                v.pop()
            inv = pow(v[-1], q - 2, q)
            return i, [(c * inv) % q for c in v]
    return cap + 1, None


def analyse(tag, y0, y1, cell, Dr, emit, want_T=True):
    name, q, n, k, r = cell
    R = n - k
    rho = R - r
    ps = pstar(y0, y1, R, q, r)
    st = stack(y0, y1, r, R, q)
    hr = rank_mod(st, r + 1, q)
    dk = r + 1 - hr
    ns = nullspace(st, r + 1, q)
    g = None
    if ns:
        g = ns[0]
        for v in ns[1:]:
            g = poly_gcd(g, v, q)
        while g and g[-1] == 0:
            g.pop()
    far = column_far(y0, y1, Dr, R, r, q)
    principal = (g is not None and len(g) - 1 == ps and dk == r + 1 - ps
                 and all(poly_divides(g, v, q) for v in ns))
    gens = []
    for gm in range(q):
        yg = [(y0[m] + gm * y1[m]) % q for m in range(R)]
        gens.append(low_generator(yg, R, q, r))
    pg = [a for a, _ in gens]
    distinct = len(set(tuple(b) for _, b in gens if b is not None))
    T = bad_slopes(y0, y1, Dr, R, r, q) if want_T else -1
    emit("  %-28s p*=%-3s h_r=%-3d dimK0=%-3d deg gcd(K0)=%-3s "
         "K0 principal=%-5s col-far=%-5s"
         % (tag, ps, hr, dk, (len(g) - 1) if g else "-", principal, far))
    emit("      p_gen over slopes: min=%d max=%d ; distinct low generators "
         "over %d slopes = %d (1 = FIXED) ; bad slopes T=%s"
         % (min(pg), max(pg), q, distinct, T))
    return dict(pstar=ps, hr=hr, dimK0=dk, far=far, principal=principal, T=T,
                distinct=distinct, gdeg=(len(g) - 1) if g else None)


CELLS = [
    ("W1_round33", 13, 11, 3, 6),
    ("S1_sep", 11, 11, 1, 8),
    ("S2_sep", 13, 13, 1, 10),
    ("S3_sep", 17, 17, 1, 13),
]


def main():
    random.seed(31415926)
    out = open(sys.argv[1], "w")

    def emit(s):
        out.write(s + "\n")
        out.flush()
        print(s)

    emit("# r34_pstar E2 -- explicit low-p* column-far constructions")
    for cell in CELLS:
        name, q, n, k, r = cell
        R = n - k
        rho = R - r
        D = list(range(n))
        Dr = build_Dr(D, r, q)
        emit("")
        emit("== %s : q=%d n=%d k=%d r=%d R=%d rho=%d 2rho=%d floor(R/2)=%d "
             "|D_r(D)|=%d  FG bracket p in (%d,%d]  lemma bracket p<=%d"
             % (name, q, n, k, r, R, rho, 2 * rho, R // 2, len(Dr), rho,
                2 * rho, R // 2))
        emit("   separating (2rho < floor(R/2))? %s" % (2 * rho < R // 2))

        # --- A : closed-form non-squarefree witness -------------------
        p = 2 * rho
        y0 = [1 if m == 2 * rho - 1 else 0 for m in range(R)]
        y1 = [1 if m == rho - 1 else 0 for m in range(R)]
        res = analyse("A  y0=e_{2rho-1},y1=e_{rho-1}", y0, y1, cell, Dr, emit)
        exp = [x for x in range(r + 1) if x >= 2 * rho]
        ok = (res["pstar"] == 2 * rho and res["hr"] == 2 * rho
              and res["dimK0"] == r + 1 - 2 * rho and res["far"])
        emit("      [A CHECK] p*==2rho and h_r==2rho and dimK0==r+1-2rho and "
             "column-far : %s" % ok)

        # --- B : squarefree disjoint-halves witness -------------------
        if rho in (2, 3):
            P1 = find_irreducible(rho, q)
            roots2 = list(range(rho))          # D-split half
            P2 = poly_from_roots(roots2, q)
            y0 = impulse(P1, R, q)
            y1 = impulse(P2, R, q)
            res = analyse("B  P1 irred(deg rho) + P2 D-split", y0, y1, cell,
                          Dr, emit)
            Pstar = poly_mul(P1, P2, q)
            okB = (res["pstar"] == 2 * rho and res["dimK0"] == r + 1 - 2 * rho
                   and res["far"] and res["principal"] and res["distinct"] >= 1)
            emit("      [B CHECK] P*=P1*P2 squarefree deg %d, p*==2rho, K_0 "
                 "principal, column-far : %s" % (len(Pstar) - 1, okB))

            # --- B' control : both halves D-split -> must NOT be far --
            P1s = poly_from_roots(list(range(rho, 2 * rho)), q)
            y0 = impulse(P1s, R, q)
            y1 = impulse(P2, R, q)
            res = analyse("B' control: BOTH halves D-split", y0, y1, cell, Dr,
                          emit)
            emit("      [B' CHECK] FG2 predicts column-far == False here : "
                 "observed far=%s -> %s"
                 % (res["far"], res["far"] is False))

        # --- C : generic V inside IS(P*), P* squarefree not D-split ---
        if rho in (2, 3):
            P1 = find_irreducible(rho, q)
            P2 = poly_from_roots(list(range(rho)), q)
            Pstar = poly_mul(P1, P2, q)
            best = None
            for trial in range(40):
                s0 = [random.randrange(q) for _ in range(2 * rho)]
                s1 = [random.randrange(q) for _ in range(2 * rho)]
                y0 = extend(s0, Pstar, R, q)
                y1 = extend(s1, Pstar, R, q)
                st = stack(y0, y1, r, R, q)
                if rank_mod(st, r + 1, q) == 2 * rho:
                    res = analyse("C  generic V in IS(P*) [trial %d]" % trial,
                                  y0, y1, cell, Dr, emit)
                    best = res
                    break
            if best is None:
                emit("  C : no full-rank draw in 40 trials")
            else:
                emit("      [C CHECK] p*==2rho=%d and column-far and K_0 "
                     "principal : %s"
                     % (2 * rho, best["pstar"] == 2 * rho and best["far"]
                        and best["principal"]))
                # bad-slope spread over many draws
                Ts = []
                for trial in range(30):
                    s0 = [random.randrange(q) for _ in range(2 * rho)]
                    s1 = [random.randrange(q) for _ in range(2 * rho)]
                    y0 = extend(s0, Pstar, R, q)
                    y1 = extend(s1, Pstar, R, q)
                    st = stack(y0, y1, r, R, q)
                    if rank_mod(st, r + 1, q) != 2 * rho:
                        continue
                    if not column_far(y0, y1, Dr, R, r, q):
                        continue
                    Ts.append(bad_slopes(y0, y1, Dr, R, r, q))
                if Ts:
                    hist = {}
                    for t in Ts:
                        hist[t] = hist.get(t, 0) + 1
                    emit("      [C] bad-slope counts over %d column-far FG "
                         "draws: %s ; MAX T=%d (q=%d, rho=%d, p=%d, r+1=%d)"
                         % (len(Ts), " ".join("%d:%d" % (a, hist[a])
                                              for a in sorted(hist)),
                            max(Ts), q, rho, 2 * rho, r + 1))

        # --- E : intermediate stratum 2rho < p <= floor(R/2) ----------
        for p in range(2 * rho + 1, R // 2 + 1):
            if p > r:
                continue
            # P* squarefree of degree p, not D-split (one irreducible factor)
            base = find_irreducible(2, q) if p >= 2 else None
            if p - 2 > n:
                continue
            P2 = poly_from_roots(list(range(p - 2)), q)
            Pstar = poly_mul(base, P2, q)
            got = False
            for trial in range(60):
                s0 = [random.randrange(q) for _ in range(p)]
                s1 = [random.randrange(q) for _ in range(p)]
                y0 = extend(s0, Pstar, R, q)
                y1 = extend(s1, Pstar, R, q)
                if pstar(y0, y1, R, q, r) != p:
                    continue
                res = analyse("E  V in IS(P*), deg P*=%d (2rho<p<=R/2)" % p,
                              y0, y1, cell, Dr, emit)
                emit("      [E CHECK] p*=%d <= floor(R/2)=%d but h_r=%d "
                     "(=2rho=%d, NOT p) and dimK0=%d > r+1-p=%d  => K_0 NOT "
                     "principal => NOT in FG : %s"
                     % (res["pstar"], R // 2, res["hr"], 2 * rho, res["dimK0"],
                        r + 1 - p, (not res["principal"])))
                got = True
                break
            if not got:
                emit("  E deg P*=%d : no clean draw in 60 trials" % p)
    out.close()


if __name__ == "__main__":
    main()
