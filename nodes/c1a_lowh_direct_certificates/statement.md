# c1a_lowh_direct_certificates

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/a_pilot_wh_torsion_data.md']

## Statement

At h = 4 (and plausibly 5): the per-row trade search at n = 1024 is FEASIBLE by MITM — pattern space C(1024, 8) ~ 2^55, halves ~ 2^{35} hash entries. Certify the official Row-C primes directly: no non-toral h=4 trades at (p, zeta). Pure compute; the exact analogue of the banked toy MITM machinery scaled up. Covers the window's most exposed sizes (the smallest h dominate risk). DELIVERED (27-check verifier green; 13/13 fast-mode replayed): (1) EXACT COMPLETE census over REAL finite fields at n = 16/32/64/128/256 — zero non-toral h=4 trades, toral exactly C(n/4,2) at every scale (extends the pilot's char-0 emptiness to actual F_p, two octaves further); (2) a decisive DETECTION gate: at the exceptional prime F17 the pipeline finds all 120 genuine non-toral 4-trades — sensitivity proved, and it caught+fixed a sign-convention bug that would have silently blinded the fast path; (3) n = 1024: machinery validated, toral family certified (32640), exhaustive spot-slice clean; the FULL run honestly deferred (~18h and ~16GB unbucketed; e_1-bucketing fits 2GB) — unconditional n=1024 closure rests on the A3+X24 route with C1a as corroborating harness, or a future bucketed long run; (4) h = 5 measured INFEASIBLE (~2.2yr) — the descent (C1b) must carry h >= 5. CONDITIONAL on: stand-in prime (see official_row_primes_pinning).

## Attack surface

the F2/E37 MITM machinery at n = 1024 with disk-backed hashing if needed; SOLO

## Falsifier

a real trade found at an official prime (then absorbency counts it — budget ~1e5 per h)
