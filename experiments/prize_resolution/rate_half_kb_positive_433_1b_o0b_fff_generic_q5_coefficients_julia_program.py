#!/usr/bin/env python3
"""Build one generic normal-form program for a banked q5 coefficient."""

import re


PRIME = 2130706433
VARIABLES = "xtrcb"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def singular_to_julia(polynomial):
    terms = re.findall(r"[+-]?[^+-]+", polynomial)
    require(terms and "".join(terms) == polynomial, "canonical term split")
    output = []
    for term in terms:
        sign = ""
        if term[0] in "+-":
            sign, term = term[0], term[1:]
        coefficient = re.match(r"\d+", term)
        coefficient_text = coefficient.group(0) if coefficient else ""
        monomial = term[len(coefficient_text):]
        factors = [coefficient_text] if coefficient_text else []
        position = 0
        while position < len(monomial):
            variable = monomial[position]
            require(variable in VARIABLES, f"unknown variable {variable}")
            position += 1
            start = position
            while position < len(monomial) and monomial[position].isdigit():
                position += 1
            exponent = monomial[start:position]
            factors.append(variable if not exponent else f"{variable}^{exponent}")
        require(factors, "empty term")
        output.append(("-" if sign == "-" else "+") + "*".join(factors))
    converted = "".join(output)
    return converted[1:] if converted.startswith("+") else converted


def build(coefficient_index, q5_payload, generic_payload):
    q5 = q5_payload["row"]
    generic = generic_payload["row"]
    require(q5_payload["collection_complete"] is True and
            q5["status"] == "COMPLETE" and q5["coefficient_order"] == [0, 1, 2]
            and len(q5["coefficients"]) == 3, "q5 bank")
    require(generic_payload["collection_complete"] is True and
            generic["status"] == "COMPLETE" and generic["basis_size"] == 10 and
            generic["quotient_dimension"] == 8, "generic basis")
    require(coefficient_index in range(3), "coefficient index")
    source = q5["coefficients"][coefficient_index]
    require(source["coefficient"] == coefficient_index, "coefficient order")
    polynomial = singular_to_julia(source["polynomial"])
    basis_literal = ",\n".join(generic["basis"])
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(x,r,c,b)=polynomial_ring(K,["x","r","c","b"],
                            internal_ordering=:degrevlex)
basis=[{basis_literal}]
@assert isgroebner(basis; ordering=DegRevLex())
source={polynomial}
normal=only(normalform(basis,[source]; ordering=DegRevLex()))
println("COEFFICIENT_COMPLETE {coefficient_index} ",total_degree(normal)," ",length(normal))
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_q5_coefficient.txt","w") do io
  println(io,string(normal))
end
open("/tmp/fff_generic_q5_coefficient_entries.txt","w") do io
  for termIndex in 1:length(normal)
    scalar=coeff(normal,termIndex)
    println(io,termIndex,"\t",coefficient_list(numerator(scalar)),"\t",
            coefficient_list(denominator(scalar)))
  end
end
println("COEFFICIENT_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic normal form of banked FFF q5 coefficient",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "fiber_variables": ["x", "r", "c", "b"],
        "coefficient_index": coefficient_index,
        "source_polynomial_sha256": source["polynomial_sha256"],
        "source_basis_sha256": generic["basis_sha256"],
        "source_quotient_dimension": 8,
        "transformation_denominators_open": True,
    }


if __name__ == "__main__":
    require(singular_to_julia("x2tr3-2xcb+7") == "x^2*t*r^3-2*x*c*b+7",
            "converter self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_Q5_COEFFICIENTS_PROGRAM_PASS "
          "coefficients=3 parallel=1")
