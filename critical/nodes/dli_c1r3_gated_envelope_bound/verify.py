"""Fail-closed pose/evidence pin for dli_c1r3_gated_envelope_bound.

Pins the frozen c1r3 program packet (both rounds), replays the exact-rational
worst-row arithmetic, asserts the amber-2 headroom, and marker-pins the
Decision 6 ruling. Minted at the 2026-07-21 amber ceremony.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROG = ROOT / "critical" / "nodes" / "dli_prime_weighted_large_block_support" / "notes" / "c1r3_program_20260719"

PINS = {
    "c1r3_census_modal.py": "13a767c4931e38ef8144f91ad6ba2feb6b3285ebf2fa0412dfc52d435e701246",
    "c1r3_falsifiers.md": "2ff379120678fd642f66a1034510746b03f5d15fa5bbbe5acb0107239fca4a21",
    "c1r3_findings.md": "b28f59ed4d260193d024e73cc871dca7f33828e00a80bf0463167d7b157434ce",
    "c1r3_pose.md": "4220b966a7cde8789a785ee25f8032b202d42e7226c6dec7a9e0d5a97205eedf",
    "c1r3_pose_arith.py": "008044b2c765708aa5975ca6fca4e47221ec788b7ed10b2e02721c3c303bccdc",
    "c1r3_primecheck.py": "0dbfdeedce339a032e6e08ba905f134454eca7de2379b41aa7844cfe62ce8db5",
    "c1r3_report.md": "32dcc2746173841effca2e3092ad2768c9db02bb2a556d02c4f34d8649e6d1a1",
    "c1r3_results.md": "0c683d570375fbc105c541759e870843396f85d617f22246d7ddfb450c361836",
    "c1r3_trendfit.py": "9871a737c284ec8cb5e55bc35c1aa3d5d41f72b9bbaff22db5baa6e8763f3962",
    "c1r3b_census_modal.py": "d4a8229dc1d54a2403ce25557dbe4dc2beaaf0cb7a03843ee0302c257beaceef",
    "c1r3b_falsifiers.md": "ece54e45e1c09b508f7fd76c2780efb3feed5f269e8d4008c6849f7daa2ce0f8",
    "c1r3b_findings.md": "342a151bfa2f3e4913c1311d8efdd027f802bde7ae3810a6b8c0d23186cd76dd",
    "c1r3b_l2table.txt": "183ae3c9c49a3c5acfa39011ea65ed4e2e2cfb43927e5c14b1048167d8094975",
    "c1r3b_report.md": "c50a024f3292110d912d64c07b80d283132e05d59e8513b6bbdaef695b86c25b",
    "c1r3b_results.md": "a69dedc7b740928baab798ac6a544cc4efa23b9c5d83372d66e49457ecb9c27b",
    "c1r3b_table.txt": "0ebdbe4fd723f1cc7500a5a0b377cbb2b1b2b0fb2cfefb0a3b4d435bac571644"
}


def main() -> None:
    for name, want in PINS.items():
        got = hashlib.sha256((PROG / name).read_bytes()).hexdigest()
        assert got == want, f"packet drift: {name} {got[:16]} != {want[:16]}"

    r1_worst = Fraction(1058880560632659, 1033540934303744)
    r2_worst = Fraction(35507502101438673, 25332747971067904)
    repriced = Fraction(35377985723389915, 24013333967405056) / (1 + Fraction(1, 2))
    oct30 = Fraction(63649405960591697, 45810052493213696)
    worsts = (r1_worst, r2_worst, repriced, oct30)
    assert max(worsts) == r2_worst
    for k in worsts:
        assert k < 4, "literal line violated by a banked worst"
        assert k < 2, "amber-2 violated by a banked worst"
    assert repriced < 1, "extended-window repricing must land below iid"

    text = PROG.parent.parent.joinpath("statement.md").read_text()
    del text
    decisions = (ROOT / "notes" / "MAINTAINER_DECISIONS_20260713.md").read_text()
    assert "Decision 6" in decisions
    assert "amber-2" in decisions and "K'_r3 >= 2" in decisions

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    me = nodes["dli_c1r3_gated_envelope_bound"]
    assert me["status"] == "TARGET"
    kinds = {(e["to"], e.get("kind")) for e in dag["edges"]
             if e["from"] == "dli_c1r3_gated_envelope_bound"}
    assert ("dli_marginal_baseline100_coverage", "req") in kinds
    assert nodes["dli_marginal_baseline100_coverage"]["status"] == "CONDITIONAL"

    print(f"DLI_C1R3_GATED_ENVELOPE_BOUND_PASS pins={len(PINS)} "
          f"worst=1.4016 margin_literal=2.85x amber2_headroom={float(2/r2_worst):.2f}x")


if __name__ == "__main__":
    main()
