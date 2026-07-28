#!/usr/bin/env python3
"""Compute dual exact cyclotomic norms for the full E23 residue."""

from __future__ import annotations

import hashlib,json
from pathlib import Path
import modal

HERE=Path(__file__).resolve().parent
CENSUS=HERE/"e23_four_profile_census_result.json"
RESULT=HERE/"e23_four_profile_norm_result.json"
BATCH_SIZE=16
app=modal.App("e1-n256-e23-four-profile-norm")
image=modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image,cpu=1.0,memory=256,timeout=120,max_containers=32)
def run_flint(batch:int,vectors:list[dict[str,object]])->dict[str,object]:
    import time
    from flint import fmpz_poly
    started=time.monotonic(); cyclotomic=fmpz_poly([1]+[0]*127+[1]); norms=[]
    for vector in vectors:
        positions=[int(v) for v in vector["positions"]]
        dense=[0]*(max(positions)+1)
        for position,coefficient in zip(positions,vector["coefficients"]):
            dense[position]=int(coefficient)
        norms.append(abs(int(cyclotomic.resultant(fmpz_poly(dense)))))
    return {"batch":batch,"norms":norms,"worker_seconds":time.monotonic()-started}


@app.function(image=image,cpu=1.0,memory=256,timeout=120,max_containers=32)
def run_pari(batch:int,vectors:list[dict[str,object]])->dict[str,object]:
    import subprocess,time
    started=time.monotonic(); script=[]
    for vector in vectors:
        terms=[f"({int(c)})*x^{int(p)}" for p,c in zip(vector["positions"],vector["coefficients"])]
        script.append(f"print(abs(polresultant(x^128+1,{'+'.join(terms)})));")
    completed=subprocess.run(["gp","-q"],input="\n".join(script)+"\n",
                             capture_output=True,check=True,text=True,timeout=110)
    return {"batch":batch,"norms":[int(line) for line in completed.stdout.splitlines() if line.strip()],
            "worker_seconds":time.monotonic()-started}


@app.local_entrypoint()
def main()->None:
    census=json.loads(CENSUS.read_text())
    if not census["complete"]: raise RuntimeError("E23 census is incomplete")
    vectors=[match for row in census["rows"] for match in row["primary"]["matches"]]
    if len(vectors)!=census["summary"]["collected_full_conductor"]:
        raise RuntimeError("E23 full-conductor count mismatch")
    batches=[vectors[start:start+BATCH_SIZE] for start in range(0,len(vectors),BATCH_SIZE)]
    indices=list(range(len(batches))); flint_rows=[]; pari_rows=[]
    def flatten(rows):
        return [int(norm) for row in sorted(rows,key=lambda item:int(item["batch"])) for norm in row["norms"]]
    def checkpoint(complete:bool):
        flint=flatten(flint_rows); pari=flatten(pari_rows)
        agreement=len(flint)==len(vectors) and flint==pari
        packet={"schema":"e1-e23-four-profile-norm-v1","complete":complete,"agreement":agreement,
                "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "census_sha256":hashlib.sha256(CENSUS.read_bytes()).hexdigest(),
                "batch_size":BATCH_SIZE,"expected_batches":len(batches),
                "completed_flint_batches":len(flint_rows),"completed_pari_batches":len(pari_rows),
                "vectors":vectors,"flint_norms":flint,"pari_norms":pari,
                "flint_worker_seconds":sum(float(row["worker_seconds"]) for row in flint_rows),
                "pari_worker_seconds":sum(float(row["worker_seconds"]) for row in pari_rows)}
        if agreement:
            maximum=max(flint)
            packet["summary"]={"vectors":len(vectors),"distinct_norms":len(set(flint)),
                               "maximum_norm":maximum,"maximum_norm_bits":maximum.bit_length(),
                               "norm_at_or_above_2_250":sum(value>=2**250 for value in flint),
                               "maximizing_indices":[i for i,value in enumerate(flint) if value==maximum]}
        RESULT.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n")
        return packet
    checkpoint(False)
    try:
        for row in run_flint.map(indices,batches): flint_rows.append(row)
        checkpoint(False)
        for row in run_pari.map(indices,batches): pari_rows.append(row)
    except BaseException:
        checkpoint(False)
        print(f"E23_FOUR_PROFILE_NORM_INCOMPLETE flint={len(flint_rows)}/{len(batches)} pari={len(pari_rows)}/{len(batches)}")
        raise
    packet=checkpoint(len(flint_rows)==len(batches) and len(pari_rows)==len(batches) and flatten(flint_rows)==flatten(pari_rows))
    print("E23_FOUR_PROFILE_NORM "+json.dumps(packet["summary"],sort_keys=True))
    print(f"E23_FOUR_PROFILE_NORM_AGREEMENT {packet['agreement']}")
    print(f"E23_FOUR_PROFILE_NORM_RESULT {RESULT}")
