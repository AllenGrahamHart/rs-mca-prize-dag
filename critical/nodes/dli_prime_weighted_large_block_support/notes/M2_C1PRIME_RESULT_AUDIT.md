# M2 C1' result audit

- **status:** candidate route survived one preregistered round
- **verdict:** `C1_prime_SURVIVES_M2`
- **nonclaim:** C1', B-WEAK, and the DLI target remain unproved

The frozen level-scaled candidate uses `w_max(L)=L+5` and requires

```text
E-1 <= 4r(1+W_cl).
```

All twelve balanced full-half-section rows survived. The maximum exact ratio
was

```text
K' = 0.246909432... at L=1, q=7937,
```

below `4` by a factor greater than sixteen. This is the deliberately included
orbit-quantized accident row. The ledger is load-bearing: deleting `W_cl`
makes that same row violate the bound.

`verify_m2_c1prime_result.py` independently reconstructs `E` from the complete
M1 signed spectra, reconstructs `W_cl` from the M2 primitive counts, and checks
all inequalities as exact rational numbers. It also checks census consistency:
primitive counts never exceed complete-spectrum counts and agree below twice
the minimum nonzero relation weight, where decomposition is impossible.
Strict gaps at higher weights confirm that decomposable mass is actually
excluded rather than silently charged.

Under the pre-existing F-round rule, the candidate C1' route is now eligible
for proof work and later predicate wiring. M3 and M4 must still be completed
before any DLI route surgery is considered.
