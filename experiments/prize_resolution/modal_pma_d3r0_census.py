#!/usr/bin/env python3
"""Exact bounded Modal census for the sigma-one PMA (d,r)=(3,0) cell."""

from __future__ import annotations

import json
import subprocess
import textwrap
from pathlib import Path

import modal


HERE = Path(__file__).resolve()
ROOT = HERE.parents[2] if len(HERE.parents) > 2 else Path("/tmp")
OUTPUT = ROOT / "experiments" / "prize_resolution" / "pma_d3r0_census_results.json"

app = modal.App("rs-mca-pma-d3r0-census")
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

int eval_poly(const std::array<int, 4>& coeff, int x, int p) {
    u64 value = 0;
    for (int j = 3; j >= 0; --j) value = (value * x + coeff[j]) % p;
    return static_cast<int>(value);
}

int locator_value(const std::array<int, 3>& roots, int x, int p) {
    u64 value = 1;
    for (int root : roots) value = value * ((x - root + p) % p) % p;
    return static_cast<int>(value);
}

struct Owner {
    std::array<int, 4> index{};
    std::array<int, 16> inverse{};
};

std::array<int, 16> inverse_vandermonde(const std::array<int, 4>& xs, int p) {
    int matrix[4][8]{};
    for (int row = 0; row < 4; ++row) {
        int power = 1;
        for (int col = 0; col < 4; ++col) {
            matrix[row][col] = power;
            power = static_cast<int>((u64)power * xs[row] % p);
        }
        matrix[row][4 + row] = 1;
    }
    for (int col = 0; col < 4; ++col) {
        int pivot = col;
        while (pivot < 4 && matrix[pivot][col] == 0) ++pivot;
        if (pivot == 4) std::exit(10);
        for (int j = 0; j < 8; ++j) std::swap(matrix[col][j], matrix[pivot][j]);
        const int inverse = mod_inv(matrix[col][col], p);
        for (int j = 0; j < 8; ++j) matrix[col][j] = static_cast<int>((u64)matrix[col][j] * inverse % p);
        for (int row = 0; row < 4; ++row) {
            if (row == col || matrix[row][col] == 0) continue;
            const int factor = matrix[row][col];
            for (int j = 0; j < 8; ++j) {
                matrix[row][j] = (matrix[row][j] - static_cast<int>((u64)factor * matrix[col][j] % p) + p) % p;
            }
        }
    }
    std::array<int, 16> output{};
    for (int row = 0; row < 4; ++row) {
        for (int col = 0; col < 4; ++col) output[4 * row + col] = matrix[row][4 + col];
    }
    return output;
}

u64 encode(const std::array<int, 4>& coeff, int p) {
    u64 code = 0;
    for (int j = 3; j >= 0; --j) code = code * p + coeff[j];
    return code;
}

