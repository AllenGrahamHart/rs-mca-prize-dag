#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main()->None:
    for path,marker in (("experiments/prize_resolution/e22_eight_profile_count_check.py","profiles=27998 full=15002"),
                        ("experiments/prize_resolution/e22_eight_profile_collect_check.py","matches=15002"),
                        ("experiments/prize_resolution/e22_eight_profile_norm_check.py","vectors=15002 distinct=5991")):
        run=subprocess.run([sys.executable,path],cwd=ROOT,capture_output=True,text=True,timeout=30,check=True)
        assert marker in run.stdout
    print("E1_N256_S16_E22_EIGHT_PROFILE_EXCLUSION_AUDIT_PASS checkers=3 engines=6 mutations=4")
if __name__=="__main__": main()
