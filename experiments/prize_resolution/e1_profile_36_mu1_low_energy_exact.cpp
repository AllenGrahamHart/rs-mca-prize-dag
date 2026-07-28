#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using Support = std::array<int, 6>;

struct Counts {
    uint64_t orbits = 0;
    uint64_t sign_assignments = 0;
    uint64_t targets = 0;
    uint64_t xor_probes = 0;
    uint64_t triple_candidates = 0;
    uint64_t exact_sign_tests = 0;
};

static int folded_lag(int left, int right) {
    int delta = std::abs(right - left);
    return delta <= 64 ? delta : 128 - delta;
}

static uint64_t odd_chord_mask(const Support& support) {
    uint64_t mask = 0;
    for (int i = 0; i < 6; ++i) {
        for (int j = i + 1; j < 6; ++j) {
            int lag = folded_lag(support[i], support[j]);
            if (lag != 64) mask ^= uint64_t{1} << (lag - 1);
        }
    }
    return mask;
}

static std::array<int, 64> autocorrelation(
    const Support& singleton_support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>* heavy_support = nullptr,
    const std::array<int, 3>* heavy_signs = nullptr
) {
    std::vector<std::pair<int, int>> terms;
    terms.reserve(9);
    for (int i = 0; i < 6; ++i) {
        terms.emplace_back(singleton_support[i], singleton_signs[i]);
    }
    if (heavy_support != nullptr) {
        for (int i = 0; i < 3; ++i) {
            terms.emplace_back((*heavy_support)[i], 2 * (*heavy_signs)[i]);
        }
    }
    std::sort(terms.begin(), terms.end());
    std::array<int, 64> result{};
    for (size_t i = 0; i < terms.size(); ++i) {
        for (size_t j = i + 1; j < terms.size(); ++j) {
            int delta = terms[j].first - terms[i].first;
            int product = terms[i].second * terms[j].second;
            if (delta < 64) result[delta] += product;
            else if (delta > 64) result[128 - delta] -= product;
        }
    }
    return result;
}

static int energy(const std::array<int, 64>& correlation) {
    int result = 0;
    for (int lag = 1; lag < 64; ++lag) result += correlation[lag] * correlation[lag];
    return result;
}

static uint64_t heavy_column(const Support& support, int position) {
    uint64_t column = 0;
    for (int singleton : support) {
        int lag = folded_lag(singleton, position);
        if (lag != 64) column ^= uint64_t{1} << (lag - 1);
    }
    return column;
}

static uint16_t pack_pair(int left, int right) {
    return static_cast<uint16_t>(left | (right << 7));
}

static std::pair<int, int> unpack_pair(uint16_t packed) {
    return {packed & 127, packed >> 7};
}

static uint32_t pack_triple(const std::array<int, 3>& values) {
    return static_cast<uint32_t>(values[0] | (values[1] << 7) | (values[2] << 14));
}

static std::array<int, 3> unpack_triple(uint32_t packed) {
    return {static_cast<int>(packed & 127), static_cast<int>((packed >> 7) & 127),
            static_cast<int>((packed >> 14) & 127)};
}

static bool contains(const Support& support, int value) {
    return std::find(support.begin(), support.end(), value) != support.end();
}

static bool process_orbit(const Support& support, Counts& counts, bool triple_engine) {
    ++counts.orbits;
    uint64_t parity_mask = odd_chord_mask(support);
    std::vector<int> odd_lags;
    for (int lag = 1; lag < 64; ++lag) {
        if ((parity_mask >> (lag - 1)) & 1) odd_lags.push_back(lag);
    }
    int q = static_cast<int>(odd_lags.size());
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
                    std::array<int, 3> values{allowed[i], allowed[j], allowed[k]};
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
        ++counts.sign_assignments;
        std::array<int, 6> singleton_signs{};
        singleton_signs[0] = 1;
        for (int index = 1; index < 6; ++index) {
            singleton_signs[index] = ((sign_mask >> (index - 1)) & 1) ? -1 : 1;
        }
        auto singleton_correlation = autocorrelation(support, singleton_signs);

        auto test_target = [&](const std::array<int, 64>& target) -> bool {
            ++counts.targets;
            uint64_t rhs = 0;
            for (int lag = 1; lag < 64; ++lag) {
                int difference = target[lag] - singleton_correlation[lag];
                if (difference & 1) {
                    std::cerr << "parity mismatch\n";
                    std::exit(3);
                }
                if ((difference / 2) & 1) rhs ^= uint64_t{1} << (lag - 1);
            }

            auto test_heavy_support = [&](const std::array<int, 3>& heavy_support) -> bool {
                ++counts.triple_candidates;
                for (int heavy_mask = 0; heavy_mask < 8; ++heavy_mask) {
                    ++counts.exact_sign_tests;
                    std::array<int, 3> heavy_signs{};
                    for (int index = 0; index < 3; ++index) {
                        heavy_signs[index] = ((heavy_mask >> index) & 1) ? -1 : 1;
                    }
                    auto full = autocorrelation(
                        support, singleton_signs, &heavy_support, &heavy_signs
                    );
                    int candidate_energy = energy(full);
                    if (candidate_energy >= 2 && candidate_energy <= 6) {
                        std::cout << "WITNESS E=" << candidate_energy << " singleton=";
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
                }
                return false;
            };

            if (triple_engine) {
                ++counts.xor_probes;
                auto range = triple_map.equal_range(rhs);
                for (auto iterator = range.first; iterator != range.second; ++iterator) {
                    if (test_heavy_support(unpack_triple(iterator->second))) return true;
                }
            } else {
                std::unordered_set<uint32_t> seen;
                for (int third : allowed) {
                    ++counts.xor_probes;
                    auto range = pair_map.equal_range(rhs ^ columns[third]);
                    for (auto iterator = range.first; iterator != range.second; ++iterator) {
                        auto [left, right] = unpack_pair(iterator->second);
                        if (third == left || third == right) continue;
                        std::array<int, 3> heavy_support{left, right, third};
                        std::sort(heavy_support.begin(), heavy_support.end());
                        uint32_t packed = pack_triple(heavy_support);
                        if (!seen.insert(packed).second) continue;
                        if (test_heavy_support(heavy_support)) return true;
                    }
                }
            }
            return false;
        };

        if (q >= 2 && q <= 6) {
            for (int target_sign_mask = 0; target_sign_mask < (1 << q); ++target_sign_mask) {
                std::array<int, 64> target{};
                for (int index = 0; index < q; ++index) {
                    target[odd_lags[index]] = ((target_sign_mask >> index) & 1) ? -1 : 1;
                }
                if (test_target(target)) return true;
            }
        }
        if (q + 4 >= 2 && q + 4 <= 6) {
            for (int target_sign_mask = 0; target_sign_mask < (1 << q); ++target_sign_mask) {
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
    bool triple_engine = argc > 1 && std::string(argv[1]) == "triple";
    Counts counts;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        std::istringstream input(line);
        Support support{};
        for (int& value : support) input >> value;
        if (!input) return 2;
        if (process_orbit(support, counts, triple_engine)) return 1;
    }
    std::cout << "PASS engine=" << (triple_engine ? "triple-xor" : "pair-xor-plus-third")
              << " orbits=" << counts.orbits
              << " sign_assignments=" << counts.sign_assignments
              << " targets=" << counts.targets
              << " xor_probes=" << counts.xor_probes
              << " triple_candidates=" << counts.triple_candidates
              << " exact_sign_tests=" << counts.exact_sign_tests << '\n';
    return 0;
}
