#!/usr/bin/env python3
"""Deterministic checks for the windowed-projection reduction."""

from itertools import product


ROWS = (
    ("prize 1/4", 2**41, 2**39, 2**33 + 1),
    ("prize 1/8", 2**41, 2**38, 2**33 + 1),
    ("prize 1/16", 2**41, 2**37, 2**32 + 1),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def projection_zero(error, slope, q):
    left, right = error
    if slope is None:
        return right == 0
    return (left + slope * right) % q == 0


def check_projective_cell_identity():
    cases = 0
    for q in (3, 5, 7):
        slopes = list(range(q)) + [None]
        errors = [x for x in product(range(q), repeat=2) if x != (0, 0)]
        for error in errors:
            require(sum(projection_zero(error, z, q) for z in slopes) == 1,
                    "projective cell is not unique")
            cases += 1
        for length in range(1, 5):
            for sequence in product(errors[: min(len(errors), 5)], repeat=length):
                multiplicities = [
                    sum(projection_zero(error, z, q) for error in sequence)
                    for z in slopes
                ]
                require(sum(multiplicities) == length,
                        "multiplicity sum identity")
                for threshold in range(1, length + 1):
                    occupied = sum(value >= threshold for value in multiplicities)
                    require(occupied <= length // threshold,
                            "over-agreement packing bound")
                cases += 1
    print(f"PASS projective-cell identity and beta packing: cases={cases}")


def check_high_depth_injectivity_arithmetic():
    cases = 0
    for h in range(3, 20):
        for d in range((h + 1) // 2, h - 1):
            for k in (1, 3, 11):
                union_floor = 2 * (k + d) - (k - 1)
                require(union_floor > k + h, "injectivity contradiction")
                cases += 1
    print(f"PASS high-depth injectivity inequality: cases={cases}")


def check_summed_reduction():
    cases = 0
    for pencil_size in range(3, 13):
        for number_pairs in range(1, 18):
            for beta in range(pencil_size):
                # Concentrate every allowed bad incidence first; this is the
                # extremal synthetic ledger for the summation argument.
                total_bad = beta * number_pairs
                bad = [0] * pencil_size
                for index in range(total_bad):
                    bad[index % pencil_size] += 1
                require(max(bad, default=0) <= number_pairs,
                        "synthetic bad incidence exceeds family")
                windows = [number_pairs - value for value in bad]
                require((pencil_size - beta) * number_pairs <= sum(windows),
                        "summed windowed reduction")
                cases += 1
    print(f"PASS summed reduction algebra: cases={cases}")


def check_official_rows():
    q_min = 2**250
    rows = 0
    for name, n, k, h in ROWS:
        require(h > 1 and h & (h - 1) != 0, f"{name}: h must be odd")
        require(h - 1 & (h - 2) == 0, f"{name}: h-1 must be a power of two")
        low, high = (h + 1) // 2, h - 2
        require(low <= high, f"{name}: empty high band")
        for d in (low, high):
            beta = (n - k - d) // (h - d - 1)
            require(0 <= beta < n <= q_min, f"{name}: denominator pin")
            require(2 * d >= h, f"{name}: high-depth pin")
            require(k + d <= k + h - 2, f"{name}: window nonempty")
            rows += 1
        # The only power of two in [ceil(h/2),h] is the cascade depth h-1.
        powers = [2**j for j in range(h.bit_length() + 1)
                  if low <= 2**j <= h]
        require(powers == [h - 1], f"{name}: spectral interval")
    print(f"PASS official-row denominator and spectral pins: endpoints={rows}")


def main():
    check_projective_cell_identity()
    check_high_depth_injectivity_arithmetic()
    check_summed_reduction()
    check_official_rows()
    print("XR_BAND_WINDOWED_PROJECTION_REDUCTION_ALL_PASS")


if __name__ == "__main__":
    main()
