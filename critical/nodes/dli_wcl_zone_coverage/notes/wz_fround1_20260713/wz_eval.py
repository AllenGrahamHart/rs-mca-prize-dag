"""wz F-round 1: aggregate shard JSONs, evaluate pre-registered kill lines
(wz_falsifiers.md section 4). Local, tiny footprint (json + math only)."""
import json
import math
import os
from fractions import Fraction

BASE = ("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
        "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/")
THRESH = Fraction(1, 32)


def comb(n, k):
    return math.comb(n, k)


def lam_orb(q, N, L):
    return sum(comb(N, w) * 2 ** (w - 1)
               for w in range(L + 1, L + 6)) / (2 * N * q ** L)


def e_pred(q, N, L):
    return sum(comb(N, w) for w in range(L + 1, L + 6)) / (2 * q ** L)


def load(name):
    p = BASE + "wz_shard_%s.json" % name
    return json.load(open(p)) if os.path.exists(p) else None


def band_stats(cells, N, L, dedup_key=None):
    n = len(cells)
    nonempty = 0
    wsum = Fraction(0)
    exceed = 0
    for c in cells:
        wcl = Fraction(*c[dedup_key]) if dedup_key and dedup_key in c \
            else Fraction(*c["Wcl"])
        tot = sum(c["prim"].values())
        if dedup_key and dedup_key in c:
            tot = 1 if wcl > 0 else 0
        if tot > 0:
            nonempty += 1
        if wcl > THRESH:
            exceed += 1
        wsum += wcl
    phat = nonempty / n
    ppred = sum(1 - math.exp(-lam_orb(c["q"], N, L)) for c in cells) / n
    wbar = wsum / n
    epred = sum(e_pred(c["q"], N, L) for c in cells) / n
    return {"n": n, "nonempty": nonempty, "exceed_1_32": exceed,
            "Phat": phat, "Ppred": ppred,
            "rho": phat / ppred if ppred else float("inf"),
            "Wbar": [wbar.numerator, wbar.denominator],
            "Wbar_f": float(wbar), "Epred": epred,
            "rho_W": float(wbar) / epred if epred else float("inf"),
            "q_range": [min(c["q"] for c in cells),
                        max(c["q"] for c in cells)]}


