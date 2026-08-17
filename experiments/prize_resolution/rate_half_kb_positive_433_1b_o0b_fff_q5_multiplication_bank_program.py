#!/usr/bin/env python3
"""Build the q5 quotient multiplication-matrix and kernel-element bank."""

import re


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def kernel_to_julia(polynomial):
    polynomial = "".join(polynomial.split())
    require(re.fullmatch(r"[0-9xtrcb+*^-]+", polynomial) is not None,
            "kernel syntax")
    return polynomial


def build(cache_payload, generic_payload, q5_payload):
    packet_row = next(
        row for row in cache_payload["rows"] if row["epsilon"] == [-1, -1]
    )
    packet = packet_row["packet"]
    generic = generic_payload["row"]
    q5 = q5_payload["row"]
    require(packet_row["status"] == "COMPLETE" and len(packet["kernel"]) == 8,
            "packet")
    require(generic["status"] == "COMPLETE" and generic["basis_size"] == 10,
            "generic")
    require(q5_payload["collection_complete"] is True and
            q5["status"] == "COMPLETE" and q5["unit"] is False and
            q5["dimension"] == 0 and q5["basis_size"] == 16 and
            q5["quotient_dimension"] == 16 and
            q5["basis"][:10] == generic["basis"], "q5 quotient")
    basis_literal = ",\n".join(q5["basis"])
    kernels = "\n".join(
        f"k{index}={kernel_to_julia(value)}"
        for index, value in enumerate(packet["kernel"][:6])
    )
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(s,x,r,c,b)=polynomial_ring(K,["s","x","r","c","b"],
                              internal_ordering=:degrevlex)
basis=[{basis_literal}]
@assert isgroebner(basis; ordering=DegRevLex())
base=basis[1:10]
@assert isgroebner(base; ordering=DegRevLex())
{kernels}
kernelNormals=normalform(base,[k0,k1,k2,k3,k4,k5]; ordering=DegRevLex())
quotientBasis=Groebner.quotient_basis(basis; ordering=DegRevLex())
@assert length(quotientBasis)==16
basisIndex=Dict{{Tuple{{Vararg{{Int}}}},Int}}()
for (index,value) in enumerate(quotientBasis)
  basisIndex[Tuple(exponent_vector(value,1))]=index
end
variables=[s,x,r,c,b]
labels=["s","x","r","c","b"]
products=normalform(basis,[variable*value for variable in variables
                          for value in quotientBasis]; ordering=DegRevLex())
matrices=[zero_matrix(K,16,16) for _ in variables]
for variableIndex in 1:length(variables)
  for column in 1:16
    value=products[(variableIndex-1)*16+column]
    for termIndex in 1:length(value)
      row=basisIndex[Tuple(exponent_vector(value,termIndex))]
      matrices[variableIndex][row,column]=coeff(value,termIndex)
    end
  end
end
for left in 1:length(matrices), right in left:length(matrices)
  @assert matrices[left]*matrices[right]==matrices[right]*matrices[left]
end
println("MATRIX_PROFILE ",length(quotientBasis)," ",length(matrices)," ",
        sum(count(!iszero, matrix) for matrix in matrices))
for index in 1:length(kernelNormals)
  println("KERNEL_NORMAL ",index-1," ",total_degree(kernelNormals[index])," ",
          length(kernelNormals[index]))
end
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_q5_quotient_basis.txt","w") do io
  for value in quotientBasis
    println(io,string(value))
  end
end
open("/tmp/fff_q5_matrices.txt","w") do io
  for (matrixIndex,matrix) in enumerate(matrices)
    for row in 1:16, column in 1:16
      scalar=matrix[row,column]
      if !iszero(scalar)
        println(io,labels[matrixIndex],"\t",row,"\t",column,"\t",
                coefficient_list(numerator(scalar)),"\t",
                coefficient_list(denominator(scalar)))
      end
    end
  end
end
open("/tmp/fff_q5_kernel_normals.txt","w") do io
  for (index,value) in enumerate(kernelNormals)
    println(io,"k",index-1,"\t",string(value))
  end
end
open("/tmp/fff_q5_kernel_entries.txt","w") do io
  for (valueIndex,value) in enumerate(kernelNormals)
    for termIndex in 1:length(value)
      scalar=coeff(value,termIndex)
      println(io,"k",valueIndex-1,"\t",termIndex,"\t",
              coefficient_list(numerator(scalar)),"\t",
              coefficient_list(denominator(scalar)))
    end
  end
end
println("MULTIPLICATION_BANK_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic q5 quotient multiplication bank",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "quotient_variables": ["s", "x", "r", "c", "b"],
        "matrix_labels": ["s", "x", "r", "c", "b"],
        "kernel_labels": [f"k{index}" for index in range(6)],
        "source_basis_size": 16,
        "source_basis_sha256": q5["basis_sha256"],
        "source_quotient_dimension": 16,
        "packet_sha256": packet_row["packet_sha256"],
        "commutation_required": True,
        "transformation_denominators_open": True,
    }


if __name__ == "__main__":
    require(kernel_to_julia("x^2*t*r^3 - 2*x*c*b + 7") ==
            "x^2*t*r^3-2*x*c*b+7", "converter self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_Q5_MULTIPLICATION_BANK_PROGRAM_PASS "
          "dimension=16 matrices=5 kernels=6")
