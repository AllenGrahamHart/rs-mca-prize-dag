#!/usr/bin/env python3
import os, runpy
from pathlib import Path
os.environ["MIXED_AUDIT_MODES"] = "field-low-d17,field-low-q3-l,field-low-q3-q"
runpy.run_path(str(Path(__file__).with_name("verify_audit.py")), run_name="__main__")
