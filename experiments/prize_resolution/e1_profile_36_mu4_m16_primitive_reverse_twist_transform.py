#!/usr/bin/env python3
"""Quotient primitive reverse-audit signs by F(X) -> F(-X)."""

from __future__ import annotations

from pathlib import Path
import sys


SETUP_MARKER = "    const uint64_t even_mask = all_lags ^ parity_mask;"
SETUP_REPLACEMENT = r'''    const uint64_t even_mask = all_lags ^ parity_mask;
    const auto first_odd_singleton = std::find_if(
        support.begin(), support.end(),
        [](int position) { return position % 2 != 0; }
    );
    if (first_odd_singleton == support.end()) std::exit(40);
    const int twist_index = static_cast<int>(first_odd_singleton - support.begin());'''
SIGN_MARKER = r'''    for (int sign_code = 31; sign_code >= 0; --sign_code) {
        ++counts.sign_assignments;
'''
SIGN_REPLACEMENT = r'''    for (int sign_code = 31; sign_code >= 0; --sign_code) {
        if (audit_signs[sign_code][twist_index] < 0) continue;
        ++counts.sign_assignments;
'''


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text()
    assert text.count(SETUP_MARKER) == 1 and text.count(SIGN_MARKER) == 1
    text = text.replace(SETUP_MARKER, SETUP_REPLACEMENT, 1)
    text = text.replace(SIGN_MARKER, SIGN_REPLACEMENT, 1)
    path.write_text(text)


if __name__ == "__main__":
    main()
