#!/usr/bin/env python3
"""Tiny model of injective mapping from extras to kernel locator points."""

from __future__ import annotations


def main() -> None:
    extras = [
        frozenset({1, 3}),
        frozenset({2, 5}),
        frozenset({4, 6}),
    ]
    kernel_points = {
        frozenset({1, 3}),
        frozenset({2, 5}),
        frozenset({4, 6}),
        frozenset({7, 8}),
    }

    image = []
    for locator in extras:
        assert locator in kernel_points
        image.append(locator)

    assert len(image) == len(set(image))
    assert len(extras) <= len(kernel_points)

    print(
        "petal realizable-kernel injection check passed:",
        {"extras": len(extras), "kernel_points": len(kernel_points)},
    )


if __name__ == "__main__":
    main()
