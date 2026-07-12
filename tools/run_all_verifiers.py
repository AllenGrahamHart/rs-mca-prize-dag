#!/usr/bin/env python3
"""Fail-closed verifier discovery, hash manifest, replay, and self-test."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tools" / "verifier_manifest.json"
LEDGER = ROOT / "experiments" / "prize_resolution" / "verifier_replay.json"
NODE_TREES = ("critical", "background")
ASSETS = ("statement.md", "proof.md", "conditional.md")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def discover(root: Path) -> list[str]:
    found: set[str] = set()
    for tree in NODE_TREES:
        base = root / tree / "nodes"
        if not base.exists():
            continue
        for path in base.rglob("verify*.py"):
            if path.name.endswith("_modal.py") or "__pycache__" in path.parts:
                continue
            found.add(path.relative_to(root).as_posix())
    for path in (root / "tools").glob("verify_*.py"):
        found.add(path.relative_to(root).as_posix())
    return sorted(found)


def proof_assets(root: Path, scripts: list[str]) -> list[str]:
    assets: set[str] = set()
    for rel in scripts:
        parts = Path(rel).parts
        if len(parts) < 4 or parts[0] not in NODE_TREES or parts[1] != "nodes":
            continue
        node_root = root / parts[0] / parts[1] / parts[2]
        for name in ASSETS:
            path = node_root / name
            if path.exists():
                assets.add(path.relative_to(root).as_posix())
    return sorted(assets)


def is_remote_launcher(path: Path) -> bool:
    return any(line.strip() in {"import modal", "from modal import App"} for line in path.read_text().splitlines())


def build_manifest(root: Path) -> dict[str, Any]:
    discovered = discover(root)
    remote = [rel for rel in discovered if is_remote_launcher(root / rel)]
    scripts = [rel for rel in discovered if rel not in remote]
    assets = proof_assets(root, discovered)
    return {
        "schema": "prize-verifier-manifest-v1",
        "scripts": {rel: digest(root / rel) for rel in scripts},
        "remote_launchers": {rel: digest(root / rel) for rel in remote},
        "proof_assets": {rel: digest(root / rel) for rel in assets},
    }


def validate_manifest(root: Path, manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if manifest.get("schema") != "prize-verifier-manifest-v1":
        errors.append("schema mismatch")
    expected = set(discover(root))
    recorded_scripts = set(manifest.get("scripts", {}))
    recorded_remote = set(manifest.get("remote_launchers", {}))
    recorded = recorded_scripts | recorded_remote
    overlap = recorded_scripts & recorded_remote
    for rel in sorted(overlap):
        errors.append(f"verifier classified twice: {rel}")
    for rel in sorted(expected - recorded):
        errors.append(f"unmanifested verifier: {rel}")
    for rel in sorted(recorded - expected):
        errors.append(f"stale verifier entry: {rel}")
    for section in ("scripts", "remote_launchers", "proof_assets"):
        entries = manifest.get(section, {})
        if not isinstance(entries, dict):
            errors.append(f"{section} is not an object")
            continue
        for rel, expected_hash in sorted(entries.items()):
            path = root / rel
            if not path.is_file():
                errors.append(f"missing {section} file: {rel}")
            elif digest(path) != expected_hash:
                errors.append(f"hash mismatch: {rel}")
    for rel in sorted(expected):
        should_be_remote = is_remote_launcher(root / rel)
        if should_be_remote != (rel in recorded_remote):
            errors.append(f"wrong local/remote classification: {rel}")
    expected_assets = set(proof_assets(root, sorted(expected)))
    recorded_assets = set(manifest.get("proof_assets", {}))
    for rel in sorted(expected_assets - recorded_assets):
        errors.append(f"unmanifested proof asset: {rel}")
    for rel in sorted(recorded_assets - expected_assets):
        errors.append(f"stale proof asset entry: {rel}")
    return errors


def run_one(root: Path, rel: str, timeout: float) -> dict[str, Any]:
    start = time.monotonic()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        result = subprocess.run(
            [sys.executable, rel],
            cwd=root,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        status = "PASS" if result.returncode == 0 else "FAIL"
        return {
            "script": rel,
            "status": status,
            "returncode": result.returncode,
            "seconds": round(time.monotonic() - start, 6),
            "stdout_tail": result.stdout[-2000:],
            "stderr_tail": result.stderr[-2000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "script": rel,
            "status": "TIMEOUT",
            "returncode": None,
            "seconds": round(time.monotonic() - start, 6),
            "stdout_tail": (exc.stdout or "")[-2000:],
            "stderr_tail": (exc.stderr or "")[-2000:],
        }


def write_ledger(rows: list[dict[str, Any]], complete: bool) -> None:
    payload = {
        "schema": "prize-verifier-replay-v1",
        "complete": complete,
        "counts": {
            status: sum(row["status"] == status for row in rows)
            for status in ("PASS", "FAIL", "TIMEOUT")
        },
        "results": sorted(rows, key=lambda row: row["script"]),
    }
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def replay(root: Path, scripts: list[str], timeout: float, jobs: int) -> int:
    rows: list[dict[str, Any]] = []
    write_ledger(rows, complete=False)
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = {pool.submit(run_one, root, rel, timeout): rel for rel in scripts}
        for future in concurrent.futures.as_completed(futures):
            row = future.result()
            rows.append(row)
            write_ledger(rows, complete=False)
            print(f"{row['status']:7} {row['seconds']:8.3f}s  {row['script']}", flush=True)
    write_ledger(rows, complete=True)
    failures = [row for row in rows if row["status"] != "PASS"]
    print(f"RUN_ALL_VERIFIERS total={len(rows)} failures={len(failures)}")
    return 1 if failures else 0


def self_test() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw)
        node = root / "critical" / "nodes" / "sample"
        tools = root / "tools"
        node.mkdir(parents=True)
        tools.mkdir()
        verifier = node / "verify.py"
        proof = node / "proof.md"
        verifier.write_text("print('ok')\n")
        proof.write_text("proof\n")
        baseline = build_manifest(root)
        if validate_manifest(root, baseline):
            raise AssertionError("baseline manifest rejected")

        caught = 0

        mutation = json.loads(json.dumps(baseline))
        mutation["scripts"].clear()
        caught += bool(validate_manifest(root, mutation))

        mutation = json.loads(json.dumps(baseline))
        mutation["scripts"]["critical/nodes/ghost/verify.py"] = "0" * 64
        caught += bool(validate_manifest(root, mutation))

        verifier.write_text("print('tampered')\n")
        caught += bool(validate_manifest(root, baseline))
        verifier.write_text("print('ok')\n")

        proof.write_text("tampered proof\n")
        caught += bool(validate_manifest(root, baseline))
        proof.write_text("proof\n")

        verifier.write_text("raise SystemExit(7)\n")
        caught += run_one(root, "critical/nodes/sample/verify.py", 1)["status"] == "FAIL"

        verifier.write_text("import time; time.sleep(2)\n")
        caught += run_one(root, "critical/nodes/sample/verify.py", 0.05)["status"] == "TIMEOUT"

        if caught != 6:
            raise AssertionError(f"negative controls caught {caught}/6")
    print("RUN_ALL_VERIFIERS_SELF_TEST_PASS negative_controls=6/6")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh-manifest", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--match", default="")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--jobs", type=int, default=1)
    args = parser.parse_args()

    if args.refresh_manifest:
        MANIFEST.write_text(json.dumps(build_manifest(ROOT), indent=2, sort_keys=True) + "\n")
        print(f"wrote {MANIFEST.relative_to(ROOT)}")
    if not MANIFEST.is_file():
        print("missing tools/verifier_manifest.json; run --refresh-manifest", file=sys.stderr)
        return 1
    manifest = json.loads(MANIFEST.read_text())
    errors = validate_manifest(ROOT, manifest)
    if errors:
        print("VERIFIER_MANIFEST_FAIL", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(
        "VERIFIER_MANIFEST_PASS "
        f"scripts={len(manifest['scripts'])} remote_launchers={len(manifest['remote_launchers'])} "
        f"proof_assets={len(manifest['proof_assets'])}"
    )
    if args.self_test:
        self_test()
    if args.run:
        scripts = [rel for rel in manifest["scripts"] if args.match in rel]
        return replay(ROOT, scripts, args.timeout, max(1, args.jobs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
