#!/usr/bin/env python3
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())
schema = json.loads((HERE / "certificate_schema.json").read_text())
row = schema["row"]

assert node["node"]["status"] == "PROVED"
assert row["domain_size"] - row["agreement"] == row["locator_degree"] == 981104
assert row["agreement"] - row["effective_mca_locator_dimension"] == row["balanced_depth"] == 67471
assert row["effective_mca_locator_dimension"] == row["code_dimension"] + 1
assert schema["predicate_semantics"]["definition"] == "EXISTS_VALID_CERTIFICATE"
assert schema["predicate_semantics"]["balanced_profile"].endswith("PLUS_ONE")
assert len(schema["required_fields"]) == len(set(schema["required_fields"])) == 12
assert len(schema["guards"]) == len(set(schema["guards"])) == 10

selector = schema["canonical_selector"]
assert selector["selected_per_active_slope"] == 1
assert selector["selected_certificate_to_slope_fiber"] == 1
assert selector["slope_to_selected_certificate_fiber"] == 1

proof = (HERE / "proof.md").read_text()
for token in ("bcCertified(line,z)", "d1>=w+1", "unique least member", "bijection"):
    assert token in proof

print("PASS active-BC witness compiler omega=981104 w=67471 selector_fiber=1")
