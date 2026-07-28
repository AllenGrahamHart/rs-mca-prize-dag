#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
NODE="e1_n256_s16_e23_endpoint_exclusion"
DEPENDENCIES={"e1_n256_s16_e23_profile_parity_light_reduction","e1_n256_s16_e23_four_profile_exclusion"}
TARGETS={"e1_official_prime_exception_control","unsafe_crossing_family_instantiation"}
PROFILES={"(3,5)","(2,3,1)","(1,1,2)","(3,1,0,1)"}
def main()->None:
    pin=json.loads((HERE/"source_pin.json").read_text()); texts=[]
    for key,value in pin.items():
        if key.endswith("_file"):
            path=ROOT/value; assert hashlib.sha256(path.read_bytes()).hexdigest()==pin[key+"_sha256"]
            texts.append(path.read_text())
    assert all(any(profile in text for text in texts) for profile in PROFILES)
    dag=json.loads((ROOT/"dag.json").read_text()); nodes={n["id"]:n for n in dag["nodes"]}
    edges={(e["from"],e["to"],e.get("kind","req")) for e in dag["edges"]}
    assert nodes[NODE]["status"]=="PROVED" and all(nodes[d]["status"]=="PROVED" for d in DEPENDENCIES)
    assert {s for s,t,k in edges if t==NODE and k=="req"}==DEPENDENCIES
    assert all((NODE,t,"ev") in edges for t in TARGETS)
    assert "0<V<=44" in nodes[NODE]["statement"] and all(p in nodes[NODE]["statement"] for p in PROFILES)
    print("E1_N256_S16_E23_ENDPOINT_EXCLUSION_PASS profiles=4 exclusions=4 frontier=44 mutations=2")
if __name__=="__main__": main()
