#include <chrono>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static constexpr int ORDER = 512;
static u64 modulus;

static u64 mul_mod(u64 a, u64 b) {
    return static_cast<u64>((u128)a * b % modulus);
}

static u64 pow_mod(u64 a, u64 e) {
    u64 out = 1;
    while (e) {
        if (e & 1) out = mul_mod(out, a);
        a = mul_mod(a, a);
        e >>= 1;
    }
    return out;
}

static bool compatible(int a, int b) {
    if (a == b) return false;
    return ((a - b + ORDER) % ORDER) != ORDER / 2;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    modulus = std::stoull(argv[1]);
    if ((modulus - 1) % (u64(1) << 41) != 0) return 3;

    u64 seed = 2;
    while (pow_mod(seed, (modulus - 1) / 2) == 1) ++seed;
    const u64 omega = pow_mod(seed, (modulus - 1) / ORDER);
    if (pow_mod(omega, ORDER) != 1 || pow_mod(omega, ORDER / 2) != modulus - 1) {
        return 4;
    }

    std::vector<u64> roots(ORDER);
    roots[0] = 1;
    for (int i = 1; i < ORDER; ++i) roots[i] = mul_mod(roots[i - 1], omega);

    std::unordered_multimap<u64, std::uint32_t> pairs;
    pairs.reserve(180000);
    for (int a = 1; a < ORDER; ++a) {
        if (a == ORDER / 2) continue;
        for (int b = a + 1; b < ORDER; ++b) {
            if (b == ORDER / 2 || !compatible(a, b)) continue;
            pairs.emplace(
                (roots[a] + roots[b]) % modulus,
                static_cast<std::uint32_t>(a | (b << 9))
            );
        }
    }

    std::uint64_t scanned = 0;
    const auto start = std::chrono::steady_clock::now();
    for (int c = 1; c < ORDER; ++c) {
        if (c == ORDER / 2) continue;
        for (int d = c + 1; d < ORDER; ++d) {
            if (d == ORDER / 2 || !compatible(c, d)) continue;
            for (int e = d + 1; e < ORDER; ++e) {
                if (e == ORDER / 2 || !compatible(c, e) || !compatible(d, e)) continue;
                ++scanned;
                const u64 triple = ((roots[c] + roots[d]) % modulus + roots[e]) % modulus;
                const u64 target = (modulus - 1 + modulus - triple) % modulus;
                const auto range = pairs.equal_range(target);
                for (auto it = range.first; it != range.second; ++it) {
                    const int a = it->second & 511;
                    const int b = it->second >> 9;
                    if (!compatible(a, c) || !compatible(a, d) || !compatible(a, e) ||
                        !compatible(b, c) || !compatible(b, d) || !compatible(b, e)) {
                        continue;
                    }
                    const u64 check = (((((1 + roots[a]) % modulus + roots[b]) % modulus +
                                          roots[c]) % modulus + roots[d]) % modulus + roots[e]) % modulus;
                    if (check != 0) return 5;
                    std::cout << "{\"status\":\"FOUND\",\"p\":" << modulus
                              << ",\"seed\":" << seed << ",\"omega\":" << omega
                              << ",\"pair_count\":" << pairs.size()
                              << ",\"triples_scanned\":" << scanned
                              << ",\"indices\":[0," << a << ',' << b << ','
                              << c << ',' << d << ',' << e << "]}" << std::endl;
                    return 0;
                }
            }
        }
        if ((c & 63) == 0) {
            std::cerr << "PROGRESS p=" << modulus << " c=" << c
                      << " triples=" << scanned << std::endl;
        }
    }

    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    std::cout << "{\"status\":\"EXHAUSTED\",\"p\":" << modulus
              << ",\"seed\":" << seed << ",\"omega\":" << omega
              << ",\"pair_count\":" << pairs.size()
              << ",\"triples_scanned\":" << scanned
              << ",\"seconds\":" << seconds << "}" << std::endl;
    return 0;
}
