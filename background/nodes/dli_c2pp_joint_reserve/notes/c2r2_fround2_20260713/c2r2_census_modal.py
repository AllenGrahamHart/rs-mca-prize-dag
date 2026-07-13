#!/usr/bin/env python3
"""C2'' F-ROUND 2: NEW n=64 tower rows (app rs-mca-dli-c2r2).

Extends M1 (m1_dli_m1_tower_census_modal.py) to new (t,q) rows for F-a widening
(t=2 octave 14 q=17729; t=3 octaves 9-10 q=641/1153), F-c census extension
(t=2 q=11777,13697,15361,17729), and F-b search. The MEASUREMENT KERNELS below
are COPIED VERBATIM from M1 (fiber_contribs, joint_grid_census, proj_*,
even_null_census, signed_all_census, decompose_row, lam_window, mitm dict) so the
coset-strip, accident decomposition (theta=2), and /33 convention are IDENTICAL.
Only the row list + planner + entrypoint differ. House Modal law: every function
call < 280 s, <=16 GB, wide .map() fan-out; shard0 gate reproduces the banked
8-row n=32 record + n64 strategy-B==C (positive control) and aborts on FAIL.
"""
import json, math
from collections import defaultdict

try:
    import modal
    app = modal.App("rs-mca-dli-c2r2")
    image = modal.Image.debian_slim().pip_install("numpy")
except ImportError:
    modal = None
    class _App:
        def function(self, **kw): return lambda f: f
        def local_entrypoint(self, **kw): return lambda f: f
    app = _App(); image = None

N64 = 64
THETA = 2.0
FULL_GRID_MAX_CELLS = 2.6e8
RATE_DERATED = 2.5e8
TARGET_SHARD_S = 90.0            # well under the 280 s ceiling (M1 used 120)

BANKED_F2B = {
    (2, 97): (443841, 1.0268181623599442, 1.0286044319148024),
    (2, 193): (223041, 0.5223792934931246, 0.5171675677689829),
    (2, 8353): (10881, 0.05293631100082713, 0.012451587195224463),
    (2, 32801): (7713, 0.033190716971347074, 0.003951799255511239),
    (3, 97): (443841, 0.014852165527745296, 0.01429144858675763),
    (3, 193): (223041, 0.004591084150447676, 0.0039458522287911316),
    (4, 97): (4369, 0.040283817807278556, 0.01429144858675763),
    (4, 193): (1137, 0.014072119613016711, 0.0039458522287911316),
}
BANKED_F2B_RATIOS = {
    (2, 97): (0.9982634047652964, 0.9982643827159152, 0.9981285990617759),
    (2, 193): (1.010077441140837, 1.0096559781116154, 1.0091643748453256),
    (2, 8353): (4.2513705418317835, 2.751522241871854, 2.690883197134267),
    (2, 32801): (8.398887399216648, 0.0, 0.0),
    (3, 97): (1.0392344371239752, 1.0334167782499855, 1.0332762131764144),
    (3, 193): (1.1635215624519777, 1.066158533199014, 1.0656394187395681),
    (4, 97): (2.8187358029336016, 2.8741696984709986, 2.868010384467522),
    (4, 193): (3.566306794344376, 0.0, 0.0),
}

