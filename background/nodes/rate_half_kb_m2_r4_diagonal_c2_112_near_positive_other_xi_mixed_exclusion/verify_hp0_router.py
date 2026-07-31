#!/usr/bin/env python3
import os, runpy
from pathlib import Path
os.environ["MIXED_PRIMARY_MODES"] = "high-p0"
runpy.run_path(str(Path(__file__).with_name("verify.py")), run_name="__main__")
