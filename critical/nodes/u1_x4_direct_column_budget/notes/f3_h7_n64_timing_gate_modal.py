#!/usr/bin/env python3
"""Modal timing gate / rank-sharded certificate for n=64,h=7.

Default mode runs one guarded worker.  Set F3_H7_N64_MODE=full to run the
16-shard rank-balanced certificate.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


app = modal.App("rs-mca-f3-h7-n64-timing-gate")
image = modal.Image.debian_slim()

ROOT = Path(os.environ.get(
    "F3_PRIZE_ROOT",
    "/home/u2470931/smooth-read-solomin/prize-codex-overnight-20260708",
))
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
OUT = NOTES / "f3_h7_n64_timing_gate.json"
CERT_OUT = NOTES / "f3_h7_n64_boundary_certificate.json"

CPP = r'''
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

using u128 = unsigned __int128;
using Clock = std::chrono::steady_clock;

static constexpr int N = 64;
static constexpr int H = 7;
static constexpr int P = 4289;
static constexpr int RIGHT_SHARDS = 16;
static constexpr int RIGHT_SHARD = 0;
static constexpr int BITS = 32 - __builtin_clz(P - 1);

struct Record {
    u128 key;
    uint64_t mask;
    uint32_t last;
    bool toral;
};

static double elapsed(Clock::time_point t0) {
    return std::chrono::duration<double>(Clock::now() - t0).count();
}

static uint64_t mod_pow(uint64_t a, uint64_t e) {
    uint64_t r = 1;
    while (e) {
        if (e & 1) r = (r * a) % P;
        a = (a * a) % P;
        e >>= 1;
    }
    return r;
}

static int order_mod(int a) {
    int x = 1;
    for (int k = 1; k <= N; ++k) {
        x = int((uint64_t)x * a % P);
        if (x == 1) return k;
    }
    return 0;
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
    for (int j = 1; j < H; ++j) key = (key << BITS) | u128(e[j]);
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
static bool combinations(int start, int end, int need, std::vector<int>& cur, Fn&& fn) {
    if (need == 0) return fn(cur);
    for (int x = start; x <= end - need + 1; ++x) {
        cur.push_back(x);
        if (!combinations(x + 1, end, need - 1, cur, fn)) return false;
        cur.pop_back();
    }
    return true;
}

static uint64_t choose_int(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    uint64_t r = 1;
    for (int i = 1; i <= k; ++i) r = r * uint64_t(n - k + i) / uint64_t(i);
    return r;
}

static void print_json(const char* phase, uint64_t left_count, uint64_t probed,
                       uint64_t toral, uint64_t nontoral, double t0,
                       double build_sec, double sort_sec, bool complete) {
    std::cout
        << "{"
        << "\"name\":\"boundary_n64_h7_p4289_RANK_SHARDED_CPP\","
        << "\"n\":64,\"h\":7,\"p\":4289,\"W\":64,"
        << "\"phase\":\"" << phase << "\","
        << "\"complete\":" << (complete ? "true" : "false") << ","
        << "\"partial\":" << (complete ? "false" : "true") << ","
        << "\"left_records_target\":" << choose_int(63, H - 1) << ","
        << "\"right_probes_target\":" << choose_int(63, H) << ","
        << "\"left_records_built\":" << left_count << ","
        << "\"right_shards\":16,\"right_shard\":" << RIGHT_SHARD << ","
        << "\"probed\":" << probed << ","
        << "\"anchored_toral_trades\":" << toral << ","
        << "\"anchored_nontoral_trades\":" << nontoral << ","
        << "\"direct_n3_budget\":" << (64*64*64) << ","
        << "\"direct_n3_exceeded\":" << (nontoral > 64ull*64ull*64ull ? "true" : "false") << ","
        << "\"build_sec\":" << build_sec << ","
        << "\"sort_sec\":" << sort_sec << ","
        << "\"elapsed_sec\":" << t0
        << "}" << std::endl;
}

int main() {
    auto t0 = Clock::now();
    auto roots = domain();
    std::vector<Record> left;
    left.reserve(choose_int(63, H - 1));

    uint64_t built = 0;
    std::vector<int> tail;
    bool left_complete = combinations(1, 63, H - 1, tail, [&](const std::vector<int>& t) {
        std::vector<int> exps;
        exps.reserve(H);
        exps.push_back(0);
        for (int a : t) exps.push_back(a);
        Sig sig = signature(exps, roots);
        left.push_back(Record{sig.key, mask_of(exps), sig.last, is_toral(exps)});
        ++built;
        if ((built & ((1ull << 20) - 1)) == 0 && elapsed(t0) > 36.0) return false;
        return true;
    });
    double build_sec = elapsed(t0);
    if (!left_complete) {
        print_json("left_build_guard", built, 0, 0, 0, elapsed(t0), build_sec, 0.0, false);
        return 0;
    }
    if (build_sec > 42.0) {
        print_json("left_built_no_sort_guard", built, 0, 0, 0, elapsed(t0), build_sec, 0.0, false);
        return 0;
    }

    auto sort_start = Clock::now();
    std::sort(left.begin(), left.end(), [](const Record& a, const Record& b) {
        return a.key < b.key;
    });
    double sort_sec = elapsed(sort_start);
    if (elapsed(t0) > 52.0) {
        print_json("sorted_no_probe_guard", built, 0, 0, 0, elapsed(t0), build_sec, sort_sec, false);
        return 0;
    }

    uint64_t probed = 0;
    uint64_t right_index = 0;
    uint64_t toral = 0;
    uint64_t nontoral = 0;
    std::vector<int> right;
    bool right_complete = combinations(1, 63, H, right, [&](const std::vector<int>& r) {
        uint64_t idx = right_index++;
        if (idx % RIGHT_SHARDS != RIGHT_SHARD) return true;
        ++probed;
        Sig sig = signature(r, roots);
        uint64_t rmask = mask_of(r);
        bool rtoral = is_toral(r);
        Record probe{sig.key, 0, 0, false};
        auto range = std::equal_range(left.begin(), left.end(), probe,
            [](const Record& a, const Record& b) { return a.key < b.key; });
        for (auto it = range.first; it != range.second; ++it) {
            if (it->last == sig.last) continue;
            if (it->mask & rmask) continue;
            if (it->toral && rtoral) ++toral;
            else ++nontoral;
        }
        if ((probed & ((1ull << 18) - 1)) == 0 && elapsed(t0) > 56.0) return false;
        return true;
    });
    print_json(right_complete ? "complete_one_right_shard" : "probe_guard",
               built, probed, toral, nontoral, elapsed(t0), build_sec, sort_sec,
               right_complete);
    return 0;
}
'''


@app.function(image=image, cpu=4, memory=8192, timeout=60)
def timing_gate(shard: int = 0) -> dict:
    import json
    import subprocess
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory(prefix="f3_h7_n64_gate_") as tmp:
        tmp_path = Path(tmp)
        src = tmp_path / "gate.cpp"
        exe = tmp_path / "gate"
        src.write_text(
            CPP.replace(
                "static constexpr int RIGHT_SHARD = 0;",
                f"static constexpr int RIGHT_SHARD = {shard};",
            )
        )
        subprocess.run(["g++", "-O3", "-std=c++17", str(src), "-o", str(exe)], check=True)
        proc = subprocess.run([str(exe)], check=True, text=True, capture_output=True)
    return json.loads(proc.stdout)


@app.local_entrypoint()
def main():
    mode = os.environ.get("F3_H7_N64_MODE", "gate")
    if mode not in {"gate", "full"}:
        raise ValueError("F3_H7_N64_MODE must be gate or full")
    if mode == "gate":
        row = timing_gate.remote(0)
        OUT.write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
        print(json.dumps(row, sort_keys=True))
        print("H7_N64_TIMING_GATE_DONE")
        return

    rows = [row for row in timing_gate.map(range(16), return_exceptions=True) if isinstance(row, dict)]
    rows = sorted(rows, key=lambda row: row["right_shard"])
    if [row["right_shard"] for row in rows] != list(range(16)):
        raise AssertionError(rows)
    if not all(row.get("complete") for row in rows):
        raise AssertionError(rows)
    aggregate = {
        "name": "boundary_n64_h7_p4289_RANK_SHARDED_CPP",
        "n": 64,
        "h": 7,
        "p": 4289,
        "W": 64,
        "shards": 16,
        "shards_completed": len(rows),
        "left_records_per_shard": rows[0]["left_records_built"],
        "probed": sum(row["probed"] for row in rows),
        "anchored_toral_trades": sum(row["anchored_toral_trades"] for row in rows),
        "anchored_nontoral_trades": sum(row["anchored_nontoral_trades"] for row in rows),
        "direct_n3_budget": 64**3,
        "direct_n3_exceeded": any(row["direct_n3_exceeded"] for row in rows),
        "partial": False,
        "complete": True,
        "max_elapsed_sec": max(row["elapsed_sec"] for row in rows),
        "rows": rows,
    }
    expected = {
        "left_records_per_shard": 67945521,
        "probed": 553270671,
        "anchored_toral_trades": 0,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if aggregate.get(key) != value:
            raise AssertionError((key, aggregate.get(key), value, aggregate))
    CERT_OUT.write_text(json.dumps(aggregate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in aggregate.items() if k != "rows"}, sort_keys=True))
    print("H7_N64_BOUNDARY_CERTIFICATE_PASS")
