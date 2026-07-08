#!/usr/bin/env python3
"""Complete n=96,h=5 anchored boundary-prime certificate."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
OUT = (
    ROOT
    / "critical/nodes/u1_x4_direct_column_budget/notes"
    / "f3_h5_n96_boundary_certificate.json"
)

CPP = r'''
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

using u128 = unsigned __int128;

static constexpr int N = 96;
static constexpr int H = 5;
static constexpr int P = 9601;
static constexpr int BITS = 32 - __builtin_clz(P - 1);

struct Record {
    u128 key;
    u128 mask;
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

static u128 mask_of(const std::vector<int>& exps) {
    u128 m = 0;
    for (int a : exps) m |= (u128(1) << a);
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

int main() {
    auto roots = domain();
    std::vector<Record> left;
    left.reserve(choose_int(95, H - 1));

    std::vector<int> tail;
    combinations(1, 95, H - 1, tail, [&](const std::vector<int>& t) {
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
    combinations(1, 95, H, right, [&](const std::vector<int>& r) {
        ++probed;
        Sig sig = signature(r, roots);
        u128 rmask = mask_of(r);
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
    if (hashed != choose_int(95, H - 1)) throw std::runtime_error("hash count mismatch");
    if (probed != choose_int(95, H)) throw std::runtime_error("probe count mismatch");

    std::cout
        << "{"
        << "\"name\":\"boundary_n96_h5_p9601_FULL_CPP\","
        << "\"n\":96,\"h\":5,\"p\":9601,\"W\":96,"
        << "\"partial\":false,\"complete\":true,"
        << "\"hashed\":" << hashed << ","
        << "\"probed\":" << probed << ","
        << "\"anchored_toral_trades\":" << toral << ","
        << "\"anchored_nontoral_trades\":" << nontoral << ","
        << "\"direct_n3_budget\":" << (96*96*96) << ","
        << "\"direct_n3_exceeded\":" << (nontoral > 96ull*96ull*96ull ? "true" : "false")
        << "}" << std::endl;
    return 0;
}
'''


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="f3_h5_n96_") as tmp:
        tmp_path = Path(tmp)
        src = tmp_path / "cert.cpp"
        exe = tmp_path / "cert"
        src.write_text(CPP)
        subprocess.run(["g++", "-O3", "-std=c++17", str(src), "-o", str(exe)], check=True)
        proc = subprocess.run([str(exe)], check=True, text=True, capture_output=True)
    row = json.loads(proc.stdout)
    expected = {
        "n": 96,
        "h": 5,
        "p": 9601,
        "W": 96,
        "hashed": 3183545,
        "probed": 57940519,
        "anchored_toral_trades": 0,
        "anchored_nontoral_trades": 0,
        "partial": False,
        "complete": True,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    OUT.write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    print(json.dumps(row, sort_keys=True))
    print("H5_N96_BOUNDARY_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()
