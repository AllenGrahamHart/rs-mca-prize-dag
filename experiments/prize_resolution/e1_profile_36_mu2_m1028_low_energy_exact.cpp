#define main geometry_only_main
#include "e1_profile_36_mu1_low_energy_exact.cpp"
#undef main

#include <map>

struct M1028Counts {
    Counts base;
    std::array<uint64_t, 7> energy_counts{};
    uint64_t divisible_257 = 0;
};

static int mod_pow(int base, int exponent) {
    int64_t result = 1;
    int64_t power = base;
    while (exponent > 0) {
        if (exponent & 1) result = result * power % 257;
        power = power * power % 257;
        exponent >>= 1;
    }
    return static_cast<int>(result);
}

static bool divisible_by_257(
    const Support& singleton_support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>& heavy_support,
    const std::array<int, 3>& heavy_signs
) {
    for (int odd = 1; odd < 256; odd += 2) {
        const int root = mod_pow(3, odd);
        int value = 0;
        for (int index = 0; index < 6; ++index) {
            value += singleton_signs[index] * mod_pow(root, singleton_support[index]);
        }
        for (int index = 0; index < 3; ++index) {
            value += 2 * heavy_signs[index] * mod_pow(root, heavy_support[index]);
        }
        value %= 257;
        if (value < 0) value += 257;
        if (value == 0) return true;
    }
    return false;
}

