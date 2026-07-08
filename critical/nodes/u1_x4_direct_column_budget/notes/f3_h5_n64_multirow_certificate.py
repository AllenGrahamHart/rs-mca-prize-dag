#!/usr/bin/env python3
"""Complete n=64,h=5 anchored probes at p>=n^2 primes.

The default prime list is intentionally small enough for local compiled replay.
Pass explicit primes on the command line to run a timing gate or a narrower
audit, e.g.:

    python3 f3_h5_n64_multirow_certificate.py 4289
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
OUT = (
    ROOT
    / "critical/nodes/u1_x4_direct_column_budget/notes"
    / "f3_h5_n64_multirow_certificate.json"
)

PRIMES = (
    4289,
    4481,
    4673,
    4801,
    4993,
    5441,
    5569,
    5953,
    6337,
    6529,
    6977,
    12289,
    40961,
    65537,
    262337,
)

CPP = r'''
#include <algorithm>
#include <array>
#include <cstdlib>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

using u128 = unsigned __int128;

static constexpr int N = 64;
static constexpr int H = 5;
static int P = 4289;
static int BITS = 0;

struct Record {
    u128 key;
    uint64_t mask;
    uint32_t last;
    bool toral;
};

static uint64_t mod_pow(uint64_t a, uint64_t e) {
    uint64_t r = 1;
    while (e) {
        if (e & 1) r = (r * a) % P;
        a = (a * a) % P;
        e >>= 1;
    }
    return r;
}

static int order_mod(int x) {
    int y = x;
    int order = 1;
    while (y != 1) {
        y = int((uint64_t)y * x % P);
        ++order;
        if (order > N) break;
    }
    return order;
}

static std::array<int, N> domain() {
    for (int c = 2; c < P; ++c) {
        int z = int(mod_pow(c, (P - 1) / N));
        if (z != 1 && order_mod(z) == N) {
            std::array<int, N> out{};
            out[0] = 1;
            for (int i = 1; i < N; ++i) out[i] = int((uint64_t)out[i - 1] * z % P);
            return out;
        }
    }
    throw std::runtime_error("no generator");
}

struct Sig {
    u128 key;
    uint32_t last;
};

static Sig signature(const std::vector<int>& exps, const std::array<int, N>& roots) {
    int e[H + 1] = {0};
    e[0] = 1;
    int deg = 0;
    for (int a : exps) {
        int r = roots[a];
        ++deg;
        for (int j = deg; j >= 1; --j) {
            e[j] = (e[j] + int((uint64_t)r * e[j - 1] % P)) % P;
        }
    }
    u128 key = 0;
    for (int j = 1; j < H; ++j) {
        key = (key << BITS) | u128(e[j]);
    }
    return Sig{key, uint32_t(e[H])};
}

static uint64_t mask_of(const std::vector<int>& exps) {
    uint64_t m = 0;
    for (int a : exps) m |= (uint64_t(1) << a);
    return m;
}

static bool is_toral(const std::vector<int>& exps) {
    if (N % H) return false;
    int step = N / H;
    int residue = exps[0] % step;
    bool seen[H] = {false};
    for (int a : exps) {
        if (a % step != residue) return false;
        int idx = (a - residue) / step;
        if (idx < 0 || idx >= H || seen[idx]) return false;
        seen[idx] = true;
    }
    return true;
}

template <class Fn>
static void combinations(int start, int end, int need, std::vector<int>& cur, Fn&& fn) {
    if (need == 0) {
        fn(cur);
        return;
    }
    for (int x = start; x <= end - need + 1; ++x) {
        cur.push_back(x);
        combinations(x + 1, end, need - 1, cur, fn);
        cur.pop_back();
    }
}

static uint64_t choose_int(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    uint64_t r = 1;
    for (int i = 1; i <= k; ++i) {
        r = r * uint64_t(n - k + i) / uint64_t(i);
    }
    return r;
}

int main(int argc, char** argv) {
    if (argc == 2) P = std::atoi(argv[1]);
    if (P <= 1) throw std::runtime_error("bad prime argument");
    BITS = 32 - __builtin_clz(unsigned(P - 1));

    auto roots = domain();
    std::vector<Record> left;
    left.reserve(choose_int(63, H - 1));

    std::vector<int> tail;
    combinations(1, 63, H - 1, tail, [&](const std::vector<int>& t) {
        std::vector<int> exps;
        exps.reserve(H);
        exps.push_back(0);
        for (int a : t) exps.push_back(a);
        Sig sig = signature(exps, roots);
        left.push_back(Record{sig.key, mask_of(exps), sig.last, is_toral(exps)});
    });

    std::sort(left.begin(), left.end(), [](const Record& a, const Record& b) {
        return a.key < b.key;
    });

    uint64_t probed = 0;
    uint64_t toral = 0;
    uint64_t nontoral = 0;
    std::vector<int> right;
    combinations(1, 63, H, right, [&](const std::vector<int>& r) {
        ++probed;
        Sig sig = signature(r, roots);
        uint64_t rmask = mask_of(r);
        bool rtoral = is_toral(r);
        auto lo = std::lower_bound(left.begin(), left.end(), sig.key, [](const Record& rec, u128 key) {
            return rec.key < key;
        });
        auto hi = std::upper_bound(left.begin(), left.end(), sig.key, [](u128 key, const Record& rec) {
            return key < rec.key;
        });
        for (auto it = lo; it != hi; ++it) {
            if (it->last == sig.last) continue;
            if (it->mask & rmask) continue;
            if (it->toral && rtoral) ++toral;
            else ++nontoral;
        }
    });

    uint64_t hashed = left.size();
    if (hashed != choose_int(63, H - 1)) throw std::runtime_error("hash count mismatch");
    if (probed != choose_int(63, H)) throw std::runtime_error("probe count mismatch");

    std::cout
        << "{"
        << "\"name\":\"boundary_n64_h5_p" << P << "_FULL_CPP\","
        << "\"n\":64,\"h\":5,\"p\":" << P << ",\"W\":64,"
        << "\"partial\":false,\"complete\":true,"
        << "\"hashed\":" << hashed << ","
        << "\"probed\":" << probed << ","
        << "\"anchored_toral_trades\":" << toral << ","
        << "\"anchored_nontoral_trades\":" << nontoral << ","
        << "\"direct_n3_budget\":" << (64*64*64) << ","
        << "\"direct_n3_exceeded\":" << (nontoral > 64ull*64ull*64ull ? "true" : "false")
        << "}" << std::endl;
    return 0;
}
'''


def compile_certificate(tmp_path: Path) -> Path:
    src = tmp_path / "cert.cpp"
    exe = tmp_path / "cert"
    src.write_text(CPP)
    subprocess.run(["g++", "-O3", "-std=c++17", str(src), "-o", str(exe)], check=True)
    return exe


def run_certificate(exe: Path, p: int) -> dict:
    proc = subprocess.run([str(exe), str(p)], check=True, text=True, capture_output=True)
    return json.loads(proc.stdout)


def certify_primes(primes: tuple[int, ...]) -> list[dict]:
    rows = []
    with tempfile.TemporaryDirectory(prefix="f3_h5_n64_") as tmp:
        exe = compile_certificate(Path(tmp))
        for p in primes:
            row = run_certificate(exe, p)
            expected = {
                "n": 64,
                "h": 5,
                "p": p,
                "W": 64,
                "hashed": 595665,
                "probed": 7028847,
                "anchored_toral_trades": 0,
                "partial": False,
                "complete": True,
                "direct_n3_exceeded": False,
            }
            for key, value in expected.items():
                if row.get(key) != value:
                    raise AssertionError((p, key, row.get(key), value, row))
            rows.append(row)
    return rows


def main() -> None:
    primes = tuple(int(arg) for arg in sys.argv[1:]) or PRIMES
    rows = certify_primes(primes)

    if not sys.argv[1:]:
        OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    for row in rows:
        print(json.dumps(row, sort_keys=True))
    print("H5_N64_MULTIROW_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()
