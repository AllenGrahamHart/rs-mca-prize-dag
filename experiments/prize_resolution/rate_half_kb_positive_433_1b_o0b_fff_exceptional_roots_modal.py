#!/usr/bin/env python3
"""Extract every base-field exceptional root for the generic FFF proof."""

import hashlib
import importlib.util
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
GENERIC = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
FRONTIER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json"
C1 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_result.json"
Q5 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
MULTIPLICATION = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json"
Q7 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
POLYNOMIAL = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_result.json"
DETERMINANT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_result.json"
REMOTE_PATHS = [f"/root/source_{index}.json" for index in range(8)]
REMOTE_PROGRAM = "/root/fff_exceptional_roots_program.py"
SOURCES = [GENERIC, FRONTIER, C1, Q5, MULTIPLICATION, Q7, POLYNOMIAL, DETERMINANT]
SOURCE_HASHES = [
    "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e",
    "29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c",
    "899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c",
    "b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c",
    "3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e",
    "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d",
    "ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae",
    "a222789bb3e54df1a4198536644a6d331972087d968b61b227634eca22a79786",
]
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-fff-exceptional-roots")
image = modal.Image.debian_slim(python_version="3.12").pip_install("python-flint==0.8.0")
for source, remote in zip(SOURCES, REMOTE_PATHS):
    image = image.add_local_file(source, remote)
image = image.add_local_file(PROGRAM, REMOTE_PROGRAM)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@app.function(image=image, cpu=2.0, memory=4096, timeout=660)
def collect_roots():
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    core = load("fff_exceptional_roots", REMOTE_PROGRAM)
    payloads = [json.loads(Path(path).read_text()) for path in REMOTE_PATHS]
    built = core.build(*payloads)
    groups = built.pop("groups")
    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def coefficients(polynomial):
        if polynomial.is_zero():
            return []
        return [int(polynomial[index])
                for index in range(int(polynomial.degree()) + 1)]

    def monic(polynomial):
        if polynomial.is_zero():
            return polynomial
        leading = int(polynomial[int(polynomial.degree())])
        return polynomial * pow(leading, -1, PRIME)

    def field_part(polynomial):
        if int(polynomial.degree()) == 0:
            return context([1]), []
        root_part = monic(polynomial.gcd(pow(variable, PRIME, polynomial) - variable))
        _, factors = root_part.factor()
        roots = []
        for factor, multiplicity in factors:
            require(multiplicity == 1 and int(factor.degree()) == 1,
                    "base-field factor")
            roots.append(-int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME)
        roots = sorted(set(roots))
        reconstructed = context([1])
        for root in roots:
            reconstructed *= variable - root
        require(monic(reconstructed) == root_part, "root reconstruction")
        return root_part, roots

    global_lcm = context([1])
    seen = set()
    group_rows = []
    for group in groups:
        group_lcm = context([1])
        for values in group.pop("polynomials"):
            key = tuple(values)
            polynomial = context(values)
            common = group_lcm.gcd(polynomial)
            group_lcm = monic((group_lcm * polynomial) // common)
            if key not in seen:
                seen.add(key)
                common = global_lcm.gcd(polynomial)
                global_lcm = monic((global_lcm * polynomial) // common)
        root_part, roots = field_part(group_lcm)
        group_rows.append({
            **group,
            "lcm_degree": int(group_lcm.degree()),
            "lcm_sha256": hashlib.sha256(
                json.dumps(coefficients(group_lcm), separators=(",", ":")).encode()
            ).hexdigest(),
            "field_root_polynomial": coefficients(root_part),
            "field_root_polynomial_sha256": hashlib.sha256(
                json.dumps(coefficients(root_part), separators=(",", ":")).encode()
            ).hexdigest(),
            "roots": roots,
            "root_count": len(roots),
        })
    global_part, global_roots = field_part(global_lcm)
    require(global_roots == sorted({root for group in group_rows
                                    for root in group["roots"]}), "root union")
    return {
        **built,
        "status": "COMPLETE",
        "global_unique_polynomial_count": len(seen),
        "global_lcm_degree": int(global_lcm.degree()),
        "global_lcm_sha256": hashlib.sha256(
            json.dumps(coefficients(global_lcm), separators=(",", ":")).encode()
        ).hexdigest(),
        "field_root_polynomial": coefficients(global_part),
        "field_root_polynomial_sha256": hashlib.sha256(
            json.dumps(coefficients(global_part), separators=(",", ":")).encode()
        ).hexdigest(),
        "roots": global_roots,
        "root_count": len(global_roots),
        "groups": group_rows,
        "groups_sha256": hashlib.sha256(
            json.dumps(group_rows, separators=(",", ":"), sort_keys=True).encode()
        ).hexdigest(),
        "elapsed_seconds": time.perf_counter() - started,
    }


def write_checkpoint(row, complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-exceptional-roots-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-exceptional-roots",
        "collection_complete": complete,
        "field": PRIME,
        "source_sha256": SOURCE_HASHES,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


@app.local_entrypoint()
def main():
    for path, digest in zip(SOURCES, SOURCE_HASHES):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    write_checkpoint(None, False)
    try:
        row = collect_roots.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] == "COMPLETE"
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT), "status": row["status"],
        "global_lcm_degree": row.get("global_lcm_degree"),
        "root_count": row.get("root_count"),
        "roots": row.get("roots"),
        "group_roots": {group["label"]: group["root_count"]
                        for group in row.get("groups", [])},
        "elapsed_seconds": row.get("elapsed_seconds"),
    }, sort_keys=True))
