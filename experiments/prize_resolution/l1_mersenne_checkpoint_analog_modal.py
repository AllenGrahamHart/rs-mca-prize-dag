#!/usr/bin/env python3
"""Exact small analogue for the Mersenne first-checkpoint frontier.

This exhausts all 7-subsets of the order-32 subgroup in GF(7^4). Two
subsets belong to one split pencil exactly when their monic locators have
the same six nonconstant, nonleading coefficients. Distinct members of one
such group are automatically disjoint because their locators differ by a
nonzero constant.

The row is the first genuine analogue of n=m(p+1), namely (n,p,m)=(32,7,4).
It is route evidence only: it is not an official prize row and proves no
uniform statement. The worker stops enumeration after 40 seconds and sorts
whatever prefix was completed, so a timeout still yields marked partial
statistics. Resources: two CPUs, 1 GiB, one container, 60 seconds.
"""

from __future__ import annotations

import subprocess
import tempfile

import modal


app = modal.App("l1-mersenne-checkpoint-analog")
image = modal.Image.debian_slim(python_version="3.12").apt_install("g++")


CPP_SOURCE = r'''
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

using u16 = std::uint16_t;
using u32 = std::uint32_t;

constexpr int P = 7;
constexpr int FIELD = 2401;
constexpr int N = 32;
constexpr std::uint64_t TOTAL = 3365856;
constexpr double WALL_SECONDS = 40.0;

static std::array<int, 4> digits(int a) {
    std::array<int, 4> out{};
    for (int i = 0; i < 4; ++i) {
        out[i] = a % P;
        a /= P;
    }
    return out;
}

static int encode(const std::array<int, 4>& a) {
    int out = 0;
    for (int i = 3; i >= 0; --i) out = out * P + a[i];
    return out;
}

// Polynomial basis GF(7)[x]/(x^4+x+1); the modulus is irreducible.
static int add_raw(int a, int b) {
    auto x = digits(a), y = digits(b);
    for (int i = 0; i < 4; ++i) x[i] = (x[i] + y[i]) % P;
    return encode(x);
}

static int neg_raw(int a) {
    auto x = digits(a);
    for (int i = 0; i < 4; ++i) x[i] = (P - x[i]) % P;
    return encode(x);
}

static int mul_raw(int a, int b) {
    auto x = digits(a), y = digits(b);
    std::array<int, 7> c{};
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            c[i + j] = (c[i + j] + x[i] * y[j]) % P;
    // x^4=-x-1.
    for (int d = 6; d >= 4; --d) {
        int v = c[d] % P;
        c[d] = 0;
        c[d - 3] = (c[d - 3] - v + P) % P;
        c[d - 4] = (c[d - 4] - v + P) % P;
    }
    std::array<int, 4> out{c[0], c[1], c[2], c[3]};
    return encode(out);
}

static int pow_raw(int a, int e) {
    int out = 1;
    while (e) {
        if (e & 1) out = mul_raw(out, a);
        a = mul_raw(a, a);
        e >>= 1;
    }
    return out;
}

struct Record {
    std::array<u16, 6> sig{};
    u32 mask = 0;
};

static bool operator<(const Record& a, const Record& b) {
    if (a.sig != b.sig) return a.sig < b.sig;
    return a.mask < b.mask;
}

int main() {
    std::vector<u16> add(FIELD * FIELD), mul(FIELD * FIELD), neg(FIELD);
    for (int a = 0; a < FIELD; ++a) {
        neg[a] = static_cast<u16>(neg_raw(a));
        for (int b = 0; b < FIELD; ++b) {
            add[a * FIELD + b] = static_cast<u16>(add_raw(a, b));
            mul[a * FIELD + b] = static_cast<u16>(mul_raw(a, b));
        }
    }
    auto plus = [&](int a, int b) { return int(add[a * FIELD + b]); };
    auto times = [&](int a, int b) { return int(mul[a * FIELD + b]); };
    auto minus = [&](int a, int b) { return plus(a, neg[b]); };

    int primitive = 0;
    for (int g = 2; g < FIELD; ++g) {
        if (pow_raw(g, 2400 / 2) != 1 &&
            pow_raw(g, 2400 / 3) != 1 &&
            pow_raw(g, 2400 / 5) != 1) {
            primitive = g;
            break;
        }
    }
    if (!primitive) throw std::runtime_error("no primitive element");
    int zeta = pow_raw(primitive, 2400 / N);
    if (pow_raw(zeta, N) != 1 || pow_raw(zeta, N / 2) == 1)
        throw std::runtime_error("bad order-32 generator");

    std::array<int, N> roots{};
    roots[0] = 1;
    for (int i = 1; i < N; ++i) roots[i] = times(roots[i - 1], zeta);

    std::vector<Record> records;
    records.reserve(TOTAL);
    std::array<int, 7> c{0, 1, 2, 3, 4, 5, 6};
    const auto start = std::chrono::steady_clock::now();
    bool complete = true;

    while (true) {
        std::array<int, 8> poly{};
        poly[0] = 1;
        int degree = 0;
        u32 mask = 0;
        for (int index : c) {
            int root = roots[index];
            mask |= u32(1) << index;
            std::array<int, 8> next{};
            for (int j = 0; j <= degree; ++j) {
                next[j] = minus(next[j], times(root, poly[j]));
                next[j + 1] = plus(next[j + 1], poly[j]);
            }
            poly = next;
            ++degree;
        }
        Record record;
        for (int j = 1; j <= 6; ++j) record.sig[j - 1] = u16(poly[j]);
        record.mask = mask;
        records.push_back(record);

        if ((records.size() & 65535) == 0) {
            double elapsed = std::chrono::duration<double>(
                std::chrono::steady_clock::now() - start).count();
            if (elapsed >= WALL_SECONDS) {
                complete = false;
                break;
            }
        }

        int i = 6;
        while (i >= 0 && c[i] == N - 7 + i) --i;
        if (i < 0) break;
        ++c[i];
        for (int j = i + 1; j < 7; ++j) c[j] = c[j - 1] + 1;
    }

    std::sort(records.begin(), records.end());
    std::array<std::uint64_t, 9> histogram{};
    std::uint64_t pencil_groups = 0;
    std::uint64_t embedded_m2_groups = 0;
    int max_h = 0;
    int max_depth_at_max = -1;
    std::vector<u32> witnesses;

    for (std::size_t i = 0; i < records.size();) {
        std::size_t j = i + 1;
        while (j < records.size() && records[j].sig == records[i].sig) ++j;
        int h = int(j - i);
        if (h >= int(histogram.size())) histogram.back()++;
        else histogram[h]++;
        if (h >= 2) ++pencil_groups;
        if (h == 2) {
            u32 joined = records[i].mask | records[i + 1].mask;
            for (int parity = 0; parity < 2; ++parity) {
                u32 coset = 0;
                for (int bit = parity; bit < N; bit += 2) coset |= u32(1) << bit;
                if ((joined & ~coset) == 0) {
                    u32 missing = coset ^ joined;
                    if (__builtin_popcount(missing) == 2) {
                        int first = __builtin_ctz(missing);
                        if (missing & (u32(1) << ((first + N / 2) % N)))
                            ++embedded_m2_groups;
                    }
                }
            }
        }
        if (h > max_h) {
            max_h = h;
            witnesses.clear();
            for (std::size_t k = i; k < j; ++k) witnesses.push_back(records[k].mask);
            int r = 0;
            for (int degree = 6; degree >= 1; --degree) {
                if (records[i].sig[degree - 1] != 0) {
                    r = degree;
                    break;
                }
            }
            max_depth_at_max = 2 * P - r - 1;
        }
        for (std::size_t a = i; a < j; ++a)
            for (std::size_t b = a + 1; b < j; ++b)
                if (records[a].mask & records[b].mask)
                    throw std::runtime_error("same-prefix locators overlap");
        i = j;
    }

    std::cout << (complete ? "COMPLETE" : "INCOMPLETE")
              << " records=" << records.size() << "/" << TOTAL
              << " primitive=" << primitive << " zeta=" << zeta << "\n";
    std::cout << "groups_ge_2=" << pencil_groups << " max_h=" << max_h
              << " max_depth_at_max=" << max_depth_at_max
              << " embedded_m2_h2=" << embedded_m2_groups << "\n";
    std::cout << "group_size_histogram";
    for (int h = 1; h < int(histogram.size()); ++h)
        if (histogram[h]) std::cout << " " << h << ":" << histogram[h];
    if (histogram.back()) std::cout << " >=8:" << histogram.back();
    std::cout << "\nmax_group_masks";
    for (u32 mask : witnesses) std::cout << " 0x" << std::hex << mask << std::dec;
    std::cout << "\n";
    return complete ? 0 : 3;
}
'''


@app.function(image=image, cpu=2.0, memory=1024, timeout=60)
def run() -> dict[str, object]:
    with tempfile.TemporaryDirectory() as tmp:
        source = f"{tmp}/worker.cpp"
        binary = f"{tmp}/worker"
        with open(source, "w", encoding="ascii") as handle:
            handle.write(CPP_SOURCE)
        build = subprocess.run(
            ["g++", "-O3", "-std=c++17", source, "-o", binary],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if build.returncode:
            return {"exit": build.returncode, "stdout": "", "stderr": build.stderr}
        worker = subprocess.run(
            [binary], capture_output=True, text=True, timeout=50
        )
        return {
            "exit": worker.returncode,
            "stdout": worker.stdout,
            "stderr": worker.stderr,
        }


@app.local_entrypoint()
def main() -> None:
    result = run.remote()
    print(result["stdout"], end="")
    if result["stderr"]:
        print("--- stderr ---")
        print(result["stderr"], end="")
    print(f"MODAL_EXIT={result['exit']}")
    raise SystemExit(int(result["exit"]))
