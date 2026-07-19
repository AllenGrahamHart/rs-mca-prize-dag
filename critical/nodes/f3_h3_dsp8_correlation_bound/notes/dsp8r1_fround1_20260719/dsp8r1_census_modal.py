#!/usr/bin/env python3
"""DSP8 F-round 1 census (dsp8r1).

Exact measurement of the DSP8 correlation
    10*J_25^0 + 17*J_25^A <= 892*n^2,   J = 8*D,
    D_6,25^c = sum over retained targets (t != 1, P(t) >= 25, class c)
               of N_6^disj(t) * R(t)
at analogue/official rows n = 2^s, p prime = 1 (mod n), n^2 <= p <= 6^{n/4}.

Definitions pinned verbatim from
background/nodes/f3_h3_disjoint_distance_six_split_pencil_router (DSP1-DSP8)
and f3_h3_distance_six_support_overlap_payment (DSO4).  See
dsp8r1_falsifiers.md for the pre-registered round.

Modes:
  control [mutate_edges] [rhs=<int>] [expect=T,E,R]
      toy rows (17,8),(97,16),(193,16): cutoff-0 full-D totals in the
      router verify.py normalization (targets/edges/raw_records), plus
      PC-3 DSP3 identity on (32,1153), plus kill-detector exercise.
  scan n=<n> mstart=<m> mend=<m> [pmax=<int>]
      exhaustive primes p = n*m+1 in [mstart, mend), n^2 <= p <= min(6^{n/4}, pmax).
  highp n=<n> count=<k> start=<int>
      first k primes = 1 (mod n) above start (must be <= 6^{n/4}).
  official n=<n> first=<k> [must=<p1>,<p2>...]
      first k official primes at order n (numpy P-count path, exact int64
      with overflow assertion + pure-python recount of every rich fiber).
  replay n=<n> p=<p>
      full exact pure-python measurement of one row (verdict path).

All arithmetic on the verdict path is exact integer arithmetic.
"""

from __future__ import annotations

import sys
import time
from collections import Counter

from sympy import isprime

RHS_CONST = 892  # pinned; overridable ONLY in control mode (MC-2)
CUTOFF = 25      # pinned
RICH = 19        # diagnostic / escalation threshold


