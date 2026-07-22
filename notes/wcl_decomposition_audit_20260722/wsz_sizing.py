#!/usr/bin/env python3
"""wsz_sizing.py -- ITEM 4: exact Burnside sizing of every open WCL cell.

Audited conventions (notes/wcl_decomposition_audit_20260722/wcl_audit_findings.md):
cell (ell, w): reduced signed weight-w polynomial, support = w-subset of
[0, N), N = 256*ell, signs +-1 mod global sign; root of exact order n' = 2N.
Equivalent root form: antipodal-free w-subset R of Z_{n'} (element r encodes
s*omega^e with e = r mod N, s = +1 if r < N else -1).  Global sign =
translation by N; signed shift = translation by b; odd Galois dilation =
multiplication by odd a.  So the census dedup group is the full affine group
    G_m = { x -> a*x + b mod m : a odd },  m = n' = 512*ell,  |G_m| = m*m/2,
acting on antipodal-free w-subsets of Z_m.  (Global sign quotient is INSIDE
G_m via b = m/2.)

Burnside: for f = (a,b), cycles of f on Z_m are permuted by the free
involution iota(x) = x + m/2 (commutes with f since a odd).  A fixed
antipodal-free subset is a union of f-cycles containing, from each
iota-pair of distinct cycles {C, iota(C)}, either nothing or exactly one of
the two, and never touching a self-paired cycle (iota(C) = C forces an
antipodal pair inside C).  Hence the fixed-subset generating function is
    prod over iota-pairs (1 + 2 z^{|C|}),
and #orbits(w) = (1/|G_m|) * sum_f [z^w] prod (1 + 2 z^{|C|}).

Conjugacy collapse: conjugating (a,b) by translation t gives (a, b + t(a-1)),
so for fixed a only b in {0..g-1}, g = gcd(a-1, m), need explicit cycle
finding; each class has m/g members.

Subcommands (each fits ramguard tiny separately; results appended to
wsz_sizing_results.json):
  selfcheck        exhaustive small-m validation of the Burnside machinery
  count M WMIN WMAX   exact orbit counts at modulus M for w in [WMIN, WMAX]
  pairs1514        reproduce the banked ell=2 pair-orbit count 1,514
  router K         (2,w=K+3) router-candidate orbit count (wclp model,
                   re-derived); K=4 must reproduce 94,652,815
  raw              exact raw signed-support counts for all open cells
  table            assemble the sizing table from the JSON results
"""
import json
import os
import sys
from itertools import combinations
from math import comb, gcd

SCRATCH = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(SCRATCH, "wsz_sizing_results.json")


def load_results():
    if os.path.exists(RESULTS):
        with open(RESULTS) as fh:
            return json.load(fh)
    return {}


def save_results(res):
    tmp = RESULTS + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
    os.replace(tmp, RESULTS)


# ----------------------------------------------------------------------
# core Burnside machinery
# ----------------------------------------------------------------------

def fixed_genfun(m, a, b, wmax):
    """[z^0..z^wmax] of prod over iota-pairs (1 + 2 z^{cycle length}) for
    the affine map x -> a x + b on Z_m, iota(x) = x + m/2."""
    half = m // 2
    cyc_id = [-1] * m
    lengths = []          # cycle id -> length
    first = []            # cycle id -> first element seen
    for s in range(m):
        if cyc_id[s] >= 0:
            continue
        cid = len(lengths)
        x = s
        n = 0
        while cyc_id[x] < 0:
            cyc_id[x] = cid
            x = (a * x + b) % m
            n += 1
        if cyc_id[x] != cid:
            raise AssertionError("non-permutation walk")
        lengths.append(n)
        first.append(s)
    poly = [0] * (wmax + 1)
    poly[0] = 1
    done = [False] * len(lengths)
    for cid, s in enumerate(first):
        if done[cid]:
            continue
        partner = cyc_id[(s + half) % m]
        done[cid] = True
        if partner == cid:
            continue          # self-paired: unusable
        done[partner] = True
        d = lengths[cid]
        if lengths[partner] != d:
            raise AssertionError("iota partner length mismatch")
        if d <= wmax:
            # poly *= (1 + 2 z^d), truncated
            for k in range(wmax, d - 1, -1):
                poly[k] += 2 * poly[k - d]
    return poly


