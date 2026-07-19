#!/usr/bin/env python3
"""Bounded order-64 search above the deliberately strong p>=d^2 threshold."""

from __future__ import annotations

import json
import subprocess
import textwrap

import modal


app = modal.App("rate-half-list-order64-primary-gap")
image = modal.Image.debian_slim(python_version="3.12").apt_install("g++")


CPP_SOURCE = r"""
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>

using i64 = std::int64_t;

static i64 mod_pow(i64 base, i64 exponent, i64 prime) {
    i64 answer = 1;
    while (exponent > 0) {
        if (exponent & 1) answer = answer * base % prime;
        base = base * base % prime;
        exponent >>= 1;
    }
    return answer;
}

static i64 order_64_root(i64 prime) {
    for (i64 candidate = 2; candidate < prime; ++candidate) {
        i64 root = mod_pow(candidate, (prime - 1) / 64, prime);
        if (root != 1 && mod_pow(root, 32, prime) != 1) return root;
    }
    return 0;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const i64 prime = std::strtoll(argv[1], nullptr, 10);
    const i64 zeta = order_64_root(prime);
    if (zeta == 0) return 3;

    std::array<i64, 64> roots{};
    roots[0] = 1;
    for (int exponent = 1; exponent < 64; ++exponent) {
        roots[exponent] = roots[exponent - 1] * zeta % prime;
    }
    std::array<i64, 18> inverse_denominator{};
    for (int m = 1; m <= 17; ++m) {
        inverse_denominator[m] = mod_pow(4LL * m % prime, prime - 2, prime);
    }

    std::uint64_t processed = 0;
    std::uint64_t single = 0;
    std::uint64_t double_gap = 0;
    std::array<int, 4> first{-1, -1, -1, -1};
    bool complete = true;
    const auto started = std::chrono::steady_clock::now();

    for (int i = 0; i < 61 && complete; ++i) {
        for (int j = i + 1; j < 62 && complete; ++j) {
            for (int k = j + 1; k < 63 && complete; ++k) {
                for (int l = k + 1; l < 64; ++l) {
                    const i64 b0 = roots[i], b1 = roots[j];
                    const i64 b2 = roots[k], b3 = roots[l];
                    std::array<i64, 5> eta{};
                    eta[0] = 1;
                    eta[1] = (prime - (b0 + b1 + b2 + b3) % prime) % prime;
                    eta[2] = (
                        b0 * b1 + b0 * b2 + b0 * b3
                        + b1 * b2 + b1 * b3 + b2 * b3
                    ) % prime;
                    eta[3] = (
                        prime - (
                            ((b0 * b1 % prime) * b2 % prime)
                            + ((b0 * b1 % prime) * b3 % prime)
                            + ((b0 * b2 % prime) * b3 % prime)
                            + ((b1 * b2 % prime) * b3 % prime)
                        ) % prime
                    ) % prime;
                    eta[4] = ((b0 * b1 % prime) * (b2 * b3 % prime)) % prime;

                    std::array<i64, 18> a{};
                    a[0] = 1;
                    for (int m = 1; m <= 17; ++m) {
                        i64 numerator = 0;
                        for (int q = 1; q <= 4 && q <= m; ++q) {
                            const i64 weight = 4LL * m - 3LL * q;
                            numerator = (
                                numerator + (weight % prime) * eta[q] % prime
                                    * a[m - q]
                            ) % prime;
                        }
                        a[m] = (prime - numerator) * inverse_denominator[m] % prime;
                    }

                    ++processed;
                    if (a[16] == 0) {
                        ++single;
                        if (a[17] == 0) {
                            ++double_gap;
                            if (first[0] < 0) first = {i, j, k, l};
                        }
                    }
                    if ((processed & 4095ULL) == 0) {
                        const double seconds = std::chrono::duration<double>(
                            std::chrono::steady_clock::now() - started
                        ).count();
                        if (seconds >= 50.0) {
                            complete = false;
                            break;
                        }
                    }
                }
            }
        }
    }

    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started
    ).count();
    std::cout << "{\"prime\":" << prime
              << ",\"zeta\":" << zeta
              << ",\"processed\":" << processed
              << ",\"complete\":" << (complete ? "true" : "false")
              << ",\"single\":" << single
              << ",\"double\":" << double_gap
              << ",\"first\":[" << first[0] << ',' << first[1] << ','
              << first[2] << ',' << first[3] << ']'
              << ",\"seconds\":" << seconds << "}\n";
    return 0;
}
"""


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def square_threshold_primes(count: int) -> list[int]:
    value = 64 * 64 + 1
    value += (1 - value) % 64
    answer: list[int] = []
    while len(answer) < count:
        if is_prime(value):
            answer.append(value)
        value += 64
    return answer


@app.function(image=image, cpu=1, memory=512, timeout=60)
def scan_prime(prime: int) -> dict[str, object]:
    source = "/tmp/order64_primary_gap.cpp"
    binary = "/tmp/order64_primary_gap"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(CPP_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=10,
    )
    completed = subprocess.run(
        [binary, str(prime)],
        check=True,
        capture_output=True,
        text=True,
        timeout=53,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    primes = [193, *square_threshold_primes(8)]
    results = list(scan_prime.map(primes, order_outputs=False))
    results.sort(key=lambda result: int(result["prime"]))

    control = next(result for result in results if int(result["prime"]) == 193)
    if not (
        bool(control["complete"])
        and int(control["processed"]) == 635_376
        and int(control["single"]) == 3_328
        and int(control["double"]) == 64
    ):
        raise RuntimeError(f"positive control mismatch: {control}")

    digest = {
        "app": "rate-half-list-order64-primary-gap",
        "order": 64,
        "threshold": "p>=64^2 and p=1 mod 64",
        "prime_count": len(primes) - 1,
        "all_complete": all(bool(result["complete"]) for result in results),
        "square_threshold_double_gap_primes": [
            int(result["prime"])
            for result in results
            if int(result["prime"]) != 193 and int(result["double"]) > 0
        ],
        "results": results,
    }
    print(json.dumps(digest, indent=2, sort_keys=True))
    print(
        "RATE_HALF_LIST_ORDER64_PRIMARY_GAP "
        f"primes={digest['prime_count']} complete={digest['all_complete']} "
        f"falsifiers={len(digest['square_threshold_double_gap_primes'])}"
    )
