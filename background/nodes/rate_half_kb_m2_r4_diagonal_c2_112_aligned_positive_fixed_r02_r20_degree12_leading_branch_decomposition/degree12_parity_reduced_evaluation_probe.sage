#!/usr/bin/env sage
"""Use U^2=VZ before expanding the remaining-row evaluations."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", default="F04-R02")
    parser.add_argument("--prime", type=int, default=2130706433)
    parser.add_argument("--stop-after-parity", action="store_true")
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    x, s, p = base.gens()
    U = branch["equations"]["U"]
    V = branch["equations"]["V"]
    Z = branch["equations"]["Z"]
    R = branch["equations"]["R"]
    remaining_rows = branch["converted"][2:]

    def metric(value, generators):
        value = value.parent()(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in generators],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    def parity_clear(poly):
        degree = int(poly.degree())
        output = base(0)
        for index in range(degree + 1):
            coefficient = base(poly[index])
            half = index // 2
            if index % 2 == 0:
                output += coefficient * V ** (degree - half) * Z ** half
            else:
                output -= coefficient * U * V ** (degree - half - 1) * Z ** half
        return base(output)

    parity = [parity_clear(row) for row in remaining_rows]
    direct = [branch["equations"]["E2"], branch["equations"]["E3"]]
    parity_metrics = [metric(value, (x, s, p)) for value in parity]
    print(
        canonical_json(
            {
                "phase": "PARITY_COMPILED",
                "blocks": {
                    name: metric(value, (x, s, p))
                    for name, value in (("U", U), ("V", V), ("Z", Z), ("R", R))
                },
                "direct": [metric(value, (x, s, p)) for value in direct],
                "parity": parity_metrics,
            }
        ),
        flush=True,
    )
    if args.stop_after_parity:
        print(
            canonical_json(
                {
                    "phase": "DONE",
                    "cell": args.cell,
                    "parity": parity_metrics,
                    "terminal": "DEGREE12_PARITY_REPRESENTATIVES_COMPILED",
                }
            ),
            flush=True,
        )
        return

    print(canonical_json({"phase": "CONGRUENCE_BEGIN"}), flush=True)
    congruence_remainders = [base(direct[index] - parity[index]).reduce([R]) for index in range(2)]
    print(
        canonical_json(
            {
                "phase": "CONGRUENCE_DONE",
                "zero": [not bool(value) for value in congruence_remainders],
                "metrics": [metric(value, (x, s, p)) for value in congruence_remainders],
            }
        ),
        flush=True,
    )
    assert not any(congruence_remainders)

    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    selected = r_factors[2]
    degree_x = int(selected.degree(x))
    selected_leading = base(
        sum(
            QQ(coefficient) * s ** monomial[1] * p ** monomial[2]
            for monomial, coefficient in selected.dict().items()
            if monomial[0] == degree_x
        )
    )
    degree6_candidates = [
        factor for factor, _ in selected_leading.factor()
        if factor.total_degree() == 6
    ]
    assert len(degree6_candidates) == 1
    degree6 = degree6_candidates[0]

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")
    rx, rs, rp = ring.gens()

    def convert(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * rx ** monomial[0] * rs ** monomial[1] * rp ** monomial[2]
        return output

    generators = [convert(selected), convert(parity[0]), convert(parity[1])]
    print(
        canonical_json(
            {
                "phase": "GROEBNER_BEGIN",
                "generators": [metric(value, (rx, rs, rp)) for value in generators],
            }
        ),
        flush=True,
    )
    basis = list(ring.ideal(generators).groebner_basis(algorithm="singular:slimgb"))
    unit_ideal = basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(basis).dimension())
    print(
        canonical_json(
            {
                "phase": "GROEBNER_DONE",
                "unit_ideal": unit_ideal,
                "dimension": dimension,
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
                "basis_metrics": [metric(value, (rx, rs, rp)) for value in basis],
            }
        ),
        flush=True,
    )

    localizer_factors = [("prior_s", ring(rs)), ("prior_L6", convert(degree6))]
    localizer_factors.extend(
        (f"unit_{index}", convert(factor))
        for index, factor in enumerate(branch["unit_factors"], start=1)
    )
    localizer = ring(1)
    steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, (label, factor) in enumerate(localizer_factors, start=1):
            localizer = (localizer * factor).reduce(basis)
            steps.append(
                {
                    "index": index,
                    "label": label,
                    "zero": not bool(localizer),
                    "metric": metric(localizer, (rx, rs, rp)),
                }
            )
            if not localizer:
                nilpotence_index = 1
                break

    terminal = (
        "DEGREE12_PARITY_GENERIC_EMPTY"
        if nilpotence_index is not None
        else "DEGREE12_PARITY_GENERIC_SURVIVES"
    )
    print(
        canonical_json(
            {
                "phase": "DONE",
                "cell": args.cell,
                "selected_sha256": digest(selected),
                "parity_sha256": [digest(value) for value in parity],
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
                "dimension": dimension,
                "unit_ideal": unit_ideal,
                "localizer_steps": steps,
                "localizer_nilpotence_index": nilpotence_index,
                "terminal": terminal,
            }
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
