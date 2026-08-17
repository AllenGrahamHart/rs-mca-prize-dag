#!/usr/bin/env python3
"""Build direct Rabinowitsch boundary tests for O0b projective charts."""


PRIME = 2130706433
CHART_VALUES = ("finite", "infinity")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(case, chart_mask, packet_row, basis_row, compiler_core):
    chart_mask = tuple(chart_mask)
    require(len(chart_mask) == 3 and
            all(value in CHART_VALUES for value in chart_mask),
            "projective chart mask")
    require(chart_mask.count("finite") >= 2, "multi-finite chart scope")
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(basis_row["status"] == "COMPLETE", "basis status")
    require(packet_row["epsilon"] == list(case[3:5]), "packet signs")
    require(basis_row["epsilon"] == list(case[3:5]), "basis signs")
    compiled = compiler_core.compile_case(case, packet_row["packet"])
    require(compiled["equations"][3:] == ("q3", "q4", "q5", "q6", "q7"),
            "outside equation order")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    case_definitions = list(compiled["definitions"][3:])
    variables = list(compiled["variables"])
    chart_definitions = []
    chart_equations = []
    for offset, chart in enumerate(chart_mask, start=4):
        prefix = f"m{offset}"
        left_name = f"x{offset}p"
        right_name = f"x{offset}q"
        if chart == "finite":
            root = f"u{offset}"
            variables.append(root)
            left = f"{prefix}p0+{prefix}p1*{root}+{prefix}p2*{root}^2"
            right = f"{prefix}q0+{prefix}q1*{root}+{prefix}q2*{root}^2"
        else:
            left = f"{prefix}p2"
            right = f"{prefix}q2"
        chart_definitions.extend((
            f"poly {left_name}={left};",
            f"poly {right_name}={right};",
        ))
        chart_equations.extend((left_name, right_name))
    variables.append("w")
    rabinowitsch_definition = "poly rb=w*(b+1)-1;"
    generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        "q3", "q7", *chart_equations, "rb",
    )
    program = f"""
ring R={PRIME},({','.join(variables)}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
{chr(10).join(chart_definitions)}
{rabinowitsch_definition}
ideal I={','.join(generators)};
ideal G=slimgb(I);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); G; }}
print("END"); quit;
"""
    return {
        "program": program,
        "chart_mask": list(chart_mask),
        "variable_count": len(variables),
        "finite_root_count": chart_mask.count("finite"),
        "common_basis_size": len(basis_row["basis"]),
        "outside_equation_count": 8,
        "matching_chart_equation_count": len(chart_equations),
        "rabinowitsch_equation_count": 1,
        "rabinowitsch_variable": "w",
        "boundary_guard": "b+1",
        "generator_count": len(generators),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


def verify_masks():
    from itertools import product

    masks = tuple(
        mask for mask in product(CHART_VALUES, repeat=3)
        if mask.count("finite") >= 2
    )
    require(len(masks) == 4 and len(set(masks)) == 4, "multi-finite census")
    return masks


if __name__ == "__main__":
    masks = verify_masks()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_PROJECTIVE_BOUNDARY_PROGRAM_PASS "
          f"charts={len(masks)}")
