#!/usr/bin/env python3
"""P-A1 widening cost: empirical band population on the banked toy fixtures.

Machinery COPIED (not edited) from the pinned
  critical/nodes/xr_smallcore_spread_count/notes/audit_p8p9_local_20260710.py
(ray enumeration by W-scan, interpolation, T1 moment, S1 sunflower cap, H1).
The expensive I1/I2 census checks are dropped; new measurements added:

  B1  core-band census: cross-pair cores J split into  J==k | J in [k+1,A-2]
      | J >= A-1  (the pencil-cascade-paid tier)
  B2  incremental population: high-core RAYS and distinct SLOPES under the
      current predicate (J==k) vs the widened predicate (J>=k)
  B3  H1 margin on the widened class (the pinned file already uses J>=k)
  B4  sunflower cap S1 with W ranging over k-subsets of LARGER cores
  B5  line/pencil population cap: mult(core) vs floor((n-w)/(A-w)) and vs the
      banked floor(R/h) that (CLB2) prints for w=k

Run: tools/ramguard local -- python3 <this>
"""
import itertools, random, json
from math import comb

random.seed(20260710)          # same seed as the pinned file
q = 97


def inv(a): return pow(a, q - 2, q)


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return out


def interp_coeffs(xs, ys, k):
    coeff = [0] * k
    for i in range(k):
        num = [1]
        for j in range(k):
            if j == i:
                continue
            num = polymul(num, [(-xs[j]) % q, 1])
        den = 1
        for j in range(k):
            if j == i:
                continue
            den = den * ((xs[i] - xs[j]) % q) % q
        w = ys[i] * inv(den) % q
        for d_ in range(len(num)):
            coeff[d_] = (coeff[d_] + w * num[d_]) % q
    return tuple(coeff)


def evalp(c, x):
    r = 0
    for co in reversed(c):
        r = (r * x + co) % q
    return r


def mk_pair(n, kind, k):
    if kind == "random":
        return ([random.randrange(q) for _ in range(n)],
                [random.randrange(1, q) for _ in range(n)])
    if kind == "nearpencil":
        c0 = [random.randrange(q) for _ in range(k)]
        w0 = [random.randrange(q) for _ in range(k)]
        z0 = random.randrange(1, q)
        D = list(range(1, n + 1))
        u = [(evalp(tuple(c0), D[i]) + z0 * evalp(tuple(w0), D[i])) % q
             for i in range(n)]
        v = [evalp(tuple(w0), D[i]) % q for i in range(n)]
        for _ in range(3):
            i = random.randrange(n)
            u[i] = (u[i] + random.randrange(1, q)) % q
            j = random.randrange(n)
            v[j] = (v[j] + random.randrange(1, q)) % q
        v = [vv if vv != 0 else 1 for vv in v]
        return u, v
    raise ValueError


RESULTS = []
FAILS = []


