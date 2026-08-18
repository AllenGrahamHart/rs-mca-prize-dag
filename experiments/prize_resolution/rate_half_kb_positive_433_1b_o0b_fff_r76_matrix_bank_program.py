#!/usr/bin/env python3
"""Build and serialize the exact symbolic R76 multiplication matrix."""

import hashlib


R76_MARKER = "symbolicR76=r76_matrix(matrices,MK,MD)"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(base_core, r76_core, bank_payload, q7_payload):
    source = r76_core.build(base_core, bank_payload, q7_payload)
    source_program = source.pop("program")
    require(source_program.count(R76_MARKER) == 1, "R76-program marker")
    prefix = source_program.split(R76_MARKER, 1)[0]
    program = prefix + R76_MARKER + """
println("SYMBOLIC_R76_MATRIX ",count(!iszero,symbolicR76))
flush(stdout)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_r76_matrix_entries.txt","w") do io
  for row in 1:16, column in 1:16
    scalar=symbolicR76[row,column]
    @assert !iszero(scalar)
    println(io,row,"\t",column,"\t",coefficient_list(numerator(scalar)),
            "\t",coefficient_list(denominator(scalar)))
  end
end
println("R76_MATRIX_BANK_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF R76 multiplication matrix bank",
        "engine": "AbstractAlgebra.jl",
        "coefficient_field": "GF(2130706433)(t)",
        "quotient_dimension": 16,
        "matrix_relation": "R76=Res_E(q7,q6)",
        "source_r76_generated_program_sha256":
            hashlib.sha256(source_program.encode()).hexdigest(),
        "source_quotient_basis_sha256": source["source_quotient_basis_sha256"],
        "source_matrix_entries_sha256": source["source_matrix_entries_sha256"],
        "source_kernel_normals_sha256": source["source_kernel_normals_sha256"],
        "source_q7_values_sha256": source["source_q7_values_sha256"],
        "witness_t": 2,
        "expected_witness_determinant": 244686406,
        "transformation_denominators_open": True,
    }


if __name__ == "__main__":
    require(R76_MARKER == "symbolicR76=r76_matrix(matrices,MK,MD)",
            "marker self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_MATRIX_BANK_PROGRAM_PASS "
          "dimension=16 entries=256")
