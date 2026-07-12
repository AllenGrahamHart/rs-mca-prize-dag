#!/usr/bin/env python3
"""Bounded parallel falsification sweep for the paired PGL2 C36 route."""

from __future__ import annotations

import json
import subprocess
import textwrap

import modal


app = modal.App("rs-mca-h3-paired-smallrow-sweep")
image = modal.Image.debian_slim().apt_install("g++")


CPP_SOURCE = r"""
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
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

bool is_prime(u64 value) {
    if (value < 2) return false;
    if ((value & 1) == 0) return value == 2;
    for (u64 divisor = 3; divisor * divisor <= value; divisor += 2) {
        if (value % divisor == 0) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc != 4) return 1;
    const u64 n = std::strtoull(argv[1], nullptr, 10);
    const u64 first_multiplier = std::strtoull(argv[2], nullptr, 10);
    const u64 last_multiplier = std::strtoull(argv[3], nullptr, 10);
    const auto start = std::chrono::steady_clock::now();

    u64 rows = 0;
    u64 best_score = 0, best_p = 0, best_t = 0, best_product = 0, best_quotient = 0;
    u64 max_weighted_excess = 0, max_nonswap = 0;
    bool timed_out = false;

    for (u64 multiplier = first_multiplier; multiplier < last_multiplier; ++multiplier) {
        if (std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count() > 48.0) {
            timed_out = true;
            break;
        }
        const u64 p = n * multiplier + 1;
        if (p < n * n || !is_prime(p)) continue;

        u64 generator = 0;
        for (u64 candidate = 2; candidate < 1000 && generator == 0; ++candidate) {
            const u64 value = mod_pow(candidate, (p - 1) / n, p);
            if (value != 1 && mod_pow(value, n / 2, p) != 1) generator = value;
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

        std::vector<std::uint16_t> products(p, 0), quotients(p, 0), diagonal(p, 0);
        for (std::size_t i = 0; i < shifted.size(); ++i) {
            const u64 square = static_cast<u64>((__uint128_t)shifted[i] * shifted[i] % p);
            ++diagonal[square];
            for (std::size_t j = 0; j < shifted.size(); ++j) {
                const u64 product = static_cast<u64>((__uint128_t)shifted[i] * shifted[j] % p);
                const u64 quotient = static_cast<u64>((__uint128_t)shifted[i] * inverse[j] % p);
                ++products[product];
                ++quotients[quotient];
            }
        }

        u64 weighted_excess = 0, nonswap = 0;
        for (u64 t = 2; t < p; ++t) {
            const u64 product = products[t], quotient = quotients[t];
            if (quotient == 0) continue;
            const u64 score = product + 2 * quotient;
            if (score > best_score) {
                best_score = score;
                best_p = p;
                best_t = t;
                best_product = product;
                best_quotient = quotient;
            }
            if (product > 35) weighted_excess += (product - 35) * quotient;
            nonswap += (product * (product - 2) + diagonal[t]) * quotient;
        }
        max_weighted_excess = std::max(max_weighted_excess, weighted_excess);
        max_nonswap = std::max(max_nonswap, nonswap);
        ++rows;
    }

    std::cout << "{\"n\":" << n
              << ",\"first_multiplier\":" << first_multiplier
              << ",\"last_multiplier\":" << last_multiplier
              << ",\"rows\":" << rows
              << ",\"best_score\":" << best_score
              << ",\"best_p\":" << best_p
              << ",\"best_t\":" << best_t
              << ",\"best_product\":" << best_product
              << ",\"best_quotient\":" << best_quotient
              << ",\"max_weighted_excess\":" << max_weighted_excess
              << ",\"max_nonswap\":" << max_nonswap
              << ",\"timed_out\":" << (timed_out ? "true" : "false") << "}\n";
    return 0;
}
"""


