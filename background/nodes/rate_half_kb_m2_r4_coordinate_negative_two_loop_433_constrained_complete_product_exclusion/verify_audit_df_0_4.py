#!/usr/bin/env python3
from audit_runner import run_shard

checked = run_shard("DF", range(0, 5))
print(f"KB_433_CONSTRAINED_DF_AUDIT_PASS range=0:4 units={checked}")
