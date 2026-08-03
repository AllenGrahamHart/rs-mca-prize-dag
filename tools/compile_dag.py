#!/usr/bin/env python3
"""Build or check the generated dag.json compatibility artifact."""

from __future__ import annotations

import argparse

from dag_manifest import (
    DAG,
    ROOT,
    ManifestError,
    canonical_dag_text,
    load_manifest_graph,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        expected = canonical_dag_text(ROOT)
    except (ManifestError, ValueError) as error:
        print(f"DAG_MANIFEST_FAIL {error}")
        return 1
    actual = DAG.read_text() if DAG.is_file() else ""
    if args.write:
        temporary = DAG.with_suffix(".json.tmp")
        temporary.write_text(expected)
        temporary.replace(DAG)
        dag = load_manifest_graph(ROOT)
        print(
            f"DAG_COMPILED nodes={len(dag['nodes'])} edges={len(dag['edges'])} "
            f"bytes={len(expected.encode())}"
        )
        return 0
    if actual != expected:
        print(
            "DAG_MANIFEST_STALE run "
            "tools/ramguard tiny -- python3 tools/compile_dag.py --write"
        )
        return 1
    print(f"DAG_MANIFEST_PASS bytes={len(expected.encode())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