INSPECT_SOURCE = r"""
#include <cstdint>
#include <cstdlib>
#include <iostream>
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

int main(int argc, char** argv) {
    if (argc != 4) return 1;
    const u64 n = std::strtoull(argv[1], nullptr, 10);
    const u64 p = std::strtoull(argv[2], nullptr, 10);
    const u64 target = std::strtoull(argv[3], nullptr, 10);
    u64 generator = 0;
    for (u64 candidate = 2; candidate < 1000 && generator == 0; ++candidate) {
        const u64 value = mod_pow(candidate, (p - 1) / n, p);
        if (value != 1 && mod_pow(value, n / 2, p) != 1) generator = value;
    }
    if (generator == 0) return 2;

    std::vector<u64> shifted, inverse;
    u64 root = generator;
    for (u64 exponent = 1; exponent < n; ++exponent) {
        const u64 item = (1 + p - root) % p;
        shifted.push_back(item);
        inverse.push_back(mod_pow(item, p - 2, p));
        root = static_cast<u64>((__uint128_t)root * generator % p);
    }

    std::cout << "{\"n\":" << n << ",\"p\":" << p << ",\"t\":" << target
              << ",\"generator\":" << generator << ",\"product_pairs\":[";
    bool first = true;
    for (std::size_t i = 0; i < shifted.size(); ++i) {
        for (std::size_t j = 0; j < shifted.size(); ++j) {
            if (static_cast<u64>((__uint128_t)shifted[i] * shifted[j] % p) == target) {
                if (!first) std::cout << ',';
                first = false;
                std::cout << '[' << i + 1 << ',' << j + 1 << ']';
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
                std::cout << '[' << i + 1 << ',' << j + 1 << ']';
            }
        }
    }
    std::cout << "]}\n";
    return 0;
}
"""


@app.function(image=image, cpu=2, memory=1024, timeout=60)
def sweep_shard(task: tuple[int, int, int]) -> dict[str, object]:
    order, first_multiplier, last_multiplier = task
    source = "/tmp/paired_sweep.cpp"
    binary = "/tmp/paired_sweep"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(CPP_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=10,
    )
    completed = subprocess.run(
        [binary, str(order), str(first_multiplier), str(last_multiplier)],
        check=True,
        capture_output=True,
        text=True,
        timeout=52,
    )
    return json.loads(completed.stdout)


@app.function(image=image, cpu=2, memory=512, timeout=60)
def inspect_extremizer(order: int, prime: int, target: int) -> dict[str, object]:
    source = "/tmp/paired_inspect.cpp"
    binary = "/tmp/paired_inspect"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(INSPECT_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=10,
    )
    completed = subprocess.run(
        [binary, str(order), str(prime), str(target)],
        check=True,
        capture_output=True,
        text=True,
        timeout=50,
    )
    return json.loads(completed.stdout)


def tasks() -> list[tuple[int, int, int]]:
    specifications = (
        (64, 64, 20_000, 1_000),
        (128, 128, 12_000, 600),
        (256, 256, 8_000, 400),
        (512, 512, 5_000, 250),
        (1_024, 1_024, 3_000, 125),
        (2_048, 2_048, 2_800, 75),
        (4_096, 4_096, 4_500, 40),
    )
    out: list[tuple[int, int, int]] = []
    for order, first, last, width in specifications:
        for start in range(first, last, width):
            out.append((order, start, min(start + width, last)))
    return out


@app.local_entrypoint()
def main() -> None:
    results = list(sweep_shard.map(tasks(), order_outputs=False))
    completed_rows = sum(int(result["rows"]) for result in results)
    best = max(results, key=lambda result: int(result["best_score"]))
    falsifiers = [result for result in results if int(result["best_score"]) > 37]
    orders = sorted({int(result["n"]) for result in results})
    best_by_order = {
        str(order): max(
            (result for result in results if int(result["n"]) == order),
            key=lambda result: int(result["best_score"]),
        )
        for order in orders
    }
    rows_by_order = {
        str(order): sum(
            int(result["rows"]) for result in results if int(result["n"]) == order
        )
        for order in orders
    }
    max_nonswap_by_order = {
        str(order): max(
            int(result["max_nonswap"])
            for result in results
            if int(result["n"]) == order
        )
        for order in orders
    }
    digest = {
        "tasks": len(results),
        "completed_rows": completed_rows,
        "timed_out_tasks": sum(bool(result["timed_out"]) for result in results),
        "best": best,
        "best_by_order": best_by_order,
        "rows_by_order": rows_by_order,
        "max_nonswap_by_order": max_nonswap_by_order,
        "max_weighted_excess": max(
            int(result["max_weighted_excess"]) for result in results
        ),
        "falsifier_shards": sorted(
            falsifiers,
            key=lambda result: int(result["best_score"]),
            reverse=True,
        ),
    }
    digest["extremizer"] = inspect_extremizer.remote(
        int(best["n"]), int(best["best_p"]), int(best["best_t"])
    )
    print(json.dumps(digest, indent=2, sort_keys=True))
    print(
        "H3_PAIRED_SMALLROW_SWEEP "
        f"rows={completed_rows} best={best['best_score']} "
        f"falsifiers={len(falsifiers)} timeouts={digest['timed_out_tasks']}"
    )
