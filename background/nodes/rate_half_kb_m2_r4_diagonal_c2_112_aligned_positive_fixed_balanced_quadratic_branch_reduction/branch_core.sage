"""Shared exact constructor for balanced fixed quadratic branches."""

import hashlib
from pathlib import Path


ROOT = Path("/repo")
FRONTIER = (
    ROOT
    / "experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_fixed_frontier_v1.sage"
)


def digest(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def load_frontier():
    namespace = dict(globals())
    namespace.update({"__name__": "fixed_frontier_library", "__file__": str(FRONTIER)})
    raw = FRONTIER.read_text()
    exec(compile(raw, str(FRONTIER), "exec"), namespace)
    return namespace


def normalized_key(value):
    value = value.parent()(value)
    if not value:
        return "0"
    return str(value / value.lc())


def metric(value, generators=None):
    value = value.parent()(value)
    generators = value.parent().gens() if generators is None else generators
    return {
        "degree": int(value.total_degree()) if value else -1,
        "degrees": [int(value.degree(generator)) for generator in generators],
        "terms": int(len(value.monomials())) if value else 0,
        "sha256": digest(value),
    }


def factor_records(value, unit_keys):
    records = []
    for factor, exponent in value.factor():
        factor_metric = metric(factor)
        records.append(
            {
                "factor": factor,
                "exponent": int(exponent),
                "metric": factor_metric,
                "named_unit_factor": normalized_key(factor) in unit_keys,
            }
        )
    return records


def build_branch(cell):
    assignment, target = cell.split("-")
    assert assignment in ("F04", "F05", "F06", "F07")
    assert target in ("R02", "R11", "R20")
    frontier = load_frontier()
    parent = frontier["PARENT"]
    rows, _ = parent["qslice_system"](assignment, target)
    source = parent["S"]

    base = PolynomialRing(QQ, names=("x", "s", "p"), order="degrevlex")
    x, s, p = base.gens()
    univariate = PolynomialRing(base, "w")
    w = univariate.gen()

    def convert(value):
        output = univariate(0)
        for monomial, coefficient in source(value).dict().items():
            output += (
                QQ(coefficient)
                * x ** monomial[0]
                * s ** monomial[1]
                * p ** monomial[2]
                * w ** monomial[3]
            )
        return output

    converted = [convert(row) for row in rows]
    first, second = converted[:2]
    assert first.degree() == second.degree() == 2
    A, B, C = first[2], first[1], first[0]
    D, E, F = second[2], second[1], second[0]
    U = base(A * F - C * D)
    V = base(A * E - B * D)
    Z = base(B * F - C * E)
    R = base(U ** 2 - V * Z)
    assert R == base(first.resultant(second))

    def clear_at_minus_u_over_v(poly):
        degree = int(poly.degree())
        return base(
            sum(
                poly[index] * (-U) ** index * V ** (degree - index)
                for index in range(degree + 1)
            )
        )

    E2 = clear_at_minus_u_over_v(converted[2])
    E3 = clear_at_minus_u_over_v(converted[3])

    named_units = parent["middle_units"](source, True)

    def source_to_univariate(value):
        output = univariate(0)
        for monomial, coefficient in source(value).dict().items():
            output += (
                QQ(coefficient)
                * x ** monomial[0]
                * s ** monomial[1]
                * p ** monomial[2]
                * w ** monomial[3]
            )
        return output

    transported_units = [V]
    transported_units.extend(
        clear_at_minus_u_over_v(source_to_univariate(value)) for value in named_units
    )
    unit_keys = set()
    unit_factors = {}
    for value in transported_units:
        for factor, _ in value.factor():
            key = normalized_key(factor)
            unit_keys.add(key)
            unit_factors[key] = factor

    equations = {"U": U, "V": V, "Z": Z, "R": R, "E2": E2, "E3": E3}
    factors = {name: factor_records(value, unit_keys) for name, value in equations.items()}
    essential = {
        name: base.prod(
            record["factor"] ** record["exponent"]
            for record in records
            if not record["named_unit_factor"]
        )
        for name, records in factors.items()
    }
    return {
        "base": base,
        "converted": converted,
        "equations": equations,
        "factors": factors,
        "essential": essential,
        "transported_units": transported_units,
        "unit_keys": unit_keys,
        "unit_factors": [unit_factors[key] for key in sorted(unit_factors)],
    }