def run_row(n, k, t, pairs_spec):
    A = k + t
    R, h, r = n - k, t, n - A
    D = list(range(1, n + 1))
    band = (k + 1, A - 2)
    print(f"\n== row n={n}, k={k}, t=h={t}, A={A}, R={R}, r={r}, q={q} ==")
    print(f"   band [k+1,A-2] = [{band[0]},{band[1]}]  "
          f"(width {max(0, band[1] - band[0] + 1)});  "
          f"widened class = cores in [{k},{A-2}];  floor(R/h)={R//h}")
    Wsets = list(itertools.combinations(range(n), k))
    for name, (u, v) in pairs_spec:
        rays = {}
        for z in range(q):
            Uz = [(u[i] + z * v[i]) % q for i in range(n)]
            seen = set()
            for W in Wsets:
                c = interp_coeffs([D[i] for i in W], [Uz[i] for i in W], k)
                if c in seen:
                    continue
                seen.add(c)
                s = sum(1 for i in range(n) if evalp(c, D[i]) == Uz[i])
                if s >= A:
                    rays[(z, c)] = frozenset(i for i in range(n)
                                             if evalp(c, D[i]) == Uz[i])
        raylist = list(rays.items())
        nslopes = len({z for (z, c) in rays})

        # k-set multiplicities and the T1 moment
        mult = {}
        for (z, c), s in rays.items():
            for W in itertools.combinations(sorted(s), k):
                mult[W] = mult.get(W, 0) + 1
        moment = sum(comb(m, 2) for m in mult.values())

        # cross pairs
        cross = []
        for a in range(len(raylist)):
            for b in range(a + 1, len(raylist)):
                (z1, c1), s1 = raylist[a]
                (z2, c2), s2 = raylist[b]
                if z1 == z2:
                    continue
                cross.append((a, b, len(s1 & s2), s1 & s2))

        # ---- B1 core-band census -------------------------------------
        eq = sum(1 for _, _, J, _ in cross if J == k)
        bd = sum(1 for _, _, J, _ in cross if k + 1 <= J <= A - 2)
        casc = sum(1 for _, _, J, _ in cross if J >= A - 1)
        hist = {}
        for _, _, J, _ in cross:
            if J >= k:
                hist[J] = hist.get(J, 0) + 1

        # ---- B2 incremental population --------------------------------
        hc_eq_r, hc_wide_r = set(), set()
        hc_eq_s, hc_wide_s = set(), set()
        for a, b, J, _ in cross:
            (z1, _c1), _ = raylist[a]
            (z2, _c2), _ = raylist[b]
            if J == k:
                hc_eq_r |= {a, b}
                hc_eq_s |= {z1, z2}
            if J >= k:
                hc_wide_r |= {a, b}
                hc_wide_s |= {z1, z2}
        # band-only slopes = widened minus current
        band_only_s = hc_wide_s - hc_eq_s

        # ---- B3 H1 margins --------------------------------------------
        h1_wide = len(hc_wide_r) <= 2 * moment
        h1_eq = len(hc_eq_r) <= 2 * moment
        if not (h1_wide and h1_eq):
            FAILS.append(f"{name}: H1")

        # ---- B4 sunflower cap over k-subsets of larger cores ----------
        s1_ok, s1_ok_sub, worst_all, worst_sub = True, True, 0, 0
        subW = set()
        for _, _, J, core in cross:
            if J > k:
                for W in itertools.combinations(sorted(core), k):
                    subW.add(W)
        n_skip = 0
        for W, mm in mult.items():
            if mm < 2:
                continue
            P = interp_coeffs([D[i] for i in W], [u[i] for i in W], k)
            Q = interp_coeffs([D[i] for i in W], [v[i] for i in W], k)
            d_ = sum(1 for i in range(n) if i not in W
                     and evalp(Q, D[i]) == v[i] and evalp(P, D[i]) == u[i])
            if t - d_ <= 0:
                n_skip += 1
                continue
            cap = (n - k) // (t - d_)
            worst_all = max(worst_all, mm)
            if mm > cap:
                s1_ok = False
            if W in subW:
                worst_sub = max(worst_sub, mm)
                if mm > cap:
                    s1_ok_sub = False
        if not (s1_ok and s1_ok_sub):
            FAILS.append(f"{name}: S1")

        # ---- B5 line/pencil population cap at each core size ----------
        # for each distinct core of size w >= k, count live SLOPES whose ray
        # support contains it  (== L(P_W,Q_W) for the forced pair, by T4)
        corepop = {}
        seen_core = set()
        for _, _, J, core in cross:
            # w >= A-1 is the pencil-cascade tier (paid, outside the widened
            # class); w = A would divide by zero in the (n-w)/(A-w) cap.
            if J < k or J > A - 2 or core in seen_core:
                continue
            seen_core.add(core)
            w = J
            L = len({z for (z, c), s in rays.items() if core <= s})
            capw = (n - w) // (A - w)
            capk = R // h
            rec = corepop.setdefault(w, dict(ncores=0, maxL=0, cap_w=capw,
                                             cap_Rh=capk, viol_w=0, viol_Rh=0))
            rec["ncores"] += 1
            rec["maxL"] = max(rec["maxL"], L)
            if L > capw:
                rec["viol_w"] += 1
            if L > capk:
                rec["viol_Rh"] += 1

        print(f"  -- {name}: {len(rays)} rays, {nslopes} live slopes, "
              f"{len(cross)} cross pairs, moment={moment}")
        print(f"     B1 cores: J==k {eq} | band[{band[0]},{band[1]}] {bd} | "
              f"J>=A-1 {casc}   hist={dict(sorted(hist.items()))}")
        print(f"     B2 high-core RAYS   : ==k {len(hc_eq_r):4d}  "
              f">=k {len(hc_wide_r):4d}  (+{len(hc_wide_r)-len(hc_eq_r)})")
        print(f"     B2 high-core SLOPES : ==k {len(hc_eq_s):4d}  "
              f">=k {len(hc_wide_s):4d}  (+{len(band_only_s)} band-only)")
        print(f"     B3 H1  widened {len(hc_wide_r)} <= 2*{moment} : {h1_wide}"
              f"   margin x{(2*moment/max(1,len(hc_wide_r))):.1f}"
              f" | current {len(hc_eq_r)} <= 2*{moment} : {h1_eq}")
        print(f"     B4 S1  all-W ok={s1_ok} (max mult {worst_all}); "
              f"k-subsets-of-larger-cores ok={s1_ok_sub} "
              f"(#such W {len(subW)}, max mult {worst_sub}); "
              f"tangent-skipped W {n_skip}")
        for w in sorted(corepop):
            rec = corepop[w]
            print(f"     B5 core size {w}: {rec['ncores']} distinct cores, "
                  f"max #slopes-through-core {rec['maxL']}, "
                  f"cap (n-w)/(A-w)={rec['cap_w']} viol {rec['viol_w']}, "
                  f"banked floor(R/h)={rec['cap_Rh']} viol {rec['viol_Rh']}")
        RESULTS.append(dict(row=f"n{n}k{k}t{t}", pair=name, n=n, k=k, t=t, A=A,
                            rays=len(rays), slopes=nslopes, moment=moment,
                            cross=len(cross), J_eq_k=eq, J_band=bd,
                            J_cascade=casc, hist=hist,
                            hc_rays_eq=len(hc_eq_r), hc_rays_wide=len(hc_wide_r),
                            hc_slopes_eq=len(hc_eq_s),
                            hc_slopes_wide=len(hc_wide_s),
                            band_only_slopes=len(band_only_s),
                            H1_wide=h1_wide, H1_eq=h1_eq,
                            S1_all=s1_ok, S1_subsets=s1_ok_sub,
                            n_subW=len(subW), max_mult=worst_all,
                            max_mult_sub=worst_sub,
                            corepop={str(w): corepop[w] for w in corepop}))


