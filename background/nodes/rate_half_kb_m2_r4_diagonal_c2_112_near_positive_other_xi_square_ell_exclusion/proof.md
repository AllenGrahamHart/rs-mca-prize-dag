# Proof

Use the parent positive fixed-moving reconstruction with `xi=b`. For a
residual `A W^2+B W+C`, impose the square condition at `1/d` over `c` and at
`1/b` over `d`. After removing the finite-incidence factor `H^2`, the first
product condition has two linear `b`-branches and the second has two
quadratic `b`-branches.

For each selected `c`-line, solve its full equation for `b(c,d)`. The three
substituted equations share exactly

```text
(c-1)^2(cd-1)(5cd-4c-4d+5)             for d-branch 0,
(c-1)(c+1)(cd-1)(5cd-4c-4d+5)          for d-branch 1.       (1)
```

These are forbidden finite-chart components. Divide them out. Eliminating
`c` from the selected `d`-branch and each middle condition gives

```text
pair  degrees       squarefree support beyond scalars
00    (127,155)     (d-2)(d-1)(d+1)(2d-1)(2d+1)
                    (17d^2-38d+17)(11d^3-21d^2-3d+5)
01    (127,155)     (d-2)(d-1)(d+1)(2d-1)
                    (5d^2-8d+5)(17d^2-38d+17)
10    (127,155)     (d-2)(d-1)(d+1)(2d-1)
                    (2d^2-3d-1)(11d^2-20d+5)
11    (127,155)     (d-2)(d-1)(d+1)(2d-1)(2d+1)
                    (2d^2-9d+1)(5d^2-8d+5).
```

Saturated lexicographic bases classify every nonstandard factor. The two
`q17` generic ideals are units. The cubic and `q11` bases contain `c-1`;
both `q5` bases contain `c+1`. The `2d+1` fibers in pairs `00` and `11`,
the `2d^2-3d-1` fiber in pair `10`, and the `2d^2-9d+1` fiber in pair `11`
all reduce `b-1/2` to zero.

The selected `c`-line can degenerate only over

```text
(d-2)^3(d-1)^5(d+1)^5(2d-1)^3(17d^2-38d+17)
```

for its first branch, or the same standard support with exponent seven at
`d=1` and without `q17` for its second branch. On `q17`, the full unsolved
ideal has basis

```text
b-1/2,  7c+17d-30,  17d^2-38d+17.
```

Thus every generic or leading-zero point is forbidden. The primary uses
direct matrix inversion and resultants. The audit uses
`DomainMatrix.solve_den` and terminal subresultants. Both independently
repeat the support and candidate-basis checks after exact reduction modulo
`2130706433`. Resultants are used only in their necessary direction, and no
line is divided out on its leading-zero locus. QED.
