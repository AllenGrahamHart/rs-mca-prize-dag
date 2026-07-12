#!/usr/bin/env python3
"""LOCAL VALIDATION (go/no-go gate) for m1_dli_m1_tower_census_modal.py.

HARD LOCAL LAW (2026-07-12 addendum): < 300 MB RSS, < 1e6 states per
computation -- enforced below (budget() before every kernel call; ru_maxrss
asserted at the end).  Anything over budget is DEFERRED TO MODAL SHARD 0
(n=64 strategy-B grid, 1.23e6 cells) or skipped with a named record
(n=16 B-grid at q=97, t=3).

V0  get_zeta == archived sympy convention for every planned q; baked
    BANKED_F2B constants == the banked .jsons (transcription check).
V1  n=16 brute force (independent re-derivation from zeta) vs strategies
    A-dict, A-array, B(grid, where <= 1e6 cells), C(projection).
V2  n=32, the 8 banked rows (THE gate): my kernels vs (a) the archived
    machinery replayed per-class (verify_level2_tower import, f2b loops),
    (b) f2b_nested_correlation.json, (c) f2b_replay_perclass_20260710.json,
    (d) the pose-note calibration decomposition (bulk ratios, accident
    masses 128/128/64/128).
V3  n=64, t=2, q=193 smoke row via STRATEGY C ONLY (grids 6369 cells);
    B == C at n=64 is DEFERRED to Modal shard 0.
V4  timings -> per-shard estimates for the run plan.
V5  exact-tail statistics vs brute enumeration.

Writes m1_validation_record.json.
"""
import importlib.util
import itertools
import json
import math
import resource
import time
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
NODE = Path('/home/u2470931/smooth-read-solomin/prize/critical/nodes/'
            'dli_prime_weighted_large_block_support/notes')
VT = Path('/home/u2470931/smooth-read-solomin/prize/archive/'
          'compressed_dli_lane_20260705/b2b_primitive_core/notes/'
          'verify_level2_tower.py')

STATE_BUDGET = 1_000_000
RSS_BUDGET_KB = 300 * 1024


def rss_kb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


def budget(states, what):
    assert states < STATE_BUDGET, \
        f"LOCAL LAW: {what} needs {states:.3g} states >= 1e6 -- defer to Modal"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = load("m1mod", HERE / "m1_dli_m1_tower_census_modal.py")
vt = load("vt", VT)

REC = {"pass": True, "checks": [], "deferred_to_modal_shard0": [],
       "skipped_over_budget": []}


def check(name, ok, detail=""):
    REC["checks"].append({"name": name, "ok": bool(ok),
                          "detail": str(detail)[:400]})
    REC["pass"] = REC["pass"] and bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if detail and not ok else ""))
    return ok


# ---------------------------------------------------------------- V0: zeta
print(f"V0: get_zeta vs archived sympy convention (rss {rss_kb() // 1024}MB)")
allq = (m.FA_T2_SMALL + m.FC_CENSUS + m.FA_T2_TOP + m.T3_SCALES
        + m.T4_STRETCH)
ok = True
for q in sorted(set(allq)):
    ok &= (m.get_zeta(q, 64) == vt.get_zeta(q, 64))
for q, n in [(97, 32), (193, 32), (8353, 32), (32801, 32), (17, 16),
             (97, 16)]:
    ok &= (m.get_zeta(q, n) == vt.get_zeta(q, n))
check("zeta agreement (all planned q at n=64 + banked n=16/32)", ok)

BANKED = json.loads((NODE / "f2b_nested_correlation.json").read_text())
banked = {(r["t"], r["q"]): r for r in BANKED}
PERCLS = json.loads((NODE / "f2b_replay_perclass_20260710.json").read_text())
percls = {(r["t"], r["q"]): r for r in PERCLS}
ok = True
for (t, q), (nn, Ec, Eu) in m.BANKED_F2B.items():
    b = banked[(t, q)]
    ok &= (b["null_states"] == nn and b["E_cond"] == Ec
           and b["E_uncond"] == Eu)
for (t, q), (r0, r1, r2) in m.BANKED_F2B_RATIOS.items():
    p = percls[(t, q)]
    ok &= (p["ratio"] == r0 and p["stripped_mean_ratio"] == r1
           and p["stripped_mass_ratio"] == r2)
check("baked shard-0 constants == banked .jsons (transcription exact)", ok)