# ------------------------------------------------------------- field helpers
def least_primitive_root(q):
    x, d, fac = q - 1, 2, []
    while d * d <= x:
        while x % d == 0:
            fac.append(d); x //= d
        d += 1
    if x > 1: fac.append(x)
    fac = sorted(set(fac))
    return next(c for c in range(2, q)
                if all(pow(c, (q - 1) // r, q) != 1 for r in fac))

def get_zeta(q, n):
    assert (q - 1) % n == 0, f"mu_{n} does not exist in F_{q}"
    z = pow(least_primitive_root(q), (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z

def fiber_contribs(q, n, t):
    h, e, o = n // 2, t // 2, (t + 1) // 2
    zeta = get_zeta(q, n)
    out = []
    for i in range(h):
        w = [pow(zeta, (2 * s * i) % n, q) for s in range(1, e + 1)]
        v = [pow(zeta, ((2 * s + 1) * i) % n, q) for s in range(o)]
        cN = tuple([0] * t)
        cB = tuple([2 * x % q for x in w] + [0] * o)
        cP = tuple(w + v)
        cM = tuple(w + [(q - x) % q for x in v])
        out.append((cN, cB, cP, cM))
    return out

def joint_grid_census(q, n, t):
    import numpy as np
    h = n // 2; fib = fiber_contribs(q, n, t); axes = tuple(range(t))
    dp = np.zeros((q,) * t + (h + 1,), dtype=np.int64); dp[(0,) * t + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = dp + np.roll(dp, cB, axis=axes)
        tp = np.roll(dp, cP, axis=axes); new[..., 1:] += tp[..., :-1]; del tp
        tm = np.roll(dp, cM, axis=axes); new[..., 1:] += tm[..., :-1]; del tm
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * t]]

def proj_directions(q, m):
    import itertools
    dirs = []
    for lead in range(m):
        for tail in itertools.product(range(q), repeat=m - 1 - lead):
            dirs.append((0,) * lead + (1,) + tail)
    assert len(dirs) == (q ** m - 1) // (q - 1)
    return dirs

def joint_proj_chunk(q, n, t, g, dirs):
    import numpy as np
    h = n // 2; m = t - g; fib = fiber_contribs(q, n, t); gaxes = tuple(range(g + 1))
    total = [0] * (h + 1)
    for d in dirs:
        assert len(d) == m
        dp = np.zeros((q,) * g + (q, h + 1), dtype=np.int64); dp[(0,) * (g + 1) + (0,)] = 1
        for (cN, cB, cP, cM) in fib:
            sB = tuple(cB[:g]) + (sum(a * b for a, b in zip(d, cB[g:])) % q,)
            sP = tuple(cP[:g]) + (sum(a * b for a, b in zip(d, cP[g:])) % q,)
            sM = tuple(cM[:g]) + (sum(a * b for a, b in zip(d, cM[g:])) % q,)
            new = dp + np.roll(dp, sB, axis=gaxes)
            tp = np.roll(dp, sP, axis=gaxes); new[..., 1:] += tp[..., :-1]; del tp
            tm = np.roll(dp, sM, axis=gaxes); new[..., 1:] += tm[..., :-1]; del tm
            dp = new
            assert int(dp.max()) < (1 << 61)
        row = dp[(0,) * (g + 1)]
        for k in range(h + 1): total[k] += int(row[k])
    return total

def ref_census(q, n, t, g):
    import numpy as np
    h = n // 2
    if g == 0:
        return [math.comb(h, k) * (2 ** h) for k in range(h + 1)]
    fib = fiber_contribs(q, n, t); gaxes = tuple(range(g))
    dp = np.zeros((q,) * g + (h + 1,), dtype=np.int64); dp[(0,) * g + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = dp + np.roll(dp, cB[:g], axis=gaxes)
        tp = np.roll(dp, cP[:g], axis=gaxes); new[..., 1:] += tp[..., :-1]
        tm = np.roll(dp, cM[:g], axis=gaxes); new[..., 1:] += tm[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * g]]

def assemble_from_projection(q, n, t, g, sum_over_dirs, n_ref):
    h = n // 2; m = t - g; c1 = (q ** (m - 1) - 1) // (q - 1); div = q ** (m - 1)
    cs = []
    for k in range(h + 1):
        num = sum_over_dirs[k] - c1 * n_ref[k]
        assert num % div == 0, f"PROJECTION IDENTITY BROKEN k={k} q={q} t={t} g={g}"
        cs.append(num // div); assert cs[k] >= 0
    return cs

def even_null_census(q, n, t):
    import numpy as np
    h, e = n // 2, t // 2; fib = fiber_contribs(q, n, t); axes = tuple(range(e))
    dp = np.zeros((q,) * e + (h + 1,), dtype=np.int64); dp[(0,) * e + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = dp + np.roll(dp, cB[:e], axis=axes)
        ts = np.roll(dp, cP[:e], axis=axes); new[..., 1:] += ts[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * e]]

def signed_all_census(q, n, t):
    import numpy as np
    h, e, o = n // 2, t // 2, (t + 1) // 2; fib = fiber_contribs(q, n, t); axes = tuple(range(o))
    dp = np.zeros((q,) * o + (h + 1,), dtype=np.int64); dp[(0,) * o + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = 2 * dp
        tp = np.roll(dp, cP[e:], axis=axes); new[..., 1:] += tp[..., :-1]
        tm = np.roll(dp, cM[e:], axis=axes); new[..., 1:] += tm[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * o]]

def mitm_joint_census_dict(q, n, t):
    h = n // 2; fib = fiber_contribs(q, n, t)
    def half(fibers):
        agg = defaultdict(int); agg[((0,) * t, 0)] = 1
        for i in fibers:
            cN, cB, cP, cM = fib[i]; nxt = defaultdict(int)
            for (key, k), c in agg.items():
                for con, dk in ((cN, 0), (cB, 0), (cP, 1), (cM, 1)):
                    nk = tuple((a + b) % q for a, b in zip(key, con)); nxt[(nk, k + dk)] += c
            agg = nxt
        return agg
    L = half(range(0, h // 2)); R = half(range(h // 2, h))
    Rbykey = defaultdict(dict)
    for (key, k), c in R.items(): Rbykey[key][k] = Rbykey[key].get(k, 0) + c
    cs = [0] * (h + 1)
    for (key, kL), cL in L.items():
        nk = tuple((q - a) % q for a in key)
        for kR, cR in Rbykey.get(nk, {}).items(): cs[kL + kR] += cL * cR
    return cs

def lam_window(h, k, q, o):
    return math.comb(h, k) * (2 ** k) / (2 * h * (q ** o))

def decompose_row(q, n, t, cn, cs, asum, theta=THETA):
    h, o = n // 2, (t + 1) // 2
    an = [math.comb(h, k) * (2 ** (h - k)) for k in range(h + 1)]
    n_all = 3 ** h; assert sum(an) == n_all
    n_null, s_null, s_all = sum(cn), sum(cs), sum(asum)
    Ec = s_null / n_null if n_null else float('nan'); Eu = s_all / n_all
    ratio = Ec / Eu if Eu > 0 else float('nan')
    sn1, nn1 = s_null - cs[0], n_null - cn[0]
    sa1, na1 = s_all - asum[0], n_all - an[0]
    Ec1 = sn1 / nn1 if nn1 else float('nan'); Eu1 = sa1 / na1 if na1 else float('nan')
    r1 = Ec1 / Eu1 if (Eu1 and Eu1 > 0) else float('nan')
    r2 = (sn1 / n_null) / (sa1 / n_all) if sa1 else float('nan')
    accid = []
    for k in range(1, h + 1):
        Eck = cs[k] / cn[k] if cn[k] else 0.0
        Euk = asum[k] / an[k] if an[k] else 0.0
        if Euk > 0 and Eck / Euk > theta and cs[k] > 0: accid.append((k, Eck / Euk, cs[k]))
        elif Euk == 0 and cs[k] > 0: accid.append((k, float('inf'), cs[k]))
    acc_ks = {k for k, _, _ in accid}
    bn = sum(cn[k] for k in range(1, h + 1) if k not in acc_ks)
    bs = sum(cs[k] for k in range(1, h + 1) if k not in acc_ks)
    un = sum(an[k] for k in range(1, h + 1) if k not in acc_ks)
    us = sum(asum[k] for k in range(1, h + 1) if k not in acc_ks)
    Ecb = bs / bn if bn else float('nan'); Eub = us / un if un else float('nan')
    bulk = (Ecb / Eub if (Eub and Eub > 0) else (0.0 if Ecb == 0 else float('nan')))
    Vk, V_flags = {}, []
    for k in range(1, h + 1):
        pat, rem = divmod(asum[k], 2 ** (h - k)); assert rem == 0
        vq, vr = divmod(pat, 2 * h); Vk[k] = vq if vr == 0 else pat / (2 * h)
        if vr: V_flags.append(k)
    acc_list = [{"k": k, "class_ratio": (r if r != float('inf') else 'inf'),
                 "mass": mm, "quanta": mm / (2 * h), "quantized": (mm % (2 * h) == 0),
                 "lam": lam_window(h, k, q, o)} for k, r, mm in accid]
    return {"q": q, "n": n, "t": t, "n_null": n_null, "s_null": s_null,
            "E_cond": Ec, "E_uncond": Eu, "ratio": ratio,
            "stripped_mean_ratio": r1, "stripped_mass_ratio": r2, "bulk_ratio": bulk,
            "coset": {"cn0": cn[0], "cs0": cs[0], "an0": an[0], "asum0": asum[0]},
            "accidents": acc_list, "V_orbits": {k: Vk[k] for k in Vk if Vk[k]},
            "suborbit_flags": V_flags,
            "table": {k: [cn[k], cs[k], an[k], asum[k]]
                      for k in range(h + 1) if cn[k] or cs[k] or asum[k]}}

# ------------------------------------------------------------ Modal wrappers
def _shard0(spec):
    report, ok = [], True
    for (t, q), (nn, Ec, Eu) in sorted(BANKED_F2B.items()):
        cs = mitm_joint_census_dict(q, 32, t); cn = even_null_census(q, 32, t)
        asum = signed_all_census(q, 32, t); d = decompose_row(q, 32, t, cn, cs, asum)
        r0, r1, r2 = BANKED_F2B_RATIOS[(t, q)]
        row_ok = (d["n_null"] == nn and abs(d["E_cond"] - Ec) < 1e-12
                  and abs(d["E_uncond"] - Eu) < 1e-12 and abs(d["ratio"] - r0) < 1e-12)
        ok &= row_ok
        report.append({"row": [t, q], "ok": row_ok})
    csB = joint_grid_census(193, N64, 2); dirs = proj_directions(193, 2)
    csC = assemble_from_projection(193, N64, 2, 0,
            joint_proj_chunk(193, N64, 2, 0, dirs), ref_census(193, N64, 2, 0))
    n64_ok = (csB == csC)
    return {"ok": bool(ok and n64_ok), "banked_replay": report, "n64_B_eq_C": n64_ok}

def _full_row(spec):
    q, t = spec["q"], spec["t"]
    cs = joint_grid_census(q, N64, t); cn = even_null_census(q, N64, t); asum = signed_all_census(q, N64, t)
    return {"spec": spec, "cs": cs, "cn": cn, "asum": asum}

def _dirs_chunk(spec):
    q, t, g = spec["q"], spec["t"], spec["g"]
    dirs = [tuple(d) for d in spec["dirs"]]
    s = joint_proj_chunk(q, N64, t, g, dirs)
    return {"spec": {k: spec[k] for k in ("q", "t", "g", "chunk_id")},
            "ndirs": len(dirs), "sum_dirs": s}

def _marginals(spec):
    q, t, g = spec["q"], spec["t"], spec["g"]
    return {"spec": spec, "cn": even_null_census(q, N64, t),
            "asum": signed_all_census(q, N64, t), "n_ref": ref_census(q, N64, t, g)}

if modal is not None:
    shard0_gate = app.function(image=image, cpu=2, memory=4096, timeout=280)(_shard0)
    census_row_full = app.function(image=image, cpu=4, memory=16384, timeout=280)(_full_row)
    census_row_dirs = app.function(image=image, cpu=4, memory=12288, timeout=280)(_dirs_chunk)
    row_marginals = app.function(image=image, cpu=2, memory=8192, timeout=280)(_marginals)

def _plan_dir_row(q, t, g, phase):
    h = N64 // 2
    dirs = proj_directions(q, t - g)
    cells = (q ** (g + 1)) * (h + 1)
    ops_per_dir = 5 * h * cells
    per_chunk = max(1, int(TARGET_SHARD_S * RATE_DERATED / ops_per_dir))
    chunks = [{"q": q, "t": t, "g": g, "phase": phase, "chunk_id": i,
               "dirs": [list(d) for d in dirs[i:i + per_chunk]]}
              for i in range(0, len(dirs), per_chunk)]
    return {"q": q, "t": t, "g": g, "phase": phase, "ndirs": len(dirs), "chunks": chunks,
            "est_s_per_chunk": ops_per_dir * min(per_chunk, len(dirs)) / RATE_DERATED}

@app.local_entrypoint()
def main(rows: str = "2:11777,2:13697,2:15361,2:17729,3:641",
         shard0: bool = True, out: str = "c2r2_new_rows.json", dry: bool = False):
    specs = []
    for tok in rows.split(","):
        if not tok.strip(): continue
        t, q = tok.split(":"); specs.append((int(t), int(q)))
    full, dirrows = [], []
    for (t, q) in specs:
        full_cells = (q ** t) * 33          # TRUE full-grid size (q,)*t + 33
        if full_cells <= FULL_GRID_MAX_CELLS:
            full.append({"q": q, "t": t})
        else:                               # direction-shard: g = t-2 (m=2 block)
            g = t - 2
            dirrows.append(_plan_dir_row(q, t, g, "p%d" % (t - 1)))
    nchunks = sum(len(r["chunks"]) for r in dirrows)
    print(f"C2R2 PLAN: shard0={shard0}, rows={specs}")
    print(f"  {len(full)} full-grid rows, {len(dirrows)} dir-sharded rows "
          f"({nchunks} chunks + {len(dirrows)} marginal workers)")
    for r in dirrows:
        print(f"  dirs row q={r['q']} t={r['t']} g={r['g']}: {r['ndirs']} dirs in "
              f"{len(r['chunks'])} chunks (~{r['est_s_per_chunk']:.0f}s/chunk)")
    if dry:
        print("DRY RUN -- nothing launched."); return

    if shard0:
        g0 = shard0_gate.remote({})
        print(f"SHARD 0 (banked replay + n64 B==C): {'PASS' if g0['ok'] else 'FAIL'}")
        if not g0["ok"]:
            print(json.dumps(g0, indent=1, default=str)); raise SystemExit("SHARD 0 FAILED")

    rows_out = []
    for res in census_row_full.map(full, return_exceptions=True):
        if not isinstance(res, dict): raise SystemExit(f"full-row error: {res}")
        sp = res["spec"]
        rows_out.append(decompose_row(sp["q"], N64, sp["t"], res["cn"], res["cs"], res["asum"]))
    all_chunks = [c for r in dirrows for c in r["chunks"]]
    marg_specs = [{"q": r["q"], "t": r["t"], "g": r["g"]} for r in dirrows]
    chunk_res = list(census_row_dirs.map(all_chunks, return_exceptions=True))
    marg_res = list(row_marginals.map(marg_specs, return_exceptions=True))
    bad = [c for c in chunk_res + marg_res if not isinstance(c, dict)]
    if bad: raise SystemExit(f"worker error(s): {bad[:3]}")
    for r in dirrows:
        key = (r["q"], r["t"], r["g"])
        parts = [c for c in chunk_res if (c["spec"]["q"], c["spec"]["t"], c["spec"]["g"]) == key]
        ndirs = sum(p["ndirs"] for p in parts)
        assert ndirs == r["ndirs"], f"row {key}: {ndirs}/{r['ndirs']} dirs"
        sum_dirs = [sum(p["sum_dirs"][k] for p in parts) for k in range(N64 // 2 + 1)]
        marg = next(mm for mm in marg_res
                    if (mm["spec"]["q"], mm["spec"]["t"], mm["spec"]["g"]) == key)
        cs = assemble_from_projection(r["q"], N64, r["t"], r["g"], sum_dirs, marg["n_ref"])
        rows_out.append(decompose_row(r["q"], N64, r["t"], marg["cn"], cs, marg["asum"]))

    print("\nNEW ROWS (n=64):")
    for d in sorted(rows_out, key=lambda x: (x["t"], x["q"])):
        acc = ", ".join(f"k={a['k']}:{a['class_ratio']}x m={a['mass']}" for a in d["accidents"]) or "-"
        print(f"  t={d['t']} q={d['q']:>6}: raw={d['ratio']:8.4f} "
              f"strip_mass={d['stripped_mass_ratio'] if d['stripped_mass_ratio']==d['stripped_mass_ratio'] else float('nan'):8.4f} "
              f"BULK={d['bulk_ratio'] if d['bulk_ratio']==d['bulk_ratio'] else float('nan'):8.4f} | acc: {acc}")
    with open(out, "w") as fh:
        json.dump({"rows": rows_out}, fh, indent=1, default=str)
    print(f"\nwrote {out}  ({len(rows_out)} rows)")
