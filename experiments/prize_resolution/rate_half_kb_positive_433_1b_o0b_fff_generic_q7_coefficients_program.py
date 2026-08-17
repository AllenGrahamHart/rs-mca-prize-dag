#!/usr/bin/env python3
"""Build staged generic q7 coefficients in the dimension-eight base."""

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


def build(cache_payload, generic_payload):
    packet_row = next(
        row for row in cache_payload["rows"] if row["epsilon"] == [-1, -1]
    )
    packet = packet_row["packet"]
    generic = generic_payload["row"]
    require(packet_row["status"] == "COMPLETE" and len(packet["kernel"]) == 8,
            "packet")
    require(generic_payload["collection_complete"] is True and
            generic["status"] == "COMPLETE" and generic["basis_size"] == 10 and
            generic["quotient_dimension"] == 8, "generic basis")
    basis_literal = ",\n".join(generic["basis"])
    kernels = "\n".join(
        f"k{index}={kernel_to_julia(value)}"
        for index, value in enumerate(packet["kernel"])
    )
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(x,r,c,b)=polynomial_ring(K,["x","r","c","b"],
                            internal_ordering=:degrevlex)
basis=[{basis_literal}]
@assert isgroebner(basis; ordering=DegRevLex())
{kernels}
lm=-t^2
rawA2=k0+k1*lm+k2*lm^2
rawB=k6+k7*lm
elements=normalform(basis,[rawA2,rawB]; ordering=DegRevLex())
a2=elements[1]
bm=elements[2]
squares=normalform(basis,[a2^2,bm^2]; ordering=DegRevLex())
a2sq=squares[1]
bmsq=squares[2]
coefficients=normalform(basis,[-a2sq*x^2,lm*bmsq-2*a2sq*x,-a2sq];
                        ordering=DegRevLex())
values=vcat(elements,squares,coefficients)
labels=["a2m","bm","a2m_square","bm_square","D0","D1","D2"]
for index in 1:length(values)
  println("Q7_VALUE ",labels[index]," ",total_degree(values[index])," ",
          length(values[index]))
end
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_q7_values.txt","w") do io
  for (index,value) in enumerate(values)
    println(io,labels[index],"\t",string(value))
  end
end
open("/tmp/fff_generic_q7_entries.txt","w") do io
  for (valueIndex,value) in enumerate(values)
    for termIndex in 1:length(value)
      scalar=coeff(value,termIndex)
      println(io,labels[valueIndex],"\t",termIndex,"\t",
              coefficient_list(numerator(scalar)),"\t",
              coefficient_list(denominator(scalar)))
    end
  end
end
println("Q7_COEFFICIENTS_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic staged FFF q7 coefficient bank",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "fiber_variables": ["x", "r", "c", "b"],
        "source_basis_sha256": generic["basis_sha256"],
        "source_quotient_dimension": 8,
        "value_labels": ["a2m", "bm", "a2m_square", "bm_square", "D0", "D1", "D2"],
        "q7_coefficient_labels": ["D0", "D1", "D2"],
        "packet_sha256": packet_row["packet_sha256"],
        "transformation_denominators_open": True,
    }


if __name__ == "__main__":
    require(kernel_to_julia("x^2*t*r^3 - 2*x*c*b + 7") ==
            "x^2*t*r^3-2*x*c*b+7", "converter self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q7_COEFFICIENTS_PROGRAM_PASS "
          "values=7 coefficients=3")
