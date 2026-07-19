#!/usr/bin/env python3
"""Bounded dyadic order-128 search for simultaneous two-window gaps."""

from __future__ import annotations

import json
import subprocess
import textwrap

import modal


app = modal.App("rate-half-list-order128-two-window")
image = modal.Image.debian_slim(python_version="3.12").apt_install("g++")


CPP_SOURCE = r"""
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

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

static i64 exact_order_root(int order, i64 prime) {
    for (i64 candidate = 2; candidate < prime; ++candidate) {
        i64 root = mod_pow(candidate, (prime - 1) / order, prime);
        if (root != 1 && mod_pow(root, order / 2, prime) != 1) return root;
    }
    return 0;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int order = std::atoi(argv[1]);
    const i64 prime = std::strtoll(argv[2], nullptr, 10);
    const int h = order / 8 + 1;
    const int primary_first = 2 * h - 2;
    const int contact = 2 * h;
    const int final_index = 3 * h - 1;
    const i64 zeta = exact_order_root(order, prime);
    if (zeta == 0) return 3;

    std::vector<i64> roots(order, 1);
    for (int exponent = 1; exponent < order; ++exponent) {
        roots[exponent] = roots[exponent - 1] * zeta % prime;
    }
    std::vector<i64> inverse_denominator(final_index + 1, 0);
    for (int m = 1; m <= final_index; ++m) {
        inverse_denominator[m] = mod_pow(4LL * m % prime, prime - 2, prime);
    }
    const i64 inverse_two = mod_pow(2, prime - 2, prime);

    std::uint64_t processed = 0;
    std::uint64_t primary = 0;
    std::uint64_t simultaneous = 0;
    std::array<int, 4> first_primary{-1, -1, -1, -1};
    std::array<int, 4> first_simultaneous{-1, -1, -1, -1};
    std::array<i64, 2> first_terminal{-1, -1};
    bool complete = true;
    const auto started = std::chrono::steady_clock::now();

    for (int i = 0; i < order - 3 && complete; ++i) {
        for (int j = i + 1; j < order - 2 && complete; ++j) {
            for (int k = j + 1; k < order - 1 && complete; ++k) {
                for (int l = k + 1; l < order; ++l) {
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

                    std::vector<i64> a(final_index + 1, 0);
                    a[0] = 1;
                    auto extend = [&](int first, int last) {
                        for (int m = first; m <= last; ++m) {
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
                    };
                    extend(1, contact);

                    ++processed;
                    if (a[primary_first] == 0 && a[primary_first + 1] == 0
                            && a[contact] != 0) {
                        ++primary;
                        if (first_primary[0] < 0) first_primary = {i, j, k, l};
                        extend(contact + 1, final_index);

                        std::vector<i64> square(h, 0);
                        const i64 inverse_contact = mod_pow(a[contact], prime - 2, prime);
                        for (int left = 0; left < h; ++left) {
                            for (int right = 0; right + left < h; ++right) {
                                square[left + right] = (
                                    square[left + right]
                                    + a[left] * a[contact + right]
                                ) % prime;
                            }
                        }
                        for (i64& value : square) value = value * inverse_contact % prime;

                        std::vector<i64> root(h, 0);
                        root[0] = 1;
                        for (int degree = 1; degree < h; ++degree) {
                            i64 cross = 0;
                            for (int q = 1; q < degree; ++q) {
                                cross = (cross + root[q] * root[degree - q]) % prime;
                            }
                            root[degree] = (square[degree] - cross + prime) % prime;
                            root[degree] = root[degree] * inverse_two % prime;
                        }
                        if (first_terminal[0] < 0) {
                            first_terminal = {root[h - 2], root[h - 1]};
                        }
                        if (root[h - 2] == 0 && root[h - 1] == 0) {
                            ++simultaneous;
                            if (first_simultaneous[0] < 0) {
                                first_simultaneous = {i, j, k, l};
                            }
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
    std::cout << "{\"order\":" << order
              << ",\"prime\":" << prime
              << ",\"zeta\":" << zeta
              << ",\"processed\":" << processed
              << ",\"complete\":" << (complete ? "true" : "false")
              << ",\"primary\":" << primary
              << ",\"simultaneous\":" << simultaneous
              << ",\"first_primary\":[" << first_primary[0] << ','
              << first_primary[1] << ',' << first_primary[2] << ','
              << first_primary[3] << ']'
              << ",\"first_simultaneous\":[" << first_simultaneous[0] << ','
              << first_simultaneous[1] << ',' << first_simultaneous[2] << ','
              << first_simultaneous[3] << ']'
              << ",\"first_terminal\":[" << first_terminal[0] << ','
              << first_terminal[1] << ']'
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


def split_primes(order: int, count: int) -> list[int]:
    value = order + 1
    value += (1 - value) % order
    answer: list[int] = []
    while len(answer) < count:
        if is_prime(value):
            answer.append(value)
        value += order
    return answer


@app.function(image=image, cpu=1, memory=512, timeout=60)
def scan_task(task: tuple[int, int]) -> dict[str, object]:
    order, prime = task
    source = "/tmp/order128_two_window.cpp"
    binary = "/tmp/order128_two_window"
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
        timeout=53,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    tasks = [(64, 193), *((128, prime) for prime in split_primes(128, 8))]
    results = list(scan_task.map(tasks, order_outputs=False))
    results.sort(key=lambda result: (int(result["order"]), int(result["prime"])))
    control = next(result for result in results if int(result["order"]) == 64)
    if not (
        bool(control["complete"])
        and int(control["processed"]) == 635_376
        and int(control["primary"]) == 64
        and int(control["simultaneous"]) == 0
        and control["first_primary"] == [0, 1, 3, 62]
        and control["first_terminal"] == [102, 24]
    ):
        raise RuntimeError(f"positive control mismatch: {control}")

    target = [result for result in results if int(result["order"]) == 128]
    digest = {
        "app": "rate-half-list-order128-two-window",
        "target_order": 128,
        "prime_count": len(target),
        "all_complete": all(bool(result["complete"]) for result in results),
        "primary_primes": [
            int(result["prime"]) for result in target if int(result["primary"]) > 0
        ],
        "simultaneous_primes": [
            int(result["prime"])
            for result in target
            if int(result["simultaneous"]) > 0
        ],
        "results": results,
    }
    print(json.dumps(digest, indent=2, sort_keys=True))
    print(
        "RATE_HALF_LIST_ORDER128_TWO_WINDOW "
        f"primes={len(target)} complete={digest['all_complete']} "
        f"primary_fields={len(digest['primary_primes'])} "
        f"simultaneous_fields={len(digest['simultaneous_primes'])}"
    )
