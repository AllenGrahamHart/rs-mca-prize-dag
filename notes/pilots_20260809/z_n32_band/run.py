#!/usr/bin/env python3
"""Driver for the registered grid (PREREG Z2).  Append-only, resumable.

  tools/ramguard local -- python3 notes/pilots_20260809/z_n32_band/run.py TIER [n]

TIER in {t1, t2, t3, t4, lad8, lad16}.  Every cell appends one line to
CELLS.tsv; a cell already present is skipped.  Inside a cell, per-bucket
partials are checkpointed to ckpt/<tag>.ck so a wall kill loses one bucket.
"""
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bbm import bbm, record, tsv_line, HDR                 # noqa: E402
from zcore import is_prime, rows_M2, rows_M4, assert_2power_grid   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, "CELLS.tsv")
CK = os.path.join(HERE, "ckpt")
os.makedirs(CK, exist_ok=True)


def nextp(x, mod=64):
    """least prime == 1 mod `mod` with p >= x"""
    x = int(math.ceil(x))
    x += (1 - x) % mod
    while not is_prime(x):
        x += mod
    return x


def prevp(x, mod=64):
    x = int(x)
    x -= (x - 1) % mod
    while not is_prime(x):
        x -= mod
    return x


def sigma(N, k, p):
    return N - k * math.log2(p)


# ------------------------------------------------------------------ the grid
def tier1():
    """M4/I2 RSET, N=32, kappa=1, p == 1 mod 64, sigma in [-2,2] <=> p in [2^30,2^34]."""
    out = []
    seen = set()

    def add(p, tag):
        if p not in seen and (1 << 30) <= p <= (1 << 34):
            seen.add(p)
            out.append((p, tag))
    for t in (2, 1.5, 1, .5, 0, -.5, -1, -1.5, -2):          # T1a anchors
        add(nextp(2.0 ** (32 - t)), "T1a/s=%+.2f" % t)
    x = nextp(1 << 32)                                        # T1b sigma~0 cluster
    for _ in range(8):
        add(x, "T1b/above")
        x = nextp(x + 64)
    x = prevp(1 << 32)
    for _ in range(8):
        add(x, "T1b/below")
        x = prevp(x - 64)
    for i in range(33):                                       # T1c 1/8-grid
        t = -2 + i / 8.0
        add(nextp(2.0 ** (32 - t)), "T1c/s=%+.3f" % t)
    return [("M4", 32, 1, p, tag) for p, tag in out]


def band_primes(N, k, mod, lo_s=-2.0, hi_s=2.0):
    """all primes == 1 mod `mod` with sigma = N - k log2 p in [lo_s, hi_s]"""
    plo = 2.0 ** ((N - hi_s) / k)
    phi = 2.0 ** ((N - lo_s) / k)
    out = []
    p = nextp(plo, mod)
    while p <= phi:
        out.append(p)
        p = nextp(p + mod, mod)
    return out


def tier2():
    return [("M2", 32, 4, p, "T2/R4-exhaustive") for p in band_primes(32, 4, 64)]


def tier3():
    return [("M2", 32, 3, p, "T3/R3-exhaustive") for p in band_primes(32, 3, 64)]


def tier4():
    ps = band_primes(32, 2, 64)
    ps.sort(key=lambda p: abs(sigma(32, 2, p)))
    sel = ps[:12] + band_primes(32, 2, 64)[:12] + band_primes(32, 2, 64)[-12:]
    seen, out = set(), []
    for p in sel:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return [("M2", 32, 2, p, "T4/R2-sample") for p in out]


def ladder(N):
    return [("M4", N, 1, p, "LAD%d-exhaustive" % N)
            for p in band_primes(N, 1, 2 * N)]


def tier4full():
    """POST-HOC EXTENSION (declared, NOT pre-registered): the R=2 band
    exhaustively.  Added after the registered T4 sample showed kappa=2 at
    sigma~0 is the dangerous direction (CRATIO 1.3428 at p=65921)."""
    return [("M2", 32, 2, p, "T4F/R2-exhaustive") for p in band_primes(32, 2, 64)]


GRID = {"t4full": tier4full, "t1": tier1, "t2": tier2, "t3": tier3, "t4": tier4,
        "lad8": lambda: ladder(8), "lad16": lambda: ladder(16)}


def done_keys():
    import glob
    ks = set()
    for fn in glob.glob(os.path.join(HERE, "CELLS*.tsv")):
        for ln in open(fn):
            f = ln.rstrip("\n").split("\t")
            if len(f) >= 4 and f[0] != "family":
                ks.add((f[0], int(f[1]), int(f[2]), int(f[3])))
    return ks


def main():
    tier = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    rb = int(os.environ.get("RBUCK", "256"))
    cells = GRID[tier]()
    ns = int(os.environ.get("NSHARD", "1"))
    sh = int(os.environ.get("SHARD", "0"))
    out = TSV if ns == 1 else os.path.join(HERE, "CELLS.s%d.tsv" % sh)
    cells = [c for i, c in enumerate(cells) if i % ns == sh]
    if not os.path.exists(out):
        open(out, "w").write("\t".join(HDR) + "\n")
    dk = done_keys()
    n = 0
    for fam, N, k, p, tag in cells:
        if (fam, N, k, p) in dk:
            continue
        if n >= limit:
            break
        assert_2power_grid(N)
        rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
        assert len(rows) == k and len(rows[0]) == N
        ck = os.path.join(CK, "%s_%d_%d_%d.ck" % (fam, N, k, p))
        t0 = time.time()
        tn, nk, dp = bbm(rows, p, rbuck=(rb if N == 32 else 4), ckpt=ck)
        el = time.time() - t0
        d = record(rows, p, tn, nk, fam, tag)
        assert d["ZFLOOR_OK"], "EZ1 Z-FLOOR VIOLATED at %s" % ((fam, N, k, p),)
        with open(out, "a") as fh:
            fh.write(tsv_line(d) + "\n")
        print("%-4s N=%-3d k=%d p=%-12d sig=%+7.4f CRATIO=%.10f NKER=%-9d "
              "dpeak=%-8d %6.1fs  %s" %
              (fam, N, k, p, d["SIGMA"], d["CRATIO"], nk, dp, el, tag), flush=True)
        n += 1
    print("done: %d new cells" % n)


if __name__ == "__main__":
    main()