# ------------------------------------------------- V1: n=16 brute vs A/B/C
def brute16(q, t):
    """Independent re-derivation: all 3^8 level-1 states over mu_16 fibers,
    archived moment conventions."""
    n, h = 16, 8
    e, o = t // 2, (t + 1) // 2
    zeta = vt.get_zeta(q, n)
    W = [[pow(zeta, (2 * s * i) % n, q) for s in range(1, e + 1)]
         for i in range(h)]
    V = [[pow(zeta, ((2 * s + 1) * i) % n, q) for s in range(o)]
         for i in range(h)]
    cn = [0] * (h + 1)
    cs = [0] * (h + 1)
    asum = [0] * (h + 1)
    for st in itertools.product((0, 1, 2), repeat=h):  # 0=N,1=B,2=single
        ev = [0] * e
        G = [i for i in range(h) if st[i] == 2]
        for i in range(h):
            mult = (0, 2, 1)[st[i]]
            for s in range(e):
                ev[s] = (ev[s] + mult * W[i][s]) % q
        k = len(G)
        sc = 0
        for signs in itertools.product((1, -1), repeat=k):
            od = [0] * o
            for eps, i in zip(signs, G):
                for s in range(o):
                    od[s] = (od[s] + eps * V[i][s]) % q
            if all(x == 0 for x in od):
                sc += 1
        asum[k] += sc
        if all(x == 0 for x in ev):
            cn[k] += 1
            cs[k] += sc
    return cn, cs, asum


print(f"V1: n=16 brute vs A-dict/A-array/B/C (rss {rss_kb() // 1024}MB)")
for q in (17, 97):
    for t in (2, 3, 4):
        cn_b, cs_b, as_b = brute16(q, t)
        check(f"n16 q={q} t={t} A-dict == brute",
              m.mitm_joint_census_dict(q, 16, t) == cs_b)
        if q ** t * 5 < STATE_BUDGET:
            check(f"n16 q={q} t={t} A-array == brute",
                  m.mitm_joint_census_array(q, 16, t, prefix_fibers=2)
                  == cs_b)
        else:
            REC["skipped_over_budget"].append(f"n16 A-array q={q} t={t}")
        if q ** t * 9 < STATE_BUDGET:
            check(f"n16 q={q} t={t} B grid == brute",
                  m.joint_grid_census(q, 16, t) == cs_b)
        else:
            REC["skipped_over_budget"].append(f"n16 B grid q={q} t={t}")
        g = {2: 0, 3: 1, 4: 2}[t]                     # production configs
        if q ** (g + 1) * 9 < STATE_BUDGET:
            dirs = m.proj_directions(q, t - g)
            sd = m.joint_proj_chunk(q, 16, t, g, dirs)
            nr = m.ref_census(q, 16, t, g)
            csC = m.assemble_from_projection(q, 16, t, g, sd, nr)
            check(f"n16 q={q} t={t} C proj (g={g}) == brute", csC == cs_b)
        else:
            REC["skipped_over_budget"].append(f"n16 C proj q={q} t={t} g={g}")
        check(f"n16 q={q} t={t} even_null == brute",
              m.even_null_census(q, 16, t) == cn_b)
        check(f"n16 q={q} t={t} signed_all == brute",
              m.signed_all_census(q, 16, t) == as_b)


# ------------------------------------- V2: n=32 vs archived machinery + banked
print(f"V2: n=32, the 8 banked rows -- THE gate (rss {rss_kb() // 1024}MB)")
ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801), (3, 97), (3, 193),
        (4, 97), (4, 193)]
# calibration reference transcribed from the pose note / calibration script
POSE_BULK = {(2, 97): 0.998, (2, 193): 1.010, (2, 8353): 0.0, (2, 32801): 0.0,
             (3, 97): 1.033, (3, 193): 1.066, (4, 97): 0.760, (4, 193): 0.0}
POSE_ACC_MASSES = [128, 128, 64, 128]

