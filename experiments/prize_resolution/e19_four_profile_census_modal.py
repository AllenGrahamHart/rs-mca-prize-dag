#!/usr/bin/env python3
"""Run dual complete E19 four-profile censuses on Modal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE=Path(__file__).resolve().parent
PRIMARY=HERE/"e19_four_profile_census.cpp"
AUDIT=HERE/"e19_four_profile_census_audit.cpp"
PROBE=HERE/"e19_profile_parity_probe_result.json"
RESULT=HERE/"e19_four_profile_census_result.json"
REMOTE_PRIMARY_SOURCE="/root/e19_four_profile_census.cpp"
REMOTE_AUDIT_SOURCE="/root/e19_four_profile_census_audit.cpp"
REMOTE_PRIMARY="/root/e19_four_profile_census"
REMOTE_AUDIT="/root/e19_four_profile_census_audit"

app=modal.App("e1-n256-e19-four-profile-census")
image=(modal.Image.debian_slim().apt_install("g++")
       .add_local_file(PRIMARY,REMOTE_PRIMARY_SOURCE,copy=True)
       .add_local_file(AUDIT,REMOTE_AUDIT_SOURCE,copy=True)
       .run_commands(
           f"g++ -O3 -std=c++17 {REMOTE_PRIMARY_SOURCE} -o {REMOTE_PRIMARY}",
           f"g++ -O3 -std=c++17 {REMOTE_AUDIT_SOURCE} -o {REMOTE_AUDIT}"))


@app.function(image=image,cpu=1.0,memory=256,timeout=60,max_containers=8)
def run_template(template:int,light:list[int])->dict[str,object]:
    import json as remote_json
    import subprocess,time
    started=time.monotonic()
    tail=[str(template),*(str(value) for value in light)]
    primary=remote_json.loads(subprocess.run(
        [REMOTE_PRIMARY,*tail],check=True,capture_output=True,text=True,timeout=27).stdout)
    audit=remote_json.loads(subprocess.run(
        [REMOTE_AUDIT,*tail],check=True,capture_output=True,text=True,timeout=27).stdout)
    if primary!=audit:
        raise RuntimeError(f"engine disagreement at template {template}")
    return {"template":template,"primary":primary,"audit":audit,
            "worker_seconds":time.monotonic()-started}


@app.local_entrypoint()
def main()->None:
    probe=json.loads(PROBE.read_text())
    if not probe["complete"] or int(probe["relevant_affine_templates"])!=8:
        raise RuntimeError("E19 router is incomplete or changed")
    root=HERE.parents[1]
    atlas_path=(root/"background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"/
                "e27_profile_parity_probe_result.json")
    atlas=json.loads(atlas_path.read_text())
    tasks=list(atlas["light_geometry"]["orbit_representatives"]["3"])
    if len(tasks)!=8:
        raise RuntimeError("three-odd atlas mismatch")
    rows=[]
    def vector_sum(key:str)->list[int]:
        return [sum(int(row["primary"][key][i]) for row in rows) for i in range(4)]
    def write_checkpoint(complete:bool,error:str|None=None)->dict[str,object]:
        profile=vector_sum("profile_counts")
        full=vector_sum("full_conductor_counts")
        packet={
            "schema":"e1-e19-four-profile-census-v1","complete":complete,
            "completed_templates":len(rows),"expected_templates":len(tasks),"error":error,
            "primary_source_sha256":hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
            "audit_source_sha256":hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
            "probe_sha256":hashlib.sha256(PROBE.read_bytes()).hexdigest(),
            "atlas_sha256":hashlib.sha256(atlas_path.read_bytes()).hexdigest(),
            "summary":{"vectors_per_engine":sum(int(row["primary"]["vectors"]) for row in rows),
                       "profile_counts":profile,"full_conductor_counts":full,
                       "proper_conductor_counts":[profile[i]-full[i] for i in range(4)],
                       "collected_full_conductor":sum(len(row["primary"]["matches"]) for row in rows),
                       "worker_seconds_dual":sum(float(row["worker_seconds"]) for row in rows)},
            "rows":sorted(rows,key=lambda row:int(row["template"]))}
        RESULT.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n")
        return packet
    write_checkpoint(False)
    try:
        for row in run_template.map(range(8),tasks):
            rows.append(row); write_checkpoint(False)
    except BaseException as error:
        write_checkpoint(False,f"{type(error).__name__}: {error}")
        print(f"E19_FOUR_PROFILE_CENSUS_INCOMPLETE completed={len(rows)}/8")
        raise
    packet=write_checkpoint(
        len(rows)==8 and all(row["primary"]==row["audit"] for row in rows)
        and sum(int(row["primary"]["vectors"]) for row in rows)==int(probe["direct_vector_floor"]))
    print("E19_FOUR_PROFILE_CENSUS "+json.dumps(packet["summary"],sort_keys=True))
    print(f"E19_FOUR_PROFILE_CENSUS_COMPLETE {packet['complete']}")
    print(f"E19_FOUR_PROFILE_CENSUS_RESULT {RESULT}")
