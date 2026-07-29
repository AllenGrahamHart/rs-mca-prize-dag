#!/usr/bin/env python3
"""Add an exact upper-product precheck to the primitive reverse audit."""

from __future__ import annotations

from pathlib import Path
import sys


INSERT = r'''
static bool reverse_shifted_less_than(
    const cpp_int& value, int binary_exponent, const cpp_int& threshold
) {
    if (value == 0) return true;
    const int value_top = static_cast<int>(boost::multiprecision::msb(value))
        + binary_exponent;
    const int threshold_top =
        static_cast<int>(boost::multiprecision::msb(threshold));
    if (value_top != threshold_top) return value_top < threshold_top;
    return (value << binary_exponent) < threshold;
}

static int reverse_upper_cap_norm_relation(
    const Support& support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>& heavy_support,
    const std::array<int, 3>& heavy_signs
) {
    constexpr int64_t error = 12;
    cpp_int dummy_lower = 0;
    cpp_int upper_product = 1;
    int binary_exponent = 0;
    for (int root = 0; root < 64; ++root) {
        int64_t real = 0;
        int64_t imaginary = 0;
        for (int index = 0; index < 6; ++index) {
            real += singleton_signs[index] * M64_FIXED_REAL[root][support[index]];
            imaginary += singleton_signs[index] * M64_FIXED_IMAG[root][support[index]];
        }
        for (int index = 0; index < 3; ++index) {
            real += 2 * heavy_signs[index] * M64_FIXED_REAL[root][heavy_support[index]];
            imaginary += 2 * heavy_signs[index] * M64_FIXED_IMAG[root][heavy_support[index]];
        }
        const uint64_t upper_real =
            static_cast<uint64_t>(std::llabs(real)) + error;
        const uint64_t upper_imaginary =
            static_cast<uint64_t>(std::llabs(imaginary)) + error;
        const unsigned __int128 square =
            static_cast<unsigned __int128>(upper_real) * upper_real
            + static_cast<unsigned __int128>(upper_imaginary) * upper_imaginary;
        upper_product *= from_u128(square);
        normalize_product_interval(dummy_lower, upper_product, binary_exponent);
    }
    static const cpp_int prize_floor = [] {
        cpp_int value("317494674775468773183020924238786383963");
        value <<= 132 + 2 * 48 * 64;
        return value;
    }();
    if (reverse_shifted_less_than(
            upper_product, binary_exponent, prize_floor
        )) {
        return -1;
    }
    return fixed_norm_relation(
        support, singleton_signs, heavy_support, heavy_signs
    );
}

'''


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text()
    marker = "static void reverse_audit_orbit("
    call = "const int relation = fixed_norm_relation("
    assert text.count(marker) == 1 and text.count(call) == 1
    text = text.replace(marker, INSERT + marker, 1)
    text = text.replace(call, "const int relation = reverse_upper_cap_norm_relation(", 1)
    path.write_text(text)


if __name__ == "__main__":
    main()
