#!/usr/bin/env python3
"""Build original-system specialization programs for all exceptional FFF roots."""


PRIME = 2130706433
EQUATION_ORDER = ["base", "q5", "q7", "q6"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(cache_payload, graph_payload, roots_payload, root):
    packet_row = next(
        row for row in cache_payload["rows"] if row["epsilon"] == [-1, -1]
    )
    packet = packet_row["packet"]
    graph = graph_payload["row"]
    roots = roots_payload["row"]["roots"]
    require(packet_row["status"] == "COMPLETE" and len(packet["kernel"]) == 8,
            "packet")
    require(graph_payload["collection_complete"] is True and
            graph["status"] == "COMPLETE" and graph["unit"] is False and
            graph["dimension"] == 1 and graph["basis_size"] == 48 and
            len(graph["basis"]) == 48, "admissible graph")
    require(roots_payload["collection_complete"] is True and
            roots_payload["row"]["status"] == "COMPLETE" and
            roots_payload["row"]["root_count"] == len(roots) == 14 and
            root in roots, "exceptional root")
    basis_definitions = "\n".join(
        f"poly g{index}={value};" for index, value in enumerate(graph["basis"])
    )
    kernel_definitions = "\n".join(
        f"poly k{index}={value};" for index, value in enumerate(packet["kernel"])
    )
    base_generators = ",".join(f"g{index}" for index in range(48))
    program = f"""
ring R={PRIME},(E,s,x,t,r,c,b),dp;
option(redSB);
{basis_definitions}
{kernel_definitions}
poly lm=-t^2;
poly a2m=k0+k1*lm+k2*lm^2;
poly bm=k6+k7*lm;
poly q5=( (k5+x*k2)*(k3-x*s*k0)-(k3+x*k0)*(k5-x*s*k2) )^2
       -( (k5+x*k2)*(-k4+x*s*k1)-(k4+x*k1)*(k5-x*s*k2) )
        *( (k4+x*k1)*(k3-x*s*k0)-(k3+x*k0)*(-k4+x*s*k1) );
poly q7=lm*bm^2*E-a2m^2*(x+E)^2;
poly q6=( (k5+x*s*k2)*(k3+E*s*k0)-(k3+x*s*k0)*(k5+E*s*k2) )^2
       -( (k5+x*s*k2)*(-k4-E*s*k1)-(k4+x*s*k1)*(k5+E*s*k2) )
        *( (k4+x*s*k1)*(k3+E*s*k0)-(k3+x*s*k0)*(-k4-E*s*k1) );
ideal G={base_generators},t-{root}; G=slimgb(G);
print("STAGE=base,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal G5=G,q5; G=slimgb(G5);
print("STAGE=q5,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal G7=G,q7; G=slimgb(G7);
print("STAGE=q7,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal G6=G,q6; G=slimgb(G6);
print("STAGE=q6,DIM="+string(dim(G))+",SIZE="+string(size(G)));
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BASIS_BEGIN"); G; print("BASIS_END"); }}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "original guarded FFF q5-q7-q6 exceptional specialization",
        "engine": "Singular slimgb",
        "field": PRIME,
        "variables": ["E", "s", "x", "t", "r", "c", "b"],
        "root": root,
        "source_graph_basis_size": 48,
        "source_graph_basis_sha256": graph["basis_sha256"],
        "source_graph_dimension": 1,
        "equation_order": EQUATION_ORDER,
        "omitted_finite_pair": "q4",
        "uses_generic_rational_basis": False,
        "packet_sha256": packet_row["packet_sha256"],
        "root_polynomial_sha256": roots_payload["row"][
            "field_root_polynomial_sha256"
        ],
    }


if __name__ == "__main__":
    require(EQUATION_ORDER == ["base", "q5", "q7", "q6"], "equation order")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_EXCEPTIONAL_"
          "SPECIALIZATIONS_PROGRAM_PASS roots=14 stages=4")
