# Proof

The proved inversion transport has seven assignment orbits and two target
root orbits for each allocation. The canonical `F00/F01` and `M00` assignment
orbits account for twelve represented orbits. Choosing `F02,F04,F06,M01,M03`
from the other five assignment orbits gives the disjoint product `(KBDR-1)`.

For every representative, the compiler independently reconstructs the source
form by a generic `5 x 5 solve_right`. At each of `c,d`, division by the
forced `(W-1/c)^2` factor gives a degree-two residual. If
`R(W)=R_0+R_1W+R_2W^2` and the monic target is
`Q(W)=Q_0+Q_1W+W^2`, projective equality is exactly

```text
R_0-R_2 Q_0=0,       R_1-R_2 Q_1=0.              (1)
```

Applying `(1)` at both endpoints produces four equations. The compiler
clears each rational denominator, normalizes the numerator primitively, and
records exact degree, term-count, and SHA-256 fingerprints. It computes the
gcd of the four normalized equations and factors every nonmonomial
reconstruction and line denominator into the recorded radical set. The
ambient torus units and the squarefree locator condition `c-d!=0` belong to
the inherited chart contract rather than this denominator-generated list.

The exact Modal run visits all `5*2*3=30` keys, emits 120 nonzero equation
records, finds common gcd one in every cell, and reports the aggregate values
in `(KBDR-2)`. The output is a complete deterministic image of the compiler.
QED.
