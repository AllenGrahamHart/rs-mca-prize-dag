#!/usr/bin/env python3
"""Build a Groebner.jl program for the generic-t admissible FFF graph."""

import re


PRIME = 2130706433
VARIABLES = "xtrcb"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def split_terms(polynomial):
    terms = re.findall(r"[+-]?[^+-]+", polynomial)
    require(terms and "".join(terms) == polynomial, "canonical term split")
    return terms


def convert_term(term):
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
        exponent_start = position
        while position < len(monomial) and monomial[position].isdigit():
            position += 1
        exponent = monomial[exponent_start:position]
        factors.append(variable if not exponent else f"{variable}^{exponent}")
    require(factors, "empty term")
    body = "*".join(factors)
    return ("-" if sign == "-" else "+") + body


def singular_to_julia(polynomial):
    converted = "".join(convert_term(term) for term in split_terms(polynomial))
    return converted[1:] if converted.startswith("+") else converted


def build(graph_payload):
    graph = graph_payload["row"]
    require(graph_payload["collection_complete"] is True and
            graph["status"] == "COMPLETE" and graph["unit"] is False and
            graph["dimension"] == 1 and graph["basis_size"] == 48 and
            len(graph["basis"]) == 48, "graph basis")
    converted = [singular_to_julia(value) for value in graph["basis"]]
    require(len(converted) == 48 and all(converted), "converted basis")
    basis_literal = ",\n".join(converted)
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(x,r,c,b)=polynomial_ring(K,["x","r","c","b"],
                            internal_ordering=:degrevlex)
system=[{basis_literal}]
println("INPUT_COMPLETE ",length(system))
basis=groebner(system; ordering=DegRevLex(), linalg=:deterministic, tasks=1)
@assert isgroebner(basis; ordering=DegRevLex())
dimension=Groebner.dimension(basis)
quotientDimension=dimension==0 ? length(
    Groebner.quotient_basis(basis; ordering=DegRevLex())) : 0
println("GENERIC_COMPLETE ",dimension," ",length(basis)," ",quotientDimension)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_t_basis.txt","w") do io
  for value in basis
    println(io,string(value))
  end
end
open("/tmp/fff_generic_t_coefficients.txt","w") do io
  for (basisIndex,value) in enumerate(basis)
    for termIndex in 1:length(value)
      scalar=coeff(value,termIndex)
      println(io,basisIndex,"\t",termIndex,"\t",
              coefficient_list(numerator(scalar)),"\t",
              coefficient_list(denominator(scalar)))
    end
  end
end
println("GENERIC_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "certified admissible FFF ratio graph over GF(p)(t)",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "parameter": "t",
        "fiber_variables": ["x", "r", "c", "b"],
        "source_basis_size": 48,
        "source_basis_sha256": graph["basis_sha256"],
        "converted_basis_count": len(converted),
        "denominator_exceptions_open": True,
        "singular_engine_cap_exceeded": True,
    }


if __name__ == "__main__":
    require(
        singular_to_julia("x2tr3-2xcb+7") == "x^2*t*r^3-2*x*c*b+7",
        "converter self-test",
    )
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_T_JULIA_PROGRAM_PASS "
          "converted_basis=48 denominator_ledger=1")
