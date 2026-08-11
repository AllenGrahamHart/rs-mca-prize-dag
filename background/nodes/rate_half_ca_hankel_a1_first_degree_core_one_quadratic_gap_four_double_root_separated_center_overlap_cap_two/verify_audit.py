#!/usr/bin/env python3
"""Independent exhaustive bitmask audit of the j<=2 cap."""


def bit_count(value: int) -> int:
    return bin(value).count("1")


def main() -> None:
    # Bits alpha,beta,theta. Correction may use only theta; padding has
    # capacity one; separatedness makes the masks disjoint.
    survivors = []
    for correction in range(8):
        for padded in range(8):
            if correction & 0b011:
                continue
            if bit_count(correction) > 1 or bit_count(padded) > 1:
                continue
            if correction & padded:
                continue
            overlap = bit_count(correction | padded)
            assert overlap <= 2
            survivors.append((correction, padded, overlap))

    assert max(item[2] for item in survivors) == 2
    assert all(item[2] != 3 for item in survivors)
    print(
        "RATE_HALF_SEPARATED_CENTER_OVERLAP_CAP_TWO_AUDIT_PASS",
        f"survivors={len(survivors)}",
    )


if __name__ == "__main__":
    main()
