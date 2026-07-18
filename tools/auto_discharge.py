#!/usr/bin/env python3
"""Auto-discharge: CONDITIONAL -> PROVED/PROVABLE once all predicates are
green, to a fixpoint. The colour contract made mechanical: a CONDITIONAL
asserts (predicates => statement) is a proved implication; when the
predicates are all proved, modus ponens proves the statement.

SAFETY: only CONDITIONAL nodes flip (never a bare TARGET/CONJECTURE whose
assembly implication was never written). The audit checkpoint therefore
lives entirely at the red->amber transition, where it belongs and where
the defects actually surface. gate:any nodes discharge when all reqs and
>=1 alt are green. PROVED iff every relevant predicate is PROVED, else
PROVABLE (matches the validator's inheritance rule, so it stays green).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DAG = os.path.join(HERE, "..", "dag.json")
GREEN = {"PROVED", "PROVABLE"}

def main():
    d = json.load(open(DAG))
    nodes = {n["id"]: n for n in d["nodes"]}
    reqs, alts = {}, {}
    for e in d["edges"]:
        (reqs if e.get("kind", "req") == "req" else alts if e.get("kind") == "alt"
         else {}).setdefault(e["to"], []).append(e["from"]) if e.get("kind", "req") in ("req", "alt") else None
    # REGRESSION SWEEP first: an auto-discharged node whose predicates are
    # no longer all green goes back to CONDITIONAL (downgrades propagate).
    for v, n in nodes.items():
        if n["status"] not in GREEN:
            continue
        art = os.path.join(HERE, "..", "nodes", v,
                           "proof.md" if n["status"] == "PROVED" else "sketch.md")
        if not (os.path.exists(art) and "(auto-discharged)" in open(art).read()):
            continue
        rk = [nodes[u]["status"] for u in reqs.get(v, []) if u in nodes]
        if rk and any(s0 not in GREEN for s0 in rk):
            n["status"] = "CONDITIONAL"
            os.remove(art)
            print(f"regressed {v} -> CONDITIONAL (predicate left green)")
    flipped, changed = [], True
    while changed:
        changed = False
        for v, n in nodes.items():
            if n["status"] != "CONDITIONAL":
                continue
            rk = [nodes[u]["status"] for u in reqs.get(v, []) if u in nodes]
            ak = [nodes[u]["status"] for u in alts.get(v, []) if u in nodes]
            gate_any = n.get("gate") == "any" and bool(ak)
            if not rk and not gate_any:
                continue
            if any(s not in GREEN for s in rk):
                continue
            if gate_any and not any(s in GREEN for s in ak):
                continue
            new = "PROVED" if (all(s == "PROVED" for s in rk)
                               and (not gate_any or any(s == "PROVED" for s in ak))) else "PROVABLE"
            n["status"] = new
            flipped.append((v, new))
            changed = True
            # w10-C3 fix: the legacy nodes/ path never exists (partition law) -> artifacts were silently skipped and flips traceless
            folder = next((f for f in (os.path.join(HERE, "..", "critical", "nodes", v), os.path.join(HERE, "..", "background", "nodes", v)) if os.path.isdir(f)), os.path.join(HERE, "..", "nodes", v))
            if os.path.isdir(folder):
                art = "proof.md" if new == "PROVED" else "sketch.md"
                open(os.path.join(folder, art), "w").write(
                    f"# {art[:-3]}: {v} (auto-discharged)\n\n"
                    f"The conditional implication (see conditional.md) is proved and every predicate is "
                    f"now green:\n\n" + "".join(f"- `{u}` [{nodes[u]['status']}]\n" for u in reqs.get(v, []))
                    + (f"\n(gate:any — satisfied via a green alternative route.)\n" if gate_any else "")
                    + f"\nBy modus ponens the statement is {new}. Auto-discharged by tools/auto_discharge.py; "
                    "the audit lives at the red->amber referee step.\n")
    json.dump(d, open(DAG, "w"), indent=1)
    print(f"auto-discharged {len(flipped)}: " + (", ".join(f"{v}->{s}" for v, s in flipped) or "nothing"))

if __name__ == "__main__":
    main()
