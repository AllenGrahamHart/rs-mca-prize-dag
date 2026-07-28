#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main()->None:
    for path in ("experiments/prize_resolution/e21_seven_profile_count_check.py",
                 "experiments/prize_resolution/e21_seven_profile_collect_check.py",
                 "experiments/prize_resolution/e21_seven_profile_norm_check.py"):
        subprocess.run([sys.executable,path],cwd=ROOT,capture_output=True,text=True,timeout=30,check=True)
    print("E1_N256_S16_E21_SEVEN_PROFILE_EXCLUSION_AUDIT_PASS checkers=3 engines=6 mutations=3")
if __name__=="__main__": main()
