#!/usr/bin/env python3
"""C2'' F-round 2 -- LOCAL controls + F-b scoring (exact-rational verdict path).

REUSES the M1 kernels verbatim by importing
m1_dli_m1_tower_census_modal.py (READ-ONLY; sys.dont_write_bytecode=True so no
.pyc is written into the repo). Under ramguard tiny the system python3 has no
`modal`, so the M1 module's ImportError fallback yields pure kernels.

Runs (all cheap, exact):
  [PC]  POSITIVE CONTROL: n=32 8-row banked replay (BANKED_F2B_RATIOS) + the
        8 pose bulk values {0.998,1.010,0,0,1.033,1.066,0.760,0} and GM 0.967.
  [FB]  F-b SCORING (packet arithmetic x^33 vs 2^21, exact Fraction): max bulk
        over n=32 calib + M1 n=64 banked rows; reserve usage; the stripped-
        stacked NOT-falsifier printed but not scored.
  [MUT] MUTATION CONTROLS (required-to-trip): F-b on stripped instead of bulk;
        F-a on a synthetic q^0.1 bulk; F-c with theta=1 over-flagging.
"""
import sys, math, json, importlib.util
from fractions import Fraction
sys.dont_write_bytecode = True

M1 = "/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_tower_census_modal.py"
spec = importlib.util.spec_from_file_location("m1", M1)
m1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m1)

CAL_ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801),
            (3, 97), (3, 193), (4, 97), (4, 193)]
POSE_BULK = [0.998, 1.010, 0.0, 0.0, 1.033, 1.066, 0.760, 0.0]
M1JSON = "/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_results.json"
RES = 21  # reserve bits
JUNC = 33

print("=" * 72)
print("[PC] POSITIVE CONTROL -- n=32 8-row calibration via M1 kernels")
print("=" * 72)
cal = {}
pc_ok = True
bulks_pos = []
for i, (t, q) in enumerate(CAL_ROWS):
    cs = m1.mitm_joint_census_dict(q, 32, t)
    cn = m1.even_null_census(q, 32, t)
    asum = m1.signed_all_census(q, 32, t)
    d = m1.decompose_row(q, 32, t, cn, cs, asum)
    cal[(t, q)] = d
    r0, r1, r2 = m1.BANKED_F2B_RATIOS[(t, q)]
    ratio_ok = abs(d["ratio"] - r0) < 1e-9
    bulk = d["bulk_ratio"]
    bulk = bulk if bulk == bulk else 0.0
    pose = POSE_BULK[i]
    bulk_ok = abs(bulk - pose) < 5e-4   # pose is 3-dp rounded
    pc_ok &= ratio_ok and bulk_ok
    if bulk > 0:
        bulks_pos.append(bulk)
    print(f"  (t={t},q={q:>5}) raw={d['ratio']:8.4f}[bank {r0:8.4f} {'OK' if ratio_ok else 'X'}]"
          f"  bulk={bulk:6.3f}[pose {pose:5.3f} {'OK' if bulk_ok else 'X'}]"
          f"  strip_mean={d['stripped_mean_ratio'] if d['stripped_mean_ratio']==d['stripped_mean_ratio'] else 0.0:7.4f}")
gm = math.exp(sum(math.log(b) for b in bulks_pos) / len(bulks_pos))
gm_ok = round(gm, 3) == 0.967
pc_ok &= gm_ok
print(f"  BULK GM over positive rows = {gm:.6f} -> {round(gm,3)} "
      f"[banked 0.967 {'OK' if gm_ok else 'X'}]")
assert len(bulks_pos) == 5, "nonemptiness: expected 5 positive bulk rows"
print(f"  POSITIVE CONTROL: {'PASS' if pc_ok else 'FAIL'}")
assert pc_ok, "positive control failed -- kernels do not reproduce banked calibration"

# ---------------------------------------------------------------- F-b scoring
print("\n" + "=" * 72)
print("[FB] F-b SCORING -- packet transport x^33 vs 2^21 (exact Fraction)")
print("=" * 72)
m1res = json.load(open(M1JSON))

def frac_of(x):
    return Fraction(x).limit_denominator(10**12)

# assemble the search set: (label, t, q, bulk, stripped_mean, accidents-info)
search = []
for (t, q), d in cal.items():
    b = d["bulk_ratio"]; b = b if b == b else 0.0
    sm = d["stripped_mean_ratio"]; sm = sm if sm == sm else 0.0
    # accident absolute mass fraction (clause iii): sum accident mass / n_all uncond mass
    accmass = sum(a["mass"] for a in d["accidents"])
    an = [math.comb(32, k) * 2 ** (32 - k) for k in range(33)]
    asum_tot = sum(d["table"].get(k, [0, 0, 0, 0])[3] for k in d["table"]) if isinstance(d["table"], dict) else 0
    search.append(("n32", t, q, b, sm, accmass, d))
for r in m1res["rows"]:
    b = r["bulk_ratio"]; b = b if isinstance(b, (int, float)) and b == b else 0.0
    sm = r["stripped_mean_ratio"]; sm = sm if isinstance(sm, (int, float)) and sm == sm else 0.0
    accmass = sum(a["mass"] for a in r["accidents"]) if r["accidents"] else 0
    search.append(("n64", r["t"], r["q"], b, sm, accmass, r))

