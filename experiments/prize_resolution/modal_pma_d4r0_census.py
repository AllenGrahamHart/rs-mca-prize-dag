#!/usr/bin/env python3
"""Exact bounded Modal census for the sigma-one PMA (d,r)=(4,0) cell."""

from __future__ import annotations

import json
import subprocess
import textwrap
from pathlib import Path

import modal


HERE = Path(__file__).resolve()
ROOT = HERE.parents[2] if len(HERE.parents) > 2 else Path("/tmp")
OUTPUT = ROOT / "experiments" / "prize_resolution" / "pma_d4r0_census_results.json"

app = modal.App("rs-mca-pma-d4r0-census")
image = modal.Image.debian_slim().apt_install("g++")


CPP_SOURCE = r"""
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <random>
#include <unordered_set>
#include <vector>

using u64 = std::uint64_t;
constexpr int DEGREE = 4;
constexpr int BASIS = DEGREE + 1;
constexpr int THRESHOLD = DEGREE + 2;

u64 mod_pow(u64 base, u64 exponent, u64 modulus) {
    u64 result = 1;
    while (exponent) {
        if (exponent & 1) result = static_cast<u64>((__uint128_t)result * base % modulus);
        base = static_cast<u64>((__uint128_t)base * base % modulus);
        exponent >>= 1;
    }
    return result;
}

std::vector<int> prime_factors(int value) {
    std::vector<int> factors;
    for (int d = 2; d * d <= value; ++d) {
        if (value % d == 0) {
            factors.push_back(d);
            while (value % d == 0) value /= d;
        }
    }
    if (value > 1) factors.push_back(value);
    return factors;
}

int primitive_root(int p) {
    const auto factors = prime_factors(p - 1);
    for (int g = 2; g < p; ++g) {
        bool good = true;
        for (int factor : factors) {
            if (mod_pow(g, (p - 1) / factor, p) == 1) {
                good = false;
                break;
            }
        }
        if (good) return g;
    }
    return 0;
}

int mod_inv(int value, int p) {
    return static_cast<int>(mod_pow((value % p + p) % p, p - 2, p));
}

int eval_poly(const std::array<int, BASIS>& coeff, int x, int p) {
    u64 value = 0;
    for (int j = DEGREE; j >= 0; --j) value = (value * x + coeff[j]) % p;
    return static_cast<int>(value);
}

int locator_value(const std::array<int, DEGREE>& roots, int x, int p) {
    u64 value = 1;
    for (int root : roots) value = value * ((x - root + p) % p) % p;
    return static_cast<int>(value);
}

struct Owner {
    std::array<int, BASIS> index{};
    std::array<int, BASIS * BASIS> inverse{};
};

std::array<int, BASIS * BASIS> inverse_vandermonde(
    const std::array<int, BASIS>& xs, int p
) {
    int matrix[BASIS][2 * BASIS]{};
    for (int row = 0; row < BASIS; ++row) {
        int power = 1;
        for (int col = 0; col < BASIS; ++col) {
            matrix[row][col] = power;
            power = static_cast<int>((u64)power * xs[row] % p);
        }
        matrix[row][BASIS + row] = 1;
    }
    for (int col = 0; col < BASIS; ++col) {
        int pivot = col;
        while (pivot < BASIS && matrix[pivot][col] == 0) ++pivot;
        if (pivot == BASIS) std::exit(10);
        for (int j = 0; j < 2 * BASIS; ++j) {
            std::swap(matrix[col][j], matrix[pivot][j]);
        }
        const int inverse = mod_inv(matrix[col][col], p);
        for (int j = 0; j < 2 * BASIS; ++j) {
            matrix[col][j] = static_cast<int>((u64)matrix[col][j] * inverse % p);
        }
        for (int row = 0; row < BASIS; ++row) {
            if (row == col || matrix[row][col] == 0) continue;
            const int factor = matrix[row][col];
            for (int j = 0; j < 2 * BASIS; ++j) {
                matrix[row][j] = (
                    matrix[row][j]
                    - static_cast<int>((u64)factor * matrix[col][j] % p)
                    + p
                ) % p;
            }
        }
    }
    std::array<int, BASIS * BASIS> output{};
    for (int row = 0; row < BASIS; ++row) {
        for (int col = 0; col < BASIS; ++col) {
            output[BASIS * row + col] = matrix[row][BASIS + col];
        }
    }
    return output;
}

u64 encode(const std::array<int, BASIS>& coeff, int p) {
    u64 code = 0;
    for (int j = DEGREE; j >= 0; --j) code = code * p + coeff[j];
    return code;
}

std::array<int, BASIS> decode(u64 code, int p) {
    std::array<int, BASIS> coeff{};
    for (int j = 0; j < BASIS; ++j) {
        coeff[j] = static_cast<int>(code % p);
        code /= p;
    }
    return coeff;
}

u64 rotate_mask(u64 mask, int shift, int n) {
    shift %= n;
    if (shift == 0) return mask;
    if (n == 64) return (mask << shift) | (mask >> (64 - shift));
    const u64 fence = (u64{1} << n) - 1;
    return ((mask << shift) | (mask >> (n - shift))) & fence;
}

bool primitive_mask(u64 mask, int n) {
    for (int shift = 1; shift < n; ++shift) {
        if (rotate_mask(mask, shift, n) == mask) return false;
    }
    return true;
}

bool near_dyadic(u64 mask, int n, int k, int miss_limit) {
    for (int size = 1; size <= n; size *= 2) {
        if (n % size != 0 || size < k - miss_limit) continue;
        const int cosets = n / size;
        for (int residue = 0; residue < cosets; ++residue) {
            int hits = 0;
            for (int exponent = residue; exponent < n; exponent += cosets) {
                hits += static_cast<int>((mask >> exponent) & 1);
            }
            if (size - hits <= miss_limit) return true;
        }
    }
    return false;
}

int main(int argc, char** argv) {
    if (argc != 7) return 1;
    const int n = std::atoi(argv[1]);
    const int p = std::atoi(argv[2]);
    const int k = std::atoi(argv[3]);
    const int seed = std::atoi(argv[4]);
    const int pattern = std::atoi(argv[5]);
    const double time_limit = std::atof(argv[6]);
    if (n > 64 || (p - 1) % n != 0 || (n - k) % 2 != 0 || k < 6) return 2;

    const int core_size = k - 1;
    const int petal_points = n - k;
    const int petals = petal_points / 2;
    const int generator = primitive_root(p);
    const int zeta = static_cast<int>(mod_pow(generator, (p - 1) / n, p));
    std::vector<int> domain(n), exponent_by_value(p, -1);
    domain[0] = 1;
    for (int i = 1; i < n; ++i) {
        domain[i] = static_cast<int>((u64)domain[i - 1] * zeta % p);
    }
    for (int i = 0; i < n; ++i) exponent_by_value[domain[i]] = i;

    std::mt19937 rng(seed);
    std::shuffle(domain.begin(), domain.end(), rng);
    std::vector<int> core(domain.begin(), domain.begin() + core_size);
    std::vector<int> points(
        domain.begin() + core_size,
        domain.begin() + core_size + petal_points
    );
    const int background = domain.back();

    std::vector<int> scalars(p - 1);
    std::iota(scalars.begin(), scalars.end(), 1);
    if (pattern == 0) {
        std::shuffle(scalars.begin(), scalars.end(), rng);
    } else {
        std::sort(points.begin(), points.end());
        for (int i = 0; i < petals; ++i) {
            scalars[i] = (points[2 * i] + 3 * points[2 * i + 1]) % p;
            if (scalars[i] == 0) scalars[i] = 1;
        }
        std::unordered_set<int> seen;
        for (int i = 0; i < petals; ++i) {
            while (seen.count(scalars[i])) {
                scalars[i] = scalars[i] % (p - 1) + 1;
            }
            seen.insert(scalars[i]);
        }
    }
    scalars.resize(petals);

    std::vector<Owner> owners;
    for (int a = 0; a < petal_points; ++a)
    for (int b = a + 1; b < petal_points; ++b)
    for (int c = b + 1; c < petal_points; ++c)
    for (int d = c + 1; d < petal_points; ++d)
    for (int e = d + 1; e < petal_points; ++e) {
        Owner owner;
        owner.index = {a, b, c, d, e};
        owner.inverse = inverse_vandermonde(
            {points[a], points[b], points[c], points[d], points[e]}, p
        );
        owners.push_back(owner);
    }

    const auto start = std::chrono::steady_clock::now();
    u64 processed_defects = 0, interpolation_candidates = 0;
    u64 listed = 0, exact_six = 0, primitive = 0, primitive_exact_six = 0;
    u64 far_exact_six = 0, diffuse_exact_six = 0, far_diffuse_exact_six = 0;
    u64 max_per_defect = 0;
    bool timed_out = false;

    for (int a = 0; a < core_size; ++a)
    for (int b = a + 1; b < core_size; ++b)
    for (int c = b + 1; c < core_size; ++c)
    for (int d = c + 1; d < core_size; ++d) {
        if (std::chrono::duration<double>(
                std::chrono::steady_clock::now() - start
            ).count() > time_limit) {
            timed_out = true;
            goto finished;
        }
        const std::array<int, DEGREE> roots{core[a], core[b], core[c], core[d]};
        std::vector<int> target(petal_points);
        for (int i = 0; i < petal_points; ++i) {
            target[i] = static_cast<int>(
                (u64)scalars[i / 2] * locator_value(roots, points[i], p) % p
            );
        }

        std::unordered_set<u64> candidates;
        candidates.reserve(owners.size() * 2);
        for (const Owner& owner : owners) {
            std::array<int, BASIS> coeff{};
            for (int row = 0; row < BASIS; ++row) {
                u64 value = 0;
                for (int col = 0; col < BASIS; ++col) {
                    value += static_cast<u64>(
                        owner.inverse[BASIS * row + col]
                    ) * target[owner.index[col]];
                }
                coeff[row] = static_cast<int>(value % p);
            }
            candidates.insert(encode(coeff, p));
        }
        interpolation_candidates += candidates.size();

        u64 local = 0;
        for (u64 code : candidates) {
            const auto coeff = decode(code, p);
            if (eval_poly(coeff, background, p) == 0) continue;
            bool exact_defect = true;
            for (int root : roots) {
                if (eval_poly(coeff, root, p) == 0) exact_defect = false;
            }
            if (!exact_defect) continue;

            int agreements = 0, full_petals = 0;
            u64 agreement_mask = 0;
            for (int x : core) agreement_mask |= u64{1} << exponent_by_value[x];
            for (int root : roots) {
                agreement_mask &= ~(u64{1} << exponent_by_value[root]);
            }
            for (int i = 0; i < petals; ++i) {
                int in_petal = 0;
                for (int side = 0; side < 2; ++side) {
                    const int index = 2 * i + side;
                    if (eval_poly(coeff, points[index], p) == target[index]) {
                        ++agreements;
                        ++in_petal;
                        agreement_mask |= u64{1} << exponent_by_value[points[index]];
                    }
                }
                if (in_petal == 2) ++full_petals;
            }
            if (agreements < THRESHOLD) continue;
            ++local;
            ++listed;
            const bool is_primitive = primitive_mask(agreement_mask, n);
            if (is_primitive) ++primitive;
            if (agreements == THRESHOLD) {
                ++exact_six;
                if (is_primitive) ++primitive_exact_six;
                const bool far = !near_dyadic(agreement_mask, n, k, DEGREE);
                if (far) ++far_exact_six;
                if (full_petals == 0) {
                    ++diffuse_exact_six;
                    if (far) ++far_diffuse_exact_six;
                }
            }
        }
        max_per_defect = std::max(max_per_defect, local);
        ++processed_defects;
    }

finished:
    const u64 total_defects = static_cast<u64>(core_size) * (core_size - 1)
        * (core_size - 2) * (core_size - 3) / 24;
    const long double n6 = static_cast<long double>(n) * n * n * n * n * n;
    const long double n9 = n6 * n * n * n;
    std::cout << "{\"n\":" << n
              << ",\"p\":" << p
              << ",\"k\":" << k
              << ",\"seed\":" << seed
              << ",\"pattern\":" << pattern
              << ",\"owners_per_defect\":" << owners.size()
              << ",\"processed_defects\":" << processed_defects
              << ",\"total_defects\":" << total_defects
              << ",\"interpolation_candidates\":" << interpolation_candidates
              << ",\"listed\":" << listed
              << ",\"exact_six\":" << exact_six
              << ",\"primitive\":" << primitive
              << ",\"primitive_exact_six\":" << primitive_exact_six
              << ",\"far_exact_six\":" << far_exact_six
              << ",\"diffuse_exact_six\":" << diffuse_exact_six
              << ",\"far_diffuse_exact_six\":" << far_diffuse_exact_six
              << ",\"max_per_defect\":" << max_per_defect
              << ",\"exact_six_over_n6\":" << static_cast<double>(exact_six / n6)
              << ",\"exact_six_over_n9\":" << static_cast<double>(exact_six / n9)
              << ",\"seconds\":" << std::chrono::duration<double>(
                    std::chrono::steady_clock::now() - start
                 ).count()
              << ",\"timed_out\":" << (timed_out ? "true" : "false")
              << "}\n";
    return 0;
}
"""


