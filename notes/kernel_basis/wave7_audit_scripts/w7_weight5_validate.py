#!/usr/bin/env python3
"""w7 audit: run the weight-5 verifier's validate() + mutation controls only
(the C++ replay is done separately in chunks to respect the tiny wall)."""
import copy
import importlib.util
import json
import sys
from pathlib import Path

TREE = Path("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/w7_tree")
VER = TREE / "background/nodes/dli_wcl_weight5_first64_mitm_exclusion/verify.py"

spec = importlib.util.spec_from_file_location("w5verify", VER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

data = json.loads(mod.RESULT.read_text())
rows = mod.validate(data)
assert len(rows) == 64
controls = []
mutations = (
    lambda item: item["composite_witnesses"][0].__setitem__("divisor", "1"),
    lambda item: item["prime_certificates"][0]["witnesses"].__setitem__("2", 1),
    lambda item: item["completed"][0].__setitem__("found", True),
    lambda item: item["completed"][0].__setitem__("triples_checked", mod.TRIPLE_COUNT - 1),
    lambda item: item["primes"].pop(),
)
for mutate in mutations:
    altered = copy.deepcopy(data)
    mutate(altered)
    try:
        mod.validate(altered)
    except (mod.Reject, KeyError, TypeError, ValueError):
        controls.append(True)
    else:
        controls.append(False)
assert all(controls), controls
ks = [int(r["k"]) for r in rows]
print(f"W7_WEIGHT5_VALIDATE_PASS rows=64 k_first={ks[0]} k_last={ks[-1]} "
      f"negative_controls={sum(controls)}/{len(controls)}")
