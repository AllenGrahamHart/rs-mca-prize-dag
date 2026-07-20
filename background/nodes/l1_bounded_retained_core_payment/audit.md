# Audit - L1 bounded retained-core payment

## Checked axes

1. The count chooses the retained core `C\D`, not the large missed core `D`.
2. Numerator uniqueness uses the strict inequality `h>d`.
3. Maximality `b<ell` is what makes the threshold inequality strict.
4. Exactness guards can only reduce the ambient count.
5. The bound is per source chart and does not hide a chart multiplier.
6. The sub-Johnson identity retains the background gap `g=ell-b`.

## Remaining attack

The bounded-polarity sub-Johnson tail now has both `e` and retained-core size
`a=N-d` unbounded, with `a(N-a)>=Ng`. It still needs a structured split-pencil
owner or a higher-order incidence theorem.
