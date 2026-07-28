#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main()->None:
    for path,marker in (("experiments/prize_resolution/e23_four_profile_census_check.py","profile=1888 full=484"),
                        ("experiments/prize_resolution/e23_four_profile_norm_check.py","vectors=484 distinct=176")):
        run=subprocess.run([sys.executable,path],cwd=ROOT,capture_output=True,text=True,timeout=30,check=True)
        assert marker in run.stdout
    print("E1_N256_S16_E23_FOUR_PROFILE_EXCLUSION_AUDIT_PASS checkers=2 engines=4 mutations=2")
if __name__=="__main__": main()
