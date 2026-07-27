#!/usr/bin/env python3
"""Independent FLINT replay of the N=512 trinomial norm certificate."""

from __future__ import annotations

import modal


app = modal.App("e1-n512-trinomial-flint-replay")
image = modal.Image.debian_slim().pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=1024, timeout=60)
def replay() -> dict[str, object]:
    import hashlib
    import json
    from collections import Counter, defaultdict
    from itertools import combinations, product

    from flint import fmpz_poly

    order = 512
    half = order // 2
    prize_budget = 317494674775468773183020924238786383963
    intervals = (
        (1 << 250, (1 << 250) + (1 << 128) - 1),
        (prize_budget << 128, ((prize_budget + 1) << 128) - 1),
    )

    def canonical_pair(left, right, left_sign, right_sign):
        if left > right:
            return right, left, right_sign, left_sign
        return left, right, left_sign, right_sign

    def conjugate(state, unit):
        terms = []
        for exponent, sign in zip(state[:2], state[2:]):
            residue = unit * exponent % order
            if residue >= half:
                residue -= half
                sign = -sign
            assert 0 < residue < half
            assert sign in (-1, 1)
            terms.append((residue, sign))
        terms.sort()
        assert terms[0][0] < terms[1][0]
        return terms[0][0], terms[1][0], terms[0][1], terms[1][1]

    universe = {
        canonical_pair(left, right, left_sign, right_sign)
        for left, right in combinations(range(1, half), 2)
        for left_sign, right_sign in product((-1, 1), repeat=2)
    }
    states = set(universe)
    seen = set()
    representatives = []
    orbit_sizes = []
    units = tuple(range(1, order, 2))
    while states:
        representative = min(states)
        orbit = {conjugate(representative, unit) for unit in units}
        assert orbit <= universe
        assert not orbit & seen
        representatives.append(representative)
        orbit_sizes.append(len(orbit))
        seen.update(orbit)
        states.difference_update(orbit)
    assert seen == universe
    assert sum(orbit_sizes) == 129540

    def variance(state):
        left, right, left_sign, right_sign = state
        support = (0, left, right)
        values = (2, left_sign, right_sign)
        coefficients = [0] * half
        for source, source_value in zip(support, values):
            for target, target_value in zip(support, values):
                quotient, residue = divmod(source - target, half)
                coefficients[residue] += (
                    -1 if quotient % 2 else 1
                ) * source_value * target_value
        coefficients[0] -= 6
        return sum(value * value for value in coefficients)

    cyclotomic = fmpz_poly([1] + [0] * (half - 1) + [1])
    rows = []
    norm_groups = defaultdict(list)
    variance_histogram = Counter()
    for state in representatives:
        left, right, left_sign, right_sign = state
        coefficients = [0] * (right + 1)
        coefficients[0] = 2
        coefficients[left] += left_sign
        coefficients[right] += right_sign
        norm = abs(int(cyclotomic.resultant(fmpz_poly(coefficients))))
        assert norm > 0
        row = {
            "state": state,
            "variance": variance(state),
            "norm": norm,
            "bits": norm.bit_length(),
        }
        rows.append(row)
        norm_groups[norm].append(state)
        variance_histogram[row["variance"]] += 1

    canonical_rows = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    rows_sha256 = hashlib.sha256(canonical_rows).hexdigest()
    assert rows_sha256 == "83b6b8c7bc1686177e7abd68c0328769a6360d3d0e12f6e3524ec8df32403ea7"

    window_integers = 0
    max_window_width = 0
    divisible_records = []
    for norm, norm_states in norm_groups.items():
        for interval_index, (lower, upper) in enumerate(intervals):
            cofactor_low = (norm + upper - 1) // upper
            cofactor_high = norm // lower
            width = max(0, cofactor_high - cofactor_low + 1)
            max_window_width = max(max_window_width, width)
            window_integers += width
            for cofactor in range(cofactor_low, cofactor_high + 1):
                if cofactor == 0 or norm % cofactor:
                    continue
                quotient = norm // cofactor
                assert quotient % order == 0
                divisible_records.append(
                    {
                        "interval": interval_index,
                        "state": norm_states[0],
                        "norm": norm,
                        "cofactor": cofactor,
                        "quotient": quotient,
                        "quotient_is_prime": False,
                        "quotient_mod_512": quotient % order,
                    }
                )

    interval_payload = {
        "norms_screened": len(norm_groups),
        "intervals_per_norm": len(intervals),
        "window_integers": window_integers,
        "max_window_width": max_window_width,
        "divisible_records": divisible_records,
        "candidate_primes": [],
    }
    digest_payload = json.dumps(
        interval_payload, sort_keys=True, separators=(",", ":")
    ).encode()
    interval_sha256 = hashlib.sha256(digest_payload).hexdigest()
    assert interval_sha256 == "31354966797534d609acd86bcf57bb7315a310152016a27e40d0ea989a67d523"
    assert len(representatives) == 748
    assert len(norm_groups) == 746
    assert window_integers == 4
    assert max_window_width == 1
    assert len(divisible_records) == 1
    assert dict(sorted(variance_histogram.items())) == {
        0: 1,
        2: 7,
        10: 18,
        16: 6,
        18: 703,
        26: 6,
        32: 1,
        34: 6,
    }
    return {
        "rows_sha256": rows_sha256,
        "interval_sha256": interval_sha256,
        "orbits": len(representatives),
        "distinct_norms": len(norm_groups),
        "window_integers": window_integers,
        "candidate_primes": 0,
    }


@app.local_entrypoint()
def main() -> None:
    result = replay.remote()
    print("E1_N512_TRINOMIAL_FLINT_REPLAY_PASS " + repr(result))
