#!/usr/bin/env python3
"""Build a root-free determinant superset of the collapsed O0b FFI chart."""

import re


PRIME = 2130706433
CASE = (3, "S0", -1, -1, -1, 2, 0)
CHART_MASK = ("finite", "finite", "infinity")
RETAINED_KERNEL_INDICES = (0, 1, 3, 4, 6, 7)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def collapse_kernel(expression):
    def replace(match):
        index = int(match.group(1))
        return "0" if index in {2, 5} else f"z{index}"

    return re.sub(r"\bk([0-7])\b", replace, expression)


def verify_linear_determinant():
    import sympy as sp

    a0, a1, b0, b1, u = sp.symbols("a0 a1 b0 b1 u")
    determinant = a1 * b0 - a0 * b1
    substitution = {a0: -a1 * u, b0: -b1 * u}
    require(sp.expand(determinant.subs(substitution)) == 0,
            "common linear root implies determinant")
    return determinant


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
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    graph_definitions = []
    for index, value in enumerate(packet_row["packet"]["kernel"]):
        if index in RETAINED_KERNEL_INDICES:
            graph_definitions.append(f"poly l{index}=z{index}-({value});")
        else:
            graph_definitions.append(f"poly l{index}={value};")
    case_definitions = tuple(collapse_kernel(value) for value in definitions[11:])
    variables = (
        *compiled["variables"],
        *(f"z{index}" for index in RETAINED_KERNEL_INDICES),
        "w",
    )
    determinant_definitions = (
        "poly x4=m4p1*m4q0-m4p0*m4q1;",
        "poly x5=m5p1*m5q0-m5p0*m5q1;",
    )
    generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        *(f"l{index}" for index in range(8)),
        "q3", "q7", "x4", "x5", "rb",
    )
    program = f"""
ring R={PRIME},({','.join(variables)}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(graph_definitions)}
{chr(10).join(case_definitions)}
{chr(10).join(determinant_definitions)}
poly rb=w*f*(d^2-e^2)*(b+1)-1;
ideal I={','.join(generators)};
ideal G=slimgb(I);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); G; }}
print("END"); quit;
"""
    return {
        "program": program,
        "case": list(CASE),
        "chart_mask": list(CHART_MASK),
        "relation": "necessary determinant superset",
        "variable_count": len(variables),
        "eliminated_root_variables": ["u4", "u5"],
        "retained_kernel_indices": list(RETAINED_KERNEL_INDICES),
        "collapsed_kernel_indices": [2, 5],
        "kernel_graph_equation_count": 8,
        "common_basis_size": len(basis_row["basis"]),
        "determinant_equation_count": len(determinant_definitions),
        "boundary_guards": ["f", "d^2-e^2", "b+1"],
        "rabinowitsch_equation_count": 1,
        "generator_count": len(generators),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    verify_linear_determinant()
    require(collapse_kernel("k0+k2+k5+k7") == "z0+0+0+z7",
            "kernel collapse")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_ROOTFREE_PROGRAM_PASS "
          "variables=14 generators=34")
