#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
NODE="e1_n256_s16_e21_seven_profile_exclusion"
DEPENDENCIES={"e1_n256_s16_e21_profile_parity_light_reduction",
              "e1_n256_proper_conductor_collision_exclusion","collision_norm_criterion"}
TARGETS={"e1_official_prime_exception_control","unsafe_crossing_family_instantiation"}
PROFILE=[6400,1676,1658,252,348,44,76]
FULL=[3608,488,456,16,68,4,0]
PROPER=[2792,1188,1202,236,280,40,76]
MAXIMUM=1067431210213337343847285566520999617146298326197261566762764923557911188994

def main()->None:
    pin=json.loads((HERE/"source_pin.json").read_text())
    for key,value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT/value).read_bytes()).hexdigest()==pin[key+"_sha256"]
    count=json.loads((ROOT/pin["count_result_file"]).read_text())
    collect=json.loads((ROOT/pin["collect_result_file"]).read_text())
    norm=json.loads((ROOT/pin["norm_result_file"]).read_text())
    assert count["complete"] and count["summary"]["vectors_per_engine"]==2_203_120_896
    assert count["summary"]["profile_counts"]==PROFILE
    assert count["summary"]["full_conductor_counts"]==FULL
    assert count["summary"]["proper_conductor_counts"]==PROPER
    assert collect["complete"] and collect["summary"]["collected_full_conductor"]==4_640
    for key in ("vectors_per_engine","profile_counts","full_conductor_counts","hash_sums","hash_xors"):
        assert collect["summary"][key]==count["summary"][key]
    assert norm["complete"] and norm["agreement"] and norm["vectors"]==4_640
    summary=norm["summary"]
    assert summary["distinct_norms"]==1365 and summary["maximum_norm"]==MAXIMUM
    assert summary["maximum_norm_bits"]==250 and summary["norms_at_or_above_2_250"]==0
    assert summary["maximizing_indices"]==[940,943]
    assert MAXIMUM<2**250<2*MAXIMUM
    markers=((pin["count_checker_file"],"profiles=10454 full=4640"),
             (pin["collect_checker_file"],"matches=4640 profiles=[3608, 488, 456, 16, 68, 4, 0] engines=2"),
             (pin["norm_checker_file"],f"vectors=4640 distinct=1365 max={MAXIMUM} bits=250 hits=0 engines=2 mutations=1"))
    for path,marker in markers:
        run=subprocess.run([sys.executable,str(ROOT/path)],cwd=ROOT,capture_output=True,
                           text=True,timeout=30,check=True); assert marker in run.stdout
    dag=json.loads((ROOT/"dag.json").read_text()); nodes={n["id"]:n for n in dag["nodes"]}
    edges={(e["from"],e["to"],e.get("kind","req")) for e in dag["edges"]}
    assert nodes[NODE]["status"]=="PROVED" and all(nodes[d]["status"]=="PROVED" for d in DEPENDENCIES)
    assert {s for s,t,k in edges if t==NODE and k=="req"}==DEPENDENCIES
    assert all((NODE,t,"ev") in edges for t in TARGETS)
    print("E1_N256_S16_E21_SEVEN_PROFILE_EXCLUSION_PASS templates=111 vectors=2203120896 profile=10454 full=4640 distinct=1365 max_bits=250 engines=6 mutations=3")
if __name__=="__main__": main()
