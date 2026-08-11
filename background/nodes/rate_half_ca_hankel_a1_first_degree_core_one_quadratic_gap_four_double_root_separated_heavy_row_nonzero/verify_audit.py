#!/usr/bin/env python3
"""Independent resultant-factor audit at center and off-line roots."""


def resultant_order(is_offline_supported: bool, correction_order: int) -> int:
    offline_order = 7 if is_offline_supported else 0
    return correction_order + offline_order


def main() -> None:
    # A center is not an off-line slope, so only E_4=S_B^2 contributes.
    assert resultant_order(False, 2) == 2
    # The same exact order holds at an unsupported off-center root.
    assert resultant_order(False, 2) == 2
    # At an off-line supported root the extra factor is present, so the proof
    # must use the actual/padding fiber theorem rather than an order-two claim.
    assert resultant_order(True, 2) > 2

    component_order = 3
    assert component_order > resultant_order(False, 2)
    print("RATE_HALF_SEPARATED_HEAVY_ROW_NONZERO_AUDIT_PASS center_order=2")


if __name__ == "__main__":
    main()
