#!/usr/bin/env python3
from audit_runner import run_shard

checked = run_shard("DF", range(10, 15))
print(f"KB_433_M2_M3_DF_AUDIT_PASS range=10:14 units={checked}")
