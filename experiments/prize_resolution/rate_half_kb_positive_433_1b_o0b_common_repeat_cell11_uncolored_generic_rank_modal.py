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


@app.function(image=image, cpu=2.0, memory=4096, timeout=600, max_containers=64)
def profile(case):
    started = time.perf_counter()
    sys.path.insert(0, "/root")
    import cell11_core as core
    from flint import fmpz_mod_ctx, fmpz_mod_mat

    (
        tower_row, missing_record, sigma_o, pairing_index,
        determinant_metadata, resultant_metadata, norm_metadata, replay_x,
    ) = case
    context = core.FunctionFieldContext(tower_row)
    epsilon_1, epsilon_2 = tower_row["epsilon"]
    common = core.cell11_common_data(
        context, epsilon_1, epsilon_2, tower_row["bc_sign"]
    )
    modular_context = fmpz_mod_ctx(core.PRIME)
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

    def matrix_determinant(matrix):
        return int(fmpz_mod_mat(matrix, modular_context).det()) % core.PRIME

    def determinant_subset(matrix, zero, one):
        size = len(matrix)
        states = {0: one}
        for row in range(size):
            updated = {}
            for mask, value in states.items():
                for column in range(size):
                    bit = 1 << column
                    if mask & bit:
                        continue
                    term = value * matrix[row][column]
                    if (mask >> (column + 1)).bit_count() % 2:
                        term = -term
                    target = mask | bit
                    updated[target] = updated.get(target, zero) + term
            states = updated
        return states[(1 << size) - 1]

    def quartic_determinant(matrix):
        return determinant_subset(matrix, Quartic(), Quartic(1))

    def rational_function_determinant(matrix):
        size = len(matrix)
        work = [row[:] for row in matrix]
        output = context._rf_one()

        def divide_without_guard(left, right):
            if right.is_zero():
                raise ZeroDivisionError("zero determinant pivot")
            return core.RationalFunction(
                context,
                left.numer * right.denom,
                left.denom * right.numer,
            )

        for column in range(size):
            pivot = next(
                (
                    row for row in range(column, size)
                    if not work[row][column].is_zero()
                ),
                None,
            )
            if pivot is None:
                return context._rf_zero()
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
                output = -output
            pivot_value = work[column][column]
            output = output * pivot_value
            for row in range(column + 1, size):
                if work[row][column].is_zero():
                    continue
                scalar = divide_without_guard(work[row][column], pivot_value)
                for target in range(column + 1, size):
                    work[row][target] = (
                        work[row][target] - scalar * work[column][target]
                    )
                work[row][column] = context._rf_zero()
        return output

    def normalize_guard(polynomial):
        if polynomial.is_zero():
            raise ZeroDivisionError("zero guard")
        leading = int(polynomial[polynomial.degree()]) % core.PRIME
        return polynomial * pow(leading, -1, core.PRIME)

    def polynomial_descriptor(polynomial, include_coefficients=False):
        normalized = normalize_guard(polynomial)
        coefficients = polynomial_coefficients(normalized)
        output = {
            "degree": int(normalized.degree()),
            "sha256": hashlib.sha256(
                json.dumps(coefficients, separators=(",", ":")).encode()
            ).hexdigest(),
        }
        if include_coefficients:
            output["coefficients"] = coefficients
        return output

    def construction_guards_nonzero(x_value):
        return all(
            evaluate_polynomial(guard, x_value) != 0
            for guard in context.guards
        )

    guard_factors = {}
    if resultant_metadata:
        for guard in context.guards:
            _, factors = normalize_guard(guard).factor()
            for factor, _ in factors:
                descriptor = polynomial_descriptor(
                    factor, include_coefficients=factor.degree() == 1
                )
                guard_factors[descriptor["sha256"]] = descriptor

    pair_rows = []
    selected = None
    for left, right in itertools.combinations(range(3), 2):
        sylvester_matrix = sylvester(equations[left], equations[right])
        matrix = flatten(sylvester_matrix)
        row = {
            "equations": [left, right],
            "size": len(matrix),
            "specialization_attempts": 0,
        }
        pair_rows.append(row)
        if replay_x:
            row["replay_x"] = replay_x
            row["construction_guards_nonzero"] = (
                construction_guards_nonzero(replay_x)
            )
            specialized = specialize(matrix, replay_x)
            if not row["construction_guards_nonzero"] or specialized is None:
                row["replay_status"] = "REPLAY_UNDEFINED"
                continue
            determinant = matrix_determinant(specialized)
            row["replay_determinant"] = determinant
            row["last_rank"] = len(matrix) if determinant else None
            row["replay_status"] = (
                "FULL_RANK" if determinant else "SINGULAR"
            )
            if determinant and selected is None:
                selected = row
            continue
        for x_value in range(2, 130):
            row["specialization_attempts"] += 1
            if not construction_guards_nonzero(x_value):
                continue
            specialized = specialize(matrix, x_value)
            if specialized is None:
                continue
            determinant = matrix_determinant(specialized)
            if determinant == 0:
                continue
            row["witness_x"] = x_value
            row["witness_determinant"] = determinant
            row["last_rank"] = len(matrix)
            row["construction_guards_nonzero"] = True
            fingerprint = []
            inverse_witness = pow(determinant, -1, core.PRIME)
            for sample in (2, 3, 5, 7, 11, 13, 17, 19):
                if not construction_guards_nonzero(sample):
                    fingerprint.append(f"{sample}:X")
                    continue
                sample_matrix = specialize(matrix, sample)
                if sample_matrix is None:
                    fingerprint.append(f"{sample}:X")
                    continue
                sample_determinant = matrix_determinant(sample_matrix)
                fingerprint.append(
                    f"{sample}:{sample_determinant * inverse_witness % core.PRIME}"
                )
            row["normalized_determinant_fingerprint"] = ",".join(fingerprint)
            if resultant_metadata:
                resultant = quartic_determinant(sylvester_matrix)
                coordinates = []
                for quartic_index, algebra_value in enumerate(resultant.values):
                    for base_index, value in enumerate(algebra_value.values):
                        if value.is_zero():
                            continue
                        numerator = normalize_guard(value.numer)
                        denominator = normalize_guard(value.denom)
                        descriptor = {
                            "quartic_index": quartic_index,
                            "base_index": base_index,
                            "numerator": polynomial_descriptor(numerator),
                            "denominator": polynomial_descriptor(denominator),
                        }
                        coordinates.append((descriptor, numerator))
                if not coordinates:
                    raise ValueError("selected quartic resultant is zero")
                row["resultant_nonzero_coordinate_count"] = len(coordinates)
                minimum, _ = min(
                    coordinates,
                    key=lambda item: (
                        item[0]["numerator"]["degree"],
                        item[0]["denominator"]["degree"],
                        item[0]["quartic_index"],
                        item[0]["base_index"],
                    ),
                )
                common_numerator = context.polynomial_context.zero()
                for _, numerator in coordinates:
                    common_numerator = common_numerator.gcd(numerator)
                common_numerator = normalize_guard(common_numerator)
                _, factors = common_numerator.factor()
                factorization = []
                base_field_roots = []
                for factor, multiplicity in factors:
                    descriptor = polynomial_descriptor(
                        factor, include_coefficients=factor.degree() == 1
                    )
                    descriptor["multiplicity"] = int(multiplicity)
                    descriptor["construction_guard_factor"] = (
                        descriptor["sha256"] in guard_factors
                    )
                    factorization.append(descriptor)
                    if factor.degree() == 1:
                        coefficients = descriptor["coefficients"]
                        root = (
                            -coefficients[0]
                            * pow(coefficients[1], -1, core.PRIME)
                        ) % core.PRIME
                        base_field_roots.append({
                            "x": root,
                            "factor_sha256": descriptor["sha256"],
                            "construction_guard_factor": descriptor[
                                "construction_guard_factor"
                            ],
                        })
                row["resultant_minimum_coordinate"] = minimum
                row["resultant_coordinate_gcd"] = {
                    **polynomial_descriptor(common_numerator),
                    "factorization": factorization,
                    "all_factors_construction_guards": all(
                        factor["construction_guard_factor"]
                        for factor in factorization
                    ),
                    "base_field_roots": sorted(
                        base_field_roots, key=lambda item: item["x"]
                    ),
                    "non_guard_base_field_roots": sorted(
                        (
                            item for item in base_field_roots
                            if not item["construction_guard_factor"]
                        ),
                        key=lambda item: item["x"],
                    ),
                }
                if norm_metadata:
                    endpoint_norm = determinant_subset(
                        resultant.multiplication_matrix(),
                        context.zero(),
                        context.one(),
                    )
                    nested_norm = rational_function_determinant(
                        endpoint_norm.multiplication_matrix()
                    )
                    if nested_norm.is_zero():
                        raise ValueError("selected nested norm is zero")
                    nested_norm_at_witness = (
                        evaluate_polynomial(nested_norm.numer, x_value)
                        * pow(
                            evaluate_polynomial(nested_norm.denom, x_value),
                            -1,
                            core.PRIME,
                        )
                    ) % core.PRIME
                    if nested_norm_at_witness != determinant:
                        raise ValueError("nested norm determinant mismatch")
                    norm_numerator = normalize_guard(nested_norm.numer)
                    norm_denominator = normalize_guard(nested_norm.denom)
                    norm_base_field_roots = []
                    for root_value, multiplicity in norm_numerator.roots():
                        root = int(root_value) % core.PRIME
                        factor = context.polynomial_context([-root, 1])
                        descriptor = polynomial_descriptor(
                            factor, include_coefficients=True
                        )
                        construction_guard_factor = (
                            descriptor["sha256"] in guard_factors
                        )
                        norm_base_field_roots.append({
                            "x": root,
                            "multiplicity": int(multiplicity),
                            "factor_sha256": descriptor["sha256"],
                            "construction_guard_factor": (
                                construction_guard_factor
                            ),
                        })
                    row["resultant_nested_norm"] = {
                        "numerator": polynomial_descriptor(norm_numerator),
                        "denominator": polynomial_descriptor(norm_denominator),
                        "witness_value": nested_norm_at_witness,
                        "base_field_roots": sorted(
                            norm_base_field_roots,
                            key=lambda item: item["x"],
                        ),
                        "non_guard_base_field_roots": sorted(
                            (
                                item for item in norm_base_field_roots
                                if not item["construction_guard_factor"]
                            ),
                            key=lambda item: item["x"],
                        ),
                    }
            if determinant_metadata:
                degree_bound = 0
                row_denominator_degree_sum = 0
                maximum_entry_degree = 0
                cleared_matrix = []
                for matrix_row in matrix:
                    row_denominator = context.polynomial_context.one()
                    for value in matrix_row:
                        common_denominator = row_denominator.gcd(value.denom)
                        row_denominator = (
                            row_denominator // common_denominator
                        ) * value.denom
                    row_denominator_degree_sum += int(row_denominator.degree())
                    row_maximum = 0
                    cleared_row = []
                    for value in matrix_row:
                        cleared = value.numer * (
                            row_denominator // value.denom
                        )
                        cleared_row.append(cleared)
                        row_maximum = max(
                            row_maximum, int(cleared.degree())
                        )
                    cleared_matrix.append(cleared_row)
                    degree_bound += row_maximum
                    maximum_entry_degree = max(maximum_entry_degree, row_maximum)
                row_content_degree_sum = 0
                for row_index, cleared_row in enumerate(cleared_matrix):
                    content = context.polynomial_context.zero()
                    for value in cleared_row:
                        content = content.gcd(value)
                    if content.is_zero():
                        raise ValueError("zero cleared row")
                    row_content_degree_sum += int(content.degree())
                    if content.degree() > 0:
                        cleared_matrix[row_index] = [
                            value // content for value in cleared_row
                        ]
                column_content_degree_sum = 0
                for column in range(len(cleared_matrix)):
                    content = context.polynomial_context.zero()
                    for cleared_row in cleared_matrix:
                        content = content.gcd(cleared_row[column])
                    if content.is_zero():
                        raise ValueError("zero cleared column")
                    column_content_degree_sum += int(content.degree())
                    if content.degree() > 0:
                        for cleared_row in cleared_matrix:
                            cleared_row[column] = (
                                cleared_row[column] // content
                            )
                primitive_degree_bound = sum(
                    max(int(value.degree()) for value in cleared_row)
                    for cleared_row in cleared_matrix
                )
                row["cleared_determinant_degree_bound"] = degree_bound
                row["row_denominator_degree_sum"] = row_denominator_degree_sum
                row["maximum_cleared_entry_degree"] = maximum_entry_degree
                row["row_content_degree_sum"] = row_content_degree_sum
                row["column_content_degree_sum"] = column_content_degree_sum
                row["primitive_determinant_degree_bound"] = primitive_degree_bound
            selected = row
            break
        if selected and not replay_x:
            break

    unique_guards = {}
    for guard in context.guards:
        normalized = normalize_guard(guard)
        coefficients = polynomial_coefficients(normalized)
        digest = hashlib.sha256(
            json.dumps(coefficients, separators=(",", ":")).encode()
        ).hexdigest()
        unique_guards[digest] = coefficients
    output = {
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
        "status": (
            "EXCEPTIONAL_ROOT_EXCLUDED"
            if replay_x and selected
            else "EXCEPTIONAL_ROOT_UNRESOLVED"
            if replay_x
            else "DEPLOYED_OFF_GUARD_UNIT"
            if selected and norm_metadata and not selected[
                "resultant_nested_norm"
            ]["non_guard_base_field_roots"]
            else "DEPLOYED_POINTWISE_NORM_COVER"
            if selected and norm_metadata
            else "NO_OFF_GUARD_VERTICAL_COMPONENT"
            if selected and resultant_metadata and selected[
                "resultant_coordinate_gcd"
            ]["all_factors_construction_guards"]
            else "GENERIC_UNIT" if selected else "NO_UNIT_PAIR"
        ),
        "guards": unique_guards,
        "guard_factors": guard_factors,
        "seconds": time.perf_counter() - started,
    }
    if replay_x:
        output["replay_x"] = replay_x
    return output