def burnside_counts(m, wmin, wmax, progress=False):
    """Exact orbit counts of antipodal-free w-subsets of Z_m under G_m,
    for all w in [wmin, wmax]."""
    group = m * (m // 2)
    totals = [0] * (wmax + 1)
    aa = 0
    for a in range(1, m, 2):
        g = gcd(a - 1, m) if a != 1 else m
        cls = m // g
        for b in range(g):
            gf = fixed_genfun(m, a, b, wmax)
            for w in range(wmax + 1):
                totals[w] += cls * gf[w]
        aa += 1
        if progress and aa % 128 == 0:
            print(f"  ..a-progress {aa}/{m//2}", flush=True)
    out = {}
    for w in range(wmin, wmax + 1):
        if totals[w] % group:
            raise AssertionError(f"Burnside non-integer at m={m} w={w}")
        out[w] = totals[w] // group
    return out


# ----------------------------------------------------------------------
# selfcheck: exhaustive small-m validation
# ----------------------------------------------------------------------

def antipodal_free_subsets(m, w):
    half = m // 2
    for S in combinations(range(m), w):
        ok = True
        ss = set(S)
        for x in S:
            if (x + half) % m in ss:
                ok = False
                break
        if ok:
            yield S


def exhaustive_orbits(m, w):
    half = m // 2
    seen = set()
    orbits = 0
    for S in antipodal_free_subsets(m, w):
        if S in seen:
            continue
        orbits += 1
        for a in range(1, m, 2):
            for b in range(m):
                T = tuple(sorted((a * x + b) % m for x in S))
                seen.add(T)
    return orbits


def cmd_selfcheck():
    print("SELFCHECK: exhaustive vs Burnside on small moduli")
    all_ok = True
    for m, wlist in [(8, [1, 2, 3]), (16, [2, 3, 4, 5]), (32, [3, 5])]:
        bs = burnside_counts(m, min(wlist), max(wlist))
        for w in wlist:
            ex = exhaustive_orbits(m, w)
            ok = ex == bs[w]
            all_ok &= ok
            print(f"  m={m:3d} w={w}: exhaustive={ex:6d} burnside={bs[w]:6d} "
                  f"{'PASS' if ok else 'FAIL'}")
    # raw subset counts: antipodal-free w-subsets of Z_m = C(m/2,w)*2^w
    for m, w in [(16, 3), (32, 4)]:
        raw = sum(1 for _ in antipodal_free_subsets(m, w))
        ok = raw == comb(m // 2, w) * 2 ** w
        all_ok &= ok
        print(f"  m={m:3d} w={w}: raw subsets={raw} == C(m/2,w)*2^w "
              f"{'PASS' if ok else 'FAIL'}")
    # coset-descent orbit bijection: all-even orbits at m <-> all orbits at m/2
    for m, w in [(16, 3), (32, 3), (32, 5)]:
        half = m // 2
        seen = set()
        ev = 0
        for S in antipodal_free_subsets(m, w):
            if any(x % 2 for x in S):
                continue
            if S in seen:
                continue
            ev += 1
            for a in range(1, m, 2):
                for b in range(m):
                    T = tuple(sorted((a * x + b) % m for x in S))
                    if all(y % 2 == 0 for y in T):
                        seen.add(T)
        bs = burnside_counts(half, w, w)[w]
        ok = ev == bs
        all_ok &= ok
        print(f"  coset-descent m={m} w={w}: even-support orbits={ev} "
              f"burnside(m/2)={bs} {'PASS' if ok else 'FAIL'}")
    res = load_results()
    res["selfcheck"] = "PASS" if all_ok else "FAIL"
    save_results(res)
    print("SELFCHECK:", res["selfcheck"])
    if not all_ok:
        sys.exit(1)


# ----------------------------------------------------------------------
# calibration + production counts
# ----------------------------------------------------------------------

BANKED = {  # (m, w) -> banked exact affine-Galois class count
    (512, 3): 254,
    (512, 4): 24_979,
    (512, 5): 2_296_920,
    (512, 6): 185_569_028,
}


def cmd_count(m, wmin, wmax):
    print(f"BURNSIDE m={m} w in [{wmin},{wmax}]", flush=True)
    counts = burnside_counts(m, wmin, wmax, progress=(m >= 1024))
    res = load_results()
    key = f"orbits_m{m}"
    res.setdefault(key, {})
    for w, c in counts.items():
        res[key][str(w)] = c
        tag = ""
        if (m, w) in BANKED:
            tag = ("  == banked PASS" if c == BANKED[(m, w)]
                   else f"  != banked {BANKED[(m, w)]} FAIL")
        print(f"  m={m} w={w}: orbits={c}{tag}")
        if (m, w) in BANKED and c != BANKED[(m, w)]:
            sys.exit(1)
    save_results(res)


def cmd_pairs1514():
    """Banked anchor (b): unordered pairs {i,j} from Z_1024 \\ {0,512},
    (j-i) mod 1024 != 512, dedup by odd dilation ONLY -> 1,514 orbits.
    Independent implementation: Burnside over the 512 odd units."""
    M = 1024
    legal = 0
    fixed_total = 0
    for u in range(1, M, 2):
        # fixed points of x -> ux
        g = gcd(u - 1, M)
        # fixed elements = multiples of M/g; 0 and 512 always fixed (g even)
        fixed_legal = g - 2
        # legal pairs of fixed elements: antipodal-free; fixed set closed
        # under +512, so it contains fixed_legal/2 antipodal pairs
        pf = comb(fixed_legal, 2) - fixed_legal // 2
        # 2-cycles {i, ui}: u^2 i == i, ui != i, both legal, ui - i != 512
        h = 0
        for i in range(M):
            if i in (0, 512):
                continue
            j = u * i % M
            if j == i or j in (0, 512):
                continue
            if u * j % M != i:
                continue
            if (j - i) % M == 512:
                continue
            h += 1
        assert h % 2 == 0
        fixed_total += pf + h // 2
    # legal pair universe (u = 1 term) must be 521,220
    g1 = gcd(0, M)  # = 0 -> handle: u=1 fixes everything
    legal = comb(1022, 2) - 511
    assert fixed_total % 512 == 0
    orbits = fixed_total // 512
    print(f"legal pairs = {legal} (banked 521,220)")
    print(f"pair orbits under odd dilation = {orbits} (banked 1,514)")
    ok = legal == 521_220 and orbits == 1_514
    res = load_results()
    res["pairs_ell2"] = {"legal_pairs": legal, "orbits": orbits,
                         "status": "PASS" if ok else "FAIL"}
    save_results(res)
    print("PASS" if ok else "FAIL")
    if not ok:
        sys.exit(1)


# ----------------------------------------------------------------------
# (2,w) router-candidate orbit counts (wclp_b_count model, re-derived)
# ----------------------------------------------------------------------

def clean_pair_multiset(m_mod, t, maxlen):
    """{cycle length: #iota-pairs of clean cycles} for x -> t*x on Z_m."""
    half = m_mod // 2
    seen = [False] * m_mod
    cyc_id = [-1] * m_mod
    lengths = []
    first = []
    for s in range(m_mod):
        if seen[s]:
            continue
        cid = len(lengths)
        x = s
        n = 0
        while not seen[x]:
            seen[x] = True
            cyc_id[x] = cid
            x = x * t % m_mod
            n += 1
        lengths.append(n)
        first.append(s)
    out = {}
    done = [False] * len(lengths)
    for cid, s in enumerate(first):
        if done[cid]:
            continue
        partner = cyc_id[(s + half) % m_mod]
        done[cid] = True
        if partner == cid:
            continue
        done[partner] = True
        d = lengths[cid]
        if d <= maxlen:
            out[d] = out.get(d, 0) + 1
    return out


def n_inv_k(mult, k):
    """# legal k-subsets of Z_1024 invariant under the dilation whose clean
    iota-pair multiset is `mult`: choose iota-pairs with distinct
    pair-slots, cycle lengths summing to k, 2 orientations per chosen pair.
    Generating function prod (1 + 2 z^d)^{m_d}, coefficient of z^k."""
    poly = [0] * (k + 1)
    poly[0] = 1
    for d, cnt in mult.items():
        for _ in range(cnt):
            for j in range(k, d - 1, -1):
                poly[j] += 2 * poly[j - d]
    return poly[k]


def cmd_router(k):
    """(2, w=k+3) router-candidate orbit count.

    Model (audited (2,6) census / wclp_b_count.py, collapse re-derived):
    W = {(Q, c)}: Q a legal (antipodal-free) k-subset of Z_1024, c in
    Z_1024; H = dilations x scalings (t, r): (Q,c) -> (tQ+r, tc+3r),
    |H| = 512*1024.  Burnside collapses to
        orbits = (1/512) * sum_{t odd} N_inv_k(t)
    because for fixed t: sum_r fixQ(t,r)*#{c: (t-1)c = -3r} =
    g*sum_{g|r} fixQ(t,r) with g = gcd(t-1,1024) (3 odd => g|3r <=> g|r),
    and the multiples of g form a single translation-conjugacy class of r
    containing r = 0, so fixQ(t,r) = N_inv_k(t) on it: the inner sum is
    (1024/g)*g*N_inv_k(t) = 1024*N_inv_k(t)."""
    M = 1024
    total = 0
    for t in range(1, M, 2):
        mult = clean_pair_multiset(M, t, k)
        total += n_inv_k(mult, k)
    assert total % 512 == 0, total
    orbits = total // 512
    w = k + 3
    print(f"(2,{w}) router-candidate orbits (k={k}): {orbits}")
    if k == 3:
        print("  control: audited (2,6) census 404,740:",
              "PASS" if orbits == 404_740 else "FAIL")
        assert orbits == 404_740
    if k == 4:
        print("  anchor: Pilot B (2,7) census 94,652,815:",
              "PASS" if orbits == 94_652_815 else "FAIL")
        assert orbits == 94_652_815
    res = load_results()
    res.setdefault("router_orbits", {})[f"2,{w}"] = orbits
    save_results(res)


# ----------------------------------------------------------------------
# raw counts + final table
# ----------------------------------------------------------------------

OPEN_CELLS = [(1, 5), (1, 6), (1, 7), (1, 8),
              (2, 7), (2, 8), (2, 9),
              (4, 9), (4, 10), (4, 11)]


def cmd_raw():
    res = load_results()
    res.setdefault("raw", {})
    print("RAW reduced signed support counts  C(256*ell, w) * 2^(w-1):")
    for ell, w in OPEN_CELLS:
        n = comb(256 * ell, w) * 2 ** (w - 1)
        res["raw"][f"{ell},{w}"] = n
        print(f"  ({ell},{w}): {n:,}")
    # calibration anchors
    a3 = comb(256, 3) * 4
    a4 = comb(256, 4) * 8
    print(f"  anchor (1,3): {a3:,} (banked 11,054,080)",
          "PASS" if a3 == 11_054_080 else "FAIL")
    print(f"  anchor (1,4): {a4:,} (banked 1,398,341,120)",
          "PASS" if a4 == 1_398_341_120 else "FAIL")
    assert a3 == 11_054_080 and a4 == 1_398_341_120
    save_results(res)


RATE_A = 0.698     # s/row, (1,5)-style single-norm + complete-factor rows
RATE_B = 1.25      # s/orbit, (2,7)-style recursive-norm gcd-heavy orbits


def cmd_table():
    res = load_results()
    print("=" * 100)
    print("SIZING TABLE (exact counts; projections at banked rates)")
    print("=" * 100)
    hdr = (f"{'cell':7s} {'raw signed supports':>24s} {'affine-Galois orbits':>22s} "
           f"{'rate':>6s} {'CPU-hours':>14s} {'CPU-years':>10s}")
    print(hdr)
    for ell, w in OPEN_CELLS:
        m = 512 * ell
        raw = res["raw"][f"{ell},{w}"]
        orb = res.get(f"orbits_m{m}", {}).get(str(w))
        if orb is None:
            print(f"({ell},{w}) : orbit count MISSING")
            continue
        rate = RATE_A if ell == 1 else RATE_B
        cpuh = orb * rate / 3600.0
        print(f"({ell},{w}) {raw:>26,} {orb:>22,} {rate:>6.3f} "
              f"{cpuh:>14,.0f} {cpuh/8766:>10,.1f}")
    rr = res.get("router_orbits", {})
    if rr:
        print("-" * 100)
        print("(2,w) router-candidate (constraint-first) spaces, rate 1.25 s/orbit:")
        for key, orb in sorted(rr.items()):
            cpuh = orb * RATE_B / 3600.0
            print(f"  ({key}): {orb:>22,} orbits  -> {cpuh:>14,.0f} CPU-h "
                  f"({cpuh/8766:,.1f} CPU-y)")
    print("=" * 100)


def main():
    cmd = sys.argv[1]
    if cmd == "selfcheck":
        cmd_selfcheck()
    elif cmd == "count":
        cmd_count(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif cmd == "pairs1514":
        cmd_pairs1514()
    elif cmd == "router":
        cmd_router(int(sys.argv[2]))
    elif cmd == "raw":
        cmd_raw()
    elif cmd == "table":
        cmd_table()
    else:
        raise SystemExit("unknown subcommand")


if __name__ == "__main__":
    main()
