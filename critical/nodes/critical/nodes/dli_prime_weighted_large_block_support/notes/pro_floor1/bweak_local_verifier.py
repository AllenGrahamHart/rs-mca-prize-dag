#!/usr/bin/env python3
# CATCH #41 (2026-07-10 amber audit): this file was banked as "Pro's
# Floor-1 verifier, saved verbatim from the relay" but contained NO BODY —
# a false artifact citation in the survival ledger (same failure shape as
# catches #33/#35/#36: existence claims unchecked). The SURVIVAL +4 spike
# itself is real: independently reconstructed and replayed 2026-07-10
# (q=15,249,281 prime, ord(omega)=128, 256 signed weight-5 vanishers,
# K = 16.000270 vs claimed 16.0003). The working replay is
# bweak_spike_replay_restored_20260710.py in this directory; run that.
import pathlib, runpy, sys
sys.exit(runpy.run_path(pathlib.Path(__file__).with_name(
    "bweak_spike_replay_restored_20260710.py")) and 0)
