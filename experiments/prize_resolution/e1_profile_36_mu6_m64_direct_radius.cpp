#define main low_energy_base_main
#include "e1_profile_36_mu1_low_energy_exact.cpp"
#undef main

#include "e1_profile_36_mu6_m64_fixed_roots.hpp"

#include <chrono>
#include <cmath>
#include <limits>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;

struct DirectCounts {
    uint64_t orbits = 0;
    uint64_t triple_syndromes = 0;
    uint64_t distance_tests = 0;
    uint64_t radius_matches = 0;
    uint64_t exact_sign_tests = 0;
    uint64_t low_energy_vectors = 0;
    uint64_t product_live_vectors = 0;
    uint64_t screen_below = 0;
    uint64_t screen_above = 0;
    uint64_t screen_near = 0;
    uint64_t fixed_below = 0;
    uint64_t fixed_above = 0;
    uint64_t fixed_unresolved = 0;
};

static int energy_limit(int q) {
    static const std::array<int, 16> limits = {
        -1, -1, 34, 35, 36, 37, 38, 39,
        44, 45, 42, 43, 44, 45, 46, 43,
    };
    return 0 <= q && q < static_cast<int>(limits.size()) ? limits[q] : -1;
}

static const std::array<std::array<long double, 128>, 64>& root_real();
static const std::array<std::array<long double, 128>, 64>& root_imag();

static cpp_int from_u128(unsigned __int128 value) {
    cpp_int result = static_cast<uint64_t>(value >> 64);
    result <<= 64;
    result += static_cast<uint64_t>(value);
    return result;
}

static int fixed_norm_relation(
    const Support& support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>& heavy_support,
    const std::array<int, 3>& heavy_signs
) {
    constexpr int64_t error = 12;
    cpp_int lower_product = 1;
    cpp_int upper_product = 1;
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
        const uint64_t absolute_real = static_cast<uint64_t>(std::llabs(real));
        const uint64_t absolute_imaginary = static_cast<uint64_t>(std::llabs(imaginary));
        const uint64_t lower_real = absolute_real > error ? absolute_real - error : 0;
        const uint64_t lower_imaginary =
            absolute_imaginary > error ? absolute_imaginary - error : 0;
        const uint64_t upper_real = absolute_real + error;
        const uint64_t upper_imaginary = absolute_imaginary + error;
        const unsigned __int128 lower_square =
            static_cast<unsigned __int128>(lower_real) * lower_real
            + static_cast<unsigned __int128>(lower_imaginary) * lower_imaginary;
        const unsigned __int128 upper_square =
            static_cast<unsigned __int128>(upper_real) * upper_real
            + static_cast<unsigned __int128>(upper_imaginary) * upper_imaginary;
        lower_product *= from_u128(lower_square);
        upper_product *= from_u128(upper_square);
    }
    static const cpp_int prize_floor = [] {
        cpp_int value("317494674775468773183020924238786383963");
        value <<= 134 + 2 * 48 * 64;
        return value;
    }();
    static const cpp_int prize_ceiling = [] {
        cpp_int value("317494674775468773183020924238786383964");
        value <<= 134;
        value -= 64;
        value <<= 2 * 48 * 64;
        return value;
    }();
    if (upper_product < prize_floor) return -1;
    if (lower_product > prize_ceiling) return 1;
    return 0;
}

static const std::array<std::array<long double, 128>, 64>& root_real() {
    static const auto table = [] {
        std::array<std::array<long double, 128>, 64> result{};
        const long double pi = acosl(-1.0L);
        for (int index = 0; index < 64; ++index) {
            const int unit = 2 * index + 1;
            for (int position = 0; position < 128; ++position) {
                result[index][position] = cosl(pi * unit * position / 128.0L);
            }
        }
        return result;
    }();
    return table;
}

static const std::array<std::array<long double, 128>, 64>& root_imag() {
    static const auto table = [] {
        std::array<std::array<long double, 128>, 64> result{};
        const long double pi = acosl(-1.0L);
        for (int index = 0; index < 64; ++index) {
            const int unit = 2 * index + 1;
            for (int position = 0; position < 128; ++position) {
                result[index][position] = sinl(pi * unit * position / 128.0L);
            }
        }
        return result;
    }();
    return table;
}

static long double log_norm(
    const Support& support,
    const std::array<int, 6>& singleton_signs,
    const std::array<int, 3>& heavy_support,
    const std::array<int, 3>& heavy_signs
) {
    long double result = 0.0L;
    for (int root = 0; root < 64; ++root) {
        long double real = 0.0L;
        long double imaginary = 0.0L;
        for (int index = 0; index < 6; ++index) {
            real += singleton_signs[index] * root_real()[root][support[index]];
            imaginary += singleton_signs[index] * root_imag()[root][support[index]];
        }
        for (int index = 0; index < 3; ++index) {
            real += 2 * heavy_signs[index] * root_real()[root][heavy_support[index]];
            imaginary += 2 * heavy_signs[index] * root_imag()[root][heavy_support[index]];
        }
        const long double square = real * real + imaginary * imaginary;
        if (square == 0.0L) return -std::numeric_limits<long double>::infinity();
        result += logl(square);
    }
    return result;
}

static bool product_live(int energy_value, int l1_norm) {
    static const std::array<int, 47> minimum_l1 = {
        -1, -1, 2, 3, 4, 5, 4, 5, 6, 7, 4, 5, 6, 7, 6, 7,
        8, 9, 6, 7, 8, 9, 8, 9, 10, 11, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 26, 27, 30,
    };
    return 2 <= energy_value && energy_value < static_cast<int>(minimum_l1.size())
        && l1_norm >= minimum_l1[energy_value];
}

