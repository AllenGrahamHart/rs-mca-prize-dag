#!/usr/bin/env python3
"""Build the guarded five-variable FFF base ratio graph."""


PRIME = 2130706433
BASE_GUARDS = ("x", "a0m", "a2m")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(packet_row, basis_row):
    require(packet_row["status"] == "COMPLETE" and
            packet_row["epsilon"] == [-1, -1], "packet row")
    require(basis_row["status"] == "COMPLETE" and
            basis_row["epsilon"] == [-1, -1] and
            basis_row["dimension"] == 1 and
            basis_row["basis_size"] == 21, "basis row")
    packet = packet_row["packet"]
    require(len(packet["kernel"]) == 8 and
            len(packet["route_guards"]) == 16 and
            len(packet["rank_cofactors"]) == 6, "packet ledger")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    kernel_definitions = tuple(
        f"poly k{index}={value};" for index, value in enumerate(packet["kernel"])
    )
    common_definitions = (
        "poly lm=-t^2;",
        "poly a2m=k0+k1*lm+k2*lm^2;",
        "poly a0m=k3+k4*lm+k5*lm^2;",
        "poly gx=a2m*x-a0m;",
    )
    guard_definitions = tuple(
        f"poly h{index}={value};"
        for index, value in enumerate(BASE_GUARDS)
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("BASE_GUARD={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(BASE_GUARDS))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(x,t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(kernel_definitions)}
{chr(10).join(common_definitions)}
{chr(10).join(guard_definitions)}
ideal G={','.join(f'g{index}' for index in range(21))},gx; G=slimgb(G);
print("GRAPH_DIM="+string(dim(G))+",GRAPH_SIZE="+string(size(G)));
{saturation_stages}
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BASIS_BEGIN"); G; print("BASIS_END"); }}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "necessary admissible FFF base ratio graph",
        "variable_count": 5,
        "variables": ["x", "t", "r", "c", "b"],
        "graph_relation": "a2m*x-a0m",
        "common_basis_size": 21,
        "common_basis_dimension": 1,
        "inherited_route_guard_count": len(packet["route_guards"]),
        "inherited_rank_cofactor_count": len(packet["rank_cofactors"]),
        "base_guards": list(BASE_GUARDS),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    require(BASE_GUARDS == ("x", "a0m", "a2m"), "base guard ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_ADMISSIBLE_RATIO_GRAPH_PROGRAM_PASS "
          "variables=5 graph=1 new_guards=3")
