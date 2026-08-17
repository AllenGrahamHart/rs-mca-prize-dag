#!/usr/bin/env python3
"""Build exact basis-fed projective-chart programs for O0b resultants."""


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
    # Definitions 0..2 are replaced by the saturated common basis.
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
    guard_definitions = tuple(
        f"poly h{index}={value};"
        for index, value in enumerate(compiled["guards"])
    )
    cofactor_definitions = tuple(
        f"poly c{index}={value};"
        for index, value in enumerate(compiled["rank_cofactors"])
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(compiled["guards"]))
    )
    initial_generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        "q3", "q7", *chart_equations,
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},({','.join(variables)}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
{chr(10).join(chart_definitions)}
{chr(10).join(guard_definitions)}
{chr(10).join(cofactor_definitions)}
ideal I={','.join(initial_generators)};
ideal G=slimgb(I);
print("INITIAL_DIM="+string(dim(G))+",INITIAL_SIZE="+string(size(G)));
{saturation_stages}
ideal C={','.join(f'c{index}' for index in range(6))};
list SC=sat(G,C); G=SC[1]; G=slimgb(G);
print("COFACTOR_DIM="+string(dim(G))+",COFACTOR_SIZE="+string(size(G)));
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
        "guard_count": len(compiled["guards"]),
        "rank_cofactor_count": len(compiled["rank_cofactors"]),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


def verify_masks():
    from itertools import product

    masks = tuple(product(CHART_VALUES, repeat=3))
    require(len(masks) == 8 and len(set(masks)) == 8, "chart mask census")
    require(masks[0] == ("finite", "finite", "finite") and
            masks[-1] == ("infinity", "infinity", "infinity"),
            "chart mask order")
    return masks


if __name__ == "__main__":
    masks = verify_masks()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_PROJECTIVE_CHART_PROGRAM_PASS "
          f"charts={len(masks)}")
