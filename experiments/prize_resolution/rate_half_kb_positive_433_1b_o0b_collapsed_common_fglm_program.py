#!/usr/bin/env python3
"""Build an FGLM audit of the zero-dimensional O0b collapsed common basis."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(source):
    require(source["collection_complete"] is True, "source completion")
    row = source["row"]
    require(row["status"] == "COMPLETE" and row["unit"] is False,
            "nonunit source basis")
    require(row["dimension"] == 0 and row["basis_size"] == 43 and
            len(row["basis"]) == 43, "zero-dimensional source ledger")
    definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(row["basis"])
    )
    program = f"""
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{chr(10).join(definitions)}
ideal G={','.join(f'g{index}' for index in range(len(definitions)))};
print("DP_BEGIN"); print("DP_DIM="+string(dim(G)));
print("DP_SIZE="+string(size(G))); print("DP_VDIM="+string(vdim(G)));
print("DP_END");
ring L={PRIME},(t,r,c,b),lp;
option(redSB);
ideal H=fglm(R,G);
print("LEX_BEGIN"); print("LEX_DIM="+string(dim(H)));
print("LEX_SIZE="+string(size(H))); print("LEX_VDIM="+string(vdim(H)));
print("LEX_BASIS_BEGIN"); H; print("LEX_BASIS_END");
print("LEX_END"); quit;
"""
    return {
        "program": program,
        "relation": "exact basis-order conversion",
        "variable_count": 4,
        "source_dimension": row["dimension"],
        "source_basis_size": row["basis_size"],
    }


if __name__ == "__main__":
    require(PRIME < 2**31 and PRIME % 2 == 1, "field")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_FGLM_PROGRAM_PASS "
          "variables=4 source_basis=43")
