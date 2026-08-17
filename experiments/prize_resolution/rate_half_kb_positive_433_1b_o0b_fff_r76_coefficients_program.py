#!/usr/bin/env python3
"""Build coefficient-wise Res_E(q7,q6) reductions for the FFF chart."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add_arrays(*signed_arrays):
    length = max(len(values) for _, values in signed_arrays)
    output = []
    for index in range(length):
        terms = []
        for sign, values in signed_arrays:
            if index >= len(values) or values[index] == "0":
                continue
            value = values[index]
            terms.append(f"+({value})" if sign == 1 else f"-({value})")
        output.append("".join(terms).lstrip("+") or "0")
    return output


def multiply_arrays(left, right):
    output = ["0"] * (len(left) + len(right) - 1)
    buckets = [[] for _ in output]
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            if first != "0" and second != "0":
                buckets[i+j].append(f"({first})*({second})")
    return ["+".join(bucket) if bucket else "0" for bucket in buckets]


def scale_array(value, values):
    return ["0" if item == "0" else f"({value})*({item})" for item in values]


def declare_array(name, expressions, definitions):
    names = []
    for index, expression in enumerate(expressions):
        item = f"{name}{index}"
        definitions.append(f"poly {item}={expression};")
        names.append(item)
    return names


def verify_r76_decomposition():
    import sympy as sp

    E, s, x, a2m, lm, bm = sp.symbols("E s x a2m lm bm")
    k = sp.symbols("k0:6")
    p = [k[3]+x*s*k[0], k[4]+x*s*k[1], k[5]+x*s*k[2]]
    q = [k[3]+E*s*k[0], -k[4]-E*s*k[1], k[5]+E*s*k[2]]

    def quadratic_resultant(first, second):
        p0, p1, p2 = [sp.expand(first).coeff(E, index) for index in range(3)]
        q0, q1, q2 = [sp.expand(second).coeff(E, index) for index in range(3)]
        return sp.expand(
            (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
        )

    y6 = sp.expand(
        (p[2]*q[0]-p[0]*q[2])**2
        - (p[2]*q[1]-p[1]*q[2])*(p[1]*q[0]-p[0]*q[1])
    )
    y7 = lm*bm**2*E-a2m**2*(x+E)**2
    r76 = quadratic_resultant(y7, y6)
    coefficients = [sp.expand(r76).coeff(s, index) for index in range(9)]
    require(sp.Poly(r76, s).degree() <= 8 and
            sp.expand(r76-sum(value*s**index
                              for index, value in enumerate(coefficients))) == 0,
            "R76 coefficient identity")
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
    definitions = [
        "poly lm=-t^2;",
        "poly a2m=k0+k1*lm+k2*lm^2;",
        "poly bm=k6+k7*lm;",
        "poly p00=k3;", "poly p01=x*k0;",
        "poly p10=k4;", "poly p11=x*k1;",
        "poly p20=k5;", "poly p21=x*k2;",
    ]
    p0, p1, p2 = ["p00", "p01"], ["p10", "p11"], ["p20", "p21"]
    q0e0, q0e1 = ["k3"], ["0", "k0"]
    q1e0, q1e1 = ["-k4"], ["0", "-k1"]
    q2e0, q2e1 = ["k5"], ["0", "k2"]

    a0 = declare_array(
        "a0c", add_arrays(
            (1, multiply_arrays(p2, q0e0)),
            (-1, multiply_arrays(p0, q2e0))),
        definitions)
    a1 = declare_array(
        "a1c", add_arrays(
            (1, multiply_arrays(p2, q0e1)),
            (-1, multiply_arrays(p0, q2e1))),
        definitions)
    b0 = declare_array(
        "b0c", add_arrays(
            (1, multiply_arrays(p2, q1e0)),
            (-1, multiply_arrays(p1, q2e0))),
        definitions)
    b1 = declare_array(
        "b1c", add_arrays(
            (1, multiply_arrays(p2, q1e1)),
            (-1, multiply_arrays(p1, q2e1))),
        definitions)
    c0 = declare_array(
        "c0c", add_arrays(
            (1, multiply_arrays(p1, q0e0)),
            (-1, multiply_arrays(p0, q1e0))),
        definitions)
    c1 = declare_array(
        "c1c", add_arrays(
            (1, multiply_arrays(p1, q0e1)),
            (-1, multiply_arrays(p0, q1e1))),
        definitions)

    d0 = declare_array(
        "d0c", add_arrays(
            (1, multiply_arrays(a0, a0)),
            (-1, multiply_arrays(b0, c0))),
        definitions)
    d1 = declare_array(
        "d1c", add_arrays(
            (1, scale_array("2", multiply_arrays(a0, a1))),
            (-1, multiply_arrays(b0, c1)),
            (-1, multiply_arrays(b1, c0))),
        definitions)
    d2 = declare_array(
        "d2c", add_arrays(
            (1, multiply_arrays(a1, a1)),
            (-1, multiply_arrays(b1, c1))),
        definitions)

    definitions.extend((
        "poly u0=-a2m^2*x^2;",
        "poly u1=lm*bm^2-2*a2m^2*x;",
        "poly u2=-a2m^2;",
    ))
    m0 = declare_array(
        "m0c", add_arrays(
            (1, scale_array("u2", d0)),
            (-1, scale_array("u0", d2))),
        definitions)
    m1 = declare_array(
        "m1c", add_arrays(
            (1, scale_array("u2", d1)),
            (-1, scale_array("u1", d2))),
        definitions)
    m2 = declare_array(
        "m2c", add_arrays(
            (1, scale_array("u1", d0)),
            (-1, scale_array("u0", d1))),
        definitions)
    r76 = declare_array(
        "y76c", add_arrays(
            (1, multiply_arrays(m0, m0)),
            (-1, multiply_arrays(m1, m2))),
        definitions)
    require(len(r76) == 9, "nine R76 coefficients")

    reduction_stages = "\n".join(
        (
            f"poly n76{index}=reduce(y76c{index},G); "
            f'print("COEFFICIENT={index},DEG="+string(deg(n76{index}))'
            f'+",SIZE="+string(size(n76{index}))); '
            f'print("C{index}_BEGIN"); print(n76{index}); print("C{index}_END");'
        )
        for index in range(9)
    )
    program = f"""
ring R={PRIME},(x,t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(kernel_definitions)}
{chr(10).join(definitions)}
ideal G={','.join(f'g{index}' for index in range(48))};
{reduction_stages}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "exact R76 coefficients on admissible FFF base graph",
        "resultant_variable": "E",
        "variable_count": 5,
        "variables": ["x", "t", "r", "c", "b"],
        "coefficient_order": list(range(9)),
        "maximum_s_degree": 8,
        "q7_E_degree": 2,
        "q6_E_degree": 2,
        "graph_basis_size": 48,
        "graph_basis_sha256": graph["basis_sha256"],
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    verify_r76_decomposition()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_COEFFICIENTS_PROGRAM_PASS "
          "coefficients=9 max_s_degree=8")
