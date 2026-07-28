#!/usr/bin/env python3
"""Insert an independent exact Walsh energy ledger into the reverse audit."""

from __future__ import annotations

from pathlib import Path
import sys


TRIPLE_MARKER = "        for (size_t first_index = 0; first_index < allowed.size(); ++first_index) {"
PRECOMPUTE = r'''        std::array<int, 128> fast_cross_norm{};
        std::array<int, 128> fast_base_cross{};
        std::vector<int> fast_cross_dot(128 * 128, 0);
        int fast_base_energy = 0;
        for (int lag = 1; lag < 64; ++lag) {
            fast_base_energy += singleton_correlation[lag] * singleton_correlation[lag];
        }
        for (const int position : allowed) {
            for (int lag = 1; lag < 64; ++lag) {
                const int value = 2 * cross[position][sign_code][lag];
                fast_cross_norm[position] += value * value;
                fast_base_cross[position] += singleton_correlation[lag] * value;
            }
        }
        for (size_t left_index = 0; left_index < allowed.size(); ++left_index) {
            const int left = allowed[left_index];
            for (size_t right_index = left_index + 1; right_index < allowed.size(); ++right_index) {
                const int right = allowed[right_index];
                int value = 0;
                for (int lag = 1; lag < 64; ++lag) {
                    value += 4
                        * cross[left][sign_code][lag]
                        * cross[right][sign_code][lag];
                }
                fast_cross_dot[left * 128 + right] = value;
                fast_cross_dot[right * 128 + left] = value;
            }
        }

'''

START = "                    std::array<int, 8> energies{};"
END = "                    for (int heavy_code = 7; heavy_code >= 0; --heavy_code) {\n                        const int candidate_energy"
REPLACEMENT = r'''                    std::array<int, 8> energies{};
                    std::array<int, 8> l1_norms{};
                    const auto cross_value = [&](int position, int lag) {
                        return 2 * cross[position][sign_code][lag];
                    };
                    const auto sparse_base = [&](int pair) {
                        return pair_lags[pair]
                            ? 4 * pair_orientations[pair]
                                * singleton_correlation[pair_lags[pair]]
                            : 0;
                    };
                    const auto sparse_cross = [&](int position, int pair) {
                        return pair_lags[pair]
                            ? 4 * pair_orientations[pair]
                                * cross_value(position, pair_lags[pair])
                            : 0;
                    };
                    const auto sparse_pair = [&](int left, int right) {
                        return pair_lags[left] && pair_lags[left] == pair_lags[right]
                            ? 16 * pair_orientations[left] * pair_orientations[right]
                            : 0;
                    };
                    const auto cross_dot = [&](int left, int right) {
                        return fast_cross_dot[left * 128 + right];
                    };

                    const int first_heavy = heavy_support[0];
                    const int second_heavy = heavy_support[1];
                    const int third_heavy = heavy_support[2];
                    const int coefficient_0 = fast_base_energy
                        + fast_cross_norm[first_heavy]
                        + fast_cross_norm[second_heavy]
                        + fast_cross_norm[third_heavy]
                        + (pair_lags[0] ? 16 : 0)
                        + (pair_lags[1] ? 16 : 0)
                        + (pair_lags[2] ? 16 : 0);
                    const int coefficient_1 = 2 * (
                        fast_base_cross[first_heavy]
                        + sparse_cross(second_heavy, 0) + sparse_cross(third_heavy, 1)
                    );
                    const int coefficient_2 = 2 * (
                        fast_base_cross[second_heavy]
                        + sparse_cross(first_heavy, 0) + sparse_cross(third_heavy, 2)
                    );
                    const int coefficient_4 = 2 * (
                        fast_base_cross[third_heavy]
                        + sparse_cross(first_heavy, 1) + sparse_cross(second_heavy, 2)
                    );
                    const int coefficient_3 = 2 * (
                        sparse_base(0) + cross_dot(first_heavy, second_heavy)
                        + sparse_pair(1, 2)
                    );
                    const int coefficient_5 = 2 * (
                        sparse_base(1) + cross_dot(first_heavy, third_heavy)
                        + sparse_pair(0, 2)
                    );
                    const int coefficient_6 = 2 * (
                        sparse_base(2) + cross_dot(second_heavy, third_heavy)
                        + sparse_pair(0, 1)
                    );
                    const int coefficient_7 = 2 * (
                        sparse_cross(first_heavy, 2)
                        + sparse_cross(second_heavy, 1)
                        + sparse_cross(third_heavy, 0)
                    );
                    for (int heavy_code = 0; heavy_code < 8; ++heavy_code) {
                        const int x = (heavy_code & 1) ? -1 : 1;
                        const int y = (heavy_code & 2) ? -1 : 1;
                        const int z = (heavy_code & 4) ? -1 : 1;
                        energies[heavy_code] = coefficient_0
                            + x * coefficient_1 + y * coefficient_2
                            + z * coefficient_4 + x * y * coefficient_3
                            + x * z * coefficient_5 + y * z * coefficient_6
                            + x * y * z * coefficient_7;
                        if (energies[heavy_code] > limit) continue;
                        int replay_energy = 0;
                        for (int lag = 1; lag < 64; ++lag) {
                            const int value = singleton_correlation[lag]
                                + x * cross_value(first_heavy, lag)
                                + y * cross_value(second_heavy, lag)
                                + z * cross_value(third_heavy, lag)
                                + x * y * (pair_lags[0] == lag
                                    ? 4 * pair_orientations[0] : 0)
                                + x * z * (pair_lags[1] == lag
                                    ? 4 * pair_orientations[1] : 0)
                                + y * z * (pair_lags[2] == lag
                                    ? 4 * pair_orientations[2] : 0);
                            replay_energy += value * value;
                            l1_norms[heavy_code] += std::abs(value);
                        }
                        if (replay_energy != energies[heavy_code]) std::exit(41);
                    }
'''


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text()
    assert text.count(TRIPLE_MARKER) == 1
    assert text.count(START) == 1 and text.count(END) == 1
    text = text.replace(TRIPLE_MARKER, PRECOMPUTE + TRIPLE_MARKER, 1)
    start = text.index(START)
    end = text.index(END, start)
    text = text[:start] + REPLACEMENT + text[end:]
    path.write_text(text)


if __name__ == "__main__":
    main()
