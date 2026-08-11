# Cycle 62: rate-half locator-extension kernel (2026-08-10)

## Missing linear layer

The deficiency-aware matrix `M_W` enforces the shortened apolarity condition
on `L_x(Y)Q_Y(x)`, but it does not separately enforce that the values
`Q_Y(x)` come from locator coefficient polynomials of `X`-degree at most
`rho`.

For `a=|W|`, put `sigma_W(X)=product_(x in W)(X-x)`. The exact missing rows
are

```text
sum_(x in W) x^i [Y^j]Q_Y(x)/sigma'_W(x)=0,
0<=i<a-rho-1,  0<=j<=m.
```

After substituting `Q_Y(x)=A_x(Y)R_x(Y)`, these form a linear matrix `E_W`
on the same deficiency-clone variables. Dual Reed-Solomon interpolation
proves that `E_W r=0` is equivalent to coefficientwise extension with
`X`-degree at most `rho`.

## New rank target

Every actual failure has a blockwise-nonzero kernel for

```text
C_W=vertical_stack(M_W,E_W).
```

The proved node `rate_half_bivariate_locator_extension_kernel_reduction`
adds this exact necessary layer. It preserves all ten genuine `m=1`
failures: `rank(M_W)=rank(C_W)=5<6`. The live rank problem is now `C_W`, not
`M_W`; no critical status changes.
