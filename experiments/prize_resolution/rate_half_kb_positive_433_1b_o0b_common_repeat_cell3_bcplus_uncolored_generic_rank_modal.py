#!/usr/bin/env python3
"""Generic function-field rank atlas for uncolored cell-3 BC+ records."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_generic_rank_result.json"
)
PRIME = 2130706433
IOTA = 16711679
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
MISSING_RECORDS = ("DE+", "DF+", "EF")

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcplus-uncolored-rank")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
)


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((items[0], items[index]),)+tail)
    return tuple(output)


MATCHINGS = canonical_matchings(tuple(range(6)))


@app.function(image=image, cpu=2.0, memory=3072, timeout=300, max_containers=100)
def profile(case):
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, missing_record, sigma_o, pairing_index = case
    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    u_polynomial = polynomial_context([0, 1])
    guard_polynomials = []
    capture_guards = True

    def normalize_guard(value):
        if value.is_zero():
            raise ZeroDivisionError("identically zero function-field guard")
        leading = int(value[value.degree()]) % PRIME
        return value*pow(leading, -1, PRIME)

    def register_guard(value):
        if not capture_guards:
            return
        value = normalize_guard(value)
        guard_polynomials.append(value)

    class RationalFunction:
        __slots__ = ("numer", "denom")

        def __init__(self, numer=0, denom=1):
            if isinstance(numer, RationalFunction):
                if denom != 1:
                    raise TypeError("second denominator")
                self.numer, self.denom = numer.numer, numer.denom
                return
            numer = numer if hasattr(numer, "degree") else polynomial_context([numer])
            denom = denom if hasattr(denom, "degree") else polynomial_context([denom])
            if denom.is_zero():
                raise ZeroDivisionError("zero rational denominator")
            if numer.is_zero():
                self.numer, self.denom = polynomial_context.zero(), polynomial_context.one()
                return
            common = numer.gcd(denom)
            numer, denom = numer//common, denom//common
            scale = pow(int(denom[denom.degree()]), -1, PRIME)
            self.numer, self.denom = numer*scale, denom*scale

        @staticmethod
        def coerce(value):
            return value if isinstance(value, RationalFunction) else RationalFunction(value)

        def __add__(self, other):
            other = RationalFunction.coerce(other)
            common = self.denom.gcd(other.denom)
            left, right = self.denom//common, other.denom//common
            return RationalFunction(
                self.numer*right+other.numer*left, left*other.denom
            )

        __radd__ = __add__

        def __neg__(self):
            return RationalFunction(-self.numer, self.denom)

        def __sub__(self, other):
            return self+(-RationalFunction.coerce(other))

        def __rsub__(self, other):
            return RationalFunction.coerce(other)-self

        def __mul__(self, other):
            other = RationalFunction.coerce(other)
            left_common = self.numer.gcd(other.denom)
            right_common = other.numer.gcd(self.denom)
            return RationalFunction(
                (self.numer//left_common)*(other.numer//right_common),
                (self.denom//right_common)*(other.denom//left_common),
            )

        __rmul__ = __mul__

        def inverse(self):
            register_guard(self.numer)
            return RationalFunction(self.denom, self.numer)

        def __truediv__(self, other):
            return self*RationalFunction.coerce(other).inverse()

        def __rtruediv__(self, other):
            return RationalFunction.coerce(other)/self

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse()**(-exponent)
            output, base = RationalFunction(1), self
            while exponent:
                if exponent & 1:
                    output = output*base
                base = base*base
                exponent //= 2
            return output

        def is_zero(self):
            return self.numer.is_zero()

        def __eq__(self, other):
            other = RationalFunction.coerce(other)
            return self.numer == other.numer and self.denom == other.denom

    u = RationalFunction(u_polynomial)
    alpha = (
        epsilon_1*(IOTA+epsilon_2)*(u*u+1)/u
    )
    beta = RationalFunction(-epsilon_2*IOTA)

    class Quadratic:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = RationalFunction.coerce(constant)
            self.linear = RationalFunction.coerce(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quadratic) else Quadratic(value)

        def __add__(self, other):
            other = Quadratic.coerce(other)
            return Quadratic(self.constant+other.constant, self.linear+other.linear)

        __radd__ = __add__

        def __neg__(self):
            return Quadratic(-self.constant, -self.linear)

        def __sub__(self, other):
            return self+(-Quadratic.coerce(other))

        def __rsub__(self, other):
            return Quadratic.coerce(other)-self

        def __mul__(self, other):
            other = Quadratic.coerce(other)
            return Quadratic(
                self.constant*other.constant+self.linear*other.linear*beta,
                self.constant*other.linear+self.linear*other.constant
                +self.linear*other.linear*alpha,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse()**(-exponent)
            output, base = Quadratic(1), self
            while exponent:
                if exponent & 1:
                    output = output*base
                base = base*base
                exponent //= 2
            return output

        def inverse(self):
            norm = (
                self.constant*(self.constant+self.linear*alpha)
                - self.linear*self.linear*beta
            )
            register_guard(norm.numer)
            inverse_norm = RationalFunction(1)/norm
            return Quadratic(
                (self.constant+self.linear*alpha)*inverse_norm,
                -self.linear*inverse_norm,
            )

        def norm(self):
            return (
                self.constant*(self.constant+self.linear*alpha)
                - self.linear*self.linear*beta
            )

        def __truediv__(self, other):
            return self*Quadratic.coerce(other).inverse()

        def __rtruediv__(self, other):
            return Quadratic.coerce(other)/self

        def is_zero(self):
            return self.constant.is_zero() and self.linear.is_zero()

        def __eq__(self, other):
            other = Quadratic.coerce(other)
            return self.constant == other.constant and self.linear == other.linear

    r = Quadratic(0, 1)
    if r*r != r*alpha+beta:
        raise ValueError("torus quadratic relation")

    def determinant_no_division(matrix):
        size = len(matrix)
        output = Quadratic()
        for permutation in itertools.permutations(range(size)):
            inversions = sum(
                permutation[left] > permutation[right]
                for left in range(size) for right in range(left+1, size)
            )
            term = Quadratic(-1 if inversions % 2 else 1)
            for row, column in enumerate(permutation):
                term = term*matrix[row][column]
            output = output+term
        return output

    b = -u**-3
    c = u
    r2, r4 = r*r, r**4
    labels = (Quadratic(1), r4, Quadratic(-1), r2, -r2)
    products = (Quadratic(-1), Quadratic(b), Quadratic(c),
                Quadratic(b*c), Quadratic(b*c))
    matrix = [
        [-product, -product*label, -product*label*label,
         Quadratic(1), label, label*label]
        for product, label in zip(products, labels)
    ]
    cofactors = []
    for column in range(6):
        minor = [row[:column]+row[column+1:] for row in matrix]
        cofactors.append(((-1)**column)*determinant_no_division(minor))
    scale = r4*(1-r4)
    kernel = [scale*value for value in cofactors]
    a_values, b_values = kernel[:3], kernel[3:]
    a_pivot = sum(
        (value*r4**index for index, value in enumerate(cofactors[:3])),
        Quadratic(),
    )
    beta_0 = -epsilon_1*epsilon_2*r2*(1+b)*a_pivot
    beta_1 = -beta_0
    missing_label = -r4

    def evaluate(coefficients, value):
        return sum(
            (coefficient*value**index
             for index, coefficient in enumerate(coefficients)),
            Quadratic(),
        )

    a_missing = evaluate(a_values, missing_label)
    b_missing = evaluate(b_values, missing_label)
    beta_missing = beta_0+beta_1*missing_label
    q_value = b_missing/a_missing
    sum_squared = missing_label*beta_missing**2/a_missing**2
    quartic_relation = (
        -q_value*q_value,
        Quadratic(),
        sum_squared-2*q_value,
        Quadratic(),
    )

    class Quartic:
        __slots__ = ("values",)

        def __init__(self, *values):
            values = values or (0,)
            self.values = tuple(
                Quadratic.coerce(values[index] if index < len(values) else 0)
                for index in range(4)
            )

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quartic) else Quartic(value)

        def __add__(self, other):
            other = Quartic.coerce(other)
            return Quartic(*(left+right for left, right in zip(
                self.values, other.values
            )))

        __radd__ = __add__

        def __neg__(self):
            return Quartic(*(-value for value in self.values))

        def __sub__(self, other):
            return self+(-Quartic.coerce(other))

        def __rsub__(self, other):
            return Quartic.coerce(other)-self

        def __mul__(self, other):
            other = Quartic.coerce(other)
            coefficients = [Quadratic() for _ in range(7)]
            for left_degree, left in enumerate(self.values):
                for right_degree, right in enumerate(other.values):
                    coefficients[left_degree+right_degree] = (
                        coefficients[left_degree+right_degree]+left*right
                    )
            for degree in range(6, 3, -1):
                value = coefficients[degree]
                coefficients[degree] = Quadratic()
                for relation_degree, relation_value in enumerate(quartic_relation):
                    target = degree-4+relation_degree
                    coefficients[target] = coefficients[target]+value*relation_value
            return Quartic(*coefficients[:4])

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output, base = Quartic(1), self
            while exponent:
                if exponent & 1:
                    output = output*base
                base = base*base
                exponent //= 2
            return output

        def is_zero(self):
            return all(value.is_zero() for value in self.values)

        def multiplication_matrix(self):
            basis = tuple(Quartic(*(0 for _ in range(index)), 1)
                          for index in range(4))
            columns = [(self*value).values for value in basis]
            return [[columns[column][row] for column in range(4)]
                    for row in range(4)]

    x = Quartic(0, 1)
    quartic_check = (
        x**4-(x*x)*sum_squared+(x*x)*(2*q_value)+q_value*q_value
    )
    if not quartic_check.is_zero():
        raise ValueError("missing endpoint quartic")
    x_inverse = -(x**3+x*(2*q_value-sum_squared))*(q_value*q_value).inverse()
    if not (x*x_inverse-1).is_zero():
        raise ValueError("quartic endpoint inverse")
    other_endpoint = x_inverse*q_value

    class YPolynomial:
        __slots__ = ("values",)

        def __init__(self, *values):
            values = values or (0,)
            values = [Quartic.coerce(value) for value in values]
            while len(values) > 1 and values[-1].is_zero():
                values.pop()
            self.values = tuple(values)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, YPolynomial) else YPolynomial(value)

        def __add__(self, other):
            other = YPolynomial.coerce(other)
            size = max(len(self.values), len(other.values))
            return YPolynomial(*(
                (self.values[index] if index < len(self.values) else Quartic())
                +(other.values[index] if index < len(other.values) else Quartic())
                for index in range(size)
            ))

        __radd__ = __add__

        def __neg__(self):
            return YPolynomial(*(-value for value in self.values))

        def __sub__(self, other):
            return self+(-YPolynomial.coerce(other))

        def __rsub__(self, other):
            return YPolynomial.coerce(other)-self

        def __mul__(self, other):
            other = YPolynomial.coerce(other)
            output = [Quartic()]*(len(self.values)+len(other.values)-1)
            for left_degree, left in enumerate(self.values):
                for right_degree, right in enumerate(other.values):
                    degree = left_degree+right_degree
                    output[degree] = output[degree]+left*right
            return YPolynomial(*output)

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output, base = YPolynomial(1), self
            while exponent:
                if exponent & 1:
                    output = output*base
                base = base*base
                exponent //= 2
            return output

        def degree(self):
            return len(self.values)-1 if not self.values[-1].is_zero() else -1

    y = YPolynomial(0, 1)
    b_quartic, c_quartic = Quartic(b), Quartic(c)
    if missing_record == "DE+":
        records = {
            "BE": b_quartic*other_endpoint,
            "CF": y*c_quartic,
            "DE-": -Quartic(q_value),
            "DF+": y*x,
            "DF-": -(y*x),
            "EF": y*(sigma_o*other_endpoint),
        }
    elif missing_record == "DF+":
        records = {
            "BE": y*b_quartic,
            "CF": c_quartic*other_endpoint,
            "DE+": y*x,
            "DE-": -(y*x),
            "DF-": -Quartic(q_value),
            "EF": y*(sigma_o*other_endpoint),
        }
    elif missing_record == "EF":
        f_value = sigma_o*other_endpoint
        records = {
            "BE": b_quartic*x,
            "CF": c_quartic*f_value,
            "DE+": y*x,
            "DE-": -(y*x),
            "DF+": y*f_value,
            "DF-": -(y*f_value),
        }
    else:
        raise ValueError("missing record")
    residual_names = tuple(name for name in GLOBAL_RECORDS if name != missing_record)
    residual = tuple(YPolynomial.coerce(records[name]) for name in residual_names)

    def paired(left, right):
        p_values = [YPolynomial(b_coefficient)-left*a_coefficient
                    for a_coefficient, b_coefficient in zip(a_values, b_values)]
        q_values = (
            YPolynomial(b_values[0])-right*a_values[0],
            YPolynomial(-b_values[1])+right*a_values[1],
            YPolynomial(b_values[2])-right*a_values[2],
        )
        return (
            (p_values[2]*q_values[0]-p_values[0]*q_values[2])**2
            -(p_values[2]*q_values[1]-p_values[1]*q_values[2])
            *(p_values[1]*q_values[0]-p_values[0]*q_values[1])
        )

    matching = MATCHINGS[pairing_index]
    equations = [paired(residual[left], residual[right])
                 for left, right in matching]
    equation_degrees = [value.degree() for value in equations]

    def sylvester(left, right):
        left_degree, right_degree = left.degree(), right.degree()
        size = left_degree+right_degree
        left_descending = list(reversed(left.values))
        right_descending = list(reversed(right.values))
        matrix = []
        for shift in range(right_degree):
            matrix.append([Quartic()]*shift+left_descending
                          +[Quartic()]*(right_degree-1-shift))
        for shift in range(left_degree):
            matrix.append([Quartic()]*shift+right_descending
                          +[Quartic()]*(left_degree-1-shift))
        if len(matrix) != size or any(len(row) != size for row in matrix):
            raise ValueError("Sylvester shape")
        return matrix

    def flatten(matrix):
        size = len(matrix)
        output = [[Quadratic() for _ in range(4*size)] for _ in range(4*size)]
        for block_row, row in enumerate(matrix):
            for block_column, value in enumerate(row):
                block = value.multiplication_matrix()
                for inner_row in range(4):
                    for inner_column in range(4):
                        output[4*block_row+inner_row][4*block_column+inner_column] = (
                            block[inner_row][inner_column]
                        )
        return output

    def matrix_rank(matrix):
        work = [row[:] for row in matrix]
        row_index = 0
        determinant_value = Quadratic(1)
        for column in range(len(work[0])):
            pivot = next(
                (row for row in range(row_index, len(work))
                 if not work[row][column].is_zero()),
                None,
            )
            if pivot is None:
                continue
            if pivot != row_index:
                work[row_index], work[pivot] = work[pivot], work[row_index]
                determinant_value = -determinant_value
            pivot_value = work[row_index][column]
            determinant_value = determinant_value*pivot_value
            inverse = pivot_value.inverse()
            for index in range(column, len(work[0])):
                work[row_index][index] = work[row_index][index]*inverse
            for row in range(row_index+1, len(work)):
                scalar = work[row][column]
                if scalar.is_zero():
                    continue
                for index in range(column, len(work[0])):
                    work[row][index] = (
                        work[row][index]-scalar*work[row_index][index]
                    )
            row_index += 1
            if row_index == len(work):
                break
        return row_index, determinant_value

    pair_rows = []
    selected = None
    capture_guards = False
    for left, right in itertools.combinations(range(3), 2):
        matrix = flatten(sylvester(equations[left], equations[right]))
        rank, determinant_value = matrix_rank(matrix)
        row = {
            "equations": [left, right],
            "size": len(matrix),
            "rank": rank,
        }
        pair_rows.append(row)
        if rank == len(matrix):
            selected = row
            raw_determinant_guard = normalize_guard(
                determinant_value.norm().numer
            )
            determinant_guard = raw_determinant_guard
            for construction_guard in guard_polynomials:
                construction_guard = normalize_guard(construction_guard)
                while determinant_guard.degree() > 0:
                    common = determinant_guard.gcd(construction_guard)
                    if common.degree() == 0:
                        break
                    determinant_guard = determinant_guard//common
            determinant_guard = normalize_guard(determinant_guard)
            selected["raw_determinant_degree"] = int(
                raw_determinant_guard.degree()
            )
            selected["residual_determinant_degree"] = int(
                determinant_guard.degree()
            )
            guard_polynomials.append(determinant_guard)
            break

    unique_guards = {}
    for guard in guard_polynomials:
        coefficients = [int(guard[index]) % PRIME
                        for index in range(int(guard.degree())+1)]
        digest = hashlib.sha256(
            json.dumps(coefficients, separators=(",", ":")).encode()
        ).hexdigest()
        unique_guards[digest] = coefficients
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "missing_record": missing_record,
        "sigma_o": sigma_o,
        "pairing_index": pairing_index,
        "residual_records": residual_names,
        "matching": [[residual_names[left], residual_names[right]]
                     for left, right in matching],
        "equation_degrees": equation_degrees,
        "pair_rows": pair_rows,
        "status": "GENERIC_UNIT" if selected else "NO_UNIT_PAIR",
        "selected": selected,
        "guards": unique_guards,
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(itertools.product(
        (-1, 1), (-1, 1), MISSING_RECORDS, (-1, 1), range(15)
    ))
    if limit:
        cases = cases[:limit]
    raw = list(profile.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    guard_atlas = {}
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "missing_record": case[2],
                "sigma_o": case[3], "pairing_index": case[4],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
            continue
        guards = row.pop("guards")
        row["guard_hashes"] = sorted(guards)
        guard_atlas.update(guards)
        rows.append(row)
    status_counts = dict(sorted(Counter(row["status"] for row in rows).items()))
    guard_degree_histogram = dict(sorted(Counter(
        str(len(coefficients)-1) for coefficients in guard_atlas.values()
    ).items()))
    compact_guard_atlas = {
        digest: ",".join(map(str, coefficients))
        for digest, coefficients in guard_atlas.items()
    }
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-uncolored-generic-rank-v1",
        "scope": (
            "Generic function-field rank of residual paired-product systems "
            "for missing DE+, DF+, and EF; exceptional-base fibers unpaid."
        ),
        "case_count": len(rows),
        "complete_atlas": not limit,
        "status_counts": status_counts,
        "guard_atlas": compact_guard_atlas,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "case_count": len(rows),
        "status_counts": status_counts,
        "guard_count": len(guard_atlas),
        "guard_degree_histogram": guard_degree_histogram,
        "equation_degree_histogram": dict(sorted(Counter(
            str(tuple(row.get("equation_degrees", []))) for row in rows
        ).items())),
        "maximum_seconds": max(
            (row.get("seconds", 0) for row in rows), default=0
        ),
    }, sort_keys=True))