std::array<int, 4> decode(u64 code, int p) {
    std::array<int, 4> coeff{};
    for (int j = 0; j < 4; ++j) {
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

int main(int argc, char** argv) {
    if (argc != 8) return 1;
    const int n = std::atoi(argv[1]);
    const int p = std::atoi(argv[2]);
    const int k = std::atoi(argv[3]);
    const int seed = std::atoi(argv[4]);
    const int pattern = std::atoi(argv[5]);
    const int layout = std::atoi(argv[6]);
    const double time_limit = std::atof(argv[7]);
    if (n > 64 || (p - 1) % n != 0 || (n - k) % 2 != 0 || k % 2 != 0) return 2;

    const int core_size = k - 1;
    const int petal_points = n - k;
    const int petals = petal_points / 2;
    const int generator = primitive_root(p);
    const int zeta = static_cast<int>(mod_pow(generator, (p - 1) / n, p));
    std::vector<int> domain(n), exponent_by_value(p, -1);
    domain[0] = 1;
    for (int i = 1; i < n; ++i) domain[i] = static_cast<int>((u64)domain[i - 1] * zeta % p);
    for (int i = 0; i < n; ++i) exponent_by_value[domain[i]] = i;

    std::mt19937 rng(seed);
    std::vector<int> core, points;
    int background = 0;
    if (layout == 0) {
        std::shuffle(domain.begin(), domain.end(), rng);
        core.assign(domain.begin(), domain.begin() + core_size);
        points.assign(domain.begin() + core_size, domain.begin() + core_size + petal_points);
        background = domain.back();
    } else {
        const int half = n / 2;
        const int split = k / 2 - 1;
        for (int i = 0; i < split; ++i) {
            core.push_back(domain[i]);
            core.push_back(domain[i + half]);
        }
        core.push_back(domain[split]);
        background = domain[split + half];
        for (int i = split + 1; i < half; ++i) {
            points.push_back(domain[i]);
            points.push_back(domain[i + half]);
        }
    }
    if (static_cast<int>(core.size()) != core_size ||
        static_cast<int>(points.size()) != petal_points) return 3;

    std::vector<int> scalars;
    if (pattern == 0) {
        for (int value = 1; value < p && static_cast<int>(scalars.size()) < petals; ++value) scalars.push_back(value);
    } else if (pattern == 1) {
        scalars.resize(p - 1);
        std::iota(scalars.begin(), scalars.end(), 1);
        std::shuffle(scalars.begin(), scalars.end(), rng);
        scalars.resize(petals);
    } else if (pattern == 2) {
        for (int i = 0; i < petals; ++i) scalars.push_back(points[2 * i]);
    } else {
        for (int i = 0; i < petals; ++i) {
            scalars.push_back(static_cast<int>((u64)points[2 * i] * points[2 * i] % p));
        }
    }

    std::vector<Owner> owners;
    for (int a = 0; a < petal_points; ++a) {
        for (int b = a + 1; b < petal_points; ++b) {
            for (int c = b + 1; c < petal_points; ++c) {
                for (int d = c + 1; d < petal_points; ++d) {
                    Owner owner;
                    owner.index = {a, b, c, d};
                    owner.inverse = inverse_vandermonde(
                        {points[a], points[b], points[c], points[d]}, p
                    );
                    owners.push_back(owner);
                }
            }
        }
    }

    const auto start = std::chrono::steady_clock::now();
    u64 processed_defects = 0, listed = 0, primitive = 0;
    u64 diffuse = 0, primitive_diffuse = 0, with_full = 0;
    u64 interpolation_candidates = 0, max_per_defect = 0, max_diffuse_per_defect = 0;
    bool timed_out = false;

    for (int a = 0; a < core_size; ++a) {
        for (int b = a + 1; b < core_size; ++b) {
            for (int c = b + 1; c < core_size; ++c) {
                if (std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count() > time_limit) {
                    timed_out = true;
                    goto finished;
                }
                const std::array<int, 3> roots{core[a], core[b], core[c]};
                std::vector<int> target(petal_points);
                for (int i = 0; i < petal_points; ++i) {
                    target[i] = static_cast<int>((u64)scalars[i / 2] * locator_value(roots, points[i], p) % p);
                }

                std::unordered_set<u64> candidates;
                candidates.reserve(owners.size() * 2);
                for (const Owner& owner : owners) {
                    std::array<int, 4> coeff{};
                    for (int row = 0; row < 4; ++row) {
                        u64 value = 0;
                        for (int col = 0; col < 4; ++col) {
                            value += static_cast<u64>(owner.inverse[4 * row + col]) * target[owner.index[col]];
                        }
                        coeff[row] = static_cast<int>(value % p);
                    }
                    candidates.insert(encode(coeff, p));
                }
                interpolation_candidates += candidates.size();

                u64 local = 0, local_diffuse = 0;
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
                    for (int root : roots) agreement_mask &= ~(u64{1} << exponent_by_value[root]);
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
                    if (agreements < 5) continue;
                    ++local;
                    ++listed;
                    const bool is_primitive = primitive_mask(agreement_mask, n);
                    if (is_primitive) ++primitive;
                    if (full_petals == 0) {
                        ++local_diffuse;
                        ++diffuse;
                        if (is_primitive) ++primitive_diffuse;
                    } else {
                        ++with_full;
                    }
                }
                max_per_defect = std::max(max_per_defect, local);
                max_diffuse_per_defect = std::max(max_diffuse_per_defect, local_diffuse);
                ++processed_defects;
            }
        }
    }

finished:
    const u64 total_defects = static_cast<u64>(core_size) * (core_size - 1) * (core_size - 2) / 6;
    const long double n6 = static_cast<long double>(n) * n * n * n * n * n;
    const long double n7 = n6 * n;
    std::cout << "{\"n\":" << n
              << ",\"p\":" << p
              << ",\"k\":" << k
              << ",\"seed\":" << seed
              << ",\"pattern\":" << pattern
              << ",\"layout\":" << layout
              << ",\"owners_per_defect\":" << owners.size()
              << ",\"processed_defects\":" << processed_defects
              << ",\"total_defects\":" << total_defects
              << ",\"interpolation_candidates\":" << interpolation_candidates
              << ",\"listed\":" << listed
              << ",\"primitive\":" << primitive
              << ",\"diffuse\":" << diffuse
              << ",\"primitive_diffuse\":" << primitive_diffuse
              << ",\"with_full\":" << with_full
              << ",\"max_per_defect\":" << max_per_defect
              << ",\"max_diffuse_per_defect\":" << max_diffuse_per_defect
              << ",\"listed_over_n6\":" << static_cast<double>(listed / n6)
              << ",\"listed_over_n7\":" << static_cast<double>(listed / n7)
              << ",\"seconds\":"
              << std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count()
              << ",\"timed_out\":" << (timed_out ? "true" : "false") << "}\n";
    return 0;
}
"""


@app.function(image=image, cpu=2, memory=1024, timeout=60)
def census(task: tuple[int, int, int, int, int, int]) -> dict[str, object]:
    n, p, k, seed, pattern, layout = task
    source = "/tmp/pma_d3r0_census.cpp"
    binary = "/tmp/pma_d3r0_census"
    with open(source, "w", encoding="ascii") as handle:
        handle.write(textwrap.dedent(CPP_SOURCE))
    subprocess.run(
        ["g++", "-O3", "-std=c++17", source, "-o", binary],
        check=True,
        timeout=12,
    )
    completed = subprocess.run(
        [binary, str(n), str(p), str(k), str(seed), str(pattern), str(layout), "46"],
        check=True,
        capture_output=True,
        text=True,
        timeout=49,
    )
    return json.loads(completed.stdout)


@app.local_entrypoint()
def main() -> None:
    tasks = [
        # General PMA pair-petal source charts.
        (32, 97, 16, 101, 0, 0),
        (32, 97, 16, 102, 1, 0),
        (32, 97, 16, 103, 2, 0),
        (40, 241, 20, 201, 1, 0),
        (48, 97, 24, 301, 0, 0),
        (48, 97, 24, 302, 1, 0),
        (48, 97, 24, 303, 2, 0),
        (56, 113, 28, 401, 1, 0),
        # Antipodal house-chart slices. Pattern 3 uses c_i=x_i^2.
        (32, 97, 16, 501, 0, 1),
        (32, 97, 16, 502, 1, 1),
        (32, 97, 16, 503, 3, 1),
        (32, 97, 8, 504, 1, 1),
        (32, 97, 8, 505, 3, 1),
        (32, 97, 4, 506, 1, 1),
        (32, 97, 4, 507, 3, 1),
        (64, 193, 32, 601, 0, 1),
        (64, 193, 32, 602, 1, 1),
        (64, 193, 32, 603, 3, 1),
        (64, 193, 16, 604, 1, 1),
        (64, 193, 16, 605, 3, 1),
        (64, 193, 8, 606, 1, 1),
        (64, 193, 8, 607, 3, 1),
    ]
    raw = list(census.map(tasks, return_exceptions=True))
    rows: list[dict[str, object]] = []
    for task, result in zip(tasks, raw):
        if isinstance(result, BaseException):
            rows.append({"task": list(task), "error": repr(result)})
        else:
            rows.append(result)
    output = {
        "schema": "pma-d3r0-exact-census-v2",
        "scope": "sigma=1, exact (d,r)=(3,0), general pair-petal sources and antipodal house-chart slices",
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
