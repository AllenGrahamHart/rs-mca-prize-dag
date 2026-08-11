#!/usr/bin/env python3
"""Independent partition-profile audit of the dichotomy."""


def partitions(total, cap=None):
    if total == 0:
        yield ()
        return
    if cap is None or cap > total:
        cap = total
    for first in range(cap, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def max_score(parts, m):
    rho = 4 * m - 1
    T = 4 * m + 1
    N = 16 * m
    scores = [-1] * (rho + 1)
    scores[0] = 0
    for part in parts:
        updated = [-1] * (rho + 1)
        for used, score in enumerate(scores):
            if score < 0:
                continue
            for degree in range(rho - used + 1):
                value = score + min(T * degree, N * part)
                index = used + degree
                if value > updated[index]:
                    updated[index] = value
        scores = updated
    return max(scores)


def main():
    checked = 0
    for m in range(1, 11):
        need = (4 * m + 1) * (4 * m - 1) - (m - 1)
        threshold = -(-(3 * m + 1) // 4)
        survivors = []
        for parts in partitions(m):
            if max_score(parts, m) >= need:
                survivors.append(parts)
                assert max(parts) >= threshold
                if m >= 2:
                    assert parts != (1,) * m
                checked += 1
        assert survivors
        if m in (2, 3, 4):
            assert survivors == [(m,)]
    print(f"PASS endpoint factor-degree profile audit survivors={checked}")


if __name__ == "__main__":
    main()
