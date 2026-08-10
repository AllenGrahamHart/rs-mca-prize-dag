"""k3_chain_seams attack A5 (owner/partition mismatch), link 4:
verify the 13-route positive partition claimed across three texts.

Texts compared (all quoted in REPORT.md):
  critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/statement.md:11-18
  critical/nodes/rate_half_kb_m2_r4_coordinate_positive_complete_payment/conditional.md:3-8
  critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/statement.md:11-13

Kill condition: an overlap, a miscount, or a route named in one text and
absent from the others. Stdlib only; the route lists are transcribed here
by hand from the statements (transcription is the object under test, so it
is printed back for eyeball comparison).
"""

# from remaining_route_payment/statement.md:14-18 (the eleven this target owns)
REMAINING = [
    ("442-0a", "O0b"), ("442-0a", "O1b"), ("442-0a", "O1d"),
    ("442-1b", "O0a"), ("442-1b", "O0b"),
    ("433-0", "O0a"), ("433-0", "O0b"), ("433-0", "O1b"),
    ("433-0", "O1c"), ("433-0", "O1d"),
    ("433-1b", "O0b"),
]

# from remaining_route_payment/statement.md:7-8 and complete_payment/conditional.md:4-6
CLOSED = [("433-1a", "O0b"), ("433-1b", "O0a")]


def main():
    r = set(REMAINING)
    c = set(CLOSED)
    print("remaining routes transcribed :", len(REMAINING), "distinct:", len(r))
    for x in REMAINING:
        print("   ", x[0], "->", x[1])
    print("closed routes transcribed    :", len(CLOSED), "distinct:", len(c))
    for x in CLOSED:
        print("   ", x[0], "->", x[1])
    print()
    print("overlap remaining & closed   :", sorted(r & c), "(kill if nonempty)")
    print("duplicate inside remaining   :", len(REMAINING) != len(r), "(kill if True)")
    print("total distinct routes        :", len(r | c))
    print("complete_payment/conditional.md:7 claims 1+1+11 = 13  ->",
          "CONSISTENT" if len(r | c) == 13 and len(r) == 11 and len(c) == 2 else "MISMATCH")
    print("ledger/statement.md:12 claims 'all thirteen positive routes' ->",
          "CONSISTENT" if len(r | c) == 13 else "MISMATCH")

    # per-source-cell breakdown, to expose any silently missing (source, target)
    from collections import defaultdict
    by_src = defaultdict(list)
    for s, t in sorted(r | c):
        by_src[s].append(t)
    print()
    print("per-source breakdown of the 13:")
    for s in sorted(by_src):
        print("   %-8s -> %s   (%d)" % (s, ", ".join(sorted(by_src[s])), len(by_src[s])))

    # structural_surplus/statement.md:24-26 says only 433-1a->O0b and
    # 433-1b->O0a are closed, "leaving eleven named route payments"
    print()
    print("structural_surplus/statement.md:24-26 'eleven named route payments' ->",
          "CONSISTENT" if len(r) == 11 else "MISMATCH")


if __name__ == "__main__":
    main()
