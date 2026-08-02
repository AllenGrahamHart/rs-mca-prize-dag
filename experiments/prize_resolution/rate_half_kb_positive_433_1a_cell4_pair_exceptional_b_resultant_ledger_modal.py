#!/usr/bin/env python3
"""Build an unisolvent resultant ledger for plane=F=L=M=0."""

import base64
import hashlib
import json
from pathlib import Path
import re
import zlib

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
LIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt"
LINEAR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_linear_factor_0.txt"
CONSTANT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_constant_factor_1.txt"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_ledger_result.json"
REMOTE = {
    PLANE: "/root/cell4_plane.json",
    LIVE: "/root/cell4_live.txt",
    LINEAR: "/root/cell4_linear.txt",
    CONSTANT: "/root/cell4_constant.txt",
}
PRIME = 2130706433
POINTS = [(s, u) for total in range(5) for s in range(total+1)
          for u in (total-s,)]
MONOMIALS = [(i, j) for total in range(5) for i in range(total+1)
             for j in (total-i,)]

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-b-resultant-ledger")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
)
for local_path, remote_path in REMOTE.items():
    image = image.add_local_file(local_path, remote_path)


def matrix_rank_mod(matrix, prime):
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value*inverse % prime for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                (left-scale*right) % prime
                for left, right in zip(work[row], work[rank])
            ]
        rank += 1
    return rank


def shape(polynomial):
    return {
        "degrees": [int(value) for value in polynomial.degrees()],
        "total_degree": int(polynomial.total_degree()),
        "terms": len(list(polynomial.terms())),
    }


@app.function(image=image, cpu=4.0, memory=16384, timeout=300)
def evaluate_resultant(point):
    from flint import fmpz_mod_mpoly_ctx

    s, u = point
    context = fmpz_mod_mpoly_ctx.get(["w0", "b", "t"], PRIME)

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
            exponents = {"w0": 0, "b": 0, "t": 0}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(w0|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in ("w0", "b", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    plane_payload = json.loads(Path(REMOTE[PLANE]).read_text())["result"]
    plane = parse_polynomial(plane_payload["plane_polynomial"])
    linear = parse_polynomial(Path(REMOTE[LINEAR]).read_text().strip())
    constant = parse_polynomial(Path(REMOTE[CONSTANT]).read_text().strip())
    live = parse_polynomial(Path(REMOTE[LIVE]).read_text().strip())
    combination = linear+s*constant+u*live
    resultant = plane.resultant(combination, "b")
    if int(resultant.degrees()[1]) != 0:
        raise RuntimeError("b was not eliminated")
    text = resultant.str()
    return {
        "point": [s, u],
        "status": "COMPLETE",
        "combination_shape": shape(combination),
        "resultant_shape": shape(resultant),
        "resultant_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "zlib_base64": base64.b64encode(
            zlib.compress(text.encode(), level=9)
        ).decode(),
    }


@app.local_entrypoint()
def main():
    evaluation_matrix = [
        [pow(s, i, PRIME)*pow(u, j, PRIME) % PRIME
         for i, j in MONOMIALS]
        for s, u in POINTS
    ]
    rank = matrix_rank_mod(evaluation_matrix, PRIME)
    if rank != len(MONOMIALS):
        raise RuntimeError("evaluation grid is not unisolvent")
    rows = list(evaluate_resultant.map(
        POINTS, order_outputs=True, return_exceptions=True
    ))
    normalized_rows = []
    for index, row in enumerate(rows):
        if isinstance(row, Exception):
            normalized_rows.append({
                "point": list(POINTS[index]), "status": "REMOTE_ERROR",
                "error": repr(row),
            })
            continue
        text = zlib.decompress(base64.b64decode(row.pop("zlib_base64"))).decode()
        filename = (
            "rate_half_kb_positive_433_1a_cell4_pair_exceptional_"
            f"b_resultant_{row['point'][0]}_{row['point'][1]}.txt"
        )
        path = DIRECTORY / filename
        path.write_text(text+"\n")
        row["file"] = filename
        row["file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        normalized_rows.append(row)
    complete = all(row["status"] == "COMPLETE" for row in normalized_rows)
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-ledger-v1",
        "scope": (
            "Fifteen exact unisolvent evaluations of "
            "Res_b(plane,L+sM+uF); simultaneous vanishing is equivalent, "
            "away from the plane-leading guard, to a common algebraic root "
            "of plane,L,M,F. No unit, deployed-point, colored, orbit, or "
            "Prize claim."
        ),
        "field": PRIME,
        "degree_bound": 4,
        "monomials": [list(row) for row in MONOMIALS],
        "points": [list(row) for row in POINTS],
        "evaluation_rank": rank,
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "status": "COMPLETE" if complete else "INCOMPLETE",
        "rows": normalized_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["status"],
        "evaluation_rank": rank,
        "shapes": [row.get("resultant_shape") for row in normalized_rows],
        "errors": [row for row in normalized_rows
                   if row["status"] != "COMPLETE"],
    }, sort_keys=True))
