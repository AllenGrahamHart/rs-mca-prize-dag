#!/usr/bin/env python3
"""Verify the official abstract-code route-cut arithmetic."""


N = 1 << 41
LENGTH = N // 4
T_UPPER = N // 128 - 2
E = N // 8
D = E - T_UPPER - 1


def main() -> None:
    assert T_UPPER > 0 and D > 0
    assert T_UPPER <= LENGTH // 32
    assert T_UPPER + 1 < 1 << 35

    volume_log_upper = 7 * LENGTH // 32 + 35
    code_log_lower = LENGTH - volume_log_upper
    target_log = 4 + 3 * 41
    assert target_log == 127
    assert code_log_lower > target_log

    assert E == T_UPPER + D + 1
    assert 4 * E * E <= N * (E + D)
    assert N // 2 - T_UPPER >= 2 * E
    print(
        "X4_JOHNSON_NONPOSITIVE_ABSTRACT_CODE_ROUTE_CUT_PASS "
        f"length={LENGTH} t_upper={T_UPPER} code_log_lower={code_log_lower}"
    )


if __name__ == "__main__":
    main()
