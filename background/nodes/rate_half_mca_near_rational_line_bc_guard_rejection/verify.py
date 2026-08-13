#!/usr/bin/env python3
"""Verify the #1160 line rejection by the candidate BC degree guard."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "dccd5b094d00570cca5c6b7453b20d7f190f53d733df2948fabc77c601eabfc0"


class Reject(ValueError):
    pass


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def validate(data: object) -> dict[str, int]:
    if not isinstance(data, dict) or set(data) != {
        "schema",
        "canonical_dossier_commit",
        "upstream",
        "candidate_contract",
        "row",
        "construction",
    }:
        raise Reject("top-level schema")
    if data["schema"] != "rate-half-mca-near-rational-line-bc-guard-rejection-v1":
        raise Reject("schema")
    if data["canonical_dossier_commit"] != "c8d48cd4b94fb256ad9fedfc1d53b4b14c77bfad":
        raise Reject("canonical pin")
    if data["upstream"] != {
        "pr1160_head": "c5f4ea7a0c78828c901ae5f3428894a8b2e2806b",
        "note_blob": "12bc4a0f06189829a9490928e4855d1aa958f940",
        "manifest_blob": "d7442684309e51487a139979332a41c754650609",
        "python_verifier_blob": "3b4533b53e947466de55262e3577108f125738c0",
        "pr1163_head": "e26c15b2d2c2f98ae12dda17b97c40981f76e1ff",
    }:
        raise Reject("upstream pins")
    if data["candidate_contract"] != {
        "local_commit": "80d430a681ee1f823ec1941e8a57a204a73843a0",
        "path": "background/nodes/rate_half_kb_active_balanced_core_witness_compiler/certificate_schema.json",
        "git_blob_sha1": "ced513e99adb807de2dfd621813f0cb6611052d4",
        "sha256": "b0b0711124387038a48c9b5ae1ffbb4b33fdede260b22df2e8c77b84597e06f9",
        "minimum_shifted_degree_guard": 67472,
    }:
        raise Reject("candidate contract pin")

    row = data["row"]
    construction = data["construction"]
    if not isinstance(row, dict) or set(row) != {
        "base_prime",
        "extension_degree",
        "domain_size",
        "code_dimension",
        "effective_locator_dimension",
        "agreement",
        "w",
    }:
        raise Reject("row schema")
    if not isinstance(construction, dict) or set(construction) != {
        "error_set_size",
        "distinct_displayed_slopes",
        "slope_word_support_size",
        "support_locator_degree",
        "expected_accepted_displayed_slopes",
    }:
        raise Reject("construction schema")

    p = integer(row["base_prime"])
    extension = integer(row["extension_degree"])
    n = integer(row["domain_size"])
    k = integer(row["code_dimension"])
    effective_k = integer(row["effective_locator_dimension"])
    m = integer(row["agreement"])
    w = integer(row["w"])
    error_size = integer(construction["error_set_size"])
    slopes = integer(construction["distinct_displayed_slopes"])
    support_size = integer(construction["slope_word_support_size"])
    locator_degree = integer(construction["support_locator_degree"])
    accepted = integer(construction["expected_accepted_displayed_slopes"])
    guard = integer(data["candidate_contract"]["minimum_shifted_degree_guard"])

    if (
        p != 2130706433
        or extension != 6
        or n != 1 << 21
        or k != 1 << 20
        or effective_k != k + 1
        or m != 1116048
        or w != m - k
        or error_size != w
        or slopes != w
        or support_size != w - 1
        or locator_degree != support_size
        or support_size != m - effective_k
        or guard != support_size + 1
        or accepted != 0
        or slopes >= p
    ):
        raise Reject("deployed arithmetic")

    # A small exact model checks the pointwise support-locator identity used
    # in the symbolic proof.  Its size is irrelevant to the deployed count.
    toy_p = 101
    toy_domain = tuple(range(1, 21))
    toy_error = toy_domain[:7]
    toy_slopes = tuple(range(20, 27))
    for index, gamma_i in enumerate(toy_slopes):
        support = set(toy_error)
        support.remove(toy_error[index])
        for x in toy_domain:
            if x in toy_error:
                j = toy_error.index(x)
                word = (gamma_i - toy_slopes[j]) % toy_p
            else:
                word = 0
            locator = 1
            for root in support:
                locator = locator * (x - root) % toy_p
            if locator * word % toy_p != 0:
                raise Reject("support-locator identity")

    return {
        "slopes": slopes,
        "support_size": support_size,
        "guard": guard,
        "accepted": accepted,
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["row"].__setitem__("effective_locator_dimension", 1048576),
        lambda item: item["row"].__setitem__("w", 67471),
        lambda item: item["construction"].__setitem__("slope_word_support_size", 67472),
        lambda item: item["construction"].__setitem__("support_locator_degree", 67472),
        lambda item: item["construction"].__setitem__("distinct_displayed_slopes", 67471),
        lambda item: item["construction"].__setitem__("expected_accepted_displayed_slopes", 1),
        lambda item: item["candidate_contract"].__setitem__("minimum_shifted_degree_guard", 67471),
        lambda item: item["upstream"].__setitem__("manifest_blob", "0" * 40),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")
    print(
        "RATE_HALF_MCA_NEAR_RATIONAL_LINE_BC_GUARD_REJECTION_PASS "
        f"slopes={result['slopes']} shifted_degree_ceiling={result['support_size']} "
        f"bc_guard={result['guard']} accepted={result['accepted']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
