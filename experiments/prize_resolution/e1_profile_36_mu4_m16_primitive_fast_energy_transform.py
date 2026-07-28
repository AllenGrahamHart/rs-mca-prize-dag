#!/usr/bin/env python3
"""Replace the primitive m16 lagwise energy loop by an exact Walsh ledger."""

from __future__ import annotations

from pathlib import Path
import sys


OUTER_MARKER = "    for (size_t first_index = 0; first_index < allowed.size(); ++first_index) {"
PRECOMPUTE = r'''    std::array<int, 32> fast_base_energy{};
    std::array<std::array<int, 128>, 32> fast_cross_norm{};
    std::array<std::array<int, 128>, 32> fast_base_cross{};
    std::vector<int> fast_cross_dot(32 * 128 * 128, 0);
    const auto fast_dot_index = [](int sign_mask, int left, int right) {
        return (sign_mask * 128 + left) * 128 + right;
    };
    for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
        for (int lag = 1; lag < 64; ++lag) {
            const int base = singleton_correlations[sign_mask][lag];
            fast_base_energy[sign_mask] += base * base;
        }
        for (const int position : allowed) {
            for (int lag = 1; lag < 64; ++lag) {
                const int value = 2 * singleton_heavy[position][sign_mask][lag];
                fast_cross_norm[sign_mask][position] += value * value;
                fast_base_cross[sign_mask][position] +=
                    singleton_correlations[sign_mask][lag] * value;
            }
        }
        for (size_t left_index = 0; left_index < allowed.size(); ++left_index) {
            const int left = allowed[left_index];
            for (size_t right_index = left_index + 1; right_index < allowed.size(); ++right_index) {
                const int right = allowed[right_index];
                int value = 0;
                for (int lag = 1; lag < 64; ++lag) {
                    value += 4
                        * singleton_heavy[left][sign_mask][lag]
                        * singleton_heavy[right][sign_mask][lag];
                }
                fast_cross_dot[fast_dot_index(sign_mask, left, right)] = value;
                fast_cross_dot[fast_dot_index(sign_mask, right, left)] = value;
            }
        }
    }

'''

START = "                    std::array<int, 8> candidate_energies{};"
END = "                    for (int heavy_mask = 0; heavy_mask < 8; ++heavy_mask) {\n                        const int candidate_energy"
REPLACEMENT = r'''                    std::array<int, 8> candidate_energies{};
                    std::array<int, 8> l1_norms{};
                    const auto cross_value = [&](int position, int lag) {
                        return 2 * singleton_heavy[position][sign_mask][lag];
                    };
                    const auto sparse_base = [&](int pair) {
                        return heavy_pair_lag[pair]
                            ? 4 * heavy_pair_orientation[pair]
                                * singleton_correlations[sign_mask][heavy_pair_lag[pair]]
                            : 0;
                    };
                    const auto sparse_cross = [&](int position, int pair) {
                        return heavy_pair_lag[pair]
                            ? 4 * heavy_pair_orientation[pair]
                                * cross_value(position, heavy_pair_lag[pair])
                            : 0;
                    };
                    const auto sparse_pair = [&](int left, int right) {
                        return heavy_pair_lag[left]
                            && heavy_pair_lag[left] == heavy_pair_lag[right]
                            ? 16 * heavy_pair_orientation[left]
                                * heavy_pair_orientation[right]
                            : 0;
                    };
                    const auto cross_dot = [&](int left, int right) {
                        return fast_cross_dot[fast_dot_index(sign_mask, left, right)];
                    };

                    const int coefficient_0 = fast_base_energy[sign_mask]
                        + fast_cross_norm[sign_mask][first]
                        + fast_cross_norm[sign_mask][second]
                        + fast_cross_norm[sign_mask][third]
                        + (heavy_pair_lag[0] ? 16 : 0)
                        + (heavy_pair_lag[1] ? 16 : 0)
                        + (heavy_pair_lag[2] ? 16 : 0);
                    const int coefficient_1 = 2 * (
                        fast_base_cross[sign_mask][first]
                        + sparse_cross(second, 0) + sparse_cross(third, 1)
                    );
                    const int coefficient_2 = 2 * (
                        fast_base_cross[sign_mask][second]
                        + sparse_cross(first, 0) + sparse_cross(third, 2)
                    );
                    const int coefficient_4 = 2 * (
                        fast_base_cross[sign_mask][third]
                        + sparse_cross(first, 1) + sparse_cross(second, 2)
                    );
                    const int coefficient_3 = 2 * (
                        sparse_base(0) + cross_dot(first, second)
                        + sparse_pair(1, 2)
                    );
                    const int coefficient_5 = 2 * (
                        sparse_base(1) + cross_dot(first, third)
                        + sparse_pair(0, 2)
                    );
                    const int coefficient_6 = 2 * (
                        sparse_base(2) + cross_dot(second, third)
                        + sparse_pair(0, 1)
                    );
                    const int coefficient_7 = 2 * (
                        sparse_cross(first, 2) + sparse_cross(second, 1)
                        + sparse_cross(third, 0)
                    );
                    for (int heavy_mask = 0; heavy_mask < 8; ++heavy_mask) {
                        const int x = (heavy_mask & 1) ? -1 : 1;
                        const int y = (heavy_mask & 2) ? -1 : 1;
                        const int z = (heavy_mask & 4) ? -1 : 1;
                        candidate_energies[heavy_mask] = coefficient_0
                            + x * coefficient_1 + y * coefficient_2
                            + z * coefficient_4 + x * y * coefficient_3
                            + x * z * coefficient_5 + y * z * coefficient_6
                            + x * y * z * coefficient_7;
                        if (candidate_energies[heavy_mask] > limit) continue;
                        int replay_energy = 0;
                        for (int lag = 1; lag < 64; ++lag) {
                            const int value = singleton_correlations[sign_mask][lag]
                                + x * cross_value(first, lag)
                                + y * cross_value(second, lag)
                                + z * cross_value(third, lag)
                                + x * y * (heavy_pair_lag[0] == lag
                                    ? 4 * heavy_pair_orientation[0] : 0)
                                + x * z * (heavy_pair_lag[1] == lag
                                    ? 4 * heavy_pair_orientation[1] : 0)
                                + y * z * (heavy_pair_lag[2] == lag
                                    ? 4 * heavy_pair_orientation[2] : 0);
                            replay_energy += value * value;
                            l1_norms[heavy_mask] += std::abs(value);
                        }
                        if (replay_energy != candidate_energies[heavy_mask]) std::exit(41);
                    }
'''


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text()
    assert text.count(OUTER_MARKER) == 1
    assert text.count(START) == 1 and text.count(END) == 1
    text = text.replace(OUTER_MARKER, PRECOMPUTE + OUTER_MARKER, 1)
    start = text.index(START)
    end = text.index(END, start)
    text = text[:start] + REPLACEMENT + text[end:]
    path.write_text(text)


if __name__ == "__main__":
    main()
