#!/usr/bin/env python3
"""Verify the official_row_primes_pinning reframe packet.

The packet closes the old "missing literal official primes" ask by citation:
ABF26 quantifies over admissible fields rather than naming a finite official
prime list.  The verifier intentionally does not require the full PDF to live
in this minimal DAG tree, but if the recorded PDF path exists it checks the
sha256.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NODE = ROOT / "nodes" / "official_row_primes_pinning"
CERT = NODE / "official_row_primes_reframe.json"
PROOF = NODE / "proof.md"

EXPECTED_SHA = "426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5"
REQUIRED_FRAGMENTS = {
    "assuming |F| is sufficiently large",
    "for every choice of F, L, and k",
    "k <= 2^40",
    "|F| < 2^256",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    errors: list[str] = []
    if not CERT.exists():
        raise SystemExit(f"missing certificate: {CERT}")
    if not PROOF.exists():
        raise SystemExit(f"missing proof packet: {PROOF}")

    cert = json.loads(CERT.read_text())
    if cert.get("node") != "official_row_primes_pinning":
        errors.append("certificate node mismatch")
    if cert.get("verdict") != "no_fixed_official_primes":
        errors.append("unexpected verdict")

    source = cert.get("source", {})
    if source.get("sha256") != EXPECTED_SHA:
        errors.append("source sha256 does not match pinned ABF26 hash")
    if source.get("page") != 5:
        errors.append("source page must be ABF26 p.5")

    fragments = set(cert.get("quote_fragments", []))
    missing = sorted(REQUIRED_FRAGMENTS - fragments)
    if missing:
        errors.append("missing quote fragments: " + ", ".join(missing))

    consequence = cert.get("consequence", {})
    if "uniform" not in consequence.get("certificate_obligation", ""):
        errors.append("certificate obligation must mention uniform certificates")
    if "exhibit" not in consequence.get("certificate_obligation", ""):
        errors.append("certificate obligation must mention exhibit certificates")

    pdf_path = Path(source.get("verified_from", ""))
    if pdf_path.exists() and sha256(pdf_path) != EXPECTED_SHA:
        errors.append(f"PDF exists but hash mismatch: {pdf_path}")

    proof = PROOF.read_text()
    for needle in [
        "no finite list",
        "family-uniform",
        "exhibit-specific",
        "No additional prime list",
    ]:
        if needle not in proof:
            errors.append(f"proof packet missing phrase: {needle}")

    if errors:
        print("FAIL official_row_primes_pinning verifier")
        for err in errors:
            print(" -", err)
        raise SystemExit(1)

    print("PASS official_row_primes_pinning reframe packet")
    print(f"verified {CERT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
