#!/usr/bin/env python3
"""Build an exact ratio-graph necessary subsystem for the O0b FFF chart."""


PRIME = 2130706433
EXTRA_GUARDS = ("E", "s", "x", "a0m", "a2m")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def resultant(prefix):
    return (
        f"({prefix}p2*{prefix}q0-{prefix}p0*{prefix}q2)^2"
        f"-({prefix}p2*{prefix}q1-{prefix}p1*{prefix}q2)"
        f"*({prefix}p1*{prefix}q0-{prefix}p0*{prefix}q1)"
    )


def verify_ratio_graph():
    import sympy as sp

    A, B, E, s, x = sp.symbols("A B E s x")
    lm, bm = sp.symbols("lm bm")
    k = sp.symbols("k0:6")

    def res(p, q):
        return (
            (p[2] * q[0] - p[0] * q[2]) ** 2
            - (p[2] * q[1] - p[1] * q[2])
            * (p[1] * q[0] - p[0] * q[1])
        )

    p5 = [A*k[3] + B*k[0], A*k[4] + B*k[1],
          A*k[5] + B*k[2]]
    q5 = [A*k[3] - B*s*k[0], -A*k[4] + B*s*k[1],
          A*k[5] - B*s*k[2]]
    p5_hat = [k[3] + x*k[0], k[4] + x*k[1],
              k[5] + x*k[2]]
    q5_hat = [k[3] - x*s*k[0], -k[4] + x*s*k[1],
              k[5] - x*s*k[2]]
    require(sp.expand(res(p5, q5).subs(B, A*x) -
                      A**4 * res(p5_hat, q5_hat)) == 0,
            "q5 graph identity")

    p6 = [A*k[3] + B*s*k[0], A*k[4] + B*s*k[1],
          A*k[5] + B*s*k[2]]
    q6 = [k[3] + E*s*k[0], -k[4] - E*s*k[1],
          k[5] + E*s*k[2]]
    p6_hat = [k[3] + x*s*k[0], k[4] + x*s*k[1],
              k[5] + x*s*k[2]]
    require(sp.expand(res(p6, q6).subs(B, A*x) -
                      A**2 * res(p6_hat, q6)) == 0,
            "q6 graph identity")

    q7 = lm*bm**2*E - (B + E*A)**2
    q7_hat = lm*bm**2*E - A**2*(x + E)**2
    require(sp.expand(q7.subs(B, A*x) - q7_hat) == 0,
            "q7 graph identity")
    return True


def build(packet_row, basis_row):
    require(packet_row["status"] == "COMPLETE" and
            packet_row["epsilon"] == [-1, -1], "packet row")
    require(basis_row["status"] == "COMPLETE" and
            basis_row["epsilon"] == [-1, -1] and
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
        "poly bm=k6+k7*lm;",
        "poly gx=a2m*x-a0m;",
    )
    q5_definitions = (
        "poly r5p0=k3+x*k0;",
        "poly r5p1=k4+x*k1;",
        "poly r5p2=k5+x*k2;",
        "poly r5q0=k3-x*s*k0;",
        "poly r5q1=-k4+x*s*k1;",
        "poly r5q2=k5-x*s*k2;",
        f"poly y5={resultant('r5')};",
    )
    q6_definitions = (
        "poly r6p0=k3+x*s*k0;",
        "poly r6p1=k4+x*s*k1;",
        "poly r6p2=k5+x*s*k2;",
        "poly r6q0=k3+E*s*k0;",
        "poly r6q1=-k4-E*s*k1;",
        "poly r6q2=k5+E*s*k2;",
        f"poly y6={resultant('r6')};",
    )
    q7_definition = "poly y7=lm*bm^2*E-a2m^2*(x+E)^2;"
    guard_definitions = tuple(
        f"poly h{index}={value};"
        for index, value in enumerate(packet["route_guards"])
    )
    extra_definitions = tuple(
        f"poly xh{index}={value};"
        for index, value in enumerate(EXTRA_GUARDS)
    )
    cofactor_definitions = tuple(
        f"poly c{index}={value};"
        for index, value in enumerate(packet["rank_cofactors"])
    )
    route_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("ROUTE={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(packet["route_guards"]))
    )
    extra_stages = "\n".join(
        f"ideal XH{index}=xh{index}; "
        f"list XS{index}=sat(G,XH{index}); G=XS{index}[1]; G=slimgb(G); "
        f'print("EXTRA={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(EXTRA_GUARDS))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(E,s,x,t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(kernel_definitions)}
{chr(10).join(common_definitions)}
{chr(10).join(q5_definitions)}
{chr(10).join(q6_definitions)}
{q7_definition}
{chr(10).join(guard_definitions)}
{chr(10).join(extra_definitions)}
{chr(10).join(cofactor_definitions)}
ideal G={','.join(f'g{index}' for index in range(21))},gx; G=slimgb(G);
print("GRAPH_DIM="+string(dim(G))+",GRAPH_SIZE="+string(size(G)));
poly n5=reduce(y5,G);
print("NORMAL=5,DEG="+string(deg(n5))+",SIZE="+string(size(n5)));
ideal I5=G,n5; G=slimgb(I5);
print("EQUATION=5,DIM="+string(dim(G))+",SIZE="+string(size(G)));
poly n7=reduce(y7,G);
print("NORMAL=7,DEG="+string(deg(n7))+",SIZE="+string(size(n7)));
ideal I7=G,n7; G=slimgb(I7);
print("EQUATION=7,DIM="+string(dim(G))+",SIZE="+string(size(G)));
poly n6=reduce(y6,G);
print("NORMAL=6,DEG="+string(deg(n6))+",SIZE="+string(size(n6)));
ideal I6=G,n6; G=slimgb(I6);
print("EQUATION=6,DIM="+string(dim(G))+",SIZE="+string(size(G)));
{route_stages}
{extra_stages}
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
        "relation": "necessary FFF ratio-graph subsystem superset",
        "omitted_finite_pair": "q4",
        "variable_count": 7,
        "variables": ["E", "s", "x", "t", "r", "c", "b"],
        "graph_relation": "a2m*x-a0m",
        "common_basis_size": 21,
        "outside_equation_order": [5, 7, 6],
        "normal_form_order": [5, 7, 6],
        "route_guard_count": len(packet["route_guards"]),
        "extra_guards": list(EXTRA_GUARDS),
        "rank_cofactor_count": len(packet["rank_cofactors"]),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    verify_ratio_graph()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_RATIO_GRAPH_PROGRAM_PASS "
          "variables=7 equations=3 graph=1 guards=21")
