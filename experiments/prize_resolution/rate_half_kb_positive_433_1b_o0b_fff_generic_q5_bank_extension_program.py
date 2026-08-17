#!/usr/bin/env python3
"""Build the generic q5 extension from the completed coefficient bank."""


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(generic_payload, frontier_payload, c1_payload):
    generic = generic_payload["row"]
    frontier = frontier_payload["rows"]
    c1 = c1_payload["row"]
    require(generic_payload["collection_complete"] is True and
            generic["status"] == "COMPLETE" and generic["basis_size"] == 10 and
            generic["quotient_dimension"] == 8, "generic basis")
    require(frontier_payload["collection_complete"] is True and
            [row["status"] for row in frontier] ==
            ["COMPLETE", "TIMEOUT", "COMPLETE"], "coefficient frontier")
    require(c1_payload["collection_complete"] is True and
            c1["status"] == "COMPLETE" and c1["coefficient_index"] == 1,
            "coefficient one")
    normals = [frontier[0]["normal"], c1["normal"], frontier[2]["normal"]]
    normal_hashes = [frontier[0]["normal_sha256"], c1["normal_sha256"],
                     frontier[2]["normal_sha256"]]
    require(all(normals) and all(row.count("//") > 0 for row in normals),
            "normal forms")
    basis_literal = ",\n".join(generic["basis"])
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(s,x,r,c,b)=polynomial_ring(K,["s","x","r","c","b"],
                              internal_ordering=:degrevlex)
base=[{basis_literal}]
@assert isgroebner(base; ordering=DegRevLex())
c0={normals[0]}
c1={normals[1]}
c2={normals[2]}
q5=c0+c1*s+c2*s^2
println("Q5_BANK_INPUT ",length(q5))
system=vcat(base,[q5])
basis=groebner(system; ordering=DegRevLex(), linalg=:deterministic, tasks=1)
@assert isgroebner(basis; ordering=DegRevLex())
unit=length(basis)==1 && isone(basis[1])
dimension=unit ? -1 : Groebner.dimension(basis)
quotientDimension=dimension==0 ? length(
    Groebner.quotient_basis(basis; ordering=DegRevLex())) : 0
println("Q5_BANK_COMPLETE ",unit ? 1 : 0," ",dimension," ",length(basis),
        " ",quotientDimension)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_q5_bank_basis.txt","w") do io
  for value in basis
    println(io,string(value))
  end
end
open("/tmp/fff_generic_q5_bank_coefficients.txt","w") do io
  for (basisIndex,value) in enumerate(basis)
    for termIndex in 1:length(value)
      scalar=coeff(value,termIndex)
      println(io,basisIndex,"\t",termIndex,"\t",
              coefficient_list(numerator(scalar)),"\t",
              coefficient_list(denominator(scalar)))
    end
  end
end
println("Q5_BANK_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF q5 coefficient-bank extension",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "fiber_variables": ["s", "x", "r", "c", "b"],
        "source_basis_size": 10,
        "source_basis_sha256": generic["basis_sha256"],
        "source_quotient_dimension": 8,
        "coefficient_normal_hashes": normal_hashes,
        "equation": "q5",
        "transformation_denominators_open": True,
    }


if __name__ == "__main__":
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q5_BANK_EXTENSION_PROGRAM_PASS "
          "coefficients=3 equation=q5")
