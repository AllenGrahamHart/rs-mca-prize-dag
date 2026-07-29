#!/usr/bin/env python3
"""Generate and rigorously audit the fixed-point primitive-root table."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


BITS = 48
ROOTS = 64
POSITIONS = 128
HERE = Path(__file__).resolve()
ROOT = (
    Path("/repo")
    if Path("/repo").is_dir()
    else HERE.parents[2] if len(HERE.parents) > 2
    else Path("/")
)
HEADER = ROOT / "experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots.hpp"
RESULT = ROOT / "experiments/prize_resolution/e1_profile_36_mu6_m64_fixed_roots_result.json"

app = modal.App("e1-profile-36-mu6-m64-fixed-roots")
image = modal.Image.debian_slim().pip_install("mpmath", "python-flint")


def format_table(name: str, rows: list[list[int]]) -> str:
    body = []
    for row in rows:
        body.append("    {" + ",".join(str(value) for value in row) + "}")
    return (
        f"inline constexpr int64_t {name}[{ROOTS}][{POSITIONS}] = {{\n"
        + ",\n".join(body)
        + "\n};\n"
    )


@app.function(image=image, cpu=1.0, memory=256, timeout=180, max_containers=1)
def generate() -> dict[str, object]:
    import mpmath as mp
    from flint import arb, ctx

    mp.mp.dps = 100
    ctx.prec = 256
    scale = 1 << BITS
    real: list[list[int]] = []
    imaginary: list[list[int]] = []
    checks = 0
    for root in range(ROOTS):
        unit = 2 * root + 1
        real_row = []
        imaginary_row = []
        for position in range(POSITIONS):
            angle = mp.pi * unit * position / 128
            real_value = int(mp.floor(mp.cos(angle) * scale + mp.mpf("0.5")))
            imag_value = int(mp.floor(mp.sin(angle) * scale + mp.mpf("0.5")))

            arb_angle = arb.pi() * unit * position / 128
            real_error = arb_angle.cos() * scale - real_value
            imag_error = arb_angle.sin() * scale - imag_value
            assert real_error > -1 and real_error < 1
            assert imag_error > -1 and imag_error < 1
            checks += 2
            real_row.append(real_value)
            imaginary_row.append(imag_value)
        real.append(real_row)
        imaginary.append(imaginary_row)

    header = (
        "#pragma once\n\n"
        "#include <cstdint>\n\n"
        + format_table("M64_FIXED_REAL", real)
        + "\n"
        + format_table("M64_FIXED_IMAG", imaginary)
    )
    return {
        "header": header,
        "checks": checks,
        "bits": BITS,
        "roots": ROOTS,
        "positions": POSITIONS,
        "scaled_component_error_lt": 1,
    }


@app.local_entrypoint()
def main() -> None:
    packet = generate.remote()
    header = str(packet.pop("header"))
    HEADER.write_text(header)
    packet.update({
        "schema": "e1-profile-36-mu6-m64-fixed-roots-v1",
        "complete": True,
        "generator": "mpmath-100-decimal",
        "audit": "python-flint-arb-256-bit",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "header_sha256": hashlib.sha256(HEADER.read_bytes()).hexdigest(),
    })
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU6_M64_FIXED_ROOTS_PASS "
        f"checks={packet['checks']} bits={packet['bits']} "
        f"header_sha256={packet['header_sha256']}"
    )


if __name__ == "__main__":
    main()
