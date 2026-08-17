#!/usr/bin/env python3
"""Build the four-variable common ideal after the O0b z2=z5 collapse."""


PRIME = 2130706433
COLLAPSED_KERNEL_INDICES = (2, 5)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(packet_row, basis_row):
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(basis_row["status"] == "COMPLETE", "basis status")
    require(packet_row["epsilon"] == [-1, -1], "packet signs")
    require(basis_row["epsilon"] == [-1, -1], "basis signs")
    require(packet_row["packet"]["variables"] == ["t", "r", "c", "b"],
            "base variables")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    collapse_definitions = tuple(
        f"poly k{index}={packet_row['packet']['kernel'][index]};"
        for index in COLLAPSED_KERNEL_INDICES
    )
    generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        *(f"k{index}" for index in COLLAPSED_KERNEL_INDICES),
    )
    program = f"""
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(collapse_definitions)}
ideal I={','.join(generators)};
ideal G=slimgb(I);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BASIS_BEGIN"); G; print("BASIS_END"); }}
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "necessary collapsed common superset",
        "variable_count": 4,
        "common_basis_size": len(basis_row["basis"]),
        "collapsed_kernel_indices": list(COLLAPSED_KERNEL_INDICES),
        "collapse_equation_count": len(COLLAPSED_KERNEL_INDICES),
        "generator_count": len(generators),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
    }


if __name__ == "__main__":
    require(COLLAPSED_KERNEL_INDICES == (2, 5), "collapse ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_BASIS_PROGRAM_PASS "
          "variables=4 generators=23")
