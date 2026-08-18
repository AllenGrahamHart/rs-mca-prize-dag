# Audit

- The even moments start at `r=1`, so they remove the top `L`
  interpolation coefficients but do not force `A(0)=0`.
- The odd moments start at `r=0`, so they force `W(0)=0` and remove only
  `L-1` top coefficients. This one-degree asymmetry is load-bearing.
- `W(y_i)` includes the half-character factor `x_i`; omitting it would give
  the wrong Pell equation.
- The congruences are modulo the squarefree polynomial `Y^h-1`. Exact order
  `h` and odd characteristic ensure distinct roots and invertible Fourier
  interpolation.
- `(SP3)` plus the degree caps is sufficient for the converse. No unprinted
  sign or support condition is required.
- The quotient degree in `(SP4)` is asserted only for `L<=h/2`. Above that
  threshold the divisible numerator has degree below `h` and is identically
  zero.
