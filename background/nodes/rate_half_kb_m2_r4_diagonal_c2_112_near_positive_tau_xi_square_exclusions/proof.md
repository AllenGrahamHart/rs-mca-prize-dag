# Proof

Use the parent positive fixed-moving reconstruction. The direct checker
verifies its exact determinant and both forced roots. For either target root
assignment in `(KBNTS-1)`, each constant-to-leading condition splits as the
finite-incidence factor `H^2` times two lines in `b`.

On the generic part of a selected left line, solve its full linear equation
for `b(c,d)` and substitute in both middle conditions. For the direct
allocation the four pairs have resultant degrees/gcd degrees

```text
(0,0): (24,51)/24,  (0,1): (24,51)/20,
(1,0): (30,51)/18,  (1,1): (30,51)/18.
```

Their squarefree gcd support is `(KBNTS-2)`. The swapped allocation has

```text
(0,0): (16,34)/16,  (0,1): (18,42)/16,
(1,0): (24,34)/12,  (1,1): (28,42)/14,
```

again with only forbidden support; the `(1,0)` support merely omits `d=1/2`.

No left line is divided out globally. Imposing its full coefficient and
constant simultaneously gives `(KBNTS-3)` in the direct allocation, and
both points reduce the `z=1` factor to zero. The opposite-variable audit
also exposes `c=-2`, but direct fiber gcd gives `(d-2)(2d-1)`. For the
swapped allocation, the first exceptional basis reduces the same `z=1`
factor to zero and the second exceptional support is forbidden.

The primary uses a direct solve and resultants in `c`. The independent audit
uses `DomainMatrix.solve_den`, verifies the fraction-free source identity,
uses Bezout denominators over `QQ(d)[c]`, and eliminates exceptional loci in
`d`. Both clear denominators and reproduce all squarefree supports modulo
`2130706433`. Resultants are used only in their necessary direction, so no
leading specialization is discarded. In particular, the reciprocal-`xi`
swapped `(1,0)` factor is `(d-2)(d-1)(d+1)`, not the fixed-`xi` factor
`(d-1)(d+1)(2d-1)`; both independent paths enforce this distinction. Every
retained root is forbidden. QED.
