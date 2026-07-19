#!/usr/bin/env python3
"""Compile all terminal weight-five affine-Galois classes on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


ORDER = 512
HALF = 256
WEIGHT = 5
SHARDS = 128
EXPECTED_WEIGHT4 = 24_979
EXPECTED_WEIGHT5 = 2_296_920
WEIGHT4_RESULT = Path(__file__).with_name("dli_wcl_weight4_section_result.json.gz")
SHARD_ROOT = "/classes/shards"
REPRESENTATIVE_FILE = "/classes/weight5_affine_representatives.bin"
METADATA_FILE = "/classes/weight5_affine_representatives.json"

app = modal.App("rs-mca-dli-wcl-weight5-affine-representatives")
volume = modal.Volume.from_name(
    "rs-mca-dli-wcl-weight5-affine-classes-v1", create_if_missing=True
)
image = modal.Image.debian_slim().add_local_file(
    str(WEIGHT4_RESULT), "/input/weight4.json.gz", copy=True
)


@app.function(
    image=image,
    cpu=2,
    memory=2048,
    timeout=600,
    max_containers=128,
    volumes={"/classes": volume},
)
def enumerate_shard(shard: int) -> dict[str, object]:
    import gzip
    import json
    import struct
    import time

    if not 0 <= shard < SHARDS:
        raise AssertionError("shard")
    started = time.monotonic()
    with gzip.open("/input/weight4.json.gz", "rt", encoding="utf-8") as handle:
        source = json.load(handle)
    representatives = source["representatives"]
    if source.get("class_count") != EXPECTED_WEIGHT4 or len(representatives) != EXPECTED_WEIGHT4:
        raise AssertionError("weight-four source")
    start = shard * len(representatives) // SHARDS
    end = (shard + 1) * len(representatives) // SHARDS

    def valuation_two(value: int) -> int:
        return (value & -value).bit_length() - 1

    def encode(full_terms: tuple[int, ...]) -> int:
        reduced = sorted(
            (term % HALF, 1 if term < HALF else -1) for term in full_terms
        )
        if len(reduced) != WEIGHT or len({row[0] for row in reduced}) != WEIGHT:
            raise AssertionError("antipodal collision")
        if reduced[0][1] < 0:
            reduced = [(exponent, -sign) for exponent, sign in reduced]
        key = 0
        for index, (exponent, sign) in enumerate(reduced):
            key |= (exponent | ((sign < 0) << 8)) << (9 * index)
        return key

    def canonical_key(full: tuple[int, ...]) -> int:
        best = None
        for left in full:
            for right in full:
                if left == right:
                    continue
                difference = (right - left) % ORDER
                v2 = valuation_two(difference)
                if v2 >= 8:
                    raise AssertionError("antipodal input")
                modulus = 1 << (9 - v2)
                base = pow(difference >> v2, -1, modulus)
                for lift in range(1 << v2):
                    dilation = base + lift * modulus
                    shift = -dilation * left
                    image = tuple(
                        (dilation * term + shift) % ORDER for term in full
                    )
                    key = encode(image)
                    if best is None or key < best:
                        best = key
        if best is None:
            raise AssertionError("empty orbit")
        return best

    keys = set()
    legal_extensions = 0
    for representative in representatives[start:end]:
        full4 = tuple(
            int(exponent) + (HALF if int(sign) < 0 else 0)
            for exponent, sign in zip(
                representative["exponents"], representative["signs"]
            )
        )
        if len(full4) != 4:
            raise AssertionError("weight-four representative")
        forbidden = set(full4) | {(term + HALF) % ORDER for term in full4}
        for term in range(ORDER):
            if term in forbidden:
                continue
            legal_extensions += 1
            keys.add(canonical_key((*full4, term)))

    rows = sorted(keys)
    path = f"{SHARD_ROOT}/shard_{shard:03d}.bin"
    Path(SHARD_ROOT).mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as handle:
        for key in rows:
            handle.write(struct.pack("<Q", key))
    volume.commit()
    return {
        "shard": shard,
        "weight4_start": start,
        "weight4_end": end,
        "weight4_rows": end - start,
        "legal_extensions": legal_extensions,
        "shard_unique_keys": len(rows),
        "seconds": round(time.monotonic() - started, 6),
        "status": "COMPLETE",
    }


@app.function(
    image=image,
    cpu=2,
    memory=2048,
    timeout=600,
    volumes={"/classes": volume},
)
def merge_shards(summaries: list[dict[str, object]]) -> dict[str, object]:
    import hashlib
    import heapq
    import json
    import struct
    import time

    started = time.monotonic()
    volume.reload()
    if (
        len(summaries) != SHARDS
        or sorted(int(row["shard"]) for row in summaries) != list(range(SHARDS))
        or any(row["status"] != "COMPLETE" for row in summaries)
        or sum(int(row["weight4_rows"]) for row in summaries) != EXPECTED_WEIGHT4
    ):
        raise AssertionError("shard summaries")

    handles = []

    def rows(handle):
        while True:
            payload = handle.read(8)
            if not payload:
                return
            if len(payload) != 8:
                raise AssertionError("truncated shard")
            yield struct.unpack("<Q", payload)[0]

    try:
        iterators = []
        for shard in range(SHARDS):
            handle = open(f"{SHARD_ROOT}/shard_{shard:03d}.bin", "rb")
            handles.append(handle)
            iterators.append(rows(handle))
        merged = heapq.merge(*iterators)
        digest = hashlib.sha256()
        binary_digest = hashlib.sha256()
        count = 0
        previous = None
        with open(REPRESENTATIVE_FILE, "wb") as output:
            for key in merged:
                if key == previous:
                    continue
                payload = struct.pack("<Q", key)
                output.write(payload)
                binary_digest.update(payload)
                digest.update(f"{key}\n".encode())
                previous = key
                count += 1
    finally:
        for handle in handles:
            handle.close()
    if count != EXPECTED_WEIGHT5:
        raise AssertionError(("weight-five class count", count))

    metadata = {
        "schema": "dli-wcl-weight5-affine-representatives-v1",
        "status": "COMPLETE",
        "order": ORDER,
        "weight": WEIGHT,
        "source_weight4_classes": EXPECTED_WEIGHT4,
        "shards": SHARDS,
        "legal_extensions": sum(int(row["legal_extensions"]) for row in summaries),
        "sum_shard_unique_keys": sum(
            int(row["shard_unique_keys"]) for row in summaries
        ),
        "class_count": count,
        "representative_digest": digest.hexdigest(),
        "binary_sha256": binary_digest.hexdigest(),
        "max_shard_seconds": max(float(row["seconds"]) for row in summaries),
        "merge_seconds": round(time.monotonic() - started, 6),
        "shard_summaries": sorted(summaries, key=lambda row: int(row["shard"])),
    }
    Path(METADATA_FILE).write_text(json.dumps(metadata, sort_keys=True) + "\n")
    volume.commit()
    return metadata


@app.local_entrypoint()
def main() -> None:
    remote_rows = list(enumerate_shard.map(range(SHARDS), return_exceptions=True))
    errors = [repr(row) for row in remote_rows if isinstance(row, BaseException)]
    if errors:
        raise AssertionError(errors)
    result = merge_shards.remote(remote_rows)
    print(
        "DLI_WCL_WEIGHT5_AFFINE_REPRESENTATIVES "
        + json.dumps(
            {
                "classes": result["class_count"],
                "legal_extensions": result["legal_extensions"],
                "sum_shard_unique_keys": result["sum_shard_unique_keys"],
                "max_shard_seconds": result["max_shard_seconds"],
                "merge_seconds": result["merge_seconds"],
                "digest": result["representative_digest"],
            },
            sort_keys=True,
        )
    )
