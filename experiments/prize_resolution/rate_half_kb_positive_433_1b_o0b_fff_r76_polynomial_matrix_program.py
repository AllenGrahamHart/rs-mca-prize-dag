#!/usr/bin/env python3
"""Clear the R76 rational matrix denominators column by column."""


PRIME = 2130706433
DIMENSION = 16
EXPECTED_WITNESS = 244686406


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


def build(matrix_payload):
    row = matrix_payload["row"]
    require(matrix_payload["collection_complete"] is True and
            matrix_payload["field"] == PRIME and row["status"] == "COMPLETE" and
            row["quotient_dimension"] == DIMENSION and
            row["matrix_nonzero_entry_count"] == len(row["matrix_entries"]) == 256,
            "matrix bank")
    numerator_lines = [f"numerators=zero_matrix(R,{DIMENSION},{DIMENSION})"]
    denominator_lines = [f"denominators=zero_matrix(R,{DIMENSION},{DIMENSION})"]
    for entry in row["matrix_entries"]:
        numerator_lines.append(
            f'numerators[{entry["row"]},{entry["column"]}]='
            f'{polynomial_literal(entry["numerator"])}'
        )
        denominator_lines.append(
            f'denominators[{entry["row"]},{entry["column"]}]='
            f'{polynomial_literal(entry["denominator"])}'
        )
    declarations = "\n".join(numerator_lines + denominator_lines)
    program = f"""
using AbstractAlgebra, SHA
F=GF({PRIME})
R,t=polynomial_ring(F,"t")
{declarations}
columnLCM=[one(R) for _ in 1:{DIMENSION}]
for column in 1:{DIMENSION}, row in 1:{DIMENSION}
  @assert !iszero(denominators[row,column])
  columnLCM[column]=lcm(columnLCM[column],denominators[row,column])
end
polynomialMatrix=zero_matrix(R,{DIMENSION},{DIMENSION})
for column in 1:{DIMENSION}, row in 1:{DIMENSION}
  multiplier=divexact(columnLCM[column],denominators[row,column])
  polynomialMatrix[row,column]=numerators[row,column]*multiplier
end
for column in 1:{DIMENSION}
  println("COLUMN_LCM ",column," ",degree(columnLCM[column])," ",
          length(columnLCM[column]))
end
println("POLYNOMIAL_MATRIX_PROFILE ",count(!iszero,polynomialMatrix)," ",
        minimum(degree(value) for value in polynomialMatrix)," ",
        maximum(degree(value) for value in polynomialMatrix))
flush(stdout)
point=F(2)
rationalWitness=zero_matrix(F,{DIMENSION},{DIMENSION})
polynomialWitness=zero_matrix(F,{DIMENSION},{DIMENSION})
for row in 1:{DIMENSION}, column in 1:{DIMENSION}
  denominatorValue=evaluate(denominators[row,column],point)
  @assert !iszero(denominatorValue)
  rationalWitness[row,column]=evaluate(numerators[row,column],point)*
                              inv(denominatorValue)
  polynomialWitness[row,column]=evaluate(polynomialMatrix[row,column],point)
end
rationalDeterminant=det(rationalWitness)
polynomialDeterminant=det(polynomialWitness)
scaling=prod(evaluate(value,point) for value in columnLCM)
@assert rationalDeterminant==F({EXPECTED_WITNESS})
@assert polynomialDeterminant==rationalDeterminant*scaling
println("WITNESS_COMPLETE 2 ",rationalDeterminant," ",polynomialDeterminant,
        " ",scaling)
function coefficient_list(value)
  return join([string(coeff(value,index)) for index in 0:degree(value)],",")
end
open("/tmp/fff_r76_column_lcms.txt","w") do io
  for (column,value) in enumerate(columnLCM)
    println(io,column,"\t",coefficient_list(value))
  end
end
open("/tmp/fff_r76_polynomial_matrix.txt","w") do io
  for row in 1:{DIMENSION}, column in 1:{DIMENSION}
    println(io,row,"\t",column,"\t",
            coefficient_list(polynomialMatrix[row,column]))
  end
end
println("R76_POLYNOMIAL_MATRIX_CERTIFIED")
"""
    return {
        "program": program,
        "relation": "column-cleared generic admissible FFF R76 matrix",
        "engine": "AbstractAlgebra.jl",
        "coefficient_ring": f"GF({PRIME})[t]",
        "dimension": DIMENSION,
        "clearing": "column LCM",
        "source_matrix_entries_sha256": row["matrix_entries_sha256"],
        "source_unique_denominators_sha256": row["unique_denominators_sha256"],
        "source_witness_determinant": row["witness_determinant"],
        "witness_t": 2,
        "expected_witness_determinant": EXPECTED_WITNESS,
        "determinant_open": True,
    }


if __name__ == "__main__":
    require(polynomial_literal([0, 2, 0, PRIME + 3]) == "2*t+3*t^3",
            "literal self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_POLYNOMIAL_MATRIX_"
          "PROGRAM_PASS dimension=16")
