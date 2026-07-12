#!/usr/bin/env python3
"""Audit the fail-closed manifest and pinned complete Modal replay."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from run_all_verifiers import self_test, validate_manifest  # noqa: E402


MANIFEST = ROOT / "tools" / "verifier_manifest.json"
REPLAY = ROOT / "experiments" / "prize_resolution" / "modal_verifier_replay.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    errors = validate_manifest(ROOT, manifest)
    if errors:
        raise AssertionError(errors)
    self_test()

    replay = json.loads(REPLAY.read_text())
    manifest_hash = digest(MANIFEST)
    if replay.get("manifest_sha256") != manifest_hash:
        raise AssertionError("replay used a different manifest")
    if not replay.get("complete") or replay.get("match") != "":
        raise AssertionError("replay is partial")

    rows = {row["script"]: row for row in replay["results"]}
    if set(rows) != set(manifest["scripts"]):
        raise AssertionError("replay script set differs from manifest")
    for rel, expected_hash in manifest["scripts"].items():
        row = rows[rel]
        if row.get("status") != "PASS" or row.get("returncode") != 0:
            raise AssertionError((rel, row.get("status"), row.get("returncode")))
        if row.get("sha256") != expected_hash:
            raise AssertionError((rel, "remote hash mismatch"))

    print(
        "HARNESS_AUDIT_PASS "
        f"verifiers={len(rows)} remote_launchers={len(manifest['remote_launchers'])} "
        "negative_controls=6"
    )


if __name__ == "__main__":
    main()
