#!/usr/bin/env python3
import os, runpy
from pathlib import Path
os.environ["MOVING_A_MIXED_PRIMARY_MODE"] = "pairs"
runpy.run_path(str(Path(__file__).with_name("verify.py")), run_name="__main__")
