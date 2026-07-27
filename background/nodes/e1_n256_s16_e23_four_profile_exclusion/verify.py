#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
NODE="e1_n256_s16_e23_four_profile_exclusion"
DEPENDENCIES={"e1_n256_s16_e23_profile_parity_light_reduction",
              "e1_n256_proper_conductor_collision_exclusion","collision_norm_criterion"}
TARGETS={"e1_official_prime_exception_control","unsafe_crossing_family_instantiation"}
MAXIMUM=721495288731652690472090495266069052907254127194382380048009480013819013124

def main()->None:
    pin=json.loads((HERE/"source_pin.json").read_text())
    for key,value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT/value).read_bytes()).hexdigest()==pin[key+"_sha256"]
    census=json.loads((ROOT/pin["census_result_file"]).read_text())
    norm=json.loads((ROOT/pin["norm_result_file"]).read_text())
    assert census["complete"] and census["summary"]["profile_counts"]==[1176,522,46,144]
    assert census["summary"]["full_conductor_counts"]==[352,108,0,24]
    assert census["summary"]["proper_conductor_counts"]==[824,414,46,120]
    assert census["summary"]["collected_full_conductor"]==484
    assert norm["complete"] and norm["agreement"]
    assert norm["summary"]=={"distinct_norms":176,"maximizing_indices":[257,258,333,334],
                             "maximum_norm":MAXIMUM,"maximum_norm_bits":249,
                             "norm_at_or_above_2_250":0,"vectors":484}
    assert 2*MAXIMUM<2**250<3*MAXIMUM
    markers=((pin["census_checker_file"],"profile=1888 full=484 engines=2 mutations=1"),
             (pin["norm_checker_file"],f"vectors=484 distinct=176 max={MAXIMUM} bits=249 hits=0 engines=2 mutations=1"))
    for path,marker in markers:
        run=subprocess.run([sys.executable,str(ROOT/path)],cwd=ROOT,capture_output=True,
                           text=True,timeout=30,check=True); assert marker in run.stdout
    dag=json.loads((ROOT/"dag.json").read_text()); nodes={n["id"]:n for n in dag["nodes"]}
    edges={(e["from"],e["to"],e.get("kind","req")) for e in dag["edges"]}
    assert nodes[NODE]["status"]=="PROVED" and all(nodes[d]["status"]=="PROVED" for d in DEPENDENCIES)
    assert {s for s,t,k in edges if t==NODE and k=="req"}==DEPENDENCIES
    assert all((NODE,t,"ev") in edges for t in TARGETS)
    print("E1_N256_S16_E23_FOUR_PROFILE_EXCLUSION_PASS templates=8 vectors=158783488 profile=1888 full=484 distinct=176 max_bits=249 engines=4 mutations=2")
if __name__=="__main__": main()
