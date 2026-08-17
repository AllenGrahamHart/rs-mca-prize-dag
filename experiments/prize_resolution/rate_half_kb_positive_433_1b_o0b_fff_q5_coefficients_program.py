#!/usr/bin/env python3
"""Build coefficient-wise q5 reductions on the admissible FFF base graph."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_decomposition():
    import sympy as sp

    s = sp.symbols("s")
    p0, p1, p2 = sp.symbols("p0 p1 p2")
    q00, q01, q10, q11, q20, q21 = sp.symbols(
        "q00 q01 q10 q11 q20 q21"
    )
    q0, q1, q2 = q00+s*q01, q10+s*q11, q20+s*q21
    aa0, aa1 = p2*q00-p0*q20, p2*q01-p0*q21
    bb0, bb1 = p2*q10-p1*q20, p2*q11-p1*q21
    cc0, cc1 = p1*q00-p0*q10, p1*q01-p0*q11
    coefficients = (
        aa0**2-bb0*cc0,
        2*aa0*aa1-bb0*cc1-bb1*cc0,
        aa1**2-bb1*cc1,
    )
    resultant = (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
    require(sp.expand(resultant-sum(value*s**index
                                    for index, value in enumerate(coefficients)))
            == 0, "quadratic coefficient identity")
    return coefficients


def build(packet_row, graph_payload):
    require(packet_row["status"] == "COMPLETE" and
            packet_row["epsilon"] == [-1, -1], "packet row")
    require(graph_payload["collection_complete"] is True and
            graph_payload["field"] == PRIME, "graph payload")
    graph = graph_payload["row"]
    require(graph["status"] == "COMPLETE" and graph["unit"] is False and
            graph["dimension"] == 1 and graph["basis_size"] == 48 and
            len(graph["basis"]) == 48, "graph basis")
    packet = packet_row["packet"]
    require(len(packet["kernel"]) == 8, "kernel ledger")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(graph["basis"])
    )
    kernel_definitions = tuple(
        f"poly k{index}={value};" for index, value in enumerate(packet["kernel"])
    )
    coefficient_definitions = (
        "poly p0=k3+x*k0;",
        "poly p1=k4+x*k1;",
        "poly p2=k5+x*k2;",
        "poly q00=k3;",
        "poly q01=-x*k0;",
        "poly q10=-k4;",
        "poly q11=x*k1;",
        "poly q20=k5;",
        "poly q21=-x*k2;",
        "poly aa0=p2*q00-p0*q20;",
        "poly aa1=p2*q01-p0*q21;",
        "poly bb0=p2*q10-p1*q20;",
        "poly bb1=p2*q11-p1*q21;",
        "poly cc0=p1*q00-p0*q10;",
        "poly cc1=p1*q01-p0*q11;",
        "poly y50=aa0^2-bb0*cc0;",
        "poly y51=2*aa0*aa1-bb0*cc1-bb1*cc0;",
        "poly y52=aa1^2-bb1*cc1;",
    )
    reduction_stages = "\n".join(
        (
            f"poly n5{index}=reduce(y5{index},G); "
            f'print("COEFFICIENT={index},DEG="+string(deg(n5{index}))'
            f'+",SIZE="+string(size(n5{index}))); '
            f'print("C{index}_BEGIN"); print(n5{index}); print("C{index}_END");'
        )
        for index in range(3)
    )
    program = f"""
ring R={PRIME},(x,t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(kernel_definitions)}
{chr(10).join(coefficient_definitions)}
ideal G={','.join(f'g{index}' for index in range(48))};
{reduction_stages}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "exact q5 coefficients on admissible FFF base graph",
        "variable_count": 5,
        "variables": ["x", "t", "r", "c", "b"],
        "coefficient_order": [0, 1, 2],
        "s_degree": 2,
        "graph_basis_size": 48,
        "graph_basis_sha256": graph["basis_sha256"],
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    verify_decomposition()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_Q5_COEFFICIENTS_PROGRAM_PASS "
          "coefficients=3 s_degree=2")
