#!/usr/bin/env python3
"""Independent sorted-pair audit of representative weight-six rows."""

from __future__ import annotations

import json
import math
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_admissible_mitm_result.json"
PAIR_COUNT = 129_540
TRIPLE_COUNT = 21_849_080

AUDIT_CPP = r'''
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;
struct Entry { u64 sum; std::uint32_t pair; };
static u64 p;

static u64 mul(u64 a, u64 b) { return static_cast<u64>((u128)a*b % p); }
static u64 power(u64 a, u64 e) {
    u64 z=1;
    while (e) { if (e&1) z=mul(z,a); a=mul(a,a); e>>=1; }
    return z;
}
static bool ok(int a, int b) { return a!=b && ((a-b+512)%512)!=256; }

int main(int argc, char** argv) {
    if (argc!=2) return 2;
    p=std::stoull(argv[1]);
    u64 seed=2;
    while (power(seed,(p-1)/2)==1) ++seed;
    u64 omega=power(seed,(p-1)/512);
    if (power(omega,512)!=1 || power(omega,256)!=p-1) return 3;
    std::vector<u64> root(512,1);
    for (int i=1;i<512;++i) root[i]=mul(root[i-1],omega);

    std::vector<Entry> pairs;
    pairs.reserve(129540);
    for (int a=1;a<512;++a) if (a!=256)
      for (int b=a+1;b<512;++b) if (b!=256 && ok(a,b))
        pairs.push_back({(root[a]+root[b])%p, static_cast<std::uint32_t>(a|(b<<9))});
    std::sort(pairs.begin(),pairs.end(),[](const Entry& x,const Entry& y){
        return x.sum<y.sum || (x.sum==y.sum && x.pair<y.pair);
    });

    std::uint64_t triples=0;
    for (int c=1;c<512;++c) if (c!=256)
      for (int d=c+1;d<512;++d) if (d!=256 && ok(c,d))
        for (int e=d+1;e<512;++e) if (e!=256 && ok(c,e) && ok(d,e)) {
          ++triples;
          u64 sum=((root[c]+root[d])%p+root[e])%p;
          u64 target=(2*p-1-sum)%p;
          auto lo=std::lower_bound(pairs.begin(),pairs.end(),target,
            [](const Entry& x,u64 value){ return x.sum<value; });
          auto hi=std::upper_bound(lo,pairs.end(),target,
            [](u64 value,const Entry& x){ return value<x.sum; });
          for (auto it=lo;it!=hi;++it) {
            int a=it->pair&511, b=it->pair>>9;
            if (ok(a,c)&&ok(a,d)&&ok(a,e)&&ok(b,c)&&ok(b,d)&&ok(b,e)) {
              std::cout << "FOUND " << pairs.size() << ' ' << triples << '\n';
              return 0;
            }
          }
        }
    std::cout << "EXHAUSTED " << pairs.size() << ' ' << triples << ' '
              << seed << ' ' << omega << '\n';
    return 0;
}
'''


def main() -> None:
    data = json.loads(RESULT.read_text())
    rows = data.get("rows")
    if (
        data.get("status") != "COMPLETE"
        or data.get("relation_count") != 0
        or not isinstance(rows, list)
        or len(rows) != 64
        or PAIR_COUNT != math.comb(510, 2) - 255
        or TRIPLE_COUNT != math.comb(510, 3) - 255 * 508
    ):
        raise AssertionError("artifact or combinatorial ledger")

    for row in rows:
        p = row["p"]
        if (
            row["status"] != "EXHAUSTED"
            or row["pair_count"] != PAIR_COUNT
            or row["triples_scanned"] != TRIPLE_COUNT
            or pow(row["omega"], 512, p) != 1
            or pow(row["omega"], 256, p) != p - 1
        ):
            raise AssertionError("banked row")

    with tempfile.TemporaryDirectory() as directory:
        directory = Path(directory)
        source = directory / "audit.cpp"
        binary = directory / "audit"
        source.write_text(AUDIT_CPP)
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(binary)],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        for index in (0, len(rows) // 2, len(rows) - 1):
            row = rows[index]
            process = subprocess.run(
                [str(binary), str(row["p"])],
                check=True,
                capture_output=True,
                text=True,
                timeout=15,
            )
            fields = process.stdout.split()
            if fields != [
                "EXHAUSTED",
                str(PAIR_COUNT),
                str(TRIPLE_COUNT),
                str(row["seed"]),
                str(row["omega"]),
            ]:
                raise AssertionError(f"independent replay row {index}: {fields}")

    print(
        "DLI_WCL_ELL1_WEIGHT6_FIRST64_AUDIT_PASS "
        f"rows_checked=64 independent_replays=3 pairs={PAIR_COUNT} triples={TRIPLE_COUNT}"
    )


if __name__ == "__main__":
    main()
