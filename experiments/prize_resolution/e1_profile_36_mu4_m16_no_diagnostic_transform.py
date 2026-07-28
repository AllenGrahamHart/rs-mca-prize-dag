#!/usr/bin/env python3
"""Remove the non-proof long-double m16 norm diagnostic mechanically."""

from __future__ import annotations

from pathlib import Path
import sys


OLD = r'''                        const long double measured = log_norm(
                            support, singleton_signs[sign_mask],
                            heavy_support, heavy_signs
                        );
                        static const long double threshold =
                            logl(16.0L)
                            + logl(strtold(
                                "317494674775468773183020924238786383963", nullptr
                            ))
                            + 128.0L * logl(2.0L);
                        if (measured < threshold - 1e-9L) ++counts.screen_below;
                        else if (measured > threshold + 1e-9L) ++counts.screen_above;
                        else ++counts.screen_near;
'''


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text()
    assert text.count(OLD) == 1
    path.write_text(text.replace(OLD, "", 1))


if __name__ == "__main__":
    main()
