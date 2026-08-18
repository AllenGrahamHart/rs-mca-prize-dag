#!/usr/bin/env python3
"""Assemble every exceptional polynomial used by the generic FFF proof."""

import hashlib
import json


PRIME = 2130706433
GROUP_LABELS = [
    "generic_basis_denominators",
    "q5_coefficient_denominators",
    "q5_extension_denominators",
    "q5_multiplication_denominators",
    "q7_coefficient_denominators",
    "r76_column_lcms",
    "r76_determinant",
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def deduplicate(polynomials):
    output = []
    seen = set()
    for values in polynomials:
        require(values and all(isinstance(value, int) for value in values) and
                any(value % PRIME for value in values), "polynomial")
        normalized = tuple(value % PRIME for value in values)
        while len(normalized) > 1 and normalized[-1] == 0:
            normalized = normalized[:-1]
        if normalized not in seen:
            seen.add(normalized)
            output.append(list(normalized))
    return output


def build(generic, frontier, c1, q5, multiplication, q7, polynomial, determinant):
    require(generic["collection_complete"] is True and
            generic["row"]["status"] == "COMPLETE", "generic")
    require(frontier["collection_complete"] is True and
            [row["coefficient_index"] for row in frontier["rows"]] == [0, 1, 2] and
            frontier["rows"][0]["status"] == frontier["rows"][2]["status"] ==
            "COMPLETE", "q5 frontier")
    require(c1["collection_complete"] is True and c1["row"]["status"] == "COMPLETE"
            and c1["row"]["coefficient_index"] == 1, "q5 c1")
    for payload, label in ((q5, "q5 extension"),
                           (multiplication, "q5 multiplication"),
                           (q7, "q7 coefficients"),
                           (polynomial, "polynomial matrix"),
                           (determinant, "determinant")):
        require(payload["collection_complete"] is True and
                payload["row"]["status"] == "COMPLETE", label)

    q5_coefficients = []
    for row in (frontier["rows"][0], c1["row"], frontier["rows"][2]):
        q5_coefficients.extend(row["unique_denominators"])
    multiplication_denominators = [
        entry["denominator"] for entry in multiplication["row"]["matrix_entries"]
    ] + [
        entry["denominator"] for entry in multiplication["row"]["kernel_entries"]
    ]
    groups = [
        (GROUP_LABELS[0], generic["row"]["unique_denominators"]),
        (GROUP_LABELS[1], q5_coefficients),
        (GROUP_LABELS[2], q5["row"]["unique_denominators"]),
        (GROUP_LABELS[3], multiplication_denominators),
        (GROUP_LABELS[4], q7["row"]["unique_denominators"]),
        (GROUP_LABELS[5], [item["coefficients"]
                           for item in polynomial["row"]["column_lcms"]]),
        (GROUP_LABELS[6], [determinant["row"]["determinant_coefficients"]]),
    ]
    rows = []
    for label, values in groups:
        unique = deduplicate(values)
        rows.append({
            "label": label,
            "raw_count": len(values),
            "polynomials": unique,
            "polynomial_count": len(unique),
            "polynomials_sha256": hashlib.sha256(
                json.dumps(unique, separators=(",", ":")).encode()
            ).hexdigest(),
        })
    require([row["label"] for row in rows] == GROUP_LABELS, "group order")
    return {
        "groups": rows,
        "relation": "complete generic FFF exceptional-polynomial ledger",
        "method": "LCM union then gcd(H,t^p-t) over the base field",
        "field": PRIME,
        "group_labels": GROUP_LABELS,
        "raw_polynomial_count": sum(row["raw_count"] for row in rows),
        "group_unique_polynomial_count": sum(row["polynomial_count"] for row in rows),
        "source_generic_denominators_sha256":
            generic["row"]["unique_denominators_sha256"],
        "source_q5_extension_denominators_sha256":
            q5["row"]["unique_denominators_sha256"],
        "source_q5_matrix_entries_sha256":
            multiplication["row"]["matrix_entries_sha256"],
        "source_q5_kernel_entries_sha256":
            multiplication["row"]["kernel_entries_sha256"],
        "source_q7_denominators_sha256":
            q7["row"]["unique_denominators_sha256"],
        "source_column_lcms_sha256": polynomial["row"]["column_lcms_sha256"],
        "source_determinant_sha256":
            determinant["row"]["determinant_coefficients_sha256"],
    }


if __name__ == "__main__":
    require(deduplicate([[1, 0], [1], [0, PRIME + 2]]) == [[1], [0, 2]],
            "deduplication self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_EXCEPTIONAL_ROOTS_PROGRAM_PASS "
          "groups=7")
