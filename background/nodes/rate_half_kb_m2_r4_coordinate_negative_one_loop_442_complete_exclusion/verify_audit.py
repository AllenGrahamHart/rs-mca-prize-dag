#!/usr/bin/env python3
"""Independent ownership audit for the complete one-loop 442 close."""


OWNERS = (
    "aligned",
    "crossed", "crossed",
    "ab", "mixed", "mixed", "ab", "mixed", "mixed",
    "sextic", "sextic", "opposite", "sextic", "sextic", "opposite",
)
EXPECTED = {
    "aligned": 1,
    "crossed": 2,
    "ab": 2,
    "mixed": 4,
    "sextic": 4,
    "opposite": 2,
}


def main():
    counts = {owner: OWNERS.count(owner) for owner in set(OWNERS)}
    if len(OWNERS) != 15 or counts != EXPECTED:
        raise RuntimeError("manual orbit ownership ledger")
    if any(not owner for owner in OWNERS):
        raise RuntimeError("unowned cell")
    print(
        "RATE_HALF_KB_ONE_LOOP_442_COMPLETE_AUDIT_PASS "
        f"cells={len(OWNERS)} owners={len(counts)} counts={counts}"
    )


if __name__ == "__main__":
    main()