@app.local_entrypoint()
def main(bc_sign: int = 0, limit: int = 0,
         determinant_metadata: bool = False,
         resultant_metadata: bool = False, norm_metadata: bool = False,
         start: int = 0, replay_manifest: str = ""):
    if norm_metadata and not resultant_metadata:
        raise ValueError("norm metadata requires resultant metadata")
    tower = json.loads(TOWER.read_text())
    rows = tuple(
        row for row in tower["rows"]
        if not bc_sign or row["bc_sign"] == bc_sign
    )
    if replay_manifest:
        manifest = json.loads(Path(replay_manifest).read_text())
        tower_by_key = {
            (row["bc_sign"], tuple(row["epsilon"])): row
            for row in tower["rows"]
        }
        cases = tuple(
            (
                tower_by_key[(case["bc_sign"], tuple(case["epsilon"]))],
                case["missing_record"], case["sigma_o"],
                case["pairing_index"], False, False, False, case["x"],
            )
            for case in manifest["cases"]
        )
    else:
        cases = tuple(
            (
                row, missing_record, sigma_o, pairing_index,
                determinant_metadata, resultant_metadata, norm_metadata, 0,
            )
            for row in rows
            for missing_record, sigma_o, pairing_index in itertools.product(
                MISSING_RECORDS, (-1, 1), range(15)
            )
        )
    if start:
        cases = cases[start:]
    if limit:
        cases = cases[:limit]
    raw = list(profile.map(cases, order_outputs=True, return_exceptions=True))
    output_rows = []
    guard_atlas = {}
    guard_factor_atlas = {}
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            tower_row, missing_record, sigma_o, pairing_index, _, _, _, replay_x = case
            output_rows.append({
                "epsilon": tower_row["epsilon"],
                "bc_sign": tower_row["bc_sign"],
                "missing_record": missing_record,
                "sigma_o": sigma_o,
                "pairing_index": pairing_index,
                "replay_x": replay_x or None,
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
            continue
        guards = row.pop("guards")
        guard_factors = row.pop("guard_factors")
        row["guard_hashes"] = sorted(guards)
        if resultant_metadata:
            row["guard_factor_hashes"] = sorted(guard_factors)
        guard_atlas.update(guards)
        guard_factor_atlas.update(guard_factors)
        output_rows.append(row)
    suffix = ""
    if bc_sign == -1:
        suffix = "_bcminus"
    elif bc_sign == 1:
        suffix = "_bcplus"
    if limit:
        suffix += f"_pilot_s{start}_n{limit}"
    if determinant_metadata:
        suffix += "_metadata"
    if resultant_metadata:
        suffix += "_resultant"
    if norm_metadata:
        suffix += "_norm"
    if replay_manifest:
        suffix = "_exceptional_replay"
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
        "case_offset": start,
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
    if resultant_metadata:
        output["guard_factor_atlas"] = {
            digest: descriptor
            for digest, descriptor in sorted(guard_factor_atlas.items())
        }

    result_paths = []
    if replay_manifest:
        grouped_rows = {}
        for row in output_rows:
            key = (row["bc_sign"], tuple(row["epsilon"]))
            grouped_rows.setdefault(key, []).append(row)
        for (row_bc_sign, epsilon), rows_for_tower in sorted(grouped_rows.items()):
            compact_rows = []
            shard_guard_hashes = set()
            for row in rows_for_tower:
                if row["status"] == "REMOTE_ERROR":
                    compact_rows.append(row)
                    continue
                shard_guard_hashes.update(row["guard_hashes"])
                compact_rows.append({
                    key: row[key]
                    for key in (
                        "epsilon", "bc_sign", "missing_record", "sigma_o",
                        "pairing_index", "matching", "equation_degrees",
                        "base_degree", "pair_rows", "replay_x", "status",
                        "seconds",
                    )
                })
            sign_token = "plus" if row_bc_sign == 1 else "minus"
            epsilon_token = "".join(
                "p" if value == 1 else "m" for value in epsilon
            )
            shard_result = DIRECTORY / (
                "rate_half_kb_positive_433_1b_o0b_common_repeat_"
                "cell11_uncolored_exceptional_replay_"
                f"bc{sign_token}_e{epsilon_token}_result.json"
            )
            shard_output = {
                "schema": (
                    "rate-half-kb-positive-433-1b-o0b-common-repeat-"
                    "cell11-uncolored-exceptional-pair-replay-v1"
                ),
                "scope": (
                    "Exact all-pair rank replay on every non-guard deployed "
                    "root in the nested-norm atlas for one source tower."
                ),
                "core_sha256": output["core_sha256"],
                "tower_sha256": output["tower_sha256"],
                "bc_sign": row_bc_sign,
                "epsilon": list(epsilon),
                "case_count": len(compact_rows),
                "status_counts": dict(sorted(Counter(
                    row["status"] for row in compact_rows
                ).items())),
                "guard_atlas": {
                    digest: output["guard_atlas"][digest]
                    for digest in sorted(shard_guard_hashes)
                },
                "rows": compact_rows,
            }
            shard_result.write_text(
                json.dumps(shard_output, indent=2, sort_keys=True) + "\n"
            )
            result_paths.append(str(shard_result))
    elif resultant_metadata and not limit:
        grouped_rows = {}
        for row in output_rows:
            key = (row["bc_sign"], tuple(row["epsilon"]))
            grouped_rows.setdefault(key, []).append(row)
        for (row_bc_sign, epsilon), rows_for_tower in sorted(grouped_rows.items()):
            compact_rows = []
            shard_guard_hashes = set()
            shard_guard_factor_hashes = set()
            for row in rows_for_tower:
                if row["status"] == "REMOTE_ERROR":
                    compact_rows.append(row)
                    continue
                shard_guard_hashes.update(row["guard_hashes"])
                shard_guard_factor_hashes.update(row["guard_factor_hashes"])
                compact_rows.append({
                    key: row[key]
                    for key in (
                        "epsilon", "bc_sign", "missing_record", "sigma_o",
                        "pairing_index", "matching", "equation_degrees",
                        "base_degree", "selected", "status", "seconds",
                    )
                })
            sign_token = "plus" if row_bc_sign == 1 else "minus"
            epsilon_token = "".join("p" if value == 1 else "m" for value in epsilon)
            norm_token = "_norm" if norm_metadata else ""
            shard_result = DIRECTORY / (
                "rate_half_kb_positive_433_1b_o0b_common_repeat_"
                f"cell11_uncolored_resultant{norm_token}_"
                f"bc{sign_token}_e{epsilon_token}_result.json"
            )
            shard_output = {
                "schema": (
                    "rate-half-kb-positive-433-1b-o0b-common-repeat-"
                    "cell11-uncolored-resultant-factor-atlas-v1"
                ),
                "scope": (
                    "Exact nested-norm factor atlas for one cell-11 source "
                    "tower; its non-guard base-field roots are the complete "
                    "pointwise exceptional cover."
                    if norm_metadata else
                    "Exact coordinate-gcd factor atlas for one cell-11 "
                    "source tower. It excludes off-guard vertical resultant "
                    "components; pointwise zeros in split source fibers and "
                    "their norm/owner payment remain open."
                ),
                "core_sha256": output["core_sha256"],
                "tower_sha256": output["tower_sha256"],
                "bc_sign": row_bc_sign,
                "epsilon": list(epsilon),
                "complete_source_tower_atlas": len(compact_rows) == 90,
                "case_count": len(compact_rows),
                "status_counts": dict(sorted(Counter(
                    row["status"] for row in compact_rows
                ).items())),
                "guard_atlas": {
                    digest: output["guard_atlas"][digest]
                    for digest in sorted(shard_guard_hashes)
                },
                "guard_factor_atlas": {
                    digest: output["guard_factor_atlas"][digest]
                    for digest in sorted(shard_guard_factor_hashes)
                },
                "rows": compact_rows,
            }
            shard_result.write_text(
                json.dumps(shard_output, indent=2, sort_keys=True) + "\n"
            )
            result_paths.append(str(shard_result))
    else:
        result.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
        result_paths.append(str(result))
    print(json.dumps({
        "results": result_paths,
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
