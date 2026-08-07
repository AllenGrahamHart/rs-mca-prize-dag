#!/usr/bin/env sage
"""Reduce full-J coefficients directly on an F04 cubic/J11 quotient."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")
FULL_IDENTITY = Path("/full_identity.json")


def load_library():
    namespace = dict(globals())
    namespace.update({"__name__": "branch_core_library", "__file__": str(LIBRARY)})
    raw = LIBRARY.read_text()
    exec(compile(raw, str(LIBRARY), "exec"), namespace)
    return namespace


def digest(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def canonical_json(value):
    return json.dumps(
        value,
        sort_keys=True,
        default=lambda item: int(item) if item in ZZ else str(item),
    )


def polynomial_metric(value, generators=None):
    value = value.parent()(value)
    generators = value.parent().gens() if generators is None else generators
    return {
        "degree": int(value.total_degree()) if value else -1,
        "degrees": [int(value.degree(generator)) for generator in generators],
        "terms": int(len(value.monomials())) if value else 0,
        "sha256": digest(value),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("R02", "R20"), required=True)
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    cell = f"F04-{args.target}"
    qslice_factor_index = 0 if args.target == "R02" else 1
    print(canonical_json({"phase": "START", "cell": cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](cell)
    base = branch["base"]
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    assert len(r_factors) == 3
    qslice_factor = r_factors[qslice_factor_index]

    full_data = json.loads(FULL_IDENTITY.read_text())
    row = full_data["results"][0]
    assert row["assignment"] == "F04" and row["status"] == "PASS"
    done = next(record for record in row["records"] if record.get("phase") == "DONE")
    factor_records = done["identities"]["J"]["descended_factors"]
    nonunit_records = [record for record in factor_records if record["metric"]["degree"] > 1]
    assert len(nonunit_records) == 4
    j11_record = nonunit_records[2]
    assert j11_record["metric"]["degree"] == 11
    assert j11_record["polynomial"] is not None

    qring = PolynomialRing(QQ, names=("x", "s", "p", "w"), order="degrevlex")
    j11 = qring(j11_record["polynomial"])
    univariate = PolynomialRing(base, "w")
    w_univariate = univariate.gen()

    def to_univariate(value):
        output = univariate(0)
        for monomial, coefficient in qring(value).dict().items():
            output += (
                QQ(coefficient)
                * prod(
                    generator ** exponent
                    for generator, exponent in zip(base.gens(), monomial[:3])
                )
                * w_univariate ** monomial[3]
            )
        return output

    U = branch["equations"]["U"]
    V = branch["equations"]["V"]
    j11_univariate = to_univariate(j11)
    j11_degree = int(j11_univariate.degree())
    transformed_j11 = base(
        sum(
            j11_univariate[index] * (-U) ** index * V ** (j11_degree - index)
            for index in range(j11_degree + 1)
        )
    )
    essential_j11 = base(1)
    for factor, exponent in transformed_j11.factor():
        if library["normalized_key"](factor) not in branch["unit_keys"]:
            essential_j11 *= factor ** exponent
    essential_j11 = base(essential_j11)

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p", "c"), order="degrevlex")
    x, s, p, c = ring.gens()
    d = s - c

    def convert_base(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * prod(
                generator ** exponent
                for generator, exponent in zip((x, s, p), monomial)
            )
        return output

    base_generators = [
        convert_base(qslice_factor),
        convert_base(branch["essential"]["E2"]),
        convert_base(branch["essential"]["E3"]),
        convert_base(essential_j11),
        c ** 2 - s * c + p,
    ]
    print(canonical_json({"phase": "BASE_GROEBNER_BEGIN"}), flush=True)
    basis = list(ring.ideal(base_generators).groebner_basis(algorithm="singular:slimgb"))
    assert basis != [ring(1)]
    dimension = int(ring.ideal(basis).dimension())
    assert dimension == 1
    print(
        canonical_json(
            {
                "phase": "BASE_GROEBNER_DONE",
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
                "dimension": dimension,
            }
        ),
        flush=True,
    )

    counters = {"normal_forms": 0, "pair_additions": 0, "pair_products": 0}

    def normal(value):
        counters["normal_forms"] += 1
        return ring(value).reduce(basis)

    one = ring(1)
    zero = ring(0)

    def pair(num=zero, den=one):
        num = normal(num)
        den = normal(den)
        assert den
        if not num:
            return zero, one
        scale = den.lc() ** -1
        return normal(num * scale), normal(den * scale)

    def pair_add(left, right):
        counters["pair_additions"] += 1
        left_num, left_den = left
        right_num, right_den = right
        return pair(
            normal(left_num * right_den) + normal(right_num * left_den),
            normal(left_den * right_den),
        )

    def pair_neg(value):
        return -value[0], value[1]

    def pair_sub(left, right):
        return pair_add(left, pair_neg(right))

    def pair_mul(left, right):
        counters["pair_products"] += 1
        if not left[0] or not right[0]:
            return zero, one
        return pair(normal(left[0] * right[0]), normal(left[1] * right[1]))

    def pair_pow(value, exponent):
        result = one, one
        current = value
        while exponent:
            if exponent & 1:
                result = pair_mul(result, current)
            exponent >>= 1
            if exponent:
                current = pair_mul(current, current)
        return result

    w_pair = pair(-convert_base(U), convert_base(V))

    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
    source_u, source_v, source_z = parent["build_source_R"]("F04")
    source_ring = parent["R"]
    source_field = parent["K"]
    polynomial_w = parent["ATLAS"]["KW"]
    capital_w = parent["ATLAS"]["W"]
    b_source, c_source, d_source, w_source = source_ring.gens()

    def map_source_polynomial(value):
        value = source_ring(value)
        grouped = {}
        for monomial, coefficient in value.dict().items():
            eb, ec, ed, ew = monomial
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            grouped[ew] = grouped.get(ew, zero) + (
                reduced * x ** eb * c ** ec * d ** ed
            )
        maximum = max(grouped, default=0)
        coefficients = [normal(grouped.get(index, zero)) for index in range(maximum + 1)]
        result = pair(coefficients[maximum], one)
        for index in range(maximum - 1, -1, -1):
            result = pair_add(pair_mul(result, w_pair), pair(coefficients[index], one))
        return result

    mapped_field_cache = {}

    def map_source_field(value):
        value = source_field(value)
        key = str(value)
        if key not in mapped_field_cache:
            numerator = map_source_polynomial(value.numerator())
            denominator = map_source_polynomial(value.denominator())
            mapped_field_cache[key] = pair(
                normal(numerator[0] * denominator[1]),
                normal(numerator[1] * denominator[0]),
            )
        return mapped_field_cache[key]

    def trim(polynomial):
        while len(polynomial) > 1 and not polynomial[-1][0]:
            polynomial.pop()
        return polynomial

    def polynomial_add(left, right):
        output = []
        for index in range(max(len(left), len(right))):
            left_value = left[index] if index < len(left) else (zero, one)
            right_value = right[index] if index < len(right) else (zero, one)
            output.append(pair_add(left_value, right_value))
        return trim(output)

    def polynomial_neg(value):
        return [pair_neg(coefficient) for coefficient in value]

    def polynomial_sub(left, right):
        return polynomial_add(left, polynomial_neg(right))

    def polynomial_scale(value, scalar):
        return trim([pair_mul(coefficient, scalar) for coefficient in value])

    def polynomial_mul(left, right):
        output = [(zero, one) for _ in range(len(left) + len(right) - 1)]
        for left_index, left_value in enumerate(left):
            for right_index, right_value in enumerate(right):
                if left_value[0] and right_value[0]:
                    index = left_index + right_index
                    output[index] = pair_add(
                        output[index], pair_mul(left_value, right_value)
                    )
        return trim(output)

    def polynomial_shift(value):
        return [(zero, one), *value]

    def map_polynomial_w(value):
        value = polynomial_w(value)
        if not value:
            return [(zero, one)]
        return [map_source_field(value[index]) for index in range(value.degree() + 1)]

    mapped_u = [map_polynomial_w(value) for value in source_u]
    mapped_v = [map_polynomial_w(value) for value in source_v]

    def evaluate_vector(mapped, label):
        result = [(zero, one)]
        power = one, one
        for polynomial in mapped:
            result = polynomial_add(result, polynomial_scale(polynomial, power))
            power = pair_mul(power, label)
        return result

    def g_at(label):
        uu = evaluate_vector(mapped_u, label)
        vv = evaluate_vector(mapped_v, label)
        return polynomial_sub(
            polynomial_mul(uu, uu),
            polynomial_shift(polynomial_mul(vv, vv)),
        )

    labels_j = (
        source_field(2),
        source_field(1) / 2,
        source_field(b_source),
        1 / source_field(b_source),
        source_field(c_source),
        source_field(d_source),
    )
    labels_k = (
        source_field(w_source),
        source_z,
        1 / source_z,
        1 / source_field(c_source),
        1 / source_field(d_source),
    )
    mapped_j = [map_source_field(value) for value in labels_j]
    mapped_k = [map_source_field(value) for value in labels_k]
    mapped_c = map_source_field(source_field(c_source))
    mapped_d = map_source_field(source_field(d_source))
    observed_factors = [g_at(label) for label in mapped_j]
    expected_factors = [
        [pair_neg(label), (one, one)]
        for label in mapped_k
        for _ in range(4)
    ]
    expected_factors.extend(
        [
            [pair_neg(mapped_c), (one, one)],
            [pair_neg(mapped_c), (one, one)],
            [pair_neg(mapped_d), (one, one)],
            [pair_neg(mapped_d), (one, one)],
        ]
    )
    print(
        canonical_json(
            {
                "phase": "FACTORS_MAPPED",
                "observed_factor_count": len(observed_factors),
                "expected_factor_count": len(expected_factors),
                "mapped_field_cache": len(mapped_field_cache),
                "counters": counters,
            }
        ),
        flush=True,
    )

    def truncated_product(factors):
        coefficients = [(one, one), (zero, one)]
        leading = one, one
        for factor in factors:
            available = [
                factor[index] if index < len(factor) else (zero, one)
                for index in range(2)
            ]
            updated = [(zero, one), (zero, one)]
            for left_index in range(2):
                for right_index in range(2 - left_index):
                    updated[left_index + right_index] = pair_add(
                        updated[left_index + right_index],
                        pair_mul(coefficients[left_index], available[right_index]),
                    )
            coefficients = updated
            leading = pair_mul(leading, factor[-1])
        return coefficients, leading

    observed, observed_leading = truncated_product(observed_factors)
    expected, expected_leading = truncated_product(expected_factors)
    mismatches = [
        pair_sub(
            pair_mul(observed[index], expected_leading),
            pair_mul(expected[index], observed_leading),
        )
        for index in range(2)
    ]
    mismatch_records = []
    for index, (numerator, denominator) in enumerate(mismatches):
        record = {
            "index": index,
            "numerator": polynomial_metric(numerator),
            "denominator": polynomial_metric(denominator),
            "zero": not bool(numerator),
        }
        mismatch_records.append(record)
        print(canonical_json({"phase": "MISMATCH", **record}), flush=True)
    assert mismatch_records[0]["zero"]

    coefficient_one = mismatches[1][0]
    denominator_guard = normal(mismatches[0][1] * mismatches[1][1])
    assert denominator_guard
    extended_generators = [*base_generators]
    if coefficient_one:
        extended_generators.append(coefficient_one)
    print(canonical_json({"phase": "EXTENDED_GROEBNER_BEGIN"}), flush=True)
    extended_basis = list(
        ring.ideal(extended_generators).groebner_basis(algorithm="singular:slimgb")
    )
    unit_ideal = extended_basis == [ring(1)]
    extended_dimension = -1 if unit_ideal else int(ring.ideal(extended_basis).dimension())
    print(
        canonical_json(
            {
                "phase": "EXTENDED_GROEBNER_DONE",
                "basis_size": len(extended_basis),
                "basis_sha256": digest("\n".join(str(value) for value in extended_basis)),
                "dimension": extended_dimension,
                "unit_ideal": unit_ideal,
            }
        ),
        flush=True,
    )

    localizer = ring(1)
    localizer_steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        localizer_factors = [
            convert_base(factor) for factor in branch["unit_factors"]
        ]
        localizer_factors.append(denominator_guard)
        for index, factor in enumerate(localizer_factors, start=1):
            localizer = (localizer * factor).reduce(extended_basis)
            step = {
                "index": index,
                "zero": not bool(localizer),
                "degree": int(localizer.total_degree()) if localizer else None,
                "terms": int(len(localizer.monomials())) if localizer else None,
                "sha256": digest(localizer),
            }
            localizer_steps.append(step)
            if not localizer:
                nilpotence_index = 1
                break
        if localizer:
            current = localizer
            for exponent in range(2, 5):
                current = (current * localizer).reduce(extended_basis)
                if not current:
                    nilpotence_index = exponent
                    break

    terminal = (
        "FULL_J_COEFFICIENT_ONE_INTERSECTION_EMPTY"
        if nilpotence_index is not None
        else (
            "FULL_J_COEFFICIENT_ONE_DEPENDENT"
            if not coefficient_one
            else "FULL_J_COEFFICIENT_ONE_INTERSECTION_SURVIVES"
        )
    )
    result = {
        "phase": "DONE",
        "cell": cell,
        "base_basis_size": len(basis),
        "base_basis_sha256": digest("\n".join(str(value) for value in basis)),
        "base_dimension": dimension,
        "mismatches": mismatch_records,
        "extended_basis_size": len(extended_basis),
        "extended_basis_sha256": digest("\n".join(str(value) for value in extended_basis)),
        "extended_dimension": extended_dimension,
        "localizer_steps": localizer_steps,
        "localizer_nilpotence_index": nilpotence_index,
        "counters": counters,
        "terminal": terminal,
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
