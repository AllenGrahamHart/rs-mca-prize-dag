#!/usr/bin/env python3
"""Verify the cutoff-free E23 profile/parity router."""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
NODE="e1_n256_s16_e23_profile_parity_light_reduction"
DEPENDENCIES={"e1_n256_s16_e24_endpoint_exclusion","e1_n256_s16_sparse_l1_variance_exclusion",
              "e1_n256_s16_signed_chord_collision_gate","e1_n256_s16_e27_profile_parity_light_reduction",
              "collision_norm_criterion"}
EXCLUSION="e1_n256_s16_e23_four_profile_exclusion"
TARGETS={"e1_official_prime_exception_control","unsafe_crossing_family_instantiation"}
PROFILES={(3,5,0,0,0),(2,3,1,0,0),(1,1,2,0,0),(3,1,0,1,0)}

def main()->None:
    pin=json.loads((HERE/"source_pin.json").read_text())
    for key,value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT/value).read_bytes()).hexdigest()==pin[key+"_sha256"]
    packet=json.loads((ROOT/pin["probe_result_file"]).read_text())
    assert packet["complete"] and packet["variance"]==46 and packet["energy"]==23
    assert packet["l1_bound"]==13 and packet["profile_count"]==7 and packet["majorant_filter"] is None
    assert {tuple(row["profile"]) for row in packet["parity_survivors"]}==PROFILES
    assert len(packet["parity_rejected"])==3
    assert packet["relevant_affine_templates"]==8 and packet["direct_vector_floor"]==158_783_488
    run=subprocess.run([sys.executable,str(ROOT/pin["probe_checker_file"])],cwd=ROOT,
                       capture_output=True,text=True,timeout=30,check=True)
    assert "l1=13 profiles=7 survivors=4 templates=8 floor=158783488" in run.stdout
    dag=json.loads((ROOT/"dag.json").read_text()); nodes={n["id"]:n for n in dag["nodes"]}
    edges={(e["from"],e["to"],e.get("kind","req")) for e in dag["edges"]}
    assert nodes[NODE]["status"]=="PROVED" and all(nodes[d]["status"]=="PROVED" for d in DEPENDENCIES)
    assert {s for s,t,k in edges if t==NODE and k=="req"}==DEPENDENCIES
    assert (NODE,EXCLUSION,"req") in edges and all((NODE,t,"ev") in edges for t in TARGETS)
    print("E1_N256_S16_E23_PROFILE_PARITY_LIGHT_REDUCTION_PASS l1=13 profiles=7 survivors=4 templates=8 floor=158783488 mutations=1")

if __name__=="__main__": main()