@app.function(image=image, cpu=2, memory=1024, timeout=90)
def census(task: tuple[int, int, int, int, int]) -> dict[str, object]:
    n, p, k, seed, pattern = task
    source = "/tmp/pma_d4r0_census.cpp"
    binary = "/tmp/pma_d4r0_census"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(CPP_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=15,
    )
    completed = subprocess.run(
        [binary, str(n), str(p), str(k), str(seed), str(pattern), "70"],
        check=True,
        capture_output=True,
        text=True,
        timeout=76,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    tasks = [
        (16, 17, 8, seed, pattern)
        for seed in (101, 211, 307)
        for pattern in (0, 1)
    ]
    tasks += [
        (24, 97, 12, seed, 0) for seed in (101, 211, 307)
    ]
    tasks += [
        (32, p, 16, seed, 0)
        for p in (97, 193)
        for seed in (101, 211, 307)
    ]
    tasks += [
        (36, 109, 18, seed, 0) for seed in (101, 211, 307)
    ]
    results = list(census.map(tasks, return_exceptions=True))
    normalized: list[dict[str, object]] = []
    for task, result in zip(tasks, results):
        if isinstance(result, BaseException):
            normalized.append({"task": task, "error": repr(result)})
        else:
            normalized.append(result)
    payload = {"schema": "pma-d4r0-census-v1", "results": normalized}
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
