#!/usr/bin/env python3
"""Exact integer replay for the KoalaBear m2 r4 K3 allocation-inequality pilot.

Stdlib only.  No floating point anywhere.  Run under tools/ramguard.
Sections:
  A  active row constants and the reserve
  B  the 13-route positive residual workboard (KBPRW-1..4)
  C  the two closed positive routes
  D  the 433-1b -> O0b residual owner partition
  E  the lower-attack floor on the unpaid cells
  F  file digests for the binding schema
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OK = []


def chk(label, cond):
    OK.append((label, bool(cond)))
    print(("PASS " if cond else "FAIL ") + label)


print("=" * 68)
print("A. ACTIVE ROW (kb_mca) AND THE RESERVE")
print("=" * 68)
p, n, k, K = 2130706433, 2097152, 1048576, 1048577
a0, a_plus = 1116047, 1116048
q = p ** 6
B_star = q // (2 ** 128)
U_paid_cap = n - a_plus
reserve = B_star - U_paid_cap
w = a_plus - K
h = a_plus - k
print("p                      =", p)
print("n                      =", n, "= 2^21?", n == 2 ** 21)
print("k                      =", k, "= 2^20?", k == 2 ** 20)
print("K                      =", K)
print("a0                     =", a0)
print("a_plus                 =", a_plus)
print("q = p^6                =", q)
print("B_star = floor(q/2^128)=", B_star)
print("U_paid cap = n - a_plus=", U_paid_cap)
print("reserve = B_star - cap =", reserve)
print("w = a_plus - K         =", w)
print("h = a_plus - k         =", h)
chk("B_star == 274980728111395087", B_star == 274980728111395087)
chk("reserve == 274980728110413983", reserve == 274980728110413983)
chk("U_paid cap == 981104", U_paid_cap == 981104)
chk("safe-set numerator n-a_plus+1 == 981105", U_paid_cap + 1 == 981105)
chk("w == 67471 (deployed_rows.json)", w == 67471)
chk("h == 67472 (literature-map r/h pair)", h == 67472)

print()
print("=" * 68)
print("B. THE 13-ROUTE POSITIVE RESIDUAL WORKBOARD")
print("=" * 68)
# (KBPRW-1): name -> (common loops l_A l_B l_C, m_AB m_AC m_BC, defect, verdict)
common = {
    "442-0a": ((0, 0, 0), (3, 1, 1), 2, "live"),
    "442-1a": ((0, 0, 1), (4, 0, 0), 5, "delete-defect"),
    "442-1b": ((0, 1, 0), (2, 2, 0), 1, "live"),
    "442-2": ((1, 1, 0), (1, 1, 1), 2, "delete-loopcap"),
    "442-3": ((1, 1, 1), (2, 0, 0), 3, "delete-loopcap"),
    "433-0": ((0, 0, 0), (2, 2, 1), 0, "live"),
    "433-1a": ((0, 0, 1), (3, 1, 0), 3, "live"),
    "433-1b": ((1, 0, 0), (1, 1, 2), 1, "live"),
    "433-2": ((1, 0, 1), (2, 0, 1), 2, "delete-loopcap"),
    "433-3": ((1, 1, 1), (1, 1, 0), 3, "delete-loopcap"),
}
live_common = [nm for nm, v in common.items() if v[3] == "live"]
print("labeled common skeletons =", len(common))
print("live common skeletons    =", len(live_common), sorted(live_common))
chk("10 labeled skeletons", len(common) == 10)
chk("5 live common skeletons", len(live_common) == 5)

# (KBPRW-3): outside orbit -> (r, l, m, orbit_size, defect)
outside = {
    "O0a": ((0, 0, 2), (0, 0, 0), (3, 1, 1), 3, 2),
    "O0b": ((0, 1, 1), (0, 0, 0), (2, 2, 1), 3, 0),
    "O1a": ((0, 0, 2), (0, 0, 1), (4, 0, 0), 3, 5),
    "O1b": ((0, 0, 2), (0, 1, 0), (2, 2, 0), 6, 1),
    "O1c": ((0, 1, 1), (0, 0, 1), (3, 1, 0), 6, 3),
    "O1d": ((0, 1, 1), (1, 0, 0), (1, 1, 2), 3, 1),
}
print()
print("(KBPRW-2) degree/loop equations per outside orbit:")
for nm, (r, l, m, orb, dfc) in sorted(outside.items()):
    s_r, s_l, s_m = sum(r), sum(l), sum(m)
    m_full = {0: m[0] + m[1], 1: m[0] + m[2], 2: m[1] + m[2]}
    rows = [r[i] + 2 * l[i] + m_full[i] for i in range(3)]
    print("  %-4s sum r=%d sum l=%d sum m=%d  l+m=%d  rows=%s  orbit=%d defect=%d"
          % (nm, s_r, s_l, s_m, s_l + s_m, rows, orb, dfc))
    chk("%s sum r_i == 2" % nm, s_r == 2)
    chk("%s sum l_i + sum m_ij == 5" % nm, s_l + s_m == 5)
    chk("%s all degree rows == 4" % nm, rows == [4, 4, 4])
    chk("%s sum l_i <= 1" % nm, s_l <= 1)

# (KBPRW-4): total defect <= 3 and a common loop forbids an outside loop.
print()
print("(KBPRW-4) derived necessary route table:")
route_table = {}
for cname in live_common:
    cl, cm, cdef, _ = common[cname]
    has_common_loop = sum(cl) > 0
    targets = []
    for oname, (r, l, m, orb, odef) in sorted(outside.items()):
        if has_common_loop and sum(l) > 0:
            continue
        if cdef + odef <= 3:
            targets.append(oname)
    route_table[cname] = targets
    print("  %-7s (common defect %d, common loop %s) -> %s"
          % (cname, cdef, has_common_loop, ", ".join(targets)))
expected = {
    "442-0a": ["O0b", "O1b", "O1d"],
    "442-1b": ["O0a", "O0b"],
    "433-0": ["O0a", "O0b", "O1b", "O1c", "O1d"],
    "433-1a": ["O0b"],
    "433-1b": ["O0a", "O0b"],
}
chk("derived route table == printed (KBPRW-4)", route_table == expected)
total_routes = sum(len(v) for v in route_table.values())
print("total representative routes =", total_routes)
chk("13 routes", total_routes == 13)

print()
print("=" * 68)
print("C. THE TWO CLOSED POSITIVE ROUTES; THE ELEVEN OPEN ONES")
print("=" * 68)
closed = [("433-1a", "O0b"), ("433-1b", "O0a")]
all_routes = [(c, o) for c, v in route_table.items() for o in v]
open_routes = [r for r in all_routes if r not in closed]
print("closed routes =", closed)
print("open routes   =", len(open_routes))
for r in sorted(open_routes):
    print("   ", r[0], "->", r[1])
chk("11 open routes", len(open_routes) == 11)
chk("13 - 2 == 11", total_routes - len(closed) == 11)

# 433-1a -> O0b closure census (KBPCR-2)
kbpcr2 = {"[0]": 4, "[1,2]": 8, "[3,6]": 8, "[4,7]": 8, "[5,8]": 8,
          "[9,10]": 8, "[11]": 4, "[12,13]": 8, "[14]": 4}
print("433-1a->O0b common rows =", sum(kbpcr2.values()))
chk("KBPCR-2 rows sum to 60", sum(kbpcr2.values()) == 60)

# 433-1b -> O0a raw workboard census
role_cells, per_cell, per_label = 15, 7 * 15, 4 * 4
labels = role_cells * per_cell
systems = labels * per_label
print("433-1b->O0a role cells  =", role_cells)
print("433-1b->O0a raw labels  =", labels)
print("433-1b->O0a systems     =", systems)
chk("labels == 1575", labels == 1575)
chk("systems == 25200", systems == 25200)

print()
print("=" * 68)
print("D. THE 433-1b -> O0b RESIDUAL OWNER PARTITION (OPEN ROUTE)")
print("=" * 68)
blocks = {
    "split BC, product rank five": (6 * 15 * 4, 6 * 15 * 4 * 105),
    "repeated BC, cells 1/2": (16, 16 * 105),
    "repeated BC, cells 11/14": (32, 32 * 105),
}
tot_rows = sum(v[0] for v in blocks.values())
tot_labels = sum(v[1] for v in blocks.values())
for nm, (rows, labs) in blocks.items():
    print("  %-30s rows=%6d labels=%7d" % (nm, rows, labs))
print("  %-30s rows=%6d labels=%7d" % ("total", tot_rows, tot_labels))
chk("common rows == 408", tot_rows == 408)
chk("raw labels == 42840", tot_labels == 42840)
chk("6*15*4 == 360", 6 * 15 * 4 == 360)
chk("360*105 == 37800", 360 * 105 == 37800)
# cells 3/6 closure census (already PROVED, subtracted before this partition)
cell36 = 120 + 120 + 240 + 240 + 120
print("cells 3/6 per-cell census BE+CF+DE+-+DF+-+EF =", cell36)
chk("cells 3/6 per-cell census == 840", cell36 == 840)
# split-BC product-rank-drop replay
print("split-BC rank-drop cases 16*6*7*15 =", 16 * 6 * 7 * 15)
chk("split-BC cases == 10080", 16 * 6 * 7 * 15 == 10080)
# cell-11 generic rank atlas
print("cell-11 generic systems 8*2*3*15 =", 8 * 2 * 3 * 15)
chk("cell-11 generic systems == 720", 8 * 2 * 3 * 15 == 720)
chk("cell-11 rank census BC+ 248+112 == 360", 248 + 112 == 360)
chk("cell-11 boundary degree 4*4+4*6 == 40", 4 * 4 + 4 * 6 == 40)

print()
print("=" * 68)
print("E. LOWER-ATTACK FLOOR ON THE FOUR CELLS AT THE ACTIVE ROW")
print("=" * 68)
attack_a0 = 138634741058327852652
attack_a_plus = 57198030366
print("attack at a0     =", attack_a0)
print("attack at a_plus =", attack_a_plus)
chk("attack(a0) > B_star (unsafe predecessor)", attack_a0 > B_star)
chk("attack(a_plus) < B_star (lower attack ceases)", attack_a_plus < B_star)
print("attack(a0) - B_star   =", attack_a0 - B_star)
print("B_star - attack(a_plus)=", B_star - attack_a_plus)
floor_unpaid = attack_a_plus - U_paid_cap
print("floor on U_Q+U_BC+U_new = attack(a_plus) - U_paid cap =", floor_unpaid)
chk("floor_unpaid == 57197049262", floor_unpaid == 57197049262)
print("reserve - floor_unpaid  =", reserve - floor_unpaid)
chk("floor_unpaid > 0 (the three unpaid cells are not all zero)",
    floor_unpaid > 0)

print()
print("=" * 68)
print("F. FILE DIGESTS FOR THE BINDING SCHEMA")
print("=" * 68)
files = [
    "background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json",
    "background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md",
    "background/nodes/rate_half_kb_v4_tangent_source_atom/node.json",
    "background/nodes/deployed_identity_prefix_owner_scope_audit/deployed_rows.json",
    "background/nodes/rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard/statement.md",
    "background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_complete_route_exclusion/statement.md",
    "background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_raw_workboard_complete_exclusion/statement.md",
    "background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_residual_owner_partition/statement.md",
    "background/nodes/rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion/statement.md",
    "background/nodes/rate_half_kb_m2_r4_coordinate_negative_complete_exclusion/statement.md",
    "critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/node.json",
    "critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/node.json",
    "critical/nodes/rate_half_kb_m2_r4_coordinate_positive_complete_payment/node.json",
    "critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/node.json",
    "critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json",
]
for rel in files:
    fp = ROOT / rel
    d = hashlib.sha256(fp.read_bytes()).hexdigest()
    print(d, rel)

# active-row record digest, canonical JSON, kb_mca only
rows = json.loads(
    (ROOT / "background/nodes/deployed_identity_prefix_owner_scope_audit/"
            "deployed_rows.json").read_text(encoding="utf-8"))
kb = [r for r in rows["rows"] if r["row_id"] == "kb_mca"]
assert len(kb) == 1
canon = json.dumps(kb[0], sort_keys=True, separators=(",", ":"),
                   ensure_ascii=False).encode("utf-8")
print()
print("kb_mca canonical record  =", canon.decode("utf-8"))
print("kb_mca row_sha256        =", hashlib.sha256(canon).hexdigest())

# The B_star collision across rows: which rows share the budget?
share = [r["row_id"] for r in rows["rows"] if r["B_star"] == B_star]
print("rows sharing B_star      =", share)
chk("B_star alone does NOT identify the row", len(share) > 1)
same_nk = [r["row_id"] for r in rows["rows"]
           if r["n"] == n and r["k"] == k]
print("rows sharing (n,k)       =", same_nk)
chk("(n,k) alone does NOT identify the row", len(same_nk) > 1)
same_nkp = [r["row_id"] for r in rows["rows"]
            if r["n"] == n and r["k"] == k and r["p"] == p]
print("rows sharing (n,k,p)     =", same_nkp)
chk("(n,k,p) alone does NOT identify the row", len(same_nkp) > 1)
same_nkpK = [r["row_id"] for r in rows["rows"]
             if r["n"] == n and r["k"] == k and r["p"] == p and r["K"] == K]
print("rows sharing (n,k,p,K)   =", same_nkpK)
chk("(n,k,p,K) DOES identify the row", len(same_nkpK) == 1)

print()
print("=" * 68)
bad = [t for t, v in OK if not v]
print("CHECKS: %d/%d PASS" % (len(OK) - len(bad), len(OK)))
if bad:
    print("FAILED:", bad)
