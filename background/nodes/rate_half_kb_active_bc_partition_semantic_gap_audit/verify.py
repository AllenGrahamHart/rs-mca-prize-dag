#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
contract_path = ROOT / "background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json"
contract = json.loads(contract_path.read_text())
bc = next(stage for stage in contract["chronology_stages"] if stage["atom_id"] == "U_BC")

assert bc["predicate_available"] is True
assert bc["predicate"] == "BAD_SLOPE_NOT_EARLIER_AND_HAS_ACTIVE_V4_BALANCED_CORE_CERTIFICATE"
assert not any(key in bc for key in ("witness_schema", "certificate_fields", "endpoint_map", "fiber_bound"))

universe = {"z"}
bad = {"z"}
tangent = set()
q_certified = set()
bc_certified = {"z"}
z_paid = bad & tangent
r1 = bad - z_paid
z_q = r1 & q_certified
r2 = r1 - z_q
z_bc = r2 & bc_certified
z_new = r2 - z_bc
cells = (z_paid, z_q, z_bc, z_new)

assert set().union(*cells) == bad == universe
assert sum(len(cell) for cell in cells) == len(bad)
assert z_bc == {"z"}
endpoint_records = set()
assert z_bc and not endpoint_records

for path, phrases in {
    ROOT / "background/nodes/rate_half_kb_decomposition_source_pencil_compiler/statement.md":
        ("endpoint parameter line is not the evaluation carrier", "no parameter-to-carrier bridge"),
    ROOT / "background/nodes/rate_half_kb_source_pencil_rank_transverse_compiler/statement.md":
        ("per supplied record", "No global endpoint census"),
}.items():
    text = path.read_text()
    for phrase in phrases:
        assert phrase in text, (path, phrase)

print("PASS active-BC semantic gap one_slope_countermodel=1 endpoint_records=0")
