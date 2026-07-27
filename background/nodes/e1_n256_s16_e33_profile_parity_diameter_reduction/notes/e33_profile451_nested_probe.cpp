#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>

namespace {

constexpr int kModulus = 32;

uint32_t orbit_mask(int representative) {
    return (uint32_t{1} << representative)
        | (uint32_t{1} << ((kModulus - representative) % kModulus));
}

int fiber(uint32_t left, uint32_t right, int target) {
    int count = 0;
    for (int value = 0; value < kModulus; ++value) {
        if (((left >> value) & 1U) == 0U) {
            continue;
        }
        const int partner = (target - value + kModulus) % kModulus;
        count += static_cast<int>((right >> partner) & 1U);
    }
    return count;
}

int triple(uint32_t left, uint32_t right, uint32_t third) {
    int total = 0;
    for (int value = 0; value < kModulus; ++value) {
        if ((third >> value) & 1U) {
            total += fiber(left, right, (kModulus - value) % kModulus);
        }
    }
    return total;
}

int weighted_moment_128(const std::array<int, 128>& weights) {
    int total = 0;
    for (int left = 0; left < 128; ++left) {
        if (weights[left] == 0) {
            continue;
        }
        for (int right = 0; right < 128; ++right) {
            if (weights[right] == 0) {
                continue;
            }
            const int third = (256 - left - right) % 128;
            total += weights[left] * weights[right] * weights[third];
        }
    }
    return total;
}

std::array<int, 128> expand_labels(const std::array<int, 63>& labels) {
    std::array<int, 128> weights{};
    for (int index = 0; index < 63; ++index) {
        const int representative = index + 1;
        weights[representative] = labels[index];
        weights[128 - representative] = labels[index];
    }
    return weights;
}

}  // namespace

int main() {
    std::array<uint32_t, 15> orbits{};
    for (int index = 0; index < 15; ++index) {
        orbits[index] = orbit_mask(index + 1);
    }

    std::uint64_t rows = 0;
    int maximum = -1;
    std::array<int, 3> best{};
    for (uint32_t a_choice = 0; a_choice < (uint32_t{1} << 15); ++a_choice) {
        if (__builtin_popcount(a_choice) != 10) {
            continue;
        }
        uint32_t a = 0;
        std::vector<int> a_indices;
        for (int index = 0; index < 15; ++index) {
            if ((a_choice >> index) & 1U) {
                a |= orbits[index];
                a_indices.push_back(index);
            }
        }
        const int aaa = triple(a, a, a);

        for (uint32_t local_b = 0; local_b < (uint32_t{1} << 10); ++local_b) {
            if (__builtin_popcount(local_b) != 6) {
                continue;
            }
            uint32_t b = 0;
            std::vector<int> b_indices;
            for (int local = 0; local < 10; ++local) {
                if ((local_b >> local) & 1U) {
                    const int index = a_indices[local];
                    b |= orbits[index];
                    b_indices.push_back(index);
                }
            }
            const int aab = triple(a, a, b);
            const int abb = triple(a, b, b);
            const int bbb = triple(b, b, b);

            for (int top_index : b_indices) {
                const uint32_t t_set = orbits[top_index];
                const int t = top_index + 1;
                const int aat = triple(a, a, t_set);
                const int abt = triple(a, b, t_set);
                const int att = triple(a, t_set, t_set);
                const int bbt = triple(b, b, t_set);
                const int btt = triple(b, t_set, t_set);
                const int ttt = triple(t_set, t_set, t_set);
                const int moment = aaa + 3 * aab + 3 * aat + 3 * abb
                    + 6 * abt + 3 * att + bbb + 3 * bbt + 3 * btt + ttt;
                ++rows;
                if (moment > maximum) {
                    maximum = moment;
                    best = {
                        static_cast<int>(a_choice),
                        static_cast<int>(local_b),
                        t,
                    };
                }
            }
        }
    }

    std::cout << "E33_PROFILE451_NESTED_PROBE"
              << " rows=" << rows
              << " maximum=" << maximum
              << " best_a=" << best[0]
              << " best_b_local=" << best[1]
              << " best_t=" << best[2]
              << '\n';

    std::mt19937_64 generator(0xE33451ULL);
    int hill_maximum = -1;
    std::array<int, 63> hill_best{};
    constexpr int kRestarts = 4000;
    constexpr int kSteps = 500;
    for (int restart = 0; restart < kRestarts; ++restart) {
        std::array<int, 63> labels{};
        std::vector<int> positions(63);
        for (int index = 0; index < 63; ++index) {
            positions[index] = index;
        }
        std::shuffle(positions.begin(), positions.end(), generator);
        for (int index = 0; index < 4; ++index) labels[positions[index]] = 1;
        for (int index = 4; index < 9; ++index) labels[positions[index]] = 2;
        labels[positions[9]] = 3;
        int current = weighted_moment_128(expand_labels(labels));
        for (int step = 0; step < kSteps; ++step) {
            int first = static_cast<int>(generator() % 63);
            int second = static_cast<int>(generator() % 63);
            if (labels[first] == labels[second]) {
                continue;
            }
            std::swap(labels[first], labels[second]);
            const int candidate = weighted_moment_128(expand_labels(labels));
            const bool exploratory_accept = (generator() % 1000) < 4;
            if (candidate >= current || exploratory_accept) {
                current = candidate;
            } else {
                std::swap(labels[first], labels[second]);
            }
            if (current > hill_maximum) {
                hill_maximum = current;
                hill_best = labels;
            }
        }
    }
    std::cout << "E33_PROFILE451_N128_HILL"
              << " restarts=" << kRestarts
              << " steps=" << kSteps
              << " maximum=" << hill_maximum
              << " labels=";
    for (int index = 0; index < 63; ++index) {
        if (hill_best[index]) {
            std::cout << (index + 1) << ':' << hill_best[index] << ',';
        }
    }
    std::cout << '\n';
    return 0;
}
