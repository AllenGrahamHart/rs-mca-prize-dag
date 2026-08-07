#!/usr/bin/env python3
"""Merge a sharded run into one certificate.  Refuses to report a verdict
unless EVERY shard is DONE and every shard agrees on the problem hash and
the basis."""
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state")


def main():
    cid, ns = sys.argv[1], int(sys.argv[2])
    tot, secs, fnd, done, missing = 0, 0.0, set(), 0, []
    ph = None
    per = []
    for s in range(ns):
        f = os.path.join(STATE, "%s.enum.s%dof%d.json" % (cid, s, ns))
        if not os.path.exists(f):
            missing.append(s)
            continue
        d = json.load(open(f))
        ph = ph or d["phash"]
        assert d["phash"] == ph, "shard %d has a different problem hash" % s
        tot += d["nodes"]
        secs += d["secs"]
        fnd |= set(tuple(w) for w in d["found"])
        fin = d["lev"] >= 64
        done += fin
        per.append((s, d["nodes"], d["secs"], fin, len(d["found"])))
    print("== MERGE %s (%d shards) ==" % (cid, ns))
    for (s, n, sc, fin, nf) in per:
        print("   shard %-3d FPNODES=%-12d secs=%-7.0f %-9s found=%d"
              % (s, n, sc, "DONE" if fin else "RUNNING", nf))
    print("   shards finished: %d/%d %s"
          % (done, ns, ("missing: %s" % missing) if missing else ""))
    # every shard must have enumerated the SAME basis
    bh = set()
    for s in range(ns):
        cf = os.path.join(STATE, "%s.cert.s%dof%d.json" % (cid, s, ns))
        if os.path.exists(cf):
            import hashlib
            bh.add(hashlib.sha256(
                json.dumps(json.load(open(cf))["basis"]).encode()).hexdigest())
    print("   distinct bases across shard certificates: %d %s"
          % (len(bh), "(OK)" if len(bh) <= 1 else "**MISMATCH - VOID**"))
    if len(bh) > 1:
        print("   RESULT: VOID -- shards did not enumerate the same lattice "
              "basis.")
        return
    print("   TOTAL FPNODES = %d = 2^%.3f   total CPU-seconds = %.0f"
          % (tot, math.log2(max(tot, 1)), secs))
    print("   |FPFOUND| = %d" % len(fnd))
    if done == ns and not missing:
        if fnd:
            print("   RESULT: **NONEMPTY** -- WITNESS PROTOCOL TRIGGERS")
            for w in sorted(fnd):
                print("     w = %s" % (list(w),))
        else:
            print("   RESULT: CERTIFIED EMPTY (complete enumeration, all "
                  "shards finished)")
        cert = {}
        f0 = os.path.join(STATE, "%s.cert.s0of%d.json" % (cid, ns))
        if os.path.exists(f0):
            cert = json.load(open(f0))
            cert.update({"nodes": tot, "fpsec": secs,
                         "found": [list(w) for w in sorted(fnd)],
                         "nshard": ns, "merged": True})
            json.dump(cert, open(os.path.join(STATE, "%s.cert.json" % cid), "w"))
            print("   wrote state/%s.cert.json (merged)" % cid)
    else:
        print("   RESULT: INCOMPLETE -- no verdict is reported for this cell.")


if __name__ == "__main__":
    main()
