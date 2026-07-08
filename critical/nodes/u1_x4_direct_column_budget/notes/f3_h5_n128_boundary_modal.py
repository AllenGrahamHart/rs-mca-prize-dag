#!/usr/bin/env python3
"""Modal-sharded n=128,h=5 boundary-prime anchored certificate.

Mode is selected by F3_H5_N128_MODE:

  gate  - run the heaviest shard only and write a gate JSON
  full  - run all shards and write the complete certificate JSON
  extra - run all shards for two extra nearby primes and write a list JSON
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

import modal


app = modal.App("rs-mca-f3-h5-n128-boundary")
image = modal.Image.debian_slim()

N = 128
H = 5
P = 17921
SHARDS = 32
EXTRA_PRIMES = (18049, 18433)

# Modal imports this file at /root inside the remote container.  Output paths
# are used only by the local entrypoint, so keep them anchored to the worktree.
ROOT = Path(os.environ.get(
    "F3_PRIZE_ROOT",
    "/home/u2470931/smooth-read-solomin/prize-codex-overnight-20260708",
))
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
OUT = NOTES / "f3_h5_n128_boundary_certificate.json"
GATE_OUT = NOTES / "f3_h5_n128_boundary_gate.json"
EXTRA_OUT = NOTES / "f3_h5_n128_extra_primes_certificate.json"

CPP = r'''
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

using u128 = unsigned __int128;

static constexpr int N = 128;
static constexpr int H = 5;
static constexpr int P = 17921;
static constexpr int SHARDS = 32;
static constexpr int SHARD = 0;
static constexpr int BITS = 32 - __builtin_clz(P - 1);

struct Record {
    u128 key;
    u128 lo;
    u128 hi;
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

static void mask_of(const std::vector<int>& exps, u128& lo, u128& hi) {
    lo = 0;
    hi = 0;
    for (int a : exps) {
        if (a < 64) lo |= (u128(1) << a);
        else hi |= (u128(1) << (a - 64));
    }
}

static bool intersects(const Record& rec, u128 lo, u128 hi) {
    return bool((rec.lo & lo) | (rec.hi & hi));
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
    left.reserve(choose_int(127, H - 1));

    std::vector<int> tail;
    combinations(1, 127, H - 1, tail, [&](const std::vector<int>& t) {
        std::vector<int> exps;
        exps.reserve(H);
        exps.push_back(0);
        for (int a : t) exps.push_back(a);
        Sig sig = signature(exps, roots);
        u128 lo, hi;
        mask_of(exps, lo, hi);
        left.push_back(Record{sig.key, lo, hi, sig.last, is_toral(exps)});
    });

    std::sort(left.begin(), left.end(), [](const Record& a, const Record& b) {
        return a.key < b.key;
    });

    uint64_t probed = 0;
    uint64_t toral = 0;
    uint64_t nontoral = 0;
    std::vector<int> right;
    combinations(1, 127, H, right, [&](const std::vector<int>& r) {
        if (r[0] % SHARDS != SHARD) return;
        ++probed;
        Sig sig = signature(r, roots);
        u128 lo_mask, hi_mask;
        mask_of(r, lo_mask, hi_mask);
        bool rtoral = is_toral(r);
        auto lo = std::lower_bound(left.begin(), left.end(), sig.key, [](const Record& rec, u128 key) {
            return rec.key < key;
        });
        auto hi = std::upper_bound(left.begin(), left.end(), sig.key, [](u128 key, const Record& rec) {
            return key < rec.key;
        });
        for (auto it = lo; it != hi; ++it) {
            if (it->last == sig.last) continue;
            if (intersects(*it, lo_mask, hi_mask)) continue;
            if (it->toral && rtoral) ++toral;
            else ++nontoral;
        }
    });

    uint64_t hashed = left.size();
    if (hashed != choose_int(127, H - 1)) throw std::runtime_error("hash count mismatch");

    std::cout
        << "{"
        << "\"n\":128,\"h\":5,\"p\":" << P << ",\"W\":128,"
        << "\"shards\":32,\"shard\":" << SHARD << ","
        << "\"partial\":true,\"complete\":false,"
        << "\"hashed\":" << hashed << ","
        << "\"probed\":" << probed << ","
        << "\"anchored_toral_trades\":" << toral << ","
        << "\"anchored_nontoral_trades\":" << nontoral << ","
        << "\"direct_n3_budget\":" << (128*128*128) << ","
        << "\"direct_n3_exceeded\":" << (nontoral > 128ull*128ull*128ull ? "true" : "false")
        << "}" << std::endl;
    return 0;
}
'''


def expected_probe_count(shard: int) -> int:
    return sum(
        math.comb(N - 1 - first, H - 1)
        for first in range(1, N - H + 2)
        if first % SHARDS == shard
    )


@app.function(image=image, cpu=4, memory=4096, timeout=60)
def shard_certificate(job) -> dict:
    import json
    import subprocess
    import tempfile
    import time
    from pathlib import Path

    if isinstance(job, int):
        p, shard = 17921, job
    else:
        p, shard = job

    with tempfile.TemporaryDirectory(prefix="f3_h5_n128_") as tmp:
        tmp_path = Path(tmp)
        src = tmp_path / "cert.cpp"
        exe = tmp_path / "cert"
        src.write_text(
            CPP
            .replace("static constexpr int P = 17921;", f"static constexpr int P = {p};")
            .replace("static constexpr int SHARD = 0;", f"static constexpr int SHARD = {shard};")
        )
        t0 = time.monotonic()
        subprocess.run(["g++", "-O3", "-std=c++17", str(src), "-o", str(exe)], check=True)
        proc = subprocess.run([str(exe)], check=True, text=True, capture_output=True)
        elapsed = time.monotonic() - t0
    row = json.loads(proc.stdout)
    row["elapsed_sec"] = round(elapsed, 3)
    return row


def aggregate(rows: list[dict], complete: bool, p: int = P) -> dict:
    rows = sorted(rows, key=lambda row: row["shard"])
    shards_seen = [row["shard"] for row in rows]
    if len(set(shards_seen)) != len(shards_seen):
        raise AssertionError(shards_seen)
    if complete and shards_seen != list(range(SHARDS)):
        raise AssertionError([row["shard"] for row in rows])
    for row in rows:
        expected = {
            "n": N,
            "h": H,
            "p": p,
            "W": N,
            "shards": SHARDS,
            "hashed": math.comb(N - 1, H - 1),
            "probed": expected_probe_count(row["shard"]),
            "partial": True,
            "complete": False,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((key, row.get(key), value, row))
    out = {
        "name": f"boundary_n128_h5_p{p}_SHARDED_CPP",
        "n": N,
        "h": H,
        "p": p,
        "W": N,
        "shards": SHARDS,
        "shards_completed": len(rows),
        "partial": not complete,
        "complete": complete,
        "hashed_per_shard": math.comb(N - 1, H - 1),
        "probed": sum(row["probed"] for row in rows),
        "anchored_toral_trades": sum(row["anchored_toral_trades"] for row in rows),
        "anchored_nontoral_trades": sum(row["anchored_nontoral_trades"] for row in rows),
        "direct_n3_budget": N**3,
        "direct_n3_exceeded": any(row["direct_n3_exceeded"] for row in rows),
        "max_elapsed_sec": max(row["elapsed_sec"] for row in rows),
        "rows": rows,
    }
    if complete:
        expected = {
            "probed": math.comb(N - 1, H),
            "anchored_toral_trades": 0,
            "anchored_nontoral_trades": 0,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if out.get(key) != value:
                raise AssertionError((key, out.get(key), value, out))
    return out


@app.local_entrypoint()
def main():
    mode = os.environ.get("F3_H5_N128_MODE", "gate")
    if mode not in {"gate", "full", "extra"}:
        raise ValueError("F3_H5_N128_MODE must be gate, full, or extra")

    if mode == "gate":
        counts = [(expected_probe_count(shard), shard) for shard in range(SHARDS)]
        shard = max(counts)[1]
        rows = [shard_certificate.remote((P, shard))]
        out = aggregate(rows, complete=False)
        GATE_OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        print(json.dumps(out, sort_keys=True))
        print("H5_N128_BOUNDARY_GATE_PASS")
        return

    if mode == "full":
        rows = [
            row for row in shard_certificate.map(
                [(P, shard) for shard in range(SHARDS)], return_exceptions=True
            )
            if isinstance(row, dict)
        ]
        out = aggregate(rows, complete=(len(rows) == SHARDS))
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        print(json.dumps({k: v for k, v in out.items() if k != "rows"}, sort_keys=True))
        if len(rows) != SHARDS:
            raise AssertionError(f"completed {len(rows)}/{SHARDS} shards")
        print("H5_N128_BOUNDARY_CERTIFICATE_PASS")
        return

    results = []
    for p in EXTRA_PRIMES:
        rows = [
            row for row in shard_certificate.map(
                [(p, shard) for shard in range(SHARDS)], return_exceptions=True
            )
            if isinstance(row, dict)
        ]
        out = aggregate(rows, complete=(len(rows) == SHARDS), p=p)
        if len(rows) != SHARDS:
            raise AssertionError(f"p={p} completed {len(rows)}/{SHARDS} shards")
        results.append(out)
        print(json.dumps({k: v for k, v in out.items() if k != "rows"}, sort_keys=True))
    EXTRA_OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print("H5_N128_EXTRA_PRIMES_CERTIFICATE_PASS")
