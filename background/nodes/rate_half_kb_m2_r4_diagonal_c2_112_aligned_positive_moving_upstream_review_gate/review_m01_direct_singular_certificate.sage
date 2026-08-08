#!/usr/bin/env sage
"""Replay M01-R11 while keeping every large basis inside Singular."""

import hashlib
import json
import subprocess
from pathlib import Path


SOURCE = Path(
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_moving_closure_v1.sage"
)
LIBRARY = Path("/repo/experimental/scripts/moving_closure_library.sage")
SINGULAR_SCRIPT = Path("/tmp/m01_direct_certificate.sing")


def canonical_json(value):
    return json.dumps(
        value,
        sort_keys=True,
        default=lambda item: int(item) if item in ZZ else str(item),
    )


def load_upstream_library():
    source = SOURCE.read_text()
    terminal = '\nif __name__ == "__main__":\n    main()\n'
    root_line = "ROOT = Path(__file__).resolve().parents[2]"
    assert source.count(terminal) == 1
    assert source.count(root_line) == 1
    source = source.replace(root_line, 'ROOT = Path("/repo")')
    LIBRARY.write_text(source.replace(terminal, "\n"))
    load(str(LIBRARY))


def singular_polynomial(name, value):
    return f"poly {name}={value};"


def localization_lines(prefix, basis, units):
    lines = [f"poly {prefix}_localizer=1;"]
    for index, unit in enumerate(units, start=1):
        unit_name = f"{prefix}_unit_{index}"
        lines.append(singular_polynomial(unit_name, unit))
        lines.append(
            f"{prefix}_localizer=reduce({prefix}_localizer*{unit_name},{basis});"
        )
    lines.extend(
        [
            f'print("{prefix}_LOCALIZER_DEG="+string(deg({prefix}_localizer)));',
            f'print("{prefix}_LOCALIZER_TERMS="+string(size({prefix}_localizer)));',
            f"poly {prefix}_square=reduce({prefix}_localizer^2,{basis});",
            f'print("{prefix}_SQUARE_DEG="+string(deg({prefix}_square)));',
            f'print("{prefix}_SQUARE_TERMS="+string(size({prefix}_square)));',
        ]
    )
    return lines


def main():
    load_upstream_library()
    assert verify_base_dependency()
    generators, factor_audit = qslice_system("M01", "R11")
    parity = direct_middle_parity()
    expected = EXPECTED_BALANCED["M01-R11"]["polynomials"]
    for name in ("J", "I"):
        assert_expected_fields(metric(parity[name]), expected[name])

    qslice = [to_SF(value) for value in generators]
    units = middle_units(SF, True)
    J = to_SF(parity["J"])
    I = to_SF(parity["I"])
    chunk_size = 1024
    I_items = list(I.dict().items())
    I_chunk_strings = []
    for start in range(0, len(I_items), chunk_size):
        block = I_items[start:start + chunk_size]
        chunk = SF(
            sum(
                coefficient
                * prod(
                    generator ** exponent
                    for generator, exponent in zip(SF.gens(), monomial)
                )
                for monomial, coefficient in block
            )
        )
        assert len(chunk.monomials()) == len(block)
        I_chunk_strings.append(str(chunk))
    source_record = {
        "phase": "SOURCE_COMPILED",
        "upstream_script_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "qslice": [metric(value) for value in generators],
        "J": metric(parity["J"]),
        "I": metric(parity["I"]),
        "full_unit_count": len(units),
        "I_chunk_count": len(I_chunk_strings),
        "I_chunk_size": chunk_size,
        "factor_audit_count": len(factor_audit),
    }
    print(canonical_json(source_record), flush=True)

    lines = [
        "option(noredefine);",
        "option(prot);",
        "ring r=2130706433,(x,s,p,w),dp;",
    ]
    for index, value in enumerate(qslice, start=1):
        lines.append(singular_polynomial(f"g{index}", value))
    lines.append(singular_polynomial("parity_J", J))
    lines.extend(
        [
            "ideal qslice_input=g1,g2,g3,g4;",
            'print("QSLICE_BASIS_BEGIN");',
            "ideal qslice_basis=slimgb(qslice_input);",
            'print("QSLICE_BASIS_SIZE="+string(size(qslice_basis)));',
            'print("QSLICE_DIMENSION="+string(dim(qslice_basis)));',
        ]
    )
    lines.extend(
        [
            "poly J_remainder=reduce(parity_J,qslice_basis);",
            'print("J_REMAINDER_DEG="+string(deg(J_remainder)));',
            'print("J_REMAINDER_TERMS="+string(size(J_remainder)));',
            "ideal J_input=qslice_basis,J_remainder;",
            'print("J_BASIS_BEGIN");',
            "ideal J_basis=slimgb(J_input);",
            'print("J_BASIS_SIZE="+string(size(J_basis)));',
            'print("J_DIMENSION="+string(dim(J_basis)));',
        ]
    )
    lines.extend(
        [
            "poly I_remainder=0;",
        ]
    )
    for index, chunk in enumerate(I_chunk_strings, start=1):
        lines.append(singular_polynomial(f"I_chunk_{index}", chunk))
        lines.append(
            f"I_remainder=reduce(I_remainder+I_chunk_{index},J_basis);"
        )
        if index % 8 == 0 or index == len(I_chunk_strings):
            lines.extend(
                [
                    f'print("I_CHUNK_PROGRESS={index}/{len(I_chunk_strings)}");',
                    'print("I_PARTIAL_DEG="+string(deg(I_remainder)));',
                    'print("I_PARTIAL_TERMS="+string(size(I_remainder)));',
                ]
            )
    lines.extend(
        [
            'print("I_REMAINDER_DEG="+string(deg(I_remainder)));',
            'print("I_REMAINDER_TERMS="+string(size(I_remainder)));',
            "ideal I_input=J_basis,I_remainder;",
            'print("I_BASIS_BEGIN");',
            "ideal I_basis=slimgb(I_input);",
            'print("I_BASIS_SIZE="+string(size(I_basis)));',
            'print("I_DIMENSION="+string(dim(I_basis)));',
        ]
    )
    lines.extend(localization_lines("I", "I_basis", units))
    lines.extend(
        [
            'if (I_square==0) { print("FULL_EMPTY"); }',
            'if (I_square==0) { print("M01_R11_FULL_OPEN_EMPTY"); }',
            "quit;",
        ]
    )
    singular_source = "\n".join(lines) + "\n"
    SINGULAR_SCRIPT.write_text(singular_source)
    print(
        canonical_json(
            {
                "phase": "SINGULAR_SCRIPT_WRITTEN",
                "bytes": len(singular_source.encode()),
                "sha256": hashlib.sha256(singular_source.encode()).hexdigest(),
            }
        ),
        flush=True,
    )

    process = subprocess.Popen(
        ["Singular", "-q", str(SINGULAR_SCRIPT)],
        cwd="/repo",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=int(1),
    )
    assert process.stdout is not None
    lines_seen = []
    for line in process.stdout:
        line = line.rstrip()
        lines_seen.append(line)
        print(f"SINGULAR {line}", flush=True)
    returncode = process.wait()
    assert returncode == 0
    assert "FULL_EMPTY" in lines_seen
    assert "M01_R11_FULL_OPEN_EMPTY" in lines_seen
    print(
        canonical_json(
            {
                "phase": "DONE",
                "returncode": returncode,
                "terminal": "M01_R11_FULL_OPEN_EMPTY",
                "singular_output_sha256": hashlib.sha256(
                    ("\n".join(lines_seen) + "\n").encode()
                ).hexdigest(),
            }
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
