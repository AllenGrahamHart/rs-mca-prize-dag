#!/usr/bin/env python3
"""Remove the common gcd from the cell-4 exceptional resultant ledger."""

import base64
import functools
import hashlib
import json
from pathlib import Path
import re
import tarfile
import zlib

import modal


DIRECTORY = Path(__file__).parent
LEDGER = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_ledger_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_gcd_result.json"
ARCHIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_sources.tar.gz"
REMOTE_ARCHIVE = "/root/resultant_sources.tar.gz"
PRIME = 2130706433
POINTS = [(s, u) for total in range(5) for s in range(total+1)
          for u in (total-s,)]

SOURCE_FILES = [
    DIRECTORY / (
        "rate_half_kb_positive_433_1a_cell4_pair_exceptional_"
        f"b_resultant_{s}_{u}.txt"
    )
    for s, u in POINTS
]
REMOTE_FILES = [f"/root/ledger/{path.name}" for path in SOURCE_FILES]

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-b-resultant-gcd")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
).add_local_file(ARCHIVE, REMOTE_ARCHIVE)


def shape(polynomial):
    return {
        "degrees": [int(value) for value in polynomial.degrees()],
        "total_degree": int(polynomial.total_degree()),
        "terms": len(list(polynomial.terms())),
    }


def compressed(polynomial):
    text = polynomial.str()
    return {
        "shape": shape(polynomial),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "zlib_base64": base64.b64encode(
            zlib.compress(text.encode(), level=9)
        ).decode(),
    }


@app.function(image=image, cpu=4.0, memory=16384, timeout=300)
def compute_gcd():
    from flint import fmpz_mod_mpoly_ctx

    Path("/root/ledger").mkdir(exist_ok=True)
    with tarfile.open(REMOTE_ARCHIVE, "r:gz") as archive:
        archive.extractall("/root/ledger", filter="data")
    context = fmpz_mod_mpoly_ctx.get(["w0", "t"], PRIME)

    def parse_polynomial(value):
        output = {}
        for raw_term in re.findall(r"[+-]?[^+-]+", value.replace(" ", "")):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient = 1
            exponents = {"w0": 0, "t": 0}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(w0|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = (exponents["w0"], exponents["t"])
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    polynomials = [parse_polynomial(Path(path).read_text().strip())
                   for path in REMOTE_FILES]
    gcd_steps = []
    common = polynomials[0]
    for index, polynomial in enumerate(polynomials[1:], start=1):
        common = common.gcd(polynomial)
        gcd_steps.append({"through_index": index, "shape": shape(common)})
    content, factors = common.factor()
    reconstruction = context.constant(int(content))
    factor_rows = []
    for factor, multiplicity in factors:
        reconstruction *= factor**multiplicity
        factor_rows.append({
            **compressed(factor), "multiplicity": int(multiplicity),
        })
    if reconstruction != common:
        raise RuntimeError("common gcd factor reconstruction failed")

    primitive_rows = []
    for polynomial in polynomials:
        primitive, remainder = divmod(polynomial, common)
        if not remainder.is_zero():
            raise RuntimeError("common gcd division failed")
        primitive_rows.append(compressed(primitive))
    return {
        "status": "COMPLETE",
        "source_shapes": [shape(row) for row in polynomials],
        "gcd_steps": gcd_steps,
        "common": {
            **compressed(common), "content": int(content),
            "factors": factor_rows,
        },
        "primitive_rows": primitive_rows,
    }


@app.local_entrypoint()
def main():
    ledger_payload = json.loads(LEDGER.read_text())
    if [tuple(row["point"]) for row in ledger_payload["rows"]] != POINTS:
        raise RuntimeError("ledger point order mismatch")
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-gcd-v1",
        "scope": (
            "Exact common-gcd removal from the fifteen unisolvent resultant "
            "evaluations; no unit, point, colored, orbit, or Prize claim."
        ),
        "source_ledger_sha256": hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
        "source_archive_sha256": hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
        "result": compute_gcd.remote(),
    }

    def materialize(row, filename):
        text = zlib.decompress(base64.b64decode(row.pop("zlib_base64"))).decode()
        path = DIRECTORY / filename
        path.write_text(text+"\n")
        row["file"] = filename
        row["file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()

    common = output["result"]["common"]
    materialize(common,
                "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common.txt")
    for index, row in enumerate(common["factors"]):
        materialize(
            row,
            "rate_half_kb_positive_433_1a_cell4_pair_exceptional_"
            f"b_resultant_common_factor_{index}.txt",
        )
    for index, row in enumerate(output["result"]["primitive_rows"]):
        point = POINTS[index]
        materialize(
            row,
            "rate_half_kb_positive_433_1a_cell4_pair_exceptional_"
            f"b_resultant_primitive_{point[0]}_{point[1]}.txt",
        )
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["result"]["status"],
        "common": common,
        "primitive_shapes": [row["shape"]
                             for row in output["result"]["primitive_rows"]],
    }, sort_keys=True))
