# E33 profile-(1,8) route report, 2026-07-27

The abstract nested-layer cap is 2082, above the exact cubic cutoff 1732.
A complete bare mod-16 allocation census (`ap-RXcPh5MEDnYZbFoGdvCt4b`)
returns maximum 1936 in both quotient orders, so that route is retired.

Expanding the weighted support as `2*1_B+1_U` and retaining the coupling among
the cubic terms improves the exact allocation maxima to 2028 at order 128
and 1740 after division at order 64 (`ap-ghmCP8Hfnqd6pOZLcdtYJ0`). The
divided chamber misses by only eight, but the full-conductor chamber remains
far above threshold. These are upper-bound obstructions, not autocorrelation
vectors.

The decisive information is the one-odd light-chord parity geometry. An
initial classification into six light-support orbits was rejected by the
independent checker, whose first omitted support was `{0,1,63,64}`. The error
was the false identification of the two reflection families. The corrected
classification has eleven orbits: five in each reflection family and one
quarter-octant orbit. A 1/128 six-template
pilot (`ap-yyKFoUbY8pmty9ckWBjB2s`) found actual maxima at most 1200 and cost
under one aggregate worker-second but is not theorem evidence. The repaired
88-cell campaign `ap-TbM5Ao0mujKzSnl3E7cFL5` exhausts 218,327,296 normalized
vectors and gives exact maximum 1356 over 17,144 profile vectors. This closes
the branch with a 376-unit margin below the cubic boundary.
