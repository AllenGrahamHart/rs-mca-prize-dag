#!/usr/bin/env python3
"""Independent audit of the reduced B-WEAK assembly verifier."""

from __future__ import annotations

import verify_reduced_assembly as primary


def main() -> None:
    result = primary.build()
    assert result["parent_status"] == "CONDITIONAL"
    assert result["c2_status"] != "PROVED"
    assert result["baseline_status"] != "PROVED"
    assert result["scope_status"] == "PROVED"
    assert 2 ** result["joint_bits"] * 2 ** result["baseline_bits"] == 2 ** result["endpoint_bits"]
    print("DLI_REDUCED_ASSEMBLY_AUDIT_PASS")


if __name__ == "__main__":
    main()
