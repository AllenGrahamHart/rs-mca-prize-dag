#!/usr/bin/env python3
"""E22 correctness gate (LOCAL, light).

STEP 2 of the E22 task: reproduce the E15 (#197) phenomenon at the documented
toy cell BEFORE launching any census.  The gate PASSES iff an exhaustive search
at sigma=1 in the n=16 toy cell finds a NON-planted structured challenger whose
list count beats the planted count (list_size > M) at the crossing radius s.

This is intentionally tiny (a handful of n=16 exact cells) so it runs locally
in a couple of seconds with no heavy compute.  A benchmark at the end sizes the
per-cell exhaustive cap for the Modal census.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e22_core import exact_cell_census, sunflower_word, polynomial_through, P  # noqa: E402

LAYOUT = "cyclic_step_1"
SCALAR = "linear"


def run_gate() -> bool:
    print("== E22 correctness gate: reproduce E15 (#197) sigma=1 challenger ==")
    print(f"toy cell: F_{P} subgroup domain, n=16, layout={LAYOUT}, scalar={SCALAR}\n")
    print(f"{'k':>3} {'sig':>3} {'s':>3} {'M':>4} {'list':>5} {'chal':>4} "
          f"{'uncl':>4} {'beats':>5}  class_counts")
    any_challenger = False
    # k=1 is the negative control (no challenger expected); k in {2,4,8} beat.
    for k in (1, 2, 4, 8):
        cell = exact_cell_census(16, k, 1, LAYOUT, SCALAR)
        beats = cell["beats_planted"]
        chal = cell["classified_challenger"]
        uncl = cell["unclassified"]
        if chal > 0 and beats:
            any_challenger = True
        print(f"{k:>3} {1:>3} {cell['s']:>3} {cell['planted_count']:>4} "
              f"{cell['list_size']:>5} {chal:>4} {uncl:>4} {str(beats):>5}  "
              f"{cell['class_counts']}")
    # sigma>=2 control: planted should remain worst (no challenger) at n=16.
    print()
    for k in (2, 4, 8):
        cell = exact_cell_census(16, k, 2, LAYOUT, SCALAR)
        print(f"  control k={k} sigma=2: list={cell['list_size']} "
              f"M={cell['planted_count']} chal={cell['classified_challenger']} "
              f"beats={cell['beats_planted']}")
    return any_challenger


def benchmark_interp() -> None:
    print("\n== interpolation-cost benchmark (sizes the Modal exhaustive cap) ==")
    for (n, k, sigma) in [(16, 8, 3), (32, 8, 3), (64, 16, 3)]:
        word = sunflower_word(n, k, sigma, LAYOUT, SCALAR)
        s = word["s"]
        import itertools
        combos = itertools.combinations(range(n), s)
        t0 = time.time()
        count = 0
        for indices in combos:
            polynomial_through(list(indices), word["domain"], word["values"], word["k"])
            count += 1
            if count >= 20000:
                break
        dt = time.time() - t0
        per = dt / count
        print(f"  n={n} k={k} sigma={sigma} s={s}: {per*1e6:7.1f} us/interp "
              f"-> 1e6 interps ~ {per*1e6/60:6.2f} min single-core")


if __name__ == "__main__":
    passed = run_gate()
    benchmark_interp()
    print()
    if passed:
        print("GATE: PASSED  (non-planted structured challenger reproduced at sigma=1)")
        sys.exit(0)
    print("GATE: FAILED  (no challenger reproduced -- do NOT launch census)")
    sys.exit(1)
