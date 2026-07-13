#!/usr/bin/env python3
"""Stress C36' on F12 factors where 2 has exact order 8192.

The dense row verifier indexes arrays by the field size and is unusable for
these 38- and 51-bit primes. This audit sorts the 33.5M unordered products,
keeps only product fibers above the actual cutoff, then reuses the memory for
the 67.1M ordered quotients. Each worker has an internal 90-second cutoff and
prints stage checkpoints before any potentially long step.
"""

from __future__ import annotations

import json
import subprocess
import textwrap

import modal


ORDER = 8192
PRIMES = (190_274_191_361, 1_256_132_134_125_569)

app = modal.App("rs-mca-h3-fermat-factor-adversary")
image = modal.Image.debian_slim().apt_install("g++")

CPP_SOURCE = r"""
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

using u16 = std::uint16_t;
using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = __uint128_t;

struct Rich {
    u64 target;
    u32 product;
    u16 diagonal;
    u32 orbit;
    u32 quotient = 0;
};

u64 mul_mod(u64 left, u64 right, u64 modulus) {
    return static_cast<u64>(static_cast<u128>(left) * right % modulus);
}

u64 mod_pow(u64 base, u64 exponent, u64 modulus) {
    u64 result = 1;
    while (exponent) {
        if (exponent & 1) result = mul_mod(result, base, modulus);
        base = mul_mod(base, base, modulus);
        exponent >>= 1;
    }
    return result;
}

bool is_prime(u64 value) {
    if (value < 2) return false;
    for (u64 prime : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL,
                      19ULL, 23ULL, 29ULL, 31ULL, 37ULL}) {
        if (value % prime == 0) return value == prime;
    }
    u64 odd = value - 1;
    unsigned power = 0;
    while ((odd & 1) == 0) {
        odd >>= 1;
        ++power;
    }
    for (u64 base : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL,
                     9780504ULL, 1795265022ULL}) {
        if (base % value == 0) continue;
        u64 witness = mod_pow(base % value, odd, value);
        if (witness == 1 || witness == value - 1) continue;
        bool composite = true;
        for (unsigned exponent = 1; exponent < power; ++exponent) {
            witness = mul_mod(witness, witness, value);
            if (witness == value - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

std::string decimal(u128 value) {
    if (value == 0) return "0";
    std::string result;
    while (value) {
        result.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

u128 choose_five(u64 value) {
    if (value < 5) return 0;
    return static_cast<u128>(value) * (value - 1) * (value - 2)
        * (value - 3) * (value - 4) / 120;
}

double seconds_since(const std::chrono::steady_clock::time_point& start) {
    return std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start
    ).count();
}

void stage(const char* name, const std::chrono::steady_clock::time_point& start) {
    std::cout << "STAGE " << name << " seconds=" << seconds_since(start) << "\n";
    std::cout.flush();
}

int main(int argc, char** argv) {
    if (argc != 3) return 1;
    const u64 n = std::strtoull(argv[1], nullptr, 10);
    const u64 p = std::strtoull(argv[2], nullptr, 10);
    const auto start = std::chrono::steady_clock::now();

    if (n == 0 || (n & (n - 1)) || p < n * n || (p - 1) % n) return 2;
    if (!is_prime(p)) return 10;
    if (mod_pow(2, n, p) != 1 || mod_pow(2, n / 2, p) != p - 1) return 3;

    std::vector<u64> shifted;
    shifted.reserve(n - 1);
    u64 root = 2;
    for (u64 exponent = 1; exponent < n; ++exponent) {
        shifted.push_back((1 + p - root) % p);
        root = mul_mod(root, 2, p);
    }
    if (root != 1) return 4;
    auto unique_check = shifted;
    std::sort(unique_check.begin(), unique_check.end());
    if (std::adjacent_find(unique_check.begin(), unique_check.end()) != unique_check.end()) {
        return 5;
    }
    unique_check.clear();
    unique_check.shrink_to_fit();
    stage("domain", start);

    std::unordered_map<u64, u16> diagonal;
    diagonal.reserve(2 * shifted.size());
    for (u64 value : shifted) ++diagonal[mul_mod(value, value, p)];

    const u64 unordered_count = (n - 1) * n / 2;
    std::vector<u64> values;
    values.reserve(unordered_count);
    for (std::size_t left = 0; left < shifted.size(); ++left) {
        for (std::size_t right = left; right < shifted.size(); ++right) {
            values.push_back(mul_mod(shifted[left], shifted[right], p));
        }
    }
    if (values.size() != unordered_count) return 6;
    stage("products-generated", start);
    std::sort(values.begin(), values.end());
    stage("products-sorted", start);

    std::vector<Rich> rich;
    u128 ordered_product_total = 0;
    u32 product_max = 0;
    u64 product_one = 0;
    using Top = std::pair<u32, u64>;
    std::priority_queue<Top, std::vector<Top>, std::greater<Top>> top_products;
    for (std::size_t begin = 0; begin < values.size();) {
        std::size_t end = begin + 1;
        while (end < values.size() && values[end] == values[begin]) ++end;
        const u64 target = values[begin];
        const u32 orbit = static_cast<u32>(end - begin);
        const u16 fixed = diagonal.count(target) ? diagonal[target] : 0;
        const u32 product = 2 * orbit - fixed;
        ordered_product_total += product;
        product_max = std::max(product_max, product);
        if (target == 1) product_one = product;
        if (top_products.size() < 20) {
            top_products.emplace(product, target);
        } else if (top_products.top() < Top(product, target)) {
            top_products.pop();
            top_products.emplace(product, target);
        }
        if (target != 1 && product >= 19) {
            rich.push_back({target, product, fixed, orbit, 0});
        }
        begin = end;
    }
    if (ordered_product_total != static_cast<u128>(n - 1) * (n - 1)) return 7;
    std::sort(rich.begin(), rich.end(), [](const Rich& a, const Rich& b) {
        return a.target < b.target;
    });
    std::cout << "STAGE rich-extracted seconds=" << seconds_since(start)
              << " rich_targets=" << rich.size()
              << " product_max=" << product_max << "\n";
    std::cout.flush();

    values.clear();
    values.shrink_to_fit();
    diagonal.clear();

    std::vector<u64> inverse;
    inverse.reserve(shifted.size());
    for (u64 value : shifted) inverse.push_back(mod_pow(value, p - 2, p));

    const u64 ordered_count = (n - 1) * (n - 1);
    values.reserve(ordered_count);
    for (u64 numerator : shifted) {
        for (u64 denominator_inverse : inverse) {
            values.push_back(mul_mod(numerator, denominator_inverse, p));
        }
    }
    if (values.size() != ordered_count) return 8;
    stage("quotients-generated", start);
    std::sort(values.begin(), values.end());
    stage("quotients-sorted", start);

    std::size_t rich_index = 0;
    u128 quotient_total = 0;
    u64 quotient_one = 0;
    for (std::size_t begin = 0; begin < values.size();) {
        std::size_t end = begin + 1;
        while (end < values.size() && values[end] == values[begin]) ++end;
        const u64 target = values[begin];
        const u32 quotient = static_cast<u32>(end - begin);
        quotient_total += quotient;
        if (target == 1) quotient_one = quotient;
        while (rich_index < rich.size() && rich[rich_index].target < target) ++rich_index;
        if (rich_index < rich.size() && rich[rich_index].target == target) {
            rich[rich_index].quotient = quotient;
        }
        begin = end;
    }
    if (quotient_total != static_cast<u128>(ordered_count) || quotient_one != n - 1) {
        return 9;
    }
    stage("quotients-merged", start);

    u128 x18 = 0;
    u128 rich_nonswap = 0;
    u128 rich_fifth = 0;
    u64 supported_rich = 0;
    u64 max_p_plus_2r = 0;
    using Contribution = std::tuple<u128, u64, u32, u32>;
    std::vector<Contribution> contributions;
    for (const Rich& row : rich) {
        if (row.quotient == 0) continue;
        ++supported_rich;
        const u128 excess = static_cast<u128>(row.product - 18) * row.quotient;
        const u128 nonswap = static_cast<u128>(
            static_cast<u64>(row.product) * (row.product - 2) + row.diagonal
        ) * row.quotient;
        const u128 fifth = choose_five(row.orbit) * row.quotient;
        x18 += excess;
        rich_nonswap += nonswap;
        rich_fifth += fifth;
        max_p_plus_2r = std::max<u64>(
            max_p_plus_2r, row.product + 2 * row.quotient
        );
        contributions.emplace_back(excess, row.target, row.product, row.quotient);
    }
    std::sort(contributions.begin(), contributions.end(), std::greater<>());

    std::vector<Top> top;
    while (!top_products.empty()) {
        top.push_back(top_products.top());
        top_products.pop();
    }
    std::sort(top.begin(), top.end(), std::greater<>());

    std::cout << "RESULT {\"order\":" << n
              << ",\"prime\":" << p
              << ",\"prime_verified\":true"
              << ",\"generator\":2"
              << ",\"seconds\":" << seconds_since(start)
              << ",\"product_max\":" << product_max
              << ",\"product_one\":" << product_one
              << ",\"rich_targets\":" << rich.size()
              << ",\"supported_rich_targets\":" << supported_rich
              << ",\"x18\":\"" << decimal(x18) << "\""
              << ",\"rich_nonswap\":\"" << decimal(rich_nonswap) << "\""
              << ",\"rich_fifth\":\"" << decimal(rich_fifth) << "\""
              << ",\"c36_lhs\":\"" << decimal(17 * x18) << "\""
              << ",\"c36_rhs\":\"" << decimal(300 * static_cast<u128>(n) * n) << "\""
              << ",\"c36_pass\":"
              << (17 * x18 <= 300 * static_cast<u128>(n) * n ? "true" : "false")
              << ",\"nonswap_rhs\":\""
              << decimal(1200 * static_cast<u128>(n) * n) << "\""
              << ",\"nonswap_pass\":"
              << (rich_nonswap <= 1200 * static_cast<u128>(n) * n ? "true" : "false")
              << ",\"fifth_lhs\":\"" << decimal(17 * rich_fifth) << "\""
              << ",\"fifth_rhs\":\""
              << decimal(34650 * static_cast<u128>(n) * n) << "\""
              << ",\"fifth_pass\":"
              << (17 * rich_fifth <= 34650 * static_cast<u128>(n) * n ? "true" : "false")
              << ",\"max_p_plus_2r\":" << max_p_plus_2r
              << ",\"top_products\":[";
    for (std::size_t i = 0; i < top.size(); ++i) {
        if (i) std::cout << ',';
        std::cout << '[' << top[i].second << ',' << top[i].first << ']';
    }
    std::cout << "],\"top_x18\":[";
    for (std::size_t i = 0; i < std::min<std::size_t>(20, contributions.size()); ++i) {
        if (i) std::cout << ',';
        const auto& [contribution, target, product, quotient] = contributions[i];
        std::cout << '[' << target << ',' << product << ',' << quotient
                  << ",\"" << decimal(contribution) << "\"]";
    }
    std::cout << "]}\n";
    std::cout.flush();
    return 0;
}
"""