static void process_orbit(
    const Support& support, DirectCounts& counts, bool verbose
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
    for (int position = 0; position < 128; ++position) {
        if (!contains(support, position)) {
            allowed.push_back(position);
            columns[position] = heavy_column(support, position) & even_mask;
        }
    }

    std::array<uint64_t, 32> fixed{};
    std::array<std::array<int, 6>, 32> singleton_signs{};
    for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
        singleton_signs[sign_mask][0] = 1;
        for (int index = 1; index < 6; ++index) {
            singleton_signs[sign_mask][index] =
                ((sign_mask >> (index - 1)) & 1) ? -1 : 1;
        }
        const auto correlation = autocorrelation(support, singleton_signs[sign_mask]);
        for (int lag = 1; lag < 64; ++lag) {
            if ((parity_mask >> (lag - 1)) & 1) continue;
            if (correlation[lag] & 1) std::exit(5);
            const int half = -correlation[lag] / 2;
            if ((half % 2 + 2) % 2) fixed[sign_mask] ^= uint64_t{1} << (lag - 1);
        }
    }

    for (size_t first_index = 0; first_index < allowed.size(); ++first_index) {
        const int first = allowed[first_index];
        for (size_t second_index = first_index + 1; second_index < allowed.size(); ++second_index) {
            const int second = allowed[second_index];
            const uint64_t pair_key = columns[first] ^ columns[second];
            for (size_t third_index = second_index + 1; third_index < allowed.size(); ++third_index) {
                const int third = allowed[third_index];
                const uint64_t key = pair_key ^ columns[third];
                ++counts.triple_syndromes;
                for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
                    ++counts.distance_tests;
                    if (__builtin_popcountll((key ^ fixed[sign_mask]) & even_mask) > radius) {
                        continue;
                    }
                    ++counts.radius_matches;
                    const std::array<int, 3> heavy_support{first, second, third};
                    for (int heavy_mask = 0; heavy_mask < 8; ++heavy_mask) {
                        ++counts.exact_sign_tests;
                        std::array<int, 3> heavy_signs{};
                        for (int index = 0; index < 3; ++index) {
                            heavy_signs[index] =
                                ((heavy_mask >> index) & 1) ? -1 : 1;
                        }
                        const auto full = autocorrelation(
                            support, singleton_signs[sign_mask],
                            &heavy_support, &heavy_signs
                        );
                        const int candidate_energy = energy(full);
                        if (candidate_energy > limit) continue;
                        ++counts.low_energy_vectors;
                        int l1_norm = 0;
                        for (int lag = 1; lag < 64; ++lag) {
                            l1_norm += std::abs(full[lag]);
                        }
                        if (!product_live(candidate_energy, l1_norm)) continue;
                        ++counts.product_live_vectors;
                        const long double measured = log_norm(
                            support, singleton_signs[sign_mask],
                            heavy_support, heavy_signs
                        );
                        static const long double threshold =
                            logl(64.0L)
                            + logl(strtold(
                                "317494674775468773183020924238786383963", nullptr
                            ))
                            + 128.0L * logl(2.0L);
                        if (measured < threshold - 1e-9L) ++counts.screen_below;
                        else if (measured > threshold + 1e-9L) ++counts.screen_above;
                        else ++counts.screen_near;
                        const int fixed_relation = fixed_norm_relation(
                            support, singleton_signs[sign_mask],
                            heavy_support, heavy_signs
                        );
                        if (fixed_relation < 0) ++counts.fixed_below;
                        else if (fixed_relation > 0) ++counts.fixed_above;
                        else ++counts.fixed_unresolved;
                        if (!verbose || fixed_relation <= 0) continue;
                        std::vector<std::pair<int, int>> state;
                        for (int index = 0; index < 6; ++index) {
                            state.emplace_back(
                                support[index], singleton_signs[sign_mask][index]
                            );
                        }
                        for (int index = 0; index < 3; ++index) {
                            state.emplace_back(
                                heavy_support[index], 2 * heavy_signs[index]
                            );
                        }
                        std::sort(state.begin(), state.end());
                        std::cout << "WITNESS E=" << candidate_energy
                                  << " q=" << q << " L=" << l1_norm << " state=";
                        for (const auto& [position, coefficient] : state) {
                            std::cout << position << ':' << coefficient << ',';
                        }
                        std::cout << '\n';
                    }
                }
            }
        }
    }
}

#ifndef DIRECT_RADIUS_MAIN
#define DIRECT_RADIUS_MAIN main
#endif

int DIRECT_RADIUS_MAIN(int argc, char** argv) {
    const bool verbose = argc > 1 && std::string(argv[1]) == "verbose";
    DirectCounts counts;
    std::string line;
    const auto started = std::chrono::steady_clock::now();
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        std::istringstream input(line);
        Support support{};
        for (int& value : support) input >> value;
        if (!input) return 2;
        process_orbit(support, counts, verbose);
    }
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started
    ).count();
    std::cout << "PASS orbits=" << counts.orbits
              << " triple_syndromes=" << counts.triple_syndromes
              << " distance_tests=" << counts.distance_tests
              << " radius_matches=" << counts.radius_matches
              << " exact_sign_tests=" << counts.exact_sign_tests
              << " low_energy_vectors=" << counts.low_energy_vectors
              << " product_live_vectors=" << counts.product_live_vectors
              << " screen_below=" << counts.screen_below
              << " screen_above=" << counts.screen_above
              << " screen_near=" << counts.screen_near
              << " fixed_below=" << counts.fixed_below
              << " fixed_above=" << counts.fixed_above
              << " fixed_unresolved=" << counts.fixed_unresolved
              << " seconds=" << seconds << '\n';
    return 0;
}