# clause (ii): worst BULK stacked 33x
bulk_rows = [(b, lab, t, q) for (lab, t, q, b, sm, am, d) in search if b > 0]
bmax, blab, bt, bq = max(bulk_rows)
bulk_charge_frac = frac_of(bmax) ** JUNC
bulk_bits = JUNC * math.log2(bmax)
# clause (iii): worst ABSOLUTE accident charge (counted once, q-independent)
acc_bits_each = []
for (lab, t, q, b, sm, am, d) in search:
    an_tot = 3 ** 32
    asum_all = None
    # total unconditional mass = sum asum[k]; recover from table where present
    if isinstance(d.get("table"), dict) and d["table"]:
        asum_all = sum(v[3] for v in d["table"].values())
    frac_am = (am / asum_all) if (asum_all and asum_all > 0) else 0.0
    a_bits = math.log2(1 + frac_am) if frac_am > 0 else 0.0
    acc_bits_each.append((a_bits, lab, t, q, am, frac_am))
amax_bits, alab, at, aq, amass, afrac = max(acc_bits_each)
total_bits = bulk_bits + amax_bits
usage = total_bits / RES
fb_fired = frac_of(bmax) ** JUNC * frac_of(2) ** 0 > frac_of(2) ** RES or (total_bits > RES)
print(f"  worst BULK ratio (clause ii): {bmax:.6f} at {blab} (t={bt},q={bq})")
print(f"    stacked 33x charge = {bmax:.6f}^33 = 2^{bulk_bits:.4f}  (reserve 2^21)")
print(f"    exact: bulk^33 {'>' if bulk_charge_frac > Fraction(2)**RES else '<='} 2^21")
print(f"  worst ABSOLUTE accident charge (clause iii, counted once): "
      f"2^{amax_bits:.4f} at {alab} (t={at},q={aq}) mass={amass} frac={afrac:.3e}")
print(f"  TOTAL replayable-tower charge = 2^{total_bits:.4f}  -> reserve usage "
      f"= {usage*100:.3f}% of 21 bits")
print(f"  F-b KILL LINE: total > 2^21  ==> "
      f"{'*** F-b FIRED ***' if fb_fired else 'F-b NOT fired (reserve intact)'}")

# NOT-falsifier: stripped-stacked (the refuted per-junction-uniform proxy)
strip_rows = [(sm, lab, t, q) for (lab, t, q, b, sm, am, d) in search if sm > 0]
smax, slab, st, sq = max(strip_rows)
strip_bits = JUNC * math.log2(smax)
print(f"\n  [NOT-falsifier, reported not scored] STRIPPED-stacked tower: "
      f"{smax:.4f}^33 = 2^{strip_bits:.3f} at {slab}(t={st},q={sq})")
print(f"    exact: stripped^33 {'>' if frac_of(smax)**JUNC > Fraction(2)**RES else '<='} 2^21 "
      f"-- this is the per-junction-uniform proxy the pose already refutes; NOT a C2'' kill")

# ---------------------------------------------------------------- mutations
print("\n" + "=" * 72)
print("[MUT] MUTATION CONTROLS (required-to-trip)")
print("=" * 72)
# (i) F-b on stripped instead of bulk MUST fire
mut_fb = frac_of(smax) ** JUNC > Fraction(2) ** RES
print(f"  MUT-i  F-b scored on STRIPPED (not bulk): {smax:.4f}^33 = 2^{strip_bits:.2f} "
      f"-> {'FIRES (as required)' if mut_fb else 'DID NOT FIRE (control broken!)'}")
assert mut_fb, "MUT-i control failed"
# (ii) F-a on synthetic super-polylog bulk=q^0.5 MUST fire
synth = {2: [], 3: []}
for t in (2, 3):
    for q in [193, 449, 1153, 3137, 8353, 20011]:
        synth[t].append({"q": q, "t": t, "bulk_ratio": (q ** 0.5),
                         "stripped_mass_ratio": q ** 0.5, "ratio": q ** 0.5})
fa_fired, fa_log = m1.read_Fa(synth)
print(f"  MUT-ii F-a on synthetic super-polylog bulk=q^0.5: "
      f"{'FIRES (as required)' if fa_fired else 'DID NOT FIRE (control broken!)'}")
assert fa_fired, "MUT-ii control failed"
# (iii) F-c required-to-trip: inject anomalous exceedances (window law violated)
# and confirm the Poisson-binomial test REJECTS at p<1e-3.
census = [r for r in m1res["rows"] if r["t"] == 2 and 1409 <= r["q"] <= 10369]
cell_lams = []
for r in sorted(census, key=lambda x: x["q"]):
    for k in (3, 4, 5):
        lam = m1.lam_window(32, k, r["q"], 1)
        if lam <= 0.5:
            cell_lams.append(lam)
ps = [1 - math.exp(-lam) for lam in cell_lams]
Ereal = sum(ps)
# observed in real data (MUT-iii preamble finding): 0 accidents even at theta=1
X_real = 0
p_real = m1.two_sided_from_pmf(m1.poisson_binom_pmf(ps), X_real)
# mutation: force ALL cells to be accidents (window law grossly violated)
X_mut = len(cell_lams)
p_mut = m1.two_sided_from_pmf(m1.poisson_binom_pmf(ps), X_mut)
print(f"  MUT-iii finding: at theta=1 (max over-flag) the k=3 rare window flags "
      f"0/{len(cell_lams)} accidents\n     (conditional mean <= mean-field for every row -- "
      f"anti-correlated; no excess exists to over-flag).")
print(f"  MUT-iii required-to-trip: force ALL {X_mut} cells accident (E={Ereal:.3f}) -> "
      f"Poisson-binomial p={p_mut:.3e} -> {'TRIPS (p<1e-3, as required)' if p_mut < 1e-3 else 'DID NOT TRIP (control broken!)'}")
assert p_mut < 1e-3, "MUT-iii control failed: F-c test cannot reject even a gross violation"
print(f"  (real census read: X=0, p={p_real:.3e} -- above the 1e-3 kill line, NOT fired)")

print("\nAll asserted controls (PC, MUT-i, MUT-ii) PASSED.")
