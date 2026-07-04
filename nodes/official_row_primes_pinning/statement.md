# official_row_primes_pinning

- **status:** TARGET
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/c1a_lowh_mitm_certificates.md']

## Statement

The repo pins only the SHAPE of the Row-C fields (log2 q = 250, 1024 | q - 1, idealized q = 2^250) — no literal primes anywhere (xr-budget-audit/ certificate dir absent). ALL per-row certification (C1a certificates, the C2 GCD harness) currently runs on a clearly-labeled STAND-IN prime p* = 1 mod 1024 (~250 bits); re-running on real primes = swapping one constant. NEEDED: the authoritative literal row primes (prize spec / maintainer / rules-freeze artifact) before any certification claim is made about OFFICIAL rows. Goes on the maintainer asks list.
