"""k3_chain_seams attack A5 (owner/partition mismatch): scan every node.json
shard for ordered pairs (X -> Y) that carry BOTH a req edge and an ev edge.

Motivation: the band decomposition plan says the kb_m2_r4 workboard's
"existing ev edges migrate here as the req-side"; the ledger shard declares
evidence_for -> rate_half_band_structural_surplus while structural_surplus
declares requires <- ledger. If double-wiring is unique to this pair it is a
migration residue; if it is common, it is convention. This scan decides that
empirically instead of by assertion.

RAM discipline: one shard at a time, only edge lists retained. stdlib only.
"""

import json
import os

ROOTS = ["critical/nodes", "background/nodes"]


def main():
    req = set()   # (from, to)
    ev = set()    # (from, to)
    seen = 0
    bad = []
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for d in sorted(os.listdir(root)):
            p = os.path.join(root, d, "node.json")
            if not os.path.isfile(p):
                continue
            try:
                with open(p) as fh:
                    obj = json.load(fh)
            except Exception as e:
                bad.append((d, str(e)))
                continue
            seen += 1
            nid = obj.get("node", {}).get("id", d)
            for e in obj.get("requires", []) or []:
                if "from" in e:
                    req.add((e["from"], nid))
            for e in obj.get("evidence_for", []) or []:
                if "to" in e:
                    ev.add((nid, e["to"]))
            del obj

    both = sorted(req & ev)
    print("shards scanned:", seen)
    print("unreadable shards:", len(bad))
    print("distinct req edges:", len(req))
    print("distinct ev  edges:", len(ev))
    print("ordered pairs carrying BOTH req and ev:", len(both))
    for a, b in both:
        print("  BOTH:", a, "->", b)

    # focused: everything pointing into the K3 chain
    chain = {
        "rate_half_band_closure",
        "rate_half_band_structural_surplus",
        "rate_half_band_crossing_location",
        "rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger",
        "rate_half_kb_m2_r4_k3_independent_review",
        "rate_half_kb_m2_r4_k3_orientation_assembly",
        "rate_half_kb_m2_r4_k3_allocation_inequality",
        "rate_half_kb_m2_r4_coordinate_positive_complete_payment",
        "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment",
    }
    print()
    print("=== inbound edges to each chain node ===")
    for c in sorted(chain):
        r = sorted(a for (a, b) in req if b == c)
        e = sorted(a for (a, b) in ev if b == c)
        print(f"-- {c}")
        print(f"   req in ({len(r)}): {r}")
        print(f"   ev  in ({len(e)}): {e if len(e) <= 12 else str(e[:12]) + ' ...+%d' % (len(e) - 12)}")
    print()
    print("=== outbound edges from each chain node ===")
    for c in sorted(chain):
        r = sorted(b for (a, b) in req if a == c)
        e = sorted(b for (a, b) in ev if a == c)
        print(f"-- {c}")
        print(f"   req out ({len(r)}): {r}")
        print(f"   ev  out ({len(e)}): {e}")


if __name__ == "__main__":
    main()
