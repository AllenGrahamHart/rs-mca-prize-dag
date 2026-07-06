#!/usr/bin/env python3
"""Tiny route-shape validator for the E1 open-cell payload."""

from __future__ import annotations

OPEN_CELLS = {128, 256}


def accepts(payload: dict) -> bool:
    route = payload["route"]
    cells = set(payload["cells"])
    if cells != OPEN_CELLS:
        return False
    if route == "uniform_typicality":
        return bool(payload.get("theorem")) and payload.get("uniform") is True
    if route == "named_folded_certificates":
        certs = payload.get("certificates", {})
        return all(
            n in certs
            and certs[n].get("field")
            and certs[n].get("complete") is True
            and certs[n].get("nonzero_folded_vectors") == 0
            for n in OPEN_CELLS
        )
    return False


def main() -> None:
    assert accepts(
        {
            "route": "uniform_typicality",
            "cells": [128, 256],
            "uniform": True,
            "theorem": "admissible-family exceptional incidence is negligible",
        }
    )
    assert accepts(
        {
            "route": "named_folded_certificates",
            "cells": [128, 256],
            "certificates": {
                128: {
                    "field": "named-exhibit-128",
                    "complete": True,
                    "nonzero_folded_vectors": 0,
                },
                256: {
                    "field": "named-exhibit-256",
                    "complete": True,
                    "nonzero_folded_vectors": 0,
                },
            },
        }
    )
    assert not accepts({"route": "named_folded_certificates", "cells": [128]})
    print("PASS: E1 open-cell route shapes validated")


if __name__ == "__main__":
    main()
