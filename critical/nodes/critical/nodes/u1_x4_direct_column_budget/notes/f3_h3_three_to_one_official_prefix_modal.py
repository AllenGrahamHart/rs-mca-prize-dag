#!/usr/bin/env python3
"""Parallel exact falsifier for H3-3TO1-C36 near the official boundary."""

from __future__ import annotations

import json
import subprocess
import textwrap

import modal


app = modal.App("rs-mca-h3-three-to-one-official-prefix")
image = modal.Image.debian_slim().apt_install("g++")

ORDER = 8192
ROW_COUNT = 12


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
        if (exponent & 1) {
            result = static_cast<u64>((__uint128_t)result * base % modulus);
        }
        base = static_cast<u64>((__uint128_t)base * base % modulus);
        exponent >>= 1;
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 3) return 1;
    const u64 n = std::strtoull(argv[1], nullptr, 10);
    const u64 p = std::strtoull(argv[2], nullptr, 10);
    constexpr double deadline_seconds = 48.0;
    const auto started = std::chrono::steady_clock::now();

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
    std::vector<std::uint32_t> inverses;
    shifted.reserve(n - 1);
    inverses.reserve(n - 1);
    u64 value = 1;
    for (u64 exponent = 0; exponent < n; ++exponent) {
        const u64 item = (1 + p - value) % p;
        if (item != 0) {
            shifted.push_back(static_cast<std::uint32_t>(item));
            inverses.push_back(static_cast<std::uint32_t>(mod_pow(item, p - 2, p)));
        }
        value = static_cast<u64>((__uint128_t)value * generator % p);
    }
    if (shifted.size() != n - 1) return 3;

    // Pair multiplicities are at most |A|=n-1, so uint16 is exact at n=8192.
    std::vector<std::uint16_t> products(p, 0);
    std::vector<std::uint16_t> quotients(p, 0);
    std::size_t processed_left = 0;
    for (std::size_t left_index = 0; left_index < shifted.size(); ++left_index) {
        const u64 left = shifted[left_index];
        for (std::size_t right_index = 0; right_index < shifted.size(); ++right_index) {
            const u64 product = static_cast<u64>(
                (__uint128_t)left * shifted[right_index] % p);
            const u64 quotient = static_cast<u64>(
                (__uint128_t)left * inverses[right_index] % p);
            ++products[product];
            ++quotients[quotient];
        }
        processed_left = left_index + 1;
        if ((processed_left & 31U) == 0) {
            const double seconds = std::chrono::duration<double>(
                std::chrono::steady_clock::now() - started).count();
            if (seconds >= deadline_seconds) {
                std::cout << "status=PARTIAL_TIMEOUT\nprocessed_left=" << processed_left
                          << "\nseconds=" << seconds << "\n";
                return 0;
            }
        }
    }

    u64 three_to_one = 0;
    u64 overlap_max = 0;
    for (u64 item = 1; item < p; ++item) {
        three_to_one += static_cast<u64>(products[item]) * quotients[item];
        if (item != 1 && quotients[item] != 0) {
            overlap_max = std::max<u64>(overlap_max, products[item]);
        }
    }
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::cout << "status=EXHAUSTIVE\nprocessed_left=" << processed_left
              << "\nthree_to_one=" << three_to_one
              << "\noverlap_max=" << overlap_max
              << "\nseconds=" << seconds << "\n";
    return 0;
}
"""


def is_prime(value: int) -> bool:
    """Deterministic Miller-Rabin for the 64-bit range used by this sweep."""
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime
    odd = value - 1
    shift = 0
    while odd % 2 == 0:
        odd //= 2
        shift += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        witness = pow(base, odd, value)
        if witness in (1, value - 1):
            continue
        for _ in range(shift - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def official_prefix(order: int, count: int) -> list[int]:
    primes: list[int] = []
    multiplier = order
    while len(primes) < count:
        candidate = multiplier * order + 1
        if is_prime(candidate):
            primes.append(candidate)
        multiplier += 1
    return primes


@app.function(image=image, cpu=2, memory=1024, timeout=60)
def scan(order: int, prime: int) -> dict[str, object]:
    source = "/tmp/three_to_one_prefix.cpp"
    binary = "/tmp/three_to_one_prefix"
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
    result: dict[str, object] = {"order": order, "prime": prime}
    for line in completed.stdout.splitlines():
        key, value = line.split("=", 1)
        if key == "status":
            result[key] = value
        elif key == "seconds":
            result[key] = float(value)
        else:
            result[key] = int(value)
    return result


@app.local_entrypoint()
def main() -> None:
    primes = official_prefix(ORDER, ROW_COUNT)
    cases = [(ORDER, prime) for prime in primes]
    results = list(scan.starmap(cases, return_exceptions=True))
    threshold = 36 * ORDER**2 - 8 * ORDER ** (4 / 3) - ORDER / 2
    rows: list[dict[str, object]] = []
    for result in results:
        if not isinstance(result, dict):
            rows.append({"status": "REMOTE_EXCEPTION", "detail": str(result)})
            continue
        row = dict(result)
        if row.get("status") == "EXHAUSTIVE":
            count = int(row["three_to_one"])
            row["ratio_n2"] = count / ORDER**2
            row["threshold_fraction"] = count / threshold
            row["c36_survives"] = count < threshold
        rows.append(row)
    rows.sort(key=lambda row: int(row.get("prime", 0)))
    exhaustive = [row for row in rows if row.get("status") == "EXHAUSTIVE"]
    worst = max(exhaustive, key=lambda row: int(row["three_to_one"]))
    summary = {
        "order": ORDER,
        "requested": ROW_COUNT,
        "completed": len(exhaustive),
        "threshold": threshold,
        "worst_prime": worst["prime"],
        "worst_count": worst["three_to_one"],
        "worst_ratio_n2": worst["ratio_n2"],
        "worst_threshold_fraction": worst["threshold_fraction"],
        "falsified": any(not bool(row["c36_survives"]) for row in exhaustive),
    }
    print(json.dumps({"summary": summary, "rows": rows}, indent=2, sort_keys=True))
    print(
        "H3_THREE_TO_ONE_OFFICIAL_PREFIX "
        f"completed={summary['completed']} falsified={int(summary['falsified'])} "
        f"worst_prime={summary['worst_prime']} "
        f"worst_ratio_n2={float(summary['worst_ratio_n2']):.9f}"
    )
