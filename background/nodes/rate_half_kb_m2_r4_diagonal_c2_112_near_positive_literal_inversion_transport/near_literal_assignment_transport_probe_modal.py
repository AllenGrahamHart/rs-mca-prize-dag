#!/usr/bin/env python3
"""Probe exact literal near-aligned inversion transports on Modal.

The remote job patches only the entrypoint and return surface of the exact
PR #1140 aligned compiler.  It reuses that compiler's source reconstruction
for all twelve literal assignments, imposes the near relation w=1/c, and
tests source residuals before attempting any emptiness calculation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-near-literal-inversion-transport-probe"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "9e1d96cbf997c30efa448bbce9a7f48c2bea9643"
SOURCE = "experimental/scripts/compile_kb_mca_v4_m2_aligned_positive_qslice_atlas_v1.sage"
SOURCE_SHA256 = "c382adee5be3b72dcb675b4932a681f65ae958f58e24c3f5fdb8163d4d1508b7"
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "near_literal_assignment_transport_probe_output.json"
AUDIT = HERE / "near_literal_assignment_transport_audit.sage"


PROBE = r'''
# Research-only near-aligned transport probe appended by the local wrapper.
wK = K(1) / cK
NEAR_ROOTS = {
    "A": K(1) / 2,
    "TA": K(2),
    "OB": K(1) / bK,
    "OI": K(bK),
}
TARGETS = {}
for orbit_id, target_root in NEAR_ROOTS.items():
    TARGETS[f"{orbit_id}-RX"] = {
        "name": "square-xi",
        "multiplicity": [2, 0],
        "Qc": (W - target_root) ** 2,
        "Qd": (W - 1 / dK) ** 2,
    }
    TARGETS[f"{orbit_id}-RL"] = {
        "name": "square-ell",
        "multiplicity": [0, 2],
        "Qc": (W - 1 / dK) ** 2,
        "Qd": (W - target_root) ** 2,
    }
    TARGETS[f"{orbit_id}-RM"] = {
        "name": "mixed",
        "multiplicity": [1, 1],
        "Qc": (W - target_root) * (W - 1 / dK),
        "Qd": (W - target_root) * (W - 1 / dK),
    }

TW_VERTEX_ASSIGNMENT = {
    "F00": "F03", "F03": "F00", "F01": "F02", "F02": "F01",
    "F04": "F07", "F07": "F04", "F05": "F06", "F06": "F05",
    "M00": "M03", "M03": "M00", "M01": "M02", "M02": "M01",
}
# Source reciprocity changes the naive vertex-label prediction: after the
# complete positive reconstruction, simultaneous T/W inversion induces the
# same residual assignment pairing as b inversion.
TW_RESIDUAL_ASSIGNMENT = B_INVERSION


def light_localizer_record(_factors):
    return {
        "radical_factor_count": -1,
        "radical_total_degree": -1,
        "radical_factor_set_sha256": "PROBE_SKIPPED",
        "radical_factors": [],
    }


localizer_record = light_localizer_record


def substitute_fraction(value, substitutions):
    value = K(value)
    return K(value.subs(substitutions))


def transform_kw(poly, substitutions, reciprocal_w=False):
    poly = KW(poly)
    result = KW.zero()
    degree = poly.degree()
    for index in range(degree + 1):
        exponent = degree - index if reciprocal_w else index
        result += substitute_fraction(poly[index], substitutions) * W**exponent
    return result


def projectively_equal(left, right):
    left, right = KW(left), KW(right)
    if left.degree() != right.degree():
        return False
    degree = left.degree()
    return all(
        left[i] * right[j] == left[j] * right[i]
        for i in range(degree + 1)
        for j in range(i + 1, degree + 1)
    )


def transformed_target(target_id, mode):
    orbit, allocation = target_id.split("-")
    if mode == "B":
        orbit = {"A": "A", "TA": "TA", "OB": "OI", "OI": "OB"}[orbit]
    else:
        orbit = {"A": "TA", "TA": "A", "OB": "OB", "OI": "OI"}[orbit]
    return f"{orbit}-{allocation}"


def strip_bcd_unit(value):
    value = K(value)
    denominator = R(value.denominator())
    assert denominator.is_monomial()
    value = R(value.numerator())
    if not value:
        return value
    unit = R.one()
    for generator in (b, c, d):
        valuation = min(monomial.degree(generator) for monomial in value.monomials())
        unit *= generator**valuation
    return primitive(value // unit)


LOCALIZER_FACTOR_CACHE = {}


def transformed_localizer_factors(factors, mode):
    result = set()
    for value in factors:
        key = (mode, str(value))
        if key not in LOCALIZER_FACTOR_CACHE:
            if mode == "I":
                transformed = strip_bcd_unit(K(value))
            elif mode == "B":
                transformed = strip_bcd_unit(
                    substitute_fraction(value, {bK: 1 / bK})
                )
            else:
                transformed = strip_bcd_unit(
                    substitute_fraction(
                        value,
                        {bK: 1 / bK, cK: 1 / cK, dK: 1 / dK},
                    )
                )
            LOCALIZER_FACTOR_CACHE[key] = tuple(
                primitive(factor) for factor, _ in transformed.factor()
                if not factor.is_constant()
            )
        result.update(str(factor) for factor in LOCALIZER_FACTOR_CACHE[key])
    return sorted(result)


def target_transport_ok(source_id, target_id, mode):
    destination_id = transformed_target(target_id, mode)
    source = TARGETS[source_id]
    destination = TARGETS[destination_id]
    substitutions = {bK: 1 / bK} if mode == "B" else {
        bK: 1 / bK, cK: 1 / cK, dK: 1 / dK,
    }
    return all(
        projectively_equal(
            transform_kw(source[key], substitutions, reciprocal_w=(mode == "TW")),
            destination[key],
        )
        for key in ("Qc", "Qd")
    )


def residual_transport_ok(source, destination, mode):
    substitutions = {bK: 1 / bK} if mode == "B" else {
        bK: 1 / bK, cK: 1 / cK, dK: 1 / dK,
    }
    return all(
        projectively_equal(
            transform_kw(source[index], substitutions, reciprocal_w=(mode == "TW")),
            destination[index],
        )
        for index in (0, 1)
    )


def tw_search_matches(source, destination):
    variants = []
    direct_substitutions = {bK: 1 / bK, cK: 1 / cK, dK: 1 / dK}
    direct = all(
        projectively_equal(
            transform_kw(source[index], direct_substitutions, reciprocal_w=True),
            destination[index],
        )
        for index in (0, 1)
    )
    if direct:
        variants.append("same-root-order")
    swapped_substitutions = {bK: 1 / bK, cK: 1 / dK, dK: 1 / cK}
    swapped = all(
        projectively_equal(
            transform_kw(source[index], swapped_substitutions, reciprocal_w=True),
            destination[1 - index],
        )
        for index in (0, 1)
    )
    if swapped:
        variants.append("swapped-root-order")
    return variants


def probe_main():
    cache = {}
    cell_count = 0
    for assignment_id in ASSIGNMENT_EDGES:
        assignment, cells, systems, residual_c, residual_d = build_assignment(assignment_id)
        cache[assignment_id] = {
            "assignment": assignment,
            "systems": systems,
            "residuals": (residual_c, residual_d),
        }
        cell_count += len(cells)

    checks = []
    for mode, assignment_map in (("B", B_INVERSION), ("TW", TW_RESIDUAL_ASSIGNMENT)):
        for assignment_id, destination_id in assignment_map.items():
            residual_ok = residual_transport_ok(
                cache[assignment_id]["residuals"],
                cache[destination_id]["residuals"],
                mode,
            )
            for target_id in TARGETS:
                destination_target = transformed_target(target_id, mode)
                source_localizers = cache[assignment_id]["systems"][target_id]["localizer_factors"]
                destination_localizers = cache[destination_id]["systems"][destination_target]["localizer_factors"]
                localizer_ok = transformed_localizer_factors(
                    source_localizers, mode
                ) == transformed_localizer_factors(destination_localizers, "I")
                checks.append({
                    "mode": mode,
                    "source": f"{assignment_id}-{target_id}",
                    "target": f"{destination_id}-{destination_target}",
                    "residual_projective": bool(residual_ok),
                    "target_projective": bool(target_transport_ok(target_id, target_id, mode)),
                    "localizers_exact": bool(localizer_ok),
                })

    failed = [
        row for row in checks
        if not (
            row["residual_projective"]
            and row["target_projective"]
            and row["localizers_exact"]
        )
    ]
    tw_search = {}
    for assignment_id in ASSIGNMENT_EDGES:
        matches = []
        for destination_id in ASSIGNMENT_EDGES:
            for variant in tw_search_matches(
                cache[assignment_id]["residuals"],
                cache[destination_id]["residuals"],
            ):
                matches.append({"assignment": destination_id, "variant": variant})
        tw_search[assignment_id] = matches
    b_failed = [row for row in failed if row["mode"] == "B"]
    tw_failed = [row for row in failed if row["mode"] == "TW"]
    data = {
        "schema": "kb-c2-112-near-literal-inversion-transport-probe-v1",
        "upstream_commit": "9e1d96cbf997c30efa448bbce9a7f48c2bea9643",
        "source_sha256": "c382adee5be3b72dcb675b4932a681f65ae958f58e24c3f5fdb8163d4d1508b7",
        "assignments": len(cache),
        "target_variants": len(TARGETS),
        "raw_cells": cell_count,
        "semantic_cells_after_other_orientation_quotient": 108,
        "checks": len(checks),
        "failed": failed,
        "b_failed": b_failed,
        "tw_failed_count": len(tw_failed),
        "tw_all_assignment_search": tw_search,
        "b_assignment_map": B_INVERSION,
        "tw_vertex_prediction_refuted": TW_VERTEX_ASSIGNMENT,
        "tw_residual_assignment_map": TW_RESIDUAL_ASSIGNMENT,
        "target_maps": {
            mode: {target: transformed_target(target, mode) for target in TARGETS}
            for mode in ("B", "TW")
        },
        "affine_semantic_orbits_under_transports": 42,
        "canonical_orbits_already_covered": 12,
        "residual_affine_orbits": 30,
        "terminal": "B_TRANSPORT_PASS_TW_AUDITED" if not b_failed else "B_TRANSPORT_FAIL",
    }
    print("NEAR_LITERAL_PROBE_JSON " + canonical_json(data))


probe_main()
'''


app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("git", "python3", "python-is-python3")
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin pull/1140/head:refs/remotes/origin/pr1140",
        "git -C /repo checkout --detach refs/remotes/origin/pr1140",
        f'test "$(git -C /repo rev-parse HEAD)" = "{COMMIT}"',
    )
    .add_local_file(AUDIT, "/near_literal_assignment_transport_audit.sage")
)


@app.function(image=image, cpu=4, memory=8192, timeout=900)
def probe() -> dict[str, object]:
    import hashlib as remote_hashlib
    import json as remote_json
    import os
    import resource
    import subprocess
    import time
    from pathlib import Path as RemotePath

    source_path = RemotePath("/repo") / SOURCE
    source = source_path.read_text()
    assert remote_hashlib.sha256(source.encode()).hexdigest() == SOURCE_SHA256
    old_return = "    return assignment, cells, equations_by_target\n"
    new_return = "    return assignment, cells, equations_by_target, residual_c, residual_d\n"
    assert source.count(old_return) == 1
    source = source.replace(old_return, new_return)
    companion = (
        "        assert swap_cd_chart(equations[0]) == equations[2]\n"
        "        assert swap_cd_chart(equations[1]) == equations[3]\n"
    )
    assert source.count(companion) == 1
    source = source.replace(companion, "        # Near targets are oriented and need not be c/d companions.\n")
    entrypoint = 'if __name__ == "__main__":\n    main()\n'
    assert source.count(entrypoint) == 1
    source = source.replace(entrypoint, PROBE)
    patched = RemotePath("/tmp/near_literal_probe.sage")
    patched.write_text(source)

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", str(patched)],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=870,
            check=False,
        )
        stdout, stderr = completed.stdout, completed.stderr
        returncode = completed.returncode
        timed_out = False
    except subprocess.TimeoutExpired as error:
        stdout, stderr = error.stdout or "", error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        returncode, timed_out = None, True
    payload = None
    for line in stdout.splitlines():
        if line.startswith("NEAR_LITERAL_PROBE_JSON "):
            payload = remote_json.loads(line.split(" ", 1)[1])
    passed = (
        not timed_out
        and returncode == 0
        and payload is not None
        and payload.get("terminal") == "B_TRANSPORT_PASS_TW_AUDITED"
    )
    return {
        "status": "TIMEOUT" if timed_out else ("PASS" if passed else "FAIL"),
        "returncode": returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payload,
        "stdout_sha256": remote_hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-20000:],
        "stderr_tail": stderr[-10000:],
    }


@app.function(image=image, cpu=4, memory=8192, timeout=900)
def independent_audit() -> dict[str, object]:
    import hashlib as remote_hashlib
    import json as remote_json
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/near_literal_assignment_transport_audit.sage"],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=870,
            check=False,
        )
        stdout, stderr = completed.stdout, completed.stderr
        returncode = completed.returncode
        timed_out = False
    except subprocess.TimeoutExpired as error:
        stdout, stderr = error.stdout or "", error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        returncode, timed_out = None, True
    payload = None
    for line in stdout.splitlines():
        if line.startswith("NEAR_LITERAL_AUDIT_JSON "):
            payload = remote_json.loads(line.split(" ", 1)[1])
    passed = (
        not timed_out
        and returncode == 0
        and payload is not None
        and payload.get("terminal") == "INDEPENDENT_TRANSPORT_AUDIT_PASS"
    )
    return {
        "status": "TIMEOUT" if timed_out else ("PASS" if passed else "FAIL"),
        "returncode": returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payload,
        "stdout_sha256": remote_hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-20000:],
        "stderr_tail": stderr[-10000:],
    }


@app.local_entrypoint()
def main(audit_only: bool = False) -> None:
    if audit_only:
        previous = json.loads(OUTPUT.read_text())
        row = previous["result"]
    else:
        row = probe.remote()
    audit_row = independent_audit.remote()
    output = {
        "schema": "kb-c2-112-near-literal-inversion-transport-modal-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "source_path": SOURCE,
        "source_sha256": SOURCE_SHA256,
        "result": row,
        "independent_audit": audit_row,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": row["status"],
        "seconds": row["seconds"],
        "audit_status": audit_row["status"],
        "audit_seconds": audit_row["seconds"],
    }, sort_keys=True))
    print(f"wrote {OUTPUT}")
