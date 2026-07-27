# E=50 geometry falsification report

Date: 2026-07-27.

## Claim attacked

The tempting continuation of the low-slack proof was:

```text
Every full-conductor profile-(3,4,0) support with E=50 has L<=27.
```

This claim is false.

## Bounded campaign

Modal run `ap-XfP3XD3lCoE4sCUmTfC3PA` launched 16 deterministic
single-CPU workers with a 52-second internal deadline and partial-result
semantics. Every worker found a full-conductor `E=50,L=28` vector;
the slowest reported hit took 0.064 seconds. One representative is

```text
(48,-2),(51,-2),(67,-1),(81,2),(83,1),(84,-1),(111,1).
```

Its exact chord ledger is

```text
conductor gcd = 1,
E = 50,
V = 100,
L = 28,
D_64 = 0,
C = -26.
```

Thus the relaxed `L<=28` ceiling is geometrically attained; no proof may
replace it by `L<=27` without an additional hypothesis.

## Exact norm probe

Modal run `ap-Aq7Pqe17R47TNQMFyu1oT2` evaluated the representative with
python-flint:

```text
central moments M_2,...,M_6 = 100,600,24068,300470,7787140,
sampled conjugate-square range = [1.0155604732,37.6476121571],
norm bits = 233,
v_2(norm) = 1,
odd part mod 256 = 1,
odd part composite.
```

The norm computation is exploratory and not load-bearing. It indicates that
the failed geometry shortcut does not threaten the desired exclusion: the
actual norm is far below `2^250`, and a sharper logarithmic majorant is the
appropriate replacement route.

## Ruling

The geometry-only endpoint shortcut is REFUTED. The proved replacement is the
optimized quadratic majorant in the parent proof, which excludes `V=100`
without asserting `L<=27`.
