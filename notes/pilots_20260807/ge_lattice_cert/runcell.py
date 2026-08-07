#!/usr/bin/env python3
"""D3 -- THE RUN.  Checkpointed exact integer LLL + complete scaled-integer
Fincke-Pohst enumeration for one named cell.

Usage (ALWAYS through ramguard, from the repo root):
  tools/ramguard local -- python3 notes/pilots_20260807/ge_lattice_cert/runcell.py CELLID

Prints  STATUS: RUNNING | DONE  as its last line, so a shell loop can drive
it across the 5-minute wall.  All state lives in ./state/.
"""
import hashlib
import json
import math
import os
import random
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))

import latlib as LL                                       # noqa: E402
import cells as C                                         # noqa: E402
from gelib import tower_norm                              # noqa: E402

STATE = os.path.join(HERE, "state")
os.makedirs(STATE, exist_ok=True)
SOFT = float(os.environ.get("GEL_SOFT", "235"))
PLANT_SEED = 20260807          # registered: deterministic plant


def build(cid):
    """Returns (h, p, cvec, L, boxinf, label, extra) for a cell id.

    A cid of the form BASE@L is the RADIUS-GRADED version of BASE: it
    certifies 'no non-cyclotomic ternary kernel vector of support <= L'
    instead of the full box.  R^2 = min(4h, 2L)."""
    if "@" in cid:
        base, Ls = cid.split("@")
        h, p, cvec, _, boxinf, label, extra = build(base)
        return h, p, cvec, int(Ls), boxinf, \
            label + " [RADIUS-GRADED to support <= %s]" % Ls, extra
    if cid == "E1-128":
        p, rho, h, L = C.P250, C.RHO128, 64, 128
        assert pow(rho, 128, p) == 1 and pow(rho, 64, p) == p - 1, \
            "pinned root does not have exact order 128"
        return h, p, [pow(rho, j, p) for j in range(h)], L, 2, \
            "PINNED e1_folded_no_vector_certificate_128_payload", \
            {"root": rho, "root_src": "pinned rho_128"}
    if cid == "CORRIDOR-128":
        p, h, L = C.QCORR, 64, 128
        assert (p - 1) % 128 == 0
        rho = LL.zeta_of_order(128, p)
        return h, p, [pow(rho, j, p) for j in range(h)], L, 2, \
            "EXHIBIT corridor literal prime at N'=128", \
            {"root": rho, "root_src": "zeta_of_order(128,p)"}
    if cid == "CORRIDOR-128-CONJ":
        # independent replication at a GALOIS-CONJUGATE root.  symmetry.py
        # proves the verdict must be identical; this checks it in dim 64.
        p, h, L = C.QCORR, 64, 128
        rho = pow(LL.zeta_of_order(128, p), 3, p)
        assert pow(rho, 128, p) == 1 and pow(rho, 64, p) == p - 1
        return h, p, [pow(rho, j, p) for j in range(h)], L, 2, \
            "REPLICATION of CORRIDOR-128 at the conjugate root rho^3", \
            {"root": rho, "root_src": "zeta_of_order(128,p)^3"}
    if cid.startswith("PROTH-"):
        c = C.ALLCELLS[cid]
        p, h, L = c["p"], 64, 128
        assert (p - 1) % 128 == 0
        rho = LL.zeta_of_order(128, p)
        return h, p, [pow(rho, j, p) for j in range(h)], L, 2, \
            "EXTENSION deployed Proth row %s" % c["rate"], \
            {"root": rho, "root_src": "zeta_of_order(128,p)"}
    if cid == "PLANT-64":
        # G5 fail-closed control AT THE CERTIFIED DIMENSION AND DETERMINANT
        p, h, L = C.P250, 64, 128
        rnd = random.Random(PLANT_SEED)
        v = [rnd.randint(-2, 2) for _ in range(h)]
        while not any(v):
            v = [rnd.randint(-2, 2) for _ in range(h)]
        cv = [1] + [rnd.randrange(p) for _ in range(h - 1)]
        t = max(range(h), key=lambda j: (abs(v[j]), j))
        rest = sum(v[j] * cv[j] for j in range(h) if j != t)
        cv[t] = (-rest * pow(v[t], p - 2, p)) % p
        if t == 0:
            inv = pow(cv[0], p - 2, p)
            cv = [(x * inv) % p for x in cv]
        assert sum(v[j] * cv[j] for j in range(h)) % p == 0
        return h, p, cv, L, 2, \
            "PLANT-C control (seed %d) -- MUST return NONEMPTY" % PLANT_SEED, \
            {"plant": v}
    raise SystemExit("unknown cell %s" % cid)


