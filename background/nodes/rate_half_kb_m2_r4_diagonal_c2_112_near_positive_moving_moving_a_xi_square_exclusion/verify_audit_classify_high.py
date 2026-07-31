#!/usr/bin/env python3
import os, runpy
from pathlib import Path
os.environ["MOVING_A_SQUARE_AUDIT_MODE"] = "classify-high"
runpy.run_path(str(Path(__file__).with_name("verify_audit.py")), run_name="__main__")
