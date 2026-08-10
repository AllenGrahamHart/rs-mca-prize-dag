#!/usr/bin/env python3
"""D3 corollary + row inventory.

(a) COFACTOR LAW.  NORMLAW pins v_2(Norm-1)=7 on FAM-B (d3_law.py).  With
    N = c*p, c = 1+128g, p = 1+128q, N-1 = 128(g+q) mod 256, so exactly one
    of c, p has v_2 = 7: a FAM-B hit with v_2(p-1) >= 8 FORCES c = 129 mod 256.
    Tested against the banked round-24 v2hunt witnesses.
(b) The v_2(p-1) of every pinned/deployed row, for the record.
"""
import glob
import json
import sys

sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


print("(a) round-24 FAM-B witnesses: v_2(p-1) vs cofactor mod 256")
ok = bad = 0
rows = []
for f in sorted(glob.glob(
        "notes/pilots_20260808/kernel_window_hunt/state/v2hunt_*.json")):
    st = json.load(open(f))
    for r in st["best"]:
        p, c = int(r["p"]), int(r["cof"])
        vp, vc = v2(p - 1), v2(c - 1) if c > 1 else None
        pred = (c % 256 == 129)
        good = (vp == 7) or pred
        ok += good
        bad += not good
        rows.append((vp, c, c % 256, vc, good))
rows.sort(key=lambda t: -t[0])
for vp, c, c256, vc, good in rows[:12]:
    print("   v2(p-1)=%-3d cof=%-8d cof mod 256=%-4d v2(cof-1)=%-4s %s"
          % (vp, c, c256, vc, "OK" if good else "VIOLATION"))
print("   law holds on %d/%d banked witnesses (violations %d)"
      % (ok, ok + bad, bad))

print("\n(b) v_2(p-1) of the pinned and deployed rows")
ROWS = [
    ("E1-128 pinned exhibit field (2^249)",
     904625697166646869347790708689937759412227977745095982970820953353127723009),
    ("deployed Proth rate 1/2 (n=2^41)",
     132540169958804033333249306710494641010898987122689),
    ("deployed Proth rate 1/4 (n=2^42)",
     411940680852499481698306614369841346700408394874881),
    ("deployed Proth rate 1/8 (n=2^43)",
     979947269755402568812854322316630667196565607677953),
    ("deployed Proth rate 1/16 (n=2^44)",
     2121285573237585848299875619011192262679065433997313),
]
for name, p in ROWS:
    assert K.is_probable_prime(p), name
    print("   %-38s %4d bits  v_2(p-1) = %3d  p=1 mod 128: %s"
          % (name, p.bit_length(), v2(p - 1), p % 128 == 1))
