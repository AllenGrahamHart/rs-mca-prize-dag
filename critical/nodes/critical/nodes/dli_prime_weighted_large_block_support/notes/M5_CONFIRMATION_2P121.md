# M5 confirmation — dli endpoint (catch #40)

Ratified by the maintainer in-session, 2026-07-13 ("For now I will ratify
the correction"). This settles catch #40: the earlier 2^122 displays were
a complement-duality double-count (catch #30) that failed to compose under
the prize's n^3 central-band budget; the corrected two-sided split forces
the half-band endpoint to 2^121, which the decomposition clears with ~20
bits of slack (baseline (41/8)^34 ~ 2^80.16 of a 100-bit budget, plus the
21-bit joint reserve). The verifier below greps the required line verbatim.

MAINTAINER CONFIRMATION (M5, catch #40): the operative endpoint of CONJECTURE B-WEAK and of every dli route document is 2^121 (joint reserve 21 bits); the 2^122 displays are superseded.
