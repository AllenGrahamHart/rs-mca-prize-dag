#!/usr/bin/env python3
"""Generic paired-product rank atlas for repeated-BC cell 11."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import sys
import time

import modal


DIRECTORY = Path(__file__).parent
CORE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_function_field_core.py"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)
REMOTE_CORE = "/root/cell11_core.py"
REMOTE_TOWER = "/root/tower.json"
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
MISSING_RECORDS = ("DE+", "DF+", "EF")

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-uncolored-rank")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(CORE, REMOTE_CORE)
    .add_local_file(TOWER, REMOTE_TOWER)
)


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        rest = items[1:index] + items[index + 1:]
        for tail in canonical_matchings(rest):
            output.append(((items[0], items[index]),) + tail)
    return tuple(output)


MATCHINGS = canonical_matchings(tuple(range(6)))


def polynomial_coefficients(value):
    if value.is_zero():
        return []
    return [int(value[index]) for index in range(int(value.degree()) + 1)]


@app.function(image=image, cpu=2.0, memory=4096, timeout=420, max_containers=32)
def profile(case):
    started = time.perf_counter()
    sys.path.insert(0, "/root")
    import cell11_core as core

    tower_row, missing_record, sigma_o, pairing_index = case
    context = core.FunctionFieldContext(tower_row)
    epsilon_1, epsilon_2 = tower_row["epsilon"]
    common = core.cell11_common_data(
        context, epsilon_1, epsilon_2, tower_row["bc_sign"]
    )
    base_zero = context.zero()
    base_one = context.one()
    q_value = common["missing_product"]
    sum_squared = common["missing_sum_squared"]

    class Quartic:
        """Endpoint algebra with X^4+(2q-s^2)X^2+q^2=0."""

        __slots__ = ("values",)

        def __init__(self, *values):
            values = values or (0,)
            self.values = tuple(
                core.AlgebraElement.coerce(
                    context, values[index] if index < len(values) else 0
                )
                for index in range(4)
            )

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quartic) else Quartic(value)

        def __add__(self, other):
            other = Quartic.coerce(other)
            return Quartic(*(left + right for left, right in zip(
                self.values, other.values
            )))

        __radd__ = __add__

        def __neg__(self):
            return Quartic(*(-value for value in self.values))

        def __sub__(self, other):
            return self + (-Quartic.coerce(other))

        def __rsub__(self, other):
            return Quartic.coerce(other) - self

        def __mul__(self, other):
            other = Quartic.coerce(other)
            coefficients = [base_zero for _ in range(7)]
            for left_degree, left in enumerate(self.values):
                for right_degree, right in enumerate(other.values):
                    degree = left_degree + right_degree
                    coefficients[degree] = coefficients[degree] + left * right
            relation = (-q_value * q_value, base_zero,
                        sum_squared - 2 * q_value, base_zero)
            for degree in range(6, 3, -1):
                value = coefficients[degree]
                coefficients[degree] = base_zero
                for relation_degree, relation_value in enumerate(relation):
                    target = degree - 4 + relation_degree
                    coefficients[target] = (
                        coefficients[target] + value * relation_value
                    )
            return Quartic(*coefficients[:4])

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output, base = Quartic(1), self
            while exponent:
                if exponent & 1:
                    output = output * base
                base = base * base
                exponent //= 2
            return output

        def is_zero(self):
            return all(value.is_zero() for value in self.values)

        def multiplication_matrix(self):
            basis = tuple(
                Quartic(*(0 for _ in range(index)), 1) for index in range(4)
            )
            columns = [(self * value).values for value in basis]
            return [
                [columns[column][row] for column in range(4)]
                for row in range(4)
            ]

    endpoint = Quartic(0, 1)
    relation_check = (
        endpoint**4 - endpoint**2 * sum_squared
        + endpoint**2 * (2 * q_value) + q_value * q_value
    )
    if not relation_check.is_zero():
        raise ValueError("endpoint quartic")
    endpoint_inverse = -(
        endpoint**3 + endpoint * (2 * q_value - sum_squared)
    ) * (q_value * q_value).inverse()
    if not (endpoint * endpoint_inverse - 1).is_zero():
        raise ValueError("endpoint inverse")
    partner = endpoint_inverse * q_value

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
                + (other.values[index] if index < len(other.values) else Quartic())
                for index in range(size)
            ))

        __radd__ = __add__

        def __neg__(self):
            return YPolynomial(*(-value for value in self.values))

        def __sub__(self, other):
            return self + (-YPolynomial.coerce(other))

        def __rsub__(self, other):
            return YPolynomial.coerce(other) - self

        def __mul__(self, other):
            other = YPolynomial.coerce(other)
            output = [Quartic() for _ in range(
                len(self.values) + len(other.values) - 1
            )]
            for left_degree, left in enumerate(self.values):
                for right_degree, right in enumerate(other.values):
                    degree = left_degree + right_degree
                    output[degree] = output[degree] + left * right
            return YPolynomial(*output)

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output, base = YPolynomial(1), self
            while exponent:
                if exponent & 1:
                    output = output * base
                base = base * base
                exponent //= 2
            return output

        def degree(self):
            return len(self.values) - 1 if not self.values[-1].is_zero() else -1

    free_endpoint = YPolynomial(0, 1)
    b_value, c_value = Quartic(context.b), Quartic(context.c)
    if missing_record == "DE+":
        records = {
            "BE": b_value * partner,
            "CF": free_endpoint * c_value,
            "DE-": -Quartic(q_value),
            "DF+": free_endpoint * endpoint,
            "DF-": -(free_endpoint * endpoint),
            "EF": free_endpoint * (sigma_o * partner),
        }
    elif missing_record == "DF+":
        records = {
            "BE": free_endpoint * b_value,
            "CF": c_value * partner,
            "DE+": free_endpoint * endpoint,
            "DE-": -(free_endpoint * endpoint),
            "DF-": -Quartic(q_value),
            "EF": free_endpoint * (sigma_o * partner),
        }
    elif missing_record == "EF":
        f_value = sigma_o * partner
        records = {
            "BE": b_value * endpoint,
            "CF": c_value * f_value,
            "DE+": free_endpoint * endpoint,
            "DE-": -(free_endpoint * endpoint),
            "DF+": free_endpoint * f_value,
            "DF-": -(free_endpoint * f_value),
        }
    else:
        raise ValueError("missing record")

    residual_names = tuple(
        name for name in GLOBAL_RECORDS if name != missing_record
    )
    residual = tuple(YPolynomial.coerce(records[name]) for name in residual_names)
    a_values, b_values = common["a_values"], common["b_values"]

    def paired(left, right):
        p_values = [
            YPolynomial(b_coefficient) - left * a_coefficient
            for a_coefficient, b_coefficient in zip(a_values, b_values)
        ]
        q_values = (
            YPolynomial(b_values[0]) - right * a_values[0],
            YPolynomial(-b_values[1]) + right * a_values[1],
            YPolynomial(b_values[2]) - right * a_values[2],
        )
        return (
            (p_values[2] * q_values[0] - p_values[0] * q_values[2])**2
            - (p_values[2] * q_values[1] - p_values[1] * q_values[2])
            * (p_values[1] * q_values[0] - p_values[0] * q_values[1])
        )

    matching = MATCHINGS[pairing_index]
    equations = [paired(residual[left], residual[right])
                 for left, right in matching]

    def sylvester(left, right):
        left_degree, right_degree = left.degree(), right.degree()
        size = left_degree + right_degree
        left_descending = list(reversed(left.values))
        right_descending = list(reversed(right.values))
        matrix = []
        for shift in range(right_degree):
            matrix.append(
                [Quartic()] * shift + left_descending
                + [Quartic()] * (right_degree - 1 - shift)
            )
        for shift in range(left_degree):
            matrix.append(
                [Quartic()] * shift + right_descending
                + [Quartic()] * (left_degree - 1 - shift)
            )
        if len(matrix) != size or any(len(row) != size for row in matrix):
            raise ValueError("Sylvester shape")
        return matrix

    def flatten(matrix):
        base_size = context.dimension
        block_size = 4 * base_size
        size = len(matrix)
        output = [
            [context._rf_zero() for _ in range(block_size * size)]
            for _ in range(block_size * size)
        ]
        for block_row, row in enumerate(matrix):
            for block_column, value in enumerate(row):
                quartic_matrix = value.multiplication_matrix()
                for quartic_row in range(4):
                    for quartic_column in range(4):
                        base_matrix = quartic_matrix[
                            quartic_row
                        ][quartic_column].multiplication_matrix()
                        for base_row in range(base_size):
                            for base_column in range(base_size):
                                output[
                                    block_size * block_row
                                    + base_size * quartic_row + base_row
                                ][
                                    block_size * block_column
                                    + base_size * quartic_column + base_column
                                ] = base_matrix[base_row][base_column]
        return output

    def evaluate_polynomial(polynomial, x_value):
        if polynomial.is_zero():
            return 0
        output = 0
        for degree in range(int(polynomial.degree()), -1, -1):
            output = (
                output * x_value + int(polynomial[degree])
            ) % core.PRIME
        return output

    def specialize(matrix, x_value):
        output = []
        for row in matrix:
            specialized = []
            for value in row:
                numerator = evaluate_polynomial(value.numer, x_value)
                denominator = evaluate_polynomial(value.denom, x_value)
                if denominator == 0:
                    return None
                specialized.append(
                    numerator * pow(denominator, -1, core.PRIME) % core.PRIME
                )
            output.append(specialized)
        return output

    def matrix_rank(matrix):
        work = [row[:] for row in matrix]
        row_index = 0
        determinant = 1
        for column in range(len(work[0])):
            pivot = next(
                (row for row in range(row_index, len(work))
                 if work[row][column]),
                None,
            )
            if pivot is None:
                continue
            if pivot != row_index:
                work[row_index], work[pivot] = work[pivot], work[row_index]
                determinant = -determinant % core.PRIME
            pivot_value = work[row_index][column]
            determinant = determinant * pivot_value % core.PRIME
            inverse = pow(pivot_value, -1, core.PRIME)
            work[row_index] = [
                value * inverse % core.PRIME for value in work[row_index]
            ]
            for row in range(row_index + 1, len(work)):
                scalar = work[row][column]
                if not scalar:
                    continue
                work[row] = [
                    (left - scalar * right) % core.PRIME
                    for left, right in zip(work[row], work[row_index])
                ]
            row_index += 1
            if row_index == len(work):
                break
        return row_index, determinant % core.PRIME

    def normalize_guard(polynomial):
        if polynomial.is_zero():
            raise ZeroDivisionError("zero guard")
        leading = int(polynomial[polynomial.degree()]) % core.PRIME
        return polynomial * pow(leading, -1, core.PRIME)

    def construction_guards_nonzero(x_value):
        return all(
            evaluate_polynomial(guard, x_value) != 0
            for guard in context.guards
        )

    pair_rows = []
    selected = None
    for left, right in itertools.combinations(range(3), 2):
        matrix = flatten(sylvester(equations[left], equations[right]))
        row = {
            "equations": [left, right],
            "size": len(matrix),
            "specialization_attempts": 0,
        }
        pair_rows.append(row)
        for x_value in range(2, 130):
            row["specialization_attempts"] += 1
            if not construction_guards_nonzero(x_value):
                continue
            specialized = specialize(matrix, x_value)
            if specialized is None:
                continue
            rank, determinant = matrix_rank(specialized)
            row["last_rank"] = rank
            if rank != len(matrix):
                continue
            row["witness_x"] = x_value
            row["witness_determinant"] = determinant
            row["construction_guards_nonzero"] = True
            selected = row
            break
        if selected:
            break

    unique_guards = {}
    for guard in context.guards:
        normalized = normalize_guard(guard)
        coefficients = polynomial_coefficients(normalized)
        digest = hashlib.sha256(
            json.dumps(coefficients, separators=(",", ":")).encode()
        ).hexdigest()
        unique_guards[digest] = coefficients
    return {
        "epsilon": tower_row["epsilon"],
        "bc_sign": tower_row["bc_sign"],
        "missing_record": missing_record,
        "sigma_o": sigma_o,
        "pairing_index": pairing_index,
        "residual_records": residual_names,
        "matching": [
            [residual_names[left], residual_names[right]]
            for left, right in matching
        ],
        "equation_degrees": [value.degree() for value in equations],
        "base_degree": context.dimension,
        "pair_rows": pair_rows,
        "selected": selected,
        "status": "GENERIC_UNIT" if selected else "NO_UNIT_PAIR",
        "guards": unique_guards,
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main(bc_sign: int = 0, limit: int = 0):
    tower = json.loads(TOWER.read_text())
    rows = tuple(
        row for row in tower["rows"]
        if not bc_sign or row["bc_sign"] == bc_sign
    )
    cases = tuple(
        (row, missing_record, sigma_o, pairing_index)
        for row in rows
        for missing_record, sigma_o, pairing_index in itertools.product(
            MISSING_RECORDS, (-1, 1), range(15)
        )
    )
    if limit:
        cases = cases[:limit]
    raw = list(profile.map(cases, order_outputs=True, return_exceptions=True))
    output_rows = []
    guard_atlas = {}
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            tower_row, missing_record, sigma_o, pairing_index = case
            output_rows.append({
                "epsilon": tower_row["epsilon"],
                "bc_sign": tower_row["bc_sign"],
                "missing_record": missing_record,
                "sigma_o": sigma_o,
                "pairing_index": pairing_index,
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
            continue
        guards = row.pop("guards")
        row["guard_hashes"] = sorted(guards)
        guard_atlas.update(guards)
        output_rows.append(row)
    suffix = ""
    if bc_sign == -1:
        suffix = "_bcminus"
    elif bc_sign == 1:
        suffix = "_bcplus"
    if limit:
        suffix += "_pilot"
    result = DIRECTORY / (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_"
        f"cell11_uncolored_generic_rank{suffix}_result.json"
    )
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-uncolored-generic-rank-v1"
        ),
        "scope": (
            "Generic paired-product unit atlas for missing DE+, DF+, and EF "
            "over the exact degree-six/degree-four cell-11 source towers; "
            "exceptional rational fibers unpaid."
        ),
        "core_sha256": hashlib.sha256(CORE.read_bytes()).hexdigest(),
        "tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "bc_sign_filter": bc_sign,
        "complete_atlas": not limit,
        "case_count": len(output_rows),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in output_rows
        ).items())),
        "guard_atlas": {
            digest: ",".join(map(str, coefficients))
            for digest, coefficients in sorted(guard_atlas.items())
        },
        "rows": output_rows,
    }
    result.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(result),
        "case_count": len(output_rows),
        "status_counts": output["status_counts"],
        "guard_count": len(guard_atlas),
        "base_degrees": dict(sorted(Counter(
            str(row.get("base_degree")) for row in output_rows
        ).items())),
        "equation_degrees": dict(sorted(Counter(
            str(tuple(row.get("equation_degrees", ()))) for row in output_rows
        ).items())),
        "matrix_sizes": dict(sorted(Counter(
            str(tuple(item["size"] for item in row.get("pair_rows", ())))
            for row in output_rows
        ).items())),
        "maximum_seconds": max(
            (row.get("seconds", 0) for row in output_rows), default=0
        ),
    }, sort_keys=True))