def corridor_top(n: int) -> int:
    return 6 ** (n // 4)


def find_generator(p: int, n: int) -> int:
    for c in range(2, 2000):
        g = pow(c, (p - 1) // n, p)
        if g != 1 and pow(g, n // 2, p) != 1:
            return g
    raise AssertionError(f"no order-{n} generator for p={p}")


def build_row(p: int, n: int):
    g = find_generator(p, n)
    H = [1] * n
    for e in range(1, n):
        H[e] = H[e - 1] * g % p
    dlog = {v: e for e, v in enumerate(H)}
    assert len(dlog) == n, "generator order defect"
    Hset = set(H)
    A = [(1 - h) % p for h in H if h != 1]
    assert all(a != 0 for a in A)
    return g, H, dlog, Hset, A


def product_counter(A, p):
    """P(t) for all t, exact, via halved symmetric loop."""
    cnt = Counter()
    m = len(A)
    for i in range(m):
        a = A[i]
        cnt[a * a % p] += 1
        for j in range(i + 1, m):
            cnt[a * A[j] % p] += 2
    return cnt


def signed_support(dlog, half, x, y, p):
    coeff = {}
    for value, c in ((x * y % p, 1), (x, -1), (y, -1)):
        e = dlog[value]
        coord = e % half
        sign = 1 if e < half else -1
        coeff[coord] = coeff.get(coord, 0) + c * sign
    return {k: v for k, v in coeff.items() if v}


def fiber_measure(t, p, n, H, dlog, Hset, inv_shift, Pcount, diag_count,
                  check_identities=True):
    """Exact per-target measurement: reps, generic members, N_6^disj, R, class.

    Returns dict with keys P, reps, N6disj, R, antipodal, X18-style data.
    """
    half = n // 2
    reps = set()
    for x in H:
        if x == 1:
            continue
        y = (1 - t * inv_shift[x]) % p
        if y in Hset and y != 1:
            reps.add((x, y) if x <= y else (y, x))
    diag = sum(1 for (x, y) in reps if x == y)
    ordered = 2 * len(reps) - diag
    if check_identities:
        # DSP3: P(t) = 2|S_t| - diag(t); the r <-> {x,y} bijection.
        assert ordered == Pcount, (t, ordered, Pcount)
        assert diag == diag_count, (t, diag, diag_count)
        params = {}
        for (x, y) in reps:
            r = x * y % p
            assert r not in params or params[r] == (x, y)
            # roots of Q_(t,r): X^2-(1+r-t)X+r
            assert (x * x - (1 + r - t) * x + r) % p == 0
            assert (y * y - (1 + r - t) * y + r) % p == 0
            params[r] = (x, y)
        assert len(params) == len(reps)

    generic = []  # (r, support-dict, pair)
    for (x, y) in reps:
        sup = signed_support(dlog, half, x, y, p)
        if len(sup) == 3 and set(abs(v) for v in sup.values()) == {1}:
            generic.append((x * y % p, sup, (x, y)))
    generic.sort()

    n6 = 0
    for i in range(len(generic)):
        ri, si, _ = generic[i]
        ki = set(si)
        for j in range(i + 1, len(generic)):
            rj, sj, _ = generic[j]
            disjoint = ki.isdisjoint(sj)
            if check_identities:
                dist = sum((si.get(k, 0) - sj.get(k, 0)) ** 2
                           for k in ki | set(sj))
                assert disjoint == (dist == 6), (t, ri, rj, dist)
            if disjoint:
                n6 += 1

    R = 0
    for z in H:
        if z == 1:
            continue
        w = (1 - t * (1 - z)) % p
        if w in Hset and w != 1:
            R += 1

    # antipodal classification, both forms
    anti_explicit = any(
        x * x % p == (1 - t) % p for x in H if x != 1 and x != p - 1)
    H2 = {h * h % p for h in H}
    anti_member = ((1 - t) % p) in H2 and ((1 - t) % p) != 1
    assert anti_explicit == anti_member, (t, anti_explicit, anti_member)
    return {"P": Pcount, "reps": len(reps), "diag": diag,
            "generic": len(generic), "N6": n6, "R": R,
            "antipodal": anti_explicit}


def row_measure(p: int, n: int, cutoffs=(RICH, CUTOFF), full=False,
                verbose=False):
    """Measure one row exactly (pure python).  Returns summary dict."""
    g, H, dlog, Hset, A = build_row(p, n)
    cnt = product_counter(A, p)
    assert cnt.get(0, 0) == 0
    P1 = cnt.get(1, 0)
    maxP = 0
    for t, c in cnt.items():
        if t != 1 and c > maxP:
            maxP = c
    rich = sorted(t for t, c in cnt.items() if t != 1 and c >= RICH)
    if full:
        rich = sorted(t for t in cnt if t != 1)

    fibers = {}
    if rich:
        diag_cnt = Counter(a * a % p for a in A)
        inv_shift = {x: pow((1 - x) % p, p - 2, p) for x in H if x != 1}
        for t in rich:
            fibers[t] = fiber_measure(t, p, n, H, dlog, Hset, inv_shift,
                                      cnt[t], diag_cnt.get(t, 0))

    out = {"n": n, "p": p, "gen": g, "maxP": maxP, "P1": P1,
           "rich": [], "X18": 0, "X35": 0}
    for q in cutoffs:
        out[f"D{q}_0"] = 0
        out[f"D{q}_A"] = 0
    for t in rich:
        f = fibers[t]
        cls = "A" if f["antipodal"] else "0"
        out["rich"].append((t, f["P"], f["R"], f["generic"], f["N6"], cls))
        out["X18"] += max(f["P"] - 18, 0) * f["R"]
        out["X35"] += max(f["P"] - 35, 0) * f["R"]
        for q in cutoffs:
            if f["P"] >= q:
                out[f"D{q}_{cls}"] += f["N6"] * f["R"]
    D0, DA = out[f"D{CUTOFF}_0"], out[f"D{CUTOFF}_A"]
    out["LHS"] = 80 * D0 + 136 * DA          # = 10*J^0 + 17*J^A, J = 8D
    out["RHSn2"] = RHS_CONST * n * n
    out["viol"] = out["LHS"] > out["RHSn2"]
    if verbose:
        print(f"ROWFULL n={n} p={p} gen={g} maxP={maxP} P(1)={P1} "
              f"rich={out['rich']} X18={out['X18']} X35={out['X35']} "
              f"D25=({D0},{DA}) LHS={out['LHS']} RHS={out['RHSn2']} "
              f"J25=({8*D0},{8*DA}) viol={out['viol']}")
    return out


def row_measure_np(p: int, n: int, cutoffs=(RICH, CUTOFF)):
    """numpy-accelerated row measurement (exact int64, overflow-asserted).

    P-counting via vectorized products + np.unique; every rich fiber is
    then measured in pure python (fiber_measure), whose DSP3 assertion
    cross-validates the numpy count for that target.  Same output shape
    as row_measure.
    """
    import numpy as np
    assert p < 3_037_000_499, "int64 overflow guard"
    g, H, dlog, Hset, A = build_row(p, n)
    Anp = np.array(A, dtype=np.int64)
    vals = []
    step = max(1, (1 << 23) // len(A))
    for i in range(0, len(A), step):
        vals.append(((Anp[i:i + step, None] * Anp[None, :]) % p).ravel())
    products = np.concatenate(vals)
    uniq, cnts = np.unique(products, return_counts=True)
    assert int(cnts.sum()) == (n - 1) ** 2
    assert uniq[0] != 0
    P1 = 0
    one = np.searchsorted(uniq, 1)
    if one < len(uniq) and uniq[one] == 1:
        P1 = int(cnts[one])
        cnts = cnts.copy()
        cnts[one] = 0
    maxP = int(cnts.max())
    rich = [int(t) for t in uniq[cnts >= RICH]]
    richP = {int(t): int(c) for t, c in zip(uniq[cnts >= RICH],
                                            cnts[cnts >= RICH])}
    out = {"n": n, "p": p, "gen": g, "maxP": maxP, "P1": P1,
           "rich": [], "X18": 0, "X35": 0}
    for q in cutoffs:
        out[f"D{q}_0"] = 0
        out[f"D{q}_A"] = 0
    if rich:
        diag_cnt = Counter(a * a % p for a in A)
        inv_shift = {x: pow((1 - x) % p, p - 2, p) for x in H if x != 1}
        for t in sorted(rich):
            f = fiber_measure(t, p, n, H, dlog, Hset, inv_shift,
                              richP[t], diag_cnt.get(t, 0))
            cls = "A" if f["antipodal"] else "0"
            out["rich"].append((t, f["P"], f["R"], f["generic"], f["N6"], cls))
            out["X18"] += max(f["P"] - 18, 0) * f["R"]
            out["X35"] += max(f["P"] - 35, 0) * f["R"]
            for q in cutoffs:
                if f["P"] >= q:
                    out[f"D{q}_{cls}"] += f["N6"] * f["R"]
    D0, DA = out[f"D{CUTOFF}_0"], out[f"D{CUTOFF}_A"]
    out["LHS"] = 80 * D0 + 136 * DA
    out["RHSn2"] = RHS_CONST * n * n
    out["viol"] = out["LHS"] > out["RHSn2"]
    return out


def control_row_totals(p: int, n: int, mutate_edges=False):
    """Router-verify.py normalization: ALL targets (incl. t=1), cutoff 0.

    Returns (targets, edges, raw_records) exactly as
    f3_h3_disjoint_distance_six_split_pencil_router/verify.py row_check.
    """
    g, H, dlog, Hset, A = build_row(p, n)
    cnt = product_counter(A, p)
    diag_cnt = Counter(a * a % p for a in A)
    inv_shift = {x: pow((1 - x) % p, p - 2, p) for x in H if x != 1}
    targets = edges = records = 0
    for t in sorted(cnt):
        f = fiber_measure(t, p, n, H, dlog, Hset, inv_shift,
                          cnt[t], diag_cnt.get(t, 0))
        targets += 1
        edges += f["N6"]
        records += 8 * f["N6"] * f["R"]
    if mutate_edges:  # MC-1: deliberate corruption, REQUIRED to trip
        edges += 1
        records += 8
    return targets, edges, records


def kv(args, key, default=None):
    for a in args:
        if a.startswith(key + "="):
            return a.split("=", 1)[1]
    return default


def mode_control(args):
    mutate = "mutate_edges" in args
    rhs = int(kv(args, "rhs", str(RHS_CONST)))
    rows = ((17, 8), (97, 16), (193, 16))
    T = E = R = 0
    for p, n in rows:
        t_, e_, r_ = control_row_totals(p, n, mutate_edges=mutate)
        print(f"CONTROL row=({p},{n}) targets={t_} edges={e_} raw_records={r_}")
        T, E, R = T + t_, E + e_, R + r_
    print(f"CONTROL TOTALS rows=3 targets={T} edges={E} raw_records={R} "
          f"mutate_edges={mutate}")
    exp = kv(args, "expect")
    if exp:
        et, ee, er = (int(v) for v in exp.split(","))
        match = (T, E, R) == (et, ee, er)
        print(f"CONTROL EXPECT targets={et} edges={ee} raw_records={er} -> "
              f"{'MATCH' if match else 'MISMATCH'}")
    # MC-2 / kill-detector exercise on the three control rows with rhs arg
    for p, n in rows:
        out = row_measure(p, n)
        lhs = out["LHS"]
        trip = lhs > rhs * n * n
        print(f"KILLCHECK row=({p},{n}) LHS={lhs} rhs_const={rhs} "
              f"RHS={rhs * n * n} viol={trip}")
    # PC-3: DSP3 identity over ALL targets of the wave-14 toy row (32,1153)
    out = row_measure(1153, 32, full=True, verbose=False)
    print(f"PC3 row=(1153,32) all-fiber DSP3/DSP4/class assertions PASS "
          f"(fibers={len(out['rich'])})")
    # numpy-vs-pure cross-check on toy rows (only meaningful where numpy is
    # available, i.e. the Modal image)
    try:
        import numpy as np  # noqa: F401
        for p, n in ((97, 16), (193, 16), (1153, 32)):
            pure = product_counter(build_row(p, n)[4], p)
            npc = numpy_pcounts(p, n)
            assert all(npc[t] == c for t, c in pure.items())
            assert int(npc.sum()) == (n - 1) ** 2
            print(f"XCHECK numpy-vs-pure P-counts row=({p},{n}) MATCH")
    except ImportError:
        print("XCHECK numpy unavailable locally - SKIPPED (runs on Modal)")


def numpy_pcounts(p: int, n: int):
    import numpy as np
    assert p < 3_037_000_499, "int64 overflow guard"
    A = np.array(build_row(p, n)[4], dtype=np.int64)
    counts = np.zeros(p, dtype=np.int64)
    step = max(1, (1 << 23) // len(A))
    for i in range(0, len(A), step):
        block = (A[i:i + step, None] * A[None, :]) % p
        counts += np.bincount(block.ravel(), minlength=p)
    return counts


def mode_scan(args):
    n = int(kv(args, "n"))
    mstart = int(kv(args, "mstart"))
    mend = int(kv(args, "mend"))
    pmax = min(int(kv(args, "pmax", str(10 ** 7))), corridor_top(n))
    t0 = time.time()
    use_np = False
    if n >= 512:
        try:
            import numpy  # noqa: F401
            use_np = True
        except ImportError:
            pass
    rows = vac = 0
    worst = (0, 1, None)  # (LHS, RHS, p) worst exact ratio
    best_maxP = (0, None, None)
    rich_rows = []
    d19max = (0, 0, None)
    last_m = mstart
    for m in range(mstart, mend):
        p = n * m + 1
        if p < n * n or p > pmax:
            continue
        if time.time() - t0 > 230:
            print(f"PARTIAL shard n={n} stopped at m={m} (time guard); "
                  f"remaining [{m},{mend}) DEFERRED")
            break
        if not isprime(p):
            continue
        out = row_measure_np(p, n) if use_np else row_measure(p, n)
        rows += 1
        last_m = m
        if out["maxP"] > best_maxP[0]:
            best_maxP = (out["maxP"], p, None)
        if not out["rich"]:
            vac += 1
        else:
            rich_rows.append(p)
            print(f"ROW n={n} p={p} maxP={out['maxP']} rich={out['rich']} "
                  f"X18={out['X18']} X35={out['X35']} "
                  f"D25=({out['D25_0']},{out['D25_A']}) "
                  f"D19=({out['D19_0']},{out['D19_A']}) "
                  f"LHS={out['LHS']} RHS={out['RHSn2']} viol={out['viol']}")
            d19 = 80 * out["D19_0"] + 136 * out["D19_A"]
            if d19 * d19max[1] > d19max[0] * (RHS_CONST * n * n) or d19max[2] is None:
                d19max = (d19, RHS_CONST * n * n, p)
        if out["LHS"] * worst[1] > worst[0] * out["RHSn2"]:
            worst = (out["LHS"], out["RHSn2"], p)
        if out["viol"]:
            print(f"KILL1-CANDIDATE n={n} p={p} LHS={out['LHS']} "
                  f"RHS={out['RHSn2']} - REPLAY REQUIRED")
    print(f"SHARD n={n} m=[{mstart},{mend}) pmax={pmax} rows={rows} "
          f"vacuous={vac} rich_rows={rich_rows} "
          f"best_maxP={best_maxP[0]}@p={best_maxP[1]} "
          f"worst_LHS={worst[0]}/{worst[1]}@p={worst[2]} "
          f"maxD19w={d19max[0]}/{d19max[1]}@p={d19max[2]} last_m={last_m} "
          f"secs={time.time() - t0:.1f}")


def mode_highp(args):
    n = int(kv(args, "n"))
    count = int(kv(args, "count"))
    start = int(kv(args, "start"))
    top = corridor_top(n)
    m = (start - 1) // n + 1
    found = 0
    while found < count:
        p = n * m + 1
        m += 1
        if p <= start or p > top:
            assert p <= top, "left analogue corridor"
            continue
        if not isprime(p):
            continue
        out = row_measure(p, n, verbose=False)
        found += 1
        print(f"HIGHP n={n} p={p} maxP={out['maxP']} rich={out['rich']} "
              f"LHS={out['LHS']} RHS={out['RHSn2']} viol={out['viol']}")


def mode_official(args):
    import numpy as np
    n = int(kv(args, "n"))
    first = int(kv(args, "first"))
    must = [int(v) for v in kv(args, "must", "").split(",") if v]
    primes = []
    m = n  # p = n*m+1 >= n^2  =>  m >= n
    while len(primes) < first:
        p = n * m + 1
        m += 1
        if isprime(p):
            primes.append(p)
    for p in must:
        if p not in primes:
            primes.append(p)
    for p in primes:
        t0 = time.time()
        counts = numpy_pcounts(p, n)
        assert int(counts[0]) == 0
        P1 = int(counts[1])
        c = counts.copy()
        c[1] = 0
        maxP = int(c.max())
        rich = [int(t) for t in np.nonzero(c >= RICH)[0]]
        # pure-python exact recount of every rich fiber (verdict path)
        g, H, dlog, Hset, A = build_row(p, n)
        Aset = set(A)
        diag_cnt = Counter(a * a % p for a in A) if rich else Counter()
        inv_shift = ({x: pow((1 - x) % p, p - 2, p) for x in H if x != 1}
                     if rich else {})
        D = {(q, cls): 0 for q in (RICH, CUTOFF) for cls in "0A"}
        X18 = X35 = 0
        richinfo = []
        for t in rich:
            pc = sum(1 for a in A if t * pow(a, p - 2, p) % p in Aset)
            assert pc == int(counts[t]), (t, pc, int(counts[t]))
            f = fiber_measure(t, p, n, H, dlog, Hset, inv_shift,
                              pc, diag_cnt.get(t, 0))
            cls = "A" if f["antipodal"] else "0"
            richinfo.append((t, f["P"], f["R"], f["generic"], f["N6"], cls))
            X18 += max(f["P"] - 18, 0) * f["R"]
            X35 += max(f["P"] - 35, 0) * f["R"]
            for q in (RICH, CUTOFF):
                if f["P"] >= q:
                    D[(q, cls)] += f["N6"] * f["R"]
        lhs = 80 * D[(CUTOFF, "0")] + 136 * D[(CUTOFF, "A")]
        rhs = RHS_CONST * n * n
        print(f"OFFICIAL n={n} p={p} gen={g} maxP={maxP} P(1)={P1} "
              f"rich={richinfo} X18={X18} X35={X35} "
              f"D25=({D[(CUTOFF,'0')]},{D[(CUTOFF,'A')]}) "
              f"D19=({D[(RICH,'0')]},{D[(RICH,'A')]}) "
              f"J25=({8*D[(CUTOFF,'0')]},{8*D[(CUTOFF,'A')]}) "
              f"LHS={lhs} RHS={rhs} viol={lhs > rhs} "
              f"secs={time.time() - t0:.1f}")


def mode_replay(args):
    n = int(kv(args, "n"))
    p = int(kv(args, "p"))
    assert isprime(p) and (p - 1) % n == 0
    full = n <= 64 or "full" in args
    row_measure(p, n, full=full, verbose=True)
    print("REPLAY complete (all identity assertions passed)")


def mode_xcheck(args):
    """Dual-implementation exact cross-check of one row (verdict path).

    Pure-python Counter P-counts vs numpy unique P-counts compared in
    full; then both row measurements compared field by field.
    """
    import numpy as np
    n = int(kv(args, "n"))
    p = int(kv(args, "p"))
    assert isprime(p) and (p - 1) % n == 0
    pure_cnt = product_counter(build_row(p, n)[4], p)
    Anp = np.array(build_row(p, n)[4], dtype=np.int64)
    assert p < 3_037_000_499
    prods = ((Anp[:, None] * Anp[None, :]) % p).ravel()
    uniq, cnts = np.unique(prods, return_counts=True)
    np_cnt = {int(t): int(c) for t, c in zip(uniq, cnts)}
    assert pure_cnt == np_cnt, "P-counter mismatch"
    a = row_measure(p, n, verbose=True)
    b = row_measure_np(p, n)
    keys = ["n", "p", "maxP", "P1", "rich", "X18", "X35",
            "D19_0", "D19_A", "D25_0", "D25_A", "LHS", "RHSn2", "viol"]
    for k in keys:
        assert a[k] == b[k], (k, a[k], b[k])
    print(f"XCHECK n={n} p={p} pure-vs-numpy FULL MATCH "
          f"(targets={len(pure_cnt)}) LHS={a['LHS']} viol={a['viol']}")


def main():
    args = sys.argv[1:]
    assert args, __doc__
    mode = args[0]
    dispatch = {"control": mode_control, "scan": mode_scan,
                "highp": mode_highp, "official": mode_official,
                "replay": mode_replay, "xcheck": mode_xcheck}
    dispatch[mode](args[1:])


if __name__ == "__main__":
    main()
