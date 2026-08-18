#!/usr/bin/env python3
"""Tamper replay for the primitive Haar-event identity."""

from verify import main


if __name__ == "__main__":
    import sys

    sys.argv.append("--tamper-selftest")
    main()
