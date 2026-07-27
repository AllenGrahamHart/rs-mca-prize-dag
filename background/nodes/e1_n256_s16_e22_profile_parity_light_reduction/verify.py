#!/usr/bin/env python3
"""Verify the cutoff-free E22 profile/parity router."""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
NODE="e1_n256_s16_e22_profile_parity_light_reduction"
DEPENDENCIES={"e1_n256_s16_e23_endpoint_exclusion","e1_n256_s16_sparse_l1_variance_exclusion",
              "e1_n256_s16_signed_chord_collision_gate","e1_n256_s16_e26_profile_parity_light_reduction",
              "collision_norm_criterion"}
EXCLUSION="e1_n256_s16_e22_eight_profile_exclusion"
TARGETS={"e1_official_prime_exception_control","unsafe_crossing_family_instantiation"}
PROFILES={(6,4,0,0,0),(2,5,0,0,0),(5,2,1,0,0),(1,3,1,0,0),
          (4,0,2,0,0),(0,1,2,0,0),(6,0,0,1,0),(2,1,0,1,0)}

def main()->None:
    pin=json.loads((HERE/"source_pin.json").read_text())
    for key,value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT/value).read_bytes()).hexdigest()==pin[key+"_sha256"]
    packet=json.loads((ROOT/pin["probe_result_file"]).read_text())
    assert packet["complete"] and packet["variance"]==44 and packet["energy"]==22
    assert packet["l1_bound"]==14 and packet["profile_count"]==9 and packet["majorant_filter"] is None
    assert {tuple(row["profile"]) for row in packet["parity_survivors"]}==PROFILES
    assert len(packet["parity_rejected"])==1
    assert packet["used_odd_counts"]==["2","6"]
    assert packet["relevant_affine_templates"]==1321
    assert packet["direct_vector_floor"]==26_219_123_456
    assert packet["diameter_ledgers"]=={
        "zero_light_diameters":[[0,-40],[4,-38],[8,-36],[12,-34],[16,-32],[20,-30]],
        "two_light_diameters":[[2,-39],[18,-31]],
    }
    run=subprocess.run([sys.executable,str(ROOT/pin["probe_checker_file"])],cwd=ROOT,
                       capture_output=True,text=True,timeout=30,check=True)
    assert "l1=14 profiles=9 survivors=8 templates=1321 floor=26219123456" in run.stdout
    dag=json.loads((ROOT/"dag.json").read_text()); nodes={n["id"]:n for n in dag["nodes"]}
    edges={(e["from"],e["to"],e.get("kind","req")) for e in dag["edges"]}
    assert nodes[NODE]["status"]=="PROVED" and all(nodes[d]["status"]=="PROVED" for d in DEPENDENCIES)
    assert {s for s,t,k in edges if t==NODE and k=="req"}==DEPENDENCIES
    assert (NODE,EXCLUSION,"req") in edges and all((NODE,t,"ev") in edges for t in TARGETS)
    print("E1_N256_S16_E22_PROFILE_PARITY_LIGHT_REDUCTION_PASS l1=14 profiles=9 survivors=8 templates=1321 floor=26219123456 mutations=2")

if __name__=="__main__": main()
