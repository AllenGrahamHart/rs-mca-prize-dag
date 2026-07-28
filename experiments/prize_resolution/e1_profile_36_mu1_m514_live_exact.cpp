#define main low_energy_base_main
#include "e1_profile_36_mu1_low_energy_exact.cpp"
#undef main

#include <limits>

struct LiveCounts {
    uint64_t orbits = 0;
    uint64_t sign_assignments = 0;
    uint64_t xor_probes = 0;
    uint64_t triple_candidates = 0;
    uint64_t exact_sign_tests = 0;
    uint64_t root_tests = 0;
    std::array<uint64_t, 12> geometry{};
    std::array<uint64_t, 12> mod257{};
};

static int mod_pow(int base, int exponent) {
    int result = 1;
    while (exponent) {
        if (exponent & 1) result = result * base % 257;
        base = base * base % 257;
        exponent >>= 1;
    }
    return result;
}

static const std::array<std::array<int, 128>, 128>& root_values() {
    static const auto values = [] {
        std::array<std::array<int, 128>, 128> result{};
        for (int root_index = 0; root_index < 128; ++root_index) {
            const int unit = 2 * root_index + 1;
            for (int position = 0; position < 128; ++position) {
                result[root_index][position] = mod_pow(3, unit * position % 256);
            }
        }
        return result;
    }();
    return values;
}

static std::vector<uint64_t> live_errors(uint64_t even_mask, int radius) {
    std::vector<uint64_t> result{0};
    if (radius == 1) {
        for (int bit = 0; bit < 63; ++bit) {
            if ((even_mask >> bit) & 1) result.push_back(uint64_t{1} << bit);
        }
    }
    return result;
}

