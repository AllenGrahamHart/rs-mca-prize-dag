#define main low_energy_base_main
#include "e1_profile_36_mu1_low_energy_exact.cpp"
#undef main

#include <limits>
#include <set>

struct LiveCounts {
    uint64_t orbits = 0;
    uint64_t sign_assignments = 0;
    uint64_t third_queries = 0;
    uint64_t bucket_hits = 0;
    uint64_t radius_matches = 0;
    uint64_t triple_candidates = 0;
    uint64_t exact_sign_tests = 0;
    uint64_t low_energy_vectors = 0;
    uint64_t live_candidates = 0;
    std::array<uint64_t, 21> live_by_energy{};
};

static int maximum_radius(int q) {
    if (q == 1 || q == 3 || q == 5) return 3;
    if (q >= 6 && q <= 12) return 2;
    if (q >= 13 && q <= 15) return 1;
    return -1;
}

static bool product_live(int energy_value, int q, int l1_norm) {
    static const std::set<std::array<int, 3>> live = {
        {3, 3, 3},
        {5, 1, 3}, {5, 5, 5},
        {6, 6, 6},
        {7, 3, 5}, {7, 7, 7},
        {8, 8, 8},
        {9, 1, 3}, {9, 1, 5}, {9, 5, 7}, {9, 9, 9},
        {10, 6, 8}, {10, 10, 10},
        {11, 3, 5}, {11, 3, 7}, {11, 7, 9}, {11, 11, 11},
        {12, 8, 10}, {12, 12, 12},
        {13, 1, 7}, {13, 5, 7}, {13, 5, 9}, {13, 9, 11},
        {13, 13, 13},
        {14, 6, 8}, {14, 6, 10}, {14, 10, 12}, {14, 14, 14},
        {15, 3, 9}, {15, 7, 9}, {15, 7, 11}, {15, 11, 13},
        {15, 15, 15},
        {16, 8, 10}, {16, 8, 12}, {16, 12, 14},
        {17, 5, 11}, {17, 9, 11}, {17, 9, 13}, {17, 13, 15},
        {18, 10, 14}, {18, 14, 16},
        {19, 11, 15}, {19, 15, 17},
        {20, 12, 16},
    };
    return live.contains({energy_value, q, l1_norm});
}

static std::vector<uint64_t> block_masks(uint64_t even_mask, int blocks) {
    std::vector<int> bits;
    for (int bit = 0; bit < 63; ++bit) {
        if ((even_mask >> bit) & 1) bits.push_back(bit);
    }
    std::vector<uint64_t> result(blocks);
    for (size_t index = 0; index < bits.size(); ++index) {
        result[index % blocks] |= uint64_t{1} << bits[index];
    }
    uint64_t covered = 0;
    for (uint64_t mask : result) {
        if (!mask || (covered & mask)) std::exit(4);
        covered |= mask;
    }
    if (covered != even_mask) std::exit(4);
    return result;
}

