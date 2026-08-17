#!/usr/bin/env python3
"""Build the four-variable necessary superset for the surviving O0b IFF branch."""

PRIME = 2130706433
EXTRA_GUARDS = ("k2", "k5", "a2m")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def resultant(prefix):
    return (
        f"({prefix}p2*{prefix}q0-{prefix}p0*{prefix}q2)^2"
        f"-({prefix}p2*{prefix}q1-{prefix}p1*{prefix}q2)"
        f"*({prefix}p1*{prefix}q0-{prefix}p0*{prefix}q1)"
    )


def verify_rational_reduction():
    import sympy as sp

    b, c, d, e, f = sp.symbols("b c d e f")
    k2, k5, a2m, a0m, lm, bm = sp.symbols(
        "k2 k5 a2m a0m lm bm"
    )
    substitutions = {
        e: k5 / (b * k2),
        f: k5 / (c * k2),
        d: a0m * b * k2 / (k5 * a2m),
    }
    require(sp.cancel((k5-b*e*k2).subs(substitutions)) == 0,
            "q4 infinity equation")
    require(sp.cancel((b*e-c*f).subs(substitutions)) == 0,
            "record collision")
    require(sp.cancel((d*e*a2m-a0m).subs(substitutions)) == 0,
            "q3 anchor")
    records = {
        "q5_left": sp.cancel((-d*e).subs(substitutions)),
        "q5_right": sp.cancel((d*f).subs(substitutions)),
        "q6_left": sp.cancel((-d*f).subs(substitutions)),
        "q6_right": sp.cancel((-e*f).subs(substitutions)),
    }
    require(records == {
        "q5_left": -a0m/a2m,
        "q5_right": a0m*b/(a2m*c),
        "q6_left": -a0m*b/(a2m*c),
        "q6_right": -k5**2/(b*c*k2**2),
    }, "scaled record ledger")
    q7 = lm*bm**2-(d+e)**2*a2m**2
    denominator = b*k2*k5
    numerator = (
        lm*bm**2*denominator**2
        - (a0m*b**2*k2**2+k5**2*a2m)**2
    )
    require(sp.cancel(q7.subs(substitutions)*denominator**2-numerator) == 0,
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
    q5_definitions = (
        "poly r5p0=a2m*k3+a0m*k0;",
        "poly r5p1=a2m*k4+a0m*k1;",
        "poly r5p2=a2m*k5+a0m*k2;",
        "poly r5q0=c*a2m*k3-a0m*b*k0;",
        "poly r5q1=-c*a2m*k4+a0m*b*k1;",
        "poly r5q2=c*a2m*k5-a0m*b*k2;",
        f"poly y5={resultant('r5')};",
    )
    q6_definitions = (
        "poly r6p0=c*a2m*k3+a0m*b*k0;",
        "poly r6p1=c*a2m*k4+a0m*b*k1;",
        "poly r6p2=c*a2m*k5+a0m*b*k2;",
        "poly r6q0=b*c*k2^2*k3+k5^2*k0;",
        "poly r6q1=-b*c*k2^2*k4-k5^2*k1;",
        "poly r6q2=b*c*k2^2*k5+k5^2*k2;",
        f"poly y6={resultant('r6')};",
    )
    q7_definition = (
        "poly y7=lm*bm^2*(b*k2*k5)^2"
        "-(a0m*b^2*k2^2+k5^2*a2m)^2;"
    )
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
ring R={PRIME},(t,r,c,b),dp;
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
ideal G={','.join(f'g{index}' for index in range(21))};
G=slimgb(G,y7); print("EQUATION=7,DIM="+string(dim(G))+",SIZE="+string(size(G)));
G=slimgb(G,y5); print("EQUATION=5,DIM="+string(dim(G))+",SIZE="+string(size(G)));
G=slimgb(G,y6); print("EQUATION=6,DIM="+string(dim(G))+",SIZE="+string(size(G)));
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
        "relation": "necessary IFF rational-reduction superset",
        "variable_count": 4,
        "common_basis_size": 21,
        "outside_equation_order": [7, 5, 6],
        "route_guard_count": len(packet["route_guards"]),
        "extra_guards": list(EXTRA_GUARDS),
        "rank_cofactor_count": len(packet["rank_cofactors"]),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    verify_rational_reduction()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_IFF_RATIONAL_REDUCTION_PROGRAM_PASS "
          "variables=4 equations=3 guards=19")