# ---------------------------------------------------------------- fixtures
# (i) the two PINNED rows of audit_p8p9_local_20260710.py, same seed/order
n1, k1 = 12, 6
pairs1 = [(f"rand{i}", mk_pair(n1, "random", k1)) for i in range(3)] + \
         [(f"np{i}", mk_pair(n1, "nearpencil", k1)) for i in range(2)]
run_row(n1, k1, 2, pairs1)

n2, k2 = 10, 4
pairs2 = [(f"rand{i}", mk_pair(n2, "random", k2)) for i in range(2)] + \
         [(f"np{i}", mk_pair(n2, "nearpencil", k2)) for i in range(1)]
run_row(n2, k2, 3, pairs2)

# (ii) NEW wide-band rows (t=4,5): the pinned rows have band width 0 and 1
for (n3, k3, t3, nrand, nnp) in [(10, 3, 4, 3, 1), (12, 4, 4, 3, 1),
                                 (12, 5, 4, 2, 1), (12, 4, 5, 2, 1)]:
    ps = [(f"rand{i}", mk_pair(n3, "random", k3)) for i in range(nrand)] + \
         [(f"np{i}", mk_pair(n3, "nearpencil", k3)) for i in range(nnp)]
    run_row(n3, k3, t3, ps)

print()
print("FAILS:", len(FAILS), FAILS)
with open("notes/pilots_20260802/p_a1_widening_cost/band_measure.json", "w") as fh:
    json.dump(RESULTS, fh, indent=1)
print("checkpoint written: band_measure.json")
