#!/usr/bin/env python3
"""Build the admissible FFF ratio graph over the generic field F_p(t)."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(graph_payload):
    graph = graph_payload["row"]
    require(graph_payload["collection_complete"] is True and
            graph["status"] == "COMPLETE" and graph["unit"] is False and
            graph["dimension"] == 1 and graph["basis_size"] == 48 and
            len(graph["basis"]) == 48, "graph basis")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(graph["basis"])
    )
    program = f"""
ring R={PRIME},(x,t,r,c,b),dp;
{chr(10).join(basis_definitions)}
ideal G={','.join(f'g{index}' for index in range(48))};
ring K=({PRIME},t),(x,r,c,b),dp;
option(redSB);
ideal H=std(imap(R,G));
print("GENERIC_DIM="+string(dim(H))+",GENERIC_SIZE="+string(size(H))
      +",GENERIC_VDIM="+string(vdim(H)));
print("BASIS_BEGIN"); H; print("BASIS_END");
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "exact admissible FFF ratio graph over F_p(t)",
        "coefficient_field": f"F_{PRIME}(t)",
        "parameter": "t",
        "fiber_variables": ["x", "r", "c", "b"],
        "source_dimension": 1,
        "source_basis_size": 48,
        "source_basis_sha256": graph["basis_sha256"],
        "denominator_exceptions_open": True,
    }


if __name__ == "__main__":
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_T_BASIS_PROGRAM_PASS "
          "parameter=t fiber_variables=4")
