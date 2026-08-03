#!/usr/bin/env python3
"""One-time exact split of the roadmap and compute-request compatibility files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sectioned_document import ROOT, SCHEMA, compiled_text


ROADMAP = {
    "source": "notes/PRIZE_RESOLUTION_ROADMAP.md",
    "manifest": "notes/roadmap/document.json",
    "boundaries": (
        "## 1. The two theses (why the plan has this shape)",
        "## 2. The walls, and identification discipline",
        "## 3. Unifying-lemma candidates (posed attackably)",
        "## 4. Board anatomy",
        "## 5. Risk register (pre-registered triggers -> consequences; all live)",
        "## 6. The gates (sequencing; conditions, never dates)",
        "## 7. The tracks",
        "## 8. Endgame",
        "## 9. The progress metric",
        "## 10. Maintainer decision queue (standing; rule as they become ripe)",
        "## 11. Planning priors (not evidence; re-issue at every gate)",
        "## 12. Joint harvest execution log",
        "## 2026-07-29 KoalaBear cubic endpoint-cofactor narrowing",
        "### Compute request CR-KB-C2-112-POS-QS-SAT",
    ),
    "sections": (
        "notes/roadmap/sections/00-overview-and-gate-addendum.md",
        "notes/roadmap/sections/01-two-theses.md",
        "notes/roadmap/sections/02-walls.md",
        "notes/roadmap/sections/03-unifying-lemmas.md",
        "notes/roadmap/sections/04-board-anatomy.md",
        "notes/roadmap/sections/05-risk-register.md",
        "notes/roadmap/sections/06-gates.md",
        "notes/roadmap/sections/07-tracks.md",
        "notes/roadmap/sections/08-endgame.md",
        "notes/roadmap/sections/09-progress-metric.md",
        "notes/roadmap/sections/10-maintainer-decisions.md",
        "notes/roadmap/sections/11-planning-priors.md",
        "notes/work_cycles/roadmap_r3/12-joint-harvest-log.md",
        "notes/work_cycles/roadmap_r3/13-koalabear-20260729-30.md",
        "notes/work_cycles/roadmap_r3/14-rate-half-20260730-20260803.md",
    ),
}

COMPUTE = {
    "source": "notes/PRIZE_COMPUTE_REQUESTS.md",
    "manifest": "notes/compute_requests/document.json",
    "boundaries": (
        "## Request queue",
        "## CR-001: H3 fixed-order high-excess / double-accident certificate",
        "## CR-002: Quotient-pencil rank-two component classification",
        "## CR-004: WCL terminal four-slot classification",
        "## CR-003: Rate-half Hankel sharp-cap component classification",
        "## N11 deferred contributor certificate requests",
        "#### CR-E1-E34-Q16-SURVIVORS: close the three unobstructed profiles",
        "## E1 profile-(2,10), cofactor-1028 low-energy certification",
        "## CR-K3-M2-R4-DIAGONAL-FACET-SAT: order-two whole-fiber defect classifier",
    ),
    "sections": (
        "notes/compute_requests/sections/00-policy-and-spend-freeze.md",
        "notes/compute_requests/sections/01-queue-and-handoffs.md",
        "notes/compute_requests/sections/02-cr001-h3.md",
        "notes/compute_requests/sections/03-cr002-quotient-pencil.md",
        "notes/compute_requests/sections/04-cr004-wcl.md",
        "notes/compute_requests/sections/05-cr003-rate-half.md",
        "notes/compute_requests/sections/06-n11-l1-and-e1.md",
        "notes/compute_requests/sections/07-e1-exact-censuses.md",
        "notes/compute_requests/sections/08-e1-low-energy-and-class-orbit.md",
        "notes/compute_requests/sections/09-k3-and-positive-433.md",
    ),
}


def split_document(spec):
    source = ROOT / spec["source"]
    text = source.read_text()
    starts = [0]
    cursor = 0
    for boundary in spec["boundaries"]:
        marker = boundary + "\n"
        index = text.find(marker, cursor)
        if index < 0:
            raise RuntimeError(f"{source}: missing boundary {boundary}")
        starts.append(index)
        cursor = index + len(marker)
    starts.append(len(text))
    if len(spec["sections"]) != len(starts) - 1:
        raise RuntimeError(f"{source}: section count mismatch")
    sections = [
        text[starts[index]:starts[index + 1]]
        for index in range(len(starts) - 1)
    ]
    # Keep separator whitespace in the compiled view while ensuring no source
    # shard ends with a blank line (git diff --check treats that as damage).
    for index in range(len(sections) - 1):
        trailing = len(sections[index]) - len(sections[index].rstrip("\n"))
        if trailing > 1:
            moved = trailing - 1
            sections[index] = sections[index][:-moved]
            sections[index + 1] = "\n" * moved + sections[index + 1]
    return sections


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    specs = (ROADMAP, COMPUTE)
    outputs = []
    for spec in specs:
        sections = split_document(spec)
        outputs.append((spec, sections))
        manifest = ROOT / spec["manifest"]
        if manifest.exists():
            raise RuntimeError(f"refusing to overwrite {manifest}")
    if not args.apply:
        for spec, sections in outputs:
            print(
                f"SECTION_MIGRATION_READY {spec['source']} "
                f"sections={len(sections)} max_lines="
                f"{max(value.count(chr(10)) for value in sections)}"
            )
        return 0
    for spec, sections in outputs:
        for rel, text in zip(spec["sections"], sections):
            path = ROOT / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
        manifest = ROOT / spec["manifest"]
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(json.dumps({
            "schema": SCHEMA,
            "output": spec["source"],
            "sections": list(spec["sections"]),
        }, indent=2) + "\n")
        if compiled_text(manifest, ROOT) != (ROOT / spec["source"]).read_text():
            raise RuntimeError(f"{spec['source']}: compiled bytes differ")
        print(
            f"SECTION_MIGRATION_PASS {spec['source']} "
            f"sections={len(sections)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
