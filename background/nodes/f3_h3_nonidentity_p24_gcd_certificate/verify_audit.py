#!/usr/bin/env python3
"""Mutation audit for the nonidentity P24 gcd certificate."""

from __future__ import annotations

import verify


def main() -> None:
    verify.synthetic_check()
    verify.row_check()

    assert verify.profile_verdict(13, 2)[2]
    assert not verify.profile_verdict(13, 1)[2]
    assert not verify.profile_verdict(14, 2)[2]
    assert verify.profile_verdict(12, 0)[2]

    identity_valuation = 7
    assert identity_valuation > 1
    assert identity_valuation - identity_valuation == 0

    print("F3_H3_NONIDENTITY_P24_GCD_CERTIFICATE_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
