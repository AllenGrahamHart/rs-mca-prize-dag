#!/usr/bin/env python3
"""Independent set-theoretic audit of the squarefree center gcd."""


def main() -> None:
    center = {"alpha", "beta", "theta"}
    profiles = [set(), {"alpha"}, {"beta"}, {"theta"}]
    checks = 0
    for g_roots in profiles:
        correction_profiles = [set(), *({root} for root in sorted(g_roots))]
        for correction_roots in correction_profiles:
            assert correction_roots <= g_roots
            gcd_roots = center & (g_roots | correction_roots)
            assert gcd_roots == g_roots
            assert len(gcd_roots) == len(g_roots)
            checks += 1

    assert checks == 7
    print("RATE_HALF_SQUAREFREE_EXACT_DEFICIT_LEDGER_AUDIT_PASS checks=7")


if __name__ == "__main__":
    main()