@app.function(image=image, cpu=2, memory=4096, timeout=120, max_containers=2)
def audit(prime: int) -> dict[str, object]:
    source = "/tmp/fermat_factor_adversary.cpp"
    binary = "/tmp/fermat_factor_adversary"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(CPP_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=15,
    )
    process = subprocess.Popen(
        [binary, str(ORDER), str(prime)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    try:
        output, _ = process.communicate(timeout=90)
        status = "PASS" if process.returncode == 0 else "FAIL"
    except subprocess.TimeoutExpired:
        process.kill()
        output, _ = process.communicate()
        status = "TIMEOUT"
    result_line = next(
        (line.removeprefix("RESULT ") for line in output.splitlines() if line.startswith("RESULT ")),
        None,
    )
    return {
        "prime": prime,
        "status": status,
        "returncode": process.returncode,
        "checkpoints": [line for line in output.splitlines() if line.startswith("STAGE ")],
        "result": json.loads(result_line) if result_line else None,
        "output_tail": output[-4000:],
    }


@app.local_entrypoint()
def main() -> None:
    rows = list(audit.map(PRIMES, return_exceptions=True))
    normalized = []
    for prime, row in zip(PRIMES, rows, strict=True):
        if isinstance(row, BaseException):
            normalized.append({"prime": prime, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    print(json.dumps(normalized, indent=2, sort_keys=True))
    if any(row["status"] != "PASS" for row in normalized):
        raise SystemExit(1)
    print(f"H3_FERMAT_FACTOR_ADVERSARY_PASS rows={len(normalized)}")
