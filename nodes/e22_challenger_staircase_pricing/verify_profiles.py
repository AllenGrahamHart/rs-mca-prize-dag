#!/usr/bin/env python3
"""Small exact profile extractor for the E22 challenger pricing leaf.

This is evidence/calibration only.  It enumerates the n=16 exact gate cells
already known to be safe for local execution and prints the structured
challenger profiles that any proposed staircase formula must reproduce.
"""

from __future__ import annotations

import collections
import itertools
import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import classify_pattern, pattern, polynomial_through, sunflower_word  # noqa: E402


def exact_profiles(n: int, k: int, sigma: int) -> collections.Counter:
    word = sunflower_word(n, k, sigma, "cyclic_step_1", "linear")
    found = {}
    for indices in itertools.combinations(range(n), word["s"]):
        poly = polynomial_through(list(indices), word["domain"], word["values"], word["k"])
        if poly is None:
            continue
        rec = pattern(poly, word)
        if rec["agreement"] >= word["s"]:
            found[poly] = rec

    profiles: collections.Counter = collections.Counter()
    for poly, rec in found.items():
        cls = classify_pattern(rec, word["ell"])
        if cls == "planted":
            continue
        touched_profile = tuple(sorted((c for c in rec["petal_agreements"] if c), reverse=True))
        profiles[(cls, rec["core_agreement"], rec["background_agreement"],
                  touched_profile, rec["agreement"])] += 1
    return profiles


def main() -> None:
    for k in (1, 2, 4, 8):
        profiles = exact_profiles(16, k, 1)
        print(f"n=16 k={k} sigma=1 structured_profiles={sum(profiles.values())}")
        for key, count in sorted(profiles.items()):
            print(f"  {count:3d} {key}")
    for k in (2, 4, 8):
        profiles = exact_profiles(16, k, 2)
        print(f"n=16 k={k} sigma=2 structured_profiles={sum(profiles.values())}")
        for key, count in sorted(profiles.items()):
            print(f"  {count:3d} {key}")


if __name__ == "__main__":
    main()
