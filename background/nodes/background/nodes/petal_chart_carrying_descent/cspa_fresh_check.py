#!/usr/bin/env python3
"""cspa_fresh_check: independent auditor checks for the csp proof packet.

Runs (pre-registered in cspa_findings.md):
  R1  fresh cells never touched by packet or search:
      (16,12,241,consec), (16,4,113,geom3), (32,24,641,geom5), (32,16,577,rand2)
      -> struct + dual census + full battery + parity/band tabulation.
  R2  mutation MA (normalization drift, #133): u1 built with auxiliary labels
      c_i/(y_i - y_nf) must break S2 factorization AND the census bijection.
  R3  mutation MB (aperiodic complement): quotient contributors with
      y_nf NOT in agr lift to ODD |S| = 2|agr|+1, c(S) = 1 officials.
  R4  mutation MC (bijection liveness): drop one official member -> BIJECTION.
Exit 0 = all expectations met.
"""
import itertools, sys

sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/background/nodes/petal_chart_carrying_descent")
import csp_verify as V

nfail = 0

def report(tag, ok, detail=""):
    global nfail
    print(("PASS" if ok else "FAIL"), tag, detail)
    if not ok:
        nfail += 1

# ---------------- R1: fresh cells ----------------
FRESH = [(16, 12, 241, "consec"), (16, 4, 113, "geom3"),
         (32, 24, 641, "geom5"), (32, 16, 577, "rand2")]

for cell in FRESH:
    C = V.build_cell(*cell)
    sf = V.check_struct(C)
    report(f"R1-struct {cell}", not sf, str(sf))
    off = V.official_census(C)
    quo = V.quotient_census(C)
    fails, byW = V.battery(C, off, quo)
    # parity + band tabulation (auditor's own #135 check)
    sizes = sorted(len(S) for S in off.values())
    n, k = C["n"], C["k"]
    parity_ok = all(s % 2 == 0 for s in sizes)
    band_ok = True
    for g, Sq in quo.items():
        S = 2 * len(Sq)
        z = len([i for i in Sq if i <= C["nf"]])
        dq = C["kp"] - z
        m_mem = len(Sq) - z
        if (dq >= m_mem - 2) != (S <= k + 4):
            band_ok = False
    maxper = 0
    for W, recs in byW.items():
        for (g1, I1, dq), (g2, I2, _) in itertools.combinations(recs, 2):
            if len(I1 | I2) <= dq + 2:
                maxper = 2
    report(f"R1-battery {cell}", not fails, str(sorted(set(fails))))
    report(f"R1-parity/band {cell}", parity_ok and band_ok and maxper < 2,
           f"members={len(off)} charts={len(byW)} sizes={sizes} "
           f"band(k+2..k+4)={[s for s in sizes if s <= k+4]}")

# ---------------- R2: mutation MA (normalization drift #133) ----------------
def mutate_aux_labels(C):
    """u1 with auxiliary-normalized labels c_i/(y_i - y_nf) (WRONG per #133)."""
    p = C["p"]
    u1x = list(C["u1"])
    for i in C["petal_fibers"]:
        u1x[i] = u1x[i] * pow((C["dom2"][i] - C["y_nf"]) % p, -1, p) % p
    return u1x

for cell in [(16, 12, 241, "consec"), (16, 8, 97, "consec")]:
    C = V.build_cell(*cell)
    u1x = mutate_aux_labels(C)
    p, n, half = C["p"], C["n"], C["half"]
    # (i) S2 pointwise factorization must FAIL somewhere
    fact_broken = any(
        C["values"][j] != (C["dom"][j] - C["x_nf"]) * u1x[j % half] % p
        for j in range(n))
    # (ii) census bijection must FAIL: quotient census vs u1x, lifted, != official
    off = V.official_census(C)
    Cx = dict(C); Cx["u1"] = u1x
    quox = V.quotient_census(Cx)
    lifted = {}
    for g, Sq in quox.items():
        f = V.lift(g, C["x_nf"], C["k"], p)
        lifted[f] = frozenset(j for j in range(n) if (j % half) in Sq)
    bij_broken = (lifted != off)
    report(f"R2-MA {cell}", fact_broken and bij_broken,
           f"fact_broken={fact_broken} bij_broken={bij_broken} "
           f"|off|={len(off)} |quo_aux|={len(quox)}")

# ---------------- R3: mutation MB (aperiodic complement) ----------------
def quotient_census_all(C):
    """quotient contributors WITHOUT the y_nf-membership filter."""
    half, kp, p = C["half"], C["kp"], C["p"]
    dom2, u1 = C["dom2"], C["u1"]
    found = {}
    for sub in itertools.combinations(range(half), kp + 1):
        xs = [dom2[i] for i in sub]
        ys = [u1[i] for i in sub]
        g = V.newton_interp(xs[:kp], ys[:kp], p)
        if g in found:
            continue
        if V.ev(g, xs[kp], p) != ys[kp]:
            continue
        Sq = frozenset(i for i in range(half) if V.ev(g, dom2[i], p) == u1[i])
        if len(Sq) >= kp + 1:
            found[g] = Sq
    return found

for cell in [(16, 12, 241, "consec"), (16, 8, 97, "consec"), (16, 4, 113, "geom3")]:
    C = V.build_cell(*cell)
    n, half, p, nf = C["n"], C["half"], C["p"], C["nf"]
    allq = quotient_census_all(C)
    comp = {g: Sq for g, Sq in allq.items() if nf not in Sq}
    ok, checked = True, 0
    for g, Sq in comp.items():
        f = V.lift(g, C["x_nf"], C["k"], p)
        S = frozenset(j for j in range(n)
                      if V.ev(f, C["dom"][j], p) == C["values"][j])
        checked += 1
        if not (len(S) == 2 * len(Sq) + 1 and len(S) % 2 == 1
                and V.stab_order(S, n) == 1
                and nf in S and (nf + half) not in S):
            ok = False
    report(f"R3-MB {cell}", ok,
           f"complement_members={checked} (all odd-|S| aperiodic)" if ok
           else f"VIOLATION among {checked}")

# ---------------- R4: mutation MC (bijection liveness) ----------------
C = V.build_cell(16, 8, 97, "consec")
off = V.official_census(C)
quo = V.quotient_census(C)
off_bad = dict(off)
del off_bad[next(iter(sorted(off_bad)))]
fails_bad, _ = V.battery(C, off_bad, quo)
report("R4-MC drop-one-member", "BIJECTION" in fails_bad,
       f"fails={sorted(set(fails_bad))}")

print("AUDITOR VERDICT:", "ALL EXPECTATIONS MET" if nfail == 0
      else f"{nfail} DEVIATIONS")
sys.exit(0 if nfail == 0 else 1)
