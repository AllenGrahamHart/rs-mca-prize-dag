#!/usr/bin/env python3
"""Build a six-variable ratio reduction for the canonical O0b FFF chart."""


PRIME = 2130706433
EXTRA_GUARDS = ("e", "s", "a0m", "a2m")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def resultant(prefix):
    return (
        f"({prefix}p2*{prefix}q0-{prefix}p0*{prefix}q2)^2"
        f"-({prefix}p2*{prefix}q1-{prefix}p1*{prefix}q2)"
        f"*({prefix}p1*{prefix}q0-{prefix}p0*{prefix}q1)"
    )


def verify_ratio_reduction():
    import sympy as sp

    d, e, f, ratio = sp.symbols("d e f ratio")
    a2m, a0m, lm, bm = sp.symbols("a2m a0m lm bm")
    substitutions = {
        f: e * ratio,
        d: a0m / (e * a2m),
    }
    require(sp.cancel((d*e*a2m-a0m).subs(substitutions)) == 0,
            "q3 anchor")
    require(sp.cancel((f/e-ratio).subs(substitutions)) == 0,
            "ratio definition")
    records = {
        "q4_left": sp.cancel((sp.Symbol("b")*e).subs(substitutions)),
        "q4_right": sp.cancel((sp.Symbol("c")*f).subs(substitutions)),
        "q5_left": sp.cancel((-d*e).subs(substitutions)),
        "q5_right": sp.cancel((d*f).subs(substitutions)),
        "q6_left": sp.cancel((-d*f).subs(substitutions)),
        "q6_right": sp.cancel((-e*f).subs(substitutions)),
    }
    require(records["q5_left"] == -a0m/a2m and
            records["q5_right"] == a0m*ratio/a2m and
            records["q6_left"] == -a0m*ratio/a2m and
            records["q6_right"] == -e**2*ratio,
            "ratio record ledger")
    q7 = lm*bm**2-(d+e)**2*a2m**2
    numerator = lm*bm**2*e**2-(a0m+e**2*a2m)**2
    require(sp.cancel(q7.subs(substitutions)*e**2-numerator) == 0,
            "q7 cleared numerator")
    return substitutions, records, numerator


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
    )
    q4_definitions = (
        "poly r4p0=k3-b*e*k0;",
        "poly r4p1=k4-b*e*k1;",
        "poly r4p2=k5-b*e*k2;",
        "poly r4q0=k3-c*e*s*k0;",
        "poly r4q1=-k4+c*e*s*k1;",
        "poly r4q2=k5-c*e*s*k2;",
        f"poly y4={resultant('r4')};",
    )
    q5_definitions = (
        "poly r5p0=a2m*k3+a0m*k0;",
        "poly r5p1=a2m*k4+a0m*k1;",
        "poly r5p2=a2m*k5+a0m*k2;",
        "poly r5q0=a2m*k3-a0m*s*k0;",
        "poly r5q1=-a2m*k4+a0m*s*k1;",
        "poly r5q2=a2m*k5-a0m*s*k2;",
        f"poly y5={resultant('r5')};",
    )
    q6_definitions = (
        "poly r6p0=a2m*k3+a0m*s*k0;",
        "poly r6p1=a2m*k4+a0m*s*k1;",
        "poly r6p2=a2m*k5+a0m*s*k2;",
        "poly r6q0=k3+e^2*s*k0;",
        "poly r6q1=-k4-e^2*s*k1;",
        "poly r6q2=k5+e^2*s*k2;",
        f"poly y6={resultant('r6')};",
    )
    q7_definition = "poly y7=lm*bm^2*e^2-(a0m+e^2*a2m)^2;"
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
ring R={PRIME},(e,s,t,r,c,b),(dp(2),dp(4));
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(kernel_definitions)}
{chr(10).join(common_definitions)}
{chr(10).join(q4_definitions)}
{chr(10).join(q5_definitions)}
{chr(10).join(q6_definitions)}
{q7_definition}
{chr(10).join(guard_definitions)}
{chr(10).join(extra_definitions)}
{chr(10).join(cofactor_definitions)}
ideal G={','.join(f'g{index}' for index in range(21))};
ideal I7=G,y7; G=slimgb(I7);
print("EQUATION=7,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal I5=G,y5; G=slimgb(I5);
print("EQUATION=5,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal I4=G,y4; G=slimgb(I4);
print("EQUATION=4,DIM="+string(dim(G))+",SIZE="+string(size(G)));
ideal I6=G,y6; G=slimgb(I6);
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
        "relation": "necessary FFF ratio-reduction superset",
        "variable_count": 6,
        "block_order": ["dp(2)", "dp(4)"],
        "common_basis_size": 21,
        "outside_equation_order": [7, 5, 4, 6],
        "route_guard_count": len(packet["route_guards"]),
        "extra_guards": list(EXTRA_GUARDS),
        "rank_cofactor_count": len(packet["rank_cofactors"]),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    verify_ratio_reduction()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_RATIO_REDUCTION_PROGRAM_PASS "
          "variables=6 equations=4 guards=20")
