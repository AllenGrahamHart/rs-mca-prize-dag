#!/usr/bin/env python3
"""Check the exact 23+38+8 partition of the 69 exceptional fibers."""

import hashlib
import sys
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_guard_norms as guards
import check_rate_half_kb_positive_433_1a_cell5_specialization_poles as poles
import check_rate_half_kb_positive_433_1a_cell5_dynamic_fiber_replay as dynamic
import check_rate_half_kb_positive_433_1a_cell5_raw_fiber_replay as raw
import probe_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch as first


EXPECTED_ROUTER_SHA256 = (
    "bd64dc238bb3dcc4491d7d7b856078871336571cbdd5df3343014f8198cfe1d4"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def verify(first_values=None, dynamic_values=None, raw_values=None):
    forbidden = {0, 1, poles.PRIME - 1, 16711679, poles.PRIME - 16711679}
    router = guards.verify() | (poles.verify() - forbidden)
    require(len(router) == 69, "router size mismatch")
    digest = hashlib.sha256(",".join(map(str, sorted(router))).encode()).hexdigest()
    require(digest == EXPECTED_ROUTER_SHA256, "router digest mismatch")
    parts = (
        set(first.ROUTES if first_values is None else first_values),
        set(dynamic.FIBERS if dynamic_values is None else dynamic_values),
        set(raw.FIBERS if raw_values is None else raw_values),
    )
    require(tuple(map(len, parts)) == (23, 38, 8), "partition sizes mismatch")
    require(not (parts[0] & parts[1] or parts[0] & parts[2] or parts[1] & parts[2]), "partition overlap")
    require(set.union(*parts) == router, "partition does not cover router")
    return router


def main():
    router = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_COMPLETE_SIGN_ROW_PASS "
        f"router={len(router)} partition=23,38,8 sha256={EXPECTED_ROUTER_SHA256}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_COMPLETE_SIGN_ROW_FAIL {error}")
        raise SystemExit(1)
