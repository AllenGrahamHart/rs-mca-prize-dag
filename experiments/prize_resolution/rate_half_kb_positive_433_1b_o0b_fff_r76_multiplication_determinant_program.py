#!/usr/bin/env python3
"""Build the direct R76 multiplication determinant in the q5 quotient."""

import hashlib


PRIME = 2130706433
EXPECTED_WITNESS = 244686406
BASE_MARKER = 'println("NORMAL_MATRICES_READY 6 3")'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(base_core, bank_payload, q7_payload):
    base = base_core.build(bank_payload, q7_payload)
    base_program = base.pop("program")
    require(base_program.count(BASE_MARKER) == 1, "base-program marker")
    prefix = base_program.split(BASE_MARKER, 1)[0]
    program = prefix + f"""
println("NORMAL_MATRICES_READY 6 3")
flush(stdout)
function r76_matrix(baseMatrices,kernelMatrices,dMatrices)
  MS=baseMatrices[1]
  MX=baseMatrices[2]
  p0=kernelMatrices[4]+MX*MS*kernelMatrices[1]
  p1=kernelMatrices[5]+MX*MS*kernelMatrices[2]
  p2=kernelMatrices[6]+MX*MS*kernelMatrices[3]
  q00=kernelMatrices[4]
  q01=MS*kernelMatrices[1]
  q10=-kernelMatrices[5]
  q11=-MS*kernelMatrices[2]
  q20=kernelMatrices[6]
  q21=MS*kernelMatrices[3]
  a0=p2*q00-p0*q20
  a1=p2*q01-p0*q21
  b0=p2*q10-p1*q20
  b1=p2*q11-p1*q21
  c0=p1*q00-p0*q10
  c1=p1*q01-p0*q11
  y0=a0^2-b0*c0
  y1=2*a0*a1-b0*c1-b1*c0
  y2=a1^2-b1*c1
  d0=dMatrices[1]
  d1=dMatrices[2]
  d2=dMatrices[3]
  m0=d2*y0-d0*y2
  m1=d2*y1-d1*y2
  m2=d1*y0-d0*y1
  return m0^2-m1*m2
end
function specialize_scalar(value,candidate)
  point=F(candidate)
  denominatorValue=evaluate(denominator(value),point)
  @assert !iszero(denominatorValue)
  return evaluate(numerator(value),point)*inv(denominatorValue)
end
function specialize_matrix(value,candidate)
  output=zero_matrix(F,nrows(value),ncols(value))
  for row in 1:nrows(value), column in 1:ncols(value)
    output[row,column]=specialize_scalar(value[row,column],candidate)
  end
  return output
end
witnessT=2
witnessBase=[specialize_matrix(value,witnessT) for value in matrices]
witnessK=[specialize_matrix(value,witnessT) for value in MK]
witnessD=[specialize_matrix(value,witnessT) for value in MD]
witnessR76=r76_matrix(witnessBase,witnessK,witnessD)
witnessDet=det(witnessR76)
@assert witnessDet==F({EXPECTED_WITNESS})
println("WITNESS_COMPLETE ",witnessT," ",witnessDet," ",
        count(!iszero,witnessR76))
println("WITNESS_CERTIFIED")
flush(stdout)
symbolicR76=r76_matrix(matrices,MK,MD)
println("SYMBOLIC_R76_MATRIX ",count(!iszero,symbolicR76))
flush(stdout)
symbolicDet=det(symbolicR76)
@assert !iszero(symbolicDet)
println("SYMBOLIC_R76_COMPLETE ",degree(numerator(symbolicDet))," ",
        degree(denominator(symbolicDet))," ",length(numerator(symbolicDet)),
        " ",length(denominator(symbolicDet)))
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_r76_multiplication_determinant.txt","w") do io
  println(io,"R76_NUM\t",coefficient_list(numerator(symbolicDet)))
  println(io,"R76_DEN\t",coefficient_list(denominator(symbolicDet)))
end
println("R76_MULTIPLICATION_DETERMINANT_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF R76 multiplication determinant",
        "engine": "AbstractAlgebra.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "quotient_dimension": 16,
        "matrix_relation": "R76=Res_E(q7,q6)",
        "source_base_generated_program_sha256":
            hashlib.sha256(base_program.encode()).hexdigest(),
        "source_quotient_basis_sha256": base["source_quotient_basis_sha256"],
        "source_matrix_entries_sha256": base["source_matrix_entries_sha256"],
        "source_kernel_normals_sha256": base["source_kernel_normals_sha256"],
        "source_q7_values_sha256": base["source_q7_values_sha256"],
        "witness_t": 2,
        "expected_witness_determinant": EXPECTED_WITNESS,
        "transformation_denominators_open": True,
        "symbolic_determinant_roots_open_until_complete": True,
    }


if __name__ == "__main__":
    require(pow(1573108971, 2, PRIME) * 443644136 % PRIME ==
            EXPECTED_WITNESS, "norm-resultant witness identity")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_MULTIPLICATION_"
          "DETERMINANT_PROGRAM_PASS dimension=16 witness=244686406")
