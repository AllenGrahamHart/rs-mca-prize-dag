#!/usr/bin/env python3
"""Build the exact root-free presentation of the collapsed O0b FFI chart."""


EXACT_GUARDS = ("m4p1", "m5p1")
OLD_RABINOWITSCH = "poly rb=w*f*(d^2-e^2)*(b+1)-1;"
NEW_RABINOWITSCH = (
    "poly rb=w*f*(d^2-e^2)*(b+1)*m4p1*m5p1-1;"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(packet_row, basis_row, compiler_core, rootfree_core):
    built = rootfree_core.build(packet_row, basis_row, compiler_core)
    require(built["relation"] == "necessary determinant superset",
            "root-free source relation")
    program = built.pop("program")
    require(program.count(OLD_RABINOWITSCH) == 1,
            "replaceable Rabinowitsch equation")
    program = program.replace(OLD_RABINOWITSCH, NEW_RABINOWITSCH)
    require(all(guard in program for guard in EXACT_GUARDS),
            "finite-slope guards present")
    return {
        **built,
        "program": program,
        "relation": "exact collapsed FFI finite-root chart",
        "finite_slope_guards": list(EXACT_GUARDS),
        "slope_anchor_node":
            "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_"
            "xi2_pairing0_collapsed_finite_slope_anchors",
    }


if __name__ == "__main__":
    require(OLD_RABINOWITSCH != NEW_RABINOWITSCH,
            "strict guard strengthening")
    require(NEW_RABINOWITSCH.count("m4p1") == 1 and
            NEW_RABINOWITSCH.count("m5p1") == 1,
            "two exact slope guards")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_EXACT_ROOTFREE_PROGRAM_PASS "
          "slope_guards=2")
