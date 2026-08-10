"""D3 — box realization of 2-adic norm classes (named gap 2).

Banked baseline: all 2^10 classes mod 2^17 realized (round 25).
Here: Norm(w) mod 2^D for D = 48, over n sampled odd-norm box vectors at
h = 64, by a Kronecker-packed tower recursion carried out mod 2^D.
Ladder D in {12,16,20,24,26,28,30,32,36,40,44,48}; no D=7 cell (CATCH-19B).

usage: d3_depth.py bench | run <n> <seed> <outfile> | analyse <outfile> ...
"""
import sys, random, array, math, time

D = 48
MASK = (1 << D) - 1
BB = 13 * 8                       # 104-bit lanes, byte aligned (2D + 8 <= 104)
LANE = BB // 8


def negmul_ref(a, b, h):
    c = [0] * h
    for i in range(h):
        ai = a[i]
        if not ai:
            continue
        for j in range(h):
            bj = b[j]
            if not bj:
                continue
            k = i + j
            if k < h:
                c[k] += ai * bj
            else:
                c[k - h] -= ai * bj
    return c


def tower_norm_ref(w):
    w = list(w)
    h = len(w)
    while h > 1:
        wm = [w[i] if i % 2 == 0 else -w[i] for i in range(h)]
        p = negmul_ref(w, wm, h)
        w = [p[2 * i] for i in range(h // 2)]
        h //= 2
    return w[0]


def pack(co):
    v = 0
    for i in range(len(co) - 1, -1, -1):
        v = (v << BB) | co[i]
    return v


def norm_mod(w):
    """Norm(w) mod 2^D by the tower recursion, Kronecker-packed."""
    co = [x % (1 << D) for x in w]
    m = len(co)
    while m > 1:
        com = [co[i] if i % 2 == 0 else (-co[i]) % (1 << D) for i in range(m)]
        prod = pack(co) * pack(com)
        nb = (2 * m - 1) * LANE
        by = prod.to_bytes(nb + LANE, "little")
        full = [int.from_bytes(by[i * LANE:(i + 1) * LANE], "little") & MASK
                for i in range(2 * m - 1)]
        nxt = []
        for k in range(0, m, 2):
            v = full[k]
            if k + m < 2 * m - 1:
                v -= full[k + m]
            nxt.append(v & MASK)
        co = nxt
        m //= 2
    return co[0]


def sample(rng, h=64):
    while True:
        w = [rng.randint(-2, 2) for _ in range(h)]
        if sum(w) % 2:
            return w


if sys.argv[1] == "bench":
    rng = random.Random(7)
    bad = 0
    for _ in range(60):
        w = sample(rng)
        if tower_norm_ref(w) % (1 << D) != norm_mod(w):
            bad += 1
    print("validation against exact tower norm: mismatches", bad, "/60")
    t = time.time()
    K = 2000
    for _ in range(K):
        norm_mod(sample(rng))
    dt = time.time() - t
    print("rate %.0f samples/sec  -> 2^20 in %.1f min" % (K / dt, (1 << 20) / (K / dt) / 60))
    t = time.time()
    for _ in range(200):
        tower_norm_ref(sample(rng))
    print("reference rate %.0f samples/sec" % (200 / (time.time() - t)))

elif sys.argv[1] == "run":
    n = int(sys.argv[2])
    seed = int(sys.argv[3])
    out = sys.argv[4]
    rng = random.Random(seed)
    arr = array.array("Q")
    t0 = time.time()
    for i in range(n):
        arr.append(norm_mod(sample(rng)))
        if (i + 1) % 50000 == 0:
            with open(out, "wb") as f:
                arr.tofile(f)
            print("  %d  %.1fs" % (i + 1, time.time() - t0), flush=True)
    with open(out, "wb") as f:
        arr.tofile(f)
    print("done", n, "%.1fs" % (time.time() - t0))

elif sys.argv[1] == "analyse":
    arr = array.array("Q")
    tot = 0
    for fn in sys.argv[2:]:
        a = array.array("Q")
        with open(fn, "rb") as f:
            a.fromfile(f, __import__("os").path.getsize(fn) // 8)
        arr.extend(a)
        tot += len(a)
    n = len(arr)
    print("samples n = %d  (2^%.2f)" % (n, math.log2(n)))
    print("LAW-1 check: all norms = 1 mod 128 :",
          all(v % 128 == 1 for v in arr))
    print("  D  AVAIL=2^(D-7)   distinct    uniform-pred   collisions  "
          "Mcol/AVAIL   verdict")
    # registered ladder plus D=22,23 (needed to test P-D3a's "every D <= 23")
    for d in (12, 16, 20, 22, 23, 24, 26, 28, 30, 32, 36, 40, 44, 48):
        m = (1 << d) - 1
        vals = sorted(v & m for v in arr)
        dist = 1
        coll = 0
        run = 1
        for i in range(1, n):
            if vals[i] == vals[i - 1]:
                run += 1
            else:
                dist += 1
                coll += run * (run - 1) // 2
                run = 1
        coll += run * (run - 1) // 2
        M = 2 ** (d - 7)
        pred = M * (1 - math.exp(-n / M))
        sd = math.sqrt(max(M * (math.exp(-n / M) - (1 + n / M) * math.exp(-2 * n / M)), 1e-9))
        mcol = (n * (n - 1) / 2 / coll) if coll else float("inf")
        z = (dist - pred) / sd if sd > 0 else 0.0
        verdict = "FULL" if dist == M else ("z=%+.1f" % z)
        print("  %2d  2^%-6d %11d %14.1f %12d   %8.3f   %s"
              % (d, d - 7, dist, pred, coll,
                 mcol / M if coll else float("inf"), verdict))
