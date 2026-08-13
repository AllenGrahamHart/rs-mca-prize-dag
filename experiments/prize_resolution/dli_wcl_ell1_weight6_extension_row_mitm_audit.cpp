#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

struct Entry {
    u64 sum;
    std::uint32_t pair;
};

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
    return a != b && ((a - b + 512) % 512) != 256;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    modulus = std::stoull(argv[1]);
    if ((modulus - 1) % 512 != 0) return 3;

    u64 seed = 2;
    while (pow_mod(seed, (modulus - 1) / 2) == 1) ++seed;
    const u64 omega = pow_mod(seed, (modulus - 1) / 512);
    if (pow_mod(omega, 512) != 1 || pow_mod(omega, 256) != modulus - 1) return 4;

    std::vector<u64> roots(512, 1);
    for (int i = 1; i < 512; ++i) roots[i] = mul_mod(roots[i - 1], omega);

    std::vector<Entry> pairs;
    pairs.reserve(129540);
    for (int a = 1; a < 512; ++a) {
        if (a == 256) continue;
        for (int b = a + 1; b < 512; ++b) {
            if (b == 256 || !compatible(a, b)) continue;
            pairs.push_back({
                (roots[a] + roots[b]) % modulus,
                static_cast<std::uint32_t>(a | (b << 9)),
            });
        }
    }
    std::sort(pairs.begin(), pairs.end(), [](const Entry& left, const Entry& right) {
        return left.sum < right.sum || (left.sum == right.sum && left.pair < right.pair);
    });

    std::uint64_t triples = 0;
    for (int c = 1; c < 512; ++c) {
        if (c == 256) continue;
        for (int d = c + 1; d < 512; ++d) {
            if (d == 256 || !compatible(c, d)) continue;
            for (int e = d + 1; e < 512; ++e) {
                if (e == 256 || !compatible(c, e) || !compatible(d, e)) continue;
                ++triples;
                const u64 sum = ((roots[c] + roots[d]) % modulus + roots[e]) % modulus;
                const u64 target = (2 * modulus - 1 - sum) % modulus;
                const auto lower = std::lower_bound(
                    pairs.begin(), pairs.end(), target,
                    [](const Entry& item, u64 value) { return item.sum < value; }
                );
                const auto upper = std::upper_bound(
                    lower, pairs.end(), target,
                    [](u64 value, const Entry& item) { return value < item.sum; }
                );
                for (auto it = lower; it != upper; ++it) {
                    const int a = it->pair & 511;
                    const int b = it->pair >> 9;
                    if (compatible(a, c) && compatible(a, d) && compatible(a, e) &&
                        compatible(b, c) && compatible(b, d) && compatible(b, e)) {
                        std::cout << "{\"status\":\"FOUND\",\"p\":" << modulus
                                  << ",\"pair_count\":" << pairs.size()
                                  << ",\"triples_scanned\":" << triples << "}" << std::endl;
                        return 0;
                    }
                }
            }
        }
    }

    std::cout << "{\"status\":\"EXHAUSTED\",\"p\":" << modulus
              << ",\"seed\":" << seed << ",\"omega\":" << omega
              << ",\"pair_count\":" << pairs.size()
              << ",\"triples_scanned\":" << triples << "}" << std::endl;
    return 0;
}
