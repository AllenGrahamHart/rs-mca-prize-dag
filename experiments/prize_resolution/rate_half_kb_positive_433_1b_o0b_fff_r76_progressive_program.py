#!/usr/bin/env python3
"""Build R76 coefficients by progressive quotient-ring reduction."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def declare_reduced_array(name, expressions, lines, family):
    names = []
    for index, expression in enumerate(expressions):
        raw = f"raw_{name}{index}"
        value = f"{name}{index}"
        lines.extend((
            f"poly {raw}={expression};",
            f"poly {value}=reduce({raw},G);",
            f'print("INTERMEDIATE={family},INDEX={index},DEG="'
            f'+string(deg({value}))+",SIZE="+string(size({value})));',
            f"kill {raw};",
        ))
        names.append(value)
    return names


def kill_arrays(lines, *arrays):
    for values in arrays:
        for value in values:
            lines.append(f"kill {value};")


def build(packet_row, graph_payload, raw_core):
    raw_core.verify_r76_decomposition()
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
    lines = []
    for index, expression in enumerate(packet["kernel"]):
        lines.extend((
            f"poly raw_k{index}={expression};",
            f"poly k{index}=reduce(raw_k{index},G);",
            f'print("INTERMEDIATE=K,INDEX={index},DEG="'
            f'+string(deg(k{index}))+",SIZE="+string(size(k{index})));',
            f"kill raw_k{index};",
        ))
    lines.extend((
        "poly raw_lm=-t^2;",
        "poly lm=reduce(raw_lm,G);",
        'print("INTERMEDIATE=COMMON,INDEX=0,DEG="+string(deg(lm))'
        '+",SIZE="+string(size(lm)));',
        "kill raw_lm;",
        "poly raw_a2m=k0+k1*lm+k2*lm^2;",
        "poly a2m=reduce(raw_a2m,G);",
        'print("INTERMEDIATE=COMMON,INDEX=1,DEG="+string(deg(a2m))'
        '+",SIZE="+string(size(a2m)));',
        "kill raw_a2m;",
        "poly raw_bm=k6+k7*lm;",
        "poly bm=reduce(raw_bm,G);",
        'print("INTERMEDIATE=COMMON,INDEX=2,DEG="+string(deg(bm))'
        '+",SIZE="+string(size(bm)));',
        "kill raw_bm;",
    ))

    p0 = declare_reduced_array("p0c", ["k3", "x*k0"], lines, "P0")
    p1 = declare_reduced_array("p1c", ["k4", "x*k1"], lines, "P1")
    p2 = declare_reduced_array("p2c", ["k5", "x*k2"], lines, "P2")
    q0e0, q0e1 = ["k3"], ["0", "k0"]
    q1e0, q1e1 = ["-k4"], ["0", "-k1"]
    q2e0, q2e1 = ["k5"], ["0", "k2"]

    a0 = declare_reduced_array(
        "a0c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(p2, q0e0)),
            (-1, raw_core.multiply_arrays(p0, q2e0))),
        lines, "A0")
    a1 = declare_reduced_array(
        "a1c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(p2, q0e1)),
            (-1, raw_core.multiply_arrays(p0, q2e1))),
        lines, "A1")
    b0 = declare_reduced_array(
        "b0c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(p2, q1e0)),
            (-1, raw_core.multiply_arrays(p1, q2e0))),
        lines, "B0")
    b1 = declare_reduced_array(
        "b1c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(p2, q1e1)),
            (-1, raw_core.multiply_arrays(p1, q2e1))),
        lines, "B1")
    c0 = declare_reduced_array(
        "c0c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(p1, q0e0)),
            (-1, raw_core.multiply_arrays(p0, q1e0))),
        lines, "C0")
    c1 = declare_reduced_array(
        "c1c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(p1, q0e1)),
            (-1, raw_core.multiply_arrays(p0, q1e1))),
        lines, "C1")

    d0 = declare_reduced_array(
        "d0c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(a0, a0)),
            (-1, raw_core.multiply_arrays(b0, c0))),
        lines, "D0")
    d1 = declare_reduced_array(
        "d1c", raw_core.add_arrays(
            (1, raw_core.scale_array("2", raw_core.multiply_arrays(a0, a1))),
            (-1, raw_core.multiply_arrays(b0, c1)),
            (-1, raw_core.multiply_arrays(b1, c0))),
        lines, "D1")
    d2 = declare_reduced_array(
        "d2c", raw_core.add_arrays(
            (1, raw_core.multiply_arrays(a1, a1)),
            (-1, raw_core.multiply_arrays(b1, c1))),
        lines, "D2")
    kill_arrays(lines, p0, p1, p2, a0, a1, b0, b1, c0, c1)

    u = declare_reduced_array(
        "u", ["-a2m^2*x^2", "lm*bm^2-2*a2m^2*x", "-a2m^2"],
        lines, "U")
    u0, u1, u2 = u
    m0 = declare_reduced_array(
        "m0c", raw_core.add_arrays(
            (1, raw_core.scale_array(u2, d0)),
            (-1, raw_core.scale_array(u0, d2))),
        lines, "M0")
    m1 = declare_reduced_array(
        "m1c", raw_core.add_arrays(
            (1, raw_core.scale_array(u2, d1)),
            (-1, raw_core.scale_array(u1, d2))),
        lines, "M1")
    m2 = declare_reduced_array(
        "m2c", raw_core.add_arrays(
            (1, raw_core.scale_array(u1, d0)),
            (-1, raw_core.scale_array(u0, d1))),
        lines, "M2")
    kill_arrays(lines, d0, d1, d2, u)

    r76_expressions = raw_core.add_arrays(
        (1, raw_core.multiply_arrays(m0, m0)),
        (-1, raw_core.multiply_arrays(m1, m2)))
    require(len(r76_expressions) == 9, "nine R76 coefficients")
    r76 = []
    for index, expression in enumerate(r76_expressions):
        raw = f"raw_y76c{index}"
        value = f"n76{index}"
        lines.extend((
            f"poly {raw}={expression};",
            f"poly {value}=reduce({raw},G);",
            f'print("COEFFICIENT={index},DEG="+string(deg({value}))'
            f'+",SIZE="+string(size({value})));',
            f'print("C{index}_BEGIN"); print({value}); print("C{index}_END");',
            f"kill {raw};",
        ))
        r76.append(value)
    kill_arrays(lines, m0, m1, m2)

    program = f"""
ring R={PRIME},(x,t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
ideal G={','.join(f'g{index}' for index in range(48))};
attrib(G,"isSB",1);
{chr(10).join(lines)}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "exact progressive R76 coefficients on admissible FFF base graph",
        "source_relation": "exact R76 coefficients on admissible FFF base graph",
        "resultant_variable": "E",
        "variable_count": 5,
        "variables": ["x", "t", "r", "c", "b"],
        "coefficient_order": list(range(9)),
        "maximum_s_degree": 8,
        "progressive_quotient_reduction": True,
        "intermediate_reduction_count": 61,
        "total_reduction_count": 70,
        "graph_basis_size": 48,
        "graph_basis_sha256": graph["basis_sha256"],
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    require(declare_reduced_array and kill_arrays, "progressive helpers")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_PROGRESSIVE_PROGRAM_PASS "
          "coefficients=9 quotient_layers=1")
