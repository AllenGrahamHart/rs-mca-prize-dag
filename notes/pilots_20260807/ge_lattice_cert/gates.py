#!/usr/bin/env python3
"""VALIDATION GATES G1-G3, G5(small).  Registered in PREREG.md P2/P3.
Every gate must PASS before any dim-64 result is reported.

Run:  tools/ramguard local -- python3 notes/pilots_20260807/ge_lattice_cert/gates.py
"""
import os
import random
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))

import latlib as LL                                       # noqa: E402
import d4_cone                                            # noqa: E402
import d3_kernel                                          # noqa: E402
from gelib import tower_norm                              # noqa: E402

STATE = os.path.join(HERE, "state")
os.makedirs(STATE, exist_ok=True)
FAILS = []


def certify_small(h, p, cvec, L, tag, boxinf=2):
    """Full pipeline at small h, in one shot (no checkpoint needed)."""
    B = LL.coeff_basis(h, p, cvec)
    dl = time.time() + 1e9
    sp = os.path.join(STATE, "g_%s.lll.json" % tag)
    ep = os.path.join(STATE, "g_%s.enum.json" % tag)
    for q in (sp, ep):
        if os.path.exists(q):
            os.remove(q)
    st, info = LL.lll_resumable(sp, B, tag, [(3, 4), (99, 100)], dl,
                                log=lambda *a: None)
    assert st == 'DONE'
    Br = info["B"]
    d, lam = LL.integral_gso(Br)
    det = LL.isqrt(d[h])
    detok = det * det == d[h] and det == p
    memok = all(sum(w[j] * cvec[j] for j in range(h)) % p == 0 for w in Br)
    R2 = min(4 * h, 2 * L)
    st2, info2 = LL.enum_resumable(ep, Br, R2, L, tag, dl, boxinf=boxinf,
                                   log=lambda *a: None)
    assert st2 == 'DONE'
    return Br, detok, memok, info2


