#!/usr/bin/env python3
"""Reorder the FFF square subsystem through explicit normal forms."""


IDEAL_LINE = "ideal G=" + ",".join(f"g{index}" for index in range(21)) + ";"
OLD_STAGES = f"""{IDEAL_LINE}
ideal I7=G,y7; G=slimgb(I7);
print("EQUATION=7,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal I5=G,y5; G=slimgb(I5);
print("EQUATION=5,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal I6=G,y6; G=slimgb(I6);
print("EQUATION=6,DIM="+string(dim(G))+",SIZE="+string(size(G)));"""
NEW_STAGES = f"""{IDEAL_LINE}
poly n5=reduce(y5,G);
print("NORMAL=5,DEG="+string(deg(n5))+",SIZE="+string(size(n5)));
ideal I5=G,n5; G=slimgb(I5);
print("EQUATION=5,DIM="+string(dim(G))+",SIZE="+string(size(G)));
poly n7=reduce(y7,G);
print("NORMAL=7,DEG="+string(deg(n7))+",SIZE="+string(size(n7)));
ideal I7=G,n7; G=slimgb(I7);
print("EQUATION=7,DIM="+string(dim(G))+",SIZE="+string(size(G)));
poly n6=reduce(y6,G);
print("NORMAL=6,DEG="+string(deg(n6))+",SIZE="+string(size(n6)));
ideal I6=G,n6; G=slimgb(I6);
print("EQUATION=6,DIM="+string(dim(G))+",SIZE="+string(size(G)));"""


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(packet_row, basis_row, square_core):
    built = square_core.build(packet_row, basis_row)
    program = built.pop("program")
    require(program.count(OLD_STAGES) == 1, "replaceable equation stages")
    program = program.replace(OLD_STAGES, NEW_STAGES)
    return {
        **built,
        "program": program,
        "relation": "necessary FFF reduced square-subsystem superset",
        "outside_equation_order": [5, 7, 6],
        "normal_form_order": [5, 7, 6],
        "source_square_relation": built["relation"],
    }


if __name__ == "__main__":
    require(OLD_STAGES != NEW_STAGES and
            NEW_STAGES.count("reduce(") == 3, "normal-form ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_REDUCED_SQUARE_PROGRAM_PASS "
          "normal_forms=3 equation_order=5,7,6")
