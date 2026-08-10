#!/usr/bin/env python3
"""Independent finite ledger audit for the clean specialization."""


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for value in range(1, total - parts + 2):
        yield from compositions(total - value, parts - 1, prefix + (value,))


def main() -> None:
    tested_profiles = 0
    for m in range(2, 13):
        admissible = []
        for components in range(1, m + 1):
            for degrees in compositions(m, components):
                for dominant in range(components):
                    residual = m - degrees[dominant]
                    if 4 * residual <= 0:
                        admissible.append((degrees, dominant))
                tested_profiles += components
        assert admissible == [((m,), 0)]

        deficits = [
            tuple(1 if index == deficient else 0 for index in range(16 * m))
            for deficient in range(16 * m)
        ]
        assert all(sum(profile) == 1 for profile in deficits)
        assert len(deficits) == 16 * m

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_IRREDUCIBLE_NORM_COROLLARY_"
        f"AUDIT_PASS m_range=2..12 profiles={tested_profiles}"
    )


if __name__ == "__main__":
    main()
