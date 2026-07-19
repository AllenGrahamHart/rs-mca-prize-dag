# Claim contract - PMA sigma-one B11 scope

## Proves

1. The exact finite thresholds `(E,V_2,V_R)=(0,2,0)`.
2. The exact collapse `J union A2 union GROW`, with `AR=RES=empty`.
3. The exact paid-certificate formula and its field-size fit ceiling.
4. Failure of that certificate to fit `n^6` uniformly at rates `1/8` and
   `1/16`, even before any competing primitive payment is restored.

## Does not prove

- a lower bound on the realized B11 cells;
- a counterexample to PMA or `imgfib`;
- a payment for `GROW`;
- a finite mixed-branch allowance not already supplied by a consumer;
- the growing-`ell` asymptotic-reserve residual theorem.

## Consumer effect

The `sigma=1` finite branch no longer owes a threshold search or a `RES`
theorem. It owes a sharper source-coupled payment for `d<=2` and a payment for
`GROW={d>=3}`. The asymptotic branch still uses the general B11 router and
owes `GROW union RES`.
