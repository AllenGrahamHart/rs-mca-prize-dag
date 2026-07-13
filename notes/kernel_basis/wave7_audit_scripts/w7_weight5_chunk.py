#!/usr/bin/env python3
"""w7 audit: replay a chunk [start,end) of the 64 weight-5 MITM searches
against the pinned C++ (SHA-checked), comparing full JSON rows."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

TREE = Path("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/w7_tree")
SRC = TREE / "experiments/prize_resolution/dli_wcl_terminal_weight5_mitm.cpp"
RESULT = TREE / "experiments/prize_resolution/dli_wcl_terminal_weight5_mitm_result.json"
BIN = Path("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/w7_weight5_bin")
SHA = "dd61eb4c0f57334a4a03974b85a91e2447bbad042d0bb47adb4d03df86d76c5c"
PAIR_COUNT = 130560
TRIPLE_COUNT = 22108160

start, end = int(sys.argv[1]), int(sys.argv[2])
assert hashlib.sha256(SRC.read_bytes()).hexdigest() == SHA, "source hash"
if not BIN.exists():
    subprocess.run(["g++", "-O3", "-std=c++17", str(SRC), "-o", str(BIN)],
                   check=True, capture_output=True, text=True, timeout=60)

data = json.loads(RESULT.read_text())
prime_rows = sorted(data["primes"], key=lambda r: int(r["k"]))
assert len(prime_rows) == 64
for row in prime_rows[start:end]:
    proc = subprocess.run([str(BIN), str(row["q"]), str(row["generator"])],
                          check=True, capture_output=True, text=True, timeout=15)
    res = json.loads(proc.stdout)
    assert res["q"] == row["q"] and res["generator"] == row["generator"]
    assert res["pair_count"] == PAIR_COUNT, res
    assert res["triples_checked"] == TRIPLE_COUNT, res
    assert res["found"] is False and res["relation"] == [], res
print(f"W7_WEIGHT5_CHUNK_PASS rows[{start}:{end}] pair={PAIR_COUNT} triples={TRIPLE_COUNT} found=0")