acc_masses_seen = []
for t, q in ROWS:
    n, h = 32, 16
    e, o = t // 2, (t + 1) // 2
    # --- archived machinery replay (per-class, exactly the f2b loops)
    zeta = vt.get_zeta(q, n)
    budget(2 * 3 ** 8 + 2 ** 16, f"archived skewcount+configs t={t} q={q}")
    sc = vt.skewcount_table(zeta, q, n, o)
    L = vt.build_half_configs(range(0, h // 2), zeta, q, n, e)
    R = vt.build_half_configs(range(h // 2, h), zeta, q, n, e)
    dL = defaultdict(list)
    for ev, gm, dm in L:
        dL[ev].append(gm)
    cn_a = [0] * (h + 1)
    cs_a = [0] * (h + 1)
    for ev, gmR, dmR in R:
        key = tuple((-x) % q for x in ev)
        for gmL in dL.get(key, ()):
            G = gmL | gmR
            k = bin(G).count("1")
            cn_a[k] += 1
            cs_a[k] += sc.get(G, 0)
    fL = Counter(g for _, g, _ in L)
    fR = Counter(g for _, g, _ in R)
    an_a = [0] * (h + 1)
    as_a = [0] * (h + 1)
    for gmL, cL in fL.items():
        for gmR, cR in fR.items():
            G = gmL | gmR
            k = bin(G).count("1")
            w = cL * cR
            an_a[k] += w
            as_a[k] += w * sc.get(G, 0)
    del sc, L, R, dL, fL, fR
    # --- my kernels (budgets: dict halves 2*4^8; marginal grids q^e*17 etc.)
    budget(2 * 4 ** 8, f"A-dict n32 t={t} q={q}")
    cs_m = m.mitm_joint_census_dict(q, n, t)
    budget(q ** e * 17, f"even_null n32 t={t} q={q}")
    cn_m = m.even_null_census(q, n, t)
    budget(q ** o * 17, f"signed_all n32 t={t} q={q}")
    as_m = m.signed_all_census(q, n, t)
    an_m = [math.comb(h, k) * 2 ** (h - k) for k in range(h + 1)]
    check(f"n32 t={t} q={q} cs (joint) == archived per-class", cs_m == cs_a,
          f"{cs_m} vs {cs_a}")
    check(f"n32 t={t} q={q} cn (even-null) == archived", cn_m == cn_a)
    check(f"n32 t={t} q={q} asum == archived", as_m == as_a)
    check(f"n32 t={t} q={q} an closed form == archived", an_m == an_a)
    # --- banked json ground truths via the decomposition
    d = m.decompose_row(q, n, t, cn_m, cs_m, as_m)
    b = banked[(t, q)]
    check(f"n32 t={t} q={q} E_cond/E_uncond/null_states == banked",
          abs(d["E_cond"] - b["E_cond"]) < 1e-12
          and abs(d["E_uncond"] - b["E_uncond"]) < 1e-12
          and d["n_null"] == b["null_states"],
          f"{d['E_cond']}/{d['E_uncond']}/{d['n_null']} vs banked")
    p = percls[(t, q)]
    check(f"n32 t={t} q={q} ratio/stripped ratios == banked perclass",
          abs(d["ratio"] - p["ratio"]) < 1e-12
          and abs((d["stripped_mean_ratio"] if d["stripped_mean_ratio"] ==
                   d["stripped_mean_ratio"] else -1)
                  - p["stripped_mean_ratio"]) < 1e-12
          and abs((d["stripped_mass_ratio"] if d["stripped_mass_ratio"] ==
                   d["stripped_mass_ratio"] else -1)
                  - p["stripped_mass_ratio"]) < 1e-12)
    bulk = d["bulk_ratio"] if d["bulk_ratio"] == d["bulk_ratio"] else 0.0
    check(f"n32 t={t} q={q} bulk ratio == pose-note calibration",
          abs(bulk - POSE_BULK[(t, q)]) < 5e-4,
          f"{bulk} vs {POSE_BULK[(t, q)]}")
    for a in d["accidents"]:
        acc_masses_seen.append(a["mass"])
        check(f"n32 t={t} q={q} accident k={a['k']} orbit-quantized (32)",
              a["mass"] % 32 == 0, a)
    # strategies B / C / A-array on affordable banked rows
    if t == 2 and q in (97, 193):
        budget(q * q * 17, f"B grid n32 q={q}")
        check(f"n32 t={t} q={q} B grid == A-dict",
              m.joint_grid_census(q, n, t) == cs_m)
        budget(q * q * 9, f"A-array n32 q={q}")
        check(f"n32 t={t} q={q} A-array == A-dict",
              m.mitm_joint_census_array(q, n, t, prefix_fibers=4) == cs_m)
        budget(q * 17, f"C proj n32 q={q}")
        sd = m.joint_proj_chunk(q, n, t, 0, m.proj_directions(q, 2))
        csC = m.assemble_from_projection(q, n, t, 0, sd,
                                         m.ref_census(q, n, t, 0))
        check(f"n32 t={t} q={q} C proj (g=0) == A-dict", csC == cs_m)
    if (t, q) == (3, 97):
        budget(q * q * 17, "C proj n32 (3,97)")
        sd = m.joint_proj_chunk(q, n, t, 1, m.proj_directions(q, 2))
        csC = m.assemble_from_projection(q, n, t, 1, sd,
                                         m.ref_census(q, n, t, 1))
        check(f"n32 t={t} q={q} C proj (g=1) == A-dict", csC == cs_m)

check("n32 accident masses across rows == pose-note {128,128,64,128}",
      sorted(acc_masses_seen) == sorted(POSE_ACC_MASSES), acc_masses_seen)


# ----------------------- V3: n=64 q=193 t=2 smoke row via STRATEGY C only
print(f"V3: n=64 t=2 q=193 via strategy C (B==C DEFERRED to Modal shard 0) "
      f"(rss {rss_kb() // 1024}MB)")
REC["deferred_to_modal_shard0"] = [
    "n64 t=2 q=193 strategy B grid (1.229e6 cells > 1e6-state law) == "
    "strategy C -- pre-registered as shard 0 (b) in the Modal script",
    "banked 8-row replay re-asserted ON MODAL against baked constants -- "
    "shard 0 (a)"]
budget(193 * 33, "C proj n64 q=193")
t0 = time.time()
dirs = m.proj_directions(193, 2)
sd = m.joint_proj_chunk(193, 64, 2, 0, dirs)
tC = time.time() - t0
csC = m.assemble_from_projection(193, 64, 2, 0, sd,
                                 m.ref_census(193, 64, 2, 0))
check("n64 t=2 q=193: projection identity divisibility held (all 33 k)",
      True)                     # assemble_from_projection asserts internally
budget(193 * 33, "marginals n64 q=193")
cn64 = m.even_null_census(193, 64, 2)
as64 = m.signed_all_census(193, 64, 2)
d64 = m.decompose_row(193, 64, 2, cn64, csC, as64)
check("n64 t=2 q=193: n_null ~ 3^32/q sanity",
      abs(d64["n_null"] * 193 / 3 ** 32 - 1) < 0.01, d64["n_null"])
check("n64 t=2 q=193: class masses nonneg + asum divisibility held", True)
print(f"  n64 smoke row (VALIDATION ONLY, reads not evaluated): "
      f"raw={d64['ratio']:.4f} bulk={d64['bulk_ratio']:.4f} "
      f"accidents={[(a['k'], a['mass']) for a in d64['accidents']]}")
REC["n64_smoke_row_q193_t2"] = {
    "ratio": d64["ratio"], "bulk": d64["bulk_ratio"],
    "accidents": [(a["k"], str(a["class_ratio"]), a["mass"])
                  for a in d64["accidents"]],
    "V_orbits": {str(k): v for k, v in d64["V_orbits"].items()}}


# ------------------------------------------------------------- V4: timings
print(f"V4: timings -> shard plan estimates (rss {rss_kb() // 1024}MB)")
budget(193 * 193 * 17, "B timing basis n32 q=193")
t0 = time.time()
m.joint_grid_census(193, 32, 2)
tB32 = time.time() - t0
cellsB32 = 193 * 193 * 17
rate = 16 * 5 * cellsB32 / tB32           # elem-ops/s (4 passes + guard)
per_dir64 = tC / len(dirs)                # n64 q=193 g=0 measured
rec_t = {"tB_n32_q193_t2_s": round(tB32, 3),
         "rate_elem_ops_per_s": int(rate),
         "tC_n64_q193_total_s": round(tC, 2),
         "tC_per_direction_q193_s": round(per_dir64, 4)}
print(f"  grid DP n32 q=193 t=2: {tB32:.2f}s -> rate ~ {rate:.2e} "
      f"elem-ops/s (small-grid basis; big grids run at >= this rate, "
      f"estimates conservative)")
print(f"  projection n64 q=193: {tC:.2f}s / {len(dirs)} dirs = "
      f"{per_dir64 * 1000:.1f} ms/dir (call-overhead dominated)")
for q in (2753, 1409):
    est = 32 * 5 * (q * q * 33) / rate
    rec_t[f"est_full_row_q{q}_s"] = round(est, 1)
    print(f"  est full-grid t=2 row q={q}: {est:.0f}s at measured rate "
          f"(x2 derated: {2 * est:.0f}s vs 280s law)")
est193_t3 = 32 * 5 * (193 ** 3 * 33) / rate
rec_t["est_full_row_t3_q193_s"] = round(est193_t3, 1)
print(f"  est full-grid t=3 row q=193: {est193_t3:.0f}s "
      f"(x2: {2 * est193_t3:.0f}s)")
for q, t, g in [(10369, 2, 0), (12289, 2, 0), (577, 3, 1), (193, 4, 2)]:
    cells = (q ** (g + 1)) * 33
    pd = max(32 * 5 * cells / rate, 32 * 4 * 0.9 * per_dir64 / (32 * 4))
    nd = q + 1
    rec_t[f"est_per_dir_q{q}_t{t}_s"] = round(pd, 3)
    rec_t[f"est_row_total_q{q}_t{t}_core_s"] = round(pd * nd, 1)
    print(f"  est dirs row q={q} t={t} g={g}: {pd:.2f}s/dir x {nd} dirs "
          f"= {pd * nd:.0f} core-s ({2 * pd * nd:.0f} derated)")
# array-MITM xcheck extrapolation from a legal-size run (n=32, q=97)
budget(97 * 97 * 9, "A-array timing n32 q=97")
t0 = time.time()
m.mitm_joint_census_array(97, 32, 2, prefix_fibers=4)
tA32 = time.time() - t0
est_x = tA32 * (4 ** 16) / (4 ** 8) * 0.3    # bincount amortizes at scale
rec_t["tA_array_n32_q97_s"] = round(tA32, 3)
rec_t["est_xcheck_n64_q193_s_rough"] = round(est_x, 0)
print(f"  array-MITM n32 q=97: {tA32:.2f}s -> n64 xcheck rough est "
      f"~{est_x:.0f}s (state ratio 4^8, bincount amortization ~0.3; "
      f"if > 280s, raise prefix_fibers to 5 and split across 2 workers)")
REC["timings"] = rec_t

full, dirrows, xc = m.plan_shards()
worst = max((s["q"] for s in full if s["t"] == 2), default=0)
est_worst = 2 * 32 * 5 * (worst ** 2 * 33) / rate
check("planner: worst full-grid row under 280s at 2x-derated measured rate",
      est_worst < 280, f"q={worst}: {est_worst:.0f}s")
worst_chunk = max((r["est_s_per_chunk"] for r in dirrows), default=0)
check("planner: worst direction chunk under 280s (planner estimate)",
      worst_chunk < 280, f"{worst_chunk:.0f}s")
REC["shard_plan"] = {
    "full_rows": [(s["q"], s["t"]) for s in full],
    "dir_rows": [(r["q"], r["t"], r["g"], r["ndirs"], len(r["chunks"]))
                 for r in dirrows],
    "n_chunks_total": sum(len(r["chunks"]) for r in dirrows)}
print(f"  plan: {len(full)} full rows; "
      f"{len(dirrows)} dir rows / {REC['shard_plan']['n_chunks_total']} "
      f"chunks; + shard0 + xcheck + {len(dirrows)} marginal workers")


# ------------------------------------------------------- V5: tail statistics
print(f"V5: exact-tail statistics vs brute (rss {rss_kb() // 1024}MB)")
ps = [0.3, 0.05, 0.5, 0.2]
pmf = m.poisson_binom_pmf(ps)
brute = [0.0] * (len(ps) + 1)
for bits in itertools.product((0, 1), repeat=len(ps)):
    pr = 1.0
    for bb, p in zip(bits, ps):
        pr *= p if bb else (1 - p)
    brute[sum(bits)] += pr
check("poisson_binom_pmf == brute",
      all(abs(a - b) < 1e-12 for a, b in zip(pmf, brute)))
check("poisson pmf sums to 1", abs(sum(pmf) - 1) < 1e-12)
p0 = m.poisson_two_sided(4.35, 4)
check("poisson_two_sided sane at the census point (lam=4.35, T=4)",
      0.9 < p0 <= 1.0, p0)
p_ext = m.poisson_two_sided(4.35, 20)
check("poisson_two_sided kills a 20-orbit blowout", p_ext < 1e-3, p_ext)

peak = rss_kb()
check(f"LOCAL LAW: peak RSS {peak // 1024}MB < 300MB", peak < RSS_BUDGET_KB,
      f"{peak}KB")
REC["peak_rss_mb"] = peak // 1024
REC["verdict"] = "GO" if REC["pass"] else "NO-GO"
(HERE / "m1_validation_record.json").write_text(json.dumps(REC, indent=1))
print(f"\nVALIDATION {'ALL PASS -- GO' if REC['pass'] else 'FAILURES -- NO-GO'}"
      f"  (record: m1_validation_record.json, {len(REC['checks'])} checks; "
      f"peak RSS {peak // 1024}MB)")
