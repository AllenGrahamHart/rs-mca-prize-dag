#!/usr/bin/env python3
"""Audit the vendored Tier-1 Lean package and optional low-memory build."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "formal" / "lean" / "rs_mca_formalization"
CERT = PACKAGE / "BUILD_CERTIFICATE.json"
EXPECTED_TREE = "1668d2aafc37619914ae432161c35de5d47056784ea914807062678c00435ef3"


def tree_digest() -> str:
    names = [
        path
        for path in PACKAGE.rglob("*")
        if path.is_file()
        and (
            path.suffix == ".lean"
            or path.name
            in {"lean-toolchain", "lakefile.lean", "lake-manifest.json", "CERTIFICATION_MAP.md", "README.md"}
        )
    ]
    ledger = "".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}\n"
        for path in sorted(names, key=lambda item: item.relative_to(ROOT).as_posix())
    )
    return hashlib.sha256(ledger.encode()).hexdigest()


def strip_comments(text: str) -> str:
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"/-.*?-/", "", text, flags=re.S)
    return re.sub(r"--.*", "", text)


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["source_tree_sha256"] == EXPECTED_TREE
    assert tree_digest() == EXPECTED_TREE
    assert cert["toolchain"] == (PACKAGE / "lean-toolchain").read_text().strip()
    assert cert["result"].startswith("PASS")

    high = (PACKAGE / "RsMca" / "HighAgreementLedger.lean").read_text()
    finite = (PACKAGE / "RsMca" / "FiniteThreshold.lean").read_text()
    for theorem in (
        "f17_lower_add_certificate",
        "f17_upper_add_certificate",
        "f17_bracket_from_add_certificates",
        "f17_BQ_eq",
        "f17_staircase",
        "f17_endpoint_conversions",
    ):
        assert f"theorem {theorem}" in high
    assert "theorem field_count_gate" in finite
    assert "theorem safe_iff_agreement_ge_507" in finite

    all_lean = "\n".join(path.read_text() for path in PACKAGE.rglob("*.lean"))
    assert not re.search(r"\b(sorry|admit)\b", strip_comments(all_lean))
    cert_map = (PACKAGE / "CERTIFICATION_MAP.md").read_text()
    assert "Typed Targets And Non-Claims" in cert_map
    assert "this map is not a blanket proof" in cert_map

    if "--build" in sys.argv:
        subprocess.run([str(Path.home() / ".elan" / "bin" / "lake"), "-Kjobs=1", "build"], cwd=PACKAGE, check=True)
    print("LEAN_TIER1_AUDIT_PASS theorems=8 tree_hash=pinned typed_targets=nonclaims")


if __name__ == "__main__":
    main()
