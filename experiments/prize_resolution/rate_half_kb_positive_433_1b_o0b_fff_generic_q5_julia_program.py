#!/usr/bin/env python3
"""Build the incremental generic-t q5 extension for the FFF chart."""

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
    require(packet_row["status"] == "COMPLETE" and
            len(packet["kernel"]) == 8, "packet")
    require(generic_payload["collection_complete"] is True and
            generic["status"] == "COMPLETE" and
            generic["dimension"] == 0 and generic["basis_size"] == 10 and
            generic["quotient_dimension"] == 8 and
            len(generic["basis"]) == 10, "generic basis")
    basis_literal = ",\n".join(generic["basis"])
    kernel_definitions = "\n".join(
        f"k{index}={kernel_to_julia(value)}"
        for index, value in enumerate(packet["kernel"])
    )
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(s,x,r,c,b)=polynomial_ring(K,["s","x","r","c","b"],
                              internal_ordering=:degrevlex)
base=[{basis_literal}]
@assert isgroebner(base; ordering=DegRevLex())
{kernel_definitions}
function resultant(p0,p1,p2,q0,q1,q2)
  return (p2*q0-p0*q2)^2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
end
q5=resultant(k3+x*k0,k4+x*k1,k5+x*k2,
             k3-x*s*k0,-k4+x*s*k1,k5-x*s*k2)
q5normal=only(normalform(base,[q5]; ordering=DegRevLex()))
println("Q5_NORMAL ",total_degree(q5normal)," ",length(q5normal))
system=vcat(base,[q5normal])
basis=groebner(system; ordering=DegRevLex(), linalg=:deterministic, tasks=1)
@assert isgroebner(basis; ordering=DegRevLex())
unit=length(basis)==1 && isone(basis[1])
dimension=unit ? -1 : Groebner.dimension(basis)
quotientDimension=dimension==0 ? length(
    Groebner.quotient_basis(basis; ordering=DegRevLex())) : 0
println("Q5_COMPLETE ",unit ? 1 : 0," ",dimension," ",length(basis),
        " ",quotientDimension)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_q5_normal.txt","w") do io
  println(io,string(q5normal))
end
open("/tmp/fff_generic_q5_basis.txt","w") do io
  for value in basis
    println(io,string(value))
  end
end
open("/tmp/fff_generic_q5_coefficients.txt","w") do io
  for (kind,values) in [("normal",[q5normal]),("basis",basis)]
    for (valueIndex,value) in enumerate(values)
      for termIndex in 1:length(value)
        scalar=coeff(value,termIndex)
        println(io,kind,"\t",valueIndex,"\t",termIndex,"\t",
                coefficient_list(numerator(scalar)),"\t",
                coefficient_list(denominator(scalar)))
      end
    end
  end
end
println("Q5_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF q5 extension",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "fiber_variables": ["s", "x", "r", "c", "b"],
        "source_basis_size": 10,
        "source_basis_sha256": generic["basis_sha256"],
        "source_quotient_dimension": 8,
        "equation": "q5",
        "transformation_denominators_open": True,
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    require(kernel_to_julia("x^2*t*r^3 - 2*x*c*b + 7") ==
            "x^2*t*r^3-2*x*c*b+7", "converter self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q5_JULIA_PROGRAM_PASS "
          "basis=10 equation=q5 variables=5")
