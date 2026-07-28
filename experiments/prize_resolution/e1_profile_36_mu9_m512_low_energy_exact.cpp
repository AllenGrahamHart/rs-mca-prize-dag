#define main low_energy_base_main
#include "e1_profile_36_mu1_low_energy_exact.cpp"
#undef main

struct RadiusCounts {
    uint64_t orbits = 0;
    uint64_t sign_assignments = 0;
    uint64_t xor_probes = 0;
    uint64_t triple_candidates = 0;
    uint64_t exact_sign_tests = 0;
    std::array<uint64_t, 18> energy_counts{};
};

static std::vector<uint64_t> error_ball(uint64_t even_mask, int radius) {
    std::vector<int> bits;
    for (int bit = 0; bit < 63; ++bit) {
        if ((even_mask >> bit) & 1) bits.push_back(bit);
    }
    std::vector<uint64_t> errors{0};
    if (radius >= 1) {
        for (int bit : bits) errors.push_back(uint64_t{1} << bit);
    }
    if (radius >= 2) {
        for (size_t left = 0; left < bits.size(); ++left) {
            for (size_t right = left + 1; right < bits.size(); ++right) {
                errors.push_back(
                    (uint64_t{1} << bits[left]) | (uint64_t{1} << bits[right])
                );
            }
        }
    }
    return errors;
}

static bool process_radius_orbit(
    const Support& support, RadiusCounts& counts, bool triple_engine
) {
    ++counts.orbits;
    const uint64_t parity_mask = odd_chord_mask(support);
    const int q = __builtin_popcountll(parity_mask);
    if (q > 17) return false;
    const int radius = (17 - q) / 4;
    if (radius > 2) {
        std::cerr << "unexpected radius\n";
        std::exit(3);
    }
    const uint64_t all_lags = (uint64_t{1} << 63) - 1;
    const uint64_t even_mask = all_lags ^ parity_mask;
    const std::vector<uint64_t> errors = error_ball(even_mask, radius);

    std::vector<int> allowed;
    std::array<uint64_t, 128> projected_columns{};
    for (int position = 0; position < 128; ++position) {
        if (!contains(support, position)) {
            allowed.push_back(position);
            projected_columns[position] = heavy_column(support, position) & even_mask;
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
                        projected_columns[allowed[i]]
                            ^ projected_columns[allowed[j]]
                            ^ projected_columns[allowed[k]],
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
                    projected_columns[allowed[i]] ^ projected_columns[allowed[j]],
                    pack_pair(allowed[i], allowed[j])
                );
            }
        }
    }

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
            if (singleton_correlation[lag] & 1) {
                std::cerr << "even-lag parity mismatch\n";
                std::exit(3);
            }
            const int half = -singleton_correlation[lag] / 2;
            if ((half % 2 + 2) % 2) fixed ^= uint64_t{1} << (lag - 1);
        }

        std::unordered_set<uint32_t> seen;
        auto test_triple = [&](const std::array<int, 3>& heavy_support) -> bool {
            const uint32_t packed = pack_triple(heavy_support);
            if (!seen.insert(packed).second) return false;
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
                const int candidate_energy = energy(full);
                if (candidate_energy < 2 || candidate_energy > 17) continue;
                ++counts.energy_counts[candidate_energy];
                std::vector<std::pair<int, int>> state;
                for (int index = 0; index < 6; ++index) {
                    state.emplace_back(support[index], singleton_signs[index]);
                }
                for (int index = 0; index < 3; ++index) {
                    state.emplace_back(heavy_support[index], 2 * heavy_signs[index]);
                }
                std::sort(state.begin(), state.end());
                std::cout << "CANDIDATE E=" << candidate_energy << " state=";
                for (const auto& [position, coefficient] : state) {
                    std::cout << position << ':' << coefficient << ',';
                }
                std::cout << '\n';
            }
            return false;
        };

        if (triple_engine) {
            for (uint64_t error : errors) {
                ++counts.xor_probes;
                const auto range = triple_map.equal_range(fixed ^ error);
                for (auto iterator = range.first; iterator != range.second; ++iterator) {
                    if (test_triple(unpack_triple(iterator->second))) return true;
                }
            }
        } else {
            for (int third : allowed) {
                for (uint64_t error : errors) {
                    ++counts.xor_probes;
                    const uint64_t wanted =
                        fixed ^ error ^ projected_columns[third];
                    const auto range = pair_map.equal_range(wanted);
                    for (auto iterator = range.first; iterator != range.second; ++iterator) {
                        const auto [left, right] = unpack_pair(iterator->second);
                        if (third == left || third == right) continue;
                        std::array<int, 3> heavy_support{left, right, third};
                        std::sort(heavy_support.begin(), heavy_support.end());
                        if (test_triple(heavy_support)) return true;
                    }
                }
            }
        }
    }
    return false;
}

int main(int argc, char** argv) {
    const bool triple_engine = argc > 1 && std::string(argv[1]) == "triple";
    RadiusCounts counts;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        std::istringstream input(line);
        Support support{};
        for (int& value : support) input >> value;
        if (!input) return 2;
        if (process_radius_orbit(support, counts, triple_engine)) return 1;
    }
    std::cout << "PASS engine="
              << (triple_engine ? "triple-radius" : "pair-radius-plus-third")
              << " orbits=" << counts.orbits
              << " sign_assignments=" << counts.sign_assignments
              << " xor_probes=" << counts.xor_probes
              << " triple_candidates=" << counts.triple_candidates
              << " exact_sign_tests=" << counts.exact_sign_tests;
    for (int candidate_energy = 2; candidate_energy <= 17; ++candidate_energy) {
        std::cout << " energy" << candidate_energy
                  << '=' << counts.energy_counts[candidate_energy];
    }
    std::cout << '\n';
    return 0;
}
