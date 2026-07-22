# M4/H3 two-Schur CP-SAT pilot

- **status:** INCOMPLETE; no solver status and no mathematical evidence
- **script:** `l1_m4_h3_two_schur_cpsat_modal.py`
- **analogue:** `(n,p,m,h)=(128,31,4,3)` over `F_(31^4)`
- **resources:** one Modal container, two CPUs, 2 GiB RAM, 60-second
  function cap, intended 45-second CP-SAT cap

## Run ledger

```text
ap-31urbcd0fvVu1adNueXzSz  MODEL_INVALID; zero search branches
ap-cwwCYjpZqT2nwd3vKu4XD6 MODEL_INVALID; AddModuloEquality input was not affine
ap-m2tOKpIdLfCZOzoRUmRkyQ FUNCTION_TIMEOUT at 60 seconds; no solver status
```

The first repair added `CpModel.Validate()`, which exposed that OR-Tools does
not accept a many-variable linear expression directly as the modulo target.
The second repair introduced bounded auxiliary sum variables and validated
the resulting model before search. The repaired run reached the hard Modal
function timeout before returning `FEASIBLE`, `INFEASIBLE`, or `UNKNOWN`.
Startup, finite-field coefficient generation, model construction, and search
shared the same 60-second budget, so the intended 45-second solver budget was
not observed externally.

The model encodes 128 four-color variables with color multiplicities
`(35,31,31,31)`. It expands the Fourier equations for both the colored word
and its coefficientwise square at exponents 1 through 30 into 240 linear
congruences modulo 31. A feasible assignment would be replayed independently
over `F_(31^4)` before emission. None was emitted, and timeout is not evidence
for either existence or emptiness.

Any future run should precompute and hash the Fourier coefficient table, or
measure model-build time separately before choosing a function cap. It must
publish the validated model fingerprint, build time, actual solver wall time,
solver status, branch/conflict counts, and all four color classes for an
independently replayable feasible witness.
