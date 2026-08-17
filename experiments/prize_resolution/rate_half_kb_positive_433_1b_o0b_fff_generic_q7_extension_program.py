#!/usr/bin/env python3
"""Build the generic q7 extension over the certified q5 quotient."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(q5_payload, q7_payload):
    q5 = q5_payload["row"]
    q7 = q7_payload["row"]
    require(q5_payload["collection_complete"] is True and
            q5["status"] == "COMPLETE" and q5["unit"] is False and
            q5["dimension"] == 0 and q5["basis_size"] == 16 and
            q5["quotient_dimension"] == 16, "q5 quotient")
    require(q7_payload["collection_complete"] is True and
            q7["status"] == "COMPLETE" and
            [value["label"] for value in q7["values"]] ==
            ["a2m", "bm", "a2m_square", "bm_square", "D0", "D1", "D2"],
            "q7 coefficients")
    coefficients = [q7["values"][index]["polynomial"] for index in (4, 5, 6)]
    coefficient_hashes = [q7["values"][index]["polynomial_sha256"]
                          for index in (4, 5, 6)]
    basis_literal = ",\n".join(q5["basis"])
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(E,s,x,r,c,b)=polynomial_ring(K,["E","s","x","r","c","b"],
                                internal_ordering=:degrevlex)
base=[{basis_literal}]
@assert isgroebner(base; ordering=DegRevLex())
d0={coefficients[0]}
d1={coefficients[1]}
d2={coefficients[2]}
q7=d0+d1*E+d2*E^2
println("Q7_INPUT ",length(q7))
system=vcat(base,[q7])
basis=groebner(system; ordering=DegRevLex(), linalg=:deterministic, tasks=1)
@assert isgroebner(basis; ordering=DegRevLex())
unit=length(basis)==1 && isone(basis[1])
dimension=unit ? -1 : Groebner.dimension(basis)
quotientDimension=dimension==0 ? length(
    Groebner.quotient_basis(basis; ordering=DegRevLex())) : 0
println("Q7_COMPLETE ",unit ? 1 : 0," ",dimension," ",length(basis),
        " ",quotientDimension)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_q7_basis.txt","w") do io
  for value in basis
    println(io,string(value))
  end
end
open("/tmp/fff_generic_q7_entries.txt","w") do io
  for (basisIndex,value) in enumerate(basis)
    for termIndex in 1:length(value)
      scalar=coeff(value,termIndex)
      println(io,basisIndex,"\t",termIndex,"\t",
              coefficient_list(numerator(scalar)),"\t",
              coefficient_list(denominator(scalar)))
    end
  end
end
println("Q7_EXTENSION_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF q5-q7 extension",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "fiber_variables": ["E", "s", "x", "r", "c", "b"],
        "source_basis_size": 16,
        "source_basis_sha256": q5["basis_sha256"],
        "source_quotient_dimension": 16,
        "coefficient_hashes": coefficient_hashes,
        "equations": ["q5", "q7"],
        "transformation_denominators_open": True,
    }


if __name__ == "__main__":
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q7_EXTENSION_PROGRAM_PASS "
          "source_dimension=16 equation=q7")
