#!/usr/bin/env python3
"""Seeded exact sweep of aligned positive (1,1,2) q-slice candidates.

This is adversarial evidence, not a deletion theorem.  It imports the exact
prime-field reconstruction used by the original single-fixture probe and
tests every admissible internal pair on twenty fixtures at each of five
split primes.
"""

import importlib.util
import random
from collections import Counter
from itertools import combinations, combinations_with_replacement
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROBE_PATH = HERE / "kb_c2_112_qslice_probe.py"
PRIMES = (1009, 1013, 1019, 1021, 1031)
SEED = 11220260729
FIXTURES_PER_PRIME = 20


def load_probe():
    spec = importlib.util.spec_from_file_location("kb_c2_112_qslice_probe", PROBE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load q-slice probe")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    probe = load_probe()
    rng = random.Random(SEED)
    totals = Counter()
    witnesses = []

    for prime in PRIMES:
        probe.P = prime
        local = Counter()
        fixtures = 0
        while fixtures < FIXTURES_PER_PRIME:
            a, b, c, d, w = [rng.randrange(2, prime - 1) for _ in range(5)]
            labels = [a, probe.inv(a), b, probe.inv(b)]
            base = labels + [c, probe.inv(c), d, probe.inv(d), w, probe.inv(w)]
            if len(set(base)) != 10 or any(value in (1, prime - 1) for value in base):
                continue
            fixtures += 1
            q_roots = (c, d)
            q = [c * d % prime, -(c + d) % prime, 1]
            tau = {0: 1, 1: 0, 2: 3, 3: 2}
            edges = list(combinations(range(4), 2))
            edge_index = {edge: index for index, edge in enumerate(edges)}
            tau_edge = {
                index: edge_index[tuple(sorted((tau[left], tau[right])))]
                for index, (left, right) in enumerate(edges)
            }

            for first_index, second_index in combinations_with_replacement(range(6), 2):
                packet = Counter((first_index, second_index,
                                  tau_edge[first_index], tau_edge[second_index]))
                if probe.collision(packet) > 1:
                    continue
                local["assignments"] += 1
                first, second = edges[first_index], edges[second_index]
                common = next(iter(set(first) & set(second)))
                endpoint = labels[common]
                q0, q1, q2 = q
                f = (q0 - w * q2) % prime
                g = (q2 - w * q0) % prime
                m = q1 * (1 - w) % prime
                numerator = (f + m * endpoint + g * endpoint * endpoint) % prime
                denominator = (g + m * endpoint + f * endpoint * endpoint) % prime
                if not denominator:
                    local["singular"] += 1
                    continue
                z = -numerator * probe.inv(denominator) % prime
                endpoint_labels = set(base + ([z, probe.inv(z)] if z else []))
                if not z or len(endpoint_labels) != 12 or z in (1, prime - 1):
                    local["invalid"] += 1
                    continue
                candidate = probe.reconstruct(1, w, z, q, first, second, labels)
                if candidate is None:
                    local["inconsistent"] += 1
                    continue
                local["reconstructed"] += 1
                if probe.qslice_passes(*candidate, z, w, q_roots):
                    local["survivors"] += 1
                    witnesses.append((prime, a, b, c, d, w,
                                      first_index, second_index, z))

        print(f"prime={prime} fixtures={fixtures} counts={dict(local)}")
        totals.update(local)

    if totals != Counter(assignments=1200, reconstructed=1188, invalid=12):
        raise RuntimeError(f"sweep ledger changed: {dict(totals)}")
    if witnesses:
        raise RuntimeError(f"positive q-slice survivor: {witnesses[0]}")
    print(
        "KB_C2_112_POSITIVE_QSLICE_SWEEP_PASS "
        "primes=5 fixtures=100 assignments=1200 reconstructed=1188 "
        "invalid=12 survivors=0"
    )


if __name__ == "__main__":
    main()
