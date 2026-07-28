#!/usr/bin/env python3
"""Quotient primitive m16 signs by the free F(X) -> F(-X) involution."""

from __future__ import annotations

from pathlib import Path
import sys


OUTER_MARKER = "    for (size_t first_index = 0; first_index < allowed.size(); ++first_index) {"
OUTER_INSERT = r'''    const auto first_odd_singleton = std::find_if(
        support.begin(), support.end(),
        [](int position) { return position % 2 != 0; }
    );
    if (first_odd_singleton == support.end()) std::exit(40);
    const int twist_index = static_cast<int>(first_odd_singleton - support.begin());

'''
SIGN_MARKER = r'''                for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
                    ++counts.distance_tests;
'''
SIGN_REPLACEMENT = r'''                for (int sign_mask = 0; sign_mask < 32; ++sign_mask) {
                    if (singleton_signs[sign_mask][twist_index] < 0) continue;
                    ++counts.distance_tests;
'''


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text()
    assert text.count(OUTER_MARKER) == 1
    assert text.count(SIGN_MARKER) == 1
    text = text.replace(OUTER_MARKER, OUTER_INSERT + OUTER_MARKER, 1)
    text = text.replace(SIGN_MARKER, SIGN_REPLACEMENT, 1)
    path.write_text(text)


if __name__ == "__main__":
    main()
