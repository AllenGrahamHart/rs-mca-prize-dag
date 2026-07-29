#!/usr/bin/env python3
"""Add an exact 16-bit-dyadic upper-product cap to an m16 worker."""

from __future__ import annotations

from pathlib import Path
import sys


INSERT = r'''
static int u128_bits(unsigned __int128 value) {
    const uint64_t high = static_cast<uint64_t>(value >> 64);
    if (high) return 128 - __builtin_clzll(high);
    const uint64_t low = static_cast<uint64_t>(value);
    return low ? 64 - __builtin_clzll(low) : 0;
}

static bool shifted_less_than(
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

static int coarse_cap_norm_relation(
    const Support& support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>& heavy_support,
    const std::array<int, 3>& heavy_signs
) {
    constexpr int64_t error = 12;
    cpp_int coarse_upper = 1;
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
        const int shift = std::max(u128_bits(square) - 16, 0);
        unsigned __int128 mantissa = square >> shift;
        if ((mantissa << shift) != square) ++mantissa;
        coarse_upper *= from_u128(mantissa);
        binary_exponent += shift;
    }
    static const cpp_int prize_floor = [] {
        cpp_int value("317494674775468773183020924238786383963");
        value <<= 132 + 2 * 48 * 64;
        return value;
    }();
    if (shifted_less_than(coarse_upper, binary_exponent, prize_floor)) {
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
    marker = "static const std::array<std::array<long double, 128>, 64>& root_real() {"
    call = "const int fixed_relation = fixed_norm_relation("
    assert text.count(marker) == 1 and text.count(call) == 1
    text = text.replace(marker, INSERT + marker, 1)
    text = text.replace(call, "const int fixed_relation = coarse_cap_norm_relation(", 1)
    path.write_text(text)


if __name__ == "__main__":
    main()
