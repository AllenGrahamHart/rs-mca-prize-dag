#!/usr/bin/env python3
"""Tamper replay for the first-junction support-overlap verifier."""

from verify import main


if __name__ == "__main__":
    import sys

    sys.argv.append("--tamper-selftest")
    main()
