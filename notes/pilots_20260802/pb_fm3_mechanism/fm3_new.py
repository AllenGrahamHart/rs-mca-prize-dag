#!/usr/bin/env python3
"""FM3 mechanism pilot -- run the three NEW parameter points.

The enumerator, the 13 comparators and the exact first-match selection are
IMPORTED from the banked pilot (pb_selector_orders/k1_orders.py); the only
thing this file does is inject three new entries into that module's CASES
table in memory and redirect the output directory here.  No logic is forked
and nothing in pb_selector_orders is modified.

    tools/ramguard local -- python3 .../fm3_new.py select R1
    tools/ramguard local -- python3 .../fm3_new.py stats  R1
"""
from __future__ import annotations
import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(os.path.dirname(_HERE), "pb_selector_orders")
sys.dont_write_bytecode = True
sys.path.insert(0, _BANK)
sys.path.insert(0, _HERE)
import k1_orders as KO  # noqa: E402
from fm3_predict import NEW  # noqa: E402

KO.CASES.update(NEW)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["select", "stats"])
    ap.add_argument("case")
    ap.add_argument("--zlo", type=int, default=0)
    ap.add_argument("--zhi", type=int, default=-1)
    args = ap.parse_args()
    if args.stage == "select":
        zhi = args.zhi if args.zhi >= 0 else KO.CASES[args.case]["q"]
        KO.stage_select(args.case, args.zlo, zhi, _HERE)
    else:
        KO.stage_stats(args.case, _HERE)


if __name__ == "__main__":
    main()