def main():
    print("=" * 74)
    print("VALIDATION GATES -- round-23 ge_lattice_cert")
    print("=" * 74)

    # ---------------------------------------------------------------- G1
    print("\n-- G1: round-22 d4_cone.py boundary cells, BOTH directions --")
    print("   GROUND TRUTH is the EXHAUSTIVE box sweep, not round-22's")
    print("   published witness counts (see CATCH-23A / catch_d4cone.py).")
    print("   The gated quantities are: my witness SET == brute-force set,")
    print("   my VERDICT == round-22's verdict (empty vs nonempty),")
    print("   DETCHECK and MEMBERCHECK.")
    rows = [
        (4, 137, 8, "NONEMPTY", "N'=8  p=137=TIGHTEMPTY(8): witness MUST exist"),
        (4, 401, 8, "EMPTY", "N'=8  p=401 > TIGHTEMPTY: certified EMPTY"),
        (8, 12289, 6, "EMPTY", "N'=16 p=12289 2l'=6: the banked C-4 anchor"),
        (8, 12289, 16, "NONEMPTY", "N'=16 p=12289 full radius (r22 scope catch)"),
        (8, 463249, 16, "NONEMPTY", "N'=16 p=463249=TIGHTEMPTY(16): must exist"),
        (8, 463457, 16, "EMPTY", "N'=16 p=463457 > TIGHTEMPTY: certified EMPTY"),
    ]
    print("\n%-4s %-9s %-5s %-8s %-8s %-8s %-9s %-8s %-8s" %
          ("h", "p", "2l'", "r22 #w", "BRUTE", "mine", "verdict", "FPNODES",
           "det/mem"))
    for (h, p, L, verd, why) in rows:
        z = LL.zeta_of_order(2 * h, p)
        cvec = [pow(z, j, p) for j in range(h)]
        w22, n22 = d4_cone.certify(h, p, L)
        bf = sorted(LL.brute_box(h, p, cvec, L))
        Br, detok, memok, info = certify_small(h, p, cvec, L,
                                               "g1_%d_%d_%d" % (h, p, L))
        mine = sorted(info["found"])
        myverd = "NONEMPTY" if mine else "EMPTY"
        ok = (mine == bf) and myverd == verd and detok and memok
        if not ok:
            FAILS.append("G1 %s" % why)
        print("%-4d %-9d %-5d %-8d %-8d %-8d %-9s %-8d %-8s  %s  %s" %
              (h, p, L, len(w22), len(bf), len(mine), myverd, info["nodes"],
               "%s/%s" % (detok, memok), "PASS" if ok else "**FAIL**", why))
        if mine:
            nrm = set(tower_norm(list(w)) for w in mine)
            print("        %d witnesses, all with Norm in {%s}; Norm/p = %s; "
                  "r22 published %d  (delta %+d)"
                  % (len(mine), ",".join(str(t) for t in sorted(nrm)),
                     sorted(set(t // p for t in nrm)), len(w22),
                     len(bf) - len(w22)))
            print("        example: w = %s" % (str(mine[0]),))

    # ---------------------------------------------------------------- G2
    print("\n-- G2: the banked C-4 anchor, replayed verbatim from round 22 --")
    d3_kernel.c4_replay()

    # ---------------------------------------------------------------- G3
    print("\n-- G3: enumerator vs EXHAUSTIVE box sweep, both verdicts --")
    for (h, p, L) in [(4, 137, 8), (4, 401, 8), (8, 12289, 6), (8, 12289, 16),
                      (8, 463249, 16), (8, 463457, 16)]:
        z = LL.zeta_of_order(2 * h, p)
        cvec = [pow(z, j, p) for j in range(h)]
        bf = sorted(LL.brute_box(h, p, cvec, L))
        Br, detok, memok, info = certify_small(h, p, cvec, L,
                                               "g3_%d_%d_%d" % (h, p, L))
        same = bf == sorted(info["found"])
        if not same:
            FAILS.append("G3 h=%d p=%d" % (h, p))
        print("   h=%d p=%-8d 2l'=%-3d brute=%-3d enum=%-3d sets equal: %-6s %s"
              % (h, p, L, len(bf), len(info["found"]), same,
                 "PASS" if same else "**FAIL**"))

    # ---------------------------------------------------------------- G5
    print("\n-- G5: PLANT-C fail-closed mutation control (small h) --")
    rnd = random.Random(20260807)
    for (h, p) in [(4, 137), (4, 401), (8, 12289), (8, 463457)]:
        for trial in range(2):
            while True:
                v = [rnd.randint(-2, 2) for _ in range(h)]
                if any(v) and v[0] % p != 0:
                    break
            c = [1] + [rnd.randrange(p) for _ in range(h - 1)]
            # force sum_j v_j c_j = 0 mod p by solving for c_t, t = argmax|v|
            t = max(range(1, h), key=lambda j: abs(v[j])) if h > 1 else 0
            if v[t] % p == 0:
                t = 0
            rest = sum(v[j] * c[j] for j in range(h) if j != t)
            c[t] = (-rest * pow(v[t], p - 2, p)) % p
            if t == 0:
                # renormalise so c[0] = 1 (scale the whole functional)
                inv = pow(c[0], p - 2, p)
                c = [(ci * inv) % p for ci in c]
            assert sum(v[j] * c[j] for j in range(h)) % p == 0
            L = 2 * h
            Br, detok, memok, info = certify_small(
                h, p, c, L, "g5_%d_%d_%d" % (h, p, trial))
            got = tuple(v) in info["found"]
            bf = LL.brute_box(h, p, c, L)
            agree = sorted(bf) == sorted(info["found"])
            ok = got and detok and memok and agree
            if not ok:
                FAILS.append("G5 h=%d p=%d trial=%d" % (h, p, trial))
            print("   h=%-3d p=%-8d plant v=%-28s FOUND=%-6s "
                  "brute-agree=%-6s %s"
                  % (h, p, str(tuple(v)), got, agree,
                     "PASS" if ok else "**FAIL**"))

    print("\n" + "=" * 74)
    if FAILS:
        print("GATES **FAILED**: %s" % FAILS)
        sys.exit(1)
    print("ALL GATES PASS (G1 G2 G3 G5-small)")


if __name__ == "__main__":
    main()
