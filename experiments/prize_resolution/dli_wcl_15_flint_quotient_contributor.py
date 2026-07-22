#!/usr/bin/env python3
"""FLINT handoff for the WCL (1,5) exponent-256 quotient endpoint.

The guarded default stops at exponent 16. Contributor runs should first emit
the exponent-128 checkpoint with ``--max-step 7 --emit-dir DIR``, then resume
it with ``--resume-stage7 DIR --max-step 8 --emit-dir OUT``. The script does
not compute a Groebner basis or claim WCL emptiness.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import time
from pathlib import Path
from typing import Any

from flint import nmod_mpoly_ctx


MODULUS = 32003
EXPECTED_PREFIX_COUNTS = (None, 1, 1, 32, 240, 1881, 14831, 117644)
SCHEMA = "dli-wcl-15-flint-quotient-v1"


def context():
    return nmod_mpoly_ctx.get(("c0", "c1", "b"), MODULUS, "degrevlex")


def divisor_coefficients(ctx):
    c0, c1, b = ctx.gens()
    return [
        ctx.constant(MODULUS - 1),
        c0**2 - 2 * b,
        2 * c0 * c1 - b**2,
        c1**2 + 2 * c0,
        2 * c1,
    ]


def initial_remainder(ctx):
    zero = ctx.constant(0)
    return [zero, ctx.constant(1), ctx.constant(0), ctx.constant(0), ctx.constant(0)]


def square_reduce(remainder, divisor, ctx):
    """Square a degree-below-five Y-polynomial and reduce by monic G."""
    raw = [ctx.constant(0) for _ in range(9)]
    for left in range(5):
        for right in range(left, 5):
            product = remainder[left] * remainder[right]
            if left != right:
                product = 2 * product
            raw[left + right] += product

    # G=Y^5+sum_(j=0)^4 divisor[j]Y^j.
    for degree in range(8, 4, -1):
        leading = raw[degree]
        if leading.is_zero():
            continue
        shift = degree - 5
        for j in range(5):
            raw[shift + j] -= leading * divisor[j]
    return raw[:5]


def term_count(poly) -> int:
    return sum(1 for _ in poly.terms())


def stage_summary(remainder, stage: int, seconds: float) -> dict[str, Any]:
    counts = [term_count(poly) for poly in remainder]
    total = sum(counts)
    if stage < len(EXPECTED_PREFIX_COUNTS):
        assert total == EXPECTED_PREFIX_COUNTS[stage], (
            stage,
            total,
            EXPECTED_PREFIX_COUNTS[stage],
        )
    return {
        "stage": stage,
        "exponent": 1 << stage,
        "coefficient_term_counts": counts,
        "total_terms": total,
        "seconds": seconds,
    }


def write_remainder(remainder, stage: int, directory: Path) -> dict[str, Any]:
    directory.mkdir(parents=True, exist_ok=True)
    records = []
    for index, poly in enumerate(remainder):
        path = directory / f"stage{stage:02d}_r{index}.tsv.gz"
        digest = hashlib.sha256()
        count = 0
        with gzip.open(path, "wt", encoding="ascii", newline="") as handle:
            for exponents, coefficient in poly.terms():
                line = "\t".join(map(str, (*exponents, int(coefficient)))) + "\n"
                handle.write(line)
                digest.update(line.encode("ascii"))
                count += 1
        records.append(
            {
                "coefficient": index,
                "path": path.name,
                "terms": count,
                "sha256": digest.hexdigest(),
            }
        )
    return {"stage": stage, "files": records}


def read_remainder(ctx, stage: int, directory: Path):
    remainder = []
    for index in range(5):
        path = directory / f"stage{stage:02d}_r{index}.tsv.gz"
        terms = {}
        with gzip.open(path, "rt", encoding="ascii") as handle:
            for line in handle:
                e0, e1, e2, coefficient = map(int, line.split())
                terms[(e0, e1, e2)] = coefficient
        remainder.append(ctx.from_dict(terms))
    return remainder


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-step", type=int, choices=range(1, 9), default=4)
    parser.add_argument("--emit-dir", type=Path)
    parser.add_argument("--resume-stage7", type=Path)
    args = parser.parse_args()
    if args.max_step == 8 and args.emit_dir is None:
        parser.error("--max-step 8 requires --emit-dir")
    if args.resume_stage7 is not None and args.max_step != 8:
        parser.error("--resume-stage7 is valid only with --max-step 8")
    return args


def main() -> None:
    args = parse_args()
    ctx = context()
    divisor = divisor_coefficients(ctx)
    summaries = []
    emitted = []

    if args.resume_stage7 is not None:
        remainder = read_remainder(ctx, 7, args.resume_stage7)
        summary = stage_summary(remainder, 7, 0.0)
        summaries.append(summary)
        print("WCL15_FLINT_STAGE " + json.dumps(summary, sort_keys=True), flush=True)
        start = 8
    else:
        remainder = initial_remainder(ctx)
        start = 1

    for stage in range(start, args.max_step + 1):
        began = time.monotonic()
        remainder = square_reduce(remainder, divisor, ctx)
        summary = stage_summary(remainder, stage, time.monotonic() - began)
        summaries.append(summary)
        print("WCL15_FLINT_STAGE " + json.dumps(summary, sort_keys=True), flush=True)
        if args.emit_dir is not None and stage in {7, 8}:
            emitted.append(write_remainder(remainder, stage, args.emit_dir))

    result = {
        "schema": SCHEMA,
        "status": "COMPLETE",
        "modulus": MODULUS,
        "max_step": args.max_step,
        "summaries": summaries,
        "emitted": emitted,
        "nonclaim": "no Groebner basis and no WCL emptiness conclusion",
    }
    print("WCL15_FLINT_RESULT " + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
