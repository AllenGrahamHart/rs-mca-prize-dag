#!/usr/bin/env python3
"""Build the q7 block algebra and the final q6 multiplication determinant."""

import re


PRIME = 2130706433
DIMENSION = 16
VARIABLE_LABELS = ["s", "x", "r", "c", "b"]
KERNEL_LABELS = [f"k{index}" for index in range(6)]
Q7_LABELS = ["D0", "D1", "D2"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def polynomial_literal(coefficients):
    require(coefficients and all(isinstance(value, int) for value in coefficients),
            "coefficient list")
    terms = []
    for exponent, coefficient in enumerate(coefficients):
        coefficient %= PRIME
        if coefficient == 0:
            continue
        if exponent == 0:
            terms.append(str(coefficient))
        elif exponent == 1:
            terms.append(f"{coefficient}*t")
        else:
            terms.append(f"{coefficient}*t^{exponent}")
    return "+".join(terms) or "0"


def rational_literal(numerator, denominator):
    require(any(value % PRIME for value in denominator), "zero denominator")
    return (f"({polynomial_literal(numerator)})//"
            f"({polynomial_literal(denominator)})")


def normal_literal(value):
    require(isinstance(value, str) and value, "normal polynomial")
    compact = "".join(value.split())
    require(re.fullmatch(r"[0-9txsrcb+*^()/\-]+", compact) is not None,
            "normal syntax")
    return compact


def build(bank_payload, q7_payload):
    bank = bank_payload["row"]
    q7 = q7_payload["row"]
    require(bank_payload["collection_complete"] is True and
            bank["status"] == "COMPLETE" and
            bank["quotient_dimension"] == DIMENSION and
            bank["matrix_labels"] == VARIABLE_LABELS and
            bank["matrix_count"] == len(VARIABLE_LABELS) and
            bank["matrix_nonzero_entry_count"] == len(bank["matrix_entries"]) and
            [item["label"] for item in bank["kernel_normals"]] == KERNEL_LABELS,
            "multiplication bank")
    require(q7_payload["collection_complete"] is True and
            q7["status"] == "COMPLETE" and
            [item["label"] for item in q7["values"][-3:]] == Q7_LABELS,
            "q7 coefficient bank")

    matrix_names = {label: f"M{label.upper()}" for label in VARIABLE_LABELS}
    matrix_lines = [
        f'{matrix_names[label]}=zero_matrix(K,{DIMENSION},{DIMENSION})'
        for label in VARIABLE_LABELS
    ]
    for entry in bank["matrix_entries"]:
        require(entry["label"] in matrix_names, "matrix label")
        matrix_lines.append(
            f'{matrix_names[entry["label"]]}[{entry["row"]},{entry["column"]}]='
            f'{rational_literal(entry["numerator"], entry["denominator"])}'
        )
    matrix_definitions = "\n".join(matrix_lines)
    matrices = ",".join(matrix_names[label] for label in VARIABLE_LABELS)
    kernel_definitions = "\n".join(
        f'{item["label"]}={normal_literal(item["polynomial"])}'
        for item in bank["kernel_normals"]
    )
    q7_definitions = "\n".join(
        f'd{index}={normal_literal(item["polynomial"])}'
        for index, item in enumerate(q7["values"][-3:])
    )

    program = f"""
using AbstractAlgebra, SHA
F=GF({PRIME})
K,t=rational_function_field(F,"t")
S,(s,x,r,c,b)=polynomial_ring(K,["s","x","r","c","b"],
                              internal_ordering=:degrevlex)
{matrix_definitions}
matrices=[{matrices}]
for left in 1:length(matrices), right in left:length(matrices)
  @assert matrices[left]*matrices[right]==matrices[right]*matrices[left]
end
{kernel_definitions}
{q7_definitions}
function matrix_of(value)
  output=zero_matrix(K,{DIMENSION},{DIMENSION})
  for termIndex in 1:length(value)
    scalar=coeff(value,termIndex)
    exponents=exponent_vector(value,termIndex)
    term=identity_matrix(K,{DIMENSION})
    for variableIndex in 1:length(matrices)
      exponent=exponents[variableIndex]
      if exponent>0
        term=term*(matrices[variableIndex]^exponent)
      end
    end
    output=output+scalar*term
  end
  return output
end
MK=[matrix_of(k0),matrix_of(k1),matrix_of(k2),
    matrix_of(k3),matrix_of(k4),matrix_of(k5)]
MD=[matrix_of(d0),matrix_of(d1),matrix_of(d2)]
println("NORMAL_MATRICES_READY 6 3")
flush(stdout)
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
function block_lift(value,field)
  output=zero_matrix(field,32,32)
  for row in 1:{DIMENSION}, column in 1:{DIMENSION}
    output[row,column]=value[row,column]
    output[row+{DIMENSION},column+{DIMENSION}]=value[row,column]
  end
  return output
end
function extension_matrix(values,field)
  inverseD2=inv(values[3])
  upperRight=-inverseD2*values[1]
  lowerRight=-inverseD2*values[2]
  output=zero_matrix(field,32,32)
  identity=identity_matrix(field,{DIMENSION})
  for row in 1:{DIMENSION}, column in 1:{DIMENSION}
    output[row,column+{DIMENSION}]=upperRight[row,column]
    output[row+{DIMENSION},column]=identity[row,column]
    output[row+{DIMENSION},column+{DIMENSION}]=lowerRight[row,column]
  end
  return output
end
function q6_matrix(baseMatrices,kernelMatrices,dMatrices,field)
  lifted=[block_lift(value,field) for value in baseMatrices]
  kernels=[block_lift(value,field) for value in kernelMatrices]
  dLifted=[block_lift(value,field) for value in dMatrices]
  extension=extension_matrix(dMatrices,field)
  zero32=zero_matrix(field,32,32)
  @assert dLifted[3]*extension^2+dLifted[2]*extension+dLifted[1]==zero32
  for value in lifted
    @assert value*extension==extension*value
  end
  LS=lifted[1]
  LX=lifted[2]
  p0=kernels[4]+LX*LS*kernels[1]
  p1=kernels[5]+LX*LS*kernels[2]
  p2=kernels[6]+LX*LS*kernels[3]
  q0=kernels[4]+extension*LS*kernels[1]
  q1=-kernels[5]-extension*LS*kernels[2]
  q2=kernels[6]+extension*LS*kernels[3]
  q6=(p2*q0-p0*q2)^2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
  return extension,q6
end
witnessT=2
witnessBase=[specialize_matrix(value,witnessT) for value in matrices]
witnessK=[specialize_matrix(value,witnessT) for value in MK]
witnessD=[specialize_matrix(value,witnessT) for value in MD]
witnessD2Det=det(witnessD[3])
@assert !iszero(witnessD2Det)
witnessExtension,witnessQ6=q6_matrix(witnessBase,witnessK,witnessD,F)
witnessQ6Det=det(witnessQ6)
@assert !iszero(witnessQ6Det)
println("WITNESS_COMPLETE ",witnessT," ",witnessD2Det," ",witnessQ6Det," ",
        count(!iszero,witnessQ6))
println("WITNESS_CERTIFIED")
flush(stdout)
symbolicD2Det=det(MD[3])
@assert !iszero(symbolicD2Det)
println("SYMBOLIC_D2_COMPLETE ",degree(numerator(symbolicD2Det))," ",
        degree(denominator(symbolicD2Det))," ",length(numerator(symbolicD2Det)),
        " ",length(denominator(symbolicD2Det)))
flush(stdout)
symbolicExtension,symbolicQ6=q6_matrix(matrices,MK,MD,K)
println("SYMBOLIC_Q6_MATRIX ",count(!iszero,symbolicQ6))
flush(stdout)
symbolicQ6Det=det(symbolicQ6)
@assert !iszero(symbolicQ6Det)
println("SYMBOLIC_Q6_COMPLETE ",degree(numerator(symbolicQ6Det))," ",
        degree(denominator(symbolicQ6Det))," ",length(numerator(symbolicQ6Det)),
        " ",length(denominator(symbolicQ6Det)))
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_q6_block_determinants.txt","w") do io
  println(io,"D2_NUM\t",coefficient_list(numerator(symbolicD2Det)))
  println(io,"D2_DEN\t",coefficient_list(denominator(symbolicD2Det)))
  println(io,"Q6_NUM\t",coefficient_list(numerator(symbolicQ6Det)))
  println(io,"Q6_DEN\t",coefficient_list(denominator(symbolicQ6Det)))
end
println("Q6_BLOCK_DETERMINANT_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "generic admissible FFF q5-q7-q6 block determinant",
        "engine": "AbstractAlgebra.jl",
        "coefficient_field": f"GF({PRIME})(t)",
        "base_quotient_dimension": DIMENSION,
        "extension_dimension": 2 * DIMENSION,
        "matrix_labels": VARIABLE_LABELS,
        "kernel_labels": KERNEL_LABELS,
        "q7_coefficient_labels": Q7_LABELS,
        "source_quotient_basis_sha256": bank["quotient_basis_sha256"],
        "source_matrix_entries_sha256": bank["matrix_entries_sha256"],
        "source_kernel_normals_sha256": bank["kernel_normals_sha256"],
        "source_q7_values_sha256": q7["values_sha256"],
        "witness_t": 2,
        "transformation_denominators_open": True,
        "symbolic_determinant_roots_open_until_complete": True,
    }


if __name__ == "__main__":
    require(polynomial_literal([0, 2, 0, PRIME + 3]) == "2*t+3*t^3",
            "polynomial literal self-test")
    require(rational_literal([1, 2], [3]) == "(1+2*t)//(3)",
            "rational literal self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_Q6_BLOCK_DETERMINANT_PROGRAM_PASS "
          "base_dimension=16 extension_dimension=32")
