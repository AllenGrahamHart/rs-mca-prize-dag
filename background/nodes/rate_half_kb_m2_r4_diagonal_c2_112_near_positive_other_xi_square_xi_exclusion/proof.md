# Proof

Use the parent positive fixed-moving reconstruction with `xi=b`. For a
residual `A W^2+B W+C`, the square condition at target `kappa` is

```text
C-kappa^2 A=0,        B+2 kappa A=0.               (1)
```

Apply `(1)` with `kappa=1/b` over `c` and `kappa=1/d` over `d`.
After removing the finite-incidence factor `H^2`, the first product
condition splits into two bidegree-`(2,3,2)` branches in `(b,c,d)`;
the second splits into two bidegree-`(1,3,3)` branches.

For each selected `d`-line, solve its full linear equation for `b(c,d)`.
The three substituted polynomials share exactly

```text
(c-1)^e (cd-1)(5cd-4c-4d+5),       e=2 or 1.       (2)
```

All factors in `(2)` are inadmissible. Divide them out. Projecting the
selected `c`-branch against each middle condition gives the following two
nonzero resultant degrees and squarefree support:

```text
pair  degrees       squarefree support beyond scalars
00    (155,127)     (d-2)(d-1)(d+1)(2d-1)(17d^2-38d+17)
01    (155,127)     (d-2)(d-1)(d+1)(d+2)(2d-1)(2d+1)(2d^2-9d+1)
10    (174,144)     (d-2)(d-1)(d+1)(2d-1)(2d+1)(17d^2-38d+17)
11    (174,144)     (d-2)(d-1)(d+1)(d+2)(2d-1)(2d+1)(2d^2-3d-1).
```

The generic extra fibers have reduced bases

```text
01: c+2d-9=0,  2d^2-9d+1=0,      b=1/2, cd=1;
10: 13c^2+12c-28=0, 2d+1=0,      b=1/2;
11: c-2d+3=0,  2d^2-3d-1=0,      b=1/2, cd=1.
```

On the first `d`-branch the full leading-zero ideal is

```text
b-1/2=0,  7c+17d-30=0,  17d^2-38d+17=0.
```

On the second `d`-branch, the full leading-zero ideals at `d=-2,-1/2` are
units. Their generic copies are saturated by the line coefficient: five of
the six overlap fibers across all branch pairs are units, while pair `01`
at `d=-1/2` has `c=14/13` and forces `b=1/2`. Thus every retained point is
forbidden.

The primary reconstructs by direct matrix inversion and uses resultants.
The independent audit reconstructs by fraction-free
`DomainMatrix.solve_den` and obtains the same two projections as terminal
subresultants. Both independently replay the exceptional and candidate
Groebner bases. Clearing denominators and repeating all gcd and basis checks
modulo `2130706433` gives identical support. Resultants and subresultants
are used only in their necessary direction, and the complete leading-zero
ideals are checked separately. QED.
