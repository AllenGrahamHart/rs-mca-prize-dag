#!/usr/bin/env python3
"""Mechanically add the rigorous early-cap interval screen to an m16 worker."""

from __future__ import annotations

from pathlib import Path
import sys


INSERT = r'''
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

static int early_cap_norm_relation(
    const Support& support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>& heavy_support,
    const std::array<int, 3>& heavy_signs
) {
    constexpr int64_t error = 12;
    std::array<unsigned __int128, 64> upper_squares{};
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
        upper_squares[root] =
            static_cast<unsigned __int128>(upper_real) * upper_real
            + static_cast<unsigned __int128>(upper_imaginary) * upper_imaginary;
    }
    std::sort(upper_squares.begin(), upper_squares.end());
    static const auto powers_of_nine = [] {
        std::array<cpp_int, 65> result{};
        result[0] = 1;
        for (int index = 1; index <= 64; ++index) result[index] = 9 * result[index - 1];
        return result;
    }();
    static const cpp_int prize_floor = [] {
        cpp_int value("317494674775468773183020924238786383963");
        value <<= 132 + 2 * 48 * 64;
        return value;
    }();
    cpp_int dummy_lower = 0;
    cpp_int upper_product = 1;
    int binary_exponent = 0;
    for (int used = 1; used <= 64; ++used) {
        upper_product *= from_u128(upper_squares[used - 1]);
        normalize_product_interval(dummy_lower, upper_product, binary_exponent);
        const int remaining = 64 - used;
        const cpp_int capped_product = upper_product * powers_of_nine[remaining];
        if (shifted_less_than(
                capped_product,
                binary_exponent + 100 * remaining,
                prize_floor
            )) {
            return -1;
        }
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
    text = text.replace(call, "const int fixed_relation = early_cap_norm_relation(", 1)
    path.write_text(text)


if __name__ == "__main__":
    main()
