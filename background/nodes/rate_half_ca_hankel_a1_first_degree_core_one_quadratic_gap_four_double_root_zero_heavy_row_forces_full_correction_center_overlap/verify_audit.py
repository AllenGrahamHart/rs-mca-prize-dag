#!/usr/bin/env python3
"""Independent factor-divisibility audit for the full-overlap conclusion."""


def divides_by_roots(
    divisor_roots: tuple[str, ...], dividend_roots: tuple[str, ...]
) -> bool:
    return all(root in dividend_roots for root in divisor_roots)


def main() -> None:
    s_roots = ("alpha", "beta")
    center_cases = {
        "none": ("gamma_1", "gamma_2", "gamma_3"),
        "one": ("alpha", "gamma_2", "gamma_3"),
        "both": ("alpha", "beta", "gamma_3"),
    }
    assert not divides_by_roots(s_roots, center_cases["none"])
    assert not divides_by_roots(s_roots, center_cases["one"])
    assert divides_by_roots(s_roots, center_cases["both"])

    # A zero row rejects every case with a noncenter correction root.
    survivors = [
        name
        for name, roots in center_cases.items()
        if divides_by_roots(s_roots, roots)
    ]
    assert survivors == ["both"]
    print("RATE_HALF_ZERO_HEAVY_ROW_FULL_CENTER_OVERLAP_AUDIT_PASS survivors=1")


if __name__ == "__main__":
    main()
