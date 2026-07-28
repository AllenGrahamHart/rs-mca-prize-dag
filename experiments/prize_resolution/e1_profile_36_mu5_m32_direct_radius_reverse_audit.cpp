#define DIRECT_RADIUS_MAIN direct_radius_primary_main
#include "e1_profile_36_mu5_m32_direct_radius.cpp"
#undef DIRECT_RADIUS_MAIN

struct ReverseAuditCounts {
    uint64_t orbits = 0;
    uint64_t sign_assignments = 0;
    uint64_t triple_syndromes = 0;
    uint64_t radius_matches = 0;
    uint64_t exact_sign_tests = 0;
    uint64_t low_energy_vectors = 0;
    uint64_t product_live_vectors = 0;
    uint64_t fixed_below = 0;
    uint64_t fixed_above = 0;
    uint64_t fixed_unresolved = 0;
    std::array<uint64_t, 61> live_by_energy{};
    std::array<uint64_t, 61> above_by_energy{};
};

static uint64_t reverse_audit_column(const Support& support, int position) {
    uint64_t result = 0;
    for (const int singleton : support) {
        const int delta = std::abs(position - singleton);
        if (delta == 64) continue;
        const int lag = delta < 64 ? delta : 128 - delta;
        result ^= uint64_t{1} << (lag - 1);
    }
    return result;
}

static void reverse_audit_orbit(
    const Support& support, ReverseAuditCounts& counts
) {
    ++counts.orbits;
    const uint64_t parity_mask = odd_chord_mask(support);
    const int q = __builtin_popcountll(parity_mask);
    const int limit = energy_limit(q);
    if (limit < 0) return;
    const int radius = (limit - q) / 4;
    const uint64_t all_lags = (uint64_t{1} << 63) - 1;
    const uint64_t even_mask = all_lags ^ parity_mask;

    std::vector<int> allowed;
    std::array<uint64_t, 128> columns{};
    for (int position = 127; position >= 0; --position) {
        if (!contains(support, position)) {
            allowed.push_back(position);
            columns[position] = reverse_audit_column(support, position) & even_mask;
        }
    }

    std::array<std::array<int, 6>, 32> audit_signs{};
    std::array<std::array<int, 64>, 32> singleton_correlations{};
    std::array<std::array<std::array<int8_t, 64>, 32>, 128> cross{};
    for (int sign_code = 0; sign_code < 32; ++sign_code) {
        audit_signs[sign_code][0] = 1;
        for (int index = 1; index < 6; ++index) {
            audit_signs[sign_code][index] =
                ((sign_code >> (index - 1)) & 1) ? -1 : 1;
        }
        singleton_correlations[sign_code] =
            autocorrelation(support, audit_signs[sign_code]);
        for (const int position : allowed) {
            for (int singleton_index = 0; singleton_index < 6; ++singleton_index) {
                const int delta = std::abs(position - support[singleton_index]);
                if (delta == 64) continue;
                const int lag = delta < 64 ? delta : 128 - delta;
                const int orientation = delta < 64 ? 1 : -1;
                cross[position][sign_code][lag] +=
                    orientation * audit_signs[sign_code][singleton_index];
            }
        }
    }

    for (int sign_code = 31; sign_code >= 0; --sign_code) {
        ++counts.sign_assignments;
        const auto& singleton_signs = audit_signs[sign_code];
        const auto& singleton_correlation = singleton_correlations[sign_code];
        uint64_t fixed = 0;
        for (int lag = 63; lag >= 1; --lag) {
            if ((parity_mask >> (lag - 1)) & 1) continue;
            if (singleton_correlation[lag] & 1) std::exit(30);
            const int half = -singleton_correlation[lag] / 2;
            if ((half % 2 + 2) % 2) fixed ^= uint64_t{1} << (lag - 1);
        }

        for (size_t first_index = 0; first_index < allowed.size(); ++first_index) {
            const int first = allowed[first_index];
            for (size_t second_index = first_index + 1; second_index < allowed.size(); ++second_index) {
                const int second = allowed[second_index];
                const uint64_t pair_key = columns[first] ^ columns[second];
                for (size_t third_index = second_index + 1; third_index < allowed.size(); ++third_index) {
                    const int third = allowed[third_index];
                    ++counts.triple_syndromes;
                    const uint64_t key = pair_key ^ columns[third];
                    if (__builtin_popcountll((key ^ fixed) & even_mask) > radius) {
                        continue;
                    }
                    ++counts.radius_matches;
                    counts.exact_sign_tests += 8;
                    const std::array<int, 3> heavy_support{third, second, first};

                    std::array<int, 3> pair_lags{};
                    std::array<int, 3> pair_orientations{};
                    int pair_index = 0;
                    for (int left = 0; left < 3; ++left) {
                        for (int right = left + 1; right < 3; ++right) {
                            const int delta = heavy_support[right] - heavy_support[left];
                            if (delta != 64) {
                                pair_lags[pair_index] = delta < 64 ? delta : 128 - delta;
                                pair_orientations[pair_index] = delta < 64 ? 1 : -1;
                            }
                            ++pair_index;
                        }
                    }

                    std::array<int, 8> energies{};
                    std::array<int, 8> l1_norms{};
                    uint8_t active_masks = 0xff;
                    for (int lag = 1; lag < 64 && active_masks; ++lag) {
                        const int base = singleton_correlation[lag];
                        const int a = 2 * cross[heavy_support[0]][sign_code][lag];
                        const int b = 2 * cross[heavy_support[1]][sign_code][lag];
                        const int c = 2 * cross[heavy_support[2]][sign_code][lag];
                        const int d = pair_lags[0] == lag ? 4 * pair_orientations[0] : 0;
                        const int e = pair_lags[1] == lag ? 4 * pair_orientations[1] : 0;
                        const int f = pair_lags[2] == lag ? 4 * pair_orientations[2] : 0;
                        const std::array<int, 8> values = {
                            base + a + b + c + d + e + f,
                            base - a + b + c - d - e + f,
                            base + a - b + c - d + e - f,
                            base - a - b + c + d - e - f,
                            base + a + b - c + d - e - f,
                            base - a + b - c - d + e - f,
                            base + a - b - c - d - e + f,
                            base - a - b - c + d + e + f,
                        };
                        for (int heavy_code = 0; heavy_code < 8; ++heavy_code) {
                            const uint8_t bit = uint8_t{1} << heavy_code;
                            if (!(active_masks & bit)) continue;
                            const int value = values[heavy_code];
                            energies[heavy_code] += value * value;
                            l1_norms[heavy_code] += std::abs(value);
                            if (energies[heavy_code] > limit) active_masks &= ~bit;
                        }
                    }

                    for (int heavy_code = 7; heavy_code >= 0; --heavy_code) {
                        const int candidate_energy = energies[heavy_code];
                        if (candidate_energy > limit) continue;
                        std::array<int, 3> heavy_signs{};
                        for (int index = 0; index < 3; ++index) {
                            heavy_signs[index] =
                                ((heavy_code >> index) & 1) ? -1 : 1;
                        }
                        const auto full = autocorrelation(
                            support, singleton_signs, &heavy_support, &heavy_signs
                        );
                        int direct_l1 = 0;
                        for (int lag = 63; lag >= 1; --lag) direct_l1 += std::abs(full[lag]);
                        if (energy(full) != candidate_energy) std::exit(31);
                        if (direct_l1 != l1_norms[heavy_code]) std::exit(32);
                        ++counts.low_energy_vectors;
                        if (!product_live(candidate_energy, q, direct_l1)) continue;
                        ++counts.product_live_vectors;
                        ++counts.live_by_energy[candidate_energy];
                        const int relation = fixed_norm_relation(
                            support, singleton_signs, heavy_support, heavy_signs
                        );
                        if (relation < 0) {
                            ++counts.fixed_below;
                        } else if (relation > 0) {
                            ++counts.fixed_above;
                            ++counts.above_by_energy[candidate_energy];
                        } else {
                            ++counts.fixed_unresolved;
                        }
                    }
                }
            }
        }
    }
}