static void process_live_orbit(
    const Support& support, LiveCounts& counts, bool sorted_engine
) {
    ++counts.orbits;
    const uint64_t parity_mask = odd_chord_mask(support);
    const int q = __builtin_popcountll(parity_mask);
    const int radius = maximum_radius(q);
    if (radius < 0) return;
    const uint64_t all_lags = (uint64_t{1} << 63) - 1;
    const uint64_t even_mask = all_lags ^ parity_mask;
    const std::vector<uint64_t> blocks = block_masks(even_mask, radius + 1);

    std::vector<int> allowed;
    std::array<uint64_t, 128> columns{};
    for (int position = 0; position < 128; ++position) {
        if (!contains(support, position)) {
            allowed.push_back(position);
            columns[position] = heavy_column(support, position) & even_mask;
        }
    }

    std::vector<std::unordered_multimap<uint64_t, uint16_t>> hash_tables(
        blocks.size()
    );
    std::vector<std::vector<std::pair<uint64_t, uint16_t>>> sorted_tables(
        blocks.size()
    );
    for (size_t block = 0; block < blocks.size(); ++block) {
        if (sorted_engine) {
            sorted_tables[block].reserve(allowed.size() * allowed.size() / 2);
        } else {
            hash_tables[block].reserve(allowed.size() * allowed.size());
        }
    }
    for (size_t left_index = 0; left_index < allowed.size(); ++left_index) {
        for (size_t right_index = left_index + 1; right_index < allowed.size(); ++right_index) {
            const int left = allowed[left_index];
            const int right = allowed[right_index];
            const uint64_t pair_key = columns[left] ^ columns[right];
            const uint16_t packed = pack_pair(left, right);
            for (size_t block = 0; block < blocks.size(); ++block) {
                const auto row = std::make_pair(pair_key & blocks[block], packed);
                if (sorted_engine) sorted_tables[block].push_back(row);
                else hash_tables[block].emplace(row);
            }
        }
    }
    if (sorted_engine) {
        for (auto& table : sorted_tables) std::sort(table.begin(), table.end());
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
            if (singleton_correlation[lag] & 1) std::exit(5);
            const int half = -singleton_correlation[lag] / 2;
            if ((half % 2 + 2) % 2) fixed ^= uint64_t{1} << (lag - 1);
        }

        std::unordered_set<uint32_t> seen;
        auto test_pair = [&](int left, int right, int third, uint64_t wanted) {
            ++counts.bucket_hits;
            if (third == left || third == right) return;
            const uint64_t difference =
                (columns[left] ^ columns[right] ^ wanted) & even_mask;
            if (__builtin_popcountll(difference) > radius) return;
            ++counts.radius_matches;
            std::array<int, 3> heavy_support{left, right, third};
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
                const int candidate_energy = energy(full);
                if (candidate_energy < 2 || candidate_energy > 20) continue;
                ++counts.low_energy_vectors;
                int l1_norm = 0;
                for (int lag = 1; lag < 64; ++lag) {
                    l1_norm += std::abs(full[lag]);
                }
                if (!product_live(candidate_energy, q, l1_norm)) continue;
                ++counts.live_candidates;
                ++counts.live_by_energy[candidate_energy];
                std::vector<std::pair<int, int>> state;
                for (int index = 0; index < 6; ++index) {
                    state.emplace_back(support[index], singleton_signs[index]);
                }
                for (int index = 0; index < 3; ++index) {
                    state.emplace_back(heavy_support[index], 2 * heavy_signs[index]);
                }
                std::sort(state.begin(), state.end());
                std::cout << "CANDIDATE E=" << candidate_energy << " q=" << q
                          << " L=" << l1_norm << " state=";
                for (const auto& [position, coefficient] : state) {
                    std::cout << position << ':' << coefficient << ',';
                }
                std::cout << '\n';
            }
        };

        for (int third : allowed) {
            ++counts.third_queries;
            const uint64_t wanted = fixed ^ columns[third];
            for (size_t block = 0; block < blocks.size(); ++block) {
                const uint64_t key = wanted & blocks[block];
                if (sorted_engine) {
                    const auto& table = sorted_tables[block];
                    const auto lower = std::lower_bound(
                        table.begin(), table.end(),
                        std::make_pair(key, uint16_t{0})
                    );
                    const auto upper = std::upper_bound(
                        table.begin(), table.end(),
                        std::make_pair(key, std::numeric_limits<uint16_t>::max())
                    );
                    for (auto iterator = lower; iterator != upper; ++iterator) {
                        const auto [left, right] = unpack_pair(iterator->second);
                        test_pair(left, right, third, wanted);
                    }
                } else {
                    const auto range = hash_tables[block].equal_range(key);
                    for (auto iterator = range.first; iterator != range.second; ++iterator) {
                        const auto [left, right] = unpack_pair(iterator->second);
                        test_pair(left, right, third, wanted);
                    }
                }
            }
        }
    }
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
        process_live_orbit(support, counts, sorted_engine);
    }
    std::cout << "PASS engine=" << (sorted_engine ? "sorted-blocks" : "hash-blocks")
              << " orbits=" << counts.orbits
              << " sign_assignments=" << counts.sign_assignments
              << " third_queries=" << counts.third_queries
              << " bucket_hits=" << counts.bucket_hits
              << " radius_matches=" << counts.radius_matches
              << " triple_candidates=" << counts.triple_candidates
              << " exact_sign_tests=" << counts.exact_sign_tests
              << " low_energy_vectors=" << counts.low_energy_vectors
              << " live_candidates=" << counts.live_candidates;
    for (int candidate_energy = 2; candidate_energy <= 20; ++candidate_energy) {
        if (counts.live_by_energy[candidate_energy]) {
            std::cout << " live_E" << candidate_energy << '='
                      << counts.live_by_energy[candidate_energy];
        }
    }
    std::cout << '\n';
    return 0;
}