static bool process_m1028_orbit(
    const Support& support, M1028Counts& counts, bool triple_engine
) {
    ++counts.base.orbits;
    const uint64_t parity_mask = odd_chord_mask(support);
    std::vector<int> odd_lags;
    for (int lag = 1; lag < 64; ++lag) {
        if ((parity_mask >> (lag - 1)) & 1) odd_lags.push_back(lag);
    }
    const int q = static_cast<int>(odd_lags.size());
    if (q < 1 || q > 6) return false;

    std::vector<int> allowed;
    std::array<uint64_t, 128> columns{};
    for (int position = 0; position < 128; ++position) {
        if (!contains(support, position)) {
            allowed.push_back(position);
            columns[position] = heavy_column(support, position);
        }
    }

    std::unordered_multimap<uint64_t, uint16_t> pair_map;
    std::unordered_multimap<uint64_t, uint32_t> triple_map;
    if (triple_engine) {
        triple_map.reserve(400000);
        for (size_t i = 0; i < allowed.size(); ++i) {
            for (size_t j = i + 1; j < allowed.size(); ++j) {
                for (size_t k = j + 1; k < allowed.size(); ++k) {
                    const std::array<int, 3> values{
                        allowed[i], allowed[j], allowed[k]
                    };
                    triple_map.emplace(
                        columns[allowed[i]] ^ columns[allowed[j]] ^ columns[allowed[k]],
                        pack_triple(values)
                    );
                }
            }
        }
    } else {
        pair_map.reserve(allowed.size() * allowed.size());
        for (size_t i = 0; i < allowed.size(); ++i) {
            for (size_t j = i + 1; j < allowed.size(); ++j) {
                pair_map.emplace(
                    columns[allowed[i]] ^ columns[allowed[j]],
                    pack_pair(allowed[i], allowed[j])
                );
            }
        }
    }

    for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
        ++counts.base.sign_assignments;
        std::array<int, 6> singleton_signs{};
        singleton_signs[0] = 1;
        for (int index = 1; index < 6; ++index) {
            singleton_signs[index] = ((sign_mask >> (index - 1)) & 1) ? -1 : 1;
        }
        const auto singleton_correlation = autocorrelation(support, singleton_signs);

        auto test_target = [&](const std::array<int, 64>& target) -> bool {
            ++counts.base.targets;
            uint64_t rhs = 0;
            for (int lag = 1; lag < 64; ++lag) {
                const int difference = target[lag] - singleton_correlation[lag];
                if (difference & 1) {
                    std::cerr << "parity mismatch\n";
                    std::exit(3);
                }
                if ((difference / 2) & 1) rhs ^= uint64_t{1} << (lag - 1);
            }

            auto test_heavy_support = [&](const std::array<int, 3>& heavy_support) -> bool {
                ++counts.base.triple_candidates;
                for (int heavy_mask = 0; heavy_mask < 8; ++heavy_mask) {
                    ++counts.base.exact_sign_tests;
                    std::array<int, 3> heavy_signs{};
                    for (int index = 0; index < 3; ++index) {
                        heavy_signs[index] = ((heavy_mask >> index) & 1) ? -1 : 1;
                    }
                    const auto full = autocorrelation(
                        support, singleton_signs, &heavy_support, &heavy_signs
                    );
                    const int candidate_energy = energy(full);
                    if (candidate_energy < 2 || candidate_energy > 6) continue;
                    ++counts.energy_counts[candidate_energy];
                    if (!divisible_by_257(
                            support, singleton_signs, heavy_support, heavy_signs)) {
                        continue;
                    }
                    ++counts.divisible_257;
                    std::cout << "M1028_WITNESS E=" << candidate_energy
                              << " singleton=";
                    for (int value : support) std::cout << value << ',';
                    std::cout << " signs=";
                    for (int value : singleton_signs) std::cout << value << ',';
                    std::cout << " heavy=";
                    for (int value : heavy_support) std::cout << value << ',';
                    std::cout << " heavy_signs=";
                    for (int value : heavy_signs) std::cout << value << ',';
                    std::cout << '\n';
                    return true;
                }
                return false;
            };

            if (triple_engine) {
                ++counts.base.xor_probes;
                const auto range = triple_map.equal_range(rhs);
                for (auto iterator = range.first; iterator != range.second; ++iterator) {
                    if (test_heavy_support(unpack_triple(iterator->second))) return true;
                }
            } else {
                std::unordered_set<uint32_t> seen;
                for (int third : allowed) {
                    ++counts.base.xor_probes;
                    const auto range = pair_map.equal_range(rhs ^ columns[third]);
                    for (auto iterator = range.first; iterator != range.second; ++iterator) {
                        const auto [left, right] = unpack_pair(iterator->second);
                        if (third == left || third == right) continue;
                        std::array<int, 3> heavy_support{left, right, third};
                        std::sort(heavy_support.begin(), heavy_support.end());
                        const uint32_t packed = pack_triple(heavy_support);
                        if (!seen.insert(packed).second) continue;
                        if (test_heavy_support(heavy_support)) return true;
                    }
                }
            }
            return false;
        };

        if (q >= 2) {
            for (int target_sign_mask = 0; target_sign_mask < (1 << q);
                 ++target_sign_mask) {
                std::array<int, 64> target{};
                for (int index = 0; index < q; ++index) {
                    target[odd_lags[index]] =
                        ((target_sign_mask >> index) & 1) ? -1 : 1;
                }
                if (test_target(target)) return true;
            }
        }
        if (q + 4 <= 6) {
            for (int target_sign_mask = 0; target_sign_mask < (1 << q);
                 ++target_sign_mask) {
                for (int even_lag = 1; even_lag < 64; ++even_lag) {
                    if ((parity_mask >> (even_lag - 1)) & 1) continue;
                    for (int even_sign : {-1, 1}) {
                        std::array<int, 64> target{};
                        for (int index = 0; index < q; ++index) {
                            target[odd_lags[index]] =
                                ((target_sign_mask >> index) & 1) ? -1 : 1;
                        }
                        target[even_lag] = 2 * even_sign;
                        if (test_target(target)) return true;
                    }
                }
            }
        }
    }
    return false;
}

int main(int argc, char** argv) {
    const bool triple_engine = argc > 1 && std::string(argv[1]) == "triple";
    M1028Counts counts;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        std::istringstream input(line);
        Support support{};
        for (int& value : support) input >> value;
        if (!input) return 2;
        if (process_m1028_orbit(support, counts, triple_engine)) return 1;
    }
    std::cout << "PASS engine="
              << (triple_engine ? "triple-xor" : "pair-xor-plus-third")
              << " orbits=" << counts.base.orbits
              << " sign_assignments=" << counts.base.sign_assignments
              << " targets=" << counts.base.targets
              << " xor_probes=" << counts.base.xor_probes
              << " triple_candidates=" << counts.base.triple_candidates
              << " exact_sign_tests=" << counts.base.exact_sign_tests
              << " energy2=" << counts.energy_counts[2]
              << " energy3=" << counts.energy_counts[3]
              << " energy4=" << counts.energy_counts[4]
              << " energy5=" << counts.energy_counts[5]
              << " energy6=" << counts.energy_counts[6]
              << " divisible_257=" << counts.divisible_257 << '\n';
    return 0;
}