int main() {
    ReverseAuditCounts counts;
    std::string line;
    const auto started = std::chrono::steady_clock::now();
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        std::istringstream input(line);
        Support support{};
        for (int& value : support) input >> value;
        if (!input) return 2;
        reverse_audit_orbit(support, counts);
    }
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started
    ).count();
    std::cout << "PASS engine=reverse-direct"
              << " orbits=" << counts.orbits
              << " sign_assignments=" << counts.sign_assignments
              << " triple_syndromes=" << counts.triple_syndromes
              << " radius_matches=" << counts.radius_matches
              << " exact_sign_tests=" << counts.exact_sign_tests
              << " low_energy_vectors=" << counts.low_energy_vectors
              << " product_live_vectors=" << counts.product_live_vectors
              << " fixed_below=" << counts.fixed_below
              << " fixed_above=" << counts.fixed_above
              << " fixed_unresolved=" << counts.fixed_unresolved;
    for (int candidate_energy = 2; candidate_energy <= 60; ++candidate_energy) {
        if (counts.live_by_energy[candidate_energy]) {
            std::cout << " live_E" << candidate_energy << '='
                      << counts.live_by_energy[candidate_energy];
        }
        if (counts.above_by_energy[candidate_energy]) {
            std::cout << " above_E" << candidate_energy << '='
                      << counts.above_by_energy[candidate_energy];
        }
    }
    std::cout << " seconds=" << seconds << '\n';
    return 0;
}
