#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static u64 mul_mod(u64 a, u64 b, u64 mod) {
    return static_cast<u64>((static_cast<u128>(a) * b) % mod);
}

static u64 pow_mod(u64 base, u64 exponent, u64 mod) {
    u64 result = 1;
    while (exponent) {
        if (exponent & 1) result = mul_mod(result, base, mod);
        base = mul_mod(base, base, mod);
        exponent >>= 1;
    }
    return result;
}

static bool antipodal(int left, int right) {
    return ((left - right) & 511) == 256;
}

static bool compatible(int left, int right, int a, int b, int c) {
    const int terms[5] = {left, right, a, b, c};
    for (int i = 0; i < 5; ++i) {
        for (int j = i + 1; j < 5; ++j) {
            if (terms[i] == terms[j] || antipodal(terms[i], terms[j])) return false;
        }
    }
    return true;
}

static bool primitive_relation(const std::array<int, 5>& terms,
                               const std::array<u64, 512>& powers, u64 q) {
    for (int mask = 1; mask < 31; ++mask) {
        u64 sum = 0;
        for (int index = 0; index < 5; ++index) {
            if (mask & (1 << index)) {
                sum += powers[terms[index]];
                if (sum >= q) sum -= q;
            }
        }
        if (sum == 0) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const u64 q = std::stoull(argv[1]);
    const u64 generator = std::stoull(argv[2]);
    const auto started = std::chrono::steady_clock::now();
    if ((q - 1) % (u64(1) << 41) != 0) return 3;

    const u64 omega = pow_mod(generator, (q - 1) / 512, q);
    if (pow_mod(omega, 512, q) != 1 || pow_mod(omega, 256, q) != q - 1) return 4;
    std::array<u64, 512> powers{};
    powers[0] = 1;
    for (int exponent = 1; exponent < 512; ++exponent) {
        powers[exponent] = mul_mod(powers[exponent - 1], omega, q);
    }

    std::unordered_map<u64, std::vector<std::uint32_t>> pairs;
    pairs.reserve(140000);
    std::uint64_t pair_count = 0;
    for (int left = 0; left < 512; ++left) {
        for (int right = left + 1; right < 512; ++right) {
            if (antipodal(left, right)) continue;
            u64 sum = powers[left] + powers[right];
            if (sum >= q) sum -= q;
            pairs[sum].push_back((static_cast<std::uint32_t>(left) << 9) |
                                 static_cast<std::uint32_t>(right));
            ++pair_count;
        }
    }

    std::uint64_t triple_count = 0;
    std::array<int, 5> witness{};
    bool found = false;
    for (int a = 0; a < 512 && !found; ++a) {
        for (int b = a + 1; b < 512 && !found; ++b) {
            if (antipodal(a, b)) continue;
            for (int c = b + 1; c < 512; ++c) {
                if (antipodal(a, c) || antipodal(b, c)) continue;
                ++triple_count;
                u64 sum = powers[a] + powers[b];
                if (sum >= q) sum -= q;
                sum += powers[c];
                if (sum >= q) sum -= q;
                const u64 target = sum == 0 ? 0 : q - sum;
                auto iterator = pairs.find(target);
                if (iterator == pairs.end()) continue;
                for (std::uint32_t packed : iterator->second) {
                    const int left = packed >> 9;
                    const int right = packed & 511;
                    if (!compatible(left, right, a, b, c)) continue;
                    witness = {left, right, a, b, c};
                    std::sort(witness.begin(), witness.end());
                    if (!primitive_relation(witness, powers, q)) continue;
                    found = true;
                    break;
                }
                if (found) break;
            }
        }
    }

    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::cout << "{\"q\":\"" << q << "\",\"generator\":\"" << generator
              << "\",\"omega\":\"" << omega << "\",\"pair_count\":" << pair_count
              << ",\"triples_checked\":" << triple_count << ",\"found\":"
              << (found ? "true" : "false") << ",\"relation\":[";
    if (found) {
        for (int index = 0; index < 5; ++index) {
            if (index) std::cout << ',';
            std::cout << witness[index];
        }
    }
    std::cout << "],\"seconds\":" << seconds << "}\n";
    return 0;
}