def main():
    report = {"families": {}, "kills": {}, "integrity": {}, "recurrence": {}}

    # ---------- integrity (KILL-3 gates) ----------
    pc1, pc2 = load("pc_l1"), load("pc_l2")
    integ = {"pc_l1_ok": bool(pc1 and pc1["ok"]),
             "pc_l2_ok": bool(pc2 and pc2["ok"]),
             "M2_shadow_trip": pc1["controls"].get("M2_shadow_trip")
             if pc1 else None}
    xc = load("xcheck64")
    integ["xcheck64_equal_b25_vacuous"] = xc["equal"] if xc else "DEFERRED"
    xcb = load("xcheck64b")
    integ["xcheck64b_equal_nonempty"] = (
        xcb["equal"] and sum(xcb["prim"].values()) > 0) if xcb \
        else "DEFERRED"
    flags = []
    fam_defs = {
        "A": (32, 1, [("band_a17", "b17"), ("band_a19", "b19"),
                      ("band_a21", "b21"), ("band_a23", "b23")], None),
        "B": (32, 2, [("band_b10", "b10"), ("band_b1214", "b12"),
                      ("band_b1214", "b14")], None),
        "C": (64, 1, [("band_c", "b21"), ("band_c", "b23"),
                      ("band_c", "b25"), ("band_c", "b27")],
              "Wcl_liftdedup"),
    }
    all_cells = []
    for fam, (N, L, bands, dk) in fam_defs.items():
        rows = []
        for shard, band in bands:
            d = load(shard)
            if d is None:
                rows.append({"band": band, "status": "DEFERRED"})
                continue
            cells = [c for c in d["cells"] if c["band"] == band]
            for c in cells:
                flags += [(fam, band, c["q"], f) for f in c["flags"]]
                all_cells.append((fam, band, c))
            st = band_stats(cells, N, L, dk)
            st["band"] = band
            rows.append(st)
        report["families"][fam] = {"N": N, "L": L, "bands": rows}
    integ["orbit_closure_flags"] = flags
    # lift trip control (band_c): companions nonempty must have miss==0
    bc = load("band_c")
    if bc:
        miss = sum(c["lift"]["miss"] for c in bc["cells"])
        comp = sum(c["lift"]["companion_orbits"] for c in bc["cells"])
        owned = sum(c["lift"]["owned64"] for c in bc["cells"])
        integ["lift_control"] = {"companion_orbits": comp,
                                 "owned64": owned, "miss": miss,
                                 "trips": comp > 0, "ok": miss == 0}
    # nonemptiness guards on saturated bands
    for fam, band in (("A", "b17"), ("B", "b10"), ("C", "b21")):
        rows = report["families"][fam]["bands"]
        r = next((x for x in rows if x.get("band") == band), None)
        integ["guard_%s_%s" % (fam, band)] = \
            bool(r and r.get("nonempty", 0) > 0)
    report["integrity"] = integ

    # ---------- KILL-1 ----------
    k1a = []
    for fam, f in report["families"].items():
        for r in f["bands"]:
            if r.get("status") == "DEFERRED":
                continue
            if r["Ppred"] <= 0.25 and r["n"] >= 10 and r["Phat"] >= 0.75:
                k1a.append((fam, r["band"], r["Phat"], r["Ppred"]))
    # recurrence: identical orbit rep at >=3 distinct primes within a family
    seen = {}
    for fam, band, c in all_cells:
        for rep in c.get("orbit_reps", []):
            seen.setdefault((fam, rep), set()).add(c["q"])
    recur = {("%s|%s" % k): sorted(v) for k, v in seen.items()
             if len(v) >= 3}
    report["recurrence"] = {"n_keys": len(seen), "recurring": recur}
    report["kills"]["KILL_1a"] = k1a
    report["kills"]["KILL_1b"] = sorted(recur)

    # ---------- KILL-2 ----------
    k2 = {}
    for fam, f in report["families"].items():
        rows = [r for r in f["bands"] if r.get("status") != "DEFERRED"]
        if len(rows) < 3:
            k2[fam] = "INSUFFICIENT_BANDS"
            continue
        for key, topcount in (("rho", "nonempty"), ("rho_W", "nonempty")):
            vals = [r[key] for r in rows]
            inc = all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
            ratio = vals[-1] / vals[0] if vals[0] > 0 else float("inf")
            trip = inc and ratio >= 4 and rows[-1][topcount] >= 3
            k2.setdefault(fam, {})[key] = {
                "values": [round(v, 4) for v in vals],
                "monotone_up": inc, "top_over_bottom": round(ratio, 4)
                if vals[0] > 0 else None, "top_nonempty":
                rows[-1][topcount], "trip": trip}
    report["kills"]["KILL_2"] = k2

    # ---------- verdict ----------
    controls_ok = (integ["pc_l1_ok"] and integ["pc_l2_ok"]
                   and integ["M2_shadow_trip"] == "True"
                   and integ.get("lift_control", {}).get("ok", False)
                   and integ.get("lift_control", {}).get("trips", False)
                   and not flags
                   and all(integ["guard_%s_%s" % (f, b)]
                           for f, b in (("A", "b17"), ("B", "b10"),
                                        ("C", "b21"))))
    killed = bool(k1a) or bool(recur) or any(
        isinstance(v, dict) and any(x["trip"] for x in v.values())
        for v in k2.values())
    if not controls_ok:
        verdict = "INVALID_OR_MIXED"
    elif killed:
        verdict = "KILLED"
    else:
        verdict = "SURVIVED"
    report["controls_ok"] = controls_ok
    report["verdict"] = verdict
    out = BASE + "wz_eval_report.json"
    json.dump(report, open(out, "w"), indent=1, default=str)
    print(json.dumps({"verdict": verdict, "controls_ok": controls_ok,
                      "KILL_1a": k1a, "KILL_1b": sorted(recur),
                      "KILL_2": k2}, indent=1, default=str))
    for fam, f in report["families"].items():
        print("family", fam, "N=%d L=%d" % (f["N"], f["L"]))
        for r in f["bands"]:
            if r.get("status") == "DEFERRED":
                print("  ", r["band"], "DEFERRED")
            else:
                print("   %s n=%d nonempty=%d Phat=%.3f Ppred=%.3f "
                      "rho=%.3f Wbar=%.4f Epred=%.4f rho_W=%.3f "
                      "exceed=%d" %
                      (r["band"], r["n"], r["nonempty"], r["Phat"],
                       r["Ppred"], r["rho"], r["Wbar_f"], r["Epred"],
                       r["rho_W"], r["exceed_1_32"]))


if __name__ == "__main__":
    main()
