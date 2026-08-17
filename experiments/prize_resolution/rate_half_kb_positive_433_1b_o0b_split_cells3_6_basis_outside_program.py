#!/usr/bin/env python3
"""Build a basis-fed O0b cells-3/6 Singular outside program."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(case, packet_row, basis_row, compiler_core):
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(basis_row["status"] == "COMPLETE", "basis status")
    require(packet_row["epsilon"] == list(case[3:5]), "packet signs")
    require(basis_row["epsilon"] == list(case[3:5]), "basis signs")
    compiled = compiler_core.compile_case(case, packet_row["packet"])
    require(compiled["definitions"][:3] == tuple(
        f"poly q{index}={value};"
        for index, value in enumerate(packet_row["packet"]["common_equations"])
    ), "replaceable common definitions")
    case_definitions = compiled["definitions"][3:]
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    outside_equations = compiled["equations"][3:]
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
        *outside_equations,
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},({','.join(compiled['variables'])}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
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
        "common_basis_size": len(basis_row["basis"]),
        "outside_equation_count": len(outside_equations),
        "guard_count": len(compiled["guards"]),
        "rank_cofactor_count": len(compiled["rank_cofactors"]),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }
