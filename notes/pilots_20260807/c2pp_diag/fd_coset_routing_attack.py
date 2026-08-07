#!/usr/bin/env python3
"""C2'' F-ROUND 3 -- falsifier family F-d (COSET-ROUTING NEUTRALITY).

Pre-registration: notes/pilots_20260807/c2pp_diag/PREREG.md, "# PILOT
REGISTRATIONS" (hypotheses H1-H3, functionals P2.1-P2.11, escape test P3,
cells P4, predictions PR1-PR7, scope limits P6). Written and fixed BEFORE
this file was run.

F-a/F-b/F-c (rounds M1 and c2r2, both survived) all score COSET-STRIPPED
objects. F-d scores the clause-(i) reduction itself: the multiplicative
factor that routing removes, and whether the object clause (ii) bounds is
non-vacuous at the rows that actually carry the joint loss.

Kernels are the banked M1 census kernels, loaded READ-ONLY exactly as
c2r2_local.py:18-25 does. Stdlib only. Exact integer censuses.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260807/c2pp_diag/fd_coset_routing_attack.py
"""
import sys, math, json, importlib.util
from fractions import Fraction

sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"
M1PATH = (ROOT + "/critical/nodes/dli_prime_weighted_large_block_support"
                 "/notes/m1_dli_m1_tower_census_modal.py")
M1JSON = (ROOT + "/critical/nodes/dli_prime_weighted_large_block_support"
                 "/notes/m1_dli_m1_results.json")
OUT = ROOT + "/notes/pilots_20260807/c2pp_diag/fd_results.json"

spec = importlib.util.spec_from_file_location("m1", M1PATH)
m1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m1)

# ---- registered constants (PREREG P4) --------------------------------------
CAL_ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801),
            (3, 97), (3, 193), (4, 97), (4, 193)]
POSE_BULK = [0.998, 1.010, 0.0, 0.0, 1.033, 1.066, 0.760, 0.0]
N = 32
RES = 21
JUNC = 33
ALLOW = 2.0 ** (Fraction(21, 33))          # 1.554406...
NEUTRAL_TOL = 1e-3