static bool process_live_orbit(
    const Support& support, LiveCounts& counts, bool sorted_engine
) {
    ++counts.orbits;
    const uint64_t parity_mask = odd_chord_mask(support);
    const int q = __builtin_popcountll(parity_mask);
    if (q < 3 || q > 11) return false;
    const int target_energy = q <= 6 ? q + 4 : q;
    const int radius = q <= 6 ? 1 : 0;
    const uint64_t all_lags = (uint64_t{1} << 63) - 1;
    const uint64_t even_mask = all_lags ^ parity_mask;
    const std::vector<uint64_t> errors = live_errors(even_mask, radius);

    std::vector<int> allowed;
    std::array<uint64_t, 128> columns{};
    for (int position = 0; position < 128; ++position) {
        if (!contains(support, position)) {
            allowed.push_back(position);
            columns[position] = heavy_column(support, position) & even_mask;
        }
    }

    std::unordered_multimap<uint64_t, uint16_t> hash_pairs;
    std::vector<std::pair<uint64_t, uint16_t>> sorted_pairs;
    if (sorted_engine) {
        sorted_pairs.reserve(allowed.size() * allowed.size() / 2);
    } else {
        hash_pairs.reserve(allowed.size() * allowed.size());
    }
    for (size_t left_index = 0; left_index < allowed.size(); ++left_index) {
        for (size_t right_index = left_index + 1; right_index < allowed.size(); ++right_index) {
            const int left = allowed[left_index];
            const int right = allowed[right_index];
            const auto row = std::make_pair(
                columns[left] ^ columns[right], pack_pair(left, right)
            );
            if (sorted_engine) sorted_pairs.push_back(row);
            else hash_pairs.emplace(row);
        }
    }
    if (sorted_engine) std::sort(sorted_pairs.begin(), sorted_pairs.end());

    for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
        ++counts.sign_assignments;
        std::array<int, 6> singleton_signs{};
        singleton_signs[0] = 1;
        for (int index = 1; index < 6; ++index) {
            singleton_signs[index] = ((sign_mask >> (index - 1)) & 1) ? -1 : 1;
        }
        const auto singleton_correlation = autocorrelation(support, singleton_signs);
        uint64_t fixed = 0;
        for (int lag = 1; lag < 64; ++lag) {
            if ((parity_mask >> (lag - 1)) & 1) continue;
            if (singleton_correlation[lag] & 1) return true;
            const int half = -singleton_correlation[lag] / 2;
            if ((half % 2 + 2) % 2) fixed ^= uint64_t{1} << (lag - 1);
        }

        std::unordered_set<uint32_t> seen;
        auto test_triple = [&](std::array<int, 3> heavy_support) {
            std::sort(heavy_support.begin(), heavy_support.end());
            const uint32_t packed = pack_triple(heavy_support);
            if (!seen.insert(packed).second) return;
            ++counts.triple_candidates;
            for (int heavy_mask = 0; heavy_mask < 8; ++heavy_mask) {
                ++counts.exact_sign_tests;
                std::array<int, 3> heavy_signs{};
                for (int index = 0; index < 3; ++index) {
                    heavy_signs[index] = ((heavy_mask >> index) & 1) ? -1 : 1;
                }
                const auto full = autocorrelation(
                    support, singleton_signs, &heavy_support, &heavy_signs
                );
                if (energy(full) != target_energy) continue;
                ++counts.geometry[target_energy];

                std::vector<int> roots;
                for (int root_index = 0; root_index < 128; ++root_index) {
                    ++counts.root_tests;
                    int value = 0;
                    for (int index = 0; index < 6; ++index) {
                        value += singleton_signs[index]
                            * root_values()[root_index][support[index]];
                    }
                    for (int index = 0; index < 3; ++index) {
                        value += 2 * heavy_signs[index]
                            * root_values()[root_index][heavy_support[index]];
                    }
                    if ((value % 257 + 257) % 257 == 0) roots.push_back(root_index);
                }
                if (roots.empty()) continue;
                ++counts.mod257[target_energy];
                std::vector<std::pair<int, int>> state;
                for (int index = 0; index < 6; ++index) {
                    state.emplace_back(support[index], singleton_signs[index]);
                }
                for (int index = 0; index < 3; ++index) {
                    state.emplace_back(heavy_support[index], 2 * heavy_signs[index]);
                }
                std::sort(state.begin(), state.end());
                std::cout << "CANDIDATE E=" << target_energy << " q=" << q
                          << " state=";
                for (const auto& [position, coefficient] : state) {
                    std::cout << position << ':' << coefficient << ',';
                }
                std::cout << " roots=";
                for (int root : roots) std::cout << root << ',';
                std::cout << '\n';
            }
        };

        for (int third : allowed) {
            for (uint64_t error : errors) {
                ++counts.xor_probes;
                const uint64_t wanted = fixed ^ error ^ columns[third];
                if (sorted_engine) {
                    const auto lower = std::lower_bound(
                        sorted_pairs.begin(), sorted_pairs.end(),
                        std::make_pair(wanted, uint16_t{0})
                    );
                    const auto upper = std::upper_bound(
                        sorted_pairs.begin(), sorted_pairs.end(),
                        std::make_pair(wanted, std::numeric_limits<uint16_t>::max())
                    );
                    for (auto iterator = lower; iterator != upper; ++iterator) {
                        const auto [left, right] = unpack_pair(iterator->second);
                        if (third != left && third != right) {
                            test_triple({left, right, third});
                        }
                    }
                } else {
                    const auto range = hash_pairs.equal_range(wanted);
                    for (auto iterator = range.first; iterator != range.second; ++iterator) {
                        const auto [left, right] = unpack_pair(iterator->second);
                        if (third != left && third != right) {
                            test_triple({left, right, third});
                        }
                    }
                }
            }
        }
    }
    return false;
}

int main(int argc, char** argv) {
    const bool sorted_engine = argc > 1 && std::string(argv[1]) == "sorted";
    LiveCounts counts;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        std::istringstream input(line);
        Support support{};
        for (int& value : support) input >> value;
        if (!input) return 2;
        if (process_live_orbit(support, counts, sorted_engine)) return 3;
    }
    std::cout << "PASS engine=" << (sorted_engine ? "sorted-pairs" : "hash-pairs")
              << " orbits=" << counts.orbits
              << " sign_assignments=" << counts.sign_assignments
              << " xor_probes=" << counts.xor_probes
              << " triple_candidates=" << counts.triple_candidates
              << " exact_sign_tests=" << counts.exact_sign_tests
              << " root_tests=" << counts.root_tests;
    for (int candidate_energy = 7; candidate_energy <= 11; ++candidate_energy) {
        std::cout << " geometry" << candidate_energy << '=' << counts.geometry[candidate_energy]
                  << " mod257_" << candidate_energy << '=' << counts.mod257[candidate_energy];
    }
    std::cout << '\n';
    return 0;
}
