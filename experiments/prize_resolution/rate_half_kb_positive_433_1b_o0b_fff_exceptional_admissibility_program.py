#!/usr/bin/env python3
"""Build guarded q4 replays for the nine surviving exceptional FFF fibers."""


PRIME = 2130706433
SURVIVOR_ROOTS = [
    0, 1, 16711679, 47655010, 451278922, 1629292471, 1893783428,
    2113994754, 2130706432,
]
EXTRA_GUARDS = ("e", "s", "x", "a0m", "a2m")
EXPECTED_STAGES = (
    ["lift"] + [f"route:{index}" for index in range(16)] +
    [f"extra:{index}" for index in range(5)] + ["cofactor", "q4"]
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def resultant(prefix):
    return (
        f"({prefix}p2*{prefix}q0-{prefix}p0*{prefix}q2)^2"
        f"-({prefix}p2*{prefix}q1-{prefix}p1*{prefix}q2)"
        f"*({prefix}p1*{prefix}q0-{prefix}p0*{prefix}q1)"
    )


def build(cache_payload, specialization_payload, root):
    packet_row = next(
        row for row in cache_payload["rows"] if row["epsilon"] == [-1, -1]
    )
    packet = packet_row["packet"]
    survivor = next(
        row for row in specialization_payload["rows"] if row["root"] == root
    )
    require(packet_row["status"] == "COMPLETE" and len(packet["kernel"]) == 8,
            "packet")
    require(len(packet["route_guards"]) == 16 and
            len(packet["rank_cofactors"]) == 6, "guard ledger")
    require(specialization_payload["collection_complete"] is True and
            root in SURVIVOR_ROOTS and survivor["status"] == "COMPLETE" and
            survivor["unit"] is False and survivor["basis_size"] ==
            len(survivor["basis"]), "survivor")
    basis_definitions = "\n".join(
        f"poly g{index}={value};" for index, value in enumerate(survivor["basis"])
    )
    kernel_definitions = "\n".join(
        f"poly k{index}={value};" for index, value in enumerate(packet["kernel"])
    )
    guard_definitions = "\n".join(
        f"poly h{index}={value};"
        for index, value in enumerate(packet["route_guards"])
    )
    cofactor_definitions = "\n".join(
        f"poly cf{index}={value};"
        for index, value in enumerate(packet["rank_cofactors"])
    )
    route_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("STAGE=route:{index},DIM="+string(dim(G))+'
        f'",SIZE="+string(size(G)));'
        for index in range(16)
    )
    extra_stages = "\n".join(
        f"ideal XH{index}=xh{index}; "
        f"list XS{index}=sat(G,XH{index}); G=XS{index}[1]; G=slimgb(G); "
        f'print("STAGE=extra:{index},DIM="+string(dim(G))+'
        f'",SIZE="+string(size(G)));'
        for index in range(5)
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(e,E,s,x,t,r,c,b),dp;
option(redSB);
{basis_definitions}
{kernel_definitions}
poly lm=-t^2;
poly a2m=k0+k1*lm+k2*lm^2;
poly a0m=k3+k4*lm+k5*lm^2;
poly r4p0=k3-b*e*k0;
poly r4p1=k4-b*e*k1;
poly r4p2=k5-b*e*k2;
poly r4q0=k3-c*e*s*k0;
poly r4q1=-k4+c*e*s*k1;
poly r4q2=k5-c*e*s*k2;
poly q4={resultant('r4')};
{guard_definitions}
poly xh0=e;
poly xh1=s;
poly xh2=x;
poly xh3=a0m;
poly xh4=a2m;
{cofactor_definitions}
ideal G={','.join(f'g{index}' for index in range(len(survivor['basis'])))},e^2-E;
G=slimgb(G);
print("STAGE=lift,DIM="+string(dim(G))+",SIZE="+string(size(G)));
{route_stages}
{extra_stages}
ideal C={','.join(f'cf{index}' for index in range(6))};
list SC=sat(G,C); G=SC[1]; G=slimgb(G);
print("STAGE=cofactor,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal I4=G,q4; G=slimgb(I4);
print("STAGE=q4,DIM="+string(dim(G))+",SIZE="+string(size(G)));
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BASIS_BEGIN"); G; print("BASIS_END"); }}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "guarded lifted q4 replay on exceptional FFF survivor",
        "engine": "Singular slimgb and saturation",
        "field": PRIME,
        "variables": ["e", "E", "s", "x", "t", "r", "c", "b"],
        "root": root,
        "source_survivor_dimension": survivor["dimension"],
        "source_survivor_basis_size": survivor["basis_size"],
        "source_survivor_basis_sha256": survivor["basis_sha256"],
        "lift_relation": "e^2-E",
        "route_guards": packet["route_guards"],
        "extra_guards": list(EXTRA_GUARDS),
        "rank_cofactor_count": len(packet["rank_cofactors"]),
        "equation": "original finite-pair q4 resultant",
        "expected_stages": EXPECTED_STAGES,
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    require(len(SURVIVOR_ROOTS) == 9 and len(EXPECTED_STAGES) == 24,
            "ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_EXCEPTIONAL_"
          "ADMISSIBILITY_PROGRAM_PASS roots=9 stages=24")
