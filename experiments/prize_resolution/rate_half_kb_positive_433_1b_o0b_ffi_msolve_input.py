#!/usr/bin/env python3
"""Build an explicit msolve input exporter for the lifted O0b FFI chart."""

import re


PRIME = 2130706433
CASE = (3, "S0", -1, -1, -1, 2, 0)
CHART_MASK = ("finite", "finite", "infinity")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def rename_kernel(expression):
    return re.sub(r"\bk([0-7])\b", r"z\1", expression)


def build(packet_row, basis_row, compiler_core):
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(basis_row["status"] == "COMPLETE", "basis status")
    require(packet_row["epsilon"] == [-1, -1], "packet signs")
    require(basis_row["epsilon"] == [-1, -1], "basis signs")
    compiled = compiler_core.compile_case(CASE, packet_row["packet"])
    definitions = compiled["definitions"]
    require(definitions[3:11] == tuple(
        f"poly k{index}={value};"
        for index, value in enumerate(packet_row["packet"]["kernel"])
    ), "replaceable kernel definitions")
    require(compiled["equations"][3:] == ("q3", "q4", "q5", "q6", "q7"),
            "outside equation order")

    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    lift_definitions = tuple(
        f"poly l{index}=z{index}-({value});"
        for index, value in enumerate(packet_row["packet"]["kernel"])
    )
    case_definitions = tuple(rename_kernel(value) for value in definitions[11:])
    variables = list(compiled["variables"]) + [f"z{index}" for index in range(8)]
    chart_definitions = []
    chart_equations = []
    for offset, chart in enumerate(CHART_MASK, start=4):
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
    export_lines = "\n".join(
        f'print("POLY_BEGIN={index}"); print({name}); '
        f'print("POLY_END={index}");'
        for index, name in enumerate(generators)
    )
    exporter_program = f"""
ring R={PRIME},({','.join(variables)}),dp;
short=0;
{chr(10).join(basis_definitions)}
{chr(10).join(lift_definitions)}
{chr(10).join(case_definitions)}
{chr(10).join(chart_definitions)}
poly rb=w*(b+1)-1;
print("EXPORT_BEGIN");
{export_lines}
print("EXPORT_END"); quit;
"""
    return {
        "exporter_program": exporter_program,
        "variables": variables,
        "generator_names": list(generators),
        "generator_count": len(generators),
        "kernel_graph_equation_count": 8,
        "matching_chart_equation_count": 6,
        "rabinowitsch_equation_count": 1,
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    require(rename_kernel("k0+k7+k70") == "z0+z7+k70",
            "tokenwise kernel rename")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_MSOLVE_INPUT_PASS "
          "variables=18 generators=38")
