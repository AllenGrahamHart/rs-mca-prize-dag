"""wz2 F-round 2: aggregate shard JSONs, evaluate the pre-registered kill
lines (wz2_falsifiers.md section 4). Local, tiny footprint (json + math)."""
import json
import math
import os
from fractions import Fraction

BASE = ("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
        "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/")

# frozen round-1 family-B band values (wz_results.md)
R1_B = [("b10", 1.615), ("b12", 2.395), ("b14", 4.648)]


def load(name):
    p = BASE + "wz2_shard_%s.json" % name
    return json.load(open(p)) if os.path.exists(p) else None


def main():
    rep = {"integrity": {}, "kills": {}, "diagnostics": {}}
    integ = rep["integrity"]

    # ---------------- integrity / conformance ----------------
    replay = load("replay")
    integ["replay_ok"] = bool(replay and replay["ok"])
    integ["replay_checks"] = replay["checks"] if replay else None
    aud = load("c1audit")
    integ["c1audit_banked_ok"] = bool(aud and aud["ok"])
    xl3 = load("xcheckl3")
    integ["xcheckl3"] = bool(xl3 and xl3["ok"]) if xl3 else "DEFERRED"
    x96 = load("xcheck96")
    integ["xcheck96"] = bool(x96 and x96["ok"]) if x96 else "DEFERRED"
    o1a = load("o96_l1")
    o1b = load("o192_l1")
    integ["o96_l1_controls"] = o1a["checks"] if o1a else "DEFERRED"
    integ["o192_l1_controls"] = o1b["checks"] if o1b else "DEFERRED"
    integ["o96_l1_ok"] = bool(o1a and o1a["ok"])
    integ["o192_l1_ok"] = bool(o1b and o1b["ok"])
    l2names = ["o96_l2a", "o96_l2b", "o96_l2c", "o192_l2a", "o192_l2b",
               "o96_l3"]
    l2ok = True
    for n in l2names:
        d = load(n)
        integ[n + "_ok"] = bool(d and d["ok"]) if d else "DEFERRED"
        l2ok &= bool(d and d["ok"])
    # anomalous flags (closure misses / untagged degenerate) anywhere
    bad_flags = []
    for n in ["o96_l1", "o192_l1"] + l2names + ["band_b15", "band_b16"]:
        d = load(n)
        if not d:
            continue
        for c in d.get("cells", []) + d.get("cells_nonempty", []):
            for f in c.get("flags", []):
                bad_flags.append((n, c["q"], f))
    integ["anomalous_flags"] = bad_flags
    controls_ok = (integ["replay_ok"] and integ["c1audit_banked_ok"]
                   and integ["xcheckl3"] is True
                   and integ["xcheck96"] is True and integ["o96_l1_ok"]
                   and integ["o192_l1_ok"] and l2ok and not bad_flags)
    rep["controls_ok"] = controls_ok

    # ---------------- PART 1: KILL-B ----------------
    b15 = load("band_b15")
    b16 = load("band_b16")
    seq = list(R1_B)
    newbands = {}
    for d, band in ((b15, "b15"), (b16, "b16")):
        if d:
            a = d["bands"][band]
            rho = (a["Phat"] / a["Ppred"]) if a["Ppred"] else float("inf")
            seq.append((band, round(rho, 4)))
            newbands[band] = {"n": a["n"], "nonempty": a["nonempty"],
                              "Phat": a["Phat"], "Ppred": a["Ppred"],
                              "rho": round(rho, 4),
                              "null_expected": round(a["n"] * a["Ppred"],
                                                     3)}
    rhos = [r for _, r in seq]
    monotone = all(rhos[i] < rhos[i + 1] for i in range(len(rhos) - 1))
    ratio = rhos[-1] / rhos[0] if rhos[0] else None
    wit_new = sum(newbands[b]["nonempty"] for b in newbands)
    wit_b16 = newbands.get("b16", {}).get("nonempty", 0)
    trip = (monotone and ratio is not None and ratio >= 4
            and wit_new >= 4 and wit_b16 >= 2)
    turnover = (len(rhos) == 5 and (rhos[3] <= rhos[2]
                                    or rhos[4] <= rhos[3]))
    # Poisson consistency of the new bands (2-sigma)
    pois_ok = all(
        v["nonempty"] <= v["null_expected"]
        + 2 * math.sqrt(max(v["null_expected"], 1e-9)) + 1
        for v in newbands.values())
    if trip:
        verdict1 = "KILLED"
    elif turnover or pois_ok:
        verdict1 = "SURVIVED_WITH_EXPLANATION"
    elif monotone:
        verdict1 = "UNRESOLVED_ESCALATE"
    else:
        verdict1 = "SURVIVED"
    rep["kills"]["KILL_B"] = {"sequence": seq, "monotone": monotone,
                              "top_over_bottom": round(ratio, 3)
                              if ratio else None,
                              "witnesses_new_bands": wit_new,
                              "witnesses_b16": wit_b16, "trip": trip,
                              "turnover": turnover,
                              "new_bands": newbands,
                              "verdict_part1": verdict1}
    # b14-deep diagnostic
    if b15:
        a = b15["bands"]["b14"]
        rep["diagnostics"]["b14_deep"] = {
            "n": a["n"], "nonempty": a["nonempty"],
            "rho": round(a["Phat"] / a["Ppred"], 3),
            "note": "outside the kill sequence (pre-registered)"}

    # ---------------- PART 2: KILL-O1 / KILL-O2 ----------------
    sat = []
    fams = {"o96_l1": ("b21", "b23", "b25"),
            "o192_l1": ("b25", "b27", "b29"),
            "o96_l2": ("b13", "b14", "b15"),
            "o192_l2": ("b16", "b17")}
    banddata = {}
    for fam, bands in fams.items():
        for band in bands:
            if fam == "o96_l2":
                d = load({"b13": "o96_l2a", "b14": "o96_l2b",
                          "b15": "o96_l2c"}[band])
            elif fam == "o192_l2":
                d = load({"b16": "o192_l2a", "b17": "o192_l2b"}[band])
            else:
                d = load(fam)
            if not d or band not in d.get("bands", {}):
                continue
            a = d["bands"][band]
            banddata[(fam, band)] = a
            if a["Ppred"] <= 0.25 and a["n"] >= 10 \
                    and a["Phat_gen"] >= 0.75:
                sat.append((fam, band, a["Phat_gen"], a["Ppred"]))
    # generic-key recurrence across primes within each cell family
    seen = {}
    fam_of = {"o96_l1": "o96_l1", "o192_l1": "o192_l1",
              "o96_l2a": "o96_l2", "o96_l2b": "o96_l2",
              "o96_l2c": "o96_l2", "o192_l2a": "o192_l2",
              "o192_l2b": "o192_l2", "o96_l3": "o96_l3"}
    for n, fam in fam_of.items():
        d = load(n)
        if not d:
            continue
        for c in d.get("cells", []) + d.get("cells_nonempty", []):
            for o in c.get("orbs", []):
                L = 2 if "l2" in fam else (3 if "l3" in fam else 1)
                key = (fam, o["rep"])
                if o["u"] == L:  # generic
                    seen.setdefault(key, set()).add(c["q"])
    recur3 = {k: sorted(v) for k, v in seen.items() if len(v) >= 3}
    recur5 = {k: sorted(v) for k, v in seen.items() if len(v) >= 5}
    fam_recur3 = {}
    for (fam, repk), qs in recur3.items():
        fam_recur3.setdefault(fam, []).append((repk, qs))
    o1_trip = bool(sat) or any(len(v) >= 3 for v in fam_recur3.values()) \
        or bool(recur5)
    rep["kills"]["KILL_O1"] = {
        "saturation": sat, "n_generic_keys": len(seen),
        "recurring_3": {"%s|%s" % k: v for k, v in recur3.items()},
        "recurring_5": {"%s|%s" % k: v for k, v in recur5.items()},
        "trip": o1_trip}
    # KILL-O2: semi-forced rate across O96L2 bands
    sf = []
    for band in ("b13", "b14", "b15"):
        a = banddata.get(("o96_l2", band))
        if a:
            sf.append((band, a["semi_orbits"], a["n"],
                       round(a["semi_orbits"] / a["n"], 4)))
    o2_trip = False
    if len(sf) == 3:
        rates = [x[3] for x in sf]
        o2_trip = (rates[0] < rates[1] < rates[2]
                   and rates[0] > 0 and rates[2] / rates[0] >= 2
                   and sf[2][1] >= 3)
    rep["kills"]["KILL_O2"] = {"semi_rates_o96_l2": sf, "trip": o2_trip,
                               "o192_l2_corroborative": [
                                   (b, banddata[k]["semi_orbits"])
                                   for b in ("b16", "b17")
                                   for k in [("o192_l2", b)]
                                   if k in banddata]}
    verdict2 = "KILLED" if (o1_trip or o2_trip) else "SURVIVED"
    rep["kills"]["verdict_part2"] = verdict2

    # generic-population rho tables (diagnostics)
    for fam in ("o96_l1", "o192_l1", "o96_l2"):
        tab = []
        for (f, band), a in banddata.items():
            if f == fam:
                rho = a["Phat_gen"] / a["Ppred"] if a["Ppred"] else None
                tab.append((band, a["gen_nonempty"], a["n"],
                            round(a["Ppred"], 4),
                            round(rho, 3) if rho else None))
        rep["diagnostics"][fam + "_rho_gen"] = sorted(tab)

    # c1audit finding (NK-5)
    if aud:
        rep["diagnostics"]["c1_dedup_audit"] = {
            "violations": aud["violations"],
            "rows": [(r["L"], r["q"], r["W_raw"],
                      r["dedup"]["W_canon"], round(r["K_dedup"], 4),
                      r["violation_exact"]) for r in aud["rows"]]}

    rep["verdict"] = {
        "part1_familyB": verdict1,
        "part2_odd_nprime": verdict2,
        "overall": ("INVALID_OR_MIXED" if not controls_ok else
                    ("KILLED" if (trip or o1_trip or o2_trip)
                     else "SURVIVED"))}
    out = BASE + "wz2_eval_report.json"
    json.dump(rep, open(out, "w"), indent=1, default=str)
    print(json.dumps(rep["verdict"], indent=1))
    print("controls_ok:", controls_ok)
    print("KILL_B:", json.dumps(rep["kills"]["KILL_B"], default=str))
    print("KILL_O1 trip:", o1_trip, "sat:", sat,
          "recur3:", len(recur3), "recur5:", len(recur5))
    print("KILL_O2:", rep["kills"]["KILL_O2"])
    print("wrote", out)


if __name__ == "__main__":
    main()
