#!/usr/bin/env sage
"""Reduce full-J coefficients in the rank-two c/d algebra over a route curve."""

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


def metric(value, generators=None):
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
    factors = done["identities"]["J"]["descended_factors"]
    nonunit_records = [record for record in factors if record["metric"]["degree"] > 1]
    assert [record["metric"]["degree"] for record in nonunit_records] == [8, 8, 11, 12]
    j11_record = nonunit_records[2]
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
    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")
    x, s, p = ring.gens()

    def convert_base(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * prod(
                generator ** exponent
                for generator, exponent in zip(ring.gens(), monomial)
            )
        return output

    base_generators = [
        convert_base(qslice_factor),
        convert_base(branch["essential"]["E2"]),
        convert_base(branch["essential"]["E3"]),
        convert_base(essential_j11),
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

    counters = {
        "normal_forms": 0,
        "pair_additions": 0,
        "pair_products": 0,
        "quadratic_products": 0,
        "quadratic_inversions": 0,
    }

    def normal(value):
        counters["normal_forms"] += 1
        return ring(value).reduce(basis)

    zero = ring(0)
    one = ring(1)

    # A base rational element is represented by a reduced numerator and
    # denominator. Every operation takes normal forms immediately.
    def rat(num=zero, den=one):
        num = normal(num)
        den = normal(den)
        assert den
        if not num:
            return zero, one
        scale = den.lc() ** -1
        return normal(num * scale), normal(den * scale)

    rat_zero = zero, one
    rat_one = one, one

    def rat_add(left, right):
        counters["pair_additions"] += 1
        return rat(
            normal(left[0] * right[1]) + normal(right[0] * left[1]),
            normal(left[1] * right[1]),
        )

    def rat_neg(value):
        return -value[0], value[1]

    def rat_sub(left, right):
        return rat_add(left, rat_neg(right))

    def rat_mul(left, right):
        counters["pair_products"] += 1
        if not left[0] or not right[0]:
            return rat_zero
        return rat(normal(left[0] * right[0]), normal(left[1] * right[1]))

    def rat_inv(value):
        assert value[0]
        return rat(value[1], value[0])

    def rat_div(left, right):
        return rat_mul(left, rat_inv(right))

    def rat_pow(value, exponent):
        result = rat_one
        current = value
        while exponent:
            if exponent & 1:
                result = rat_mul(result, current)
            exponent >>= 1
            if exponent:
                current = rat_mul(current, current)
        return result

    rx = rat(x, one)
    rs = rat(s, one)
    rp = rat(p, one)
    rw = rat(-convert_base(U), convert_base(V))

    # A quadratic element is a+b*c with c^2=s*c-p. Components are base
    # rational elements, so the module remains rank two throughout.
    def quad(a=rat_zero, b=rat_zero):
        return a, b

    quad_zero = quad()
    quad_one = quad(rat_one)

    def quad_add(left, right):
        return rat_add(left[0], right[0]), rat_add(left[1], right[1])

    def quad_neg(value):
        return rat_neg(value[0]), rat_neg(value[1])

    def quad_sub(left, right):
        return quad_add(left, quad_neg(right))

    def quad_mul(left, right):
        counters["quadratic_products"] += 1
        ac = rat_mul(left[0], right[0])
        bd = rat_mul(left[1], right[1])
        constant = rat_sub(ac, rat_mul(bd, rp))
        linear = rat_add(
            rat_add(rat_mul(left[0], right[1]), rat_mul(left[1], right[0])),
            rat_mul(bd, rs),
        )
        return constant, linear

    def quad_inv(value):
        counters["quadratic_inversions"] += 1
        a, b = value
        norm = rat_add(
            rat_add(rat_mul(a, a), rat_mul(rat_mul(a, b), rs)),
            rat_mul(rat_mul(b, b), rp),
        )
        assert norm[0]
        conjugate = rat_add(a, rat_mul(b, rs)), rat_neg(b)
        return rat_div(conjugate[0], norm), rat_div(conjugate[1], norm)

    def quad_div(left, right):
        return quad_mul(left, quad_inv(right))

    def quad_pow(value, exponent):
        result = quad_one
        current = value
        while exponent:
            if exponent & 1:
                result = quad_mul(result, current)
            exponent >>= 1
            if exponent:
                current = quad_mul(current, current)
        return result

    qx = quad(rx)
    qc = quad(rat_zero, rat_one)
    qd = quad(rs, rat_neg(rat_one))
    qw = quad(rw)

    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
    source_u, source_v, source_z = parent["build_source_R"]("F04")
    source_ring = parent["R"]
    source_field = parent["K"]
    polynomial_w = parent["ATLAS"]["KW"]
    b_source, c_source, d_source, w_source = source_ring.gens()

    def source_power_table(value, maximum):
        table = [quad_one]
        for _ in range(maximum):
            table.append(quad_mul(table[-1], value))
        return table

    def map_source_polynomial(value):
        value = source_ring(value)
        if not value:
            return quad_zero
        maxima = [max(monomial[index] for monomial in value.dict()) for index in range(4)]
        tables = [
            source_power_table(qx, maxima[0]),
            source_power_table(qc, maxima[1]),
            source_power_table(qd, maxima[2]),
            source_power_table(qw, maxima[3]),
        ]
        output = quad_zero
        for monomial, coefficient in value.dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            term = quad(rat(reduced, one))
            for table, exponent in zip(tables, monomial):
                term = quad_mul(term, table[exponent])
            output = quad_add(output, term)
        return output

    mapped_field_cache = {}

    def map_source_field(value):
        value = source_field(value)
        key = str(value)
        if key not in mapped_field_cache:
            mapped_field_cache[key] = quad_div(
                map_source_polynomial(value.numerator()),
                map_source_polynomial(value.denominator()),
            )
        return mapped_field_cache[key]

    def quad_is_zero(value):
        return not value[0][0] and not value[1][0]

    def polynomial_trim(value):
        while len(value) > 1 and quad_is_zero(value[-1]):
            value.pop()
        return value

    def polynomial_add(left, right):
        output = []
        for index in range(max(len(left), len(right))):
            left_value = left[index] if index < len(left) else quad_zero
            right_value = right[index] if index < len(right) else quad_zero
            output.append(quad_add(left_value, right_value))
        return polynomial_trim(output)

    def polynomial_neg(value):
        return [quad_neg(coefficient) for coefficient in value]

    def polynomial_sub(left, right):
        return polynomial_add(left, polynomial_neg(right))

    def polynomial_scale(value, scalar):
        return polynomial_trim([quad_mul(coefficient, scalar) for coefficient in value])

    def polynomial_mul(left, right):
        output = [quad_zero for _ in range(len(left) + len(right) - 1)]
        for left_index, left_value in enumerate(left):
            for right_index, right_value in enumerate(right):
                if not quad_is_zero(left_value) and not quad_is_zero(right_value):
                    index = left_index + right_index
                    output[index] = quad_add(
                        output[index], quad_mul(left_value, right_value)
                    )
        return polynomial_trim(output)

    def polynomial_shift(value):
        return [quad_zero, *value]

    def map_polynomial_w(value):
        value = polynomial_w(value)
        if not value:
            return [quad_zero]
        return [map_source_field(value[index]) for index in range(value.degree() + 1)]

    mapped_u = [map_polynomial_w(value) for value in source_u]
    mapped_v = [map_polynomial_w(value) for value in source_v]

    def evaluate_vector(mapped, label):
        output = [quad_zero]
        power = quad_one
        for polynomial in mapped:
            output = polynomial_add(output, polynomial_scale(polynomial, power))
            power = quad_mul(power, label)
        return output

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
        [quad_neg(label), quad_one]
        for label in mapped_k
        for _ in range(4)
    ]
    expected_factors.extend(
        [
            [quad_neg(mapped_c), quad_one],
            [quad_neg(mapped_c), quad_one],
            [quad_neg(mapped_d), quad_one],
            [quad_neg(mapped_d), quad_one],
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
        coefficients = [quad_one, quad_zero]
        leading = quad_one
        for factor in factors:
            available = [
                factor[index] if index < len(factor) else quad_zero
                for index in range(2)
            ]
            updated = [quad_zero, quad_zero]
            for left_index in range(2):
                for right_index in range(2 - left_index):
                    updated[left_index + right_index] = quad_add(
                        updated[left_index + right_index],
                        quad_mul(coefficients[left_index], available[right_index]),
                    )
            coefficients = updated
            leading = quad_mul(leading, factor[-1])
        return coefficients, leading

    observed, observed_leading = truncated_product(observed_factors)
    expected, expected_leading = truncated_product(expected_factors)
    mismatches = [
        quad_sub(
            quad_mul(observed[index], expected_leading),
            quad_mul(expected[index], observed_leading),
        )
        for index in range(2)
    ]
    mismatch_records = []
    for index, mismatch in enumerate(mismatches):
        record = {
            "index": index,
            "constant": {
                "numerator": metric(mismatch[0][0]),
                "denominator": metric(mismatch[0][1]),
                "zero": not bool(mismatch[0][0]),
            },
            "linear": {
                "numerator": metric(mismatch[1][0]),
                "denominator": metric(mismatch[1][1]),
                "zero": not bool(mismatch[1][0]),
            },
        }
        mismatch_records.append(record)
        print(canonical_json({"phase": "MISMATCH", **record}), flush=True)
    assert mismatch_records[0]["constant"]["zero"]
    assert mismatch_records[0]["linear"]["zero"]

    coefficient_one = mismatches[1]
    coefficient_generators = [component[0] for component in coefficient_one if component[0]]
    denominator_guards = [
        component[1]
        for mismatch in mismatches
        for component in mismatch
        if component[1] != one
    ]
    extended_generators = [*base_generators, *coefficient_generators]
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

    nilpotence_index = 1 if unit_ideal else None
    localizer = ring(1)
    localizer_steps = []
    if not unit_ideal:
        localizer_factors = [convert_base(factor) for factor in branch["unit_factors"]]
        localizer_factors.extend(denominator_guards)
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
            if not coefficient_generators
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
        "coefficient_one_generator_count": len(coefficient_generators),
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
