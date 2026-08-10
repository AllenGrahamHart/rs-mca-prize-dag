#!/usr/bin/env python3
"""2-WAY VERIFICATION (PREREG Z3): re-derive every computed N=32 cell with
ALG-2 (umitm.py, unbalanced 18/14, no bucketing) and with BBM-ALT (bbm.py on a
PERMUTED coordinate order + a different RBUCK, so every intermediate residue,
bucket boundary and dict differs).  TNUM and NKER must agree EXACTLY.

  NSHARD=k SHARD=i MODE=umitm|alt tools/ramguard local -- python3 ver.py
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bbm import bbm                                          # noqa: E402
from umitm import umitm                                      # noqa: E402
from zcore import rows_M2, rows_M4                           # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MODE = os.environ.get("MODE", "alt")
OUT = os.path.join(HERE, "VERIFY.%s.s%s.tsv" % (MODE, os.environ.get("SHARD", "0")))


def cells():
    import glob
    out = []
    for fn in sorted(glob.glob(os.path.join(HERE, "CELLS*.tsv"))):
        for ln in open(fn):
            f = ln.rstrip("\n").split("\t")
            if len(f) < 8 or f[0] == "family":
                continue
            if int(f[1]) != 32:
                continue
            out.append((f[0], int(f[1]), int(f[2]), int(f[3]), int(f[5]), int(f[6]),
                        float(f[8])))
    # PRIORITY ORDER: highest CRATIO first, so that if the wall cuts the pass
    # short, the cells the verdict rests on are the ones already 2-way verified.
    out.sort(key=lambda c: -c[6])
    return [c[:6] for c in out]


def done():
    d = set()
    import glob
    for fn in glob.glob(os.path.join(HERE, "VERIFY.%s.*.tsv" % MODE)):
        for ln in open(fn):
            f = ln.split("\t")
            if len(f) >= 4:
                d.add((f[0], int(f[1]), int(f[2]), int(f[3])))
    return d


def main():
    ns = int(os.environ.get("NSHARD", "1"))
    sh = int(os.environ.get("SHARD", "0"))
    cs = [c for i, c in enumerate(cells()) if i % ns == sh]
    dn = done()
    for fam, N, k, p, tnum, nker in cs:
        if (fam, N, k, p) in dn:
            continue
        rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
        t0 = time.time()
        if MODE == "umitm":
            tn, nk, st = umitm(rows, p, small=14)
        else:
            # BBM-ALT: even coordinates first, then odd -> a completely
            # different 16/16 split, different octets, different RBUCK.
            perm = list(range(0, N, 2)) + list(range(1, N, 2))
            prows = [[r[j] for j in perm] for r in rows]
            tn, nk, st = bbm(prows, p, rbuck=181)
        ok = (tn == tnum and nk == nker)
        with open(OUT, "a") as fh:
            fh.write("%s\t%d\t%d\t%d\t%d\t%d\t%s\t%.1f\n"
                     % (fam, N, k, p, tn, nk, "AGREE" if ok else "DISAGREE",
                        time.time() - t0))
        print("%-4s k=%d p=%-12d %s  TNUM %d vs %d   NKER %d vs %d  %.1fs"
              % (fam, k, p, "AGREE" if ok else "*** DISAGREE ***",
                 tn, tnum, nk, nker, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
