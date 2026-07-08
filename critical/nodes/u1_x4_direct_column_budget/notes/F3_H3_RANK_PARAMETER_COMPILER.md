# F3 h=3 rank-form parameter compiler

Status: CONDITIONAL ARITHMETIC COMPILER, NOT `RC-RANK` AND NOT `H3-ACT`.

This packet records what the current h=3 rich-curve Stepanov arithmetic gives
once the remaining rank-form nonvanishing theorem is granted.  It is a T3
constants/parameter step for the T1 route, not a promotion packet.

## Pre-registration

Question:

```text
Assuming RC-RED(13) and rank-form nonvanishing, what explicit bounds do the
current diagonal Stepanov boxes produce for representative family sizes |Z|?
```

Success criterion:

- use only exact integer inequalities;
- verify `LS3` and the necessary image-cap inequality for each parameter row;
- print the conditional bound `sum_z T(z) <= |Z| L(A,B,n)/D`;
- keep the missing geometry explicit: this does not identify the actual F3
  batching or prove `RC-RANK`.

Failure criterion:

- a row is printed without satisfying the coefficient and image-cap checks;
- the note treats the conditional curve-family bound as `H3-ACT(C)`;
- the verifier performs a heavy local search.

## Compiler

For a family `Z` of repaired degree-2 signature curves, the reduced-condition
compiler gives

```text
conditions = 13 D (A + D) |Z|,
coeffs     = A B^3,
L          = (A - 1) + 6 n (B - 1).
```

Under rank-form nonvanishing, an auxiliary exists and is nonzero if the
conditions are fewer than the available coefficients and rank image.  The
resulting degree contradiction gives

```text
sum_{z in Z} T(z) < |Z| L / D.
```

The replay searches the diagonal subfamily `A=D`, with conservative caps that
ensure both

```text
13 D (A + D) |Z| < A B^3
13 D (A + D) |Z| < |Z| (L + 1).
```

This is not globally optimized, but it is exact and light.

## Representative Output

The replayed table includes:

```text
n=2^13, |Z|=1:      bound=6807         < n
n=2^23, |Z|=64:     bound=65729374     about 7.84 n
n=2^32, |Z|=128:    bound=6380025160   about 1.49 n
n=2^41, |Z|=256:    bound=619017527995 about 0.282 n
n=2^41, |Z|=512:    bound=1422138529491 about 0.647 n
```

Interpretation: if the actual F3 geometry supplies `RC-RANK` and batches the
curve family at these representative `|Z|` scales, the arithmetic has real
slack at high official rows.  Lower rows or larger batches still need better
constants, a level-set/batching argument, or certificates.  This is exactly
the remaining T1/T3 interface; it is not yet `H3-ACT(C)`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_parameter_compiler.py
```

Expected digest:

```text
H3_RANK_PARAMETER_COMPILER_PASS
```
