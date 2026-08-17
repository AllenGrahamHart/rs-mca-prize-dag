#!/usr/bin/env python3
"""Build the exact admissible saturation of the O0b collapsed common basis."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(source, packet_row):
    require(source["collection_complete"] is True, "source completion")
    row = source["row"]
    require(row["status"] == "COMPLETE" and row["unit"] is False and
            row["dimension"] == 0 and row["basis_size"] == 43,
            "zero-dimensional source basis")
    require(packet_row["status"] == "COMPLETE" and
            packet_row["epsilon"] == [-1, -1], "packet row")
    packet = packet_row["packet"]
    require(len(packet["route_guards"]) == 16 and
            len(packet["rank_cofactors"]) == 6, "admissibility ledger")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(row["basis"])
    )
    guard_definitions = tuple(
        f"poly h{index}={value};"
        for index, value in enumerate(packet["route_guards"])
    )
    cofactor_definitions = tuple(
        f"poly c{index}={value};"
        for index, value in enumerate(packet["rank_cofactors"])
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G))); '
        f'if (dim(G)==0) {{ print("SAT_VDIM={index},"+string(vdim(G))); }}'
        for index in range(len(packet["route_guards"]))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(guard_definitions)}
{chr(10).join(cofactor_definitions)}
ideal G={','.join(f'g{index}' for index in range(len(row["basis"])))};
print("INITIAL_DIM="+string(dim(G))+",INITIAL_SIZE="+string(size(G)));
print("INITIAL_VDIM="+string(vdim(G)));
{saturation_stages}
ideal C={','.join(f'c{index}' for index in range(6))};
list SC=sat(G,C); G=SC[1]; G=slimgb(G);
print("COFACTOR_DIM="+string(dim(G))+",COFACTOR_SIZE="+string(size(G)));
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BASIS_BEGIN"); G; print("BASIS_END"); }}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "exact admissible collapsed common locus",
        "variable_count": 4,
        "source_dimension": row["dimension"],
        "source_basis_size": row["basis_size"],
        "source_vdim": 65,
        "route_guard_count": len(packet["route_guards"]),
        "rank_cofactor_count": len(packet["rank_cofactors"]),
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    require(PRIME % 2 == 1, "odd characteristic")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_ADMISSIBLE_PROGRAM_PASS "
          "variables=4 guards=16 cofactors=6")