assert N == 32 and N & (N - 1) == 0, "CATCH-Z6: n must be a 2-power"
assert (N // 2) & (N // 2 - 1) == 0, "CATCH-Z6: h must be a 2-power"


def nn(x):
    """NaN-safe read; returns None for NaN so it is never silently 0."""
    if x is None:
        return None
    if isinstance(x, float) and x != x:
        return None
    return x


rows = []
print("=" * 78)
print("[PC] POSITIVE CONTROL -- 8 banked b2b TEST-1 rows via the M1 kernels")
print("=" * 78)
pc_ok = True
bulks_pos = []
for i, (t, q) in enumerate(CAL_ROWS):
    cs = m1.mitm_joint_census_dict(q, N, t)
    cn = m1.even_null_census(q, N, t)
    asum = m1.signed_all_census(q, N, t)
    d = m1.decompose_row(q, N, t, cn, cs, asum)

    raw = nn(d["ratio"])
    r1 = nn(d["stripped_mean_ratio"])
    bulk = nn(d["bulk_ratio"])
    bulk_z = 0.0 if bulk is None else bulk

    r0b, r1b, r2b = m1.BANKED_F2B_RATIOS[(t, q)]
    ratio_ok = raw is not None and abs(raw - r0b) < 1e-9
    bulk_ok = abs(bulk_z - POSE_BULK[i]) < 5e-4
    pc_ok &= ratio_ok and bulk_ok
    if bulk_z > 0:
        bulks_pos.append(bulk_z)

    # ---- NEW F-d functionals (PREREG P2.5-P2.11) ---------------------------
    cos = d["coset"]
    s_null, n_null = d["s_null"], d["n_null"]
    s_all = sum(asum)
    kappa = (raw / r1) if (raw is not None and r1 not in (None, 0.0)) else None
    sigma = (cos["cs0"] / s_null) if s_null else None
    sigma_u = (cos["asum0"] / s_all) if s_all else None
    b_raw = math.log2(raw) if (raw and raw > 0) else None
    vac = (bulk is None or bulk == 0.0) and (raw is not None and raw > float(ALLOW))

    rows.append(dict(t=t, q=q, raw_ratio=raw, stripped_mean_ratio=r1,
                     bulk_ratio=bulk, coset_leakage=kappa,
                     coset_mass_share=sigma, uncond_coset_share=sigma_u,
                     headline_junction_bits=b_raw, clause_ii_vacuity=vac,
                     cs0=cos["cs0"], s_null=s_null, asum0=cos["asum0"],
                     s_all=s_all,
                     accidents=[{k2: v for k2, v in a.items()}
                                for a in d["accidents"]]))
    print(f"  (t={t},q={q:>5})  raw={0.0 if raw is None else raw:9.4f}"
          f"[bank {r0b:8.4f} {'OK' if ratio_ok else 'X'}]"
          f"  strip={('  NaN' if r1 is None else f'{r1:6.3f}')}"
          f"  bulk={bulk_z:6.3f}[pose {POSE_BULK[i]:5.3f}"
          f" {'OK' if bulk_ok else 'X'}]")

gm = math.exp(sum(math.log(b) for b in bulks_pos) / len(bulks_pos))
gm_ok = round(gm, 3) == 0.967
pc_ok &= gm_ok
assert len(bulks_pos) == 5, "nonemptiness: expected 5 positive bulk rows"
print(f"  BULK GM = {gm:.6f} -> {round(gm,3)} [banked 0.967 "
      f"{'OK' if gm_ok else 'X'}]")
print(f"  POSITIVE CONTROL: {'PASS' if pc_ok else 'FAIL'}")
assert pc_ok, "positive control failed -- no F-d verdict may be issued"

# ---------------------------------------------------------------- F-d table
print("\n" + "=" * 78)
print("[F-d] COSET-ROUTING NEUTRALITY -- the functionals no F-round scored")
print("=" * 78)
print(f"  allowance 2^(21/33) = {float(ALLOW):.6f}")
print(f"  {'row':>13} {'raw':>9} {'kappa':>8} {'sigma':>8} {'sigma_u':>8}"
      f" {'33*b_raw':>9} {'vacuous':>8}")
for r in rows:
    k = r["coset_leakage"]
    print(f"  (t={r['t']},q={r['q']:>5}) "
          f"{0.0 if r['raw_ratio'] is None else r['raw_ratio']:9.4f}"
          f" {('     NaN' if k is None else f'{k:8.4f}')}"
          f" {(0.0 if r['coset_mass_share'] is None else r['coset_mass_share']):8.5f}"
          f" {(0.0 if r['uncond_coset_share'] is None else r['uncond_coset_share']):8.5f}"
          f" {(0.0 if r['headline_junction_bits'] is None else JUNC*r['headline_junction_bits']):9.3f}"
          f" {'YES' if r['clause_ii_vacuity'] else '.':>8}")

# ---- escape test (PREREG P3) ----------------------------------------------
over = [r for r in rows
        if r["raw_ratio"] is not None and r["raw_ratio"] > float(ALLOW)]
fd1 = [r for r in over if r["clause_ii_vacuity"]]
fd2 = []
for r in fd1:
    k = r["coset_leakage"]
    sig, sigu = r["coset_mass_share"], r["uncond_coset_share"]
    if k is None:
        # NaN because stripped conditional mass vanished: F-d-2 holds iff the
        # coset column carries all the conditional mass but not all the
        # unconditional mass.
        if sig is not None and sigu is not None and sig > 1 - NEUTRAL_TOL \
           and sigu < 1 - NEUTRAL_TOL:
            fd2.append(r)
    elif k > 1 + NEUTRAL_TOL:
        fd2.append(r)

esc_a = len(over) == 0
esc_b = all((r["coset_leakage"] is not None
             and abs(r["coset_leakage"] - 1.0) <= NEUTRAL_TOL) for r in over) \
    if over else True
esc_c = all((r["coset_mass_share"] is not None
             and r["uncond_coset_share"] is not None
             and abs(r["coset_mass_share"] - r["uncond_coset_share"])
             <= NEUTRAL_TOL) for r in over) if over else True
fd_fired = bool(fd1) and bool(fd2)

print("\n  ESCAPE TEST (pre-registered P3):")
print(f"    rows with raw_ratio > allowance : {len(over)}"
      f"  -> E-a (no overflow) {'HOLDS' if esc_a else 'FAILS'}")
print(f"    F-d-1 (overflow AND clause-(ii) vacuous) : {len(fd1)} rows"
      f" {[(r['t'], r['q']) for r in fd1]}")
print(f"    F-d-2 (routing not neutral there)        : {len(fd2)} rows"
      f" {[(r['t'], r['q']) for r in fd2]}")
print(f"    E-b (kappa == 1 on overflow rows) {'HOLDS' if esc_b else 'FAILS'}")
print(f"    E-c (sigma == sigma_u there)      {'HOLDS' if esc_c else 'FAILS'}")
print(f"    ==> F-d {'*** FIRED ***' if fd_fired else 'did NOT fire'}")

# ---- H3: coset q-trend at fixed depth t=2 ---------------------------------
print("\n  [H3] coset-column q-trend at fixed depth t=2 (never scored by F-a):")
t2 = sorted([r for r in rows if r["t"] == 2], key=lambda r: r["q"])
for r in t2:
    k = r["coset_leakage"]
    print(f"    q={r['q']:>6}  raw={r['raw_ratio']:9.4f}"
          f"  kappa={('NaN' if k is None else f'{k:.4f}'):>9}"
          f"  sigma={r['coset_mass_share']:.6f}"
          f"  sigma_u={r['uncond_coset_share']:.6f}")
mono_raw = all(t2[i]["raw_ratio"] < t2[i + 1]["raw_ratio"]
               for i in range(len(t2) - 1))
mono_sig = all(t2[i]["coset_mass_share"] <= t2[i + 1]["coset_mass_share"] + 1e-12
               for i in range(len(t2) - 1))
print(f"    raw_ratio strictly increasing in q: {mono_raw}")
print(f"    coset_mass_share non-decreasing in q: {mono_sig}")

# ---- mutation control (PREREG P4) -----------------------------------------
print("\n" + "=" * 78)
print("[MUT] MUTATION CONTROL -- does the F-b `if b > 0` filter matter?")
print("=" * 78)
m1res = json.load(open(M1JSON))
search = []
for i, (t, q) in enumerate(CAL_ROWS):
    r = rows[i]
    search.append(("n32", t, q, 0.0 if r["bulk_ratio"] is None
                   else r["bulk_ratio"], r["raw_ratio"]))
for r in m1res["rows"]:
    b = r["bulk_ratio"]
    b = b if isinstance(b, (int, float)) and b == b else 0.0
    ra = r.get("ratio")
    ra = ra if isinstance(ra, (int, float)) and ra == ra else 0.0
    search.append(("n64", r["t"], r["q"], b, ra))

bulk_pos = [(b, lab, t, q) for (lab, t, q, b, ra) in search if b > 0]
bmax, blab, bt, bq = max(bulk_pos)
usage_bulk = JUNC * math.log2(bmax) / RES
print(f"  F-b path (filter `if b > 0`): x_max = {bmax:.6f} at {blab}"
      f" (t={bt},q={bq})")
print(f"    33*log2(x_max)/21 = {usage_bulk*100:.3f}% of the 21-bit reserve"
      f"   [banked bulk part 2^3.05 -> {3.05/21*100:.2f}%]")

raw_all = [(ra, lab, t, q) for (lab, t, q, b, ra) in search if ra and ra > 0]
rmax, rlab, rt, rq = max(raw_all)
usage_raw = JUNC * math.log2(rmax) / RES
print(f"  F-d path (NO filter, vacuous-bulk rows scored at raw_ratio):"
      f" x_max = {rmax:.6f} at {rlab} (t={rt},q={rq})")
print(f"    33*log2(x_max)/21 = {usage_raw*100:.3f}% of the 21-bit reserve")
exact_over = Fraction(rmax).limit_denominator(10**12) ** JUNC > Fraction(2) ** RES
print(f"    exact Fraction check: raw_max^33 {'>' if exact_over else '<='} 2^21")
mut_ok = abs(usage_bulk - usage_raw) > 1e-6
print(f"  MUT (filter is load-bearing): "
      f"{'TRIPS as required' if mut_ok else 'DID NOT TRIP -> H2 is WRONG'}")

# ---- theta insensitivity spot-check ---------------------------------------
print("\n  [theta] spot-check theta in {2,3,4} on the two high-loss rows:")
for (t, q) in [(2, 8353), (2, 32801)]:
    cs = m1.mitm_joint_census_dict(q, N, t)
    cn = m1.even_null_census(q, N, t)
    asum = m1.signed_all_census(q, N, t)
    line = []
    for th in (2.0, 3.0, 4.0):
        d = m1.decompose_row(q, N, t, cn, cs, asum, theta=th)
        b = nn(d["bulk_ratio"])
        line.append(f"theta={th:.0f}: bulk={'NaN' if b is None else f'{b:.4f}'}"
                    f" nacc={len(d['accidents'])}")
    print(f"    (t={t},q={q}) " + " | ".join(line))

verdict = dict(
    pilot="c2pp_diag", round="C2'' F-round 3", family="F-d coset-routing "
    "neutrality", prereg="notes/pilots_20260807/c2pp_diag/PREREG.md",
    positive_control="PASS", allowance=float(ALLOW),
    fd_fired=fd_fired,
    fd1_rows=[(r["t"], r["q"]) for r in fd1],
    fd2_rows=[(r["t"], r["q"]) for r in fd2],
    escape_a=esc_a, escape_b=esc_b, escape_c=esc_c,
    raw_monotone_in_q_at_t2=mono_raw,
    coset_share_monotone_in_q_at_t2=mono_sig,
    fb_filter_xmax=bmax, fb_filter_usage_pct=usage_bulk * 100,
    fd_nofilter_xmax=rmax, fd_nofilter_usage_pct=usage_raw * 100,
    mutation_trips=mut_ok, rows=rows)
with open(OUT, "w") as fh:
    json.dump(verdict, fh, indent=1, default=str)
print(f"\n  artifact -> {OUT}")
print(f"\nVERDICT: F-d {'FIRED' if fd_fired else 'did not fire'}"
      f"  (scope limits: PREREG P6 -- no official-row inference)")
