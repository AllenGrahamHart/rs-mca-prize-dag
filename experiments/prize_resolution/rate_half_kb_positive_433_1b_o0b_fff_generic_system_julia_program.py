#!/usr/bin/env python3
"""Build the generic-t Julia system for the FFF necessary equations."""

import re


PRIME = 2130706433
VARIABLES = "xtrcb"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def singular_to_julia(polynomial):
    polynomial = "".join(polynomial.split())
    if "*" in polynomial or "^" in polynomial:
        require(re.fullmatch(r"[0-9xtrcb+*^-]+", polynomial) is not None,
                "expanded polynomial syntax")
        return polynomial
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
    kernels = [singular_to_julia(value) for value in packet["kernel"]]
    basis_literal = ",\n".join(generic["basis"])
    kernel_definitions = "\n".join(
        f"k{index}={value}" for index, value in enumerate(kernels)
    )
    program = f"""
using AbstractAlgebra, Groebner, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(E,s,x,r,c,b)=polynomial_ring(K,["E","s","x","r","c","b"],
                                internal_ordering=:degrevlex)
base=[{basis_literal}]
{kernel_definitions}
lm=-t^2
a2m=k0+k1*lm+k2*lm^2
bm=k6+k7*lm
function resultant(p0,p1,p2,q0,q1,q2)
  return (p2*q0-p0*q2)^2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
end
q5=resultant(k3+x*k0,k4+x*k1,k5+x*k2,
             k3-x*s*k0,-k4+x*s*k1,k5-x*s*k2)
q7=lm*bm^2*E-a2m^2*(x+E)^2
q6=resultant(k3+x*s*k0,k4+x*s*k1,k5+x*s*k2,
             k3+E*s*k0,-k4-E*s*k1,k5+E*s*k2)
system=vcat(base,[q5,q7,q6])
println("INPUT_COMPLETE ",length(base)," ",length(system))
basis=groebner(system; ordering=DegRevLex(), linalg=:deterministic, tasks=1)
@assert isgroebner(basis; ordering=DegRevLex())
unit=length(basis)==1 && isone(basis[1])
dimension=unit ? -1 : Groebner.dimension(basis)
quotientDimension=dimension==0 ? length(
    Groebner.quotient_basis(basis; ordering=DegRevLex())) : 0
println("SYSTEM_COMPLETE ",unit ? 1 : 0," ",dimension," ",length(basis),
        " ",quotientDimension)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_generic_system_basis.txt","w") do io
  for value in basis
    println(io,string(value))
  end
end
open("/tmp/fff_generic_system_coefficients.txt","w") do io
  for (basisIndex,value) in enumerate(basis)
    for termIndex in 1:length(value)
      scalar=coeff(value,termIndex)
      println(io,basisIndex,"\t",termIndex,"\t",
              coefficient_list(numerator(scalar)),"\t",
              coefficient_list(denominator(scalar)))
    end
  end
end
println("SYSTEM_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF q5-q7-q6 necessary subsystem",
        "engine": "AbstractAlgebra+Groebner.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "fiber_variables": ["E", "s", "x", "r", "c", "b"],
        "source_basis_size": 10,
        "source_basis_sha256": generic["basis_sha256"],
        "source_quotient_dimension": 8,
        "equation_order": ["q5", "q7", "q6"],
        "omitted_finite_pair": "q4",
        "transformation_denominators_open": True,
        "basis_denominator_roots_open": True,
        "packet_sha256": packet_row["packet_sha256"],
    }


if __name__ == "__main__":
    require(singular_to_julia("x^2*t*r^3 - 2*x*c*b + 7") ==
            "x^2*t*r^3-2*x*c*b+7", "converter self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_SYSTEM_JULIA_PROGRAM_PASS "
          "basis=10 equations=3 variables=6")
