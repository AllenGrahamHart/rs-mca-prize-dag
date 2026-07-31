#!/usr/bin/env python3
import os, runpy
from pathlib import Path
os.environ["MIXED_AUDIT_MODES"] = "field-hp1-l0,field-hp1-q0,field-hp1-q1"
runpy.run_path(str(Path(__file__).with_name("verify_audit.py")), run_name="__main__")
