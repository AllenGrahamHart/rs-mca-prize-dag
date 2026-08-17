#!/usr/bin/env python3
"""Build a sparse kernel-lifted O0b projective boundary program."""

import re


PRIME = 2130706433
CHART_VALUES = ("finite", "infinity")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def rename_kernel(expression):
    return re.sub(r"\bk([0-7])\b", r"z\1", expression)


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
    definitions = compiled["definitions"]
    require(definitions[:3] == tuple(
        f"poly q{index}={value};"
        for index, value in enumerate(packet_row["packet"]["common_equations"])
    ), "replaceable common equations")
    require(definitions[3:11] == tuple(
        f"poly k{index}={value};"
        for index, value in enumerate(packet_row["packet"]["kernel"])
    ), "replaceable kernel definitions")
    require(compiled["equations"][3:] == ("q3", "q4", "q5", "q6", "q7"),
            "outside equation order")

    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    lift_variables = tuple(f"z{index}" for index in range(8))
    lift_definitions = tuple(
        f"poly l{index}=z{index}-({value});"
        for index, value in enumerate(packet_row["packet"]["kernel"])
    )
    # Keep every downstream expression sparse in z0,...,z7.
    case_definitions = tuple(rename_kernel(value) for value in definitions[11:])
    variables = list(compiled["variables"]) + list(lift_variables)
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
    generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        *(f"l{index}" for index in range(8)),
        "q3", "q7", *chart_equations, "rb",
    )
    program = f"""
ring R={PRIME},({','.join(variables)}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(lift_definitions)}
{chr(10).join(case_definitions)}
{chr(10).join(chart_definitions)}
poly rb=w*(b+1)-1;
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
        "kernel_lift_variable_count": len(lift_variables),
        "kernel_graph_equation_count": len(lift_definitions),
        "common_basis_size": len(basis_row["basis"]),
        "outside_equation_count": 8,
        "matching_chart_equation_count": len(chart_equations),
        "rabinowitsch_equation_count": 1,
        "boundary_guard": "b+1",
        "generator_count": len(generators),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    require(rename_kernel("k0+k1*k7+k70") == "z0+z1*z7+k70",
            "tokenwise kernel rename")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_LIFTED_BOUNDARY_PROGRAM_PASS lifts=8")
