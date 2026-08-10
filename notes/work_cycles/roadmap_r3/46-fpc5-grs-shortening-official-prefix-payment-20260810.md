### 2026-08-10 FPC5 GRS shortening official-prefix payment

The support-shortening cap was replayed on every exact `(PF6)` cell at
`n=8192` and compiled through canonical first-layout ownership. The complete
rate-`1/8` prefix `M=29..32` has 126 cells and total cap

```text
195112047344632914122867933361797765038,
```

so it is paid on a nonempty 256-bit field slice. The complete rate-`1/16`
prefix `M=57..67` has 374 cells and total cap

```text
2444555448501019158442942184801171570,
```

so it is paid from a 249-bit threshold. This closes every `M=61,t=3` cell,
including the 37 cells outside the shifted-Johnson strip.

The exact negative controls are equally important: this compiler exceeds the
strict budget at rate-half `M=5`, rate-quarter `M=13`, rate-`1/8` `M=33`,
and rate-`1/16` `M=68`. The critical target remains open, but its smallest-row
frontier now begins at `M=5,13,33,68` on the relevant upper field slices.
