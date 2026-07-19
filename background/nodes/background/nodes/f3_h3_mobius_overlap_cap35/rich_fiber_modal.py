#!/usr/bin/env python3
"""Recover exact exponent patterns in a rich official M35 fiber on Modal."""

from __future__ import annotations

import json
import subprocess
import textwrap

import modal


app = modal.App("rs-mca-h3-mobius-rich-fiber")
image = modal.Image.debian_slim().apt_install("g++")

ORDER = 8192
PRIME = 67_657_729


CPP_SOURCE = r"""
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>

using u64 = std::uint64_t;

u64 mod_pow(u64 base, u64 exponent, u64 modulus) {
    u64 result = 1;
    while (exponent) {
        if (exponent & 1) result = static_cast<u64>((__uint128_t)result * base % modulus);
        base = static_cast<u64>((__uint128_t)base * base % modulus);
        exponent >>= 1;
    }
    return result;
}

u64 choose_five(u64 value) {
    if (value < 5) return 0;
    return value * (value - 1) * (value - 2) * (value - 3) * (value - 4) / 120;
}

int main(int argc, char** argv) {
    if (argc != 3) return 1;
    const u64 n = std::strtoull(argv[1], nullptr, 10);
    const u64 p = std::strtoull(argv[2], nullptr, 10);

    u64 generator = 0;
    for (u64 candidate = 2; candidate < p; ++candidate) {
        const u64 value = mod_pow(candidate, (p - 1) / n, p);
        if (mod_pow(value, n / 2, p) != 1) {
            generator = value;
            break;
        }
    }
    if (generator == 0) return 2;

    std::vector<std::uint32_t> shifted;
    std::vector<std::uint32_t> inverse;
    shifted.reserve(n - 1);
    inverse.reserve(n - 1);
    u64 root = generator;
    for (u64 exponent = 1; exponent < n; ++exponent) {
        const u64 item = (1 + p - root) % p;
        shifted.push_back(static_cast<std::uint32_t>(item));
        inverse.push_back(static_cast<std::uint32_t>(mod_pow(item, p - 2, p)));
        root = static_cast<u64>((__uint128_t)root * generator % p);
    }

    std::vector<std::uint16_t> products(p, 0);
    std::vector<std::uint16_t> quotients(p, 0);
    std::vector<std::uint16_t> diagonal_products(p, 0);
    for (std::size_t i = 0; i < shifted.size(); ++i) {
        const u64 square = static_cast<u64>((__uint128_t)shifted[i] * shifted[i] % p);
        ++diagonal_products[square];
        for (std::size_t j = 0; j < shifted.size(); ++j) {
            const u64 product = static_cast<u64>((__uint128_t)shifted[i] * shifted[j] % p);
            const u64 quotient = static_cast<u64>((__uint128_t)shifted[i] * inverse[j] % p);
            ++products[product];
            ++quotients[quotient];
        }
    }

    std::vector<std::tuple<u64, u64, u64>> ranked;
    for (u64 t = 2; t < p; ++t) {
        if (quotients[t] != 0) ranked.emplace_back(products[t], quotients[t], t);
    }
    std::sort(ranked.begin(), ranked.end(), std::greater<>());
    if (ranked.empty()) return 3;
    const auto [product_max, quotient_at_max, target] = ranked.front();

    u64 factorial_moment = 0;
    u64 swap_moment = 0;
    u64 weighted_excess = 0;
    u64 weighted_excess18 = 0;
    std::map<u64, std::tuple<u64, u64, u64>> quotient_profile;
    std::vector<std::tuple<u64, u64, u64, u64>> contribution_ranked;
    u64 max_p_plus_r = 0;
    u64 max_p_plus_2r = 0;
    u64 max_pr = 0;
    u64 single_accident = 0;
    u64 double_accident = 0;
    u64 rich_nonswap = 0;
    u64 rich_targets = 0;
    u64 fifth_orbit_moment = 0;
    u64 rich_fifth_orbit_moment = 0;
    for (u64 t = 2; t < p; ++t) {
        const u64 pc = products[t];
        const u64 qc = quotients[t];
        factorial_moment += pc * (pc - (pc != 0)) * qc;
        swap_moment += (pc - diagonal_products[t]) * qc;
        if (pc > 35) weighted_excess += (pc - 35) * qc;
        if (pc > 18) weighted_excess18 += (pc - 18) * qc;
        const u64 orbit_count = (pc + diagonal_products[t]) / 2;
        fifth_orbit_moment += choose_five(orbit_count) * qc;
        if (pc >= 19) rich_fifth_orbit_moment += choose_five(orbit_count) * qc;
        if (qc != 0) {
            const u64 qbase = pc * pc + diagonal_products[t] - 2 * pc;
            const u64 nonswap = qbase * qc;
            single_accident += qbase;
            double_accident += qbase * (qc - 1);
            if (pc >= 19) {
                rich_nonswap += nonswap;
                ++rich_targets;
            }
            auto& [parameters, max_product, contribution] = quotient_profile[qc];
            ++parameters;
            max_product = std::max(max_product, pc);
            contribution += nonswap;
            contribution_ranked.emplace_back(nonswap, pc, qc, t);
            max_p_plus_r = std::max(max_p_plus_r, pc + qc);
            max_p_plus_2r = std::max(max_p_plus_2r, pc + 2 * qc);
            max_pr = std::max(max_pr, pc * qc);
        }
    }
    std::sort(contribution_ranked.begin(), contribution_ranked.end(), std::greater<>());

    std::cout << "{\"order\":" << n << ",\"prime\":" << p
              << ",\"generator\":" << generator << ",\"target\":" << target
              << ",\"product_max\":" << product_max
              << ",\"quotient_at_max\":" << quotient_at_max
              << ",\"factorial_moment\":" << factorial_moment
              << ",\"swap_moment\":" << swap_moment
              << ",\"nonswap_moment\":" << (factorial_moment - swap_moment)
              << ",\"max_p_plus_r\":" << max_p_plus_r
              << ",\"max_p_plus_2r\":" << max_p_plus_2r
              << ",\"max_pr\":" << max_pr
              << ",\"single_accident\":" << single_accident
              << ",\"double_accident\":" << double_accident
              << ",\"rich_nonswap\":" << rich_nonswap
              << ",\"rich_targets\":" << rich_targets
              << ",\"fifth_orbit_moment\":" << fifth_orbit_moment
              << ",\"rich_fifth_orbit_moment\":" << rich_fifth_orbit_moment
              << ",\"weighted_excess18\":" << weighted_excess18
              << ",\"weighted_excess\":" << weighted_excess << ",\"top\":[";
    for (std::size_t i = 0; i < std::min<std::size_t>(ranked.size(), 12); ++i) {
        if (i) std::cout << ',';
        const auto [pc, qc, t] = ranked[i];
        std::cout << "[" << t << ',' << pc << ',' << qc << "]";
    }
    std::cout << "],\"quotient_profile\":[";
    bool first = true;
    for (const auto& [qc, values] : quotient_profile) {
        if (!first) std::cout << ',';
        first = false;
        const auto [parameters, max_product, contribution] = values;
        std::cout << "[" << qc << ',' << parameters << ',' << max_product << ',' << contribution << "]";
    }
    std::cout << "],\"top_nonswap_contributions\":[";
    first = true;
    for (std::size_t i = 0; i < std::min<std::size_t>(contribution_ranked.size(), 20); ++i) {
        if (!first) std::cout << ',';
        first = false;
        const auto [contribution, pc, qc, t] = contribution_ranked[i];
        std::cout << "[" << t << ',' << pc << ',' << qc << ',' << contribution << "]";
    }
    std::cout << "],\"product_pairs\":[";
    first = true;
    for (std::size_t i = 0; i < shifted.size(); ++i) {
        for (std::size_t j = i; j < shifted.size(); ++j) {
            if (static_cast<u64>((__uint128_t)shifted[i] * shifted[j] % p) == target) {
                if (!first) std::cout << ',';
                first = false;
                std::cout << "[" << i + 1 << ',' << j + 1 << "]";
            }
        }
    }
    std::cout << "],\"quotient_pairs\":[";
    first = true;
    for (std::size_t i = 0; i < shifted.size(); ++i) {
        for (std::size_t j = 0; j < shifted.size(); ++j) {
            if (static_cast<u64>((__uint128_t)shifted[i] * inverse[j] % p) == target) {
                if (!first) std::cout << ',';
                first = false;
                std::cout << "[" << i + 1 << ',' << j + 1 << "]";
            }
        }
    }
    std::cout << "]}\n";
    return 0;
}
"""


@app.function(image=image, cpu=2, memory=1024, timeout=60)
def recover(order: int, prime: int) -> dict[str, object]:
    source = "/tmp/rich_fiber.cpp"
    binary = "/tmp/rich_fiber"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(CPP_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=10,
    )
    completed = subprocess.run(
        [binary, str(order), str(prime)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    result = recover.remote(ORDER, PRIME)
    print(json.dumps(result, indent=2, sort_keys=True))
    print(
        "H3_MOBIUS_RICH_FIBER "
        f"p={PRIME} product_max={result['product_max']} "
        f"quotient_at_max={result['quotient_at_max']} "
        f"factorial_ratio={int(result['factorial_moment']) / ORDER**2:.9f}"
    )