def main():
    cid = sys.argv[1]
    h, p, cvec, L, boxinf, label, extra = build(cid)
    phash = hashlib.sha256(json.dumps(
        [cid, h, p, cvec, L, boxinf], sort_keys=True).encode()).hexdigest()[:24]
    R2 = min(4 * h, 2 * L)
    print("== cell %s :: %s ==" % (cid, label))
    print("   h=%d  log2 p=%.3f  2l'=%d  R^2=%d  problem_hash=%s"
          % (h, math.log2(p), L, R2, phash))
    shard = int(os.environ.get("GEL_SHARD", "0"))
    nshard = int(os.environ.get("GEL_NSHARD", "1"))
    sdepth = int(os.environ.get("GEL_SDEPTH", "4"))
    B0 = LL.coeff_basis(h, p, cvec)
    lp = os.path.join(STATE, "%s.lll.json" % cid)
    ep = os.path.join(STATE, "%s.enum.json" % cid if nshard == 1 else
                      "%s.enum.s%dof%d.json" % (cid, shard, nshard))
    dl = time.time() + SOFT

    st, info = LL.lll_resumable(lp, B0, phash, [(3, 4), (99, 100)], dl)
    if st == 'RUNNING':
        print("   LLL RUNNING: stage=%d k=%d swaps=%d cum_secs=%.1f"
              % (info["stage"], info["k"], info["swaps"], info["secs"]))
        print("STATUS: RUNNING")
        return
    Br = info["B"]
    print("   LLL DONE: LLLSWAPS=%d LLLSEC=%.1f" % (info["swaps"], info["secs"]))

    # --- G4: basis soundness, exact
    d, lam = LL.integral_gso(Br)
    det = LL.isqrt(d[h])
    detok = (det * det == d[h]) and (det == p)
    memok = all(sum(w[j] * cvec[j] for j in range(h)) % p == 0 for w in Br)
    prof = [math.log2(d[i + 1]) - math.log2(d[i]) for i in range(h)]
    b0 = LL.dot(Br[0], Br[0])
    rhf = (0.5 * math.log2(b0) - math.log2(p) / h) / (h - 1)
    print("   DETCHECK=%s  MEMBERCHECK=%s  |det B| == p : %s"
          % ("PASS" if detok else "**FAIL**", "PASS" if memok else "**FAIL**",
             det == p))
    print("   GSPROFILE log2||b*_i||^2, i=0..%d:" % (h - 1))
    print("     " + " ".join("%.2f" % t for t in prof))
    print("   ||b_0||^2 = %d (||b_0|| = %.3f);  RHF = 2^%.5f = %.5f;  "
          "GH lambda_1 = %.3f;  R = %.3f"
          % (b0, math.sqrt(b0), rhf, 2 ** rhf,
             math.sqrt(h / (2 * math.pi * math.e)) * 2 ** (math.log2(p) / h),
             math.sqrt(R2)))
    shortest = min(LL.dot(r, r) for r in Br)
    print("   min_i ||b_i||^2 over the reduced basis = %d  (R^2 = %d) -> "
          "%s" % (shortest, R2,
                  "no basis vector is inside the ball"
                  if shortest > R2 else "A BASIS VECTOR IS INSIDE THE BALL"))
    if not (detok and memok):
        print("STATUS: DONE")
        raise SystemExit("G4 FAILED for %s -- cell voided" % cid)

    if nshard > 1:
        print("   SHARD %d of %d (frontier level %d, sdepth %d)"
              % (shard, nshard, h - 1 - sdepth, sdepth))
    st2, info2 = LL.enum_resumable(ep, Br, R2, L, phash, dl, boxinf=boxinf,
                                   shard=shard, nshard=nshard, sdepth=sdepth)
    if st2 == 'RUNNING':
        print("   FP RUNNING: FPNODES=%d lev=%d cum_secs=%.1f found=%d"
              % (info2["nodes"], info2["lev"], info2["secs"],
                 len(info2["found"])))
        print("STATUS: RUNNING")
        return
    found = info2["found"]
    print("   FP DONE: FPNODES=%d  FPSEC=%.1f  |FPFOUND|=%d"
          % (info2["nodes"], info2["secs"], len(found)))
    if not found:
        print("   RESULT: CERTIFIED EMPTY -- no nonzero w in {-%d..%d}^%d "
              "with ||w||_1 <= %d lies in the lattice." % (boxinf, boxinf, h, L))
    else:
        print("   RESULT: **NONEMPTY** -- %d witness(es)" % len(found))
        for w in found[:8]:
            nm = tower_norm(list(w))
            print("     w = %s" % (str(w),))
            print("       ||w||_inf=%d ||w||_1=%d  sum w_j c_j mod p = %d  "
                  "Norm%%p=%d"
                  % (max(abs(t) for t in w), sum(abs(t) for t in w),
                     sum(w[j] * cvec[j] for j in range(h)) % p, nm % p))
    if "plant" in extra:
        v = tuple(extra["plant"])
        ok = v in found
        print("   PLANT-C CONTROL: planted v %s -> %s"
              % ("FOUND" if ok else "**NOT FOUND**", "PASS" if ok else "FAIL"))
        print("   planted v = %s" % (str(v),))
    json.dump({"cid": cid, "h": h, "p": p, "L": L, "boxinf": boxinf,
               "phash": phash, "nodes": info2["nodes"], "fpsec": info2["secs"],
               "lllswaps": info["swaps"], "lllsec": info["secs"],
               "detcheck": detok, "membercheck": memok,
               "gsprofile": prof, "rhf": 2 ** rhf, "b0sq": b0,
               "minbisq": shortest,
               "found": [list(w) for w in found], "basis": Br,
               "shard": shard, "nshard": nshard, "sdepth": sdepth,
               "fcnt": info2.get("fcnt", 0)},
              open(os.path.join(STATE, "%s.cert.json" % cid if nshard == 1 else
                                "%s.cert.s%dof%d.json" % (cid, shard, nshard)),
                   "w"))
    print("STATUS: DONE")


if __name__ == "__main__":
    main()
